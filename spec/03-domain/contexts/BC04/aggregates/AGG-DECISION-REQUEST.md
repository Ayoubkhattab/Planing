---
id: AGG-DECISION-REQUEST
type: aggregate
title: Decision Request
wave: W4
slice: SLC-08
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC04
importance_tier: T2
personal_data: false
traces:
  satisfies:
  - REQ-DEC-001
  state_machine: SM-DECISION-REQUEST
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-DECISION-REQUEST — Decision Request

**الغرض:** طلب قرار بسؤال وخيارات وتقييمات مستشهد بها وسلطة مطلوبة  
**السياق:** BC04 · **المستوى:** T2 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-DRQ-01** — citations are pinned by version (INV-ASM-03)
- **INV-DRQ-02** — request label ≥ labels of its citations
- **INV-DRQ-03** — a request is decided by exactly one decision

## مكونات داخلية

- Option
- Citation (pinned)

## الحالات

- غير نهائية: DRAFT, OPEN
- نهائية: DECIDED, WITHDRAWN
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-DRQ-CREATE | DRAFT | question; required decision type (RD-DECISION-TYPES); scope unit; deadline; label | EVT-DRQ-CREATED | DECISION_REQUEST_INVALID |
| DRAFT, OPEN | CMD-DRQ-ADD-OPTION | (بلا تغيير) | option text; expected impact; options ≤ 10 | EVT-DRQ-OPTION-ADDED | DECISION_REQUEST_INVALID |
| DRAFT, OPEN | CMD-DRQ-CITE | (بلا تغيير) | assessment or evidence visible; pinned URN + version; cited label ≤ request label | EVT-DRQ-CITED | CITATION_ABOVE_LABEL |
| DRAFT | CMD-DRQ-OPEN | OPEN | ≥ 2 options (one may be 'no action'); ≥ 1 citation (REQ-DEC-001, OUT-04) | EVT-DRQ-OPENED | DECISION_REQUEST_INCOMPLETE |
| OPEN | SYS:deadline passed | (بلا تغيير) | escalates to holders of the required authority in scope | EVT-DRQ-ESCALATED | — |
| OPEN | SYS:decision recorded for this request | DECIDED | EVT-DEC-RECORDED references the request | EVT-DRQ-DECIDED | — |
| DRAFT, OPEN | CMD-DRQ-WITHDRAW | WITHDRAWN | reason | EVT-DRQ-WITHDRAWN | REASON_REQUIRED |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-DRQ-CREATE | CMD-DRQ-ADD-OPTION | CMD-DRQ-CITE | CMD-DRQ-OPEN | SYS:deadline passed | SYS:decision recorded for this request | CMD-DRQ-WITHDRAW |
|---|---|---|---|---|---|---|---|
| ∅ | → DRAFT | — | — | — | — | — | — |
| DRAFT | ✗ DECISION_REQUEST_INVALID_STATE_TRANSITION | → DRAFT | → DRAFT | → OPEN | ✗ DECISION_REQUEST_INVALID_STATE_TRANSITION | ✗ DECISION_REQUEST_INVALID_STATE_TRANSITION | → WITHDRAWN |
| OPEN | ✗ DECISION_REQUEST_INVALID_STATE_TRANSITION | → OPEN | → OPEN | ✗ DECISION_REQUEST_INVALID_STATE_TRANSITION | → OPEN | → DECIDED | → WITHDRAWN |
| DECIDED | ✗ DECISION_REQUEST_INVALID_STATE_TRANSITION | ✗ DECISION_REQUEST_INVALID_STATE_TRANSITION | ✗ DECISION_REQUEST_INVALID_STATE_TRANSITION | ✗ DECISION_REQUEST_INVALID_STATE_TRANSITION | ✗ DECISION_REQUEST_INVALID_STATE_TRANSITION | ✗ DECISION_REQUEST_INVALID_STATE_TRANSITION | ✗ DECISION_REQUEST_INVALID_STATE_TRANSITION |
| WITHDRAWN | ✗ DECISION_REQUEST_INVALID_STATE_TRANSITION | ✗ DECISION_REQUEST_INVALID_STATE_TRANSITION | ✗ DECISION_REQUEST_INVALID_STATE_TRANSITION | ✗ DECISION_REQUEST_INVALID_STATE_TRANSITION | ✗ DECISION_REQUEST_INVALID_STATE_TRANSITION | ✗ DECISION_REQUEST_INVALID_STATE_TRANSITION | ✗ DECISION_REQUEST_INVALID_STATE_TRANSITION |

## التزامن وعدم التكرار

- Optimistic concurrency: `If-Match: <version>`؛ عدم التطابق → `VERSION_CONFLICT` (HTTP 409) دون تغيير.
- كل أمر يحمل `Idempotency-Key`؛ التكرار يعيد النتيجة الأصلية؛ نفس المفتاح بحمولة مختلفة → `IDEMPOTENCY_KEY_REUSED` (HTTP 422).
- الأوامر التي تبدأ بـ `SYS:` يطلقها المجدول بهوية عبء عمل، وتخضع لنفس الثوابت.

## الحفظ

- State + history (إصدار غير قابل للتعديل لكل تغيير، ADR-P02) + outbox + audit outbox في نفس المعاملة (FIT-04).
- النموذج المنطقي: `06-data/logical-model/slc-08.md`.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
id: AGG-DECISION-REQUEST
bc: BC04
name: Decision Request
tier: T2
purpose: طلب قرار بسؤال وخيارات وتقييمات مستشهد بها وسلطة مطلوبة
states:
- DRAFT
- OPEN
- DECIDED
- WITHDRAWN
terminal:
- DECIDED
- WITHDRAWN
invariants:
- 'INV-DRQ-01: citations are pinned by version (INV-ASM-03)'
- 'INV-DRQ-02: request label ≥ labels of its citations'
- 'INV-DRQ-03: a request is decided by exactly one decision'
entities:
- Option
- Citation (pinned)
requirements:
- REQ-DEC-001
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-DRQ-CREATE
  to: DRAFT
  guard: question; required decision type (RD-DECISION-TYPES); scope unit; deadline;
    label
  event: EVT-DRQ-CREATED
  guard_error: DECISION_REQUEST_INVALID
- from:
  - DRAFT
  - OPEN
  command: CMD-DRQ-ADD-OPTION
  to: '='
  guard: option text; expected impact; options ≤ 10
  event: EVT-DRQ-OPTION-ADDED
  guard_error: DECISION_REQUEST_INVALID
- from:
  - DRAFT
  - OPEN
  command: CMD-DRQ-CITE
  to: '='
  guard: assessment or evidence visible; pinned URN + version; cited label ≤ request
    label
  event: EVT-DRQ-CITED
  guard_error: CITATION_ABOVE_LABEL
- from:
  - DRAFT
  command: CMD-DRQ-OPEN
  to: OPEN
  guard: ≥ 2 options (one may be 'no action'); ≥ 1 citation (REQ-DEC-001, OUT-04)
  event: EVT-DRQ-OPENED
  guard_error: DECISION_REQUEST_INCOMPLETE
- from:
  - OPEN
  command: SYS:deadline passed
  to: '='
  guard: escalates to holders of the required authority in scope
  event: EVT-DRQ-ESCALATED
  guard_error: null
- from:
  - OPEN
  command: SYS:decision recorded for this request
  to: DECIDED
  guard: EVT-DEC-RECORDED references the request
  event: EVT-DRQ-DECIDED
  guard_error: null
- from:
  - DRAFT
  - OPEN
  command: CMD-DRQ-WITHDRAW
  to: WITHDRAWN
  guard: reason
  event: EVT-DRQ-WITHDRAWN
  guard_error: REASON_REQUIRED
```

</details>
