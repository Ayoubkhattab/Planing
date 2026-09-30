---
id: ADR-P12
type: adr
title: Map Serving & Tile Security
status: APPROVED_DELEGATED
wave: W3
deciders: HAP-05
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
blocked_by:
- WL-03
- UNK-010
corrects:
- CR-12
verified_by:
- QAS-SEC-004
- QAS-PERF-007
---

# ADR-P12: Map Serving & Tile Security

## Context and Problem
لا خدمة خرائط ولا Tiles ولا معايير OGC في PRJ.

## Considered Options
1. Tiles مخصصة لكل مستوى صلاحية
2. توليد عند الطلب دون Cache مشترك

## Initial Engineering Leaning (NOT a decision — V6 rule 75)
يُحسم بعد WL-03.

## W1 Input (delegated answers)
Q25 → OGC API Tiles/Features — يُعتمد رسمياً في W3.

## Decision Outcome
**Tiles and features are generated per security scope.** External interfaces: OGC API Features and Tiles; WMS/WFS for legacy import. Raster stored as COG. Unclassified base layers may be shared-cached; all other layers use scope-keyed cache (ADR-P06). Rendering engine selected in W8.

## Rationale
W1 Q25; A21.

## Consequences
- ✅ Standards-based
- ✅ No cross-scope leakage
- ⚠️ Lower cache hit rate for classified layers

## Impact
- **performance:** QAS-PERF-007 validated in W5

## Verified By
QAS-SEC-004, QAS-PERF-007

## Previously Blocked By
WL-03, UNK-010
