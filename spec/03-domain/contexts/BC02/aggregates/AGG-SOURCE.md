---
id: AGG-SOURCE
type: aggregate
title: Source
wave: W4
slice: SLC-02
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC02
importance_tier: T1 reliability / T2 profile
personal_data: false
traces:
  satisfies:
  - REQ-INF-001
  state_machine: SM-SOURCE
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-SOURCE — Source

**الغرض:** جهة أو نظام أو مستشعر ينتج معلومات، مع موثوقية مؤرخة وحماية هوية  
**السياق:** BC02 · **المستوى:** T1 reliability / T2 profile · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-SRC-01** — reliability is a bitemporal claim; a claim's source_reliability is the rating valid and known at the claim's recorded_from
- **INV-SRC-02** — identity attributes of person-type sources are visible only with the source-protection permission; others see type and reliability only
- **INV-SRC-03** — SUSPENDED or RETIRED sources cannot be cited by new claims or observations
- **INV-SRC-04** — retiring never alters past ratings or claims

## مكونات داخلية

- ReliabilityRating (bitemporal)
- Profile (T2)

## الحالات

- غير نهائية: ACTIVE, SUSPENDED
- نهائية: RETIRED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-SRC-REGISTER | ACTIVE | type in RD-SOURCE-TYPES; initial reliability A–F; person-type sources get protection_level ≥ 1 and label ≥ tenant default + 1 rank | EVT-SRC-REGISTERED | SOURCE_INVALID |
| ACTIVE, SUSPENDED | CMD-SRC-RATE-RELIABILITY | (بلا تغيير) | rating ∈ A–F; valid_from given; creates bitemporal reliability claim | EVT-SRC-RELIABILITY-RATED | RATING_INVALID |
| ACTIVE, SUSPENDED | CMD-SRC-UPDATE-PROFILE | (بلا تغيير) | — | EVT-SRC-PROFILE-UPDATED | — |
| ACTIVE, SUSPENDED | CMD-SRC-SET-PROTECTION | (بلا تغيير) | Security Officer; decreasing protection requires a second Security Officer | EVT-SRC-PROTECTION-CHANGED | SEGREGATION_OF_DUTIES |
| ACTIVE, SUSPENDED | CMD-SRC-RECLASSIFY | (بلا تغيير) | authority per tenant policy (REQ-GOV-004); new version; bumps object security_version | EVT-SRC-RECLASSIFIED | CLASSIFICATION_CHANGE_NOT_AUTHORIZED |
| ACTIVE | CMD-SRC-SUSPEND | SUSPENDED | reason | EVT-SRC-SUSPENDED | REASON_REQUIRED |
| SUSPENDED | CMD-SRC-REINSTATE | ACTIVE | — | EVT-SRC-REINSTATED | — |
| ACTIVE, SUSPENDED | CMD-SRC-RETIRE | RETIRED | reason; history retained | EVT-SRC-RETIRED | REASON_REQUIRED |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-SRC-REGISTER | CMD-SRC-RATE-RELIABILITY | CMD-SRC-UPDATE-PROFILE | CMD-SRC-SET-PROTECTION | CMD-SRC-RECLASSIFY | CMD-SRC-SUSPEND | CMD-SRC-REINSTATE | CMD-SRC-RETIRE |
|---|---|---|---|---|---|---|---|---|
| ∅ | → ACTIVE | — | — | — | — | — | — | — |
| ACTIVE | ✗ SOURCE_INVALID_STATE_TRANSITION | → ACTIVE | → ACTIVE | → ACTIVE | → ACTIVE | → SUSPENDED | ✗ SOURCE_INVALID_STATE_TRANSITION | → RETIRED |
| SUSPENDED | ✗ SOURCE_INVALID_STATE_TRANSITION | → SUSPENDED | → SUSPENDED | → SUSPENDED | → SUSPENDED | ✗ SOURCE_INVALID_STATE_TRANSITION | → ACTIVE | → RETIRED |
| RETIRED | ✗ SOURCE_INVALID_STATE_TRANSITION | ✗ SOURCE_INVALID_STATE_TRANSITION | ✗ SOURCE_INVALID_STATE_TRANSITION | ✗ SOURCE_INVALID_STATE_TRANSITION | ✗ SOURCE_INVALID_STATE_TRANSITION | ✗ SOURCE_INVALID_STATE_TRANSITION | ✗ SOURCE_INVALID_STATE_TRANSITION | ✗ SOURCE_INVALID_STATE_TRANSITION |

## التزامن وعدم التكرار

- Optimistic concurrency: `If-Match: <version>`؛ عدم التطابق → `VERSION_CONFLICT` (HTTP 409) دون تغيير.
- كل أمر يحمل `Idempotency-Key`؛ التكرار يعيد النتيجة الأصلية؛ نفس المفتاح بحمولة مختلفة → `IDEMPOTENCY_KEY_REUSED` (HTTP 422).
- الأوامر التي تبدأ بـ `SYS:` يطلقها المجدول بهوية عبء عمل، وتخضع لنفس الثوابت.

## الحفظ

- State + history (إصدار غير قابل للتعديل لكل تغيير، ADR-P02) + outbox + audit outbox في نفس المعاملة (FIT-04).
- النموذج المنطقي: `06-data/logical-model/slc-02.md`.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
id: AGG-SOURCE
bc: BC02
name: Source
tier: T1 reliability / T2 profile
purpose: جهة أو نظام أو مستشعر ينتج معلومات، مع موثوقية مؤرخة وحماية هوية
states:
- ACTIVE
- SUSPENDED
- RETIRED
terminal:
- RETIRED
invariants:
- 'INV-SRC-01: reliability is a bitemporal claim; a claim''s source_reliability is
  the rating valid and known at the claim''s recorded_from'
- 'INV-SRC-02: identity attributes of person-type sources are visible only with the
  source-protection permission; others see type and reliability only'
- 'INV-SRC-03: SUSPENDED or RETIRED sources cannot be cited by new claims or observations'
- 'INV-SRC-04: retiring never alters past ratings or claims'
entities:
- ReliabilityRating (bitemporal)
- Profile (T2)
requirements:
- REQ-INF-001
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-SRC-REGISTER
  to: ACTIVE
  guard: type in RD-SOURCE-TYPES; initial reliability A–F; person-type sources get
    protection_level ≥ 1 and label ≥ tenant default + 1 rank
  event: EVT-SRC-REGISTERED
  guard_error: SOURCE_INVALID
- from:
  - ACTIVE
  - SUSPENDED
  command: CMD-SRC-RATE-RELIABILITY
  to: '='
  guard: rating ∈ A–F; valid_from given; creates bitemporal reliability claim
  event: EVT-SRC-RELIABILITY-RATED
  guard_error: RATING_INVALID
- from:
  - ACTIVE
  - SUSPENDED
  command: CMD-SRC-UPDATE-PROFILE
  to: '='
  guard: —
  event: EVT-SRC-PROFILE-UPDATED
  guard_error: null
- from:
  - ACTIVE
  - SUSPENDED
  command: CMD-SRC-SET-PROTECTION
  to: '='
  guard: Security Officer; decreasing protection requires a second Security Officer
  event: EVT-SRC-PROTECTION-CHANGED
  guard_error: SEGREGATION_OF_DUTIES
- from:
  - ACTIVE
  - SUSPENDED
  command: CMD-SRC-RECLASSIFY
  to: '='
  guard: authority per tenant policy (REQ-GOV-004); new version; bumps object security_version
  event: EVT-SRC-RECLASSIFIED
  guard_error: CLASSIFICATION_CHANGE_NOT_AUTHORIZED
- from:
  - ACTIVE
  command: CMD-SRC-SUSPEND
  to: SUSPENDED
  guard: reason
  event: EVT-SRC-SUSPENDED
  guard_error: REASON_REQUIRED
- from:
  - SUSPENDED
  command: CMD-SRC-REINSTATE
  to: ACTIVE
  guard: —
  event: EVT-SRC-REINSTATED
  guard_error: null
- from:
  - ACTIVE
  - SUSPENDED
  command: CMD-SRC-RETIRE
  to: RETIRED
  guard: reason; history retained
  event: EVT-SRC-RETIRED
  guard_error: REASON_REQUIRED
```

</details>
