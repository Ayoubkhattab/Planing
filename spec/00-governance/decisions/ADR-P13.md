---
id: ADR-P13
type: adr
title: Identifiers
status: APPROVED_DELEGATED
wave: W3
deciders: HAP-04
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
blocked_by: []
corrects: []
verified_by:
- FIT-07
---

# ADR-P13: Identifiers

## Context and Problem
PRJ§12 يقترح <namespace>:<object_type>:<id> بصيغة غير قياسية.

## Considered Options
1. ULID داخلي + URN urn:<ns>:<type>:<id> + سجل إعادة توجيه بعد الدمج
2. الصيغة الحالية

## Initial Engineering Leaning (NOT a decision — V6 rule 75)
الخيار 1.

## Decision Outcome
**ULID internal id + URN `urn:<namespace>:<type>:<ulid>`** (namespace = platform or tenant namespace). External identifiers in `ExternalIdentifier` records with validity. After merges, identity is resolved through same-as links (ADR entity resolution), not by rewriting ids.

## Rationale
Sortable, globally unique, standard URN syntax.

## Consequences
- ✅ Merge/split without id rewrite

## Impact
- —

## Verified By
FIT-07

## Previously Blocked By
None — can be decided now.
