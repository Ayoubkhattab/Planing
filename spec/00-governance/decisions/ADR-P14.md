---
id: ADR-P14
type: adr
title: Reference Data Governance
status: APPROVED_DELEGATED
wave: W3
deciders: HAP-04
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
blocked_by: []
corrects:
- CR-19
verified_by: []
---

# ADR-P14: Reference Data Governance

## Context and Problem
لا إدارة لقوائم الرموز والبيانات المرجعية.

## Considered Options
1. كتالوج مرجعي بإصدارات ومالك لكل قائمة
2. قوائم مضمنة في كل سياق

## Initial Engineering Leaning (NOT a decision — V6 rule 75)
الخيار 1.

## Decision Outcome
**Reference Data Catalog** (`04-information/reference-data.md`): each code list has an owner context, version, effective time and extensibility rule. Platform lists can be extended by tenants but not modified. Historical data keeps the code-list version it was recorded with.

## Rationale
Semantic consistency (V5§49).

## Consequences
- ✅ Stable semantics

## Impact
- —

## Verified By
—

## Previously Blocked By
None — can be decided now.
