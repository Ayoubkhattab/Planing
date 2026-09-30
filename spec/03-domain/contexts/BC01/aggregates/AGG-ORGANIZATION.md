---
id: AGG-ORGANIZATION
type: aggregate
title: Organization (with unit tree)
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
  - REQ-FND-002
  state_machine: SM-ORGANIZATION
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-ORGANIZATION — Organization (with unit tree)

**الغرض:** مؤسسة داخل مستأجر مع شجرة وحداتها  
**السياق:** BC01 · **المستوى:** T2 · **بيانات شخصية:** لا

> Unit-level lifecycle: ACTIVE → INACTIVE via CMD-ORG-DEACTIVATE-UNIT; reactivation via CMD-ORG-ADD-UNIT is not allowed (create new unit) to keep history clear.

## الثوابت (Invariants)

- **INV-ORG-01** — the unit tree is acyclic with exactly one root
- **INV-ORG-02** — sibling unit names are unique (after language-model normalization)
- **INV-ORG-03** — an inactive unit cannot receive children, assignments or grants
- **INV-ORG-04** — unit count per organization ≤ 5,000 (aggregate size bound; larger orgs split into organizations)

## مكونات داخلية

- OrgUnit (entity, with own state ACTIVE/INACTIVE)

## الحالات

- غير نهائية: ACTIVE, INACTIVE
- نهائية: — (perpetual)
- قابلية الوصول لحالة نهائية (SL-06): **EXEMPT: Organizations are kept for institutional history; they become INACTIVE, never deleted (SL-06 exemption, justified)**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-ORG-CREATE | ACTIVE | tenant ACTIVE; name unique in tenant; creates root unit | EVT-ORG-CREATED | ORG_NAME_TAKEN |
| ACTIVE | CMD-ORG-RENAME | (بلا تغيير) | name unique in tenant | EVT-ORG-RENAMED | ORG_NAME_TAKEN |
| ACTIVE | CMD-ORG-ADD-UNIT | (بلا تغيير) | parent unit ACTIVE; sibling name unique | EVT-ORG-UNIT-ADDED | ORG_UNIT_INVALID_PARENT |
| ACTIVE | CMD-ORG-RENAME-UNIT | (بلا تغيير) | sibling name unique | EVT-ORG-UNIT-RENAMED | ORG_UNIT_NAME_TAKEN |
| ACTIVE | CMD-ORG-MOVE-UNIT | (بلا تغيير) | new parent ACTIVE, same org, not a descendant (no cycle); root cannot move | EVT-ORG-UNIT-MOVED | ORG_UNIT_CYCLE |
| ACTIVE | CMD-ORG-DEACTIVATE-UNIT | (بلا تغيير) | no active children; no active role assignments, grants or clearances scoped only to it (BC01 query) | EVT-ORG-UNIT-DEACTIVATED | ORG_UNIT_IN_USE |
| ACTIVE | CMD-ORG-DEACTIVATE | INACTIVE | all non-root units inactive; no active assignments | EVT-ORG-DEACTIVATED | ORG_IN_USE |
| INACTIVE | CMD-ORG-REACTIVATE | ACTIVE | tenant ACTIVE | EVT-ORG-REACTIVATED | — |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-ORG-CREATE | CMD-ORG-RENAME | CMD-ORG-ADD-UNIT | CMD-ORG-RENAME-UNIT | CMD-ORG-MOVE-UNIT | CMD-ORG-DEACTIVATE-UNIT | CMD-ORG-DEACTIVATE | CMD-ORG-REACTIVATE |
|---|---|---|---|---|---|---|---|---|
| ∅ | → ACTIVE | — | — | — | — | — | — | — |
| ACTIVE | ✗ ORGANIZATION_INVALID_STATE_TRANSITION | → ACTIVE | → ACTIVE | → ACTIVE | → ACTIVE | → ACTIVE | → INACTIVE | ✗ ORGANIZATION_INVALID_STATE_TRANSITION |
| INACTIVE | ✗ ORGANIZATION_INVALID_STATE_TRANSITION | ✗ ORGANIZATION_INVALID_STATE_TRANSITION | ✗ ORGANIZATION_INVALID_STATE_TRANSITION | ✗ ORGANIZATION_INVALID_STATE_TRANSITION | ✗ ORGANIZATION_INVALID_STATE_TRANSITION | ✗ ORGANIZATION_INVALID_STATE_TRANSITION | ✗ ORGANIZATION_INVALID_STATE_TRANSITION | → ACTIVE |

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
id: AGG-ORGANIZATION
bc: BC01
name: Organization (with unit tree)
tier: T2
purpose: مؤسسة داخل مستأجر مع شجرة وحداتها
states:
- ACTIVE
- INACTIVE
terminal: []
invariants:
- 'INV-ORG-01: the unit tree is acyclic with exactly one root'
- 'INV-ORG-02: sibling unit names are unique (after language-model normalization)'
- 'INV-ORG-03: an inactive unit cannot receive children, assignments or grants'
- 'INV-ORG-04: unit count per organization ≤ 5,000 (aggregate size bound; larger orgs
  split into organizations)'
entities:
- OrgUnit (entity, with own state ACTIVE/INACTIVE)
requirements:
- REQ-FND-002
notes: 'Unit-level lifecycle: ACTIVE → INACTIVE via CMD-ORG-DEACTIVATE-UNIT; reactivation
  via CMD-ORG-ADD-UNIT is not allowed (create new unit) to keep history clear.'
personal_data: false
reachability: 'EXEMPT: Organizations are kept for institutional history; they become
  INACTIVE, never deleted (SL-06 exemption, justified)'
transitions:
- from: ∅
  command: CMD-ORG-CREATE
  to: ACTIVE
  guard: tenant ACTIVE; name unique in tenant; creates root unit
  event: EVT-ORG-CREATED
  guard_error: ORG_NAME_TAKEN
- from:
  - ACTIVE
  command: CMD-ORG-RENAME
  to: '='
  guard: name unique in tenant
  event: EVT-ORG-RENAMED
  guard_error: ORG_NAME_TAKEN
- from:
  - ACTIVE
  command: CMD-ORG-ADD-UNIT
  to: '='
  guard: parent unit ACTIVE; sibling name unique
  event: EVT-ORG-UNIT-ADDED
  guard_error: ORG_UNIT_INVALID_PARENT
- from:
  - ACTIVE
  command: CMD-ORG-RENAME-UNIT
  to: '='
  guard: sibling name unique
  event: EVT-ORG-UNIT-RENAMED
  guard_error: ORG_UNIT_NAME_TAKEN
- from:
  - ACTIVE
  command: CMD-ORG-MOVE-UNIT
  to: '='
  guard: new parent ACTIVE, same org, not a descendant (no cycle); root cannot move
  event: EVT-ORG-UNIT-MOVED
  guard_error: ORG_UNIT_CYCLE
- from:
  - ACTIVE
  command: CMD-ORG-DEACTIVATE-UNIT
  to: '='
  guard: no active children; no active role assignments, grants or clearances scoped
    only to it (BC01 query)
  event: EVT-ORG-UNIT-DEACTIVATED
  guard_error: ORG_UNIT_IN_USE
- from:
  - ACTIVE
  command: CMD-ORG-DEACTIVATE
  to: INACTIVE
  guard: all non-root units inactive; no active assignments
  event: EVT-ORG-DEACTIVATED
  guard_error: ORG_IN_USE
- from:
  - INACTIVE
  command: CMD-ORG-REACTIVATE
  to: ACTIVE
  guard: tenant ACTIVE
  event: EVT-ORG-REACTIVATED
  guard_error: null
```

</details>
