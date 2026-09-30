---
id: SESSION-W8
type: session-report
wave: W8 — Solution & Technology Decisions
date: 2026-09-24
basis: V6§10.2 W8, V6§21.3
---

# SESSION REPORT — W8 Solution & Technology Decisions

**Result:** **G4 PASS (delegated) · G5 PASS (delegated)** — conditional on pilot performance tests and licence review before G8.

## Produced
| Artifact | Content |
|---|---|
| `12-solution/technology-decisions.md` | 17 technology decisions, each with options, evidence (WL/QAS/spec), licence and reversal trigger |
| `00-governance/decisions/ADR-P05.md` | approved (delegated): evidence-based footprint |
| `12-solution/c4-context.md`, `c4-containers.md` | C4 views (Mermaid) |
| `12-solution/deployment-units.md` | 13 deployment units with V5§97 justification and service tier |
| `12-solution/cell-architecture.md` | cell profiles, capacity sizing (estimates), default-deny egress |
| `07-quality/performance-test-strategy.md` | load mix, 8 test types mapped to QAS |
| `07-quality/cost-model.md` | cost drivers, allocation formula, per-operation indicators — no invented prices |
| `09-reliability/dr-and-continuity.md` | tier per unit, protection per store, DR, continuity |
| `12-solution/ui-architecture.md` | web + mobile, bilingual RTL, Hijri display, accessibility |
| `12-solution/release-configuration-migration.md` | one bundle for all cell profiles, GitOps, forward-only migrations |

## The footprint, and why
| Kept simple | Because |
|---|---|
| PostgreSQL/PostGIS as the only operational store | bitemporal ranges, exclusion constraints, RLS, spatial, partitioning cover all contexts |
| **No graph database** (PRJ proposed Neo4j) | ~20 graph queries/s at depth ≤ 3 — bounded recursive SQL suffices; reversal trigger defined |
| No workflow engine | timers in PostgreSQL buckets |

| Added | Evidence |
|---|---|
| OpenSearch | fact-level filtering before counting/faceting is a **functional** requirement of non-inference, plus 500 queries/s |
| Kafka (KRaft) | 50,000 events/s bursts, replayable multi-consumer streams, per-key ordering in every contract |
| Kubernetes | cells, one bundle for three profiles, air-gapped upgrade with rollback, operators for 8 stateful services |
| OPA, OpenBao + HSM, Kueue, Harbor, Zarf | policy at 10,000 decisions/s with partial evaluation; millions of keys; fair compute; signed images; offline bundles |

This closes CR-21: the original document chose technology before workloads; now every component traces to evidence, and two of its choices (Neo4j, Redis) were dropped.

## Findings during W8
- **CR-54:** search indexes were "rebuildable", but a full rebuild (≤ 24 h) cannot meet the 4-hour RTO of their tier → 15-minute OpenSearch snapshots restored in DR plus catch-up from Kafka.
- **Global coverage:** all 114 R1 requirements are now traced (slices + platform trace).
- **RSK-026:** 8 stateful services per cell is a real operational load for a small team; the operations team size (UNK-012) must be confirmed before G8; NATS JetStream is the documented lighter alternative to Kafka.

## Honest limits
- Sizing and cost are **models**, not measurements; the performance tests and pilot recalibrate them.
- Licences: MinIO and Grafana (AGPL) and HSM terms need legal review (DEP-HUM-004).

## Gates
G0–G3 PASS · **G4 PASS · G5 PASS** (delegated, conditional) · G6-SLC all R1 READY · **G6 release: W9 remaining**

## Next recommended session
**W9 — Baseline consolidation:** full consistency report, anti-pattern re-assessment, ATAM-lite for the whole release, generated traceability matrices, Engineering Baseline, Evolution Roadmap (R2/R3), and the G6 verdict for R1 with the list of conditions for G7/G8.
