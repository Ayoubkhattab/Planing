---
id: AGG-EXTERNAL-ID
type: aggregate
title: External Identifier Mapping
wave: W4
slice: SLC-02
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC02
importance_tier: T2
personal_data: false
traces:
  satisfies:
  - REQ-INF-036
  state_machine: SM-EXTERNAL-ID
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-EXTERNAL-ID — External Identifier Mapping

**الغرض:** ربط معرّف نظام خارجي بكائن داخلي لفترة  
**السياق:** BC02 · **المستوى:** T2 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-EXT-01** — at any time t, (tenant, system, external_id) maps to at most one object
- **INV-EXT-02** — mappings are never deleted

## الحالات

- غير نهائية: ACTIVE
- نهائية: ENDED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-EXT-MAP | ACTIVE | (system, external_id) has no ACTIVE mapping; target exists | EVT-EXT-MAPPED | EXTERNAL_ID_TAKEN |
| ACTIVE | CMD-EXT-END | ENDED | reason; valid_to set | EVT-EXT-ENDED | REASON_REQUIRED |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-EXT-MAP | CMD-EXT-END |
|---|---|---|
| ∅ | → ACTIVE | — |
| ACTIVE | ✗ EXTERNAL_ID_INVALID_STATE_TRANSITION | → ENDED |
| ENDED | ✗ EXTERNAL_ID_INVALID_STATE_TRANSITION | ✗ EXTERNAL_ID_INVALID_STATE_TRANSITION |

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
id: AGG-EXTERNAL-ID
bc: BC02
name: External Identifier Mapping
tier: T2
purpose: ربط معرّف نظام خارجي بكائن داخلي لفترة
states:
- ACTIVE
- ENDED
terminal:
- ENDED
invariants:
- 'INV-EXT-01: at any time t, (tenant, system, external_id) maps to at most one object'
- 'INV-EXT-02: mappings are never deleted'
entities: []
requirements:
- REQ-INF-036
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-EXT-MAP
  to: ACTIVE
  guard: (system, external_id) has no ACTIVE mapping; target exists
  event: EVT-EXT-MAPPED
  guard_error: EXTERNAL_ID_TAKEN
- from:
  - ACTIVE
  command: CMD-EXT-END
  to: ENDED
  guard: reason; valid_to set
  event: EVT-EXT-ENDED
  guard_error: REASON_REQUIRED
```

</details>
