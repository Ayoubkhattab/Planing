---
id: SESSION-SLC04
type: session-report
wave: W4–W7 (SLC-04)
date: 2026-09-24
basis: V6§21.3
---

# SESSION REPORT — SLC-04 Conflict Management & Entity Resolution

**Result:** **G6-SLC-04 READY FOR IMPLEMENTATION (delegated).**

## Produced
| Output | Count |
|---|---|
| Aggregates (Conflict, ER Case, Match Ruleset) with complete matrices | 3 · 14 invariants |
| Commands / queries / events | 19 / 6 / 23 |
| Component specifications: Conflict Detection Engine, Candidate Generation | 2 |
| Cross-slice change: kernel library §7 (resolution through identity clusters); QRY-ENT-RESOLVED returns canonical_urn | 1 |
| OpenAPI (25 ops, validated) · AsyncAPI (23 messages) · errors (20) · logical model (8 tables) | — |
| Acceptance: 21 allowed + 98 rejected (generated) + 20 scenarios · 8 properties | — |
| Threats 7 · failure modes 4 · observability 7 · quality scenarios +5 | — |

## Key design points
1. **Merge is a link; split restores exactly.** Claims never move, so split is closing one link. Identity itself is bitemporal: "who did we think this was on date K" is answerable.
2. **A merge can reveal conflicts, a split can dissolve them.** The detector re-runs on cluster changes, not only on claim changes.
3. **Conflicts and resolutions are known-at.** A resolution made on 10 May does not rewrite what decision-makers saw on 9 May.
4. **Detection sees everything; readers see only what they may.** Conflicts, review cases and cluster members are invisible unless the reader can see the underlying claims/entities — no existence leakage.
5. **Transitive safety:** a recorded NOT_A_MATCH prevents any chain of matches from joining the two entities.
6. **Matching quality is a gate, not a hope.** A ruleset cannot be activated below 95 % candidate recall and 60 % proposal precision on a labelled Arabic/English test set, including kunya, nasab chains and transliterations.

## Registers
RSK-021 added. HAP-09 evidence: SLC-04. Glossary +2.

## Gates
G0–G3 PASS · **G6-SLC-01, SLC-02, SLC-04 READY** · G6 release BLOCKED (remaining R1: SLC-03, 05, 06, 07, 08, 11, 12a)

## Next recommended session
**SLC-03 — Task lifecycle** (closes OQ-031..033) then **SLC-05 — Secured search & graph projections**, which consumes the events of SLC-02 and SLC-04.
