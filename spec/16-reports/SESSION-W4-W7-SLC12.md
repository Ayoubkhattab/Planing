---
id: SESSION-SLC12
type: session-report
wave: W4–W7 (SLC-12, Release 2)
date: 2026-09-24
basis: V6§21.3
---

# SESSION REPORT — SLC-12 Products, Knowledge, Archive & Historical Reconstruction (R2)

**Result:** **DESIGN COMPLETE.** G6 held until the R1 pilot review (RSK-027).

## Produced (all counts computed from source)
| Output | Count |
|---|---|
| Aggregates: Product Template, Product Version, Distribution, Knowledge Object Version, Archive Package, Historical Reconstruction (BC06) | 6 · 19 invariants |
| Commands / queries / events | 29 / 8 / 42 |
| Specification: generation pipeline, distribution & watermarking, knowledge suggestion, BagIt/PREMIS-style packages, retrieval tiers, reconstruction sources and labels | 1 |
| OpenAPI | 37 operations — validated |
| Hand-written acceptance scenarios | 16 (+ generated matrix scenarios) · 5 properties |

## Key design points
1. **Products never exceed or hint at what is above their label:** every data binding runs as the author through declared queries, content above the label is dropped with no count or marker, and exclusions are kept only for audit.
2. **A product is a witness of its moment:** data is pinned at generation (known_at), so an approved product reproduces exactly what decision-makers saw.
3. **Every distributed copy is traceable** by visible and invisible per-recipient watermarks; unauthorized recipients are excluded before delivery.
4. **Knowledge is reusable and measured:** lessons must come from closed work with evidence; suggestions use explicit relationships to task types, plans and areas; reuse is counted for OUT-06. Policy knowledge never changes authorization.
5. **Archives are standard and verifiable:** BagIt packages with SHA-256 manifests, preservation-event metadata, originals plus preservation formats (PDF/A-2b, GeoTIFF/COG, GeoPackage), WORM storage, yearly fixity and replica repair.
6. **Historical reconstruction is deterministic and labelled** element by element — RECORDED, RECONSTRUCTED, INFERRED (with the rule), UNKNOWN — and runs with the requester's authority.

## Housekeeping
Property ids for this slice start at P-126 (P-121..P-125 belong to SLC-12a).

## Gates
R1: G6 READY (awaiting ratification) · R2: SLC-09, **SLC-12 DESIGN COMPLETE** (G6 held)

## Next recommended session
**SLC-10 — Grounded AI** (retrieval, context packages, drafting, extraction, translation, model lifecycle, tool registry, vector projection).
