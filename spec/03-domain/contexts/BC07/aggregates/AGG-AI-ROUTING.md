---
id: AGG-AI-ROUTING
type: aggregate
title: AI Routing Configuration
wave: W4
slice: SLC-10
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC07
importance_tier: T2
personal_data: false
traces:
  satisfies:
  - REQ-AI-008
  - REQ-AI-011
  state_machine: SM-AI-ROUTING
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-AI-ROUTING — AI Routing Configuration

**الغرض:** ربط كل عملية AI بنموذج إنتاجي وقالب تعليمات وحدود الاستقلالية لكل مستأجر  
**السياق:** BC07 · **المستوى:** T2 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-RTG-01** — max AIL per operation never exceeds the platform autonomy matrix (AIL5 unreachable) — REQ-AI-008
- **INV-RTG-02** — prompt templates are versioned and immutable once referenced
- **INV-RTG-03** — exactly one ACTIVE routing per tenant

## مكونات داخلية

- Route (operation, model version, prompt template, tools, max AIL, external_allowed)

## الحالات

- غير نهائية: DRAFT, ACTIVE
- نهائية: SUPERSEDED, DISCARDED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-RTG-DRAFT | DRAFT | AI governance authority; ≤ 1 DRAFT per tenant | EVT-RTG-DRAFTED | DRAFT_EXISTS |
| DRAFT | CMD-RTG-EDIT | (بلا تغيير) | for each operation: model version in PRODUCTION (or STAGED with canary share), prompt template version, allowed tools, max AIL ≤ autonomy matrix, external model allowed only for unclassified and only if tenant policy allows | EVT-RTG-EDITED | ROUTING_INVALID |
| DRAFT | CMD-RTG-ACTIVATE | ACTIVE | approver ≠ author; previous ACTIVE → SUPERSEDED | EVT-RTG-ACTIVATED | SEGREGATION_OF_DUTIES |
| DRAFT | CMD-RTG-DISCARD | DISCARDED | reason | EVT-RTG-DISCARDED | REASON_REQUIRED |
| ACTIVE | SYS:successor activated | SUPERSEDED | system | EVT-RTG-SUPERSEDED | — |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-RTG-DRAFT | CMD-RTG-EDIT | CMD-RTG-ACTIVATE | CMD-RTG-DISCARD | SYS:successor activated |
|---|---|---|---|---|---|
| ∅ | → DRAFT | — | — | — | — |
| DRAFT | ✗ AI_ROUTING_INVALID_STATE_TRANSITION | → DRAFT | → ACTIVE | → DISCARDED | ✗ AI_ROUTING_INVALID_STATE_TRANSITION |
| ACTIVE | ✗ AI_ROUTING_INVALID_STATE_TRANSITION | ✗ AI_ROUTING_INVALID_STATE_TRANSITION | ✗ AI_ROUTING_INVALID_STATE_TRANSITION | ✗ AI_ROUTING_INVALID_STATE_TRANSITION | → SUPERSEDED |
| SUPERSEDED | ✗ AI_ROUTING_INVALID_STATE_TRANSITION | ✗ AI_ROUTING_INVALID_STATE_TRANSITION | ✗ AI_ROUTING_INVALID_STATE_TRANSITION | ✗ AI_ROUTING_INVALID_STATE_TRANSITION | ✗ AI_ROUTING_INVALID_STATE_TRANSITION |
| DISCARDED | ✗ AI_ROUTING_INVALID_STATE_TRANSITION | ✗ AI_ROUTING_INVALID_STATE_TRANSITION | ✗ AI_ROUTING_INVALID_STATE_TRANSITION | ✗ AI_ROUTING_INVALID_STATE_TRANSITION | ✗ AI_ROUTING_INVALID_STATE_TRANSITION |

## التزامن وعدم التكرار

- Optimistic concurrency: `If-Match: <version>`؛ عدم التطابق → `VERSION_CONFLICT` (HTTP 409) دون تغيير.
- كل أمر يحمل `Idempotency-Key`؛ التكرار يعيد النتيجة الأصلية؛ نفس المفتاح بحمولة مختلفة → `IDEMPOTENCY_KEY_REUSED` (HTTP 422).
- الأوامر التي تبدأ بـ `SYS:` يطلقها المجدول بهوية عبء عمل، وتخضع لنفس الثوابت.

## الحفظ

- State + history (إصدار غير قابل للتعديل لكل تغيير، ADR-P02) + outbox + audit outbox في نفس المعاملة (FIT-04).
- النموذج المنطقي: `06-data/logical-model/slc-10.md`.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
id: AGG-AI-ROUTING
bc: BC07
name: AI Routing Configuration
tier: T2
purpose: ربط كل عملية AI بنموذج إنتاجي وقالب تعليمات وحدود الاستقلالية لكل مستأجر
states:
- DRAFT
- ACTIVE
- SUPERSEDED
- DISCARDED
terminal:
- SUPERSEDED
- DISCARDED
invariants:
- 'INV-RTG-01: max AIL per operation never exceeds the platform autonomy matrix (AIL5
  unreachable) — REQ-AI-008'
- 'INV-RTG-02: prompt templates are versioned and immutable once referenced'
- 'INV-RTG-03: exactly one ACTIVE routing per tenant'
entities:
- Route (operation, model version, prompt template, tools, max AIL, external_allowed)
requirements:
- REQ-AI-008
- REQ-AI-011
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-RTG-DRAFT
  to: DRAFT
  guard: AI governance authority; ≤ 1 DRAFT per tenant
  event: EVT-RTG-DRAFTED
  guard_error: DRAFT_EXISTS
- from:
  - DRAFT
  command: CMD-RTG-EDIT
  to: '='
  guard: 'for each operation: model version in PRODUCTION (or STAGED with canary share),
    prompt template version, allowed tools, max AIL ≤ autonomy matrix, external model
    allowed only for unclassified and only if tenant policy allows'
  event: EVT-RTG-EDITED
  guard_error: ROUTING_INVALID
- from:
  - DRAFT
  command: CMD-RTG-ACTIVATE
  to: ACTIVE
  guard: approver ≠ author; previous ACTIVE → SUPERSEDED
  event: EVT-RTG-ACTIVATED
  guard_error: SEGREGATION_OF_DUTIES
- from:
  - DRAFT
  command: CMD-RTG-DISCARD
  to: DISCARDED
  guard: reason
  event: EVT-RTG-DISCARDED
  guard_error: REASON_REQUIRED
- from:
  - ACTIVE
  command: SYS:successor activated
  to: SUPERSEDED
  guard: system
  event: EVT-RTG-SUPERSEDED
  guard_error: null
```

</details>
