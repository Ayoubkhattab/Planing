---
id: AD-02-ACTORS-ROLES
type: actors-roles
title: "الفاعلون والأدوار — الكتالوج ومصفوفة الفاعل × العملية"
status: DRAFT
phase: "Phase 3.8 — 18-analysis-design (المرحلة 3)"
sources: [01-business/stakeholders.md, 08-security/policies-slc*.md, 08-security/authorization-model.md, 03-domain/contexts/BC*/commands-*.md, 03-domain/contexts/BC*/queries-*.md]
generator: 17-system-study/_build/build_analysis_design.py
---

# الفاعلون والأدوار

من يستخدم النظام، وما يحق لكل فاعل أن يفعله. المصدر المعتمد لكل صلاحية هو سياسة العملية في `08-security/policies-slc*.md`. هذا الملف يجمع السياسات الـ610 (477 أمرًا + 133 استعلامًا) حسب الفاعل.

## 1. كيف تُقرأ الصلاحيات

قرار التخويل (`08-security/authorization-model.md` §3) يُقيَّم بالترتيب: تطابق المستأجر، ثم قاعدة التصنيف، ثم **الدور** (RBAC: الدور يمنح الإجراء على نوع المورد داخل نطاق تنظيمي)، ثم **السمات** (ABAC: الغرض والوقت والجهاز والولاية والتحفظات وسمات المورد)، ثم **فصل المهام**، ثم الالتزامات. لذلك يظهر في السياسات نوعان من «الفاعل»:

| النوع | المعنى | أمثلة | كيف يُفحص |
|---|---|---|---|
| دور وظيفي | صلاحية مُسندة للمستخدم بإسناد دور (AGG-ROLE-ASSIGNMENT) | Analyst، Planner، Security Officer | RBAC في PDP من `roles[]` في طلب القرار |
| دور علاقة بالمورد | علاقة المستخدم بالمورد المحدد | assignee، reviewer، owner، requester، participant | ABAC: سمة من المورد نفسه (PIP) تُقارن بهوية المستخدم |
| صاحب سلطة | منح سلطة مسجل في BC01 لنوع قرار ونطاق | approver with plan-approval authority، allocation authority | `AuthorityCheck(actor, decision_type, scope, at)` (`03-domain/context-map.md`) |
| هوية نظام | حساب خدمة أو هوية عبء عمل | adapter service account، scheduler | نفس خط الأوامر ونفس السياسات (ADR-P17 القاعدة 5) |

## 2. التصنيف

كل وصف دور في موضوع السياسة (`subject`) يُصنَّف في مجموعة من خمس بقواعد نصية في المولِّد (`ROLE_RULES`) **[Derived]**: (A) الفاعلون الأعمال الـ15 المعرَّفون في المصدر، (B) أدوار المنصة، (C) أدوار السلطة والاعتماد، (D) أدوار العلاقة بالمورد، (E) الفاعلون النظاميون. العملية تُنسب إلى الأدوار التي تطابق فعلها (نفس قاعدة اختيار الفاعل في قصص المستخدم — `05-user-stories/00-guide.md` §3)، والعدّ يحسب العملية مرة لكل دور.

## 3. حقوق القرار (RACI)

من `01-business/stakeholders.md` (`decision_rights`)؛ نموذج السلطة قابل للتهيئة لكل مؤسسة ومملوك لـ BC01.

| القرار | المسؤول (R) | المساءَل (A) | يُستشار (C) | يُبلَّغ (I) | يُفرض في |
|---|---|---|---|---|---|
| قرار عمل (DOM-10) | Manager / Executive حسب السلطة | صاحب السلطة المسجل في BC01 | Analyst | Planner | `CMD-DEC-RECORD` + AuthorityCheck (BRL-003) |
| اعتماد الخطة وخط الأساس | Planner | Manager (≠ المُعد) | Resource Manager | Operator | `POL-PLV-APPROVE`، فصل المهام |
| اعتماد المهمة | Reviewer | Manager (≠ المنفذ) | — | Planner | `POL-TASK-APPROVE`، INV-TASK-07 |
| نشر التقييم | Analyst | Analysis lead / Manager | Knowledge Manager | Executive | AGG-ASSESSMENT |
| استثناء أمني | Security Officer | موافقة شخصين | Auditor | Administrator | AGG-SECURITY-EXCEPTION (معتمِد أول ثم ثانٍ) |
| تغيير التصنيف | صاحب المورد | Security Officer | — | Auditor | أوامر `*-RECLASSIFY` |
| الاحتفاظ والتجميد القانوني | Archivist | Legal / Compliance authority | Security Officer | Auditor | AGG-RETENTION-SCHEDULE، AGG-LEGAL-HOLD |

عمود «يُفرض في» **[Derived]** من السياسات والـAggregates.

## 4. الفاعلون النظاميون الداخليون

`01-business/stakeholders.md` يسرد سبعة فاعلين نظاميين؛ موقع كل منهم في التصميم **[Derived]**:

| الفاعل | أين يُنفَّذ |
|---|---|
| AI | BC07 (AGG-AI-REQUEST، AGG-AI-RESULT)؛ يقرأ الإسقاطات المؤمنة فقط ولا يكتب في R2 (`11-hexagonal-reference.md` §8) |
| Workflow | لا محرك سير عمل: آلات الحالات في الـAggregates والانتقالات التلقائية (`SYS:`) — TD-13 |
| Policy | PDP في BC08 (OPA، TD-08) عبر `QRY-PDP-DECIDE` |
| Event Bus | Kafka لكل خلية (TD-04) — `15-event-design.md` |
| Scheduler | سلال زمنية في PostgreSQL + عقود lease داخل الوحدة المالكة (TD-13) |
| Search | إسقاطات BC07 في OpenSearch (TD-02) |
| Notification | AGG-NOTIFICATION وAGG-SUBSCRIPTION في BC04 |

## 5. ملاحظات وفجوات

| البند | الحالة |
|---|---|
| حقوق القرار لمجموعات أصحاب المصلحة (`decision_rights: UNKNOWN` لـ SH-01..05) | **[Missing]** في المصدر |
| أدوار تستخدمها السياسات وليست ضمن ACT-01..15: Platform Operator، AI platform engineer، AI governance authority، integration engineer، Legal/Compliance authority، Privacy officer | **[Needs Review]** — تُضاف إلى `stakeholders.md` أو تُعرَّف كأدوار في AGG-ROLE |
| 35 أمرًا يذكر مصدرها أكثر من دور دون تحديد من يصدر الأمر | معلَّمة **[Needs Review]** في قصصها؛ تُحسم في `17-security-design.md` |
| وصف «finance» في سياسة `QRY-AI-USAGE` | دور غير معرَّف (§2.5) **[Needs Review]** |

## 6. الكتالوج والمصفوفات

<!-- BEGIN GENERATED: build_analysis_design.py -->

### 2.1 كتالوج الفاعلين والأدوار

#### (A) الفاعلون الأعمال (ACT-01..15 — `01-business/stakeholders.md`)

| الفاعل / الدور | الوصف | أوامر | استعلامات | السياقات |
|---|---|---|---|---|
| ACT-01 Executive — القيادي التنفيذي | القيادة (SH-01) | 2 | 1 | BC01 |
| ACT-02 Manager — المدير | القيادة (SH-01) | 40 | 4 | BC02, BC03, BC04, BC05, BC06 |
| ACT-03 Planner — المخطِّط | المستخدمون التشغيليون (SH-02) | 60 | 2 | BC02, BC04, BC05, BC06, BC07 |
| ACT-04 Analyst — المحلل | مستخدمو المعلومات والتحليل (SH-03) | 133 | 11 | BC02, BC03, BC04, BC06, BC07 |
| ACT-05 Operator — المشغِّل | المستخدمون التشغيليون (SH-02) | 7 | 0 | BC02, BC03 |
| ACT-06 Field User — المستخدم الميداني | المستخدمون التشغيليون (SH-02) | 10 | 2 | BC02, BC07 |
| ACT-07 Resource Manager — مدير الموارد | المستخدمون التشغيليون (SH-02) | 32 | 1 | BC05 |
| ACT-08 Logistics User — مستخدم الإمداد | المستخدمون التشغيليون (SH-02) | 10 | 0 | BC05 |
| ACT-09 Risk Manager — مدير المخاطر | المستخدمون التشغيليون (SH-02) | 5 | 1 | BC04 |
| ACT-10 Training Manager — مدير التدريب | المستخدمون التشغيليون (SH-02) | 24 | 1 | BC02, BC05 |
| ACT-11 Knowledge Manager — مدير المعرفة | مستخدمو المعلومات والتحليل (SH-03) | 7 | 0 | BC06 |
| ACT-12 Archivist — أمين الأرشيف | الحوكمة (SH-04) | 9 | 4 | BC06, BC08 |
| ACT-13 Security Officer — مسؤول الأمن | الحوكمة (SH-04) | 43 | 9 | BC01, BC02, BC03, BC04, BC05, BC06, BC07, BC08 |
| ACT-14 Auditor — المدقِّق | الحوكمة (SH-04) | 2 | 14 | BC03, BC06, BC07, BC08 |
| ACT-15 Administrator — مسؤول الإدارة | فرق المنصة (SH-05) | 66 | 10 | BC01, BC02, BC03, BC04, BC05, BC07 |

#### (B) أدوار المنصة

| الفاعل / الدور | الوصف | أوامر | استعلامات | السياقات |
|---|---|---|---|---|
| PLT-OPS — مشغّل المنصة | Platform Operator — فرق المنصة (SH-05) | 11 | 2 | BC01, BC07 |
| PLT-AI — مهندس/حوكمة الذكاء الاصطناعي | AI platform engineer، AI governance authority | 17 | 3 | BC07 |
| PLT-INT — مهندس التكامل | integration engineer | 8 | 2 | BC07 |

#### (C) أدوار السلطة والاعتماد

| الفاعل / الدور | الوصف | أوامر | استعلامات | السياقات |
|---|---|---|---|---|
| AUTH-LEGAL — السلطة القانونية والامتثال | Legal/Compliance authority، Privacy officer | 12 | 4 | BC06, BC08 |
| AUTH-GRANT — صاحب سلطة أو معتمِد ثانٍ | حامل منح سلطة في BC01 أو معتمِد ≠ المُعد (allocation/disposal/transfer/release authority، second approver…) | 48 | 2 | BC01, BC02, BC03, BC04, BC05, BC06, BC07, BC08 |

#### (D) أدوار العلاقة بالمورد (سمات للمورد يقيّمها قرار السياسة — ABAC عبر PIP، `08-security/authorization-model.md` §1–3)

| الفاعل / الدور | الوصف | أوامر | استعلامات | السياقات |
|---|---|---|---|---|
| REL-TASK — المنفّذ والمراجع | assignee، reviewer — دور يحدده المورد نفسه | 27 | 4 | BC02, BC03, BC04, BC05, BC06, BC07 |
| REL-OWNER — المالك والطالب والمشارك | owner، requester، custodian، participant، self | 40 | 18 | BC01, BC02, BC04, BC05, BC06, BC07, BC08 |
| REL-RECIPIENT — المستلم والمشترك | recipient، subscriber | 5 | 1 | BC03, BC04 |
| REL-INCIDENT — أدوار الحادثة | المُبلِّغ، مقيّم الحادثة، قائد الحادثة | 10 | 1 | BC04 |
| REL-PEER — الشخص الثاني | second Analyst / Administrator، peer Analyst — لفصل المهام | 10 | 0 | BC02, BC03, BC07 |
| ANY-USER — أي مستخدم مخوَّل | أي مستخدم ضمن `allowed_scope` أو مصرَّح له بعلامة المورد | 19 | 82 | BC01, BC02, BC03, BC04, BC05, BC06, BC07, BC08 |

#### (E) الفاعلون النظاميون

| الفاعل / الدور | الوصف | أوامر | استعلامات | السياقات |
|---|---|---|---|---|
| SYS — هويات النظام والخدمات | adapter/SCIM service accounts، workload identities، analysis-run identity، internal PEPs | 39 | 6 | BC01, BC02, BC05, BC08 |

### 2.2 مصفوفة الفاعل × السياق (عدد الأوامر / الاستعلامات)

| الفاعل / الدور | BC01 | BC02 | BC03 | BC04 | BC05 | BC06 | BC07 | BC08 |
|---|---|---|---|---|---|---|---|---|
| ACT-01 Executive — القيادي التنفيذي | 2 / 1 | — | — | — | — | — | — | — |
| ACT-02 Manager — المدير | — | 3 / 1 | 12 / 0 | 22 / 0 | 0 / 3 | 3 / 0 | — | — |
| ACT-03 Planner — المخطِّط | — | 6 / 1 | — | 33 / 0 | 10 / 1 | 7 / 0 | 4 / 0 | — |
| ACT-04 Analyst — المحلل | — | 72 / 9 | 42 / 1 | 5 / 0 | — | 10 / 0 | 4 / 1 | — |
| ACT-05 Operator — المشغِّل | — | 4 / 0 | 3 / 0 | — | — | — | — | — |
| ACT-06 Field User — المستخدم الميداني | — | 5 / 0 | — | — | — | — | 5 / 2 | — |
| ACT-07 Resource Manager — مدير الموارد | — | — | — | — | 32 / 1 | — | — | — |
| ACT-08 Logistics User — مستخدم الإمداد | — | — | — | — | 10 / 0 | — | — | — |
| ACT-09 Risk Manager — مدير المخاطر | — | — | — | 5 / 1 | — | — | — | — |
| ACT-10 Training Manager — مدير التدريب | — | 1 / 0 | — | — | 23 / 1 | — | — | — |
| ACT-11 Knowledge Manager — مدير المعرفة | — | — | — | — | — | 7 / 0 | — | — |
| ACT-12 Archivist — أمين الأرشيف | — | — | — | — | — | 3 / 0 | — | 6 / 4 |
| ACT-13 Security Officer — مسؤول الأمن | 10 / 2 | 5 / 0 | 3 / 0 | 1 / 0 | 6 / 0 | 0 / 1 | 6 / 3 | 12 / 3 |
| ACT-14 Auditor — المدقِّق | — | — | 0 / 1 | — | — | 2 / 2 | 0 / 3 | 0 / 8 |
| ACT-15 Administrator — مسؤول الإدارة | 40 / 6 | 5 / 2 | 3 / 0 | 4 / 0 | 4 / 0 | — | 10 / 2 | — |
| PLT-OPS — مشغّل المنصة | 7 / 1 | — | — | — | — | — | 4 / 1 | — |
| PLT-AI — مهندس/حوكمة الذكاء الاصطناعي | — | — | — | — | — | — | 17 / 3 | — |
| PLT-INT — مهندس التكامل | — | — | — | — | — | — | 8 / 2 | — |
| AUTH-LEGAL — السلطة القانونية والامتثال | — | — | — | — | — | 2 / 0 | — | 10 / 4 |
| AUTH-GRANT — صاحب سلطة أو معتمِد ثانٍ | 5 / 1 | 2 / 0 | 4 / 1 | 6 / 0 | 10 / 0 | 3 / 0 | 9 / 0 | 9 / 0 |
| REL-TASK — المنفّذ والمراجع | — | 0 / 1 | 3 / 0 | 13 / 0 | 1 / 0 | 2 / 0 | 8 / 3 | — |
| REL-OWNER — المالك والطالب والمشارك | 0 / 5 | 9 / 2 | — | 23 / 1 | 1 / 3 | 2 / 2 | 5 / 3 | 0 / 2 |
| REL-RECIPIENT — المستلم والمشترك | — | — | 4 / 0 | 1 / 1 | — | — | — | — |
| REL-INCIDENT — أدوار الحادثة | — | — | — | 10 / 1 | — | — | — | — |
| REL-PEER — الشخص الثاني | — | 5 / 0 | 1 / 0 | — | — | — | 4 / 0 | — |
| ANY-USER — أي مستخدم مخوَّل | 3 / 1 | 0 / 17 | 0 / 16 | 5 / 17 | 0 / 17 | 4 / 6 | 6 / 7 | 1 / 1 |
| SYS — هويات النظام والخدمات | 8 / 1 | 30 / 2 | — | — | 1 / 1 | — | — | 0 / 2 |

### 2.3 مصفوفة الفاعل × نوع العملية

| الفاعل / الدور | إنشاء | تعديل | سير عمل | حذف / إنهاء | نظام | جلب |
|---|---|---|---|---|---|---|
| ACT-01 Executive — القيادي التنفيذي | — | — | 1 | 1 | — | 1 |
| ACT-02 Manager — المدير | 6 | 13 | 12 | 9 | — | 4 |
| ACT-03 Planner — المخطِّط | 11 | 19 | 13 | 17 | — | 2 |
| ACT-04 Analyst — المحلل | 27 | 38 | 38 | 30 | — | 11 |
| ACT-05 Operator — المشغِّل | 2 | 3 | 1 | 1 | — | — |
| ACT-06 Field User — المستخدم الميداني | 4 | 3 | 2 | 1 | — | 2 |
| ACT-07 Resource Manager — مدير الموارد | 6 | 6 | 12 | 8 | — | 1 |
| ACT-08 Logistics User — مستخدم الإمداد | 2 | 1 | 2 | 5 | — | — |
| ACT-09 Risk Manager — مدير المخاطر | 1 | — | 3 | 1 | — | 1 |
| ACT-10 Training Manager — مدير التدريب | 4 | 6 | 8 | 6 | — | 1 |
| ACT-11 Knowledge Manager — مدير المعرفة | 1 | 1 | 2 | 3 | — | — |
| ACT-12 Archivist — أمين الأرشيف | 1 | 2 | 4 | 2 | — | 4 |
| ACT-13 Security Officer — مسؤول الأمن | 3 | 10 | 21 | 9 | — | 9 |
| ACT-14 Auditor — المدقِّق | 1 | — | — | 1 | — | 14 |
| ACT-15 Administrator — مسؤول الإدارة | 10 | 15 | 25 | 16 | — | 10 |
| PLT-OPS — مشغّل المنصة | 2 | 1 | 6 | 2 | — | 2 |
| PLT-AI — مهندس/حوكمة الذكاء الاصطناعي | 4 | 2 | 7 | 4 | — | 3 |
| PLT-INT — مهندس التكامل | 2 | 1 | 4 | 1 | — | 2 |
| AUTH-LEGAL — السلطة القانونية والامتثال | 3 | 1 | 5 | 3 | — | 4 |
| AUTH-GRANT — صاحب سلطة أو معتمِد ثانٍ | 5 | 2 | 24 | 17 | — | 2 |
| REL-TASK — المنفّذ والمراجع | — | 4 | 15 | 8 | — | 4 |
| REL-OWNER — المالك والطالب والمشارك | 6 | 12 | 9 | 13 | — | 18 |
| REL-RECIPIENT — المستلم والمشترك | 1 | — | 1 | 3 | — | 1 |
| REL-INCIDENT — أدوار الحادثة | 1 | 3 | 4 | 2 | — | 1 |
| REL-PEER — الشخص الثاني | — | — | 7 | 3 | — | — |
| ANY-USER — أي مستخدم مخوَّل | 5 | 3 | 5 | 6 | — | 82 |
| SYS — هويات النظام والخدمات | 8 | 12 | 9 | 4 | 6 | 6 |

### 2.4 عمليات كل فاعل

لكل فاعل: الأوامر ثم الاستعلامات حسب السياق. القصة المقابلة لكل معرّف في `05-user-stories/us-bcNN.md`.

#### ACT-01 Executive — القيادي التنفيذي

- **BC01:** `CMD-AUT-APPROVE-GRANT`, `CMD-AUT-REJECT-GRANT`, `QRY-AUT-LIST`

#### ACT-02 Manager — المدير

- **BC02:** `CMD-CRQ-AMEND`, `CMD-CRQ-APPROVE`, `CMD-CRQ-REJECT`, `QRY-CRQ-EVIDENCE`
- **BC03:** `CMD-ARL-ACTIVATE`, `CMD-ARL-DEFINE`, `CMD-ARL-DISABLE`, `CMD-ARL-EDIT`, `CMD-ARL-ENABLE`, `CMD-ARL-RETIRE`, `CMD-SIT-ACTIVATE`, `CMD-SIT-CLOSE`, `CMD-SIT-CREATE`, `CMD-SIT-EDIT-DEFINITION`, `CMD-SIT-PAUSE`, `CMD-SIT-RESUME`
- **BC04:** `CMD-CRD-ACTIVATE`, `CMD-CRD-ADD-PARTICIPANT`, `CMD-CRD-ASSIGN-RESPONSIBILITY`, `CMD-CRD-CANCEL`, `CMD-CRD-CLOSE`, `CMD-CRD-OPEN`, `CMD-CRD-REMOVE-PARTICIPANT`, `CMD-DRQ-ADD-OPTION`, `CMD-DRQ-CITE`, `CMD-DRQ-CREATE`, `CMD-DRQ-OPEN`, `CMD-DRQ-WITHDRAW`, `CMD-TASK-ASSIGN`, `CMD-TASK-CANCEL`, `CMD-TASK-CREATE`, `CMD-TASK-EDIT`, `CMD-TASK-MARK-READY`, `CMD-TASK-REASSIGN`, `CMD-TASK-RECLASSIFY`, `CMD-TASK-SET-DUE`, `CMD-TASK-SUSPEND`, `CMD-TASK-UNSUSPEND`
- **BC05:** `QRY-ELIG-CHECK`, `QRY-QUAL-LIST`, `QRY-READINESS`
- **BC06:** `CMD-DST-CANCEL`, `CMD-DST-DISTRIBUTE`, `CMD-PRD-WITHDRAW`

#### ACT-03 Planner — المخطِّط

- **BC02:** `CMD-CPL-ACTIVATE`, `CMD-CPL-ADD-ACTIVITY`, `CMD-CPL-CANCEL`, `CMD-CPL-COMPLETE`, `CMD-CPL-CREATE`, `CMD-CPL-REMOVE-ACTIVITY`, `QRY-CPL-GET`
- **BC04:** `CMD-DRQ-ADD-OPTION`, `CMD-DRQ-CITE`, `CMD-DRQ-CREATE`, `CMD-DRQ-OPEN`, `CMD-DRQ-WITHDRAW`, `CMD-OUT-CORRECT`, `CMD-OUT-RECORD`, `CMD-PLN-CLOSE`, `CMD-PLN-COMPLETE`, `CMD-PLN-CREATE`, `CMD-PLN-RESUME`, `CMD-PLN-SUSPEND`, `CMD-PLV-AMEND-MINOR`, `CMD-PLV-DISCARD`, `CMD-PLV-DRAFT`, `CMD-PLV-EDIT`, `CMD-PLV-SUBMIT`, `CMD-TASK-ASSIGN`, `CMD-TASK-CANCEL`, `CMD-TASK-CLOSE`, `CMD-TASK-CREATE`, `CMD-TASK-EDIT`, `CMD-TASK-ESCALATE`, `CMD-TASK-MARK-READY`, `CMD-TASK-REASSIGN`, `CMD-TASK-RECLASSIFY`, `CMD-TASK-SET-DUE`, `CMD-TASK-SUSPEND`, `CMD-TASK-UNSUSPEND`, `CMD-TTY-ACTIVATE`, `CMD-TTY-DEFINE`, `CMD-TTY-EDIT`, `CMD-TTY-RETIRE`
- **BC05:** `CMD-ALC-RELEASE`, `CMD-ALC-REQUEST`, `CMD-ASG-ASSIGN`, `CMD-ASG-CANCEL`, `CMD-ASG-RETURN`, `CMD-LGR-REQUEST`, `CMD-RSV-CANCEL`, `CMD-RSV-CONFIRM`, `CMD-RSV-HOLD`, `CMD-RSV-RELEASE`, `QRY-ELIG-CHECK`
- **BC06:** `CMD-KNO-EDIT`, `CMD-KNO-RECORD-REUSE`, `CMD-PRD-CREATE`, `CMD-PRD-DISCARD`, `CMD-PRD-EDIT-NARRATIVE`, `CMD-PRD-GENERATE`, `CMD-PRD-SUBMIT`
- **BC07:** `CMD-SCF-ASSIGN`, `CMD-SCF-DISCARD`, `CMD-SCF-REAPPLY`, `CMD-SCF-RESOLVE-MANUALLY`

#### ACT-04 Analyst — المحلل

- **BC02:** `CMD-CLM-ASSERT`, `CMD-CLM-ASSESS`, `CMD-CLM-CORRECT`, `CMD-CLM-RECLASSIFY`, `CMD-CLM-RECORD-CHANGE`, `CMD-CLM-RETRACT`, `CMD-CNF-ACCEPT`, `CMD-CNF-ASSIGN`, `CMD-CNF-RAISE`, `CMD-CNF-REOPEN`, `CMD-CNF-RESOLVE`, `CMD-CNF-START-REVIEW`, `CMD-CRP-ACCEPT`, `CMD-CRP-PROPOSE`, `CMD-CRP-REJECT`, `CMD-CRP-START-REVIEW`, `CMD-CRQ-CANCEL`, `CMD-CRQ-DRAFT`, `CMD-CRQ-EDIT`, `CMD-CRQ-MARK-SATISFIED`, `CMD-CRQ-SUBMIT`, `CMD-CRR-DEFINE`, `CMD-CRR-EDIT`, `CMD-CRR-RETIRE`, `CMD-ENT-CHANGE-TYPE`, `CMD-ENT-RECLASSIFY`, `CMD-ENT-REGISTER`, `CMD-ENT-REINSTATE`, `CMD-ENT-RETIRE`, `CMD-ER-CONFIRM-MATCH`, `CMD-ER-DECIDE-MATCH`, `CMD-ER-DECIDE-NOT-MATCH`, `CMD-ER-PARK`, `CMD-ER-PROPOSE`, `CMD-ER-REQUEST-SPLIT`, `CMD-ER-RESUME`, `CMD-ER-SPLIT`, `CMD-ER-START-REVIEW`, `CMD-ER-WITHDRAW`, `CMD-EVD-RECLASSIFY`, `CMD-EVD-REGISTER`, `CMD-EVD-SEAL`, `CMD-EVD-TRANSFER-CUSTODY`, `CMD-EVD-UPDATE-LOCATOR`, `CMD-EVD-WITHDRAW`, `CMD-EVL-LINK`, `CMD-EVL-UNLINK`, `CMD-EXT-END`, `CMD-EXT-MAP`, `CMD-MRS-DRAFT`, `CMD-MRS-EDIT`, `CMD-OBS-AMEND`, `CMD-OBS-ATTACH-EVIDENCE`, `CMD-OBS-RECLASSIFY`, `CMD-OBS-RECORD`, `CMD-OBS-REJECT`, `CMD-OBS-VALIDATE`, `CMD-REL-RECLASSIFY`, `CMD-REL-REGISTER`, `CMD-REL-REINSTATE`, `CMD-REL-RETIRE`, `CMD-RWE-CHANGE-TYPE`, `CMD-RWE-RECLASSIFY`, `CMD-RWE-REGISTER`, `CMD-RWE-REINSTATE`, `CMD-RWE-RETIRE`, `CMD-SRC-RATE-RELIABILITY`, `CMD-SRC-REGISTER`, `CMD-SRC-REINSTATE`, `CMD-SRC-RETIRE`, `CMD-SRC-SUSPEND`, `CMD-SRC-UPDATE-PROFILE`, `QRY-CLUSTER-GET`, `QRY-CNF-GET`, `QRY-CNF-LIST`, `QRY-CRP-QUEUE`, `QRY-ER-GET`, `QRY-ER-QUEUE`, `QRY-EXT-RESOLVE`, `QRY-MRS-GET`, `QRY-SRC-GET`
- **BC03:** `CMD-ACS-ADD-ASSUMPTION`, `CMD-ACS-ADD-HYPOTHESIS`, `CMD-ACS-CANCEL`, `CMD-ACS-CLOSE`, `CMD-ACS-CREATE`, `CMD-ACS-DEFINE`, `CMD-ACS-DEFINE-SCENARIO`, `CMD-ACS-DESELECT-EVIDENCE`, `CMD-ACS-OPEN`, `CMD-ACS-REOPEN`, `CMD-ACS-RETIRE-ASSUMPTION`, `CMD-ACS-SELECT-EVIDENCE`, `CMD-ACS-UPDATE-HYPOTHESIS`, `CMD-AMT-DEPRECATE`, `CMD-AMT-REGISTER`, `CMD-AMT-RETIRE`, `CMD-ARL-ACTIVATE`, `CMD-ARL-DEFINE`, `CMD-ARL-DISABLE`, `CMD-ARL-EDIT`, `CMD-ARL-ENABLE`, `CMD-ARL-RETIRE`, `CMD-ASM-DISCARD`, `CMD-ASM-DRAFT`, `CMD-ASM-EDIT`, `CMD-ASM-PUBLISH`, `CMD-ASM-RETURN`, `CMD-ASM-SUBMIT`, `CMD-ASM-WITHDRAW`, `CMD-FND-ACCEPT`, `CMD-FND-EDIT`, `CMD-FND-RECORD`, `CMD-FND-WITHDRAW`, `CMD-RUN-CANCEL`, `CMD-RUN-REPRODUCE`, `CMD-RUN-SUBMIT`, `CMD-SIT-ACTIVATE`, `CMD-SIT-CLOSE`, `CMD-SIT-CREATE`, `CMD-SIT-EDIT-DEFINITION`, `CMD-SIT-PAUSE`, `CMD-SIT-RESUME`, `QRY-AMT-LIST`
- **BC04:** `CMD-DRQ-ADD-OPTION`, `CMD-DRQ-CITE`, `CMD-DRQ-CREATE`, `CMD-DRQ-OPEN`, `CMD-DRQ-WITHDRAW`
- **BC06:** `CMD-PRD-CREATE`, `CMD-PRD-DISCARD`, `CMD-PRD-EDIT-NARRATIVE`, `CMD-PRD-GENERATE`, `CMD-PRD-SUBMIT`, `CMD-PTM-DEFINE`, `CMD-PTM-EDIT`, `CMD-PTM-RETIRE`, `CMD-REC-CANCEL`, `CMD-REC-REQUEST`
- **BC07:** `CMD-SCF-ASSIGN`, `CMD-SCF-DISCARD`, `CMD-SCF-REAPPLY`, `CMD-SCF-RESOLVE-MANUALLY`, `QRY-SNS-LIST`

#### ACT-05 Operator — المشغِّل

- **BC02:** `CMD-OBS-AMEND`, `CMD-OBS-ATTACH-EVIDENCE`, `CMD-OBS-RECLASSIFY`, `CMD-OBS-RECORD`
- **BC03:** `CMD-CAP-CANCEL`, `CMD-CAP-PREPARE`, `CMD-CAP-RETRY`

#### ACT-06 Field User — المستخدم الميداني

- **BC02:** `CMD-EVD-REGISTER`, `CMD-OBS-AMEND`, `CMD-OBS-ATTACH-EVIDENCE`, `CMD-OBS-RECLASSIFY`, `CMD-OBS-RECORD`
- **BC07:** `CMD-PKG-CONFIRM-DOWNLOAD`, `CMD-PKG-REQUEST`, `CMD-PKG-REVOKE`, `CMD-SYN-OPEN`, `CMD-SYN-UPLOAD-BATCH`, `QRY-PKG-GET`, `QRY-SYN-DELTA`

#### ACT-07 Resource Manager — مدير الموارد

- **BC05:** `CMD-ASG-ASSIGN`, `CMD-ASG-CANCEL`, `CMD-ASG-RETURN`, `CMD-AST-FAIL-MAINTENANCE`, `CMD-AST-MARK-UNSERVICEABLE`, `CMD-AST-RECOVER`, `CMD-AST-REGISTER`, `CMD-AST-REPORT-LOST`, `CMD-AST-RETURN-TO-SERVICE`, `CMD-AST-SET-CERTIFICATION`, `CMD-AST-START-MAINTENANCE`, `CMD-AST-TRANSFER-CUSTODY`, `CMD-AST-UPDATE-CONDITION`, `CMD-MNT-CANCEL`, `CMD-MNT-COMPLETE`, `CMD-MNT-PLAN`, `CMD-MNT-RESCHEDULE`, `CMD-MNT-START`, `CMD-QUAL-RECORD`, `CMD-QUAL-REINSTATE`, `CMD-QUAL-RENEW`, `CMD-QUAL-REVOKE`, `CMD-QUAL-SUSPEND`, `CMD-RPL-ADJUST-CAPACITY`, `CMD-RPL-CLOSE`, `CMD-RPL-CREATE`, `CMD-RPL-RESUME`, `CMD-RPL-SUSPEND`, `CMD-RSV-CANCEL`, `CMD-RSV-CONFIRM`, `CMD-RSV-HOLD`, `CMD-RSV-RELEASE`, `QRY-QUAL-LIST`

#### ACT-08 Logistics User — مستخدم الإمداد

- **BC05:** `CMD-LGR-CANCEL`, `CMD-LGR-DISPATCH`, `CMD-LGR-REQUEST`, `CMD-SHP-CANCEL`, `CMD-SHP-DELIVER`, `CMD-SHP-DEPART`, `CMD-SHP-PLAN`, `CMD-SHP-RECORD-CHECKPOINT`, `CMD-SHP-REPORT-DAMAGE`, `CMD-SHP-REPORT-LOST`

#### ACT-09 Risk Manager — مدير المخاطر

- **BC04:** `CMD-RIS-ASSESS`, `CMD-RIS-CLOSE`, `CMD-RIS-IDENTIFY`, `CMD-RIS-PLAN-TREATMENT`, `CMD-RIS-REASSESS`, `QRY-RIS-GET`

#### ACT-10 Training Manager — مدير التدريب

- **BC02:** `CMD-CLM-ASSESS`
- **BC05:** `CMD-EXR-CANCEL`, `CMD-EXR-PLAN`, `CMD-EXR-SCHEDULE`, `CMD-EXR-START`, `CMD-QUAL-RECORD`, `CMD-QUAL-REINSTATE`, `CMD-QUAL-RENEW`, `CMD-QUAL-REVOKE`, `CMD-QUAL-SUSPEND`, `CMD-RRQ-ACTIVATE`, `CMD-RRQ-DEFINE`, `CMD-RRQ-EDIT`, `CMD-RRQ-RETIRE`, `CMD-SCN-ACTIVATE`, `CMD-SCN-DEFINE`, `CMD-SCN-EDIT`, `CMD-SCN-RETIRE`, `CMD-SIM-ABORT`, `CMD-SIM-COMPLETE`, `CMD-SIM-DELIVER-INJECT`, `CMD-SIM-PAUSE`, `CMD-SIM-RECORD-EVALUATION`, `CMD-SIM-RESUME`, `QRY-READINESS`

#### ACT-11 Knowledge Manager — مدير المعرفة

- **BC06:** `CMD-KNO-PUBLISH`, `CMD-KNO-REJECT`, `CMD-KNO-RETIRE`, `CMD-KNO-RETURN`, `CMD-PTM-DEFINE`, `CMD-PTM-EDIT`, `CMD-PTM-RETIRE`

#### ACT-12 Archivist — أمين الأرشيف

- **BC06:** `CMD-ARC-MIGRATE-FORMAT`, `CMD-ARC-REPAIR`, `CMD-ARC-RETRY-INGEST`
- **BC08:** `CMD-DSP-APPROVE`, `CMD-DSP-CANCEL`, `CMD-DSP-SUBMIT`, `CMD-RTS-DISCARD`, `CMD-RTS-DRAFT`, `CMD-RTS-EDIT`, `QRY-DSP-GET`, `QRY-LHD-CHECK`, `QRY-LHD-LIST`, `QRY-RTS-ACTIVE`

#### ACT-13 Security Officer — مسؤول الأمن

- **BC01:** `CMD-CLR-APPROVE`, `CMD-CLR-GRANT`, `CMD-CLR-MODIFY`, `CMD-CLR-REINSTATE`, `CMD-CLR-REVOKE`, `CMD-CLR-SUSPEND`, `CMD-DEV-RETIRE`, `CMD-DEV-ROTATE-KEY`, `CMD-USR-LOCK`, `CMD-USR-UNLOCK`, `QRY-CLR-GET`, `QRY-HRS-QUEUE`
- **BC02:** `CMD-SRC-RECLASSIFY`, `CMD-SRC-REINSTATE`, `CMD-SRC-RETIRE`, `CMD-SRC-SET-PROTECTION`, `CMD-SRC-SUSPEND`
- **BC03:** `CMD-ACS-RECLASSIFY`, `CMD-SIT-RECLASSIFY`, `CMD-SIT-RESUME`
- **BC04:** `CMD-PLN-RECLASSIFY`
- **BC05:** `CMD-AST-FAIL-MAINTENANCE`, `CMD-AST-MARK-UNSERVICEABLE`, `CMD-AST-RECLASSIFY`, `CMD-AST-RECOVER`, `CMD-AST-RETURN-TO-SERVICE`, `CMD-AST-START-MAINTENANCE`
- **BC06:** `QRY-DST-LOG`
- **BC07:** `CMD-CON-ACTIVATE`, `CMD-PKG-REVOKE`, `CMD-TOL-ACTIVATE`, `CMD-TOL-DISABLE`, `CMD-TOL-ENABLE`, `CMD-TOL-RETIRE`, `QRY-CON-LIST`, `QRY-RTG-ACTIVE`, `QRY-TOL-LIST`
- **BC08:** `CMD-CLS-ACTIVATE`, `CMD-CLS-DISCARD`, `CMD-CLS-DRAFT`, `CMD-CLS-EDIT`, `CMD-EXC-APPROVE`, `CMD-EXC-REJECT`, `CMD-EXC-REVOKE`, `CMD-POL-APPROVE`, `CMD-POL-DRAFT`, `CMD-POL-EDIT`, `CMD-POL-REJECT`, `CMD-POL-SUBMIT`, `QRY-AUD-SEARCH`, `QRY-EXC-LIST`, `QRY-POL-GET`

#### ACT-14 Auditor — المدقِّق

- **BC03:** `QRY-CAP-LIST`
- **BC06:** `CMD-REC-CANCEL`, `CMD-REC-REQUEST`, `QRY-DST-LOG`, `QRY-REC-REPORT`
- **BC07:** `QRY-AIR-CONTEXT`, `QRY-AIR-GET`, `QRY-MDL-LIST`
- **BC08:** `QRY-AUD-SEARCH`, `QRY-AUD-VERIFY`, `QRY-DSP-GET`, `QRY-ERS-GET`, `QRY-EXC-LIST`, `QRY-LHD-LIST`, `QRY-POL-GET`, `QRY-RTS-ACTIVE`

#### ACT-15 Administrator — مسؤول الإدارة

- **BC01:** `CMD-DEV-CONFIRM`, `CMD-DEV-REINSTATE`, `CMD-DEV-RETIRE`, `CMD-DEV-ROTATE-KEY`, `CMD-DEV-SUSPEND`, `CMD-HRS-APPROVE`, `CMD-HRS-REJECT`, `CMD-ORG-ADD-UNIT`, `CMD-ORG-CREATE`, `CMD-ORG-DEACTIVATE`, `CMD-ORG-DEACTIVATE-UNIT`, `CMD-ORG-MOVE-UNIT`, `CMD-ORG-REACTIVATE`, `CMD-ORG-RENAME`, `CMD-ORG-RENAME-UNIT`, `CMD-PER-DEACTIVATE`, `CMD-PER-ERASE`, `CMD-PER-REACTIVATE`, `CMD-PER-REGISTER`, `CMD-PER-UPDATE-DETAILS`, `CMD-RAS-ASSIGN`, `CMD-RAS-REVOKE`, `CMD-ROL-ACTIVATE`, `CMD-ROL-DEFINE`, `CMD-ROL-RETIRE`, `CMD-ROL-SET-PERMISSIONS`, `CMD-SVC-CLOSE`, `CMD-SVC-CREATE`, `CMD-SVC-DISABLE`, `CMD-SVC-ENABLE`, `CMD-SVC-ROTATE-CREDENTIAL`, `CMD-USR-CLOSE`, `CMD-USR-DISABLE`, `CMD-USR-ENABLE`, `CMD-USR-LINK-IDENTITY`, `CMD-USR-LINK-PERSON`, `CMD-USR-LOCK`, `CMD-USR-PROVISION`, `CMD-USR-UNLINK-IDENTITY`, `CMD-USR-UNLOCK`, `QRY-AUT-LIST`, `QRY-DEV-LIST`, `QRY-HRS-QUEUE`, `QRY-TEN-GET`, `QRY-USR-GET`, `QRY-USR-LIST`
- **BC02:** `CMD-IMP-ACCEPT-QUARANTINE`, `CMD-IMP-CANCEL`, `CMD-IMP-REPROCESS-QUARANTINE`, `CMD-IMP-SUBMIT`, `CMD-MRS-ACTIVATE`, `QRY-IMP-GET`, `QRY-MRS-GET`
- **BC03:** `CMD-AMT-ACTIVATE`, `CMD-AMT-DEPRECATE`, `CMD-AMT-RETIRE`
- **BC04:** `CMD-TTY-ACTIVATE`, `CMD-TTY-DEFINE`, `CMD-TTY-EDIT`, `CMD-TTY-RETIRE`
- **BC05:** `CMD-RRQ-ACTIVATE`, `CMD-RRQ-DEFINE`, `CMD-RRQ-EDIT`, `CMD-RRQ-RETIRE`
- **BC07:** `CMD-ADP-ACTIVATE`, `CMD-ADP-REGISTER`, `CMD-ADP-RESUME`, `CMD-ADP-RETIRE`, `CMD-ADP-SUSPEND`, `CMD-ADP-UPDATE-MAPPING`, `CMD-CON-RESUME`, `CMD-CON-RETIRE`, `CMD-CON-SUSPEND`, `CMD-PKG-REVOKE`, `QRY-ADP-GET`, `QRY-AI-USAGE`

#### PLT-OPS — مشغّل المنصة

- **BC01:** `CMD-TEN-PROVISION`, `CMD-TEN-REACTIVATE`, `CMD-TEN-RETRY-PROVISIONING`, `CMD-TEN-START-CELL-MIGRATION`, `CMD-TEN-START-DECOMMISSION`, `CMD-TEN-SUSPEND`, `CMD-TEN-UPDATE-QUOTAS`, `QRY-TEN-GET`
- **BC07:** `CMD-PRJ-CANCEL-BUILD`, `CMD-PRJ-CREATE-VERSION`, `CMD-PRJ-PROMOTE`, `CMD-PRJ-RETIRE`, `QRY-PRJ-STATUS`

#### PLT-AI — مهندس/حوكمة الذكاء الاصطناعي

- **BC07:** `CMD-EVS-DRAFT`, `CMD-EVS-EDIT`, `CMD-MDL-APPROVE`, `CMD-MDL-DEPRECATE`, `CMD-MDL-FAIL-EVALUATION`, `CMD-MDL-PROMOTE`, `CMD-MDL-REGISTER`, `CMD-MDL-REINSTATE`, `CMD-MDL-RETIRE`, `CMD-MDL-STAGE`, `CMD-MDL-START-EVALUATION`, `CMD-RTG-DISCARD`, `CMD-RTG-DRAFT`, `CMD-RTG-EDIT`, `CMD-TOL-ENABLE`, `CMD-TOL-REGISTER`, `CMD-TOL-RETIRE`, `QRY-MDL-LIST`, `QRY-RTG-ACTIVE`, `QRY-TOL-LIST`

#### PLT-INT — مهندس التكامل

- **BC07:** `CMD-CON-FAIL-TEST`, `CMD-CON-REGISTER`, `CMD-CON-TEST`, `CMD-SNS-ACTIVATE`, `CMD-SNS-PAUSE`, `CMD-SNS-REGISTER`, `CMD-SNS-RETIRE`, `CMD-SNS-SET-QUALITY-RULES`, `QRY-CON-LIST`, `QRY-SNS-LIST`

#### AUTH-LEGAL — السلطة القانونية والامتثال

- **BC06:** `CMD-REC-CANCEL`, `CMD-REC-REQUEST`
- **BC08:** `CMD-DSP-APPROVE`, `CMD-ERS-APPROVE`, `CMD-ERS-REGISTER`, `CMD-ERS-REJECT`, `CMD-LHD-APPROVE-RELEASE`, `CMD-LHD-CANCEL-RELEASE`, `CMD-LHD-EXTEND`, `CMD-LHD-PLACE`, `CMD-LHD-REQUEST-RELEASE`, `CMD-RTS-ACTIVATE`, `QRY-DSP-GET`, `QRY-ERS-GET`, `QRY-LHD-LIST`, `QRY-RTS-ACTIVE`

#### AUTH-GRANT — صاحب سلطة أو معتمِد ثانٍ

- **BC01:** `CMD-AUT-DELEGATE`, `CMD-AUT-GRANT`, `CMD-AUT-RESUME`, `CMD-AUT-REVOKE`, `CMD-AUT-SUSPEND`, `QRY-AUT-LIST`
- **BC02:** `CMD-CRR-ACTIVATE`, `CMD-CRR-RETIRE`
- **BC03:** `CMD-AMT-ACTIVATE`, `CMD-AMT-DEPRECATE`, `CMD-AMT-RETIRE`, `CMD-CAP-RELEASE`, `QRY-CAP-LIST`
- **BC04:** `CMD-DEC-ANNUL`, `CMD-DEC-RECORD`, `CMD-PLN-CANCEL`, `CMD-PLV-APPROVE`, `CMD-PLV-REJECT`, `CMD-PLV-RETURN`
- **BC05:** `CMD-ALC-APPROVE`, `CMD-ALC-PREEMPT`, `CMD-ALC-REJECT`, `CMD-AST-DISPOSE`, `CMD-AST-FAIL-MAINTENANCE`, `CMD-AST-MARK-UNSERVICEABLE`, `CMD-AST-RECOVER`, `CMD-AST-RETURN-TO-SERVICE`, `CMD-AST-START-MAINTENANCE`, `CMD-LGR-CANCEL`
- **BC06:** `CMD-ARC-TRANSFER`, `CMD-PTM-ACTIVATE`, `CMD-PTM-RETIRE`
- **BC07:** `CMD-EVS-ACTIVATE`, `CMD-MDL-APPROVE`, `CMD-MDL-PROMOTE`, `CMD-MDL-REINSTATE`, `CMD-MDL-RETIRE`, `CMD-RTG-ACTIVATE`, `CMD-RTG-DISCARD`, `CMD-RTG-DRAFT`, `CMD-RTG-EDIT`
- **BC08:** `CMD-DSP-APPROVE`, `CMD-ERS-APPROVE`, `CMD-ERS-REJECT`, `CMD-LHD-APPROVE-RELEASE`, `CMD-LHD-CANCEL-RELEASE`, `CMD-LHD-EXTEND`, `CMD-LHD-PLACE`, `CMD-LHD-REQUEST-RELEASE`, `CMD-RTS-ACTIVATE`

#### REL-TASK — المنفّذ والمراجع

- **BC02:** `QRY-CRP-GET`
- **BC03:** `CMD-ASM-PUBLISH`, `CMD-ASM-RETURN`, `CMD-ASM-WITHDRAW`
- **BC04:** `CMD-TASK-ACCEPT`, `CMD-TASK-ADD-RESULT-ITEM`, `CMD-TASK-APPROVE`, `CMD-TASK-BLOCK`, `CMD-TASK-COMPLETE`, `CMD-TASK-DECLINE`, `CMD-TASK-ESCALATE`, `CMD-TASK-REJECT`, `CMD-TASK-RESUME`, `CMD-TASK-RETURN`, `CMD-TASK-START`, `CMD-TASK-START-REVIEW`, `CMD-TASK-SUBMIT`
- **BC05:** `CMD-ALC-RECORD-CONSUMPTION`
- **BC06:** `CMD-PRD-APPROVE`, `CMD-PRD-RETURN`
- **BC07:** `CMD-AIRS-ACCEPT`, `CMD-AIRS-ACCEPT-PARTIALLY`, `CMD-AIRS-REJECT`, `CMD-AIRS-START-REVIEW`, `CMD-SCF-ASSIGN`, `CMD-SCF-DISCARD`, `CMD-SCF-REAPPLY`, `CMD-SCF-RESOLVE-MANUALLY`, `QRY-AIRS-QUEUE`, `QRY-SCF-GET`, `QRY-SCF-LIST`

#### REL-OWNER — المالك والطالب والمشارك

- **BC01:** `QRY-AUT-CHECK`, `QRY-CLR-GET`, `QRY-DEV-LIST`, `QRY-SEC-CONTEXT`, `QRY-USR-GET`
- **BC02:** `CMD-ATT-COMPLETE-UPLOAD`, `CMD-ATT-ERASE`, `CMD-ATT-INITIATE-UPLOAD`, `CMD-CRQ-CANCEL`, `CMD-CRQ-DRAFT`, `CMD-CRQ-EDIT`, `CMD-CRQ-MARK-SATISFIED`, `CMD-CRQ-SUBMIT`, `CMD-EVD-TRANSFER-CUSTODY`, `QRY-CRQ-EVIDENCE`, `QRY-IMP-GET`
- **BC04:** `CMD-CRD-ACTIVATE`, `CMD-CRD-ADD-PARTICIPANT`, `CMD-CRD-ASSIGN-RESPONSIBILITY`, `CMD-CRD-CANCEL`, `CMD-CRD-CLOSE`, `CMD-CRD-OPEN`, `CMD-CRD-REMOVE-PARTICIPANT`, `CMD-CRD-REQUEST-DECISION`, `CMD-CRD-UPDATE-RESPONSIBILITY`, `CMD-OUT-CORRECT`, `CMD-OUT-RECORD`, `CMD-PLN-CLOSE`, `CMD-PLN-COMPLETE`, `CMD-PLN-CREATE`, `CMD-PLN-RESUME`, `CMD-PLN-SUSPEND`, `CMD-SUB-PAUSE`, `CMD-SUB-RESUME`, `CMD-SUB-SUBSCRIBE`, `CMD-SUB-UNSUBSCRIBE`, `CMD-SUB-UPDATE-CHANNELS`, `CMD-TASK-CLOSE`, `CMD-TASK-ESCALATE`, `QRY-CRD-GET`
- **BC05:** `CMD-LGR-CANCEL`, `QRY-MNT-SCHEDULE`, `QRY-QUAL-LIST`, `QRY-READINESS`
- **BC06:** `CMD-DST-CANCEL`, `CMD-DST-DISTRIBUTE`, `QRY-DST-LOG`, `QRY-REC-REPORT`
- **BC07:** `CMD-CON-ACTIVATE`, `CMD-SCF-ASSIGN`, `CMD-SCF-DISCARD`, `CMD-SCF-REAPPLY`, `CMD-SCF-RESOLVE-MANUALLY`, `QRY-AIR-CONTEXT`, `QRY-AIR-GET`, `QRY-PKG-GET`
- **BC08:** `QRY-AUD-SEARCH`, `QRY-LHD-CHECK`

#### REL-RECIPIENT — المستلم والمشترك

- **BC03:** `CMD-ALR-ACKNOWLEDGE`, `CMD-ALR-DISMISS`, `CMD-ALR-RESOLVE`, `CMD-CAP-PREPARE`
- **BC04:** `CMD-NTF-MARK-READ`, `QRY-NTF-INBOX`

#### REL-INCIDENT — أدوار الحادثة

- **BC04:** `CMD-INC-ACTIVATE-CONTINGENCY`, `CMD-INC-ASSESS`, `CMD-INC-CANCEL`, `CMD-INC-CLOSE`, `CMD-INC-CONTAIN`, `CMD-INC-DE-ESCALATE`, `CMD-INC-DISPATCH-RESPONSE`, `CMD-INC-ESCALATE`, `CMD-INC-REPORT`, `CMD-INC-RESOLVE`, `QRY-INC-RECOVERY-STATUS`

#### REL-PEER — الشخص الثاني

- **BC02:** `CMD-ER-CONFIRM-MATCH`, `CMD-ER-PARK`, `CMD-ER-RESUME`, `CMD-ER-SPLIT`, `CMD-ER-WITHDRAW`
- **BC03:** `CMD-FND-ACCEPT`
- **BC07:** `CMD-ADP-ACTIVATE`, `CMD-ADP-RESUME`, `CMD-ADP-RETIRE`, `CMD-ADP-SUSPEND`

#### ANY-USER — أي مستخدم مخوَّل

- **BC01:** `CMD-DEV-ENROLL`, `CMD-DEV-REPORT-LOST`, `CMD-DEV-ROTATE-KEY`, `QRY-ORG-TREE`
- **BC02:** `QRY-ATT-DOWNLOAD`, `QRY-CLM-GET`, `QRY-CPL-GET`, `QRY-CRP-GET`, `QRY-CRQ-BOARD`, `QRY-CRQ-GET`, `QRY-ENT-CLAIMS`, `QRY-ENT-LIST`, `QRY-ENT-POSITIONS`, `QRY-ENT-RESOLVED`, `QRY-EVD-GET`, `QRY-LIN-TRACE`, `QRY-OBS-GET`, `QRY-OBS-LIST`, `QRY-REL-LIST`, `QRY-RWE-GET`, `QRY-SRC-GET`
- **BC03:** `QRY-ACS-GET`, `QRY-ACS-LIST`, `QRY-ALR-LIST`, `QRY-AMT-LIST`, `QRY-ASM-GET`, `QRY-ASM-VERSIONS`, `QRY-BASE-TILE`, `QRY-FND-LIST`, `QRY-RUN-ARTIFACT`, `QRY-RUN-GET`, `QRY-SCN-COMPARE`, `QRY-SIT-CHANGES`, `QRY-SIT-COP`, `QRY-SIT-GET`, `QRY-SIT-LIST`, `QRY-SIT-TILE`
- **BC04:** `CMD-SUB-PAUSE`, `CMD-SUB-RESUME`, `CMD-SUB-SUBSCRIBE`, `CMD-SUB-UNSUBSCRIBE`, `CMD-SUB-UPDATE-CHANNELS`, `QRY-CRD-LIST`, `QRY-DEC-BASIS`, `QRY-DEC-GET`, `QRY-DRQ-GET`, `QRY-DRQ-LIST`, `QRY-INC-GET`, `QRY-INC-LIST`, `QRY-OUT-SERIES`, `QRY-PLN-GET`, `QRY-PLN-PROGRESS`, `QRY-PLV-DIFF`, `QRY-PLV-LIST`, `QRY-RIS-REGISTER`, `QRY-TASK-GET`, `QRY-TASK-HISTORY`, `QRY-TASK-LIST`, `QRY-TTY-GET`
- **BC05:** `QRY-ALC-LIST`, `QRY-AST-AVAILABILITY`, `QRY-AST-GET`, `QRY-EXR-GET`, `QRY-EXR-LIST`, `QRY-LGR-GET`, `QRY-LGR-LIST`, `QRY-MNT-SCHEDULE`, `QRY-POL-TIMELINE`, `QRY-SCN-GET`, `QRY-SCN-LIST`, `QRY-SHP-GET`, `QRY-SHP-LIST`, `QRY-SHP-TRACKING`, `QRY-SIM-GET`, `QRY-SIM-LIST`, `QRY-SIM-TIMELINE`
- **BC06:** `CMD-KNO-DISCARD`, `CMD-KNO-DRAFT`, `CMD-KNO-EDIT`, `CMD-KNO-SUBMIT`, `QRY-ARC-RETRIEVE`, `QRY-ARC-SEARCH`, `QRY-KNO-SEARCH`, `QRY-KNO-SUGGEST`, `QRY-PRD-GET`, `QRY-PRD-LIST`
- **BC07:** `CMD-AIR-CANCEL`, `CMD-AIR-SUBMIT`, `CMD-AIRS-ACCEPT`, `CMD-AIRS-ACCEPT-PARTIALLY`, `CMD-AIRS-REJECT`, `CMD-AIRS-START-REVIEW`, `QRY-AIRS-QUEUE`, `QRY-GRAPH-NEIGHBORHOOD`, `QRY-GRAPH-PATHS`, `QRY-SCF-GET`, `QRY-SCF-LIST`, `QRY-SRCH-QUERY`, `QRY-SRCH-SUGGEST`
- **BC08:** `CMD-EXC-REQUEST`, `QRY-CLS-ACTIVE`

#### SYS — هويات النظام والخدمات

- **BC01:** `CMD-TEN-COMPLETE-CELL-MIGRATION`, `CMD-TEN-COMPLETE-DECOMMISSION`, `CMD-TEN-COMPLETE-PROVISIONING`, `CMD-TEN-FAIL-PROVISIONING`, `CMD-USR-DISABLE`, `CMD-USR-ENABLE`, `CMD-USR-PROVISION`, `CMD-USR-RECORD-FIRST-SIGN-IN`, `QRY-AUT-CHECK`
- **BC02:** `CMD-CLM-ASSERT`, `CMD-CLM-ASSESS`, `CMD-CLM-CORRECT`, `CMD-CLM-RECLASSIFY`, `CMD-CLM-RECORD-CHANGE`, `CMD-CLM-RETRACT`, `CMD-ENT-CHANGE-TYPE`, `CMD-ENT-RECLASSIFY`, `CMD-ENT-REGISTER`, `CMD-ENT-REINSTATE`, `CMD-ENT-RETIRE`, `CMD-EXT-END`, `CMD-EXT-MAP`, `CMD-IMP-ACCEPT-QUARANTINE`, `CMD-IMP-CANCEL`, `CMD-IMP-REPROCESS-QUARANTINE`, `CMD-IMP-SUBMIT`, `CMD-OBS-AMEND`, `CMD-OBS-ATTACH-EVIDENCE`, `CMD-OBS-RECLASSIFY`, `CMD-OBS-RECORD`, `CMD-REL-RECLASSIFY`, `CMD-REL-REGISTER`, `CMD-REL-REINSTATE`, `CMD-REL-RETIRE`, `CMD-RWE-CHANGE-TYPE`, `CMD-RWE-RECLASSIFY`, `CMD-RWE-REGISTER`, `CMD-RWE-REINSTATE`, `CMD-RWE-RETIRE`, `QRY-EXT-RESOLVE`, `QRY-IMP-GET`
- **BC05:** `CMD-SIM-START`, `QRY-ELIG-CHECK`
- **BC08:** `QRY-LHD-CHECK`, `QRY-PDP-DECIDE`

### 2.5 أوصاف أدوار لم تُصنَّف

| الوصف في المصدر | العمليات |
|---|---|
| finance | QRY-AI-USAGE |

<!-- END GENERATED: build_analysis_design.py -->
