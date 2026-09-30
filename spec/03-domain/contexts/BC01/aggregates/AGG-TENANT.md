---
id: AGG-TENANT
type: aggregate
title: Tenant
wave: W4
slice: SLC-01
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC01
importance_tier: T2
personal_data: false
traces:
  satisfies:
  - REQ-FND-001
  - REQ-FND-003
  - REQ-FND-004
  - REQ-FND-018
  state_machine: SM-TENANT
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-TENANT — Tenant

**الغرض:** وحدة العزل العليا؛ تُربط بخلية واحدة  
**السياق:** BC01 · **المستوى:** T2 · **بيانات شخصية:** لا

> Provisioning is a saga orchestrated by BC01; each step idempotent and compensable.

## الثوابت (Invariants)

- **INV-TEN-01** — users of a tenant can authenticate only while the tenant is ACTIVE
- **INV-TEN-02** — a tenant is bound to exactly one cell at any time
- **INV-TEN-03** — cell_mode = dedicated if sovereign, or top classification level enabled, or load > 20 % of cell (ADR-P04)
- **INV-TEN-04** — namespace is unique across the platform and immutable
- **INV-TEN-05** — decommission cannot start while any legal hold is active

## مكونات داخلية

- TenantQuotas (value object)
- ProvisioningStep (value object list)

## الحالات

- غير نهائية: PROVISIONING, PROVISIONING_FAILED, ACTIVE, SUSPENDED, MIGRATING, DECOMMISSIONING
- نهائية: DECOMMISSIONED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-TEN-PROVISION | PROVISIONING | namespace unique; cell_mode valid for tenant profile (INV-TEN-03) | EVT-TEN-PROVISIONING-STARTED | TENANT_NAMESPACE_TAKEN |
| PROVISIONING | CMD-TEN-COMPLETE-PROVISIONING | ACTIVE | system; all provisioning steps confirmed (isolation, keys, scheme, roles, quotas, audit stream) | EVT-TEN-ACTIVATED | TENANT_PROVISIONING_INCOMPLETE |
| PROVISIONING | CMD-TEN-FAIL-PROVISIONING | PROVISIONING_FAILED | system; compensation completed | EVT-TEN-PROVISIONING-FAILED | — |
| PROVISIONING_FAILED | CMD-TEN-RETRY-PROVISIONING | PROVISIONING | actor = platform operator | EVT-TEN-PROVISIONING-STARTED | — |
| ACTIVE | CMD-TEN-SUSPEND | SUSPENDED | reason provided | EVT-TEN-SUSPENDED | REASON_REQUIRED |
| SUSPENDED | CMD-TEN-REACTIVATE | ACTIVE | — | EVT-TEN-REACTIVATED | — |
| ACTIVE | CMD-TEN-START-CELL-MIGRATION | MIGRATING | target cell exists and has capacity | EVT-TEN-MIGRATION-STARTED | CELL_UNAVAILABLE |
| MIGRATING | CMD-TEN-COMPLETE-CELL-MIGRATION | ACTIVE | system; export/import reconciled | EVT-TEN-MIGRATED | MIGRATION_NOT_RECONCILED |
| ACTIVE, SUSPENDED | CMD-TEN-START-DECOMMISSION | DECOMMISSIONING | no active legal hold (BC08 query); two-person approval | EVT-TEN-DECOMMISSION-STARTED | LEGAL_HOLD_ACTIVE |
| DECOMMISSIONING | CMD-TEN-COMPLETE-DECOMMISSION | DECOMMISSIONED | system; keys destroyed, stores removed | EVT-TEN-DECOMMISSIONED | — |
| ACTIVE, SUSPENDED | CMD-TEN-UPDATE-QUOTAS | (بلا تغيير) | quotas ≤ cell capacity | EVT-TEN-QUOTAS-UPDATED | QUOTA_EXCEEDS_CAPACITY |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-TEN-PROVISION | CMD-TEN-COMPLETE-PROVISIONING | CMD-TEN-FAIL-PROVISIONING | CMD-TEN-RETRY-PROVISIONING | CMD-TEN-SUSPEND | CMD-TEN-REACTIVATE | CMD-TEN-START-CELL-MIGRATION | CMD-TEN-COMPLETE-CELL-MIGRATION | CMD-TEN-START-DECOMMISSION | CMD-TEN-COMPLETE-DECOMMISSION | CMD-TEN-UPDATE-QUOTAS |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ∅ | → PROVISIONING | — | — | — | — | — | — | — | — | — | — |
| PROVISIONING | ✗ TENANT_INVALID_STATE_TRANSITION | → ACTIVE | → PROVISIONING_FAILED | ✗ TENANT_INVALID_STATE_TRANSITION | ✗ TENANT_INVALID_STATE_TRANSITION | ✗ TENANT_INVALID_STATE_TRANSITION | ✗ TENANT_INVALID_STATE_TRANSITION | ✗ TENANT_INVALID_STATE_TRANSITION | ✗ TENANT_INVALID_STATE_TRANSITION | ✗ TENANT_INVALID_STATE_TRANSITION | ✗ TENANT_INVALID_STATE_TRANSITION |
| PROVISIONING_FAILED | ✗ TENANT_INVALID_STATE_TRANSITION | ✗ TENANT_INVALID_STATE_TRANSITION | ✗ TENANT_INVALID_STATE_TRANSITION | → PROVISIONING | ✗ TENANT_INVALID_STATE_TRANSITION | ✗ TENANT_INVALID_STATE_TRANSITION | ✗ TENANT_INVALID_STATE_TRANSITION | ✗ TENANT_INVALID_STATE_TRANSITION | ✗ TENANT_INVALID_STATE_TRANSITION | ✗ TENANT_INVALID_STATE_TRANSITION | ✗ TENANT_INVALID_STATE_TRANSITION |
| ACTIVE | ✗ TENANT_INVALID_STATE_TRANSITION | ✗ TENANT_INVALID_STATE_TRANSITION | ✗ TENANT_INVALID_STATE_TRANSITION | ✗ TENANT_INVALID_STATE_TRANSITION | → SUSPENDED | ✗ TENANT_INVALID_STATE_TRANSITION | → MIGRATING | ✗ TENANT_INVALID_STATE_TRANSITION | → DECOMMISSIONING | ✗ TENANT_INVALID_STATE_TRANSITION | → ACTIVE |
| SUSPENDED | ✗ TENANT_INVALID_STATE_TRANSITION | ✗ TENANT_INVALID_STATE_TRANSITION | ✗ TENANT_INVALID_STATE_TRANSITION | ✗ TENANT_INVALID_STATE_TRANSITION | ✗ TENANT_INVALID_STATE_TRANSITION | → ACTIVE | ✗ TENANT_INVALID_STATE_TRANSITION | ✗ TENANT_INVALID_STATE_TRANSITION | → DECOMMISSIONING | ✗ TENANT_INVALID_STATE_TRANSITION | → SUSPENDED |
| MIGRATING | ✗ TENANT_INVALID_STATE_TRANSITION | ✗ TENANT_INVALID_STATE_TRANSITION | ✗ TENANT_INVALID_STATE_TRANSITION | ✗ TENANT_INVALID_STATE_TRANSITION | ✗ TENANT_INVALID_STATE_TRANSITION | ✗ TENANT_INVALID_STATE_TRANSITION | ✗ TENANT_INVALID_STATE_TRANSITION | → ACTIVE | ✗ TENANT_INVALID_STATE_TRANSITION | ✗ TENANT_INVALID_STATE_TRANSITION | ✗ TENANT_INVALID_STATE_TRANSITION |
| DECOMMISSIONING | ✗ TENANT_INVALID_STATE_TRANSITION | ✗ TENANT_INVALID_STATE_TRANSITION | ✗ TENANT_INVALID_STATE_TRANSITION | ✗ TENANT_INVALID_STATE_TRANSITION | ✗ TENANT_INVALID_STATE_TRANSITION | ✗ TENANT_INVALID_STATE_TRANSITION | ✗ TENANT_INVALID_STATE_TRANSITION | ✗ TENANT_INVALID_STATE_TRANSITION | ✗ TENANT_INVALID_STATE_TRANSITION | → DECOMMISSIONED | ✗ TENANT_INVALID_STATE_TRANSITION |
| DECOMMISSIONED | ✗ TENANT_INVALID_STATE_TRANSITION | ✗ TENANT_INVALID_STATE_TRANSITION | ✗ TENANT_INVALID_STATE_TRANSITION | ✗ TENANT_INVALID_STATE_TRANSITION | ✗ TENANT_INVALID_STATE_TRANSITION | ✗ TENANT_INVALID_STATE_TRANSITION | ✗ TENANT_INVALID_STATE_TRANSITION | ✗ TENANT_INVALID_STATE_TRANSITION | ✗ TENANT_INVALID_STATE_TRANSITION | ✗ TENANT_INVALID_STATE_TRANSITION | ✗ TENANT_INVALID_STATE_TRANSITION |

## التزامن وعدم التكرار

- Optimistic concurrency: `If-Match: <version>`؛ عدم التطابق → `VERSION_CONFLICT` (HTTP 409) دون تغيير.
- كل أمر يحمل `Idempotency-Key`؛ التكرار يعيد النتيجة الأصلية؛ نفس المفتاح بحمولة مختلفة → `IDEMPOTENCY_KEY_REUSED` (HTTP 422).
- الأوامر التي تبدأ بـ `SYS:` يطلقها المجدول بهوية عبء عمل، وتخضع لنفس الثوابت.

## الحفظ

- State + history (إصدار غير قابل للتعديل لكل تغيير، ADR-P02) + outbox + audit outbox في نفس المعاملة (FIT-04).
- النموذج المنطقي: `06-data/logical-model/slc-01.md`.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
id: AGG-TENANT
bc: BC01
name: Tenant
tier: T2
purpose: وحدة العزل العليا؛ تُربط بخلية واحدة
states:
- PROVISIONING
- PROVISIONING_FAILED
- ACTIVE
- SUSPENDED
- MIGRATING
- DECOMMISSIONING
- DECOMMISSIONED
terminal:
- DECOMMISSIONED
invariants:
- 'INV-TEN-01: users of a tenant can authenticate only while the tenant is ACTIVE'
- 'INV-TEN-02: a tenant is bound to exactly one cell at any time'
- 'INV-TEN-03: cell_mode = dedicated if sovereign, or top classification level enabled,
  or load > 20 % of cell (ADR-P04)'
- 'INV-TEN-04: namespace is unique across the platform and immutable'
- 'INV-TEN-05: decommission cannot start while any legal hold is active'
entities:
- TenantQuotas (value object)
- ProvisioningStep (value object list)
requirements:
- REQ-FND-001
- REQ-FND-003
- REQ-FND-004
- REQ-FND-018
notes: Provisioning is a saga orchestrated by BC01; each step idempotent and compensable.
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-TEN-PROVISION
  to: PROVISIONING
  guard: namespace unique; cell_mode valid for tenant profile (INV-TEN-03)
  event: EVT-TEN-PROVISIONING-STARTED
  guard_error: TENANT_NAMESPACE_TAKEN
- from:
  - PROVISIONING
  command: CMD-TEN-COMPLETE-PROVISIONING
  to: ACTIVE
  guard: system; all provisioning steps confirmed (isolation, keys, scheme, roles,
    quotas, audit stream)
  event: EVT-TEN-ACTIVATED
  guard_error: TENANT_PROVISIONING_INCOMPLETE
- from:
  - PROVISIONING
  command: CMD-TEN-FAIL-PROVISIONING
  to: PROVISIONING_FAILED
  guard: system; compensation completed
  event: EVT-TEN-PROVISIONING-FAILED
  guard_error: null
- from:
  - PROVISIONING_FAILED
  command: CMD-TEN-RETRY-PROVISIONING
  to: PROVISIONING
  guard: actor = platform operator
  event: EVT-TEN-PROVISIONING-STARTED
  guard_error: null
- from:
  - ACTIVE
  command: CMD-TEN-SUSPEND
  to: SUSPENDED
  guard: reason provided
  event: EVT-TEN-SUSPENDED
  guard_error: REASON_REQUIRED
- from:
  - SUSPENDED
  command: CMD-TEN-REACTIVATE
  to: ACTIVE
  guard: —
  event: EVT-TEN-REACTIVATED
  guard_error: null
- from:
  - ACTIVE
  command: CMD-TEN-START-CELL-MIGRATION
  to: MIGRATING
  guard: target cell exists and has capacity
  event: EVT-TEN-MIGRATION-STARTED
  guard_error: CELL_UNAVAILABLE
- from:
  - MIGRATING
  command: CMD-TEN-COMPLETE-CELL-MIGRATION
  to: ACTIVE
  guard: system; export/import reconciled
  event: EVT-TEN-MIGRATED
  guard_error: MIGRATION_NOT_RECONCILED
- from:
  - ACTIVE
  - SUSPENDED
  command: CMD-TEN-START-DECOMMISSION
  to: DECOMMISSIONING
  guard: no active legal hold (BC08 query); two-person approval
  event: EVT-TEN-DECOMMISSION-STARTED
  guard_error: LEGAL_HOLD_ACTIVE
- from:
  - DECOMMISSIONING
  command: CMD-TEN-COMPLETE-DECOMMISSION
  to: DECOMMISSIONED
  guard: system; keys destroyed, stores removed
  event: EVT-TEN-DECOMMISSIONED
  guard_error: null
- from:
  - ACTIVE
  - SUSPENDED
  command: CMD-TEN-UPDATE-QUOTAS
  to: '='
  guard: quotas ≤ cell capacity
  event: EVT-TEN-QUOTAS-UPDATED
  guard_error: QUOTA_EXCEEDS_CAPACITY
```

</details>
