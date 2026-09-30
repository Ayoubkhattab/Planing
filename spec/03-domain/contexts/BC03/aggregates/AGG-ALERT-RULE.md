---
id: AGG-ALERT-RULE
type: aggregate
title: Alert Rule
wave: W4
slice: SLC-06
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC03
importance_tier: T2
personal_data: false
traces:
  satisfies:
  - REQ-SIT-004
  state_machine: SM-ALERT-RULE
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-ALERT-RULE — Alert Rule

**الغرض:** قاعدة تنبيه على موقف أو على نطاق المستأجر  
**السياق:** BC03 · **المستوى:** T2 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-ARL-01** — an ACTIVE rule is immutable; editing requires DISABLED (no silent change to what triggers alerts)
- **INV-ARL-02** — the rule's label ≥ labels of data it reads, enforced at evaluation by computing alert labels (INV-ALR-02)
- **INV-ARL-03** — rules of a PAUSED or CLOSED situation do not fire

## مكونات داخلية

- Condition (kind, parameters)
- DedupePolicy
- AutoResolve (bool)

## الحالات

- غير نهائية: DRAFT, ACTIVE, DISABLED
- نهائية: RETIRED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-ARL-DEFINE | DRAFT | condition kind in RD-ALERT-RULE-TYPES; parameters valid; severity; dedupe window; situation ACTIVE or tenant-wide scope | EVT-ARL-DEFINED | ALERT_RULE_INVALID |
| DRAFT, DISABLED | CMD-ARL-EDIT | (بلا تغيير) | same validation; new version | EVT-ARL-EDITED | ALERT_RULE_INVALID |
| DRAFT | CMD-ARL-ACTIVATE | ACTIVE | dry-run on last 24 h of events completed and reviewed (expected alert volume shown) | EVT-ARL-ACTIVATED | DRY_RUN_REQUIRED |
| ACTIVE | CMD-ARL-DISABLE | DISABLED | reason | EVT-ARL-DISABLED | REASON_REQUIRED |
| DISABLED | CMD-ARL-ENABLE | ACTIVE | — | EVT-ARL-ENABLED | — |
| DRAFT, ACTIVE, DISABLED | CMD-ARL-RETIRE | RETIRED | reason | EVT-ARL-RETIRED | REASON_REQUIRED |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-ARL-DEFINE | CMD-ARL-EDIT | CMD-ARL-ACTIVATE | CMD-ARL-DISABLE | CMD-ARL-ENABLE | CMD-ARL-RETIRE |
|---|---|---|---|---|---|---|
| ∅ | → DRAFT | — | — | — | — | — |
| DRAFT | ✗ ALERT_RULE_INVALID_STATE_TRANSITION | → DRAFT | → ACTIVE | ✗ ALERT_RULE_INVALID_STATE_TRANSITION | ✗ ALERT_RULE_INVALID_STATE_TRANSITION | → RETIRED |
| ACTIVE | ✗ ALERT_RULE_INVALID_STATE_TRANSITION | ✗ ALERT_RULE_INVALID_STATE_TRANSITION | ✗ ALERT_RULE_INVALID_STATE_TRANSITION | → DISABLED | ✗ ALERT_RULE_INVALID_STATE_TRANSITION | → RETIRED |
| DISABLED | ✗ ALERT_RULE_INVALID_STATE_TRANSITION | → DISABLED | ✗ ALERT_RULE_INVALID_STATE_TRANSITION | ✗ ALERT_RULE_INVALID_STATE_TRANSITION | → ACTIVE | → RETIRED |
| RETIRED | ✗ ALERT_RULE_INVALID_STATE_TRANSITION | ✗ ALERT_RULE_INVALID_STATE_TRANSITION | ✗ ALERT_RULE_INVALID_STATE_TRANSITION | ✗ ALERT_RULE_INVALID_STATE_TRANSITION | ✗ ALERT_RULE_INVALID_STATE_TRANSITION | ✗ ALERT_RULE_INVALID_STATE_TRANSITION |

## التزامن وعدم التكرار

- Optimistic concurrency: `If-Match: <version>`؛ عدم التطابق → `VERSION_CONFLICT` (HTTP 409) دون تغيير.
- كل أمر يحمل `Idempotency-Key`؛ التكرار يعيد النتيجة الأصلية؛ نفس المفتاح بحمولة مختلفة → `IDEMPOTENCY_KEY_REUSED` (HTTP 422).
- الأوامر التي تبدأ بـ `SYS:` يطلقها المجدول بهوية عبء عمل، وتخضع لنفس الثوابت.

## الحفظ

- State + history (إصدار غير قابل للتعديل لكل تغيير، ADR-P02) + outbox + audit outbox في نفس المعاملة (FIT-04).
- النموذج المنطقي: `06-data/logical-model/slc-06.md`.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
id: AGG-ALERT-RULE
bc: BC03
name: Alert Rule
tier: T2
purpose: قاعدة تنبيه على موقف أو على نطاق المستأجر
states:
- DRAFT
- ACTIVE
- DISABLED
- RETIRED
terminal:
- RETIRED
invariants:
- 'INV-ARL-01: an ACTIVE rule is immutable; editing requires DISABLED (no silent change
  to what triggers alerts)'
- 'INV-ARL-02: the rule''s label ≥ labels of data it reads, enforced at evaluation
  by computing alert labels (INV-ALR-02)'
- 'INV-ARL-03: rules of a PAUSED or CLOSED situation do not fire'
entities:
- Condition (kind, parameters)
- DedupePolicy
- AutoResolve (bool)
requirements:
- REQ-SIT-004
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-ARL-DEFINE
  to: DRAFT
  guard: condition kind in RD-ALERT-RULE-TYPES; parameters valid; severity; dedupe
    window; situation ACTIVE or tenant-wide scope
  event: EVT-ARL-DEFINED
  guard_error: ALERT_RULE_INVALID
- from:
  - DRAFT
  - DISABLED
  command: CMD-ARL-EDIT
  to: '='
  guard: same validation; new version
  event: EVT-ARL-EDITED
  guard_error: ALERT_RULE_INVALID
- from:
  - DRAFT
  command: CMD-ARL-ACTIVATE
  to: ACTIVE
  guard: dry-run on last 24 h of events completed and reviewed (expected alert volume
    shown)
  event: EVT-ARL-ACTIVATED
  guard_error: DRY_RUN_REQUIRED
- from:
  - ACTIVE
  command: CMD-ARL-DISABLE
  to: DISABLED
  guard: reason
  event: EVT-ARL-DISABLED
  guard_error: REASON_REQUIRED
- from:
  - DISABLED
  command: CMD-ARL-ENABLE
  to: ACTIVE
  guard: —
  event: EVT-ARL-ENABLED
  guard_error: null
- from:
  - DRAFT
  - ACTIVE
  - DISABLED
  command: CMD-ARL-RETIRE
  to: RETIRED
  guard: reason
  event: EVT-ARL-RETIRED
  guard_error: REASON_REQUIRED
```

</details>
