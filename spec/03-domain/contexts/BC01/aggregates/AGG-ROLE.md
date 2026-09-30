---
id: AGG-ROLE
type: aggregate
title: Role
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
  - REQ-FND-014
  state_machine: SM-ROLE
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-ROLE — Role

**الغرض:** تعريف دور = مجموعة صلاحيات (action × resource type)  
**السياق:** BC01 · **المستوى:** T2 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-ROL-01** — the 15 platform roles (PRJ§45 actors) exist in every tenant and cannot be retired or edited
- **INV-ROL-02** — permissions are separate grants (View, Edit, Export, Share, Approve, Delete, Retain, Archive, command codes) — REQ-FND-014
- **INV-ROL-03** — permission changes to an ACTIVE role increment security_version of all its holders

## مكونات داخلية

- Permission (value object: action, resource_type)

## الحالات

- غير نهائية: DRAFT, ACTIVE
- نهائية: RETIRED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-ROL-DEFINE | DRAFT | code unique in tenant | EVT-ROL-DEFINED | ROLE_CODE_TAKEN |
| DRAFT, ACTIVE | CMD-ROL-SET-PERMISSIONS | (بلا تغيير) | permissions exist in catalog; system roles are locked; ACTIVE → new version | EVT-ROL-PERMISSIONS-CHANGED | SYSTEM_ROLE_LOCKED |
| DRAFT | CMD-ROL-ACTIVATE | ACTIVE | ≥ 1 permission | EVT-ROL-ACTIVATED | ROLE_EMPTY |
| ACTIVE | CMD-ROL-RETIRE | RETIRED | not a system role; no active assignments | EVT-ROL-RETIRED | ROLE_IN_USE |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-ROL-DEFINE | CMD-ROL-SET-PERMISSIONS | CMD-ROL-ACTIVATE | CMD-ROL-RETIRE |
|---|---|---|---|---|
| ∅ | → DRAFT | — | — | — |
| DRAFT | ✗ ROLE_INVALID_STATE_TRANSITION | → DRAFT | → ACTIVE | ✗ ROLE_INVALID_STATE_TRANSITION |
| ACTIVE | ✗ ROLE_INVALID_STATE_TRANSITION | → ACTIVE | ✗ ROLE_INVALID_STATE_TRANSITION | → RETIRED |
| RETIRED | ✗ ROLE_INVALID_STATE_TRANSITION | ✗ ROLE_INVALID_STATE_TRANSITION | ✗ ROLE_INVALID_STATE_TRANSITION | ✗ ROLE_INVALID_STATE_TRANSITION |

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
id: AGG-ROLE
bc: BC01
name: Role
tier: T2
purpose: تعريف دور = مجموعة صلاحيات (action × resource type)
states:
- DRAFT
- ACTIVE
- RETIRED
terminal:
- RETIRED
invariants:
- 'INV-ROL-01: the 15 platform roles (PRJ§45 actors) exist in every tenant and cannot
  be retired or edited'
- 'INV-ROL-02: permissions are separate grants (View, Edit, Export, Share, Approve,
  Delete, Retain, Archive, command codes) — REQ-FND-014'
- 'INV-ROL-03: permission changes to an ACTIVE role increment security_version of
  all its holders'
entities:
- 'Permission (value object: action, resource_type)'
requirements:
- REQ-FND-014
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-ROL-DEFINE
  to: DRAFT
  guard: code unique in tenant
  event: EVT-ROL-DEFINED
  guard_error: ROLE_CODE_TAKEN
- from:
  - DRAFT
  - ACTIVE
  command: CMD-ROL-SET-PERMISSIONS
  to: '='
  guard: permissions exist in catalog; system roles are locked; ACTIVE → new version
  event: EVT-ROL-PERMISSIONS-CHANGED
  guard_error: SYSTEM_ROLE_LOCKED
- from:
  - DRAFT
  command: CMD-ROL-ACTIVATE
  to: ACTIVE
  guard: ≥ 1 permission
  event: EVT-ROL-ACTIVATED
  guard_error: ROLE_EMPTY
- from:
  - ACTIVE
  command: CMD-ROL-RETIRE
  to: RETIRED
  guard: not a system role; no active assignments
  event: EVT-ROL-RETIRED
  guard_error: ROLE_IN_USE
```

</details>
