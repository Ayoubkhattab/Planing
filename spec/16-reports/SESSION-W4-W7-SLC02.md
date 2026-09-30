---
id: SESSION-SLC02
type: session-report
wave: W4–W7 (SLC-02)
date: 2026-09-24
basis: V6§21.3
---

# SESSION REPORT — SLC-02 Information Kernel

**Result:** **G6-SLC-02 READY FOR IMPLEMENTATION (delegated).**

## Produced
| Wave | Output | Count |
|---|---|---|
| W4 | Aggregates (11 BC02 + 1 BC07) with complete matrices | 12 · 38 invariants (corrected; first stated 46) |
| | Commands / queries / events | 57 / 16 / 64 |
| | **Claims & Temporal Kernel library specification** (types, operations, normative resolve algorithm, visibility, completeness, generalization, performance budgets) | 1 |
| | Policy tables + 4 new platform baseline rules (PB-08..PB-11) | 57 + 16 + 4 |
| W5 | Workloads (7), quality scenarios (+5), threats (10), failure modes (8), degradation, observability (10 signals) | — |
| W6 | OpenAPI 3.1 (BC02 66 ops, BC07 7 ops) — validated · AsyncAPI (64 messages) · errors (45) · logical model (19 tables) | — |
| | Acceptance: 63 allowed + 111 rejected (generated) + 28 temporal/claims/security/ingestion scenarios · 8 library properties | — |
| W7 | Lint 0 errors · traceability 24 requirements, 0 untested · ATAM-lite · readiness record | — |

## Key design points
1. **The resolve algorithm is normative.** One library, one algorithm, one oracle test set (500 temporal cases). Every later slice calls it instead of re-implementing time and claims (RSK-019).
2. **Visibility first.** Hidden claims are removed before status, counts and completeness are computed. Two users can legitimately see SINGLE and DISPUTED for the same attribute; that is correct and closes the inference channel (QAS-SEC-010).
3. **Units, Arabic spelling and tolerances are normalized before comparing values**, so "1.2 km" and "1200 m", or "أحمد" and "احمد", corroborate instead of conflicting.
4. **High-rate data stays in observations; claims are summarized** per predicate sampling interval — the design keeps 5,000 obs/s from turning into 5,000 claim writes/s on hot keys.
5. **Files never pass through the application tier** (direct signed transfer, offline scanning, content-addressed dedupe).
6. **Withdrawn evidence re-evaluates dependent claims automatically** through a system assessment command — no silent change, full audit.

## Registers
RSK-020 added (current-table divergence). HAP-09 evidence: SLC-02 approved (delegated). Glossary +3.

## Stale-draft cleanup
Two orphan files from an abandoned earlier draft of this slice (`AGG-REAL-WORLD-EVENT`, `AGG-INGESTION-BATCH`) were found and removed before packaging; the package contains only the design documented here.

## Gates
G0–G3 PASS · **G6-SLC-01 READY · G6-SLC-02 READY** · G6 release BLOCKED (8 R1 slices remaining: SLC-03..08, SLC-11, SLC-12a)

## Next recommended session
**SLC-03 — Task lifecycle** (smaller slice; completes V6§13.5 with the open questions OQ-031..033) — or **SLC-04 — Conflict & Entity Resolution**, which directly extends the kernel just specified.
