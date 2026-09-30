---
id: AGG-INTEGRATION-CONNECTION
type: aggregate
title: Integration Connection
wave: W4
slice: SLC-16
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC07
importance_tier: T2
personal_data: false
traces:
  satisfies:
  - REQ-INT-001
  state_machine: SM-INTEGRATION-CONNECTION
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-INTEGRATION-CONNECTION — Integration Connection

**الغرض:** اتصال بنظام خارجي داخل حدود المؤسسة (ERP، HRIS، DMS، CMMS، بوابة حساسات، نقطة CAP)  
**السياق:** BC07 · **المستوى:** T2 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-CON-01** — every active connection has exactly one egress/ingress allow-list entry, approved by a Security Officer other than the requester
- **INV-CON-02** — no writes into ERP/HRIS/DMS/CMMS in R2 — external systems are sources, never sinks (BRL-013); the only outbound kind is CAP
- **INV-CON-03** — credentials never appear in specifications, logs or events — reference to OpenBao only

## مكونات داخلية

- HealthCheck
- AllowListEntry

## الحالات

- غير نهائية: DRAFT, TESTING, ACTIVE, DEGRADED, SUSPENDED
- نهائية: RETIRED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-CON-REGISTER | DRAFT | system kind ∈ {erp, hris, dms, cmms, sensor_gateway, cap_endpoint}; endpoint on an internal network; protocol; direction ∈ {inbound, outbound}, outbound only for cap_endpoint in R2 (INV-CON-02); credentials stored in OpenBao (reference only) | EVT-CON-REGISTERED | CONNECTION_INVALID |
| DRAFT | CMD-CON-TEST | TESTING | integration engineer; connectivity and schema probe run | EVT-CON-TEST-STARTED | — |
| TESTING | CMD-CON-ACTIVATE | ACTIVE | probe passed; egress allow-list entry approved by Security Officer ≠ requester (GOV-005) | EVT-CON-ACTIVATED | SEGREGATION_OF_DUTIES |
| TESTING | CMD-CON-FAIL-TEST | DRAFT | probe failed; errors recorded | EVT-CON-TEST-FAILED | — |
| ACTIVE | SYS:health checks failing 5 min | DEGRADED | backlog buffered by adapters (QAS-INT-001) | EVT-CON-DEGRADED | — |
| DEGRADED | SYS:health restored | ACTIVE | backlog replayed | EVT-CON-RECOVERED | — |
| ACTIVE, DEGRADED | CMD-CON-SUSPEND | SUSPENDED | reason; egress rule disabled | EVT-CON-SUSPENDED | REASON_REQUIRED |
| SUSPENDED | CMD-CON-RESUME | ACTIVE | egress rule re-enabled after re-check | EVT-CON-RESUMED | — |
| DRAFT, SUSPENDED | CMD-CON-RETIRE | RETIRED | no ACTIVE adapter or stream bound; egress rule removed | EVT-CON-RETIRED | CONNECTION_IN_USE |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-CON-REGISTER | CMD-CON-TEST | CMD-CON-ACTIVATE | CMD-CON-FAIL-TEST | SYS:health checks failing 5 min | SYS:health restored | CMD-CON-SUSPEND | CMD-CON-RESUME | CMD-CON-RETIRE |
|---|---|---|---|---|---|---|---|---|---|
| ∅ | → DRAFT | — | — | — | — | — | — | — | — |
| DRAFT | ✗ INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION | → TESTING | ✗ INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION | ✗ INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION | ✗ INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION | ✗ INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION | ✗ INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION | ✗ INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION | → RETIRED |
| TESTING | ✗ INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION | ✗ INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION | → ACTIVE | → DRAFT | ✗ INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION | ✗ INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION | ✗ INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION | ✗ INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION | ✗ INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION |
| ACTIVE | ✗ INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION | ✗ INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION | ✗ INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION | ✗ INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION | → DEGRADED | ✗ INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION | → SUSPENDED | ✗ INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION | ✗ INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION |
| DEGRADED | ✗ INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION | ✗ INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION | ✗ INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION | ✗ INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION | ✗ INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION | → ACTIVE | → SUSPENDED | ✗ INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION | ✗ INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION |
| SUSPENDED | ✗ INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION | ✗ INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION | ✗ INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION | ✗ INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION | ✗ INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION | ✗ INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION | ✗ INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION | → ACTIVE | → RETIRED |
| RETIRED | ✗ INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION | ✗ INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION | ✗ INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION | ✗ INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION | ✗ INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION | ✗ INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION | ✗ INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION | ✗ INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION | ✗ INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION |

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
id: AGG-INTEGRATION-CONNECTION
bc: BC07
name: Integration Connection
tier: T2
purpose: اتصال بنظام خارجي داخل حدود المؤسسة (ERP، HRIS، DMS، CMMS، بوابة حساسات،
  نقطة CAP)
states:
- DRAFT
- TESTING
- ACTIVE
- DEGRADED
- SUSPENDED
- RETIRED
terminal:
- RETIRED
invariants:
- 'INV-CON-01: every active connection has exactly one egress/ingress allow-list entry,
  approved by a Security Officer other than the requester'
- 'INV-CON-02: no writes into ERP/HRIS/DMS/CMMS in R2 — external systems are sources,
  never sinks (BRL-013); the only outbound kind is CAP'
- 'INV-CON-03: credentials never appear in specifications, logs or events — reference
  to OpenBao only'
entities:
- HealthCheck
- AllowListEntry
requirements:
- REQ-INT-001
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-CON-REGISTER
  to: DRAFT
  guard: system kind ∈ {erp, hris, dms, cmms, sensor_gateway, cap_endpoint}; endpoint
    on an internal network; protocol; direction ∈ {inbound, outbound}, outbound only
    for cap_endpoint in R2 (INV-CON-02); credentials stored in OpenBao (reference
    only)
  event: EVT-CON-REGISTERED
  guard_error: CONNECTION_INVALID
- from:
  - DRAFT
  command: CMD-CON-TEST
  to: TESTING
  guard: integration engineer; connectivity and schema probe run
  event: EVT-CON-TEST-STARTED
  guard_error: null
- from:
  - TESTING
  command: CMD-CON-ACTIVATE
  to: ACTIVE
  guard: probe passed; egress allow-list entry approved by Security Officer ≠ requester
    (GOV-005)
  event: EVT-CON-ACTIVATED
  guard_error: SEGREGATION_OF_DUTIES
- from:
  - TESTING
  command: CMD-CON-FAIL-TEST
  to: DRAFT
  guard: probe failed; errors recorded
  event: EVT-CON-TEST-FAILED
  guard_error: null
- from:
  - ACTIVE
  command: SYS:health checks failing 5 min
  to: DEGRADED
  guard: backlog buffered by adapters (QAS-INT-001)
  event: EVT-CON-DEGRADED
  guard_error: null
- from:
  - DEGRADED
  command: SYS:health restored
  to: ACTIVE
  guard: backlog replayed
  event: EVT-CON-RECOVERED
  guard_error: null
- from:
  - ACTIVE
  - DEGRADED
  command: CMD-CON-SUSPEND
  to: SUSPENDED
  guard: reason; egress rule disabled
  event: EVT-CON-SUSPENDED
  guard_error: REASON_REQUIRED
- from:
  - SUSPENDED
  command: CMD-CON-RESUME
  to: ACTIVE
  guard: egress rule re-enabled after re-check
  event: EVT-CON-RESUMED
  guard_error: null
- from:
  - DRAFT
  - SUSPENDED
  command: CMD-CON-RETIRE
  to: RETIRED
  guard: no ACTIVE adapter or stream bound; egress rule removed
  event: EVT-CON-RETIRED
  guard_error: CONNECTION_IN_USE
```

</details>
