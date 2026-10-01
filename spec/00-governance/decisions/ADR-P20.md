---
id: ADR-P20
type: adr
title: Event Consumer Retry and Dead-Letter Policy
status: APPROVED
wave: Phase 3.8 (18-analysis-design, stage 4)
deciders: project owner (chose "5 retries then DLQ", 2026-10-01)
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
- FIT-11
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
| Retries | 5 attempts in the consumer, exponential backoff with ±20 % jitter: about 1, 2, 4, 8 and 16 s (≈ 31 s worst case). The inbox makes every retry safe. |
| Dead-letter topic | `{cell}.<domain>.events.dlq`, one per consumed domain topic. The record keeps the original message unchanged and adds: consumer name, failure class, error code, attempt count, first and last failure time and `trace_id`. Retention is at least that of the source topic (set in `22-deployment-design.md`). |
| Per-aggregate order | When a message is dead-lettered, its key (`tenant_id + aggregate.id`) is **parked** for that consumer. Later events with a parked key go to the consumer's parking store and are not applied. Other keys in the partition continue. |
| Infrastructure outage | When transient failures exceed a threshold across messages, the consumer **pauses** (stops polling, reports not-ready) instead of dead-lettering, and resumes when its dependencies are healthy. This is a circuit breaker on the consumer. The threshold is a configuration value: proposed 50 % of the messages in 1 min, **[Derived]**. |
| Alerting | Any message in a DLQ raises a P2 alert for the owning unit. Metrics: `consumer.dlq_total{consumer,class}`, `consumer.parked_keys{consumer}`, `consumer.paused{consumer}`. |
| Replay | An audited operator action (role PLT-OPS) re-delivers a dead-lettered message, then the parked messages of that key in order, to the same consumer. The inbox prevents double application. A message that cannot be fixed is **discarded by an audited decision**, which also releases the parked key. Discarding is never automatic. |
| Scope | Applies to every Kafka consumer: process handlers, projection builders (DU-09), the audit ingest (DU-03) and the evaluators (DU-07). Outbox relays keep retrying until success: they hold no consumer state and order is preserved at the source (ADR-P02). Projection builders may instead rebuild a projection from its owner (FIT-11). |

## Consequences
### Positive
- A poison message affects one aggregate for one consumer, not a partition.
- Order per aggregate is preserved by parking instead of skipping.
- Every non-applied message is visible, alerted and replayable.

### Negative
- Each consumer needs a parking store (a table next to its `inbox`, keyed `(tenant_id, consumer, aggregate_key)`). This is an addition to the logical model, to be carried into `16-database-schema.md`.
- In-consumer retries can hold a partition for up to about 31 s. That budget is longer than the ≤ 5 s evaluation path of DU-07. DU-07 relies on enough partitions and on the infrastructure-outage pause, and its latency is watched by its own metric.
- Operators need a replay tool, and P2 alerts need an owner on call.

### Risks and mitigations
- **Risk:** a fault in a handler sends many messages to the DLQ at once. **Mitigation:** a DLQ-rate alert, the pause rule, and bulk replay by key range after the fix.

## Related Decisions
- ADR-P02: transactional outbox and inbox.
- ADR-P17: process handlers re-enter the command pipeline.
- `18-analysis-design/23-crosscutting.md` §6 applies this decision.
