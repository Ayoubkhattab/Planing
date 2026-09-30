---
id: AGG-HR-SYNC-PROPOSAL
type: aggregate
title: HR Sync Proposal
wave: W4
slice: SLC-16
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC01
importance_tier: T2
personal_data: true
traces:
  satisfies:
  - REQ-INT-004
  state_machine: SM-HR-SYNC-PROPOSAL
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-HR-SYNC-PROPOSAL — HR Sync Proposal

**الغرض:** تغيير دور أو وحدة من HRIS يُقترح على المسؤول ولا يُطبق آلياً  
**السياق:** BC01 · **المستوى:** T2 · **بيانات شخصية:** نعم

## الثوابت (Invariants)

- **INV-HRS-01** — no role or access change is applied automatically from HRIS (REQ-INT-004, THR-S01-01)
- **INV-HRS-02** — 'leave' proposals are highlighted and escalated — access removal is time-critical
- **INV-HRS-03** — SCIM account disablement from the IdP remains immediate and independent of HR proposals (QAS-SEC-008)

## مكونات داخلية

- ProposedChange

## الحالات

- غير نهائية: PROPOSED
- نهائية: APPROVED, REJECTED, SUPERSEDED, EXPIRED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | SYS:HRIS change received | PROPOSED | person matched to a platform Person by HR identifier; change ∈ {join, leave, move_unit, change_position}; mapped to proposed role-assignment changes by tenant mapping table | EVT-HRS-PROPOSED | — |
| PROPOSED | CMD-HRS-APPROVE | APPROVED | Administrator in scope of the affected units; applies CMD-RAS-ASSIGN / CMD-RAS-REVOKE and, for leave, CMD-USR-DISABLE — each through its own guards | EVT-HRS-APPROVED | OWNER_REJECTED |
| PROPOSED | CMD-HRS-REJECT | REJECTED | reason | EVT-HRS-REJECTED | REASON_REQUIRED |
| PROPOSED | SYS:newer HR change for the same person | SUPERSEDED | system | EVT-HRS-SUPERSEDED | — |
| PROPOSED | SYS:14 days without decision | EXPIRED | scheduler; escalated to Security Officer for leave events | EVT-HRS-EXPIRED | — |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | SYS:HRIS change received | CMD-HRS-APPROVE | CMD-HRS-REJECT | SYS:newer HR change for the same person | SYS:14 days without decision |
|---|---|---|---|---|---|
| ∅ | → PROPOSED | — | — | — | — |
| PROPOSED | ✗ HR_SYNC_PROPOSAL_INVALID_STATE_TRANSITION | → APPROVED | → REJECTED | → SUPERSEDED | → EXPIRED |
| APPROVED | ✗ HR_SYNC_PROPOSAL_INVALID_STATE_TRANSITION | ✗ HR_SYNC_PROPOSAL_INVALID_STATE_TRANSITION | ✗ HR_SYNC_PROPOSAL_INVALID_STATE_TRANSITION | ✗ HR_SYNC_PROPOSAL_INVALID_STATE_TRANSITION | ✗ HR_SYNC_PROPOSAL_INVALID_STATE_TRANSITION |
| REJECTED | ✗ HR_SYNC_PROPOSAL_INVALID_STATE_TRANSITION | ✗ HR_SYNC_PROPOSAL_INVALID_STATE_TRANSITION | ✗ HR_SYNC_PROPOSAL_INVALID_STATE_TRANSITION | ✗ HR_SYNC_PROPOSAL_INVALID_STATE_TRANSITION | ✗ HR_SYNC_PROPOSAL_INVALID_STATE_TRANSITION |
| SUPERSEDED | ✗ HR_SYNC_PROPOSAL_INVALID_STATE_TRANSITION | ✗ HR_SYNC_PROPOSAL_INVALID_STATE_TRANSITION | ✗ HR_SYNC_PROPOSAL_INVALID_STATE_TRANSITION | ✗ HR_SYNC_PROPOSAL_INVALID_STATE_TRANSITION | ✗ HR_SYNC_PROPOSAL_INVALID_STATE_TRANSITION |
| EXPIRED | ✗ HR_SYNC_PROPOSAL_INVALID_STATE_TRANSITION | ✗ HR_SYNC_PROPOSAL_INVALID_STATE_TRANSITION | ✗ HR_SYNC_PROPOSAL_INVALID_STATE_TRANSITION | ✗ HR_SYNC_PROPOSAL_INVALID_STATE_TRANSITION | ✗ HR_SYNC_PROPOSAL_INVALID_STATE_TRANSITION |

## التزامن وعدم التكرار

- Optimistic concurrency: `If-Match: <version>`؛ عدم التطابق → `VERSION_CONFLICT` (HTTP 409) دون تغيير.
- كل أمر يحمل `Idempotency-Key`؛ التكرار يعيد النتيجة الأصلية؛ نفس المفتاح بحمولة مختلفة → `IDEMPOTENCY_KEY_REUSED` (HTTP 422).
- الأوامر التي تبدأ بـ `SYS:` يطلقها المجدول بهوية عبء عمل، وتخضع لنفس الثوابت.

## الحفظ

- State + history (إصدار غير قابل للتعديل لكل تغيير، ADR-P02) + outbox + audit outbox في نفس المعاملة (FIT-04).
- النموذج المنطقي: `06-data/logical-model/slc-16.md`.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
id: AGG-HR-SYNC-PROPOSAL
bc: BC01
name: HR Sync Proposal
tier: T2
purpose: تغيير دور أو وحدة من HRIS يُقترح على المسؤول ولا يُطبق آلياً
states:
- PROPOSED
- APPROVED
- REJECTED
- SUPERSEDED
- EXPIRED
terminal:
- APPROVED
- REJECTED
- SUPERSEDED
- EXPIRED
invariants:
- 'INV-HRS-01: no role or access change is applied automatically from HRIS (REQ-INT-004,
  THR-S01-01)'
- 'INV-HRS-02: ''leave'' proposals are highlighted and escalated — access removal
  is time-critical'
- 'INV-HRS-03: SCIM account disablement from the IdP remains immediate and independent
  of HR proposals (QAS-SEC-008)'
entities:
- ProposedChange
requirements:
- REQ-INT-004
notes: null
personal_data: true
reachability: PASS
transitions:
- from: ∅
  command: SYS:HRIS change received
  to: PROPOSED
  guard: person matched to a platform Person by HR identifier; change ∈ {join, leave,
    move_unit, change_position}; mapped to proposed role-assignment changes by tenant
    mapping table
  event: EVT-HRS-PROPOSED
  guard_error: null
- from:
  - PROPOSED
  command: CMD-HRS-APPROVE
  to: APPROVED
  guard: Administrator in scope of the affected units; applies CMD-RAS-ASSIGN / CMD-RAS-REVOKE
    and, for leave, CMD-USR-DISABLE — each through its own guards
  event: EVT-HRS-APPROVED
  guard_error: OWNER_REJECTED
- from:
  - PROPOSED
  command: CMD-HRS-REJECT
  to: REJECTED
  guard: reason
  event: EVT-HRS-REJECTED
  guard_error: REASON_REQUIRED
- from:
  - PROPOSED
  command: SYS:newer HR change for the same person
  to: SUPERSEDED
  guard: system
  event: EVT-HRS-SUPERSEDED
  guard_error: null
- from:
  - PROPOSED
  command: SYS:14 days without decision
  to: EXPIRED
  guard: scheduler; escalated to Security Officer for leave events
  event: EVT-HRS-EXPIRED
  guard_error: null
```

</details>
