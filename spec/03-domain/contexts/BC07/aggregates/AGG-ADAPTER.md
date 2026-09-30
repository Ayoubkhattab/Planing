---
id: AGG-ADAPTER
type: aggregate
title: Adapter
wave: W4
slice: SLC-02
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC07
importance_tier: T2
personal_data: false
traces:
  satisfies:
  - REQ-INF-005
  - REQ-INF-008
  - REQ-INF-009
  state_machine: SM-ADAPTER
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-ADAPTER — Adapter

**الغرض:** محول تكامل مسجل بمصدر وحساب خدمة وإصدار تحويل  
**السياق:** BC07 · **المستوى:** T2 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-ADP-01** — an adapter writes only through BC02 commands, as its service account
- **INV-ADP-02** — mapping versions are immutable and referenced by lineage
- **INV-ADP-03** — an adapter is bound to exactly one Source

## مكونات داخلية

- MappingVersion (spec, tests)

## الحالات

- غير نهائية: DRAFT, ACTIVE, SUSPENDED
- نهائية: RETIRED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-ADP-REGISTER | DRAFT | source ACTIVE; service account ACTIVE; mapping spec present | EVT-ADP-REGISTERED | ADAPTER_INVALID |
| DRAFT, ACTIVE | CMD-ADP-UPDATE-MAPPING | (بلا تغيير) | mapping tests pass; new immutable mapping version | EVT-ADP-MAPPING-UPDATED | MAPPING_TESTS_FAILED |
| DRAFT | CMD-ADP-ACTIVATE | ACTIVE | mapping tests pass; approver ≠ author | EVT-ADP-ACTIVATED | SEGREGATION_OF_DUTIES |
| ACTIVE | CMD-ADP-SUSPEND | SUSPENDED | reason | EVT-ADP-SUSPENDED | REASON_REQUIRED |
| SUSPENDED | CMD-ADP-RESUME | ACTIVE | — | EVT-ADP-RESUMED | — |
| DRAFT, ACTIVE, SUSPENDED | CMD-ADP-RETIRE | RETIRED | reason | EVT-ADP-RETIRED | REASON_REQUIRED |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-ADP-REGISTER | CMD-ADP-UPDATE-MAPPING | CMD-ADP-ACTIVATE | CMD-ADP-SUSPEND | CMD-ADP-RESUME | CMD-ADP-RETIRE |
|---|---|---|---|---|---|---|
| ∅ | → DRAFT | — | — | — | — | — |
| DRAFT | ✗ ADAPTER_INVALID_STATE_TRANSITION | → DRAFT | → ACTIVE | ✗ ADAPTER_INVALID_STATE_TRANSITION | ✗ ADAPTER_INVALID_STATE_TRANSITION | → RETIRED |
| ACTIVE | ✗ ADAPTER_INVALID_STATE_TRANSITION | → ACTIVE | ✗ ADAPTER_INVALID_STATE_TRANSITION | → SUSPENDED | ✗ ADAPTER_INVALID_STATE_TRANSITION | → RETIRED |
| SUSPENDED | ✗ ADAPTER_INVALID_STATE_TRANSITION | ✗ ADAPTER_INVALID_STATE_TRANSITION | ✗ ADAPTER_INVALID_STATE_TRANSITION | ✗ ADAPTER_INVALID_STATE_TRANSITION | → ACTIVE | → RETIRED |
| RETIRED | ✗ ADAPTER_INVALID_STATE_TRANSITION | ✗ ADAPTER_INVALID_STATE_TRANSITION | ✗ ADAPTER_INVALID_STATE_TRANSITION | ✗ ADAPTER_INVALID_STATE_TRANSITION | ✗ ADAPTER_INVALID_STATE_TRANSITION | ✗ ADAPTER_INVALID_STATE_TRANSITION |

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
id: AGG-ADAPTER
bc: BC07
name: Adapter
tier: T2
purpose: محول تكامل مسجل بمصدر وحساب خدمة وإصدار تحويل
states:
- DRAFT
- ACTIVE
- SUSPENDED
- RETIRED
terminal:
- RETIRED
invariants:
- 'INV-ADP-01: an adapter writes only through BC02 commands, as its service account'
- 'INV-ADP-02: mapping versions are immutable and referenced by lineage'
- 'INV-ADP-03: an adapter is bound to exactly one Source'
entities:
- MappingVersion (spec, tests)
requirements:
- REQ-INF-005
- REQ-INF-008
- REQ-INF-009
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-ADP-REGISTER
  to: DRAFT
  guard: source ACTIVE; service account ACTIVE; mapping spec present
  event: EVT-ADP-REGISTERED
  guard_error: ADAPTER_INVALID
- from:
  - DRAFT
  - ACTIVE
  command: CMD-ADP-UPDATE-MAPPING
  to: '='
  guard: mapping tests pass; new immutable mapping version
  event: EVT-ADP-MAPPING-UPDATED
  guard_error: MAPPING_TESTS_FAILED
- from:
  - DRAFT
  command: CMD-ADP-ACTIVATE
  to: ACTIVE
  guard: mapping tests pass; approver ≠ author
  event: EVT-ADP-ACTIVATED
  guard_error: SEGREGATION_OF_DUTIES
- from:
  - ACTIVE
  command: CMD-ADP-SUSPEND
  to: SUSPENDED
  guard: reason
  event: EVT-ADP-SUSPENDED
  guard_error: REASON_REQUIRED
- from:
  - SUSPENDED
  command: CMD-ADP-RESUME
  to: ACTIVE
  guard: —
  event: EVT-ADP-RESUMED
  guard_error: null
- from:
  - DRAFT
  - ACTIVE
  - SUSPENDED
  command: CMD-ADP-RETIRE
  to: RETIRED
  guard: reason
  event: EVT-ADP-RETIRED
  guard_error: REASON_REQUIRED
```

</details>
