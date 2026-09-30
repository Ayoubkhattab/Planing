---
id: SESSION-SLC10
type: session-report
wave: W4–W7 (SLC-10, Release 2)
date: 2026-09-24
basis: V6§21.3
---

# SESSION REPORT — SLC-10 Grounded AI (R2)

**Result:** **DESIGN COMPLETE.** G6 held until the R1 pilot review **and** a first model passing the evaluation thresholds on tenant data.

## Produced (counts computed from source)
| Output | Count |
|---|---|
| Aggregates: AI Request, AI Result, Model Version, AI Routing, AI Tool, Evaluation Suite (BC07) | 6 · 19 invariants |
| Commands / queries / events | 27 / 7 / 37 |
| Specification: pipeline, authorized hybrid retrieval, context packages, grounding verifier and insufficient-evidence path, guards, autonomy ceiling, serving | 1 |
| OpenAPI (`/api/v1/ai/…`) | 34 operations — validated |
| Hand-written acceptance scenarios | 18 · 6 properties |
| Technology additions | TD-18 vLLM (local inference), TD-19 OpenSearch k-NN (no new component) |

## Key design points
1. **The model sees only what the user sees:** hybrid retrieval runs as the user over the same labelled search facts, with pre-filtering and LabelCheck — the non-inference properties now cover AI retrieval (P-101).
2. **No answer without evidence:** low coverage stops before generation; a separate verifier model checks each statement against its citations; unsupported statements are dropped; if nothing remains, the result is "Insufficient Evidence".
3. **Retrieved text is data, never instructions:** tools are limited to the operation's list and validated arguments; no write tools exist in R2; no network egress; classified context never reaches external models.
4. **AI never changes state by itself:** extractions, drafts, translations-as-evidence and match suggestions become AI Results that a human accepts; accepted effects keep lineage to the request, context package and model version.
5. **Models earn production:** registration, evaluation against a versioned suite (citation ≥ 95 %, hallucination ≤ 2 %, insufficient-evidence recall ≥ 95 %, zero injection/exfiltration successes), approval by a different person, 10 % canary for 7 days, drift monitoring and rollback.
6. **Autonomy is capped by construction:** the routing schema cannot express AIL 5, and R2 routes stay ≤ AIL 3.

## Cross-slice change
CR-58: projection versions gain the `vector` kind (embedding model version is part of the projection version); SLC-05 regenerated.

## Gates
R1: G6 READY (awaiting ratification) · R2: SLC-09, SLC-12, **SLC-10 DESIGN COMPLETE** (G6 held)

## Next recommended session
**SLC-14 — Collection requirements & planning**, then SLC-15 (coordination & fusion) and SLC-16 (enterprise integrations).
