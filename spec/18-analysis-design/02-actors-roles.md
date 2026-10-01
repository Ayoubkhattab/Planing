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

من يستخدم النظام، وما يحق لكل فاعل أن يفعله. المصدر المعتمد لكل صلاحية هو سياسة العملية في `08-security/policies-slc*.md`. هذا الملف يجمع سياسات 477 أمرًا و133 استعلامًا من الكتالوجات حسب الفاعل (وسياسة `QRY-LABEL-CHECK` المشتركة بين السياقات خارج العدّ لأنها بلا كتالوج).

## 1. كيف تُقرأ الصلاحيات

قرار التخويل (`08-security/authorization-model.md` §3) يُقيَّم بالترتيب: تطابق المستأجر، ثم قاعدة التصنيف، ثم **الدور** (RBAC: الدور يمنح الإجراء على نوع المورد داخل نطاق تنظيمي)، ثم **السمات** (ABAC: الغرض والوقت والجهاز والولاية والتحفظات وسمات المورد)، ثم **فصل المهام**، ثم الالتزامات. لذلك يظهر في السياسات نوعان من «الفاعل»:

| النوع | المعنى | أمثلة | كيف يُفحص |
|---|---|---|---|
| دور وظيفي | صلاحية مُسندة للمستخدم بإسناد دور (AGG-ROLE-ASSIGNMENT) | Analyst، Planner، Security Officer | RBAC في PDP من `roles[]` في طلب القرار |
| دور علاقة بالمورد | علاقة المستخدم بالمورد المحدد | assignee، reviewer، owner، requester، participant | ABAC: سمة من المورد نفسه (PIP) تُقارن بهوية المستخدم |
| صاحب سلطة | منح سلطة مسجل في BC01 لنوع قرار ونطاق | approver with plan-approval authority، allocation authority | `AuthorityCheck(actor, decision_type, scope, at)` (`03-domain/context-map.md`) |
| هوية نظام | حساب خدمة أو هوية عبء عمل | adapter service account، scheduler | نفس خط الأوامر ونفس السياسات (ADR-P17 القاعدة 5) |

## 2. التصنيف

كل وصف دور في موضوع السياسة (`subject`) يُصنَّف في مجموعة من خمس بقواعد نصية في المولِّد (`ROLE_RULES`) **[Derived]**، بعد حذف قيود فصل المهام (`≠ requester` وأمثالها) التي تقيّد الدور ولا تمنحه: (A) الفاعلون الأعمال الـ15 المعرَّفون في المصدر، (B) أدوار المنصة، (C) أدوار السلطة والاعتماد، (D) أدوار العلاقة بالمورد، (E) الفاعلون النظاميون. العملية تُنسب إلى الأدوار التي تطابق فعلها (نفس قاعدة اختيار الفاعل في قصص المستخدم — `05-user-stories/00-guide.md` §3)، والعدّ يحسب العملية مرة لكل دور. الأوامر التي لم يُحسم فاعلها لا تُنسب لأي دور (§6.6)، وكل مكافأة يفترضها التصنيف مكشوفة في §6.5.

## 3. حقوق القرار (RACI)

من `01-business/stakeholders.md` (`decision_rights`)؛ نموذج السلطة قابل للتهيئة لكل مؤسسة ومملوك لـ BC01.

| القرار | المسؤول (R) | المساءَل (A) | يُستشار (C) | يُبلَّغ (I) | يُفرض في |
|---|---|---|---|---|---|
| قرار عمل (DOM-10) | Manager / Executive حسب السلطة | صاحب السلطة المسجل في BC01 | Analyst | Planner | `CMD-DEC-RECORD` + AuthorityCheck (BRL-003) |
| اعتماد الخطة وخط الأساس | Planner | Manager (≠ المُعد) | Resource Manager | Operator | `POL-PLV-APPROVE` — موضوعها «approver with plan-approval authority ≠ author» لا Manager **[Needs Review]** |
| اعتماد المهمة | Reviewer | Manager (≠ المنفذ) | — | Planner | `POL-TASK-APPROVE` (موضوعها reviewer)، INV-TASK-07 — لا ذكر لـManager **[Needs Review]** |
| نشر التقييم | Analyst | Analysis lead / Manager | Knowledge Manager | Executive | `CMD-ASM-PUBLISH` (reviewer / Analysis lead) — لا ذكر لـManager **[Needs Review]** |
| استثناء أمني | Security Officer | موافقة شخصين | Auditor | Administrator | AGG-SECURITY-EXCEPTION (معتمِد أول ثم ثانٍ) |
| تغيير التصنيف | المُنشئ (Originator) | Security Officer | — | Auditor | أوامر `*-RECLASSIFY` |
| الاحتفاظ والتجميد القانوني | Archivist | Legal / Compliance authority | Security Officer | Auditor | AGG-RETENTION-SCHEDULE، AGG-LEGAL-HOLD |

عمود «يُفرض في» **[Derived]** من السياسات والـAggregates.

## 4. الفاعلون النظاميون الداخليون

`01-business/stakeholders.md` يسرد سبعة فاعلين نظاميين؛ موقع كل منهم في التصميم **[Derived]**:

| الفاعل | أين يُنفَّذ |
|---|---|
| AI | BC07 (AGG-AI-REQUEST، AGG-AI-RESULT)؛ يقرأ الإسقاطات المؤمنة فقط ولا يكتب في R2 (`11-hexagonal-reference.md` §8) |
| Workflow | لا محرك سير عمل: آلات الحالات في الـAggregates والانتقالات التلقائية (`SYS:`) — TD-13 |
| Policy | سياسات OPA مترجمة وموقّعة تُقيَّم مضمَّنة في كل وحدة (TD-08)، وخدمة القرار `QRY-PDP-DECIDE` ومخزن السياسات في BC08 |
| Event Bus | Kafka لكل خلية (TD-04) — `15-event-design.md` |
| Scheduler | سلال زمنية في PostgreSQL + عقود lease داخل الوحدة المالكة (TD-13) |
| Search | إسقاطات BC07 في OpenSearch (TD-02) |
| Notification | AGG-NOTIFICATION وAGG-SUBSCRIPTION في BC04 |

## 5. ملاحظات وفجوات

| البند | الحالة |
|---|---|
| حقوق القرار لمجموعات أصحاب المصلحة (`decision_rights: UNKNOWN` لـ SH-01..05) | **[Missing]** في المصدر |
| أدوار تستخدمها السياسات وليست ضمن ACT-01..15: Platform Operator، AI platform engineer، AI governance authority، integration engineer، Legal/Compliance authority، Privacy officer؛ وأدوار مكافأة لـACT بالتصنيف (dispatcher، carrier operator، Exercise Director/Controller، Evaluator، technician، collection manager… — §6.5) | **[Needs Review]** — تُضاف إلى `stakeholders.md` أو تُعرَّف كأدوار في AGG-ROLE |
| 26 أمرًا يذكر مصدرها أدوارًا لا يشمل أيٌّ منها فعل الأمر | محسومة في `17-security-design.md` §5، ومطبَّقة على السياسات وكتالوجات الأوامر (CR-77) |
| وصف «finance» في سياسة `QRY-AI-USAGE` | دور غير معرَّف (§2.5) **[Needs Review]** |

## 6. الكتالوج والمصفوفات

<!-- BEGIN GENERATED: build_analysis_design.py -->

### 6.1 كتالوج الفاعلين والأدوار

العدّ على 477 أمرًا حُسم فاعلها و133 استعلامًا؛ الأوامر الـ0 التي لم يُحسم فاعلها في §6.6. العملية تُحسب مرة لكل دور تنسب إليه، فمجموع الأعمدة أكبر من عدد العمليات.

#### (A) الفاعلون الأعمال (ACT-01..15 — `01-business/stakeholders.md`)

| الفاعل / الدور | الوصف | أوامر | استعلامات | السياقات |
|---|---|---|---|---|
| ACT-01 Executive — القيادي التنفيذي | القيادة (SH-01) | 2 | 1 | BC01 |
| ACT-02 Manager — المدير | القيادة (SH-01) | 40 | 4 | BC02, BC03, BC04, BC05, BC06 |
| ACT-03 Planner — المخطِّط | المستخدمون التشغيليون (SH-02) | 59 | 2 | BC02, BC04, BC05, BC06, BC07 |
| ACT-04 Analyst — المحلل | مستخدمو المعلومات والتحليل (SH-03) | 128 | 11 | BC02, BC03, BC04, BC06, BC07 |
| ACT-05 Operator — المشغِّل | المستخدمون التشغيليون (SH-02) | 3 | 0 | BC03 |
| ACT-06 Field User — المستخدم الميداني | المستخدمون التشغيليون (SH-02) | 6 | 2 | BC02, BC07 |
| ACT-07 Resource Manager — مدير الموارد | المستخدمون التشغيليون (SH-02) | 32 | 1 | BC05 |
| ACT-08 Logistics User — مستخدم الإمداد | المستخدمون التشغيليون (SH-02) | 9 | 0 | BC05 |
| ACT-09 Risk Manager — مدير المخاطر | المستخدمون التشغيليون (SH-02) | 1 | 1 | BC04 |
| ACT-10 Training Manager — مدير التدريب | المستخدمون التشغيليون (SH-02) | 23 | 1 | BC05 |
| ACT-11 Knowledge Manager — مدير المعرفة | مستخدمو المعلومات والتحليل (SH-03) | 7 | 0 | BC06 |
| ACT-12 Archivist — أمين الأرشيف | الحوكمة (SH-04) | 8 | 4 | BC06, BC08 |
| ACT-13 Security Officer — مسؤول الأمن | الحوكمة (SH-04) | 33 | 9 | BC01, BC02, BC03, BC04, BC05, BC06, BC07, BC08 |
| ACT-14 Auditor — المدقِّق | الحوكمة (SH-04) | 2 | 14 | BC03, BC06, BC07, BC08 |
| ACT-15 Administrator — مسؤول الإدارة | فرق المنصة (SH-05) | 59 | 10 | BC01, BC02, BC03, BC04, BC05, BC07 |

#### (B) أدوار المنصة

| الفاعل / الدور | الوصف | أوامر | استعلامات | السياقات |
|---|---|---|---|---|
| PLT-OPS — مشغّل المنصة | Platform Operator — فرق المنصة (SH-05) | 11 | 2 | BC01, BC07 |
| PLT-AI — مهندس/حوكمة الذكاء الاصطناعي | AI platform engineer، AI governance authority | 15 | 3 | BC07 |
| PLT-INT — مهندس التكامل | integration engineer | 8 | 2 | BC07 |

#### (C) أدوار السلطة والاعتماد

| الفاعل / الدور | الوصف | أوامر | استعلامات | السياقات |
|---|---|---|---|---|
| AUTH-LEGAL — السلطة القانونية والامتثال | Legal/Compliance authority، Privacy officer | 12 | 4 | BC06, BC08 |
| AUTH-GRANT — صاحب سلطة أو معتمِد ثانٍ | حامل منح سلطة في BC01 أو معتمِد ≠ المُعد (allocation/disposal/transfer/release authority، second approver…) | 23 | 2 | BC01, BC02, BC03, BC04, BC05, BC06, BC07 |

#### (D) أدوار العلاقة بالمورد (سمات للمورد يقيّمها قرار السياسة — ABAC عبر PIP، `08-security/authorization-model.md` §1–3)

| الفاعل / الدور | الوصف | أوامر | استعلامات | السياقات |
|---|---|---|---|---|
| REL-TASK — المنفّذ والمراجع | assignee، reviewer — دور يحدده المورد نفسه | 27 | 4 | BC02, BC03, BC04, BC05, BC06, BC07 |
| REL-OWNER — المالك والطالب والمشارك | owner، requester، custodian، participant، self | 39 | 15 | BC01, BC02, BC04, BC05, BC06, BC07 |
| REL-RECIPIENT — المستلم والمشترك | recipient، subscriber | 5 | 1 | BC03, BC04 |
| REL-INCIDENT — أدوار الحادثة | المُبلِّغ، مقيّم الحادثة، قائد الحادثة | 10 | 1 | BC04 |
| REL-RISK — أدوار الخطر | محدِّد الخطر، المقيّم، موافق المعالجة، مالك النطاق — أدوار منفصلة بفصل المهام (INV-RIS-01: المقيّم ≠ المحدِّد) | 4 | 1 | BC04 |
| REL-PEER — الشخص الثاني | second Analyst / Administrator، peer Analyst — لفصل المهام | 5 | 0 | BC02, BC03, BC07 |
| ANY-USER — أي مستخدم مخوَّل | أي مستخدم ضمن `allowed_scope` أو مصرَّح له بعلامة المورد | 10 | 74 | BC01, BC02, BC03, BC04, BC05, BC06, BC07, BC08 |

#### (E) الفاعلون النظاميون

| الفاعل / الدور | الوصف | أوامر | استعلامات | السياقات |
|---|---|---|---|---|
| SYS — هويات النظام والخدمات | adapter/SCIM service accounts، workload identities، analysis-run identity، internal PEPs | 35 | 6 | BC01, BC02, BC05, BC08 |

### 6.2 مصفوفة الفاعل × السياق (عدد الأوامر / الاستعلامات)

| الفاعل / الدور | BC01 | BC02 | BC03 | BC04 | BC05 | BC06 | BC07 | BC08 |
|---|---|---|---|---|---|---|---|---|
| ACT-01 Executive — القيادي التنفيذي | 2 / 1 | — | — | — | — | — | — | — |
| ACT-02 Manager — المدير | — | 3 / 1 | 12 / 0 | 22 / 0 | 0 / 3 | 3 / 0 | — | — |
| ACT-03 Planner — المخطِّط | — | 6 / 1 | — | 33 / 0 | 10 / 1 | 6 / 0 | 4 / 0 | — |
| ACT-04 Analyst — المحلل | — | 67 / 9 | 42 / 1 | 5 / 0 | — | 10 / 0 | 4 / 1 | — |
| ACT-05 Operator — المشغِّل | — | — | 3 / 0 | — | — | — | — | — |
| ACT-06 Field User — المستخدم الميداني | — | 1 / 0 | — | — | — | — | 5 / 2 | — |
| ACT-07 Resource Manager — مدير الموارد | — | — | — | — | 32 / 1 | — | — | — |
| ACT-08 Logistics User — مستخدم الإمداد | — | — | — | — | 9 / 0 | — | — | — |
| ACT-09 Risk Manager — مدير المخاطر | — | — | — | 1 / 1 | — | — | — | — |
| ACT-10 Training Manager — مدير التدريب | — | — | — | — | 23 / 1 | — | — | — |
| ACT-11 Knowledge Manager — مدير المعرفة | — | — | — | — | — | 7 / 0 | — | — |
| ACT-12 Archivist — أمين الأرشيف | — | — | — | — | — | 3 / 0 | — | 5 / 4 |
| ACT-13 Security Officer — مسؤول الأمن | 9 / 2 | 2 / 0 | 2 / 0 | 1 / 0 | 1 / 0 | 0 / 1 | 6 / 3 | 12 / 3 |
| ACT-14 Auditor — المدقِّق | — | — | 0 / 1 | — | — | 2 / 2 | 0 / 3 | 0 / 8 |
| ACT-15 Administrator — مسؤول الإدارة | 35 / 6 | 5 / 2 | 1 / 0 | 4 / 0 | 4 / 0 | — | 10 / 2 | — |
| PLT-OPS — مشغّل المنصة | 7 / 1 | — | — | — | — | — | 4 / 1 | — |
| PLT-AI — مهندس/حوكمة الذكاء الاصطناعي | — | — | — | — | — | — | 15 / 3 | — |
| PLT-INT — مهندس التكامل | — | — | — | — | — | — | 8 / 2 | — |
| AUTH-LEGAL — السلطة القانونية والامتثال | — | — | — | — | — | 2 / 0 | — | 10 / 4 |
| AUTH-GRANT — صاحب سلطة أو معتمِد ثانٍ | 5 / 1 | 1 / 0 | 2 / 1 | 6 / 0 | 5 / 0 | 2 / 0 | 2 / 0 | — |
| REL-TASK — المنفّذ والمراجع | — | 0 / 1 | 3 / 0 | 13 / 0 | 1 / 0 | 2 / 0 | 8 / 3 | — |
| REL-OWNER — المالك والطالب والمشارك | 0 / 5 | 9 / 1 | — | 23 / 1 | 1 / 3 | 2 / 2 | 4 / 3 | — |
| REL-RECIPIENT — المستلم والمشترك | — | — | 4 / 0 | 1 / 1 | — | — | — | — |
| REL-INCIDENT — أدوار الحادثة | — | — | — | 10 / 1 | — | — | — | — |
| REL-RISK — أدوار الخطر | — | — | — | 4 / 1 | — | — | — | — |
| REL-PEER — الشخص الثاني | — | 2 / 0 | 1 / 0 | — | — | — | 2 / 0 | — |
| ANY-USER — أي مستخدم مخوَّل | 3 / 1 | 0 / 14 | 0 / 15 | 0 / 17 | 0 / 16 | 4 / 6 | 2 / 4 | 1 / 1 |
| SYS — هويات النظام والخدمات | 8 / 1 | 26 / 2 | — | — | 1 / 1 | — | — | 0 / 2 |

### 6.3 مصفوفة الفاعل × نوع العملية

| الفاعل / الدور | إنشاء | تعديل | سير عمل | حذف / إنهاء | نظام | جلب |
|---|---|---|---|---|---|---|
| ACT-01 Executive — القيادي التنفيذي | — | — | 1 | 1 | — | 1 |
| ACT-02 Manager — المدير | 6 | 13 | 12 | 9 | — | 4 |
| ACT-03 Planner — المخطِّط | 11 | 18 | 13 | 17 | — | 2 |
| ACT-04 Analyst — المحلل | 26 | 34 | 38 | 30 | — | 11 |
| ACT-05 Operator — المشغِّل | 1 | — | 1 | 1 | — | — |
| ACT-06 Field User — المستخدم الميداني | 3 | — | 2 | 1 | — | 2 |
| ACT-07 Resource Manager — مدير الموارد | 6 | 6 | 12 | 8 | — | 1 |
| ACT-08 Logistics User — مستخدم الإمداد | 2 | 1 | 2 | 4 | — | — |
| ACT-09 Risk Manager — مدير المخاطر | — | — | — | 1 | — | 1 |
| ACT-10 Training Manager — مدير التدريب | 4 | 5 | 8 | 6 | — | 1 |
| ACT-11 Knowledge Manager — مدير المعرفة | 1 | 1 | 2 | 3 | — | — |
| ACT-12 Archivist — أمين الأرشيف | 1 | 2 | 3 | 2 | — | 4 |
| ACT-13 Security Officer — مسؤول الأمن | 3 | 9 | 13 | 8 | — | 9 |
| ACT-14 Auditor — المدقِّق | 1 | — | — | 1 | — | 14 |
| ACT-15 Administrator — مسؤول الإدارة | 10 | 14 | 20 | 15 | — | 10 |
| PLT-OPS — مشغّل المنصة | 2 | 1 | 6 | 2 | — | 2 |
| PLT-AI — مهندس/حوكمة الذكاء الاصطناعي | 4 | 2 | 6 | 3 | — | 3 |
| PLT-INT — مهندس التكامل | 2 | 1 | 4 | 1 | — | 2 |
| AUTH-LEGAL — السلطة القانونية والامتثال | 3 | 1 | 5 | 3 | — | 4 |
| AUTH-GRANT — صاحب سلطة أو معتمِد ثانٍ | 3 | — | 10 | 10 | — | 2 |
| REL-TASK — المنفّذ والمراجع | — | 4 | 15 | 8 | — | 4 |
| REL-OWNER — المالك والطالب والمشارك | 6 | 12 | 8 | 13 | — | 15 |
| REL-RECIPIENT — المستلم والمشترك | 1 | — | 1 | 3 | — | 1 |
| REL-INCIDENT — أدوار الحادثة | 1 | 3 | 4 | 2 | — | 1 |
| REL-RISK — أدوار الخطر | 1 | — | 3 | — | — | 1 |
| REL-PEER — الشخص الثاني | — | — | 4 | 1 | — | — |
| ANY-USER — أي مستخدم مخوَّل | 4 | 2 | 2 | 2 | — | 74 |
| SYS — هويات النظام والخدمات | 8 | 9 | 9 | 3 | 6 | 6 |

### 6.4 عمليات كل فاعل

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
- **BC06:** `CMD-KNO-RECORD-REUSE`, `CMD-PRD-CREATE`, `CMD-PRD-DISCARD`, `CMD-PRD-EDIT-NARRATIVE`, `CMD-PRD-GENERATE`, `CMD-PRD-SUBMIT`
- **BC07:** `CMD-SCF-ASSIGN`, `CMD-SCF-DISCARD`, `CMD-SCF-REAPPLY`, `CMD-SCF-RESOLVE-MANUALLY`

#### ACT-04 Analyst — المحلل

- **BC02:** `CMD-CLM-ASSERT`, `CMD-CLM-CORRECT`, `CMD-CLM-RECLASSIFY`, `CMD-CLM-RECORD-CHANGE`, `CMD-CLM-RETRACT`, `CMD-CNF-ACCEPT`, `CMD-CNF-ASSIGN`, `CMD-CNF-RAISE`, `CMD-CNF-REOPEN`, `CMD-CNF-RESOLVE`, `CMD-CNF-START-REVIEW`, `CMD-CRP-ACCEPT`, `CMD-CRP-PROPOSE`, `CMD-CRP-REJECT`, `CMD-CRP-START-REVIEW`, `CMD-CRQ-CANCEL`, `CMD-CRQ-DRAFT`, `CMD-CRQ-EDIT`, `CMD-CRQ-MARK-SATISFIED`, `CMD-CRQ-SUBMIT`, `CMD-CRR-DEFINE`, `CMD-CRR-EDIT`, `CMD-CRR-RETIRE`, `CMD-ENT-CHANGE-TYPE`, `CMD-ENT-RECLASSIFY`, `CMD-ENT-REGISTER`, `CMD-ENT-REINSTATE`, `CMD-ENT-RETIRE`, `CMD-ER-CONFIRM-MATCH`, `CMD-ER-DECIDE-MATCH`, `CMD-ER-DECIDE-NOT-MATCH`, `CMD-ER-PARK`, `CMD-ER-PROPOSE`, `CMD-ER-REQUEST-SPLIT`, `CMD-ER-RESUME`, `CMD-ER-SPLIT`, `CMD-ER-START-REVIEW`, `CMD-ER-WITHDRAW`, `CMD-EVD-RECLASSIFY`, `CMD-EVD-REGISTER`, `CMD-EVD-SEAL`, `CMD-EVD-UPDATE-LOCATOR`, `CMD-EVD-WITHDRAW`, `CMD-EVL-LINK`, `CMD-EVL-UNLINK`, `CMD-EXT-END`, `CMD-EXT-MAP`, `CMD-MRS-DRAFT`, `CMD-MRS-EDIT`, `CMD-OBS-RECLASSIFY`, `CMD-OBS-REJECT`, `CMD-OBS-VALIDATE`, `CMD-REL-RECLASSIFY`, `CMD-REL-REGISTER`, `CMD-REL-REINSTATE`, `CMD-REL-RETIRE`, `CMD-RWE-CHANGE-TYPE`, `CMD-RWE-RECLASSIFY`, `CMD-RWE-REGISTER`, `CMD-RWE-REINSTATE`, `CMD-RWE-RETIRE`, `CMD-SRC-RATE-RELIABILITY`, `CMD-SRC-REGISTER`, `CMD-SRC-REINSTATE`, `CMD-SRC-RETIRE`, `CMD-SRC-SUSPEND`, `CMD-SRC-UPDATE-PROFILE`, `QRY-CLUSTER-GET`, `QRY-CNF-GET`, `QRY-CNF-LIST`, `QRY-CRP-QUEUE`, `QRY-ER-GET`, `QRY-ER-QUEUE`, `QRY-EXT-RESOLVE`, `QRY-MRS-GET`, `QRY-SRC-GET`
- **BC03:** `CMD-ACS-ADD-ASSUMPTION`, `CMD-ACS-ADD-HYPOTHESIS`, `CMD-ACS-CANCEL`, `CMD-ACS-CLOSE`, `CMD-ACS-CREATE`, `CMD-ACS-DEFINE`, `CMD-ACS-DEFINE-SCENARIO`, `CMD-ACS-DESELECT-EVIDENCE`, `CMD-ACS-OPEN`, `CMD-ACS-REOPEN`, `CMD-ACS-RETIRE-ASSUMPTION`, `CMD-ACS-SELECT-EVIDENCE`, `CMD-ACS-UPDATE-HYPOTHESIS`, `CMD-AMT-DEPRECATE`, `CMD-AMT-REGISTER`, `CMD-AMT-RETIRE`, `CMD-ARL-ACTIVATE`, `CMD-ARL-DEFINE`, `CMD-ARL-DISABLE`, `CMD-ARL-EDIT`, `CMD-ARL-ENABLE`, `CMD-ARL-RETIRE`, `CMD-ASM-DISCARD`, `CMD-ASM-DRAFT`, `CMD-ASM-EDIT`, `CMD-ASM-PUBLISH`, `CMD-ASM-RETURN`, `CMD-ASM-SUBMIT`, `CMD-ASM-WITHDRAW`, `CMD-FND-ACCEPT`, `CMD-FND-EDIT`, `CMD-FND-RECORD`, `CMD-FND-WITHDRAW`, `CMD-RUN-CANCEL`, `CMD-RUN-REPRODUCE`, `CMD-RUN-SUBMIT`, `CMD-SIT-ACTIVATE`, `CMD-SIT-CLOSE`, `CMD-SIT-CREATE`, `CMD-SIT-EDIT-DEFINITION`, `CMD-SIT-PAUSE`, `CMD-SIT-RESUME`, `QRY-AMT-LIST`
- **BC04:** `CMD-DRQ-ADD-OPTION`, `CMD-DRQ-CITE`, `CMD-DRQ-CREATE`, `CMD-DRQ-OPEN`, `CMD-DRQ-WITHDRAW`
- **BC06:** `CMD-PRD-CREATE`, `CMD-PRD-DISCARD`, `CMD-PRD-EDIT-NARRATIVE`, `CMD-PRD-GENERATE`, `CMD-PRD-SUBMIT`, `CMD-PTM-DEFINE`, `CMD-PTM-EDIT`, `CMD-PTM-RETIRE`, `CMD-REC-CANCEL`, `CMD-REC-REQUEST`
- **BC07:** `CMD-SCF-ASSIGN`, `CMD-SCF-DISCARD`, `CMD-SCF-REAPPLY`, `CMD-SCF-RESOLVE-MANUALLY`, `QRY-SNS-LIST`

#### ACT-05 Operator — المشغِّل

- **BC03:** `CMD-CAP-CANCEL`, `CMD-CAP-PREPARE`, `CMD-CAP-RETRY`

#### ACT-06 Field User — المستخدم الميداني

- **BC02:** `CMD-EVD-REGISTER`
- **BC07:** `CMD-PKG-CONFIRM-DOWNLOAD`, `CMD-PKG-REQUEST`, `CMD-PKG-REVOKE`, `CMD-SYN-OPEN`, `CMD-SYN-UPLOAD-BATCH`, `QRY-PKG-GET`, `QRY-SYN-DELTA`

#### ACT-07 Resource Manager — مدير الموارد

- **BC05:** `CMD-ASG-ASSIGN`, `CMD-ASG-CANCEL`, `CMD-ASG-RETURN`, `CMD-AST-FAIL-MAINTENANCE`, `CMD-AST-MARK-UNSERVICEABLE`, `CMD-AST-RECOVER`, `CMD-AST-REGISTER`, `CMD-AST-REPORT-LOST`, `CMD-AST-RETURN-TO-SERVICE`, `CMD-AST-SET-CERTIFICATION`, `CMD-AST-START-MAINTENANCE`, `CMD-AST-TRANSFER-CUSTODY`, `CMD-AST-UPDATE-CONDITION`, `CMD-MNT-CANCEL`, `CMD-MNT-COMPLETE`, `CMD-MNT-PLAN`, `CMD-MNT-RESCHEDULE`, `CMD-MNT-START`, `CMD-QUAL-RECORD`, `CMD-QUAL-REINSTATE`, `CMD-QUAL-RENEW`, `CMD-QUAL-REVOKE`, `CMD-QUAL-SUSPEND`, `CMD-RPL-ADJUST-CAPACITY`, `CMD-RPL-CLOSE`, `CMD-RPL-CREATE`, `CMD-RPL-RESUME`, `CMD-RPL-SUSPEND`, `CMD-RSV-CANCEL`, `CMD-RSV-CONFIRM`, `CMD-RSV-HOLD`, `CMD-RSV-RELEASE`, `QRY-QUAL-LIST`

#### ACT-08 Logistics User — مستخدم الإمداد

- **BC05:** `CMD-LGR-DISPATCH`, `CMD-LGR-REQUEST`, `CMD-SHP-CANCEL`, `CMD-SHP-DELIVER`, `CMD-SHP-DEPART`, `CMD-SHP-PLAN`, `CMD-SHP-RECORD-CHECKPOINT`, `CMD-SHP-REPORT-DAMAGE`, `CMD-SHP-REPORT-LOST`

#### ACT-09 Risk Manager — مدير المخاطر

- **BC04:** `CMD-RIS-CLOSE`, `QRY-RIS-GET`

#### ACT-10 Training Manager — مدير التدريب

- **BC05:** `CMD-EXR-CANCEL`, `CMD-EXR-PLAN`, `CMD-EXR-SCHEDULE`, `CMD-EXR-START`, `CMD-QUAL-RECORD`, `CMD-QUAL-REINSTATE`, `CMD-QUAL-RENEW`, `CMD-QUAL-REVOKE`, `CMD-QUAL-SUSPEND`, `CMD-RRQ-ACTIVATE`, `CMD-RRQ-DEFINE`, `CMD-RRQ-EDIT`, `CMD-RRQ-RETIRE`, `CMD-SCN-ACTIVATE`, `CMD-SCN-DEFINE`, `CMD-SCN-EDIT`, `CMD-SCN-RETIRE`, `CMD-SIM-ABORT`, `CMD-SIM-COMPLETE`, `CMD-SIM-DELIVER-INJECT`, `CMD-SIM-PAUSE`, `CMD-SIM-RECORD-EVALUATION`, `CMD-SIM-RESUME`, `QRY-READINESS`

#### ACT-11 Knowledge Manager — مدير المعرفة

- **BC06:** `CMD-KNO-PUBLISH`, `CMD-KNO-REJECT`, `CMD-KNO-RETIRE`, `CMD-KNO-RETURN`, `CMD-PTM-DEFINE`, `CMD-PTM-EDIT`, `CMD-PTM-RETIRE`

#### ACT-12 Archivist — أمين الأرشيف

- **BC06:** `CMD-ARC-MIGRATE-FORMAT`, `CMD-ARC-REPAIR`, `CMD-ARC-RETRY-INGEST`
- **BC08:** `CMD-DSP-CANCEL`, `CMD-DSP-SUBMIT`, `CMD-RTS-DISCARD`, `CMD-RTS-DRAFT`, `CMD-RTS-EDIT`, `QRY-DSP-GET`, `QRY-LHD-CHECK`, `QRY-LHD-LIST`, `QRY-RTS-ACTIVE`

#### ACT-13 Security Officer — مسؤول الأمن

- **BC01:** `CMD-CLR-APPROVE`, `CMD-CLR-GRANT`, `CMD-CLR-MODIFY`, `CMD-CLR-REINSTATE`, `CMD-CLR-REVOKE`, `CMD-CLR-SUSPEND`, `CMD-DEV-RETIRE`, `CMD-USR-LOCK`, `CMD-USR-UNLOCK`, `QRY-CLR-GET`, `QRY-HRS-QUEUE`
- **BC02:** `CMD-SRC-RECLASSIFY`, `CMD-SRC-SET-PROTECTION`
- **BC03:** `CMD-ACS-RECLASSIFY`, `CMD-SIT-RECLASSIFY`
- **BC04:** `CMD-PLN-RECLASSIFY`
- **BC05:** `CMD-AST-RECLASSIFY`
- **BC06:** `QRY-DST-LOG`
- **BC07:** `CMD-CON-ACTIVATE`, `CMD-PKG-REVOKE`, `CMD-TOL-ACTIVATE`, `CMD-TOL-DISABLE`, `CMD-TOL-ENABLE`, `CMD-TOL-RETIRE`, `QRY-CON-LIST`, `QRY-RTG-ACTIVE`, `QRY-TOL-LIST`
- **BC08:** `CMD-CLS-ACTIVATE`, `CMD-CLS-DISCARD`, `CMD-CLS-DRAFT`, `CMD-CLS-EDIT`, `CMD-EXC-APPROVE`, `CMD-EXC-REJECT`, `CMD-EXC-REVOKE`, `CMD-POL-APPROVE`, `CMD-POL-DRAFT`, `CMD-POL-EDIT`, `CMD-POL-REJECT`, `CMD-POL-SUBMIT`, `QRY-AUD-SEARCH`, `QRY-EXC-LIST`, `QRY-POL-GET`

#### ACT-14 Auditor — المدقِّق

- **BC03:** `QRY-CAP-LIST`
- **BC06:** `CMD-REC-CANCEL`, `CMD-REC-REQUEST`, `QRY-DST-LOG`, `QRY-REC-REPORT`
- **BC07:** `QRY-AIR-CONTEXT`, `QRY-AIR-GET`, `QRY-MDL-LIST`
- **BC08:** `QRY-AUD-SEARCH`, `QRY-AUD-VERIFY`, `QRY-DSP-GET`, `QRY-ERS-GET`, `QRY-EXC-LIST`, `QRY-LHD-LIST`, `QRY-POL-GET`, `QRY-RTS-ACTIVE`

#### ACT-15 Administrator — مسؤول الإدارة

- **BC01:** `CMD-DEV-CONFIRM`, `CMD-DEV-REINSTATE`, `CMD-DEV-RETIRE`, `CMD-DEV-SUSPEND`, `CMD-HRS-APPROVE`, `CMD-HRS-REJECT`, `CMD-ORG-ADD-UNIT`, `CMD-ORG-CREATE`, `CMD-ORG-DEACTIVATE`, `CMD-ORG-DEACTIVATE-UNIT`, `CMD-ORG-MOVE-UNIT`, `CMD-ORG-REACTIVATE`, `CMD-ORG-RENAME`, `CMD-ORG-RENAME-UNIT`, `CMD-PER-DEACTIVATE`, `CMD-PER-ERASE`, `CMD-PER-REACTIVATE`, `CMD-PER-REGISTER`, `CMD-PER-UPDATE-DETAILS`, `CMD-RAS-ASSIGN`, `CMD-RAS-REVOKE`, `CMD-ROL-ACTIVATE`, `CMD-ROL-DEFINE`, `CMD-ROL-RETIRE`, `CMD-ROL-SET-PERMISSIONS`, `CMD-SVC-CLOSE`, `CMD-SVC-CREATE`, `CMD-SVC-DISABLE`, `CMD-SVC-ENABLE`, `CMD-SVC-ROTATE-CREDENTIAL`, `CMD-USR-CLOSE`, `CMD-USR-LINK-IDENTITY`, `CMD-USR-LINK-PERSON`, `CMD-USR-PROVISION`, `CMD-USR-UNLINK-IDENTITY`, `QRY-AUT-LIST`, `QRY-DEV-LIST`, `QRY-HRS-QUEUE`, `QRY-TEN-GET`, `QRY-USR-GET`, `QRY-USR-LIST`
- **BC02:** `CMD-IMP-ACCEPT-QUARANTINE`, `CMD-IMP-CANCEL`, `CMD-IMP-REPROCESS-QUARANTINE`, `CMD-IMP-SUBMIT`, `CMD-MRS-ACTIVATE`, `QRY-IMP-GET`, `QRY-MRS-GET`
- **BC03:** `CMD-AMT-ACTIVATE`
- **BC04:** `CMD-TTY-ACTIVATE`, `CMD-TTY-DEFINE`, `CMD-TTY-EDIT`, `CMD-TTY-RETIRE`
- **BC05:** `CMD-RRQ-ACTIVATE`, `CMD-RRQ-DEFINE`, `CMD-RRQ-EDIT`, `CMD-RRQ-RETIRE`
- **BC07:** `CMD-ADP-ACTIVATE`, `CMD-ADP-REGISTER`, `CMD-ADP-RESUME`, `CMD-ADP-RETIRE`, `CMD-ADP-SUSPEND`, `CMD-ADP-UPDATE-MAPPING`, `CMD-CON-RESUME`, `CMD-CON-RETIRE`, `CMD-CON-SUSPEND`, `CMD-PKG-REVOKE`, `QRY-ADP-GET`, `QRY-AI-USAGE`

#### PLT-OPS — مشغّل المنصة

- **BC01:** `CMD-TEN-PROVISION`, `CMD-TEN-REACTIVATE`, `CMD-TEN-RETRY-PROVISIONING`, `CMD-TEN-START-CELL-MIGRATION`, `CMD-TEN-START-DECOMMISSION`, `CMD-TEN-SUSPEND`, `CMD-TEN-UPDATE-QUOTAS`, `QRY-TEN-GET`
- **BC07:** `CMD-PRJ-CANCEL-BUILD`, `CMD-PRJ-CREATE-VERSION`, `CMD-PRJ-PROMOTE`, `CMD-PRJ-RETIRE`, `QRY-PRJ-STATUS`

#### PLT-AI — مهندس/حوكمة الذكاء الاصطناعي

- **BC07:** `CMD-EVS-DRAFT`, `CMD-EVS-EDIT`, `CMD-MDL-APPROVE`, `CMD-MDL-DEPRECATE`, `CMD-MDL-FAIL-EVALUATION`, `CMD-MDL-PROMOTE`, `CMD-MDL-REGISTER`, `CMD-MDL-REINSTATE`, `CMD-MDL-RETIRE`, `CMD-MDL-STAGE`, `CMD-MDL-START-EVALUATION`, `CMD-RTG-DISCARD`, `CMD-RTG-DRAFT`, `CMD-RTG-EDIT`, `CMD-TOL-REGISTER`, `QRY-MDL-LIST`, `QRY-RTG-ACTIVE`, `QRY-TOL-LIST`

#### PLT-INT — مهندس التكامل

- **BC07:** `CMD-CON-FAIL-TEST`, `CMD-CON-REGISTER`, `CMD-CON-TEST`, `CMD-SNS-ACTIVATE`, `CMD-SNS-PAUSE`, `CMD-SNS-REGISTER`, `CMD-SNS-RETIRE`, `CMD-SNS-SET-QUALITY-RULES`, `QRY-CON-LIST`, `QRY-SNS-LIST`

#### AUTH-LEGAL — السلطة القانونية والامتثال

- **BC06:** `CMD-REC-CANCEL`, `CMD-REC-REQUEST`
- **BC08:** `CMD-DSP-APPROVE`, `CMD-ERS-APPROVE`, `CMD-ERS-REGISTER`, `CMD-ERS-REJECT`, `CMD-LHD-APPROVE-RELEASE`, `CMD-LHD-CANCEL-RELEASE`, `CMD-LHD-EXTEND`, `CMD-LHD-PLACE`, `CMD-LHD-REQUEST-RELEASE`, `CMD-RTS-ACTIVATE`, `QRY-DSP-GET`, `QRY-ERS-GET`, `QRY-LHD-LIST`, `QRY-RTS-ACTIVE`

#### AUTH-GRANT — صاحب سلطة أو معتمِد ثانٍ

- **BC01:** `CMD-AUT-DELEGATE`, `CMD-AUT-GRANT`, `CMD-AUT-RESUME`, `CMD-AUT-REVOKE`, `CMD-AUT-SUSPEND`, `QRY-AUT-LIST`
- **BC02:** `CMD-CRR-ACTIVATE`
- **BC03:** `CMD-AMT-ACTIVATE`, `CMD-CAP-RELEASE`, `QRY-CAP-LIST`
- **BC04:** `CMD-DEC-ANNUL`, `CMD-DEC-RECORD`, `CMD-PLN-CANCEL`, `CMD-PLV-APPROVE`, `CMD-PLV-REJECT`, `CMD-PLV-RETURN`
- **BC05:** `CMD-ALC-APPROVE`, `CMD-ALC-PREEMPT`, `CMD-ALC-REJECT`, `CMD-AST-DISPOSE`, `CMD-LGR-CANCEL`
- **BC06:** `CMD-ARC-TRANSFER`, `CMD-PTM-ACTIVATE`
- **BC07:** `CMD-EVS-ACTIVATE`, `CMD-RTG-ACTIVATE`

#### REL-TASK — المنفّذ والمراجع

- **BC02:** `QRY-CRP-GET`
- **BC03:** `CMD-ASM-PUBLISH`, `CMD-ASM-RETURN`, `CMD-ASM-WITHDRAW`
- **BC04:** `CMD-TASK-ACCEPT`, `CMD-TASK-ADD-RESULT-ITEM`, `CMD-TASK-APPROVE`, `CMD-TASK-BLOCK`, `CMD-TASK-COMPLETE`, `CMD-TASK-DECLINE`, `CMD-TASK-ESCALATE`, `CMD-TASK-REJECT`, `CMD-TASK-RESUME`, `CMD-TASK-RETURN`, `CMD-TASK-START`, `CMD-TASK-START-REVIEW`, `CMD-TASK-SUBMIT`
- **BC05:** `CMD-ALC-RECORD-CONSUMPTION`
- **BC06:** `CMD-PRD-APPROVE`, `CMD-PRD-RETURN`
- **BC07:** `CMD-AIRS-ACCEPT`, `CMD-AIRS-ACCEPT-PARTIALLY`, `CMD-AIRS-REJECT`, `CMD-AIRS-START-REVIEW`, `CMD-SCF-ASSIGN`, `CMD-SCF-DISCARD`, `CMD-SCF-REAPPLY`, `CMD-SCF-RESOLVE-MANUALLY`, `QRY-AIRS-QUEUE`, `QRY-SCF-GET`, `QRY-SCF-LIST`

#### REL-OWNER — المالك والطالب والمشارك

- **BC01:** `QRY-AUT-CHECK`, `QRY-CLR-GET`, `QRY-DEV-LIST`, `QRY-SEC-CONTEXT`, `QRY-USR-GET`
- **BC02:** `CMD-ATT-COMPLETE-UPLOAD`, `CMD-ATT-ERASE`, `CMD-ATT-INITIATE-UPLOAD`, `CMD-CRQ-CANCEL`, `CMD-CRQ-DRAFT`, `CMD-CRQ-EDIT`, `CMD-CRQ-MARK-SATISFIED`, `CMD-CRQ-SUBMIT`, `CMD-EVD-TRANSFER-CUSTODY`, `QRY-CRQ-EVIDENCE`
- **BC04:** `CMD-CRD-ACTIVATE`, `CMD-CRD-ADD-PARTICIPANT`, `CMD-CRD-ASSIGN-RESPONSIBILITY`, `CMD-CRD-CANCEL`, `CMD-CRD-CLOSE`, `CMD-CRD-OPEN`, `CMD-CRD-REMOVE-PARTICIPANT`, `CMD-CRD-REQUEST-DECISION`, `CMD-CRD-UPDATE-RESPONSIBILITY`, `CMD-OUT-CORRECT`, `CMD-OUT-RECORD`, `CMD-PLN-CLOSE`, `CMD-PLN-COMPLETE`, `CMD-PLN-CREATE`, `CMD-PLN-RESUME`, `CMD-PLN-SUSPEND`, `CMD-SUB-PAUSE`, `CMD-SUB-RESUME`, `CMD-SUB-SUBSCRIBE`, `CMD-SUB-UNSUBSCRIBE`, `CMD-SUB-UPDATE-CHANNELS`, `CMD-TASK-CLOSE`, `CMD-TASK-ESCALATE`, `QRY-CRD-GET`
- **BC05:** `CMD-LGR-CANCEL`, `QRY-MNT-SCHEDULE`, `QRY-QUAL-LIST`, `QRY-READINESS`
- **BC06:** `CMD-DST-CANCEL`, `CMD-DST-DISTRIBUTE`, `QRY-DST-LOG`, `QRY-REC-REPORT`
- **BC07:** `CMD-SCF-ASSIGN`, `CMD-SCF-DISCARD`, `CMD-SCF-REAPPLY`, `CMD-SCF-RESOLVE-MANUALLY`, `QRY-AIR-CONTEXT`, `QRY-AIR-GET`, `QRY-PKG-GET`

#### REL-RECIPIENT — المستلم والمشترك

- **BC03:** `CMD-ALR-ACKNOWLEDGE`, `CMD-ALR-DISMISS`, `CMD-ALR-RESOLVE`, `CMD-CAP-PREPARE`
- **BC04:** `CMD-NTF-MARK-READ`, `QRY-NTF-INBOX`

#### REL-INCIDENT — أدوار الحادثة

- **BC04:** `CMD-INC-ACTIVATE-CONTINGENCY`, `CMD-INC-ASSESS`, `CMD-INC-CANCEL`, `CMD-INC-CLOSE`, `CMD-INC-CONTAIN`, `CMD-INC-DE-ESCALATE`, `CMD-INC-DISPATCH-RESPONSE`, `CMD-INC-ESCALATE`, `CMD-INC-REPORT`, `CMD-INC-RESOLVE`, `QRY-INC-RECOVERY-STATUS`

#### REL-RISK — أدوار الخطر

- **BC04:** `CMD-RIS-ASSESS`, `CMD-RIS-IDENTIFY`, `CMD-RIS-PLAN-TREATMENT`, `CMD-RIS-REASSESS`, `QRY-RIS-GET`

#### REL-PEER — الشخص الثاني

- **BC02:** `CMD-ER-CONFIRM-MATCH`, `CMD-ER-SPLIT`
- **BC03:** `CMD-FND-ACCEPT`
- **BC07:** `CMD-ADP-ACTIVATE`, `CMD-ADP-RESUME`

#### ANY-USER — أي مستخدم مخوَّل

- **BC01:** `CMD-DEV-ENROLL`, `CMD-DEV-REPORT-LOST`, `CMD-DEV-ROTATE-KEY`, `QRY-ORG-TREE`
- **BC02:** `QRY-ATT-DOWNLOAD`, `QRY-CLM-GET`, `QRY-CRQ-BOARD`, `QRY-CRQ-GET`, `QRY-ENT-CLAIMS`, `QRY-ENT-LIST`, `QRY-ENT-POSITIONS`, `QRY-ENT-RESOLVED`, `QRY-EVD-GET`, `QRY-LIN-TRACE`, `QRY-OBS-GET`, `QRY-OBS-LIST`, `QRY-REL-LIST`, `QRY-RWE-GET`
- **BC03:** `QRY-ACS-GET`, `QRY-ACS-LIST`, `QRY-ALR-LIST`, `QRY-ASM-GET`, `QRY-ASM-VERSIONS`, `QRY-BASE-TILE`, `QRY-FND-LIST`, `QRY-RUN-ARTIFACT`, `QRY-RUN-GET`, `QRY-SCN-COMPARE`, `QRY-SIT-CHANGES`, `QRY-SIT-COP`, `QRY-SIT-GET`, `QRY-SIT-LIST`, `QRY-SIT-TILE`
- **BC04:** `QRY-CRD-LIST`, `QRY-DEC-BASIS`, `QRY-DEC-GET`, `QRY-DRQ-GET`, `QRY-DRQ-LIST`, `QRY-INC-GET`, `QRY-INC-LIST`, `QRY-OUT-SERIES`, `QRY-PLN-GET`, `QRY-PLN-PROGRESS`, `QRY-PLV-DIFF`, `QRY-PLV-LIST`, `QRY-RIS-REGISTER`, `QRY-TASK-GET`, `QRY-TASK-HISTORY`, `QRY-TASK-LIST`, `QRY-TTY-GET`
- **BC05:** `QRY-ALC-LIST`, `QRY-AST-AVAILABILITY`, `QRY-AST-GET`, `QRY-EXR-GET`, `QRY-EXR-LIST`, `QRY-LGR-GET`, `QRY-LGR-LIST`, `QRY-POL-TIMELINE`, `QRY-SCN-GET`, `QRY-SCN-LIST`, `QRY-SHP-GET`, `QRY-SHP-LIST`, `QRY-SHP-TRACKING`, `QRY-SIM-GET`, `QRY-SIM-LIST`, `QRY-SIM-TIMELINE`
- **BC06:** `CMD-KNO-DISCARD`, `CMD-KNO-DRAFT`, `CMD-KNO-EDIT`, `CMD-KNO-SUBMIT`, `QRY-ARC-RETRIEVE`, `QRY-ARC-SEARCH`, `QRY-KNO-SEARCH`, `QRY-KNO-SUGGEST`, `QRY-PRD-GET`, `QRY-PRD-LIST`
- **BC07:** `CMD-AIR-CANCEL`, `CMD-AIR-SUBMIT`, `QRY-GRAPH-NEIGHBORHOOD`, `QRY-GRAPH-PATHS`, `QRY-SRCH-QUERY`, `QRY-SRCH-SUGGEST`
- **BC08:** `CMD-EXC-REQUEST`, `QRY-CLS-ACTIVE`

#### SYS — هويات النظام والخدمات

- **BC01:** `CMD-TEN-COMPLETE-CELL-MIGRATION`, `CMD-TEN-COMPLETE-DECOMMISSION`, `CMD-TEN-COMPLETE-PROVISIONING`, `CMD-TEN-FAIL-PROVISIONING`, `CMD-USR-DISABLE`, `CMD-USR-ENABLE`, `CMD-USR-PROVISION`, `CMD-USR-RECORD-FIRST-SIGN-IN`, `QRY-AUT-CHECK`
- **BC02:** `CMD-CLM-ASSERT`, `CMD-CLM-ASSESS`, `CMD-CLM-RECLASSIFY`, `CMD-ENT-CHANGE-TYPE`, `CMD-ENT-RECLASSIFY`, `CMD-ENT-REGISTER`, `CMD-ENT-REINSTATE`, `CMD-ENT-RETIRE`, `CMD-EXT-END`, `CMD-EXT-MAP`, `CMD-IMP-ACCEPT-QUARANTINE`, `CMD-IMP-CANCEL`, `CMD-IMP-REPROCESS-QUARANTINE`, `CMD-IMP-SUBMIT`, `CMD-OBS-AMEND`, `CMD-OBS-ATTACH-EVIDENCE`, `CMD-OBS-RECORD`, `CMD-REL-RECLASSIFY`, `CMD-REL-REGISTER`, `CMD-REL-REINSTATE`, `CMD-REL-RETIRE`, `CMD-RWE-CHANGE-TYPE`, `CMD-RWE-RECLASSIFY`, `CMD-RWE-REGISTER`, `CMD-RWE-REINSTATE`, `CMD-RWE-RETIRE`, `QRY-EXT-RESOLVE`, `QRY-IMP-GET`
- **BC05:** `CMD-SIM-START`, `QRY-ELIG-CHECK`
- **BC08:** `QRY-LHD-CHECK`, `QRY-PDP-DECIDE`

### 6.5 كل أوصاف الأدوار في السياسات وتصنيفها

يكشف هذا الجدول كل مكافأة يفترضها التصنيف (مثل dispatcher ← مستخدم الإمداد، Exercise Controller ← مدير التدريب) **[Derived]**. الوصف غير المصنَّف يظهر بـ«—».

| الوصف في المصدر | التصنيف |
|---|---|
| adapter owner | SYS |
| adapter service account | SYS |
| adapter service accounts | SYS |
| Administrator | ACT-15 |
| Administrator / MDM policy | ACT-15 |
| Administrator / Planner lead | ACT-03 · ACT-15 |
| Administrator / Security Officer | ACT-13 · ACT-15 |
| Administrator in scope | ACT-15 |
| Administrator with org scope ⊇ person's unit | ACT-15 |
| Administrator with org scope ⊇ target | ACT-15 |
| Administrator with scope ⊇ assignment scope | ACT-15 |
| Administrator with scope ⊇ user's units | ACT-15 |
| Administrator ≠ author | ACT-15 |
| AI governance | PLT-AI |
| AI governance authority | PLT-AI |
| AI platform engineer | PLT-AI |
| alert recipient / duty officer | ACT-05 · REL-RECIPIENT |
| allocation authority | AUTH-GRANT |
| Analysis lead | ACT-04 |
| analysis-run identity | SYS |
| Analyst | ACT-04 |
| Analyst / any requester | ACT-04 · REL-OWNER |
| Analyst / Manager | ACT-02 · ACT-04 |
| Analyst / Planner | ACT-03 · ACT-04 |
| Analyst / Planner / Manager | ACT-02 · ACT-03 · ACT-04 |
| Analyst and above | ACT-04 |
| Analyst lead | ACT-04 |
| Analyst lead / Manager | ACT-02 · ACT-04 |
| Analyst or verification re-evaluator system identity | SYS |
| any analyst | ACT-04 |
| any authorized user | ANY-USER |
| any user | ANY-USER |
| any user (self) | REL-OWNER |
| any user of tenant | ANY-USER |
| any user of tenant (view org structure) | ANY-USER |
| approver with plan-approval authority ≠ author | AUTH-GRANT |
| Archivist | ACT-12 |
| asset owner scope | REL-OWNER |
| assignee | REL-TASK |
| assignee, owner, Planner | ACT-03 · REL-TASK · REL-OWNER |
| Auditor | ACT-14 |
| Auditor (metadata) | ACT-14 |
| Auditor / Legal / Analyst | ACT-04 · ACT-14 · AUTH-LEGAL |
| authenticated user | ANY-USER |
| authority | AUTH-GRANT |
| authority holder | AUTH-GRANT |
| authorized by package label and purpose | ANY-USER |
| authorized on the owning evidence/observation | ANY-USER |
| carrier operator | ACT-08 |
| cleared for situation | ANY-USER |
| cleared for situation label | ANY-USER |
| collection manager | ACT-02 |
| collection managers | ACT-02 |
| collection planner | ACT-03 |
| custodian role | REL-OWNER |
| device + user of the session | ACT-06 |
| dispatcher | ACT-08 |
| disposal authority | AUTH-GRANT |
| distributor | REL-OWNER |
| Evaluator | ACT-10 |
| Executive | ACT-01 |
| Executive in scope | ACT-01 |
| Exercise Controller | ACT-10 |
| Exercise Director | ACT-10 |
| Exercise Director / Training Manager | ACT-10 |
| field device + user | ACT-06 |
| Field User | ACT-06 |
| field user | ACT-06 |
| Field User / Operator / Analyst / adapter service account | SYS |
| finance | — |
| higher authority | AUTH-GRANT |
| holder | AUTH-GRANT |
| holder of parent grant | AUTH-GRANT |
| holder of permission authority.grant in scope | AUTH-GRANT |
| integration engineer | PLT-INT |
| integration engineers | PLT-INT |
| internal BC04 (workload identity) | SYS |
| internal PEPs only (workload identity) | SYS |
| internal services (workload identity) | SYS |
| Knowledge Manager | ACT-11 |
| Knowledge Manager / Analysis lead | ACT-04 · ACT-11 |
| lead | REL-OWNER |
| lead organization Manager | ACT-02 · REL-OWNER |
| Legal | AUTH-LEGAL |
| Legal authority ≠ registrar | AUTH-LEGAL |
| Legal/Compliance authority | AUTH-LEGAL |
| logistics authority | AUTH-GRANT |
| Logistics Officer / Planner | ACT-03 · ACT-08 |
| Manager | ACT-02 |
| Manager / product owner | ACT-02 · REL-OWNER |
| Manager / Training Manager in scope | ACT-02 · ACT-10 |
| Manager/Resource Manager in scope | ACT-02 · ACT-07 |
| operator | ACT-05 |
| owner / Planner | ACT-03 · REL-OWNER |
| owner contexts (workload identity) | SYS |
| package owner device + user | ACT-06 · REL-OWNER |
| participant members | REL-OWNER |
| participants (scope-limited) | REL-OWNER |
| peer Analyst | ACT-04 · REL-PEER |
| Planner | ACT-03 |
| planner | ACT-03 |
| Planner / owner | ACT-03 · REL-OWNER |
| Planner / Resource Manager | ACT-03 · ACT-07 |
| planner scope | ACT-03 |
| Planner/Manager in scope | ACT-02 · ACT-03 |
| platform operator | PLT-OPS |
| Platform Operator (platform tenant) | PLT-OPS |
| Privacy officer / Legal | AUTH-LEGAL |
| receiving party | ACT-08 |
| recipient | REL-RECIPIENT |
| Records/Legal authority ≠ submitter | AUTH-LEGAL |
| release authority | AUTH-GRANT |
| requester | REL-OWNER |
| requester if cleared | REL-OWNER |
| Resource Manager | ACT-07 |
| Resource Manager / Planner | ACT-03 · ACT-07 |
| Resource Manager / technician | ACT-07 |
| Resource Manager / Training Manager | ACT-07 · ACT-10 |
| reviewer | REL-TASK |
| reviewer / Analysis lead | ACT-04 · REL-TASK |
| reviewer authorized on target | REL-TASK |
| reviewer authorized on the target | REL-TASK |
| reviewer cleared for all inputs | REL-TASK |
| reviewer or attestation role | REL-TASK |
| reviewer role in scope | REL-TASK |
| reviewer: task owner/Planner, Analyst for observations | ACT-03 · ACT-04 · REL-TASK · REL-OWNER |
| reviewers authorized on targets | REL-TASK |
| SCIM service account | SYS |
| second Administrator | ACT-15 · REL-PEER |
| second Analyst | ACT-04 · REL-PEER |
| second approver | AUTH-GRANT |
| second authority | AUTH-GRANT |
| second lead or Administrator | ACT-15 · AUTH-GRANT |
| Security Officer | ACT-13 |
| Security Officer (itself audited) | ACT-13 |
| Security Officer ≠ requester | ACT-13 |
| self | REL-OWNER |
| system | SYS |
| task assignee | REL-TASK |
| tenant Administrator of that tenant | ACT-15 |
| Training Manager | ACT-10 |
| Training Manager / Administrator | ACT-10 · ACT-15 |
| transfer authority | AUTH-GRANT |
| user | ANY-USER |
| user with write permission on the target object | REL-OWNER |
| workload identity: scheduler / provisioning saga | SYS |
| أي مُبلِّغ مخوَّل | REL-INCIDENT |
| القائد | REL-INCIDENT |
| قائد الحادثة | REL-INCIDENT |
| قائد الحادثة بسلطة صريحة | REL-INCIDENT |
| قائد الحادثة بسلطة صريحة لتفعيل الاستمرارية | REL-INCIDENT |
| مالك الاستمرارية | REL-INCIDENT |
| مالك النطاق | REL-RISK |
| محدِّد الخطر | REL-RISK |
| مدير المخاطر | ACT-09 |
| مستخدم مخوَّل (ضمن allowed_scope) | ANY-USER |
| مقيّم | REL-RISK |
| مقيّم الحادثة | REL-INCIDENT |
| موافق المعالجة مخوَّل | REL-RISK |

### 6.6 أوامر لم يُحسم فاعلها

موضوع السياسة يسرد أدوارًا بأفعالها ولا يشمل أيٌّ منها فعل الأمر؛ لا تُنسب هنا لأي دور، وقصصها معلَّمة **[Needs Review]** (تُحسم في `17-security-design.md`، المرحلة 4).

| الأمر | الأدوار المذكورة في السياسة |
|---|---|
| — | لا شيء: الأوامر الـ26 التي لم يحسمها المصدر محسومة في `17-security-design.md` §5 (CR-77) |

### 6.7 أوصاف لم تُصنَّف

| الوصف في المصدر | العمليات |
|---|---|
| finance | QRY-AI-USAGE |

<!-- END GENERATED: build_analysis_design.py -->
