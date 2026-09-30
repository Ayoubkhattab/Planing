---
id: AGG-SERVICE-ACCOUNT
type: aggregate
title: Service Account
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
  - REQ-FND-006
  state_machine: SM-SERVICE-ACCOUNT
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-SERVICE-ACCOUNT — Service Account

**الغرض:** هوية لنظام أو محول، ليست لشخص  
**السياق:** BC01 · **المستوى:** T2 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-SVC-01** — a service account is never linked to a Person
- **INV-SVC-02** — every service account has an ACTIVE accountable owner user
- **INV-SVC-03** — credential lifetime ≤ 90 days (W4 delegated decision)

## مكونات داخلية

- Credential (entity: id, fingerprint, expires_at)

## الحالات

- غير نهائية: ACTIVE, DISABLED
- نهائية: CLOSED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-SVC-CREATE | ACTIVE | owner user ACTIVE; purpose stated | EVT-SVC-CREATED | OWNER_REQUIRED |
| ACTIVE | CMD-SVC-ROTATE-CREDENTIAL | (بلا تغيير) | new credential expiry ≤ 90 days | EVT-SVC-CREDENTIAL-ROTATED | CREDENTIAL_LIFETIME_EXCEEDED |
| ACTIVE | CMD-SVC-DISABLE | DISABLED | — | EVT-SVC-DISABLED | — |
| DISABLED | CMD-SVC-ENABLE | ACTIVE | owner still ACTIVE | EVT-SVC-ENABLED | OWNER_REQUIRED |
| DISABLED | CMD-SVC-CLOSE | CLOSED | — | EVT-SVC-CLOSED | — |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-SVC-CREATE | CMD-SVC-ROTATE-CREDENTIAL | CMD-SVC-DISABLE | CMD-SVC-ENABLE | CMD-SVC-CLOSE |
|---|---|---|---|---|---|
| ∅ | → ACTIVE | — | — | — | — |
| ACTIVE | ✗ SERVICE_ACCOUNT_INVALID_STATE_TRANSITION | → ACTIVE | → DISABLED | ✗ SERVICE_ACCOUNT_INVALID_STATE_TRANSITION | ✗ SERVICE_ACCOUNT_INVALID_STATE_TRANSITION |
| DISABLED | ✗ SERVICE_ACCOUNT_INVALID_STATE_TRANSITION | ✗ SERVICE_ACCOUNT_INVALID_STATE_TRANSITION | ✗ SERVICE_ACCOUNT_INVALID_STATE_TRANSITION | → ACTIVE | → CLOSED |
| CLOSED | ✗ SERVICE_ACCOUNT_INVALID_STATE_TRANSITION | ✗ SERVICE_ACCOUNT_INVALID_STATE_TRANSITION | ✗ SERVICE_ACCOUNT_INVALID_STATE_TRANSITION | ✗ SERVICE_ACCOUNT_INVALID_STATE_TRANSITION | ✗ SERVICE_ACCOUNT_INVALID_STATE_TRANSITION |

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
id: AGG-SERVICE-ACCOUNT
bc: BC01
name: Service Account
tier: T2
purpose: هوية لنظام أو محول، ليست لشخص
states:
- ACTIVE
- DISABLED
- CLOSED
terminal:
- CLOSED
invariants:
- 'INV-SVC-01: a service account is never linked to a Person'
- 'INV-SVC-02: every service account has an ACTIVE accountable owner user'
- 'INV-SVC-03: credential lifetime ≤ 90 days (W4 delegated decision)'
entities:
- 'Credential (entity: id, fingerprint, expires_at)'
requirements:
- REQ-FND-006
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-SVC-CREATE
  to: ACTIVE
  guard: owner user ACTIVE; purpose stated
  event: EVT-SVC-CREATED
  guard_error: OWNER_REQUIRED
- from:
  - ACTIVE
  command: CMD-SVC-ROTATE-CREDENTIAL
  to: '='
  guard: new credential expiry ≤ 90 days
  event: EVT-SVC-CREDENTIAL-ROTATED
  guard_error: CREDENTIAL_LIFETIME_EXCEEDED
- from:
  - ACTIVE
  command: CMD-SVC-DISABLE
  to: DISABLED
  guard: —
  event: EVT-SVC-DISABLED
  guard_error: null
- from:
  - DISABLED
  command: CMD-SVC-ENABLE
  to: ACTIVE
  guard: owner still ACTIVE
  event: EVT-SVC-ENABLED
  guard_error: OWNER_REQUIRED
- from:
  - DISABLED
  command: CMD-SVC-CLOSE
  to: CLOSED
  guard: —
  event: EVT-SVC-CLOSED
  guard_error: null
```

</details>
