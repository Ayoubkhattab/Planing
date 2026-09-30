---
id: CONTEXT-MAP
type: context-map
title: Bounded Context Map
wave: W3
tier: T0
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
traces: {decided_by: [ADR-P06, ADR-P07, ADR-P11], rules: [BRL-014], fitness: [FIT-01]}
---

# Bounded Context Map

```mermaid
flowchart LR
  BC01[BC01 Foundation<br/>tenant · org · identity · authority]
  BC08[BC08 Governance & Runtime<br/>policy · classification · audit]
  BC02[BC02 Information<br/>entities · claims · evidence · sources · observations]
  BC03[BC03 Intelligence & Analysis<br/>analysis · assessment · situation · alerts]
  BC04[BC04 Operations<br/>decision · plan · task · comms · risk]
  BC05[BC05 Resources & Readiness<br/>assets · resources · eligibility]
  BC06[BC06 Knowledge & Products]
  BC07[BC07 Platform Intelligence<br/>AI · integration adapters]
  EXT[(External systems)]

  BC01 -- OHS: SecurityContext, AuthorityCheck --> BC02 & BC03 & BC04 & BC05 & BC06 & BC07
  BC08 -- OHS: PolicyDecision, Classification --> BC01 & BC02 & BC03 & BC04 & BC05 & BC06 & BC07
  BC02 -- OHS + events --> BC03
  BC02 -- OHS + events --> BC04
  BC02 -- events --> BC06
  BC03 -- Customer/Supplier: Assessment refs --> BC04
  BC05 -- Customer/Supplier: EligibilityCheck, Availability --> BC04
  BC04 -- events: TaskAssigned/Completed --> BC05
  BC03 -- events --> BC06
  BC04 -- events --> BC06
  EXT -- ACL adapters --> BC07
  BC07 -- commands via BC02 API --> BC02
```

## العلاقات

| من (upstream) | إلى (downstream) | النمط | العقد | الاتساق |
|---|---|---|---|---|
| BC01 | الكل | Open Host Service + Published Language | `SecurityContext`، `AuthorityCheck(actor, decision_type, scope, at)` | متزامن |
| BC08 | الكل | Open Host Service (PDP) | `PolicyDecision(subject, action, resource, context)`، labels | متزامن، fail-closed |
| BC02 | BC03، BC04، BC06، BC07 | OHS + Domain Events | Entity/Claim/Observation queries (as-of)، events | استعلام متزامن؛ أحداث نهائية الاتساق |
| BC03 | BC04 | Customer / Supplier | Assessment references (versioned URNs) | مرجع لإصدار ثابت |
| BC05 | BC04 | Customer / Supplier | `EligibilityCheck(person, task_type, at)`، availability | متزامن |
| BC04 | BC05 | Domain Events | TaskAssigned، TaskCompleted (تحرير الموارد) | نهائي |
| External | BC07 | Anti-Corruption Layer | adapters → commands على BC02 | نهائي، مع lineage |

## قواعد
1. لا قراءة من مخزن سياق آخر (FIT-01). الوصول عبر OHS أو أحداث أو إسقاطات معلنة.
2. المراجع بين السياقات = URN + (version أو known_at) عند الحاجة لثبات الدليل.
3. BC07 لا يملك بيانات عمل؛ المحولات تكتب عبر أوامر BC02 كأي عميل (REQ-INF-005).
4. AI (R2) يقرأ عبر الإسقاطات المؤمنة فقط (ADR-P06)، ولا يكتب إلا بأوامر تمر بصلاحيات المستخدم وضمن AIL.
