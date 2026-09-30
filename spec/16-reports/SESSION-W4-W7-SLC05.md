---
id: SESSION-SLC05
type: session-report
wave: W4–W7 (SLC-05)
date: 2026-09-24
basis: V6§21.3
---

# SESSION REPORT — SLC-05 Secured Search & Graph Projections

**Result:** **G6-SLC-05 READY (delegated), conditional** — the search engine chosen in W8 must satisfy the capability list in SPEC-DISCOVERY §8. Everything specified here is engine-independent.

## Produced
| Output | Count |
|---|---|
| Discovery architecture: pipeline (notify + fetch), document model with **search facts**, normative query semantics (search, suggest, facets, neighbourhood, paths), inference rules per channel, Arabic analysis, partitioning, degradation, engine capability list | 1 spec |
| Aggregate: Projection Version (blue/green rebuilds) | 1 · 4 invariants |
| OpenAPI: 10 operations with detailed Search/Graph schemas + **LabelCheck OHS contract** for every owning context — validated | — |
| Acceptance: 24 generated + 21 scenarios · **formal non-inference properties P-51..P-56** | — |
| Threats 8 · failure modes 5 · observability 7 · quality scenarios +3 | — |
| New register: `12-solution/w8-inputs.md` collecting capability and workload evidence for ADR-P05 | 1 |

## Key design points
1. **Non-inference is defined formally:** for any user, adding hidden data must not change any output — results, order, counts, facets, suggestions, graph neighbourhoods, paths or truncation flags (P-51..P-53). This turns a security intention into a property test.
2. **Index facts, not flattened values.** Each current claim is indexed with its own label inside the entity document; queries match only visible facts. A visible entity can never be found through the value of a hidden claim — the most dangerous inference channel.
3. **Revocation beats index lag** through a batched LabelCheck to the owning context for each returned page (CR-47 refines ADR-P06), keeping ownership intact.
4. **Graph traversal filters before expanding;** a path through a hidden node or edge simply does not exist for that reader.
5. **Health-based completeness signal:** when an owner is unavailable, its results are dropped and the partial flag is driven by service health, never by whether hidden hits existed.
6. **Blue/green projection versions** make normalization or schema changes safe and keep search available during rebuilds.

## Registers
CR-47 applied (ADR-P06 amended) · RSK-022 added · HAP-09 evidence: SLC-05 (conditional) · glossary +3 · W8 input register created.

## Gates
G0–G3 PASS · **G6-SLC-01..05 READY** (SLC-05 conditional on ADR-P05) · G6 release BLOCKED (remaining R1: SLC-06, 07, 08, 11, 12a)

## Next recommended session
**SLC-06 — Situation, Alerts & Notifications** (includes the common operational picture, secured map tiles per ADR-P12, and the notification service that SLC-03 already depends on).
