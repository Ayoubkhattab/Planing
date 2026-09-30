---
id: SESSION-SLC12A
type: session-report
wave: W4–W7 (SLC-12a) + R1 slice consolidation
date: 2026-09-24
basis: V6§21.3
---

# SESSION REPORT — SLC-12a Retention, Legal Hold, Disposition & Erasure (+ R1 consolidation)

**Result:** **G6-SLC-12a READY (delegated), legal values pending UNK-002.** With it, **all 10 R1 slices are designed and READY.**

## SLC-12a produced
| Output | Count |
|---|---|
| Aggregates: Retention Schedule, Legal Hold, Disposition Run, Erasure Request (BC08) | 4 · 15 invariants |
| Commands / queries / events | 15 / 5 / 25 |
| Specification: key hierarchy, class-bucket crypto-shredding, hold re-wrapping, subject erasure, **restore gate** | 1 |
| OpenAPI (20 ops; RetentionRule, HoldScopeItem, HoldCheck) — validated · AsyncAPI (25) · errors (19) · logical model | — |
| Acceptance: 73 generated + 14 scenarios · 5 properties | — |

## Key design points
1. **Destroy keys, not rows.** Records are encrypted per (record class × trigger month); one key destruction retires a whole bucket everywhere, including backups — the only practical way at a billion-record scale.
2. **Holds win, precisely.** Held records inside a bucket are re-wrapped under the hold's key before the bucket key is destroyed; holds never block versioned changes, only destruction.
3. **Restore gate (CR-51).** An old key-store backup could have revived destroyed keys, silently undoing erasure. An append-only destruction log is replayed on every restore before any service starts, and key-store backups are kept ≤ 35 days. This corrects an over-strong claim in ADR-P08.
4. **Two people for every destructive decision:** schedule activation, disposition, erasure and hold release.

## R1 consolidation — global checks run after the last slice
| Check | Finding | Action |
|---|---|---|
| Requirement coverage across all slices | **15 of 114 R1 requirements were not traced by any domain slice** (platform & cross-cutting) | 8 traced now via fitness functions and contract lint; 7 assigned explicitly to W8/W9 (`15-traceability/trace-platform.md`, CR-53) |
| REQ-GOV-002 (classification on every T1/T2 object) | 12 creation commands carried no label | label source defined for all 54 aggregates — explicit, derived by rule, or administrative (`08-security/label-derivation-rules.md`, SL-29, CR-52) |
| Counts in earlier session reports | invariant counts in 6 earlier reports were overstated (e.g. SLC-01 stated 53, actual 44) | corrected in those reports from the source data |

## R1 design totals (computed from source data)
| Slice | Aggregates | Invariants | Commands | Events | Queries |
|---|---|---|---|---|---|
| SLC-01 | 12 | 44 | 71 | 79 | 14 |
| SLC-02 | 12 | 38 | 57 | 64 | 16 |
| SLC-03 | 3 | 14 | 33 | 36 | 6 |
| SLC-04 | 3 | 14 | 19 | 23 | 6 |
| SLC-05 | 1 | 4 | 4 | 7 | 5 |
| SLC-06 | 5 | 15 | 22 | 30 | 8 |
| SLC-07 | 5 | 16 | 32 | 35 | 9 |
| SLC-08 | 5 | 17 | 24 | 33 | 9 |
| SLC-11 | 4 | 14 | 16 | 25 | 5 |
| SLC-12a | 4 | 15 | 15 | 25 | 5 |
| **Total** | **54** | **191** | **293** | **357** | **83** |

OpenAPI operations across all contract files: **376**, every file validated.

## Registers
CR-51, CR-52, CR-53 · RSK-025 · HAP-09 **approved (delegated)** for all R1 slices, with two conditions (ADR-P05 capability list for SLC-05; UNK-002 legal values before G8) · FIT-19, SL-29 · glossary +3.

## Gates
G0–G3 PASS · **G6-SLC for all 10 R1 slices READY** · G4/G5 PARTIAL (W8) · G6 release BLOCKED only by W8 and W9.

## Next recommended session
**W8 — Solution & Technology Decisions:** decide ADR-P05 and the remaining technical choices from `12-solution/w8-inputs.md` (measured/estimated workloads and capability lists from every slice), define deployment units, C4 views, the cost model, and close the 7 platform requirements in `trace-platform.md`. Then **W9 — Baseline consolidation and G6 for R1.**
