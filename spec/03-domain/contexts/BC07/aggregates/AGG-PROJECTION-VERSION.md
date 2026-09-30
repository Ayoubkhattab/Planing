---
id: AGG-PROJECTION-VERSION
type: aggregate
title: Projection Version
wave: W4
slice: SLC-05
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC07
importance_tier: T3
personal_data: false
traces:
  satisfies:
  - REQ-SRC-004
  state_machine: SM-PROJECTION-VERSION
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-PROJECTION-VERSION — Projection Version

**الغرض:** إصدار فهرس بحث أو رسم يُبنى ويُرقّى بأسلوب blue/green  
**السياق:** BC07 · **المستوى:** T3 · **بيانات شخصية:** لا

> Operational aggregate (T3): the platform operator manages rebuilds; tenants never see projection versions.

## الثوابت (Invariants)

- **INV-PRJ-01** — a projection is never a source of truth; every document is reproducible from owner contexts (A07, FIT-11)
- **INV-PRJ-02** — exactly one ACTIVE version per (tenant group, kind) serves queries; promotion is atomic (alias switch)
- **INV-PRJ-03** — every document carries security labels (tenant, level, compartments, caveats, org_scope, security_version) — ADR-P06
- **INV-PRJ-04** — normalization, schema or embedding-model changes require a new version (no in-place re-analysis)

## مكونات داخلية

- SourceCheckpoint (stream, position)
- VerificationReport

## الحالات

- غير نهائية: BUILDING, READY, ACTIVE, DEGRADED
- نهائية: FAILED, RETIRED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-PRJ-CREATE-VERSION | BUILDING | kind ∈ {search, graph, vector (R2, SLC-10)}; document schema version, embedding model version (vector), analyzer/normalization version and source checkpoint set; at most one BUILDING version per (tenant group, kind) | EVT-PRJ-BUILD-STARTED | PROJECTION_BUILD_IN_PROGRESS |
| BUILDING | SYS:full rebuild reached live checkpoint | READY | all source streams replayed to current checkpoint; verification sample equals source (FIT-11) | EVT-PRJ-READY | — |
| BUILDING | SYS:build failed | FAILED | unrecoverable build error | EVT-PRJ-FAILED | — |
| READY | CMD-PRJ-PROMOTE | ACTIVE | operator; verification passed; previous ACTIVE of same kind → RETIRED in the same step (alias switch) | EVT-PRJ-PROMOTED | PROJECTION_NOT_VERIFIED |
| ACTIVE | SYS:lag above threshold | DEGRADED | lag > 5 min or error rate > 1 % for 5 min | EVT-PRJ-DEGRADED | — |
| DEGRADED | SYS:lag back within target | ACTIVE | lag ≤ 30 s for 5 min | EVT-PRJ-RECOVERED | — |
| READY, ACTIVE, DEGRADED | CMD-PRJ-RETIRE | RETIRED | operator; not the only ACTIVE version of its kind | EVT-PRJ-RETIRED | LAST_ACTIVE_PROJECTION |
| BUILDING | CMD-PRJ-CANCEL-BUILD | FAILED | operator; reason | EVT-PRJ-FAILED | REASON_REQUIRED |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-PRJ-CREATE-VERSION | SYS:full rebuild reached live checkpoint | SYS:build failed | CMD-PRJ-PROMOTE | SYS:lag above threshold | SYS:lag back within target | CMD-PRJ-RETIRE | CMD-PRJ-CANCEL-BUILD |
|---|---|---|---|---|---|---|---|---|
| ∅ | → BUILDING | — | — | — | — | — | — | — |
| BUILDING | ✗ PROJECTION_VERSION_INVALID_STATE_TRANSITION | → READY | → FAILED | ✗ PROJECTION_VERSION_INVALID_STATE_TRANSITION | ✗ PROJECTION_VERSION_INVALID_STATE_TRANSITION | ✗ PROJECTION_VERSION_INVALID_STATE_TRANSITION | ✗ PROJECTION_VERSION_INVALID_STATE_TRANSITION | → FAILED |
| READY | ✗ PROJECTION_VERSION_INVALID_STATE_TRANSITION | ✗ PROJECTION_VERSION_INVALID_STATE_TRANSITION | ✗ PROJECTION_VERSION_INVALID_STATE_TRANSITION | → ACTIVE | ✗ PROJECTION_VERSION_INVALID_STATE_TRANSITION | ✗ PROJECTION_VERSION_INVALID_STATE_TRANSITION | → RETIRED | ✗ PROJECTION_VERSION_INVALID_STATE_TRANSITION |
| ACTIVE | ✗ PROJECTION_VERSION_INVALID_STATE_TRANSITION | ✗ PROJECTION_VERSION_INVALID_STATE_TRANSITION | ✗ PROJECTION_VERSION_INVALID_STATE_TRANSITION | ✗ PROJECTION_VERSION_INVALID_STATE_TRANSITION | → DEGRADED | ✗ PROJECTION_VERSION_INVALID_STATE_TRANSITION | → RETIRED | ✗ PROJECTION_VERSION_INVALID_STATE_TRANSITION |
| DEGRADED | ✗ PROJECTION_VERSION_INVALID_STATE_TRANSITION | ✗ PROJECTION_VERSION_INVALID_STATE_TRANSITION | ✗ PROJECTION_VERSION_INVALID_STATE_TRANSITION | ✗ PROJECTION_VERSION_INVALID_STATE_TRANSITION | ✗ PROJECTION_VERSION_INVALID_STATE_TRANSITION | → ACTIVE | → RETIRED | ✗ PROJECTION_VERSION_INVALID_STATE_TRANSITION |
| FAILED | ✗ PROJECTION_VERSION_INVALID_STATE_TRANSITION | ✗ PROJECTION_VERSION_INVALID_STATE_TRANSITION | ✗ PROJECTION_VERSION_INVALID_STATE_TRANSITION | ✗ PROJECTION_VERSION_INVALID_STATE_TRANSITION | ✗ PROJECTION_VERSION_INVALID_STATE_TRANSITION | ✗ PROJECTION_VERSION_INVALID_STATE_TRANSITION | ✗ PROJECTION_VERSION_INVALID_STATE_TRANSITION | ✗ PROJECTION_VERSION_INVALID_STATE_TRANSITION |
| RETIRED | ✗ PROJECTION_VERSION_INVALID_STATE_TRANSITION | ✗ PROJECTION_VERSION_INVALID_STATE_TRANSITION | ✗ PROJECTION_VERSION_INVALID_STATE_TRANSITION | ✗ PROJECTION_VERSION_INVALID_STATE_TRANSITION | ✗ PROJECTION_VERSION_INVALID_STATE_TRANSITION | ✗ PROJECTION_VERSION_INVALID_STATE_TRANSITION | ✗ PROJECTION_VERSION_INVALID_STATE_TRANSITION | ✗ PROJECTION_VERSION_INVALID_STATE_TRANSITION |

## التزامن وعدم التكرار

- Optimistic concurrency: `If-Match: <version>`؛ عدم التطابق → `VERSION_CONFLICT` (HTTP 409) دون تغيير.
- كل أمر يحمل `Idempotency-Key`؛ التكرار يعيد النتيجة الأصلية؛ نفس المفتاح بحمولة مختلفة → `IDEMPOTENCY_KEY_REUSED` (HTTP 422).
- الأوامر التي تبدأ بـ `SYS:` يطلقها المجدول بهوية عبء عمل، وتخضع لنفس الثوابت.

## الحفظ

- State + history (إصدار غير قابل للتعديل لكل تغيير، ADR-P02) + outbox + audit outbox في نفس المعاملة (FIT-04).
- النموذج المنطقي: `06-data/logical-model/slc-05.md`.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
id: AGG-PROJECTION-VERSION
bc: BC07
name: Projection Version
tier: T3
purpose: إصدار فهرس بحث أو رسم يُبنى ويُرقّى بأسلوب blue/green
states:
- BUILDING
- READY
- ACTIVE
- DEGRADED
- FAILED
- RETIRED
terminal:
- FAILED
- RETIRED
invariants:
- 'INV-PRJ-01: a projection is never a source of truth; every document is reproducible
  from owner contexts (A07, FIT-11)'
- 'INV-PRJ-02: exactly one ACTIVE version per (tenant group, kind) serves queries;
  promotion is atomic (alias switch)'
- 'INV-PRJ-03: every document carries security labels (tenant, level, compartments,
  caveats, org_scope, security_version) — ADR-P06'
- 'INV-PRJ-04: normalization, schema or embedding-model changes require a new version
  (no in-place re-analysis)'
entities:
- SourceCheckpoint (stream, position)
- VerificationReport
requirements:
- REQ-SRC-004
notes: 'Operational aggregate (T3): the platform operator manages rebuilds; tenants
  never see projection versions.'
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-PRJ-CREATE-VERSION
  to: BUILDING
  guard: kind ∈ {search, graph, vector (R2, SLC-10)}; document schema version, embedding
    model version (vector), analyzer/normalization version and source checkpoint set;
    at most one BUILDING version per (tenant group, kind)
  event: EVT-PRJ-BUILD-STARTED
  guard_error: PROJECTION_BUILD_IN_PROGRESS
- from:
  - BUILDING
  command: SYS:full rebuild reached live checkpoint
  to: READY
  guard: all source streams replayed to current checkpoint; verification sample equals
    source (FIT-11)
  event: EVT-PRJ-READY
  guard_error: null
- from:
  - BUILDING
  command: SYS:build failed
  to: FAILED
  guard: unrecoverable build error
  event: EVT-PRJ-FAILED
  guard_error: null
- from:
  - READY
  command: CMD-PRJ-PROMOTE
  to: ACTIVE
  guard: operator; verification passed; previous ACTIVE of same kind → RETIRED in
    the same step (alias switch)
  event: EVT-PRJ-PROMOTED
  guard_error: PROJECTION_NOT_VERIFIED
- from:
  - ACTIVE
  command: SYS:lag above threshold
  to: DEGRADED
  guard: lag > 5 min or error rate > 1 % for 5 min
  event: EVT-PRJ-DEGRADED
  guard_error: null
- from:
  - DEGRADED
  command: SYS:lag back within target
  to: ACTIVE
  guard: lag ≤ 30 s for 5 min
  event: EVT-PRJ-RECOVERED
  guard_error: null
- from:
  - READY
  - ACTIVE
  - DEGRADED
  command: CMD-PRJ-RETIRE
  to: RETIRED
  guard: operator; not the only ACTIVE version of its kind
  event: EVT-PRJ-RETIRED
  guard_error: LAST_ACTIVE_PROJECTION
- from:
  - BUILDING
  command: CMD-PRJ-CANCEL-BUILD
  to: FAILED
  guard: operator; reason
  event: EVT-PRJ-FAILED
  guard_error: REASON_REQUIRED
```

</details>
