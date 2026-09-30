---
id: SESSION-SLC15
type: session-report
wave: W4–W7 (SLC-15, Release 2)
date: 2026-09-24
basis: V6§21.3
---

# SESSION REPORT — SLC-15 Coordination & Correlation/Fusion (R2)

**Result:** **DESIGN COMPLETE** (G6 held until the R1 pilot review).

| Output (computed) | Count |
|---|---|
| Aggregates: Coordination Case (BC04); Correlation Proposal, Correlation Rule (BC02) | 3 · 10 invariants |
| Commands / queries / events | 17 / 4 / 19 |
| OpenAPI | 21 operations — validated |
| Hand-written acceptance scenarios | 8 · 5 properties |

## Key design points
1. **Coordination with boundaries:** each participant sees only its sections and what its members may see; coordination stays inside one tenant.
2. **Authority is not borrowed:** an action needing another organization's authority stays blocked until that organization records a decision through a Decision Request.
3. **Correlation proposes, humans accept:** spatio-temporal bucketing with accuracy-aware distances; proposals never touch data; acceptance acts through owner commands.
4. **Honest corroboration:** independence is judged by lineage — a source cannot corroborate itself, nor can a copy corroborate its original.
5. **Transparent fusion:** inverse-variance location, interval intersection for time, majority for type with ties left DISPUTED; fused values are derived claims citing every contributor and never overwrite existing claims (conflicts go to SLC-04).

## Next recommended session
**SLC-16 — Enterprise integrations** (ERP, HRIS, DMS, sensors, CAP alerts) — the last R2 slice.
