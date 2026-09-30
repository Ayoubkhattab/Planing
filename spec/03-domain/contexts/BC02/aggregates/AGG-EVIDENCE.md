---
id: AGG-EVIDENCE
type: aggregate
title: Evidence
wave: W4
slice: SLC-02
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC02
importance_tier: T1
personal_data: false
traces:
  satisfies:
  - REQ-INF-003
  - REQ-INF-004
  state_machine: SM-EVIDENCE
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-EVIDENCE — Evidence

**الغرض:** مادة تدعم أو تنفي ادعاءً، بسلسلة حيازة  
**السياق:** BC02 · **المستوى:** T1 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-EVD-01** — evidence is never deleted; withdrawal keeps it and its links
- **INV-EVD-02** — after SEALED only custody and label change
- **INV-EVD-03** — custody chain is gapless

## مكونات داخلية

- CustodyEntry
- Locator

## الحالات

- غير نهائية: REGISTERED, SEALED
- نهائية: WITHDRAWN
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-EVD-REGISTER | REGISTERED | attachment STORED or observation_ref; type in RD-EVIDENCE-TYPES; source ACTIVE | EVT-EVD-REGISTERED | EVIDENCE_INVALID |
| REGISTERED | CMD-EVD-UPDATE-LOCATOR | (بلا تغيير) | locator within attachment bounds | EVT-EVD-LOCATOR-UPDATED | LOCATOR_INVALID |
| REGISTERED | CMD-EVD-SEAL | SEALED | integrity hash over metadata + attachment hash | EVT-EVD-SEALED | — |
| REGISTERED, SEALED | CMD-EVD-TRANSFER-CUSTODY | (بلا تغيير) | actor is current holder or custodian role; new holder named | EVT-EVD-CUSTODY-TRANSFERRED | CUSTODY_INVALID |
| REGISTERED, SEALED, WITHDRAWN | CMD-EVD-RECLASSIFY | (بلا تغيير) | authority per tenant policy (REQ-GOV-004); new version; bumps object security_version | EVT-EVD-RECLASSIFIED | CLASSIFICATION_CHANGE_NOT_AUTHORIZED |
| REGISTERED, SEALED | CMD-EVD-WITHDRAW | WITHDRAWN | reason (e.g. forged); links kept and flagged; dependent verification re-evaluated | EVT-EVD-WITHDRAWN | REASON_REQUIRED |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-EVD-REGISTER | CMD-EVD-UPDATE-LOCATOR | CMD-EVD-SEAL | CMD-EVD-TRANSFER-CUSTODY | CMD-EVD-RECLASSIFY | CMD-EVD-WITHDRAW |
|---|---|---|---|---|---|---|
| ∅ | → REGISTERED | — | — | — | — | — |
| REGISTERED | ✗ EVIDENCE_INVALID_STATE_TRANSITION | → REGISTERED | → SEALED | → REGISTERED | → REGISTERED | → WITHDRAWN |
| SEALED | ✗ EVIDENCE_INVALID_STATE_TRANSITION | ✗ EVIDENCE_INVALID_STATE_TRANSITION | ✗ EVIDENCE_INVALID_STATE_TRANSITION | → SEALED | → SEALED | → WITHDRAWN |
| WITHDRAWN | ✗ EVIDENCE_INVALID_STATE_TRANSITION | ✗ EVIDENCE_INVALID_STATE_TRANSITION | ✗ EVIDENCE_INVALID_STATE_TRANSITION | ✗ EVIDENCE_INVALID_STATE_TRANSITION | → WITHDRAWN | ✗ EVIDENCE_INVALID_STATE_TRANSITION |

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
id: AGG-EVIDENCE
bc: BC02
name: Evidence
tier: T1
purpose: مادة تدعم أو تنفي ادعاءً، بسلسلة حيازة
states:
- REGISTERED
- SEALED
- WITHDRAWN
terminal:
- WITHDRAWN
invariants:
- 'INV-EVD-01: evidence is never deleted; withdrawal keeps it and its links'
- 'INV-EVD-02: after SEALED only custody and label change'
- 'INV-EVD-03: custody chain is gapless'
entities:
- CustodyEntry
- Locator
requirements:
- REQ-INF-003
- REQ-INF-004
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-EVD-REGISTER
  to: REGISTERED
  guard: attachment STORED or observation_ref; type in RD-EVIDENCE-TYPES; source ACTIVE
  event: EVT-EVD-REGISTERED
  guard_error: EVIDENCE_INVALID
- from:
  - REGISTERED
  command: CMD-EVD-UPDATE-LOCATOR
  to: '='
  guard: locator within attachment bounds
  event: EVT-EVD-LOCATOR-UPDATED
  guard_error: LOCATOR_INVALID
- from:
  - REGISTERED
  command: CMD-EVD-SEAL
  to: SEALED
  guard: integrity hash over metadata + attachment hash
  event: EVT-EVD-SEALED
  guard_error: null
- from:
  - REGISTERED
  - SEALED
  command: CMD-EVD-TRANSFER-CUSTODY
  to: '='
  guard: actor is current holder or custodian role; new holder named
  event: EVT-EVD-CUSTODY-TRANSFERRED
  guard_error: CUSTODY_INVALID
- from:
  - REGISTERED
  - SEALED
  - WITHDRAWN
  command: CMD-EVD-RECLASSIFY
  to: '='
  guard: authority per tenant policy (REQ-GOV-004); new version; bumps object security_version
  event: EVT-EVD-RECLASSIFIED
  guard_error: CLASSIFICATION_CHANGE_NOT_AUTHORIZED
- from:
  - REGISTERED
  - SEALED
  command: CMD-EVD-WITHDRAW
  to: WITHDRAWN
  guard: reason (e.g. forged); links kept and flagged; dependent verification re-evaluated
  event: EVT-EVD-WITHDRAWN
  guard_error: REASON_REQUIRED
```

</details>
