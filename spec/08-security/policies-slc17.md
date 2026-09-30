---
id: POLICIES-SLC17
type: policy-decision-tables
title: Policy Decision Tables — SLC-17
wave: W6
slice: SLC-17
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-27'
recalibrate_after_pilot: true
---

# Policy Decision Tables — SLC-17

## command_policies

_15 items_

### POL-RIS-IDENTIFY

- **command:** CMD-RIS-IDENTIFY
- **subject:** محدِّد الخطر (تحديد) · مقيّم (تقييم، إعادة تقييم) · موافق المعالجة (تخطيط المعالجة) · مدير المخاطر (إغلاق)
- **resource:** AGG-RISK
- **context_conditions:** tenant match; scope_refs visible to actor
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-RIS-ASSESS

- **command:** CMD-RIS-ASSESS
- **subject:** مقيّم (تقييم، إعادة تقييم)
- **resource:** AGG-RISK
- **context_conditions:** tenant match; scope_refs visible to actor
- **segregation_of_duties:** assessor ≠ identifier when tenant policy requires it (INV-RIS-01)
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-RIS-PLAN-TREATMENT

- **command:** CMD-RIS-PLAN-TREATMENT
- **subject:** موافق المعالجة مخوَّل
- **resource:** AGG-RISK
- **context_conditions:** tenant match; scope_refs visible to actor
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-RIS-REASSESS

- **command:** CMD-RIS-REASSESS
- **subject:** مقيّم (تقييم، إعادة تقييم)
- **resource:** AGG-RISK
- **context_conditions:** tenant match; scope_refs visible to actor
- **segregation_of_duties:** assessor ≠ identifier when tenant policy requires it (INV-RIS-01)
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-RIS-CLOSE

- **command:** CMD-RIS-CLOSE
- **subject:** مدير المخاطر
- **resource:** AGG-RISK
- **context_conditions:** tenant match; scope_refs visible to actor
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-INC-REPORT

- **command:** CMD-INC-REPORT
- **subject:** أي مُبلِّغ مخوَّل (تبليغ، إلغاء)
- **resource:** AGG-INCIDENT
- **context_conditions:** tenant match; scope_refs visible to actor
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-INC-ASSESS

- **command:** CMD-INC-ASSESS
- **subject:** مقيّم الحادثة
- **resource:** AGG-INCIDENT
- **context_conditions:** tenant match; affected_scope_refs visible to actor
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-INC-DISPATCH-RESPONSE

- **command:** CMD-INC-DISPATCH-RESPONSE
- **subject:** قائد الحادثة
- **resource:** AGG-INCIDENT
- **context_conditions:** tenant match; commander authorized in scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-INC-CONTAIN

- **command:** CMD-INC-CONTAIN
- **subject:** قائد الحادثة
- **resource:** AGG-INCIDENT
- **context_conditions:** tenant match
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-INC-RESOLVE

- **command:** CMD-INC-RESOLVE
- **subject:** قائد الحادثة
- **resource:** AGG-INCIDENT
- **context_conditions:** tenant match; كل مهام الاستجابة نهائية (INV-INC-02)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-INC-CLOSE

- **command:** CMD-INC-CLOSE
- **subject:** قائد الحادثة
- **resource:** AGG-INCIDENT
- **context_conditions:** tenant match
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-INC-CANCEL

- **command:** CMD-INC-CANCEL
- **subject:** أي مُبلِّغ مخوَّل (تبليغ، إلغاء)
- **resource:** AGG-INCIDENT
- **context_conditions:** tenant match
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-INC-ESCALATE

- **command:** CMD-INC-ESCALATE
- **subject:** قائد الحادثة
- **resource:** AGG-INCIDENT
- **context_conditions:** tenant match; new_severity أعلى فقط (INV-INC-01)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit; notify next authority level

### POL-INC-DE-ESCALATE

- **command:** CMD-INC-DE-ESCALATE
- **subject:** قائد الحادثة بسلطة صريحة
- **resource:** AGG-INCIDENT
- **context_conditions:** tenant match; new_severity أدنى بمستوى واحد كحد أقصى (INV-INC-01)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-INC-ACTIVATE-CONTINGENCY

- **command:** CMD-INC-ACTIVATE-CONTINGENCY
- **subject:** قائد الحادثة بسلطة صريحة لتفعيل الاستمرارية
- **resource:** AGG-INCIDENT
- **context_conditions:** tenant match; أمر صريح دائماً (INV-INC-03)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

## query_policies

_5 items_

| id | query | subject | otherwise |
|---|---|---|---|
| POL-RIS-GET | QRY-RIS-GET | مالك النطاق؛ مدير المخاطر | DENY (not-found shape) |
| POL-RIS-REGISTER | QRY-RIS-REGISTER | allowed_scope | DENY (not-found shape) |
| POL-INC-GET | QRY-INC-GET | allowed_scope | DENY (not-found shape) |
| POL-INC-LIST | QRY-INC-LIST | allowed_scope | DENY (not-found shape) |
| POL-INC-RECOVERY-STATUS | QRY-INC-RECOVERY-STATUS | القائد؛ مالك الاستمرارية | DENY (not-found shape) |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
command_policies:
- id: POL-RIS-IDENTIFY
  command: CMD-RIS-IDENTIFY
  subject: محدِّد الخطر (تحديد) · مقيّم (تقييم، إعادة تقييم) · موافق المعالجة (تخطيط المعالجة) · مدير المخاطر (إغلاق)
  resource: AGG-RISK
  context_conditions: tenant match; scope_refs visible to actor
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-RIS-ASSESS
  command: CMD-RIS-ASSESS
  subject: مقيّم (تقييم، إعادة تقييم)
  resource: AGG-RISK
  context_conditions: tenant match; scope_refs visible to actor
  segregation_of_duties: assessor ≠ identifier when tenant policy requires it (INV-RIS-01)
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-RIS-PLAN-TREATMENT
  command: CMD-RIS-PLAN-TREATMENT
  subject: موافق المعالجة مخوَّل
  resource: AGG-RISK
  context_conditions: tenant match; scope_refs visible to actor
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-RIS-REASSESS
  command: CMD-RIS-REASSESS
  subject: مقيّم (تقييم، إعادة تقييم)
  resource: AGG-RISK
  context_conditions: tenant match; scope_refs visible to actor
  segregation_of_duties: assessor ≠ identifier when tenant policy requires it (INV-RIS-01)
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-RIS-CLOSE
  command: CMD-RIS-CLOSE
  subject: مدير المخاطر
  resource: AGG-RISK
  context_conditions: tenant match; scope_refs visible to actor
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-INC-REPORT
  command: CMD-INC-REPORT
  subject: أي مُبلِّغ مخوَّل (تبليغ، إلغاء)
  resource: AGG-INCIDENT
  context_conditions: tenant match; scope_refs visible to actor
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-INC-ASSESS
  command: CMD-INC-ASSESS
  subject: مقيّم الحادثة
  resource: AGG-INCIDENT
  context_conditions: tenant match; affected_scope_refs visible to actor
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-INC-DISPATCH-RESPONSE
  command: CMD-INC-DISPATCH-RESPONSE
  subject: قائد الحادثة
  resource: AGG-INCIDENT
  context_conditions: tenant match; commander authorized in scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-INC-CONTAIN
  command: CMD-INC-CONTAIN
  subject: قائد الحادثة
  resource: AGG-INCIDENT
  context_conditions: tenant match
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-INC-RESOLVE
  command: CMD-INC-RESOLVE
  subject: قائد الحادثة
  resource: AGG-INCIDENT
  context_conditions: tenant match; كل مهام الاستجابة نهائية (INV-INC-02)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-INC-CLOSE
  command: CMD-INC-CLOSE
  subject: قائد الحادثة
  resource: AGG-INCIDENT
  context_conditions: tenant match
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-INC-CANCEL
  command: CMD-INC-CANCEL
  subject: أي مُبلِّغ مخوَّل (تبليغ، إلغاء)
  resource: AGG-INCIDENT
  context_conditions: tenant match
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-INC-ESCALATE
  command: CMD-INC-ESCALATE
  subject: قائد الحادثة
  resource: AGG-INCIDENT
  context_conditions: tenant match; new_severity أعلى فقط (INV-INC-01)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit; notify next authority level
- id: POL-INC-DE-ESCALATE
  command: CMD-INC-DE-ESCALATE
  subject: قائد الحادثة بسلطة صريحة
  resource: AGG-INCIDENT
  context_conditions: tenant match; new_severity أدنى بمستوى واحد كحد أقصى (INV-INC-01)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-INC-ACTIVATE-CONTINGENCY
  command: CMD-INC-ACTIVATE-CONTINGENCY
  subject: قائد الحادثة بسلطة صريحة لتفعيل الاستمرارية
  resource: AGG-INCIDENT
  context_conditions: tenant match; أمر صريح دائماً (INV-INC-03)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
query_policies:
- id: POL-RIS-GET
  query: QRY-RIS-GET
  subject: مالك النطاق؛ مدير المخاطر
  otherwise: DENY (not-found shape)
- id: POL-RIS-REGISTER
  query: QRY-RIS-REGISTER
  subject: allowed_scope
  otherwise: DENY (not-found shape)
- id: POL-INC-GET
  query: QRY-INC-GET
  subject: allowed_scope
  otherwise: DENY (not-found shape)
- id: POL-INC-LIST
  query: QRY-INC-LIST
  subject: allowed_scope
  otherwise: DENY (not-found shape)
- id: POL-INC-RECOVERY-STATUS
  query: QRY-INC-RECOVERY-STATUS
  subject: القائد؛ مالك الاستمرارية
  otherwise: DENY (not-found shape)
```

</details>
