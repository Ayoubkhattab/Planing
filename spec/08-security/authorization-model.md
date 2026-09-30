---
id: AUTHZ-MODEL
type: security-model
title: Authorization Model
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
wave: W3
tier: T0
traces: {decided_by: [ADR-P06, ADR-P11], requirements: [REQ-FND-010, REQ-FND-011, REQ-FND-012, REQ-FND-013, REQ-FND-014]}
---

# Authorization Model

## 1. المكونات
| المكون | المسؤولية |
|---|---|
| PEP (في كل تطبيق وبوابة) | يبني الطلب، يستدعي PDP قبل أي استرجاع، يطبق القرار والالتزامات |
| PDP (BC08) | يقيّم السياسات المعتمدة بزمن سريانها ويعيد القرار |
| PIP | مصادر السمات: BC01 (هوية، تنظيم، سلطة، clearance)، تسميات الكائن، السياق |
| Policy Store | سياسات T2 بإصدارات وزمن سريان (REQ-GOV-009) |

## 2. طلب القرار
```text
DecisionRequest {
  subject:  {user, roles[], org_units[], clearance, attributes, device, auth_strength}
  action:   view | edit | export | share | approve | delete | retain | archive | <command code>
  resource: {type, urn?, labels, owner_org, tier}     or  {type, scope} for list/search
  purpose:  operations | analysis | audit | administration | …
  context:  {time, jurisdiction, network_zone, offline: bool}
}
DecisionResponse {
  decision: ALLOW | DENY | CONDITIONAL | REDACT | AGGREGATE | REQUIRE_APPROVAL
  obligations[]: audit | redact(fields) | aggregate(min_group) | watermark | approval(workflow) | mfa
  allowed_scope?: filter expression for list/search (ADR-P06)
  reason_code, policy_version
}
```

## 3. ترتيب التقييم
```text
1 tenant match            else DENY (not-found shape)
2 classification rule     (classification-scheme §2) else DENY
3 permission (RBAC)       role grants action on resource type within org scope
4 attribute policies      (ABAC) purpose, time, device, jurisdiction, caveats
5 segregation of duties   (REQ-OPS-005, REQ-OPS-009)
6 obligations             combine; most restrictive wins
PDP error / timeout → DENY (REQ-FND-013)
```

## 4. أمثلة جداول قرار
| POL | subject | action | resource | condition | decision |
|---|---|---|---|---|---|
| POL-TASK-COMPLETE | role ∈ {Manager, Planner} ∧ org ⊇ task.org | complete | Task | state = APPROVED | ALLOW + audit |
| POL-TASK-APPROVE-SOD | any | approve | Task | subject = task.assignee ∧ tenant.sod = on | DENY (SEGREGATION_OF_DUTIES) |
| POL-EXPORT-BULK | Analyst | export | list > 10,000 | — | REQUIRE_APPROVAL(Manager) + watermark |
| POL-PERSONAL-DATA | purpose ∉ {operations, legal} | view | attr.personal_data | — | REDACT(personal fields) |
| POL-AGG-STATS | role = Executive | view | statistics over T1 | group < 5 | AGGREGATE(min_group=5) |
| POL-OFFLINE-PRELOAD | Field User | preload | area data | level > INTERNAL | DENY |

## 5. التخزين المؤقت للقرارات
قرارات ALLOW تُخزن مؤقتاً ≤ 60 ثانية بمفتاح يتضمن `security_version` للموضوع والمورد؛ أي تغيير في الصلاحيات يرفع الإصدار ويبطل الذاكرة فوراً (QAS-SEC-003).

## 6. خدمة إلى خدمة
هوية عبء عمل لكل تطبيق (mTLS). الطلب الداخلي يحمل SecurityContext المستخدم الأصلي؛ الخدمة لا ترفع صلاحياتها باسم المستخدم.
