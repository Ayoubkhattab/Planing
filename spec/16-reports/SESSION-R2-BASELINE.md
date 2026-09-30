---
id: SESSION-R2-BASELINE
type: session-report
wave: R2 baseline consolidation (W9-style)
date: 2026-09-27
basis: V6§10.2 W9, V6§20.3, RSK-027
---

# SESSION REPORT — R2 Baseline Consolidation

**Result:** **R2 DESIGN BASELINED** (EB-R2-2026-09-24). **No G6** for any R2 slice — all six remain held pending the R1 pilot review, exactly as agreed in `01-business/release-2-scope.md` §3 (RSK-027). This session did not change that: it consolidated six independently-designed slices into one coherent, checked, traceable release baseline, the same way W9 did for R1.

## Preceding this session
A new conversation was started with the package delivered as `spec-R2-SLC16.zip` plus the V6 operating-system document. Before any new work, the package was extracted and its embedded tooling (`13-verification/tooling/spec-tooling.md`, `slice-sources.md`) was pulled out and run end-to-end (`slice_gen ← slice_contracts ← acc_gen` for all 16 slices, then `w9_check`). **Round-trip result: 0 differing files** against every generated artifact — the package's self-description of its own reproducibility held. Two Windows-environment-only issues surfaced and were worked around locally (the tools' hardcoded `/tmp` needs a real directory at the current drive's root, and `slice_contracts.py` needs `work/05-contracts/` pre-created) — neither is a defect in the package.

## Produced
| Artifact | Purpose |
|---|---|
| `16-reports/CONSISTENCY-REPORT-R2.md` | automated cross-artifact checks over the whole R1+R2 corpus (`w9_check` re-run for real, not simulated) |
| `16-reports/ANTI-PATTERN-REPORT-R2.md` | anti-pattern re-assessment for the six R2 slices, on top of the R1 re-assessment (unchanged) |
| `16-reports/ARCHITECTURE-REVIEW-R2.md` | ATAM-lite for R2: new utility-tree entries, sensitivity points, trade-offs, risk themes |
| `15-traceability/rtm-r2.md` | OUT → BRQ → REQ → slice → verification for all 51 R2 requirements (51/51) |
| `16-reports/ENGINEERING-BASELINE-R2.md` | what is baselined as **design** (EB-R2-2026-09-24), explicitly not build-ready, and the per-slice conditions that gate each one's own future G6 |
| `12-solution/deployment-units.md` (updated) | +3 deployment units (DU-14 Readiness, DU-15 Knowledge, DU-16 AI Serving) split out or added under V5§97 criteria for the new load/failure profiles R2 introduced |

## What the consolidation found (computed, `w9_check` over the full corpus)
| Check | Verdict |
|---|---|
| Commands / queries / events missing from contracts | 0 / 0 / 0 (across all 82 aggregates) |
| Aggregates without acceptance / label source / policy | 0 / 0 / 0 |
| Requirements untraced (R1, must be 0) | 0 |
| Requirements untraced (R2) | 0 — all 51 already traced via the six slices' own `trace-slcXX.md`, even though G6 is held |
| QAS without a verification reference | 0 / 89 |
| Corrections not applied | 0 / 59 |
| Risks without mitigation | 0 / 27 |

No new inconsistency was found. This is expected, not a coincidence: each R2 slice session already ran its own lint/consistency pass before moving to the next (CR-58 at SLC-10, CR-59 at SLC-14 — both cross-slice corrections into R1 slices, both applied and re-verified at the time). This session's contribution was to re-run those checks over the *combined, final* corpus rather than slice-by-slice, and to produce the release-level artifacts (traceability roll-up, architecture review, anti-pattern review, baseline record) that only make sense once every slice is in.

## Architecture change made during consolidation
`12-solution/deployment-units.md` previously merged BC05 into DU-08 ("BC05 small in R1, no reason to split yet"). R2's SLC-09 grows BC05 into an hourly-capacity-ledger allocation engine with a 250 ms priority-ordered contention window and a database-enforced no-overcommit constraint — a distinct scaling and consistency profile from BC04's general task/plan CRUD, meeting the V5§97 separation criteria on its own terms. Split into **DU-14 Readiness**. Two more units were added for contexts that had no unit at all in R1 because they were empty: **DU-15 Knowledge** (BC06 — batch generation, watermarking, WORM archive, distinct change/failure cadence) and **DU-16 AI Serving** (BC07/AI — GPU-bound vLLM inference, Kueue-scheduled, isolated from the CPU-only rest of BC07). All three are **designed, not deployed**: no ADR was needed (the deployment-units document is a design artifact under its own V5§97 criteria, not a build commitment), and the note on the file says explicitly that no actual deployment precedes the R1 pilot review and, for DU-16, confirmation of GPU pool sizing (UNK-012).

## Conditions tied to the R1 pilot (consolidated, supersedes scattered per-slice notes)
1. **Common to all six R2 slices:** R1 pilot executed, its results reviewed by the owner or delegate, and confirmation that nothing in the pilot invalidates a structural R2 design assumption. Only then may a slice's G6 be considered — and even then, one at a time, not as a block.
2. **SLC-10 (Grounded AI) only, additional:** at least one language model passes the `SPEC-AI` evaluation thresholds (citation ≥ 95%, hallucination ≤ 2%, insufficient-evidence recall ≥ 95%, zero successful injection/exfiltration) on real tenant data, not synthetic data.
3. **SLC-16 (Enterprise Integrations) only, additional:** the first tenant's actual ERP/HRIS/DMS/CMMS systems are identified well enough to build one real adapter (partial closure of UNK-021 — the framework itself does not wait on this).
4. **Common, before any production commitment (not a G6 gate, but before G8-equivalent for R2):** GPU pool sizing (UNK-012) confirmed before DU-16's quotas are fixed in production.

## Gates
G0–G6 for R1: unchanged (**R1 G6 READY, awaiting ratification** — see `00-governance/RATIFICATION-PACKAGE.md`, still the user's open action item). R2: G1/G2 PASS (from W1/W2-R2) · all 6 slices DESIGN COMPLETE · **R2 baseline consolidated at the design level (this session)** · **G6 held for every R2 slice**, condition list above.

## Next recommended session
Nothing further is designable in R2 without new information. The next substantive step is **R1 pilot execution** (outside the study phase) or, if the owner wants to continue studying regardless, **R3 scoping** (risk & contingency, full training, exercises/simulation, logistics, extended comms — explicitly out of R2 per `01-business/release-2-scope.md` §1) with the same RSK-027-style timing safeguard.
