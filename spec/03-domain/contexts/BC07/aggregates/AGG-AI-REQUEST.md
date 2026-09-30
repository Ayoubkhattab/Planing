---
id: AGG-AI-REQUEST
type: aggregate
title: AI Request
wave: W4
slice: SLC-10
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC07
importance_tier: T1 (when its output is used) / T2
personal_data: false
traces:
  satisfies:
  - REQ-AI-001
  - REQ-AI-002
  - REQ-AI-003
  - REQ-AI-004
  - REQ-AI-007
  - REQ-AI-008
  - REQ-AI-011
  - REQ-AI-012
  state_machine: SM-AI-REQUEST
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-AI-REQUEST — AI Request

**الغرض:** طلب ذكاء اصطناعي واحد بمساره الكامل: سياسة، استرجاع مصرّح، حزمة سياق، نموذج، تأريض  
**السياق:** BC07 · **المستوى:** T1 (when its output is used) / T2 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-AIR-01** — the context package contains only items the requesting user may see at request time (REQ-AI-002)
- **INV-AIR-02** — retrieved content is data: it can never add tools, change recipients, widen scope or raise AIL (REQ-AI-012)
- **INV-AIR-03** — every COMPLETED statement has ≥ 1 citation to a context item (REQ-AI-004)
- **INV-AIR-04** — request, context package hash, model version, prompt template version and output are recorded (REQ-AI-001, BRL-009)
- **INV-AIR-05** — classified context never goes to an external model (REQ-AI-011)

## مكونات داخلية

- ContextPackage (items, hash)
- ContextItem (urn, version, known_at, label, score)
- Statement (text, citations)
- GuardResult

## الحالات

- غير نهائية: RECEIVED, RETRIEVING, GENERATING
- نهائية: COMPLETED, INSUFFICIENT_EVIDENCE, REFUSED, FAILED, CANCELLED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-AIR-SUBMIT | RECEIVED | operation ∈ AI autonomy matrix and allowed at the tenant's routing; user authenticated; purpose; input size ≤ limit; per-tenant AI quota | EVT-AIR-RECEIVED | AI_OPERATION_NOT_ALLOWED |
| RECEIVED | SYS:policy denied | REFUSED | PDP on (user, ai.<operation>, scope) denied or AIL above matrix | EVT-AIR-REFUSED | — |
| RECEIVED | SYS:retrieval started | RETRIEVING | authorized hybrid retrieval as the user (SPEC-AI §2) | EVT-AIR-RETRIEVING | — |
| RETRIEVING | SYS:context package sealed | GENERATING | context items pinned (URN + version/known_at + label); package hash; token budget respected | EVT-AIR-CONTEXT-SEALED | — |
| RETRIEVING | SYS:no sufficient evidence retrieved | INSUFFICIENT_EVIDENCE | coverage below threshold (SPEC-AI §4) | EVT-AIR-INSUFFICIENT-EVIDENCE | — |
| GENERATING | SYS:output grounded | COMPLETED | every statement cites ≥ 1 context item; citation check passed; output label = max(context labels); guard checks passed (SPEC-AI §5) | EVT-AIR-COMPLETED | — |
| GENERATING | SYS:output not grounded | INSUFFICIENT_EVIDENCE | ungrounded statements removed leave no answer | EVT-AIR-INSUFFICIENT-EVIDENCE | — |
| RETRIEVING, GENERATING | SYS:error or timeout | FAILED | error recorded | EVT-AIR-FAILED | — |
| RECEIVED, RETRIEVING, GENERATING | CMD-AIR-CANCEL | CANCELLED | requester | EVT-AIR-CANCELLED | — |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-AIR-SUBMIT | SYS:policy denied | SYS:retrieval started | SYS:context package sealed | SYS:no sufficient evidence retrieved | SYS:output grounded | SYS:output not grounded | SYS:error or timeout | CMD-AIR-CANCEL |
|---|---|---|---|---|---|---|---|---|---|
| ∅ | → RECEIVED | — | — | — | — | — | — | — | — |
| RECEIVED | ✗ AI_REQUEST_INVALID_STATE_TRANSITION | → REFUSED | → RETRIEVING | ✗ AI_REQUEST_INVALID_STATE_TRANSITION | ✗ AI_REQUEST_INVALID_STATE_TRANSITION | ✗ AI_REQUEST_INVALID_STATE_TRANSITION | ✗ AI_REQUEST_INVALID_STATE_TRANSITION | ✗ AI_REQUEST_INVALID_STATE_TRANSITION | → CANCELLED |
| RETRIEVING | ✗ AI_REQUEST_INVALID_STATE_TRANSITION | ✗ AI_REQUEST_INVALID_STATE_TRANSITION | ✗ AI_REQUEST_INVALID_STATE_TRANSITION | → GENERATING | → INSUFFICIENT_EVIDENCE | ✗ AI_REQUEST_INVALID_STATE_TRANSITION | ✗ AI_REQUEST_INVALID_STATE_TRANSITION | → FAILED | → CANCELLED |
| GENERATING | ✗ AI_REQUEST_INVALID_STATE_TRANSITION | ✗ AI_REQUEST_INVALID_STATE_TRANSITION | ✗ AI_REQUEST_INVALID_STATE_TRANSITION | ✗ AI_REQUEST_INVALID_STATE_TRANSITION | ✗ AI_REQUEST_INVALID_STATE_TRANSITION | → COMPLETED | → INSUFFICIENT_EVIDENCE | → FAILED | → CANCELLED |
| COMPLETED | ✗ AI_REQUEST_INVALID_STATE_TRANSITION | ✗ AI_REQUEST_INVALID_STATE_TRANSITION | ✗ AI_REQUEST_INVALID_STATE_TRANSITION | ✗ AI_REQUEST_INVALID_STATE_TRANSITION | ✗ AI_REQUEST_INVALID_STATE_TRANSITION | ✗ AI_REQUEST_INVALID_STATE_TRANSITION | ✗ AI_REQUEST_INVALID_STATE_TRANSITION | ✗ AI_REQUEST_INVALID_STATE_TRANSITION | ✗ AI_REQUEST_INVALID_STATE_TRANSITION |
| INSUFFICIENT_EVIDENCE | ✗ AI_REQUEST_INVALID_STATE_TRANSITION | ✗ AI_REQUEST_INVALID_STATE_TRANSITION | ✗ AI_REQUEST_INVALID_STATE_TRANSITION | ✗ AI_REQUEST_INVALID_STATE_TRANSITION | ✗ AI_REQUEST_INVALID_STATE_TRANSITION | ✗ AI_REQUEST_INVALID_STATE_TRANSITION | ✗ AI_REQUEST_INVALID_STATE_TRANSITION | ✗ AI_REQUEST_INVALID_STATE_TRANSITION | ✗ AI_REQUEST_INVALID_STATE_TRANSITION |
| REFUSED | ✗ AI_REQUEST_INVALID_STATE_TRANSITION | ✗ AI_REQUEST_INVALID_STATE_TRANSITION | ✗ AI_REQUEST_INVALID_STATE_TRANSITION | ✗ AI_REQUEST_INVALID_STATE_TRANSITION | ✗ AI_REQUEST_INVALID_STATE_TRANSITION | ✗ AI_REQUEST_INVALID_STATE_TRANSITION | ✗ AI_REQUEST_INVALID_STATE_TRANSITION | ✗ AI_REQUEST_INVALID_STATE_TRANSITION | ✗ AI_REQUEST_INVALID_STATE_TRANSITION |
| FAILED | ✗ AI_REQUEST_INVALID_STATE_TRANSITION | ✗ AI_REQUEST_INVALID_STATE_TRANSITION | ✗ AI_REQUEST_INVALID_STATE_TRANSITION | ✗ AI_REQUEST_INVALID_STATE_TRANSITION | ✗ AI_REQUEST_INVALID_STATE_TRANSITION | ✗ AI_REQUEST_INVALID_STATE_TRANSITION | ✗ AI_REQUEST_INVALID_STATE_TRANSITION | ✗ AI_REQUEST_INVALID_STATE_TRANSITION | ✗ AI_REQUEST_INVALID_STATE_TRANSITION |
| CANCELLED | ✗ AI_REQUEST_INVALID_STATE_TRANSITION | ✗ AI_REQUEST_INVALID_STATE_TRANSITION | ✗ AI_REQUEST_INVALID_STATE_TRANSITION | ✗ AI_REQUEST_INVALID_STATE_TRANSITION | ✗ AI_REQUEST_INVALID_STATE_TRANSITION | ✗ AI_REQUEST_INVALID_STATE_TRANSITION | ✗ AI_REQUEST_INVALID_STATE_TRANSITION | ✗ AI_REQUEST_INVALID_STATE_TRANSITION | ✗ AI_REQUEST_INVALID_STATE_TRANSITION |

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
id: AGG-AI-REQUEST
bc: BC07
name: AI Request
tier: T1 (when its output is used) / T2
purpose: 'طلب ذكاء اصطناعي واحد بمساره الكامل: سياسة، استرجاع مصرّح، حزمة سياق، نموذج،
  تأريض'
states:
- RECEIVED
- RETRIEVING
- GENERATING
- COMPLETED
- INSUFFICIENT_EVIDENCE
- REFUSED
- FAILED
- CANCELLED
terminal:
- COMPLETED
- INSUFFICIENT_EVIDENCE
- REFUSED
- FAILED
- CANCELLED
invariants:
- 'INV-AIR-01: the context package contains only items the requesting user may see
  at request time (REQ-AI-002)'
- 'INV-AIR-02: retrieved content is data: it can never add tools, change recipients,
  widen scope or raise AIL (REQ-AI-012)'
- 'INV-AIR-03: every COMPLETED statement has ≥ 1 citation to a context item (REQ-AI-004)'
- 'INV-AIR-04: request, context package hash, model version, prompt template version
  and output are recorded (REQ-AI-001, BRL-009)'
- 'INV-AIR-05: classified context never goes to an external model (REQ-AI-011)'
entities:
- ContextPackage (items, hash)
- ContextItem (urn, version, known_at, label, score)
- Statement (text, citations)
- GuardResult
requirements:
- REQ-AI-001
- REQ-AI-002
- REQ-AI-003
- REQ-AI-004
- REQ-AI-007
- REQ-AI-008
- REQ-AI-011
- REQ-AI-012
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-AIR-SUBMIT
  to: RECEIVED
  guard: operation ∈ AI autonomy matrix and allowed at the tenant's routing; user
    authenticated; purpose; input size ≤ limit; per-tenant AI quota
  event: EVT-AIR-RECEIVED
  guard_error: AI_OPERATION_NOT_ALLOWED
- from:
  - RECEIVED
  command: SYS:policy denied
  to: REFUSED
  guard: PDP on (user, ai.<operation>, scope) denied or AIL above matrix
  event: EVT-AIR-REFUSED
  guard_error: null
- from:
  - RECEIVED
  command: SYS:retrieval started
  to: RETRIEVING
  guard: authorized hybrid retrieval as the user (SPEC-AI §2)
  event: EVT-AIR-RETRIEVING
  guard_error: null
- from:
  - RETRIEVING
  command: SYS:context package sealed
  to: GENERATING
  guard: context items pinned (URN + version/known_at + label); package hash; token
    budget respected
  event: EVT-AIR-CONTEXT-SEALED
  guard_error: null
- from:
  - RETRIEVING
  command: SYS:no sufficient evidence retrieved
  to: INSUFFICIENT_EVIDENCE
  guard: coverage below threshold (SPEC-AI §4)
  event: EVT-AIR-INSUFFICIENT-EVIDENCE
  guard_error: null
- from:
  - GENERATING
  command: SYS:output grounded
  to: COMPLETED
  guard: every statement cites ≥ 1 context item; citation check passed; output label
    = max(context labels); guard checks passed (SPEC-AI §5)
  event: EVT-AIR-COMPLETED
  guard_error: null
- from:
  - GENERATING
  command: SYS:output not grounded
  to: INSUFFICIENT_EVIDENCE
  guard: ungrounded statements removed leave no answer
  event: EVT-AIR-INSUFFICIENT-EVIDENCE
  guard_error: null
- from:
  - RETRIEVING
  - GENERATING
  command: SYS:error or timeout
  to: FAILED
  guard: error recorded
  event: EVT-AIR-FAILED
  guard_error: null
- from:
  - RECEIVED
  - RETRIEVING
  - GENERATING
  command: CMD-AIR-CANCEL
  to: CANCELLED
  guard: requester
  event: EVT-AIR-CANCELLED
  guard_error: null
```

</details>
