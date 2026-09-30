---
id: AGG-QUALIFICATION-RECORD
type: aggregate
title: Qualification Record
wave: W4
slice: SLC-03
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC05
importance_tier: T2
personal_data: true
traces:
  satisfies:
  - REQ-RDY-001
  - REQ-RDY-002
  state_machine: SM-QUALIFICATION-RECORD
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-QUALIFICATION-RECORD — Qualification Record

**الغرض:** كفاءة أو تأهيل أو شهادة لشخص بفترة صلاحية  
**السياق:** BC05 · **المستوى:** T2 · **بيانات شخصية:** نعم

## الثوابت (Invariants)

- **INV-QUAL-01** — eligibility evaluates validity at the requested time even if the EXPIRED transition is late
- **INV-QUAL-02** — records are never deleted; history supports as-of eligibility

## الحالات

- غير نهائية: ACTIVE, SUSPENDED
- نهائية: EXPIRED, REVOKED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-QUAL-RECORD | ACTIVE | person ACTIVE; code in RD-COMPETENCIES; level valid; valid_from < valid_to; issuer; evidence ref optional | EVT-QUAL-RECORDED | QUALIFICATION_INVALID |
| ACTIVE | CMD-QUAL-RENEW | (بلا تغيير) | new valid_to > old; evidence; new version | EVT-QUAL-RENEWED | QUALIFICATION_INVALID |
| ACTIVE | CMD-QUAL-SUSPEND | SUSPENDED | reason | EVT-QUAL-SUSPENDED | REASON_REQUIRED |
| SUSPENDED | CMD-QUAL-REINSTATE | ACTIVE | validity not ended | EVT-QUAL-REINSTATED | QUALIFICATION_EXPIRED |
| ACTIVE, SUSPENDED | CMD-QUAL-REVOKE | REVOKED | reason | EVT-QUAL-REVOKED | REASON_REQUIRED |
| ACTIVE, SUSPENDED | SYS:valid_to reached | EXPIRED | scheduler (eligibility also checks validity at read time) | EVT-QUAL-EXPIRED | — |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-QUAL-RECORD | CMD-QUAL-RENEW | CMD-QUAL-SUSPEND | CMD-QUAL-REINSTATE | CMD-QUAL-REVOKE | SYS:valid_to reached |
|---|---|---|---|---|---|---|
| ∅ | → ACTIVE | — | — | — | — | — |
| ACTIVE | ✗ QUALIFICATION_RECORD_INVALID_STATE_TRANSITION | → ACTIVE | → SUSPENDED | ✗ QUALIFICATION_RECORD_INVALID_STATE_TRANSITION | → REVOKED | → EXPIRED |
| SUSPENDED | ✗ QUALIFICATION_RECORD_INVALID_STATE_TRANSITION | ✗ QUALIFICATION_RECORD_INVALID_STATE_TRANSITION | ✗ QUALIFICATION_RECORD_INVALID_STATE_TRANSITION | → ACTIVE | → REVOKED | → EXPIRED |
| EXPIRED | ✗ QUALIFICATION_RECORD_INVALID_STATE_TRANSITION | ✗ QUALIFICATION_RECORD_INVALID_STATE_TRANSITION | ✗ QUALIFICATION_RECORD_INVALID_STATE_TRANSITION | ✗ QUALIFICATION_RECORD_INVALID_STATE_TRANSITION | ✗ QUALIFICATION_RECORD_INVALID_STATE_TRANSITION | ✗ QUALIFICATION_RECORD_INVALID_STATE_TRANSITION |
| REVOKED | ✗ QUALIFICATION_RECORD_INVALID_STATE_TRANSITION | ✗ QUALIFICATION_RECORD_INVALID_STATE_TRANSITION | ✗ QUALIFICATION_RECORD_INVALID_STATE_TRANSITION | ✗ QUALIFICATION_RECORD_INVALID_STATE_TRANSITION | ✗ QUALIFICATION_RECORD_INVALID_STATE_TRANSITION | ✗ QUALIFICATION_RECORD_INVALID_STATE_TRANSITION |

## التزامن وعدم التكرار

- Optimistic concurrency: `If-Match: <version>`؛ عدم التطابق → `VERSION_CONFLICT` (HTTP 409) دون تغيير.
- كل أمر يحمل `Idempotency-Key`؛ التكرار يعيد النتيجة الأصلية؛ نفس المفتاح بحمولة مختلفة → `IDEMPOTENCY_KEY_REUSED` (HTTP 422).
- الأوامر التي تبدأ بـ `SYS:` يطلقها المجدول بهوية عبء عمل، وتخضع لنفس الثوابت.

## الحفظ

- State + history (إصدار غير قابل للتعديل لكل تغيير، ADR-P02) + outbox + audit outbox في نفس المعاملة (FIT-04).
- النموذج المنطقي: `06-data/logical-model/slc-03.md`.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
id: AGG-QUALIFICATION-RECORD
bc: BC05
name: Qualification Record
tier: T2
purpose: كفاءة أو تأهيل أو شهادة لشخص بفترة صلاحية
states:
- ACTIVE
- SUSPENDED
- EXPIRED
- REVOKED
terminal:
- EXPIRED
- REVOKED
invariants:
- 'INV-QUAL-01: eligibility evaluates validity at the requested time even if the EXPIRED
  transition is late'
- 'INV-QUAL-02: records are never deleted; history supports as-of eligibility'
entities: []
requirements:
- REQ-RDY-001
- REQ-RDY-002
notes: null
personal_data: true
reachability: PASS
transitions:
- from: ∅
  command: CMD-QUAL-RECORD
  to: ACTIVE
  guard: person ACTIVE; code in RD-COMPETENCIES; level valid; valid_from < valid_to;
    issuer; evidence ref optional
  event: EVT-QUAL-RECORDED
  guard_error: QUALIFICATION_INVALID
- from:
  - ACTIVE
  command: CMD-QUAL-RENEW
  to: '='
  guard: new valid_to > old; evidence; new version
  event: EVT-QUAL-RENEWED
  guard_error: QUALIFICATION_INVALID
- from:
  - ACTIVE
  command: CMD-QUAL-SUSPEND
  to: SUSPENDED
  guard: reason
  event: EVT-QUAL-SUSPENDED
  guard_error: REASON_REQUIRED
- from:
  - SUSPENDED
  command: CMD-QUAL-REINSTATE
  to: ACTIVE
  guard: validity not ended
  event: EVT-QUAL-REINSTATED
  guard_error: QUALIFICATION_EXPIRED
- from:
  - ACTIVE
  - SUSPENDED
  command: CMD-QUAL-REVOKE
  to: REVOKED
  guard: reason
  event: EVT-QUAL-REVOKED
  guard_error: REASON_REQUIRED
- from:
  - ACTIVE
  - SUSPENDED
  command: SYS:valid_to reached
  to: EXPIRED
  guard: scheduler (eligibility also checks validity at read time)
  event: EVT-QUAL-EXPIRED
  guard_error: null
```

</details>
