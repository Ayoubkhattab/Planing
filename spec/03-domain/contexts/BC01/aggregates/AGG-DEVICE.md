---
id: AGG-DEVICE
type: aggregate
title: Field Device
wave: W4
slice: SLC-11
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC01
importance_tier: T2
personal_data: false
traces:
  satisfies:
  - REQ-OFF-005
  state_machine: SM-DEVICE
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-DEVICE — Field Device

**الغرض:** جهاز ميداني مسجل ومربوط بمستخدم ومفتاح  
**السياق:** BC01 · **المستوى:** T2 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-DEV-01** — only ACTIVE devices can open sync sessions or download preload packages
- **INV-DEV-02** — device key is bound to (user, device); every offline command is signed with it (THR-012)
- **INV-DEV-03** — LOST revokes the key at once; the next contact receives a wipe instruction and nothing else
- **INV-DEV-04** — ≤ 3 ACTIVE devices per user (W4 delegated decision)

## مكونات داخلية

- DeviceKey (public key, valid_from, revoked_at)

## الحالات

- غير نهائية: PENDING_ENROLLMENT, ACTIVE, SUSPENDED, LOST
- نهائية: WIPED, RETIRED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-DEV-ENROLL | PENDING_ENROLLMENT | user ACTIVE; device public key; platform; MDM reference; ≤ 3 active devices per user | EVT-DEV-ENROLL-REQUESTED | DEVICE_LIMIT_REACHED |
| PENDING_ENROLLMENT | CMD-DEV-CONFIRM | ACTIVE | hardware attestation valid (or MDM compliance); Administrator or MDM policy | EVT-DEV-ACTIVATED | ATTESTATION_FAILED |
| ACTIVE | CMD-DEV-ROTATE-KEY | (بلا تغيير) | signed by current key; new public key | EVT-DEV-KEY-ROTATED | SIGNATURE_INVALID |
| ACTIVE | CMD-DEV-SUSPEND | SUSPENDED | reason; sync rejected while suspended | EVT-DEV-SUSPENDED | REASON_REQUIRED |
| SUSPENDED | CMD-DEV-REINSTATE | ACTIVE | reason | EVT-DEV-REINSTATED | REASON_REQUIRED |
| ACTIVE, SUSPENDED | CMD-DEV-REPORT-LOST | LOST | user or Security Officer; key revoked immediately; wipe instruction queued; queued commands from the device after the lost time require review | EVT-DEV-REPORTED-LOST | — |
| LOST | SYS:wipe confirmed by device | WIPED | device acknowledges wipe on next contact | EVT-DEV-WIPED | — |
| ACTIVE, SUSPENDED | CMD-DEV-RETIRE | RETIRED | device synced and wiped (confirmation) or Security Officer override | EVT-DEV-RETIRED | DEVICE_NOT_WIPED |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-DEV-ENROLL | CMD-DEV-CONFIRM | CMD-DEV-ROTATE-KEY | CMD-DEV-SUSPEND | CMD-DEV-REINSTATE | CMD-DEV-REPORT-LOST | SYS:wipe confirmed by device | CMD-DEV-RETIRE |
|---|---|---|---|---|---|---|---|---|
| ∅ | → PENDING_ENROLLMENT | — | — | — | — | — | — | — |
| PENDING_ENROLLMENT | ✗ DEVICE_INVALID_STATE_TRANSITION | → ACTIVE | ✗ DEVICE_INVALID_STATE_TRANSITION | ✗ DEVICE_INVALID_STATE_TRANSITION | ✗ DEVICE_INVALID_STATE_TRANSITION | ✗ DEVICE_INVALID_STATE_TRANSITION | ✗ DEVICE_INVALID_STATE_TRANSITION | ✗ DEVICE_INVALID_STATE_TRANSITION |
| ACTIVE | ✗ DEVICE_INVALID_STATE_TRANSITION | ✗ DEVICE_INVALID_STATE_TRANSITION | → ACTIVE | → SUSPENDED | ✗ DEVICE_INVALID_STATE_TRANSITION | → LOST | ✗ DEVICE_INVALID_STATE_TRANSITION | → RETIRED |
| SUSPENDED | ✗ DEVICE_INVALID_STATE_TRANSITION | ✗ DEVICE_INVALID_STATE_TRANSITION | ✗ DEVICE_INVALID_STATE_TRANSITION | ✗ DEVICE_INVALID_STATE_TRANSITION | → ACTIVE | → LOST | ✗ DEVICE_INVALID_STATE_TRANSITION | → RETIRED |
| LOST | ✗ DEVICE_INVALID_STATE_TRANSITION | ✗ DEVICE_INVALID_STATE_TRANSITION | ✗ DEVICE_INVALID_STATE_TRANSITION | ✗ DEVICE_INVALID_STATE_TRANSITION | ✗ DEVICE_INVALID_STATE_TRANSITION | ✗ DEVICE_INVALID_STATE_TRANSITION | → WIPED | ✗ DEVICE_INVALID_STATE_TRANSITION |
| WIPED | ✗ DEVICE_INVALID_STATE_TRANSITION | ✗ DEVICE_INVALID_STATE_TRANSITION | ✗ DEVICE_INVALID_STATE_TRANSITION | ✗ DEVICE_INVALID_STATE_TRANSITION | ✗ DEVICE_INVALID_STATE_TRANSITION | ✗ DEVICE_INVALID_STATE_TRANSITION | ✗ DEVICE_INVALID_STATE_TRANSITION | ✗ DEVICE_INVALID_STATE_TRANSITION |
| RETIRED | ✗ DEVICE_INVALID_STATE_TRANSITION | ✗ DEVICE_INVALID_STATE_TRANSITION | ✗ DEVICE_INVALID_STATE_TRANSITION | ✗ DEVICE_INVALID_STATE_TRANSITION | ✗ DEVICE_INVALID_STATE_TRANSITION | ✗ DEVICE_INVALID_STATE_TRANSITION | ✗ DEVICE_INVALID_STATE_TRANSITION | ✗ DEVICE_INVALID_STATE_TRANSITION |

## التزامن وعدم التكرار

- Optimistic concurrency: `If-Match: <version>`؛ عدم التطابق → `VERSION_CONFLICT` (HTTP 409) دون تغيير.
- كل أمر يحمل `Idempotency-Key`؛ التكرار يعيد النتيجة الأصلية؛ نفس المفتاح بحمولة مختلفة → `IDEMPOTENCY_KEY_REUSED` (HTTP 422).
- الأوامر التي تبدأ بـ `SYS:` يطلقها المجدول بهوية عبء عمل، وتخضع لنفس الثوابت.

## الحفظ

- State + history (إصدار غير قابل للتعديل لكل تغيير، ADR-P02) + outbox + audit outbox في نفس المعاملة (FIT-04).
- النموذج المنطقي: `06-data/logical-model/slc-11.md`.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
id: AGG-DEVICE
bc: BC01
name: Field Device
tier: T2
purpose: جهاز ميداني مسجل ومربوط بمستخدم ومفتاح
states:
- PENDING_ENROLLMENT
- ACTIVE
- SUSPENDED
- LOST
- WIPED
- RETIRED
terminal:
- WIPED
- RETIRED
invariants:
- 'INV-DEV-01: only ACTIVE devices can open sync sessions or download preload packages'
- 'INV-DEV-02: device key is bound to (user, device); every offline command is signed
  with it (THR-012)'
- 'INV-DEV-03: LOST revokes the key at once; the next contact receives a wipe instruction
  and nothing else'
- 'INV-DEV-04: ≤ 3 ACTIVE devices per user (W4 delegated decision)'
entities:
- DeviceKey (public key, valid_from, revoked_at)
requirements:
- REQ-OFF-005
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-DEV-ENROLL
  to: PENDING_ENROLLMENT
  guard: user ACTIVE; device public key; platform; MDM reference; ≤ 3 active devices
    per user
  event: EVT-DEV-ENROLL-REQUESTED
  guard_error: DEVICE_LIMIT_REACHED
- from:
  - PENDING_ENROLLMENT
  command: CMD-DEV-CONFIRM
  to: ACTIVE
  guard: hardware attestation valid (or MDM compliance); Administrator or MDM policy
  event: EVT-DEV-ACTIVATED
  guard_error: ATTESTATION_FAILED
- from:
  - ACTIVE
  command: CMD-DEV-ROTATE-KEY
  to: '='
  guard: signed by current key; new public key
  event: EVT-DEV-KEY-ROTATED
  guard_error: SIGNATURE_INVALID
- from:
  - ACTIVE
  command: CMD-DEV-SUSPEND
  to: SUSPENDED
  guard: reason; sync rejected while suspended
  event: EVT-DEV-SUSPENDED
  guard_error: REASON_REQUIRED
- from:
  - SUSPENDED
  command: CMD-DEV-REINSTATE
  to: ACTIVE
  guard: reason
  event: EVT-DEV-REINSTATED
  guard_error: REASON_REQUIRED
- from:
  - ACTIVE
  - SUSPENDED
  command: CMD-DEV-REPORT-LOST
  to: LOST
  guard: user or Security Officer; key revoked immediately; wipe instruction queued;
    queued commands from the device after the lost time require review
  event: EVT-DEV-REPORTED-LOST
  guard_error: null
- from:
  - LOST
  command: SYS:wipe confirmed by device
  to: WIPED
  guard: device acknowledges wipe on next contact
  event: EVT-DEV-WIPED
  guard_error: null
- from:
  - ACTIVE
  - SUSPENDED
  command: CMD-DEV-RETIRE
  to: RETIRED
  guard: device synced and wiped (confirmation) or Security Officer override
  event: EVT-DEV-RETIRED
  guard_error: DEVICE_NOT_WIPED
```

</details>
