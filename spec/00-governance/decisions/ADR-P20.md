---
id: ADR-P20
type: adr
title: Event Consumer Retry and Dead-Letter Policy
status: APPROVED
wave: Phase 3.8 (18-analysis-design, stage 4)
deciders: project owner (chose "5 retries then DLQ", 2026-10-01); details amended after the independent review the same day, within the chosen option
approved_by: project owner
approved_at: '2026-10-01'
blocked_by: []
depends_on:
- ADR-P02
- ADR-P17
related:
- REQ-FND-013
- FIT-11
verified_by:
- "[Missing] — acceptance and chaos tests for retry, dead-letter, parking and pause (24-testing-strategy.md); FIT-11 covers only the projection-rebuild alternative"
---

# ADR-P20: Event Consumer Retry and Dead-Letter Policy

## Context and Problem
Events are delivered at least once through the outbox, and every consumer de-duplicates with its `inbox` table in the same transaction as its effect (ADR-P02, `06-data/logical-model/slc-01.md`). The partition key is `tenant_id + aggregate.id`, so the events of one aggregate are ordered (`18-analysis-design/15-event-design.md` §3). The only ratified text on delivery failure is the notification row of `09-reliability/fmea-slc03.md` ("prevention: outbox; retry", "mitigation_recovery: deliver on recovery"). No source gives a retry count, a backoff, a poison-message rule or a dead-letter queue (`15-event-design.md` §5, source gap). An unbounded retry blocks every aggregate that shares the partition behind one poison message. Dropping the message silently breaks the C-SYS rule that a failed automatic transition is recorded and alerted, never lost (`05-user-stories/00-guide.md`).

## Decision Drivers
1. One poison message must not stall unrelated aggregates.
2. Per-aggregate order must hold: no later event of an aggregate is applied while an earlier one is unresolved.
3. Nothing is lost silently: every message that is not applied is visible, alerted and replayable.
4. An infrastructure outage must not flood the dead-letter queue.

## Considered Options
1. **5 retries, then a dead-letter queue**, with later events of the same aggregate parked.
2. **Retry forever, no DLQ**: block the partition until the fault is fixed.

## Decision Outcome
The project owner chose **option 1**.

| Element | Rule |
|---|---|
| Failure classes | **Transient** (database, PDP, another context's OHS or object storage unavailable; timeout): retried. **Message-specific** (payload fails the event schema, unknown `event_version`, or the handler fails on this message after the retries): sent to the DLQ. **Domain rejection** of the command the handler issues (for example a state that already moved on) is a normal outcome: recorded in the audit log with `outcome: rejected` and alerted under C-SYS. It is not retried and not dead-lettered. |
| Retries | Up to 5 retries after the first attempt (6 tries in total), exponential backoff with ±20 % jitter: about 1, 2, 4, 8 and 16 s between tries (≈ 31 s worst case). The inbox makes every retry safe. |
| Dead-letter topic | `{cell}.<domain>.events.dlq`, one per consumed domain topic. The record keeps the original message unchanged and adds: consumer name, failure class, error code, attempt count, first and last failure time and `trace_id`. Retention is set in `22-deployment-design.md` and must outlast the alert-to-replay time (proposed ≥ 30 days). Payloads stay encrypted with the tenant's keys, so crypto-shredding and erasure reach DLQ and parking copies too (`key-hierarchy-and-disposition.md`). |
| Per-aggregate order | When a message is dead-lettered, its key (`tenant_id + aggregate.id`) is **parked** for that consumer. Later events with a parked key go to the consumer's parking store and are not applied. Other keys in the partition continue. |
| Infrastructure outage | When transient failures exceed a threshold across messages, the consumer **pauses** (stops polling, reports not-ready) instead of dead-lettering, and resumes when its dependencies are healthy. This is a circuit breaker on the consumer. The threshold is a configuration value: proposed 50 % of the messages in 1 min, **[Derived]**. |
| Alerting | Any message in a DLQ raises an alert for the owning unit: **P1** for consumers on a critical-tier path (the evaluators in DU-07, the audit ingest in DU-03, `dr-and-continuity.md`), **P2** otherwise. Metrics: `consumer.dlq_total{consumer,class}`, `consumer.parked_keys{consumer}`, `consumer.paused{consumer}`. |
| Replay | An audited operator action (role PLT-OPS) re-delivers a dead-lettered message, then the parked messages of that key in order, to the same consumer. The inbox prevents double application. The operator sees **metadata only** (event_id, consumer, failure class, error code, times), never the tenant payload (TB-09). A message that cannot be fixed is **discarded by an audited decision that needs a tenant role** (the owning context's administrator or the Security Officer) in addition to the operator. Discarding releases the parked key and is never automatic. |
| Scope | Applies to every Kafka consumer of a domain topic: process handlers, projection builders (DU-09), the audit ingest (DU-03), the evaluators (DU-07) and the Kafka consumption of adapters. It does not cover adapters pulling from external systems; those use quarantine and `DEGRADED` (`20-integration-design.md`). Outbox relays keep retrying until success: they hold no consumer state and order is preserved at the source (ADR-P02). Projection builders may instead rebuild a projection from its owner (FIT-11). |
| Exception: `{cell}.security.versions` | Consumers of the security-version topic (the Valkey replica, PEP caches) **never park and never dead-letter**. A message they cannot apply marks the subject's cached version stale, so the PEP rebuilds it from BC01 or denies (fail closed, REQ-FND-013); the consumer keeps going. Parking a subject would leave a revocation unapplied and break QAS-SEC-003 ("effective on next request in every path"). |

## Consequences
### Positive
- A poison message affects one aggregate for one consumer, not a partition.
- Order per aggregate is preserved by parking instead of skipping.
- Every non-applied message is visible, alerted and replayable.

### Negative
- Each consumer needs a parking store (a table next to its `inbox`, keyed `(tenant_id, consumer, aggregate_key)`). This is an addition to the logical model, to be carried into `16-database-schema.md`.
- In-consumer retries can hold a partition for up to about 31 s. That budget is longer than the ≤ 5 s evaluation path of DU-07. DU-07 relies on enough partitions and on the infrastructure-outage pause, and its latency is watched by its own metric.
- Operators need a replay tool that shows metadata only, and alerts (P1 on critical-tier consumers) need an owner on call.
- A discard needs a tenant role as well as the operator, so an unrecoverable message waits for the tenant's decision.

### Risks and mitigations
- **Risk:** a fault in a handler sends many messages to the DLQ at once. **Mitigation:** a DLQ-rate alert, the pause rule, and bulk replay by key range after the fix.

## Related Decisions
- ADR-P02: transactional outbox and inbox.
- ADR-P17: process handlers re-enter the command pipeline.
- `18-analysis-design/23-crosscutting.md` §6 applies this decision.
