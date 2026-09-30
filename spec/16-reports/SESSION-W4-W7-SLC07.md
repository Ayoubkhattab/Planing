---
id: SESSION-SLC07
type: session-report
wave: W4–W7 (SLC-07)
date: 2026-09-24
basis: V6§21.3
---

# SESSION REPORT — SLC-07 Analysis Case → Run → Finding → Assessment

**Result:** **G6-SLC-07 READY FOR IMPLEMENTATION (delegated).**

## Produced
| Output | Count |
|---|---|
| Aggregates: Analysis Case, Analysis Method, Analysis Run, Finding, Assessment Version | 5 · 16 invariants (corrected; first stated 20) |
| Commands / queries / events | 32 / 9 / 35 |
| Specification: reproducibility (5 pinned elements), execution under the submitter's authority, estimative language, pinned citations and withholding | 1 |
| OpenAPI (40 ops; InputPin, KeyJudgment, Citation schemas) — validated · AsyncAPI (35) · errors (29) · logical model (12 tables) | — |
| Acceptance: 141 generated + 19 scenarios · 6 properties | — |
| Threats 6 · failure modes 4 · observability 6 · quality scenarios +2 | — |

## Key design points
1. **Reproducibility by construction.** Data pinned by known_at (bitemporal kernel), method version, container image digest, parameters and seed. A deterministic run reproduces bit-for-bit even after the underlying claims were corrected; a different environment is reported, never silently substituted.
2. **Runs execute with the submitter's authority,** never with system privileges, so an analysis cannot read beyond its author's clearance; results are labelled at least as high as their inputs.
3. **CR-29 closed for analysis:** the 12-component AnalysisCase of the original document becomes five aggregates with independent lifecycles.
4. **Published assessments are immutable and version-pinned;** a decision keeps pointing to the version it relied on even after revisions.
5. **Estimative language is structured:** probability term (with fixed numeric range) separate from analytic confidence.
6. **Retiring a method is blocked while it backs published work,** so reproduction stays possible.

## Registers
CR-29 partially closed · RSK-024 added · HAP-09 evidence: SLC-07 · glossary +2 · W8 inputs +1.

## Gates
G0–G3 PASS · **G6-SLC-01..07 READY** · G6 release BLOCKED (remaining R1: SLC-08, SLC-11, SLC-12a)

## Next recommended session
**SLC-08 — Decision → Plan → Version → Baseline → Tasks** (closes CR-29 for Plan and connects analysis to execution).
