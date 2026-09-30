# Specification Package — Unified Geospatial Information, Intelligence, Knowledge, Planning & Operations Platform

**Governed by:** V6 — Engineering Study Operating System
**Source document:** PRJ (المشروع الكامل.md) — epistemic level: DOCUMENTED
**Current wave:** R1 study COMPLETE — **G6 RATIFIED (2026-09-27)**, ready for build (G7) pending a build team · R2 slices ALL DESIGN COMPLETE, baseline consolidated (EB-R2-2026-09-24) → G6 held per slice until R1 pilot review (RSK-027) · R3 scoped (W1/W2); **all three R3 slices — SLC-17 (Risk & Contingency), SLC-18 (Logistics & Supply), SLC-19 (Training, Competency & Exercises) — DESIGN COMPLETE** → G6 held until R1 **and** R2 pilot review (RSK-028); R3 detailed design fully done, no further R3 slice design remains
**File format:** Markdown only (HAP-11); data files embed machine-readable YAML

## Wave status
| Wave | Status |
|---|---|
| W0 Setup | DONE (DRAFT) |
| W1 Discovery & Framing | DONE — delegated decisions (`W1-answers.md`) |
| W2 Requirements & QAS | DONE — 114 REQ, 43 QAS at W2 (74 after slices), G2 PASS (delegated) |
| W3 Information Kernel | DONE — 15 ADRs, kernel models, security kernel, G3 PASS (delegated) |
| W4–W7 Slices | DONE — all 10 R1 slices READY (delegated; SLC-12a legal values pending UNK-002) |
| W8 Solution & Technology | DONE — ADR-P05, 17 technology decisions, C4, deployment units, cells, DR, cost model |
| W9 Baseline | DONE — Engineering Baseline EB-R1-2026-09-24, **G6 RATIFIED (2026-09-27)** |
| **R2** W1/W2 | DONE — 6 slices, 51 REQ, 15 QAS (`01-business/release-2-scope.md`) |
| R2 slices | ALL 6 DESIGN COMPLETE (SLC-09, 10, 12, 14, 15, 16; G6 held until R1 pilot) |
| R2 baseline consolidation | DONE — EB-R2-2026-09-24 (design baseline only); consistency, anti-pattern and architecture reviews, full traceability (51/51); see `16-reports/SESSION-R2-BASELINE.md` |
| **R3** W1/W2 | DONE (scope, delegated) — risk & contingency, training/exercises, logistics, extended comms (undecomposed, UNK-022); see `01-business/release-3-scope.md` |
| R3 slices | **SLC-17 (Risk & Contingency) DESIGN COMPLETE** (`16-reports/SESSION-W4-W7-SLC17.md`) — 2 aggregates, 16 REQ, 2 cross-slice corrections to R1 (CR-60 Plan, CR-61 Task); G6 held until R1 **and** R2 pilot review (RSK-028). **SLC-18 (Logistics & Supply) DESIGN COMPLETE** (`16-reports/SESSION-W4-W7-SLC18.md`) — 2 aggregates, 14 REQ, 1 cross-slice correction to R2 (CR-62 Allocation, guard text only); G6 held until R1 **and** R2 pilot review (RSK-028; this slice's real dependency, SLC-09, is R2 and unmeasured). **SLC-19 (Training, Competency & Exercises) DESIGN COMPLETE** (`16-reports/SESSION-W4-W7-SLC19.md`) — 3 aggregates, 15 REQ, 1 cross-slice correction to R2 (CR-63 Knowledge Object, guard text only; SLC-03 and SLC-09 both unmodified); G6 held until R1 **and** R2 pilot review (RSK-028; narrowest actual exposure of the three R3 slices). **R3 is now fully DESIGN COMPLETE.** |

## Where to start reading
1. `16-reports/IMPLEMENTATION-READINESS-R1.md` — the verdict, conditions and build order
2. `00-governance/RATIFICATION-PACKAGE.md` — **RATIFIED 2026-09-27**; §7 external facts (legal jurisdiction, budget, licences) still open before G8
3. `16-reports/ENGINEERING-BASELINE-R1.md` — what is baselined and how to change it
4. `16-reports/SESSION-W9.md` — final checks and totals (R1)
5. `16-reports/SESSION-R2-BASELINE.md` — R2 design baseline, consolidated checks, and the conditions gating each R2 slice's own future G6
6. `16-reports/ENGINEERING-BASELINE-R2.md` — what R2 adds (design only — not build-ready)
7. `15-traceability/rtm-r1.md`, `15-traceability/rtm-r2.md` — full traceability
8. `13-verification/tooling/` — generators and slice sources (regenerate the package)

## Folder map
00-governance · 01-business · 02-requirements · 03-domain · 04-information · 05-contracts · 06-data · 07-quality · 08-security · 09-reliability · 10-ai · 11-integration · 12-solution · 13-verification · 14-slices · 15-traceability · 16-reports
