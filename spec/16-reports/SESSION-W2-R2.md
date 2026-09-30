---
id: SESSION-W2-R2
type: session-report
wave: W1/W2 for Release 2
date: 2026-09-24
basis: V6§10.2, V6§21.3
---

# SESSION REPORT — Release 2: scope, requirements and quality scenarios

**Context:** the project owner chose to continue with the R2 study before the R1 pilot. Per V6 (one wave per session) and because R2 had no requirements baseline, this session establishes R2's W1/W2 before any R2 slice is designed.

## Produced
| Artifact | Content |
|---|---|
| `01-business/release-2-scope.md` | R2 capabilities → 6 slices (SLC-09, 10, 12, 14, 15, 16), design order, 10 delegated decisions, timing safeguard |
| `02-requirements/requirements.md` | **+51 R2 system requirements** in EARS (R1's 114 unchanged) |
| `02-requirements/quality-scenarios.md` | **+15 R2 quality scenarios** (AI groundedness, citation accuracy, hallucination, AI security, allocation integrity, archive retrieval, reconstruction…) |
| `02-requirements/use-cases.md` | +9 new use cases; 17 existing R2 use cases linked to requirements |
| `14-slices/slices.md` | R2 slices and order |
| `16-reports/REQUIREMENTS-QUALITY-REPORT-R2.md` | checks: 0 EARS violations, 0 missing criteria, 2 defects found and fixed |

## Key R2 requirements
- **Resources:** allocation checks authorization, type, availability, capacity, time, geography, priority, commitments and policy (PRJ§63); no over-commitment under concurrency; pre-emption only by authority; structured links replace R1's text-only resource notes (closes DEBT-001).
- **AI:** the full pipeline of PRJ§25 (identity → policy → authorized retrieval → context package → model → grounding → confidence → human review); "Insufficient Evidence" instead of invention (PRJ§112); citations for every statement; AIL ≤ 3 in R2; local models by default; injected instructions treated as data.
- **Products & knowledge:** template-based products whose label is at least their content's; distribution only to authorized recipients with watermarks; knowledge as reviewed, versioned claims; lessons linked to closed work.
- **Archive:** OAIS-style packages, preservation formats, periodic integrity verification, labelled historical reconstruction (RECORDED / RECONSTRUCTED / INFERRED / UNKNOWN).

## Safeguard for designing before the pilot (RSK-027)
Every numeric target in R2 is marked for recalibration after the R1 pilot, and no R2 slice receives G6 before those results are reviewed.

## Not decided by delegation
Tenant ERP/HRIS/DMS/CMMS systems (UNK-021), GPU pool size (UNK-012), and the actual language model — chosen by evaluation on tenant data, not assumed.

## Gates (R2)
G1-R2 PASS (delegated) · **G2-R2 PASS (delegated)** · G3: R1 kernel applies (no new kernel ADR required so far) · G6-SLC for R2 slices: NOT_STARTED

## Next recommended session
**SLC-09 — Assets & Resources** (W4–W7), which also closes DEBT-001.
