---
id: ADR-P04
type: adr
title: Tenant Isolation
status: APPROVED_DELEGATED
wave: W3
deciders: HAP-05
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
blocked_by:
- UNK-002
- UNK-004
- UNK-006
- UNK-018
corrects:
- CR-14
- CR-41
verified_by:
- QAS-SEC-001
- QAS-SCAL-003
- FIT-02
---

# ADR-P04: Tenant Isolation

## Context and Problem
PRJ§6 يعدد مستويات العزل دون آلية؛ PRJ§81 يقسم Schemas حسب السياق لا المستأجر.

## Considered Options
1. Row-Level Security في قاعدة مشتركة
2. Schema لكل مستأجر
3. قاعدة لكل مستأجر
4. هجين حسب التصنيف

## Initial Engineering Leaning (NOT a decision — V6 rule 75)
لا ترجيح قبل UNK-004 وUNK-018.

## W1 Input (delegated answers)
Q6,Q16,Q20 → هجين: عزل منطقي في النشر المشترك + خلايا/نشر مخصص للمستأجرين الكبار والسياديين والتصنيف الأعلى — يُعتمد رسمياً في W3.

## Decision Outcome
**Hybrid isolation: shared cells with layered logical isolation + dedicated cells.**
- **Shared cell (defense in depth):** `tenant_id` in every record and every partition key; database row-level security enforced as a second barrier; per-tenant encryption keys (envelope encryption); tenant-prefixed object storage paths with per-tenant keys; tenant label on every index document and event; per-tenant quotas.
- **Dedicated cell** is mandatory when any is true: sovereign deployment; tenant holds data at the top classification level of its scheme; tenant load > 20 % of cell capacity.
- **Promotion path:** a tenant can be moved from a shared to a dedicated cell by tenant-scoped export/import without code change.

## Rationale
W1 Q6, Q16, Q20; scale-ready via cells (SR-09) without paying for per-tenant databases at small scale.

## Consequences
- ✅ Cheap for small tenants
- ✅ Strong isolation for sensitive/large tenants
- ✅ Linear scale by adding cells
- ⚠️ Two isolation modes to test (mitigated: same release, same suite)

## Impact
- **cost:** proportional to usage
- **security:** two independent barriers in shared cells

## Verified By
QAS-SEC-001, QAS-SCAL-003, FIT-02

## Previously Blocked By
UNK-002, UNK-004, UNK-006, UNK-018
