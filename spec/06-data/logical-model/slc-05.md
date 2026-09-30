---
id: LDM-SLC05
type: logical-data-model
title: Logical Data Model — SLC-05 (projection documents)
wave: W6
slice: SLC-05
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Logical Data Model — SLC-05

كل ما هنا **إسقاطات** قابلة لإعادة البناء (INV-PRJ-01)، مستقلة عن المحرك (ADR-P05).

| الوثيقة / الجدول | المفتاح | حقول | ملاحظات |
|---|---|---|---|
| EntityDoc | (projection_version, tenant, urn) | canonical_urn, type, labels, security_version, facts[] (nested), current_location_per_level? | facts: predicate, value_text_ar/en, value_norm, translit[], phonetic[], value_num, unit, geo, valid, labels, claim_urn |
| RealWorldEventDoc | (…, urn) | type, event_time(fuzzy), facts[] | — |
| ObservationDoc | (…, month, urn) | observed_at, geo, method, narrative forms, source_type, labels, state | VALIDATED only; monthly indices |
| TaskDoc | (…, urn) | title forms, state, assignee, due_at, plan_ref, labels | from SLC-03 |
| GraphNode | (…, urn) | type, display name (per visible facts at query), labels | — |
| GraphEdge | (…, urn) | type, source, target, valid, recorded, labels | from relationship + existence claim |
| projection_versions (BC07 store) | (tenant_group, kind, version) | state, schema_version, normalization_version, checkpoints(json), verification(json) | AGG-PROJECTION-VERSION |
| projection_inbox | (version, consumer, event_id) | processed_at | dedupe |
