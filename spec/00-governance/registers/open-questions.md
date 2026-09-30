---
id: REG-OQ
type: register
title: Open Questions
wave: W0
tier: T3
owner_role: Orchestrator
status: DRAFT
approved_by: null
approved_at: null
consumers: []
---

# Open Questions

## open_questions

_10 items_ (OQ-034 added — see CR-64 / spec/17-system-study/bc01-foundation.md)

### OQ-001

- **question:** هل فجوات ترقيم Use Cases (UC-009، UC-017–019، …) مقصودة كنطاقات محجوزة؟
- **affects:** traceability numbering
- **owner:** Business & Requirements
- **deadline_gate:** W2
- **status:** closed
- **answer:** gaps are reserved ranges; new UCs from UC-080

### OQ-010

- **question:** ما تعريف 'Major Plan change' في BRL-005؟
- **affects:** SM-PLAN, versioning
- **owner:** BC04
- **deadline_gate:** W4
- **status:** closed
- **answer:** BRL-005 rewritten (major change defined)

### OQ-011

- **question:** أي الإسنادات تتطلب أهلية أو تأهيلاً (BRL-007)؟ وهل ينطبق على المهام والأصول معاً؟
- **affects:** POL, AGG-TASK, BO-ELIGIBILITY
- **owner:** BC04 + BC05
- **deadline_gate:** W4
- **status:** closed
- **answer:** BRL-007 rewritten

### OQ-012

- **question:** هل 'Logistics' كائن واحد أم عائلة (Inventory, Shipment, Movement…)؟
- **affects:** ownership
- **owner:** BC05
- **deadline_gate:** W3
- **status:** closed
- **answer:** Logistics = family of BOs owned by BC05

### OQ-013

- **question:** هل مطابقة الكيانات عملية تحليلية (BC03) أم جزء من النواة المعلوماتية (BC02)؟
- **affects:** CR-02, SLC-04
- **owner:** BC02 + BC03
- **deadline_gate:** W3
- **status:** closed
- **answer:** ER in BC02; BC03 proposes

### OQ-034

- **question:** لماذا REQ-FND-010 (تقييم التخويل قبل كل استرجاع)، REQ-FND-013 (فشل PDP = DENY)، وREQ-GOV-002 (تصنيف إلزامي لكائنات T1/T2) بلا أي Use Case مرتبط في كامل كتالوج use-cases.md، بينما كل متطلبات BC01 الأخرى من نمط EARS نفسه (ubiquitous) مرتبطة بـUC واحد على الأقل؟ هل هذا نقص توثيقي (Missing UC) أم تصنيف صحيح بالتصميم؟
- **affects:** REQ-FND-010, REQ-FND-013, REQ-GOV-002, traceability BC01 (spec/17-system-study/bc01-foundation.md §4/§20)
- **owner:** BC01 (Foundation) + منهجية المتطلبات
- **deadline_gate:** Phase 3 (System Study reconstruction)
- **status:** closed
- **answer:** تصنيف صحيح بالتصميم، وليس نقصًا. الثلاثة تصف سلوك إنفاذ (enforcement) مدمجًا في شرط مسبق (precondition) يُطبَّق داخل *كل* Use Case آخر في المنصة (تقييم PDP قبل أي استرجاع؛ الفشل الآمن عند تعطّل PDP؛ إلزامية التصنيف عند إنشاء أي كائن T1/T2 في أي BC)، وليست فعلًا مستقلاً يقوم به فاعل بخطوات خاصة به. الفرق عن باقي متطلبات BC01 الـubiquitous (مثل REQ-FND-001/007/011) هو أن تلك الأخيرة تصف *إدارة* مورد (تزويد مستأجر، تعريف صلاحية، إدارة سياسة) له واجهة مستخدم واضحة، بينما هذه الثلاثة تصف *تشغيل النظام نفسه* أثناء تنفيذ أي واجهة أخرى. اختراع UC مستقل لها (مثل "تقييم التخويل") كان سيكون Use Case وهميًا بلا فاعل حقيقي، فتم تفادي ذلك عمدًا. لا حاجة لإجراء تصحيحي.

- **question:** هل يُمنع أن يعتمد المنفذ مهمته بنفسه؟
- **affects:** SM-TASK
- **owner:** BC04
- **deadline_gate:** W4
- **status:** closed
- **answer:** Segregation of duties ON by default; tenant-configurable by documented policy (Q8)

### OQ-031

- **question:** ما الفرق التشغيلي بين APPROVED وCOMPLETED وCLOSED؟
- **affects:** SM-TASK
- **owner:** BC04
- **deadline_gate:** W4
- **status:** closed
- **answer:** APPROVED = review accepted; COMPLETED = all criteria met (auto if machine-checkable); CLOSED = admin close after follow-ups (manual or auto after 7 d) (SPEC-TASK-RULES §1)

### OQ-032

- **question:** هل انتهاء المهلة يُنهي المهمة أم يصعّدها؟
- **affects:** SM-TASK
- **owner:** BC04
- **deadline_gate:** W4
- **status:** closed
- **answer:** escalation by default; EXPIRED only if task type expires_on_due = true (SPEC-TASK-RULES §1)

### OQ-033

- **question:** هل REJECTED نهائية؟
- **affects:** SM-TASK
- **owner:** BC04
- **deadline_gate:** W4
- **status:** closed
- **answer:** REJECTED is terminal; retry = linked follow-up task (SPEC-TASK-RULES §1)

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
open_questions:
- id: OQ-001
  question: هل فجوات ترقيم Use Cases (UC-009، UC-017–019، …) مقصودة كنطاقات محجوزة؟
  affects: traceability numbering
  owner: Business & Requirements
  deadline_gate: W2
  status: closed
  answer: gaps are reserved ranges; new UCs from UC-080
- id: OQ-010
  question: ما تعريف 'Major Plan change' في BRL-005؟
  affects: SM-PLAN, versioning
  owner: BC04
  deadline_gate: W4
  status: closed
  answer: BRL-005 rewritten (major change defined)
- id: OQ-011
  question: أي الإسنادات تتطلب أهلية أو تأهيلاً (BRL-007)؟ وهل ينطبق على المهام والأصول معاً؟
  affects: POL, AGG-TASK, BO-ELIGIBILITY
  owner: BC04 + BC05
  deadline_gate: W4
  status: closed
  answer: BRL-007 rewritten
- id: OQ-012
  question: هل 'Logistics' كائن واحد أم عائلة (Inventory, Shipment, Movement…)؟
  affects: ownership
  owner: BC05
  deadline_gate: W3
  status: closed
  answer: Logistics = family of BOs owned by BC05
- id: OQ-013
  question: هل مطابقة الكيانات عملية تحليلية (BC03) أم جزء من النواة المعلوماتية (BC02)؟
  affects: CR-02, SLC-04
  owner: BC02 + BC03
  deadline_gate: W3
  status: closed
  answer: ER in BC02; BC03 proposes
- id: OQ-034
  question: لماذا REQ-FND-010، REQ-FND-013، وREQ-GOV-002 بلا أي Use Case مرتبط، بينما
    كل متطلبات BC01 الأخرى من نمط ubiquitous نفسه مرتبطة بـUC واحد على الأقل؟ هل هذا
    نقص توثيقي أم تصنيف صحيح بالتصميم؟
  affects: REQ-FND-010, REQ-FND-013, REQ-GOV-002, traceability BC01 (spec/17-system-study/bc01-foundation.md)
  owner: BC01 (Foundation) + منهجية المتطلبات
  deadline_gate: Phase 3 (System Study reconstruction)
  status: closed
  answer: تصنيف صحيح بالتصميم. الثلاثة تصف سلوك إنفاذ مدمجًا في الشرط المسبق لكل Use
    Case آخر في المنصة (تقييم PDP قبل أي استرجاع؛ الفشل الآمن عند تعطّل PDP؛ إلزامية
    التصنيف عند إنشاء أي كائن T1/T2 في أي BC)، وليست فعلًا مستقلاً بخطوات خاصة به. الفرق
    عن باقي متطلبات BC01 ubiquitous (مثل REQ-FND-001/007/011) أن تلك الأخيرة تصف إدارة
    مورد له واجهة مستخدم واضحة، بينما هذه الثلاثة تصف تشغيل النظام نفسه أثناء أي واجهة
    أخرى. اختراع UC مستقل لها كان سيكون وهميًا بلا فاعل حقيقي، فتم تفاديه عمدًا. لا إجراء
    تصحيحي مطلوب.
- id: OQ-030
  question: هل يُمنع أن يعتمد المنفذ مهمته بنفسه؟
  affects: SM-TASK
  owner: BC04
  deadline_gate: W4
  status: closed
  answer: Segregation of duties ON by default; tenant-configurable by documented policy (Q8)
- id: OQ-031
  question: ما الفرق التشغيلي بين APPROVED وCOMPLETED وCLOSED؟
  affects: SM-TASK
  owner: BC04
  deadline_gate: W4
  status: closed
  answer: APPROVED = review accepted; COMPLETED = all criteria met (auto if machine-checkable); CLOSED = admin close after
    follow-ups (manual or auto after 7 d) (SPEC-TASK-RULES §1)
- id: OQ-032
  question: هل انتهاء المهلة يُنهي المهمة أم يصعّدها؟
  affects: SM-TASK
  owner: BC04
  deadline_gate: W4
  status: closed
  answer: escalation by default; EXPIRED only if task type expires_on_due = true (SPEC-TASK-RULES §1)
- id: OQ-033
  question: هل REJECTED نهائية؟
  affects: SM-TASK
  owner: BC04
  deadline_gate: W4
  status: closed
  answer: REJECTED is terminal; retry = linked follow-up task (SPEC-TASK-RULES §1)
```

</details>
