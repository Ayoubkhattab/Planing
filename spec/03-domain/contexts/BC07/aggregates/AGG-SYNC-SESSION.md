---
id: AGG-SYNC-SESSION
type: aggregate
title: Sync Session
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
  - REQ-OFF-001
  - REQ-OFF-003
  - REQ-OFF-004
  - REQ-OFF-006
  state_machine: SM-SYNC-SESSION
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-SYNC-SESSION — Sync Session

**الغرض:** جلسة مزامنة جهاز: مصافحة، رفع أوامر مرتبة، تطبيقها، ثم تنزيل الفروق  
**السياق:** BC07 · **المستوى:** T2 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-SYN-01** — commands are applied in device seq order; client_command_id makes re-delivery idempotent (REQ-OFF-006)
- **INV-SYN-02** — record time = server receipt; device time stored and corrected by the measured clock offset (REQ-OFF-003)
- **INV-SYN-03** — the gateway applies commands through owner-context APIs with the user's delegated SecurityContext — never bypassing owner guards or policies
- **INV-SYN-04** — no last-write-wins for T1/T2: a state-changing command whose base_version ≠ current becomes a sync conflict (REQ-OFF-004)

## مكونات داخلية

- CommandEnvelope (client_command_id, seq, target, base_version, device_time, payload, signature)
- BatchReceipt

## الحالات

- غير نهائية: OPEN, APPLYING
- نهائية: COMPLETED, COMPLETED_WITH_CONFLICTS, FAILED, REJECTED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-SYN-OPEN | OPEN | device ACTIVE; user authenticated (fresh token); device signature on handshake; clock offset measured (server − device); resumes after last acknowledged seq | EVT-SYN-OPENED | DEVICE_NOT_ACTIVE |
| ∅ (إنشاء) | SYS:device LOST or SUSPENDED at handshake | REJECTED | returns wipe (LOST) or stop (SUSPENDED) instruction only | EVT-SYN-REJECTED | — |
| OPEN, APPLYING | CMD-SYN-UPLOAD-BATCH | APPLYING | ≤ 200 commands; contiguous seq after last acknowledged; each envelope signed by device key; batch hash chain continues | EVT-SYN-BATCH-RECEIVED | SEQUENCE_GAP |
| APPLYING | SYS:all uploaded commands processed without conflict | COMPLETED | device declared end of queue; every command applied or idempotently recognized | EVT-SYN-COMPLETED | — |
| APPLYING | SYS:all processed with ≥ 1 sync conflict | COMPLETED_WITH_CONFLICTS | conflicts opened as AGG-SYNC-CONFLICT | EVT-SYN-COMPLETED-WITH-CONFLICTS | — |
| OPEN, APPLYING | SYS:idle timeout (5 min) or transport loss | FAILED | acknowledged seq retained; next session resumes (REQ-OFF-006) | EVT-SYN-FAILED | — |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-SYN-OPEN | SYS:device LOST or SUSPENDED at handshake | CMD-SYN-UPLOAD-BATCH | SYS:all uploaded commands processed without conflict | SYS:all processed with ≥ 1 sync conflict | SYS:idle timeout (5 min) or transport loss |
|---|---|---|---|---|---|---|
| ∅ | → OPEN | → REJECTED | — | — | — | — |
| OPEN | ✗ SYNC_SESSION_INVALID_STATE_TRANSITION | ✗ SYNC_SESSION_INVALID_STATE_TRANSITION | → APPLYING | ✗ SYNC_SESSION_INVALID_STATE_TRANSITION | ✗ SYNC_SESSION_INVALID_STATE_TRANSITION | → FAILED |
| APPLYING | ✗ SYNC_SESSION_INVALID_STATE_TRANSITION | ✗ SYNC_SESSION_INVALID_STATE_TRANSITION | → APPLYING | → COMPLETED | → COMPLETED_WITH_CONFLICTS | → FAILED |
| COMPLETED | ✗ SYNC_SESSION_INVALID_STATE_TRANSITION | ✗ SYNC_SESSION_INVALID_STATE_TRANSITION | ✗ SYNC_SESSION_INVALID_STATE_TRANSITION | ✗ SYNC_SESSION_INVALID_STATE_TRANSITION | ✗ SYNC_SESSION_INVALID_STATE_TRANSITION | ✗ SYNC_SESSION_INVALID_STATE_TRANSITION |
| COMPLETED_WITH_CONFLICTS | ✗ SYNC_SESSION_INVALID_STATE_TRANSITION | ✗ SYNC_SESSION_INVALID_STATE_TRANSITION | ✗ SYNC_SESSION_INVALID_STATE_TRANSITION | ✗ SYNC_SESSION_INVALID_STATE_TRANSITION | ✗ SYNC_SESSION_INVALID_STATE_TRANSITION | ✗ SYNC_SESSION_INVALID_STATE_TRANSITION |
| FAILED | ✗ SYNC_SESSION_INVALID_STATE_TRANSITION | ✗ SYNC_SESSION_INVALID_STATE_TRANSITION | ✗ SYNC_SESSION_INVALID_STATE_TRANSITION | ✗ SYNC_SESSION_INVALID_STATE_TRANSITION | ✗ SYNC_SESSION_INVALID_STATE_TRANSITION | ✗ SYNC_SESSION_INVALID_STATE_TRANSITION |
| REJECTED | ✗ SYNC_SESSION_INVALID_STATE_TRANSITION | ✗ SYNC_SESSION_INVALID_STATE_TRANSITION | ✗ SYNC_SESSION_INVALID_STATE_TRANSITION | ✗ SYNC_SESSION_INVALID_STATE_TRANSITION | ✗ SYNC_SESSION_INVALID_STATE_TRANSITION | ✗ SYNC_SESSION_INVALID_STATE_TRANSITION |

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
id: AGG-SYNC-SESSION
bc: BC07
name: Sync Session
tier: T2
purpose: 'جلسة مزامنة جهاز: مصافحة، رفع أوامر مرتبة، تطبيقها، ثم تنزيل الفروق'
states:
- OPEN
- APPLYING
- COMPLETED
- COMPLETED_WITH_CONFLICTS
- FAILED
- REJECTED
terminal:
- COMPLETED
- COMPLETED_WITH_CONFLICTS
- FAILED
- REJECTED
invariants:
- 'INV-SYN-01: commands are applied in device seq order; client_command_id makes re-delivery
  idempotent (REQ-OFF-006)'
- 'INV-SYN-02: record time = server receipt; device time stored and corrected by the
  measured clock offset (REQ-OFF-003)'
- 'INV-SYN-03: the gateway applies commands through owner-context APIs with the user''s
  delegated SecurityContext — never bypassing owner guards or policies'
- 'INV-SYN-04: no last-write-wins for T1/T2: a state-changing command whose base_version
  ≠ current becomes a sync conflict (REQ-OFF-004)'
entities:
- CommandEnvelope (client_command_id, seq, target, base_version, device_time, payload,
  signature)
- BatchReceipt
requirements:
- REQ-OFF-001
- REQ-OFF-003
- REQ-OFF-004
- REQ-OFF-006
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-SYN-OPEN
  to: OPEN
  guard: device ACTIVE; user authenticated (fresh token); device signature on handshake;
    clock offset measured (server − device); resumes after last acknowledged seq
  event: EVT-SYN-OPENED
  guard_error: DEVICE_NOT_ACTIVE
- from: ∅
  command: SYS:device LOST or SUSPENDED at handshake
  to: REJECTED
  guard: returns wipe (LOST) or stop (SUSPENDED) instruction only
  event: EVT-SYN-REJECTED
  guard_error: null
- from:
  - OPEN
  - APPLYING
  command: CMD-SYN-UPLOAD-BATCH
  to: APPLYING
  guard: ≤ 200 commands; contiguous seq after last acknowledged; each envelope signed
    by device key; batch hash chain continues
  event: EVT-SYN-BATCH-RECEIVED
  guard_error: SEQUENCE_GAP
- from:
  - APPLYING
  command: SYS:all uploaded commands processed without conflict
  to: COMPLETED
  guard: device declared end of queue; every command applied or idempotently recognized
  event: EVT-SYN-COMPLETED
  guard_error: null
- from:
  - APPLYING
  command: SYS:all processed with ≥ 1 sync conflict
  to: COMPLETED_WITH_CONFLICTS
  guard: conflicts opened as AGG-SYNC-CONFLICT
  event: EVT-SYN-COMPLETED-WITH-CONFLICTS
  guard_error: null
- from:
  - OPEN
  - APPLYING
  command: SYS:idle timeout (5 min) or transport loss
  to: FAILED
  guard: acknowledged seq retained; next session resumes (REQ-OFF-006)
  event: EVT-SYN-FAILED
  guard_error: null
```

</details>
