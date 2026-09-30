---
id: AGG-AI-TOOL
type: aggregate
title: AI Tool
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
  - REQ-AI-013
  - REQ-AI-012
  state_machine: SM-AI-TOOL
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-AI-TOOL — AI Tool

**الغرض:** أداة يمكن لتشغيل AI استدعاؤها، بصلاحية وأثر ومستوى استقلالية  
**السياق:** BC07 · **المستوى:** T2 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-TOL-01** — in R2 no tool has effect 'write'; 'propose' tools create AI results for human review only (REQ-AI-013, INV-AIRS-01)
- **INV-TOL-02** — a tool executes with the requesting user's authority through the platform's own query/command APIs
- **INV-TOL-03** — tools cannot reach external networks (FIT-12)

## الحالات

- غير نهائية: DRAFT, ACTIVE, DISABLED
- نهائية: RETIRED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-TOL-REGISTER | DRAFT | name; input JSON schema; underlying platform query or command; effect ∈ {read, propose}; required permission; max AIL | EVT-TOL-REGISTERED | TOOL_INVALID |
| DRAFT | CMD-TOL-ACTIVATE | ACTIVE | security review passed (injection, exfiltration, scope); approver = Security Officer | EVT-TOL-ACTIVATED | SECURITY_REVIEW_REQUIRED |
| ACTIVE | CMD-TOL-DISABLE | DISABLED | reason | EVT-TOL-DISABLED | REASON_REQUIRED |
| DISABLED | CMD-TOL-ENABLE | ACTIVE | — | EVT-TOL-ENABLED | — |
| DRAFT, ACTIVE, DISABLED | CMD-TOL-RETIRE | RETIRED | reason | EVT-TOL-RETIRED | REASON_REQUIRED |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-TOL-REGISTER | CMD-TOL-ACTIVATE | CMD-TOL-DISABLE | CMD-TOL-ENABLE | CMD-TOL-RETIRE |
|---|---|---|---|---|---|
| ∅ | → DRAFT | — | — | — | — |
| DRAFT | ✗ AI_TOOL_INVALID_STATE_TRANSITION | → ACTIVE | ✗ AI_TOOL_INVALID_STATE_TRANSITION | ✗ AI_TOOL_INVALID_STATE_TRANSITION | → RETIRED |
| ACTIVE | ✗ AI_TOOL_INVALID_STATE_TRANSITION | ✗ AI_TOOL_INVALID_STATE_TRANSITION | → DISABLED | ✗ AI_TOOL_INVALID_STATE_TRANSITION | → RETIRED |
| DISABLED | ✗ AI_TOOL_INVALID_STATE_TRANSITION | ✗ AI_TOOL_INVALID_STATE_TRANSITION | ✗ AI_TOOL_INVALID_STATE_TRANSITION | → ACTIVE | → RETIRED |
| RETIRED | ✗ AI_TOOL_INVALID_STATE_TRANSITION | ✗ AI_TOOL_INVALID_STATE_TRANSITION | ✗ AI_TOOL_INVALID_STATE_TRANSITION | ✗ AI_TOOL_INVALID_STATE_TRANSITION | ✗ AI_TOOL_INVALID_STATE_TRANSITION |

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
id: AGG-AI-TOOL
bc: BC07
name: AI Tool
tier: T2
purpose: أداة يمكن لتشغيل AI استدعاؤها، بصلاحية وأثر ومستوى استقلالية
states:
- DRAFT
- ACTIVE
- DISABLED
- RETIRED
terminal:
- RETIRED
invariants:
- 'INV-TOL-01: in R2 no tool has effect ''write''; ''propose'' tools create AI results
  for human review only (REQ-AI-013, INV-AIRS-01)'
- 'INV-TOL-02: a tool executes with the requesting user''s authority through the platform''s
  own query/command APIs'
- 'INV-TOL-03: tools cannot reach external networks (FIT-12)'
entities: []
requirements:
- REQ-AI-013
- REQ-AI-012
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-TOL-REGISTER
  to: DRAFT
  guard: name; input JSON schema; underlying platform query or command; effect ∈ {read,
    propose}; required permission; max AIL
  event: EVT-TOL-REGISTERED
  guard_error: TOOL_INVALID
- from:
  - DRAFT
  command: CMD-TOL-ACTIVATE
  to: ACTIVE
  guard: security review passed (injection, exfiltration, scope); approver = Security
    Officer
  event: EVT-TOL-ACTIVATED
  guard_error: SECURITY_REVIEW_REQUIRED
- from:
  - ACTIVE
  command: CMD-TOL-DISABLE
  to: DISABLED
  guard: reason
  event: EVT-TOL-DISABLED
  guard_error: REASON_REQUIRED
- from:
  - DISABLED
  command: CMD-TOL-ENABLE
  to: ACTIVE
  guard: —
  event: EVT-TOL-ENABLED
  guard_error: null
- from:
  - DRAFT
  - ACTIVE
  - DISABLED
  command: CMD-TOL-RETIRE
  to: RETIRED
  guard: reason
  event: EVT-TOL-RETIRED
  guard_error: REASON_REQUIRED
```

</details>
