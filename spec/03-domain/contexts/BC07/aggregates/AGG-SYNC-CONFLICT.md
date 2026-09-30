---
id: AGG-SYNC-CONFLICT
type: aggregate
title: Sync Conflict
wave: W4
slice: SLC-11
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC07
importance_tier: T2
personal_data: false
traces:
  satisfies:
  - REQ-OFF-004
  state_machine: SM-SYNC-CONFLICT
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-SYNC-CONFLICT — Sync Conflict

**الغرض:** أمر ميداني لم يُطبق لأن الحالة تغيرت؛ ينتظر قراراً بشرياً  
**السياق:** BC07 · **المستوى:** T2 · **بيانات شخصية:** لا

> Claim-level disagreements are not sync conflicts: observations are append-only and their claims flow into BC02's conflict engine (CF-01..04). CF-05 is for stale state-changing commands only (CR-49).

## الثوابت (Invariants)

- **INV-SCF-01** — the original field command and device time are preserved as evidence of what the field user did
- **INV-SCF-02** — reapplying never bypasses the owner's state machine, guards or policies
- **INV-SCF-03** — commands recorded after a device's reported-lost time always open a conflict (never auto-applied)

## مكونات داخلية

- OriginalEnvelope
- StateSnapshot

## الحالات

- غير نهائية: OPEN
- نهائية: RESOLVED_APPLIED, RESOLVED_DISCARDED, RESOLVED_MANUAL
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | SYS:stale state-changing command | OPEN | rule CF-05: base_version ≠ current; stores original envelope, current state snapshot and owner rejection reason; reviewer = owner-context default (task: owner/Planner; observation: Analyst) | EVT-SCF-OPENED | — |
| OPEN | CMD-SCF-ASSIGN | (بلا تغيير) | assignee authorized on the target | EVT-SCF-ASSIGNED | REVIEWER_NOT_AUTHORIZED |
| OPEN | CMD-SCF-REAPPLY | RESOLVED_APPLIED | reviewer re-sends the original intent against the current version; owner-context accepts (its guards still apply) | EVT-SCF-REAPPLIED | OWNER_REJECTED |
| OPEN | CMD-SCF-DISCARD | RESOLVED_DISCARDED | reason; field user notified | EVT-SCF-DISCARDED | REASON_REQUIRED |
| OPEN | CMD-SCF-RESOLVE-MANUALLY | RESOLVED_MANUAL | note + reference to the alternative action taken | EVT-SCF-RESOLVED-MANUALLY | REASON_REQUIRED |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | SYS:stale state-changing command | CMD-SCF-ASSIGN | CMD-SCF-REAPPLY | CMD-SCF-DISCARD | CMD-SCF-RESOLVE-MANUALLY |
|---|---|---|---|---|---|
| ∅ | → OPEN | — | — | — | — |
| OPEN | ✗ SYNC_CONFLICT_INVALID_STATE_TRANSITION | → OPEN | → RESOLVED_APPLIED | → RESOLVED_DISCARDED | → RESOLVED_MANUAL |
| RESOLVED_APPLIED | ✗ SYNC_CONFLICT_INVALID_STATE_TRANSITION | ✗ SYNC_CONFLICT_INVALID_STATE_TRANSITION | ✗ SYNC_CONFLICT_INVALID_STATE_TRANSITION | ✗ SYNC_CONFLICT_INVALID_STATE_TRANSITION | ✗ SYNC_CONFLICT_INVALID_STATE_TRANSITION |
| RESOLVED_DISCARDED | ✗ SYNC_CONFLICT_INVALID_STATE_TRANSITION | ✗ SYNC_CONFLICT_INVALID_STATE_TRANSITION | ✗ SYNC_CONFLICT_INVALID_STATE_TRANSITION | ✗ SYNC_CONFLICT_INVALID_STATE_TRANSITION | ✗ SYNC_CONFLICT_INVALID_STATE_TRANSITION |
| RESOLVED_MANUAL | ✗ SYNC_CONFLICT_INVALID_STATE_TRANSITION | ✗ SYNC_CONFLICT_INVALID_STATE_TRANSITION | ✗ SYNC_CONFLICT_INVALID_STATE_TRANSITION | ✗ SYNC_CONFLICT_INVALID_STATE_TRANSITION | ✗ SYNC_CONFLICT_INVALID_STATE_TRANSITION |

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
id: AGG-SYNC-CONFLICT
bc: BC07
name: Sync Conflict
tier: T2
purpose: أمر ميداني لم يُطبق لأن الحالة تغيرت؛ ينتظر قراراً بشرياً
states:
- OPEN
- RESOLVED_APPLIED
- RESOLVED_DISCARDED
- RESOLVED_MANUAL
terminal:
- RESOLVED_APPLIED
- RESOLVED_DISCARDED
- RESOLVED_MANUAL
invariants:
- 'INV-SCF-01: the original field command and device time are preserved as evidence
  of what the field user did'
- 'INV-SCF-02: reapplying never bypasses the owner''s state machine, guards or policies'
- 'INV-SCF-03: commands recorded after a device''s reported-lost time always open
  a conflict (never auto-applied)'
entities:
- OriginalEnvelope
- StateSnapshot
requirements:
- REQ-OFF-004
notes: 'Claim-level disagreements are not sync conflicts: observations are append-only
  and their claims flow into BC02''s conflict engine (CF-01..04). CF-05 is for stale
  state-changing commands only (CR-49).'
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: SYS:stale state-changing command
  to: OPEN
  guard: 'rule CF-05: base_version ≠ current; stores original envelope, current state
    snapshot and owner rejection reason; reviewer = owner-context default (task: owner/Planner;
    observation: Analyst)'
  event: EVT-SCF-OPENED
  guard_error: null
- from:
  - OPEN
  command: CMD-SCF-ASSIGN
  to: '='
  guard: assignee authorized on the target
  event: EVT-SCF-ASSIGNED
  guard_error: REVIEWER_NOT_AUTHORIZED
- from:
  - OPEN
  command: CMD-SCF-REAPPLY
  to: RESOLVED_APPLIED
  guard: reviewer re-sends the original intent against the current version; owner-context
    accepts (its guards still apply)
  event: EVT-SCF-REAPPLIED
  guard_error: OWNER_REJECTED
- from:
  - OPEN
  command: CMD-SCF-DISCARD
  to: RESOLVED_DISCARDED
  guard: reason; field user notified
  event: EVT-SCF-DISCARDED
  guard_error: REASON_REQUIRED
- from:
  - OPEN
  command: CMD-SCF-RESOLVE-MANUALLY
  to: RESOLVED_MANUAL
  guard: note + reference to the alternative action taken
  event: EVT-SCF-RESOLVED-MANUALLY
  guard_error: REASON_REQUIRED
```

</details>
