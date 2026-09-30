---
id: SESSION-SLC09
type: session-report
wave: W4–W7 (SLC-09, Release 2)
date: 2026-09-24
basis: V6§21.3
---

# SESSION REPORT — SLC-09 Assets, Resources, Allocation & Readiness (R2)

**Result:** **DESIGN COMPLETE.** G6 held until the R1 pilot review, as agreed for all R2 slices (RSK-027).

## Produced (counts computed from source)
| Output | Count |
|---|---|
| Aggregates: Asset, Maintenance Order, Asset Reservation, Asset Assignment, Resource Pool, Allocation, Role Requirement (BC05) | 7 · 18 invariants |
| Commands / queries / events | 39 / 6 / 40 |
| Specification: ordered allocation checks with reason codes, hourly capacity ledger, priority-ordered contention, decision-backed pre-emption, availability function, readiness, DEBT-001 migration | 1 |
| OpenAPI (45 ops) — validated · AsyncAPI (40) · errors (38) · logical model (13 tables, with database EXCLUDE constraints) | — |
| Acceptance: 172 generated + 17 scenarios · 6 properties | — |

## Key design points
1. **No over-commitment, provably:** an hourly capacity ledger, updated in the allocation transaction, backed by a database check — and a property test under random concurrent requests (P-91/P-92).
2. **Priority then time, deterministically:** requests per pool are ordered in 250 ms windows by priority, then arrival.
3. **Pre-emption is a decision, never a side effect:** it requires a recorded decision by the pool-scope authority and notifies affected task owners.
4. **Availability is one explicit function** — service state, certifications valid for the whole window, maintenance, reservations, assignments — evaluated at read time so expiries apply instantly; hidden blockers are not revealed.
5. **Asset location reuses the claims kernel** (bitemporal claims on a linked information entity) instead of a location column.
6. **DEBT-001 closes:** R1's text-only resource notes become structured references through a reviewed migration that never deletes the original notes.

## Gates
R1: G6 READY (awaiting ratification) · R2: G1/G2 PASS · **SLC-09 DESIGN COMPLETE (G6 held)**

## Next recommended session
**SLC-12 — Products, Knowledge, Archive & Historical Reconstruction.**
