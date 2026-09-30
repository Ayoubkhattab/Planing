---
id: AGG-ALERT
type: aggregate
title: Alert
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
  - REQ-SIT-005
  - REQ-SIT-006
  state_machine: SM-ALERT
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-ALERT — Alert

**الغرض:** تنبيه صادر عن قاعدة، بدورة حياة مدققة  
**السياق:** BC03 · **المستوى:** T2 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-ALR-01** — every transition is audited (REQ-SIT-005)
- **INV-ALR-02** — alert label = max(rule label, labels of triggering objects); only recipients cleared for that label receive it — others receive nothing, not a redacted alert (REQ-SIT-006)
- **INV-ALR-03** — dedupe: at most one non-terminal alert per (rule, subject) within the dedupe window

## مكونات داخلية

- Occurrence (at, trigger_ref)

## الحالات

- غير نهائية: RAISED, ACKNOWLEDGED
- نهائية: RESOLVED, DISMISSED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | SYS:rule condition met | RAISED | no non-terminal alert for (rule, subject) inside dedupe window; label = max(rule label, triggering object labels) | EVT-ALR-RAISED | — |
| RAISED, ACKNOWLEDGED | SYS:condition met again within dedupe window | (بلا تغيير) | occurrence counter + last_occurrence updated | EVT-ALR-REPEATED | — |
| RAISED | CMD-ALR-ACKNOWLEDGE | ACKNOWLEDGED | actor is a recipient | EVT-ALR-ACKNOWLEDGED | NOT_A_RECIPIENT |
| RAISED | SYS:unacknowledged beyond escalation delay | (بلا تغيير) | escalates to the rule's escalation recipients | EVT-ALR-ESCALATED | — |
| RAISED, ACKNOWLEDGED | CMD-ALR-RESOLVE | RESOLVED | actor is a recipient; note | EVT-ALR-RESOLVED | NOT_A_RECIPIENT |
| RAISED, ACKNOWLEDGED | SYS:condition cleared and rule auto_resolve | RESOLVED | system | EVT-ALR-RESOLVED | — |
| RAISED, ACKNOWLEDGED | CMD-ALR-DISMISS | DISMISSED | actor is a recipient; reason (REQ-SIT-005) | EVT-ALR-DISMISSED | REASON_REQUIRED |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | SYS:rule condition met | SYS:condition met again within dedupe window | CMD-ALR-ACKNOWLEDGE | SYS:unacknowledged beyond escalation delay | CMD-ALR-RESOLVE | SYS:condition cleared and rule auto_resolve | CMD-ALR-DISMISS |
|---|---|---|---|---|---|---|---|
| ∅ | → RAISED | — | — | — | — | — | — |
| RAISED | ✗ ALERT_INVALID_STATE_TRANSITION | → RAISED | → ACKNOWLEDGED | → RAISED | → RESOLVED | → RESOLVED | → DISMISSED |
| ACKNOWLEDGED | ✗ ALERT_INVALID_STATE_TRANSITION | → ACKNOWLEDGED | ✗ ALERT_INVALID_STATE_TRANSITION | ✗ ALERT_INVALID_STATE_TRANSITION | → RESOLVED | → RESOLVED | → DISMISSED |
| RESOLVED | ✗ ALERT_INVALID_STATE_TRANSITION | ✗ ALERT_INVALID_STATE_TRANSITION | ✗ ALERT_INVALID_STATE_TRANSITION | ✗ ALERT_INVALID_STATE_TRANSITION | ✗ ALERT_INVALID_STATE_TRANSITION | ✗ ALERT_INVALID_STATE_TRANSITION | ✗ ALERT_INVALID_STATE_TRANSITION |
| DISMISSED | ✗ ALERT_INVALID_STATE_TRANSITION | ✗ ALERT_INVALID_STATE_TRANSITION | ✗ ALERT_INVALID_STATE_TRANSITION | ✗ ALERT_INVALID_STATE_TRANSITION | ✗ ALERT_INVALID_STATE_TRANSITION | ✗ ALERT_INVALID_STATE_TRANSITION | ✗ ALERT_INVALID_STATE_TRANSITION |

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
id: AGG-ALERT
bc: BC03
name: Alert
tier: T2
purpose: تنبيه صادر عن قاعدة، بدورة حياة مدققة
states:
- RAISED
- ACKNOWLEDGED
- RESOLVED
- DISMISSED
terminal:
- RESOLVED
- DISMISSED
invariants:
- 'INV-ALR-01: every transition is audited (REQ-SIT-005)'
- 'INV-ALR-02: alert label = max(rule label, labels of triggering objects); only recipients
  cleared for that label receive it — others receive nothing, not a redacted alert
  (REQ-SIT-006)'
- 'INV-ALR-03: dedupe: at most one non-terminal alert per (rule, subject) within the
  dedupe window'
entities:
- Occurrence (at, trigger_ref)
requirements:
- REQ-SIT-004
- REQ-SIT-005
- REQ-SIT-006
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: SYS:rule condition met
  to: RAISED
  guard: no non-terminal alert for (rule, subject) inside dedupe window; label = max(rule
    label, triggering object labels)
  event: EVT-ALR-RAISED
  guard_error: null
- from:
  - RAISED
  - ACKNOWLEDGED
  command: SYS:condition met again within dedupe window
  to: '='
  guard: occurrence counter + last_occurrence updated
  event: EVT-ALR-REPEATED
  guard_error: null
- from:
  - RAISED
  command: CMD-ALR-ACKNOWLEDGE
  to: ACKNOWLEDGED
  guard: actor is a recipient
  event: EVT-ALR-ACKNOWLEDGED
  guard_error: NOT_A_RECIPIENT
- from:
  - RAISED
  command: SYS:unacknowledged beyond escalation delay
  to: '='
  guard: escalates to the rule's escalation recipients
  event: EVT-ALR-ESCALATED
  guard_error: null
- from:
  - RAISED
  - ACKNOWLEDGED
  command: CMD-ALR-RESOLVE
  to: RESOLVED
  guard: actor is a recipient; note
  event: EVT-ALR-RESOLVED
  guard_error: NOT_A_RECIPIENT
- from:
  - RAISED
  - ACKNOWLEDGED
  command: SYS:condition cleared and rule auto_resolve
  to: RESOLVED
  guard: system
  event: EVT-ALR-RESOLVED
  guard_error: null
- from:
  - RAISED
  - ACKNOWLEDGED
  command: CMD-ALR-DISMISS
  to: DISMISSED
  guard: actor is a recipient; reason (REQ-SIT-005)
  event: EVT-ALR-DISMISSED
  guard_error: REASON_REQUIRED
```

</details>
