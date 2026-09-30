---
id: AGG-PRODUCT-TEMPLATE
type: aggregate
title: Product Template
wave: W4
slice: SLC-12
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC06
importance_tier: T2
personal_data: false
traces:
  satisfies:
  - REQ-PRD-001
  state_machine: SM-PRODUCT-TEMPLATE
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-PRODUCT-TEMPLATE — Product Template

**الغرض:** قالب منتج بأقسام وربط بيانات، بإصدارات  
**السياق:** BC06 · **المستوى:** T2 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-PTM-01** — bindings call only declared queries (no free-form data access), so products obey the same authorization as the UI
- **INV-PTM-02** — products pin the template version

## مكونات داخلية

- Section
- Binding (query id, parameters)

## الحالات

- غير نهائية: DRAFT, ACTIVE
- نهائية: RETIRED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-PTM-DEFINE | DRAFT | code unique; product kind ∈ {report, briefing, map_product, analytical_product} | EVT-PTM-DEFINED | TEMPLATE_INVALID |
| DRAFT, ACTIVE | CMD-PTM-EDIT | (بلا تغيير) | sections valid (text, map, chart, table, key_judgments, citations); every data binding is a declared platform query with typed parameters; ACTIVE → new version | EVT-PTM-EDITED | TEMPLATE_INVALID |
| DRAFT | CMD-PTM-ACTIVATE | ACTIVE | sample generation succeeded; approver ≠ author | EVT-PTM-ACTIVATED | SEGREGATION_OF_DUTIES |
| ACTIVE | CMD-PTM-RETIRE | RETIRED | reason; existing products keep their pinned version | EVT-PTM-RETIRED | REASON_REQUIRED |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-PTM-DEFINE | CMD-PTM-EDIT | CMD-PTM-ACTIVATE | CMD-PTM-RETIRE |
|---|---|---|---|---|
| ∅ | → DRAFT | — | — | — |
| DRAFT | ✗ PRODUCT_TEMPLATE_INVALID_STATE_TRANSITION | → DRAFT | → ACTIVE | ✗ PRODUCT_TEMPLATE_INVALID_STATE_TRANSITION |
| ACTIVE | ✗ PRODUCT_TEMPLATE_INVALID_STATE_TRANSITION | → ACTIVE | ✗ PRODUCT_TEMPLATE_INVALID_STATE_TRANSITION | → RETIRED |
| RETIRED | ✗ PRODUCT_TEMPLATE_INVALID_STATE_TRANSITION | ✗ PRODUCT_TEMPLATE_INVALID_STATE_TRANSITION | ✗ PRODUCT_TEMPLATE_INVALID_STATE_TRANSITION | ✗ PRODUCT_TEMPLATE_INVALID_STATE_TRANSITION |

## التزامن وعدم التكرار

- Optimistic concurrency: `If-Match: <version>`؛ عدم التطابق → `VERSION_CONFLICT` (HTTP 409) دون تغيير.
- كل أمر يحمل `Idempotency-Key`؛ التكرار يعيد النتيجة الأصلية؛ نفس المفتاح بحمولة مختلفة → `IDEMPOTENCY_KEY_REUSED` (HTTP 422).
- الأوامر التي تبدأ بـ `SYS:` يطلقها المجدول بهوية عبء عمل، وتخضع لنفس الثوابت.

## الحفظ

- State + history (إصدار غير قابل للتعديل لكل تغيير، ADR-P02) + outbox + audit outbox في نفس المعاملة (FIT-04).
- النموذج المنطقي: `06-data/logical-model/slc-12.md`.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
id: AGG-PRODUCT-TEMPLATE
bc: BC06
name: Product Template
tier: T2
purpose: قالب منتج بأقسام وربط بيانات، بإصدارات
states:
- DRAFT
- ACTIVE
- RETIRED
terminal:
- RETIRED
invariants:
- 'INV-PTM-01: bindings call only declared queries (no free-form data access), so
  products obey the same authorization as the UI'
- 'INV-PTM-02: products pin the template version'
entities:
- Section
- Binding (query id, parameters)
requirements:
- REQ-PRD-001
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-PTM-DEFINE
  to: DRAFT
  guard: code unique; product kind ∈ {report, briefing, map_product, analytical_product}
  event: EVT-PTM-DEFINED
  guard_error: TEMPLATE_INVALID
- from:
  - DRAFT
  - ACTIVE
  command: CMD-PTM-EDIT
  to: '='
  guard: sections valid (text, map, chart, table, key_judgments, citations); every
    data binding is a declared platform query with typed parameters; ACTIVE → new
    version
  event: EVT-PTM-EDITED
  guard_error: TEMPLATE_INVALID
- from:
  - DRAFT
  command: CMD-PTM-ACTIVATE
  to: ACTIVE
  guard: sample generation succeeded; approver ≠ author
  event: EVT-PTM-ACTIVATED
  guard_error: SEGREGATION_OF_DUTIES
- from:
  - ACTIVE
  command: CMD-PTM-RETIRE
  to: RETIRED
  guard: reason; existing products keep their pinned version
  event: EVT-PTM-RETIRED
  guard_error: REASON_REQUIRED
```

</details>
