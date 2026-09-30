---
id: AGG-ASSET
type: aggregate
title: Asset
wave: W4
slice: SLC-09
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC05
importance_tier: T2 (location as T1 claims on the linked entity)
personal_data: false
traces:
  satisfies:
  - REQ-RES-001
  - REQ-RES-002
  - REQ-RES-003
  - REQ-RES-005
  state_machine: SM-ASSET
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-ASSET — Asset

**الغرض:** أصل مادي بملكية وحيازة وحالة وقدرات وشهادات وصيانة  
**السياق:** BC05 · **المستوى:** T2 (location as T1 claims on the linked entity) · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-AST-01** — available(asset, window) ⇔ IN_SERVICE ∧ required certifications valid throughout window ∧ no overlapping maintenance window, CONFIRMED/HELD reservation or ACTIVE assignment (REQ-RES-003/004/014)
- **INV-AST-02** — custody chain is gapless; each transfer by the current holder or custodian authority (REQ-RES-002)
- **INV-AST-03** — location lives as bitemporal claims on the linked information entity, never as a column (REQ-RES-005)
- **INV-AST-04** — an expired certification makes the asset unavailable for new assignments from that instant, evaluated at read time

## مكونات داخلية

- Certification
- CustodyEntry
- Capability (code, level)

## الحالات

- غير نهائية: IN_SERVICE, UNSERVICEABLE, UNDER_MAINTENANCE, LOST
- نهائية: DISPOSED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-AST-REGISTER | IN_SERVICE | type in RD-ASSET-TYPES; owner org; custody holder ACTIVE; linked information entity (entity_type asset-ref) created or referenced in BC02; capabilities; label | EVT-AST-REGISTERED | ASSET_INVALID |
| IN_SERVICE, UNSERVICEABLE, UNDER_MAINTENANCE | CMD-AST-UPDATE-CONDITION | (بلا تغيير) | condition grade in RD-CONDITION-GRADES; inspector; unserviceable grades require CMD-AST-MARK-UNSERVICEABLE | EVT-AST-CONDITION-UPDATED | CONDITION_INVALID |
| IN_SERVICE | CMD-AST-MARK-UNSERVICEABLE | UNSERVICEABLE | reason; active assignments are notified; future reservations flagged | EVT-AST-UNSERVICEABLE | REASON_REQUIRED |
| IN_SERVICE, UNSERVICEABLE | CMD-AST-START-MAINTENANCE | UNDER_MAINTENANCE | maintenance order IN_PROGRESS for this asset | EVT-AST-MAINTENANCE-STARTED | MAINTENANCE_ORDER_REQUIRED |
| UNDER_MAINTENANCE | CMD-AST-RETURN-TO-SERVICE | IN_SERVICE | maintenance order COMPLETED; condition serviceable; required certifications valid | EVT-AST-RETURNED-TO-SERVICE | ASSET_NOT_SERVICEABLE |
| UNDER_MAINTENANCE | CMD-AST-FAIL-MAINTENANCE | UNSERVICEABLE | maintenance order COMPLETED with outcome failed; reason | EVT-AST-UNSERVICEABLE | REASON_REQUIRED |
| IN_SERVICE, UNSERVICEABLE, UNDER_MAINTENANCE | CMD-AST-TRANSFER-CUSTODY | (بلا تغيير) | actor is current holder or custodian authority; new holder ACTIVE in scope; gapless chain | EVT-AST-CUSTODY-TRANSFERRED | CUSTODY_INVALID |
| IN_SERVICE, UNSERVICEABLE, UNDER_MAINTENANCE | CMD-AST-SET-CERTIFICATION | (بلا تغيير) | certification code, issuer, valid_from/to; evidence | EVT-AST-CERTIFICATION-SET | CERTIFICATION_INVALID |
| IN_SERVICE, UNSERVICEABLE | CMD-AST-REPORT-LOST | LOST | reason; active assignments ended; reservations cancelled | EVT-AST-REPORTED-LOST | REASON_REQUIRED |
| LOST | CMD-AST-RECOVER | UNSERVICEABLE | found; inspection required before service | EVT-AST-RECOVERED | — |
| UNSERVICEABLE, LOST | CMD-AST-DISPOSE | DISPOSED | disposal authority (decision type asset-disposal); no active reservation or assignment; no legal hold | EVT-AST-DISPOSED | AUTHORITY_REQUIRED |
| IN_SERVICE, UNSERVICEABLE, UNDER_MAINTENANCE, LOST | CMD-AST-RECLASSIFY | (بلا تغيير) | authority per policy | EVT-AST-RECLASSIFIED | CLASSIFICATION_CHANGE_NOT_AUTHORIZED |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-AST-REGISTER | CMD-AST-UPDATE-CONDITION | CMD-AST-MARK-UNSERVICEABLE | CMD-AST-START-MAINTENANCE | CMD-AST-RETURN-TO-SERVICE | CMD-AST-FAIL-MAINTENANCE | CMD-AST-TRANSFER-CUSTODY | CMD-AST-SET-CERTIFICATION | CMD-AST-REPORT-LOST | CMD-AST-RECOVER | CMD-AST-DISPOSE | CMD-AST-RECLASSIFY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ∅ | → IN_SERVICE | — | — | — | — | — | — | — | — | — | — | — |
| IN_SERVICE | ✗ ASSET_INVALID_STATE_TRANSITION | → IN_SERVICE | → UNSERVICEABLE | → UNDER_MAINTENANCE | ✗ ASSET_INVALID_STATE_TRANSITION | ✗ ASSET_INVALID_STATE_TRANSITION | → IN_SERVICE | → IN_SERVICE | → LOST | ✗ ASSET_INVALID_STATE_TRANSITION | ✗ ASSET_INVALID_STATE_TRANSITION | → IN_SERVICE |
| UNSERVICEABLE | ✗ ASSET_INVALID_STATE_TRANSITION | → UNSERVICEABLE | ✗ ASSET_INVALID_STATE_TRANSITION | → UNDER_MAINTENANCE | ✗ ASSET_INVALID_STATE_TRANSITION | ✗ ASSET_INVALID_STATE_TRANSITION | → UNSERVICEABLE | → UNSERVICEABLE | → LOST | ✗ ASSET_INVALID_STATE_TRANSITION | → DISPOSED | → UNSERVICEABLE |
| UNDER_MAINTENANCE | ✗ ASSET_INVALID_STATE_TRANSITION | → UNDER_MAINTENANCE | ✗ ASSET_INVALID_STATE_TRANSITION | ✗ ASSET_INVALID_STATE_TRANSITION | → IN_SERVICE | → UNSERVICEABLE | → UNDER_MAINTENANCE | → UNDER_MAINTENANCE | ✗ ASSET_INVALID_STATE_TRANSITION | ✗ ASSET_INVALID_STATE_TRANSITION | ✗ ASSET_INVALID_STATE_TRANSITION | → UNDER_MAINTENANCE |
| LOST | ✗ ASSET_INVALID_STATE_TRANSITION | ✗ ASSET_INVALID_STATE_TRANSITION | ✗ ASSET_INVALID_STATE_TRANSITION | ✗ ASSET_INVALID_STATE_TRANSITION | ✗ ASSET_INVALID_STATE_TRANSITION | ✗ ASSET_INVALID_STATE_TRANSITION | ✗ ASSET_INVALID_STATE_TRANSITION | ✗ ASSET_INVALID_STATE_TRANSITION | ✗ ASSET_INVALID_STATE_TRANSITION | → UNSERVICEABLE | → DISPOSED | → LOST |
| DISPOSED | ✗ ASSET_INVALID_STATE_TRANSITION | ✗ ASSET_INVALID_STATE_TRANSITION | ✗ ASSET_INVALID_STATE_TRANSITION | ✗ ASSET_INVALID_STATE_TRANSITION | ✗ ASSET_INVALID_STATE_TRANSITION | ✗ ASSET_INVALID_STATE_TRANSITION | ✗ ASSET_INVALID_STATE_TRANSITION | ✗ ASSET_INVALID_STATE_TRANSITION | ✗ ASSET_INVALID_STATE_TRANSITION | ✗ ASSET_INVALID_STATE_TRANSITION | ✗ ASSET_INVALID_STATE_TRANSITION | ✗ ASSET_INVALID_STATE_TRANSITION |

## التزامن وعدم التكرار

- Optimistic concurrency: `If-Match: <version>`؛ عدم التطابق → `VERSION_CONFLICT` (HTTP 409) دون تغيير.
- كل أمر يحمل `Idempotency-Key`؛ التكرار يعيد النتيجة الأصلية؛ نفس المفتاح بحمولة مختلفة → `IDEMPOTENCY_KEY_REUSED` (HTTP 422).
- الأوامر التي تبدأ بـ `SYS:` يطلقها المجدول بهوية عبء عمل، وتخضع لنفس الثوابت.

## الحفظ

- State + history (إصدار غير قابل للتعديل لكل تغيير، ADR-P02) + outbox + audit outbox في نفس المعاملة (FIT-04).
- النموذج المنطقي: `06-data/logical-model/slc-09.md`.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
id: AGG-ASSET
bc: BC05
name: Asset
tier: T2 (location as T1 claims on the linked entity)
purpose: أصل مادي بملكية وحيازة وحالة وقدرات وشهادات وصيانة
states:
- IN_SERVICE
- UNSERVICEABLE
- UNDER_MAINTENANCE
- LOST
- DISPOSED
terminal:
- DISPOSED
invariants:
- 'INV-AST-01: available(asset, window) ⇔ IN_SERVICE ∧ required certifications valid
  throughout window ∧ no overlapping maintenance window, CONFIRMED/HELD reservation
  or ACTIVE assignment (REQ-RES-003/004/014)'
- 'INV-AST-02: custody chain is gapless; each transfer by the current holder or custodian
  authority (REQ-RES-002)'
- 'INV-AST-03: location lives as bitemporal claims on the linked information entity,
  never as a column (REQ-RES-005)'
- 'INV-AST-04: an expired certification makes the asset unavailable for new assignments
  from that instant, evaluated at read time'
entities:
- Certification
- CustodyEntry
- Capability (code, level)
requirements:
- REQ-RES-001
- REQ-RES-002
- REQ-RES-003
- REQ-RES-005
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-AST-REGISTER
  to: IN_SERVICE
  guard: type in RD-ASSET-TYPES; owner org; custody holder ACTIVE; linked information
    entity (entity_type asset-ref) created or referenced in BC02; capabilities; label
  event: EVT-AST-REGISTERED
  guard_error: ASSET_INVALID
- from:
  - IN_SERVICE
  - UNSERVICEABLE
  - UNDER_MAINTENANCE
  command: CMD-AST-UPDATE-CONDITION
  to: '='
  guard: condition grade in RD-CONDITION-GRADES; inspector; unserviceable grades require
    CMD-AST-MARK-UNSERVICEABLE
  event: EVT-AST-CONDITION-UPDATED
  guard_error: CONDITION_INVALID
- from:
  - IN_SERVICE
  command: CMD-AST-MARK-UNSERVICEABLE
  to: UNSERVICEABLE
  guard: reason; active assignments are notified; future reservations flagged
  event: EVT-AST-UNSERVICEABLE
  guard_error: REASON_REQUIRED
- from:
  - IN_SERVICE
  - UNSERVICEABLE
  command: CMD-AST-START-MAINTENANCE
  to: UNDER_MAINTENANCE
  guard: maintenance order IN_PROGRESS for this asset
  event: EVT-AST-MAINTENANCE-STARTED
  guard_error: MAINTENANCE_ORDER_REQUIRED
- from:
  - UNDER_MAINTENANCE
  command: CMD-AST-RETURN-TO-SERVICE
  to: IN_SERVICE
  guard: maintenance order COMPLETED; condition serviceable; required certifications
    valid
  event: EVT-AST-RETURNED-TO-SERVICE
  guard_error: ASSET_NOT_SERVICEABLE
- from:
  - UNDER_MAINTENANCE
  command: CMD-AST-FAIL-MAINTENANCE
  to: UNSERVICEABLE
  guard: maintenance order COMPLETED with outcome failed; reason
  event: EVT-AST-UNSERVICEABLE
  guard_error: REASON_REQUIRED
- from:
  - IN_SERVICE
  - UNSERVICEABLE
  - UNDER_MAINTENANCE
  command: CMD-AST-TRANSFER-CUSTODY
  to: '='
  guard: actor is current holder or custodian authority; new holder ACTIVE in scope;
    gapless chain
  event: EVT-AST-CUSTODY-TRANSFERRED
  guard_error: CUSTODY_INVALID
- from:
  - IN_SERVICE
  - UNSERVICEABLE
  - UNDER_MAINTENANCE
  command: CMD-AST-SET-CERTIFICATION
  to: '='
  guard: certification code, issuer, valid_from/to; evidence
  event: EVT-AST-CERTIFICATION-SET
  guard_error: CERTIFICATION_INVALID
- from:
  - IN_SERVICE
  - UNSERVICEABLE
  command: CMD-AST-REPORT-LOST
  to: LOST
  guard: reason; active assignments ended; reservations cancelled
  event: EVT-AST-REPORTED-LOST
  guard_error: REASON_REQUIRED
- from:
  - LOST
  command: CMD-AST-RECOVER
  to: UNSERVICEABLE
  guard: found; inspection required before service
  event: EVT-AST-RECOVERED
  guard_error: null
- from:
  - UNSERVICEABLE
  - LOST
  command: CMD-AST-DISPOSE
  to: DISPOSED
  guard: disposal authority (decision type asset-disposal); no active reservation
    or assignment; no legal hold
  event: EVT-AST-DISPOSED
  guard_error: AUTHORITY_REQUIRED
- from:
  - IN_SERVICE
  - UNSERVICEABLE
  - UNDER_MAINTENANCE
  - LOST
  command: CMD-AST-RECLASSIFY
  to: '='
  guard: authority per policy
  event: EVT-AST-RECLASSIFIED
  guard_error: CLASSIFICATION_CHANGE_NOT_AUTHORIZED
```

</details>
