---
id: ADR-P17
type: adr
title: Internal Service Architecture (Hexagonal / Ports & Adapters)
status: APPROVED_DELEGATED
wave: Phase 3.8 (18-analysis-design)
deciders: project owner (chose the style, 2026-09-30) + Claude (acting decision owner, delegated)
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-30'
blocked_by: []
depends_on:
- ADR-P02
- ADR-P04
- ADR-P05
- ADR-P06
- ADR-P11
- ADR-P13
related:
- ADR-P18
verified_by:
- FIT-01
- FIT-02
- FIT-03
- FIT-04
- FIT-10
- FIT-16
- FIT-20
---

# ADR-P17: Internal Service Architecture (Hexagonal / Ports & Adapters)

## Context and Problem
The ratified design fixes *what* the platform is — 8 bounded contexts, 89 aggregates with complete state × command matrices and 302 invariants, 477 commands, 133 queries, 584 domain events (585 AsyncAPI messages including the derived `EVT-SEC-VERSION-INCREMENTED`), 16 deployment units (`12-solution/deployment-units.md`) — but not *how the code inside a deployment unit is organised*. Without a single internal structure, 16 units built by a small team (system-definition §6) would drift into 16 structures, and the platform's hardest guarantees would be re-implemented, or skipped, unit by unit:

- a policy decision before **any** retrieval, failing closed (ADR-P11, REQ-FND-010/013, FIT-03, FIT-16);
- tenant scope on every access, with row-level security as a second barrier (ADR-P04, FIT-02);
- state + history + outbox + audit outbox in **one** transaction (ADR-P02, FIT-04);
- no reads from another context's store (FIT-01);
- `If-Match` optimistic concurrency and `Idempotency-Key` on every command (89/89 aggregates);
- generated contracts driving server stubs, with hot paths possibly re-implemented in Go behind the same contracts (TD-15);
- acceptance specs that exercise every state transition (89 files, `13-verification/acceptance/`).

## Decision Drivers
1. **Domain rules must be testable without infrastructure.** 302 invariants and 89 state machines are the core of the specification; they must run in plain unit tests.
2. **Cross-cutting guarantees must be enforced once, structurally,** not remembered per handler (tenant scope, PEP, transaction boundary, idempotency, audit).
3. **Technology replaceability** is already anticipated: TD-03 (graph engine) and TD-04 (NATS instead of Kafka) must stay local to adapters; TD-15 (Go for hot paths) must stay local to one unit, behind unchanged contracts.
4. **Operational simplicity** for a small team: the structure must be learnable in a day and identical in every unit.
5. **Traceability**: every specification artifact (aggregate, command, query, policy, event, error) must have exactly one home in the code structure.

## Considered Options

### Option 1 — Hexagonal (Ports & Adapters), organised by use case inside the application layer
- **Pros:** the domain core has no I/O, so invariants and transition tables are tested directly; tenant scope, PEP, unit of work and outbox sit in one application pipeline, so they cannot be bypassed; infrastructure choices are adapters behind ports, so TD-03/TD-04 reversals are local, and a TD-15 rewrite is a bounded re-implementation of one unit with its test suite unchanged; maps one-to-one onto the specification (aggregate → domain, command → handler, policy → authorization port, event → outbox port).
- **Cons:** more interfaces and files than a CRUD service; requires discipline on dependency direction (mitigated by FIT-10 and FIT-20).

### Option 2 — Classic layered (controller → service → repository)
- **Pros:** familiar to most developers; fewer abstractions.
- **Cons:** persistence and framework types leak into business logic; no structural place that forces the PEP before retrieval or the outbox in the same transaction; replacing a technology touches service code.

### Option 3 — Pure vertical slices (one file per feature, from HTTP to SQL)
- **Pros:** fastest to write, very low ceremony.
- **Cons:** invariants spread across slices instead of living in the aggregate; the cross-cutting guarantees must be repeated per slice; weak fit with 89 explicit state machines.

## Decision Outcome
**Option 1, with vertical organisation inside the application layer** ("hexagonal outside, slices inside"). Every deployment unit follows the same four rings, detailed in `18-analysis-design/11-hexagonal-reference.md` (full port catalog in its §5):

| Ring | Contains | May depend on |
|---|---|---|
| **Domain** | aggregates (state, transition table, invariants), value objects, domain events, domain errors | shared kernel value types only |
| **Application** | one command handler per `CMD-*`, one query handler per `QRY-*`, one process handler per consumed event or `SYS:` trigger; the command pipeline; the context's own command/query types | domain, ports |
| **Ports** | interfaces owned by the application at real I/O boundaries: repository / unit of work, authorization (PEP), security context, idempotency, outbox / audit, read models, other-context clients, encryption, clock | domain types |
| **Adapters** | inbound: HTTP (generated contract types mapped to application types), Kafka consumer, scheduler / worker; outbound: PostgreSQL, OPA, OpenSearch, object storage, KMS, other-context OHS clients | application, ports, domain types, platform libraries, contracts |

**Non-negotiable rules:**
1. Dependencies point inward only. The domain imports no framework, database, messaging or HTTP type (FIT-10).
2. Every command passes through one pipeline, in this order:
   1. establish the security context and set the **tenant scope** for the unit of work (row-level security session setting — ADR-P04, FIT-02);
   2. **coarse authorization** before any data access: tenant match, action on resource type within the caller's scope (FIT-03, fail-closed — FIT-16);
   3. idempotency check (`Idempotency-Key`);
   4. load the aggregate at the expected version (`If-Match`);
   5. **full authorization** with the loaded resource's attributes — labels, owning organisation, state, participants — as policy information (PIP); segregation-of-duties rules evaluated here; nothing about the resource is returned before this decision;
   6. execute the transition in the domain;
   7. persist state + history + outbox event + audit record + idempotency record in **one** unit of work (FIT-04);
   8. apply decision obligations (audit, watermark, MFA) and return the `ResourceRef`.
3. Queries never load aggregates. They read declared read models or projections, with the PDP's `allowed_scope` applied before scoring, counting or paging, and re-check returned items as amended by CR-47: subjects against the BC01 security-version store, objects through a batched `LabelCheck` per page (ADR-P06).
4. Another context is reached only through its published contract: synchronous OHS client port, or events through the inbox. Never its tables (FIT-01).
5. `SYS:` transitions — time-driven, condition-driven, event-driven or worker-driven — enter through the same pipeline under a workload identity, with the same invariants as actor commands.

## Rationale
Drivers 1, 2, 3 and 5 are only fully met by Option 1; driver 4 is met by keeping the rings identical across all 16 units and by organising the application layer by use case, which removes the "service class" sprawl that makes hexagonal code feel heavy. The specification is already written in the hexagon's vocabulary (aggregates, commands, policies, events, projections), so the mapping adds no new concepts. The two-step authorization (rule 2.2 and 2.5) is required because many policies need resource attributes — e.g. `POL-TASK-COMPLETE` needs the task's state and `POL-TASK-APPROVE-SOD` its assignee (`08-security/authorization-model.md` §4) — while FIT-03 forbids data access without a prior policy decision.

## Consequences

### Positive
- Every state machine and invariant is unit-testable in isolation; the 89 acceptance files map to application-level tests with in-memory adapters.
- Tenant scope, authorization, the single transaction and idempotency are properties of the pipeline, not of individual handlers.
- TD-03/TD-04 reversals replace adapters only; a TD-15 rewrite stays inside one unit behind unchanged contracts and acceptance specs.
- New team members find any specification artifact in a predictable place.

### Negative
- More files per feature than a CRUD service (handler, port, adapter).
- Mapping between contract types, domain objects and persistence rows is explicit work.
- Commands pay two policy evaluations; mitigated by the ≤ 60 s decision cache keyed by `security_version` (`authorization-model.md` §5).

### Risks and mitigations
- **Risk:** dependency rules erode under delivery pressure. **Mitigation:** FIT-10 (domain purity) and FIT-20 (module-boundary rules) in CI; FIT-03 and FIT-16 (policy decision before access, fail-closed) as call-graph and chaos tests (`13-verification/fitness-functions.md`).
- **Risk:** over-abstraction (ports with a single trivial implementation everywhere). **Mitigation:** ports exist only at the I/O boundaries listed in `11-hexagonal-reference.md` §5; no port for pure in-process logic.

## Related Decisions
- ADR-P02 (persistence style) — the unit of work and outbox placed in the pipeline.
- ADR-P04 (tenant isolation) — tenant scope set per unit of work.
- ADR-P06 (as amended by CR-47), ADR-P11 — PEP/PDP, `allowed_scope` and result re-checks placed in the authorization port and query handlers.
- ADR-P18 — repository and module structure that realises these rings per bounded context and per deployment unit.
