---
id: SESSION-SLC14
type: session-report
wave: W4–W7 (SLC-14, Release 2)
date: 2026-09-24
basis: V6§21.3
---

# SESSION REPORT — SLC-14 Collection Requirements & Planning (R2)

**Result:** **DESIGN COMPLETE** (G6 held until the R1 pilot review).

| Output (computed) | Count |
|---|---|
| Aggregates: Collection Requirement, Collection Plan (BC02) | 2 · 6 invariants |
| Commands / queries / events | 14 / 4 / 16 |
| OpenAPI | 18 operations — validated |
| Hand-written acceptance scenarios | 8 · 4 properties |

## Key design points
1. **Requirements are decomposed into EEIs** that say exactly what counts as an answer, so fulfilment is computed, not argued.
2. **Only validated observations count,** matched automatically by area, window and EEI criteria, with lineage.
3. **Fulfilment is viewer-scoped:** a requester never learns that classified collection answered their question; expiry depends only on the due date.
4. **Plans become field tasks** that work offline (SLC-11) and whose observations flow back into matching — closing value stream VS01 end to end.

## Cross-slice change
CR-59: task `plan_ref` accepts a collection plan; SLC-03 regenerated.

## Next recommended session
**SLC-15 — Coordination cases & correlation/fusion.**
