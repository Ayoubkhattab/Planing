---
id: ADR-P16
type: adr
title: Canonical CRS
status: APPROVED_DELEGATED
wave: W3
deciders: HAP-04
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
blocked_by: []
corrects:
- CR-12
verified_by:
- FIT-08
---

# ADR-P16: Canonical CRS

## Context and Problem
PRJ§4 requires CRS on geometry but no canonical reference system. Cross-source spatial queries need one.

## Considered Options
1. Store canonical WGS 84 (EPSG:4326) + original CRS and coordinates.
2. Store only original CRS, transform at query time.
3. Projected CRS per deployment region.

## W2 Input (delegated)
Option 1, as required by REQ-INF-029. Distance/area calculations use geodesic functions or a suitable projected CRS at computation time.

## Decision Outcome
**Option 1 — store canonical WGS 84 (EPSG:4326, lon/lat order) plus the original CRS and original coordinates as received.** Distance and area are computed with geodesic functions or a suitable projected CRS at computation time. Applied in `04-information/spatial-model.md` (`geometry` in EPSG:4326; `crs_original`, `coordinates_original` preserved; geometry without CRS or precision is rejected) and required by REQ-INF-029.

> Corrected by CR-73 (2026-09-30): this section still read "TBD — formal in W3" although the ADR was approved and the decision applied in W3.
