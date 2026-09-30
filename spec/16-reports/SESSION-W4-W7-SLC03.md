---
id: SESSION-SLC03
type: session-report
wave: W4–W7 (SLC-03)
date: 2026-09-24
basis: V6§21.3
---

# SESSION REPORT — SLC-03 Task Lifecycle

**Result:** **G6-SLC-03 READY FOR IMPLEMENTATION (delegated).**

## Produced
| Output | Count |
|---|---|
| Aggregates: Task (BC04), Task Type (BC04), Qualification Record (BC05) | 3 · 14 invariants |
| Commands / queries / events | 33 / 6 / 36 |
| Specifications: Task Lifecycle Rules (decisions, criteria, scheduling, dependencies, offline contract), Eligibility Evaluation (decision table + precedence) | 2 |
| OpenAPI (39 ops, validated; offline-capable operations flagged) · AsyncAPI (36) · errors (29) · logical model (9 tables) | — |
| Acceptance: 86 allowed + 306 rejected (generated) + 22 scenarios · 9 properties | — |
| Threats 6 · failure modes 4 · observability 6 · quality scenarios +3 | — |

## Decisions that close the Task questions open since V6
- **OQ-031:** APPROVED (review accepted) → COMPLETED (all criteria met; automatic when all criteria are machine-checkable) → CLOSED (administrative, manual or automatic after 7 days without open follow-ups).
- **OQ-032:** deadlines escalate by default; expiry only for task types that declare it.
- **OQ-033:** rejection is final; retry is a linked follow-up task.
- **CR-46:** suspension is an orthogonal flag, not a state — it can be tested with a fixed transition table, unlike the "return to prior state" in the V6 example.

## Other design points
- Eligibility is evaluated at the requested time from qualification history, independent of whether the expiry job has run, and is stored on the task as an audit snapshot. Unreachable eligibility service → assignment denied (fail-closed).
- A task cannot be assigned to someone not cleared for its label; reclassifying a task above its assignee's clearance requires reassignment first.
- Completion criteria freeze at assignment.
- The offline contract for SLC-11 is fixed now: six field commands carry `base_version`; stale replays become sync conflicts (CF-05), never last-write-wins.
- `task_events` from the original document is removed from the data model (ADR-P02).

## Registers
OQ-031..033 closed · CR-46 added and applied · HAP-09 evidence: SLC-03 · glossary +2.

## Gates
G0–G3 PASS · **G6-SLC-01, 02, 03, 04 READY** · G6 release BLOCKED (remaining R1: SLC-05, 06, 07, 08, 11, 12a)

## Next recommended session
**SLC-05 — Secured search & graph projections**: consumes SLC-01..04 events and implements ADR-P06 (pre-filter + authoritative re-check, inference-safe counts and facets, Arabic analyzers).
