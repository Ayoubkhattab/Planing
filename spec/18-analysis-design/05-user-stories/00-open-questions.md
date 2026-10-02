---
id: AD-05-OPEN-QUESTIONS
type: open-questions
title: "أسئلة مفتوحة وفجوات — قصص المستخدم والميزات"
status: DRAFT
version: "0.1"
phase: "Phase 3.8 — إعادة هيكلة الميزات والقصص (المرحلتان 1 و2)"
sources: [18-analysis-design/05-user-stories/00-index.md, 17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv, 02-requirements/requirements.md, 02-requirements/use-cases.md, 18-analysis-design/21-ui-design.md]
---

# أسئلة مفتوحة وفجوات

| البند | القيمة |
|---|---|
| المعرّف | AD-05-OPEN-QUESTIONS |
| الإصدار | 0.1 |
| الحالة | مسودة |

## 1. الغرض

يجمع هذا الملف شيئين:

1. **قرارات تحتاج تأكيد المالك:** حين تحتمل القصة أو الميزة أكثر من مكان، أو لا يحسم المصدر أمرها. ولكل قرار اقتراح يُطبَّق إن لم يعترض المالك.
2. **فجوات:** متطلبات أو حالات استخدام لا تقابلها اليوم أي قصة. تُكتب لها قصص في المرحلة 3.

**طريقة الإضافة:** سطر جديد بمعرّف تالٍ لا يُعاد استخدامه. وعند الحسم تتغير الحالة إلى «محسوم» ويُذكر القرار، ولا يُحذف السطر.

## 2. قرارات خريطة الميزات

| المعرّف | السؤال | الاقتراح المطبَّق | الحالة |
|---|---|---|---|
| OQ-US-001 | قصص مجموعة السياسات الثماني: في «إدارة سياسات الوصول» (CAP-01.04) أم في التصنيف والأمن (CAP-13.01)؟ متطلباتها تذكر الاثنين | CAP-01.04 `FEAT-ORG-ACCESS-POLICY`، لأنها سياسة الوصول نفسها (UC-086) | محسوم: اعتمد المالك الاقتراح (2026-10-02) |
| OQ-US-002 | تحديث حصص المستأجر ونقله بين الخلايا: مع دورة حياة المستأجر (CAP-01.01) أم مع تشغيل المنصة (CAP-14.03)؟ | CAP-14.03 `FEAT-PLT-TENANT-QUOTAS` و`FEAT-PLT-CELL-MIGRATION`، لأنها عمل تشغيلي للمنصة. ومتطلباتها REQ-FND-001 و003 و004 في CAP-01.01، وREQ-FND-018 وحده في CAP-14.03 | محسوم: اعتمد المالك الاقتراح (2026-10-02) |
| OQ-US-003 | ميزة الواجهة ثنائية اللغة والتقويم الهجري في CAP-14.01 لأن المتطلب REQ-PLT-010 منسوب إليها، مع أنها تخص كل الشاشات | تبقى في CAP-14.01 `FEAT-PLT-LOCALIZATION`، وكل قصة واجهة تشير إليها | محسوم: اعتمد المالك الاقتراح (2026-10-02) |
| OQ-US-004 | قصص الدليل: في الجمع الميداني (CAP-02.03) أم في الادعاءات والأدلة (CAP-03.02)؟ | CAP-02.03 كما تنسبها متطلباتها | محسوم: اعتمد المالك الاقتراح (2026-10-02) |
| OQ-US-005 | توجيه نماذج الذكاء الاصطناعي وأدواته: في المساعدة (CAP-12.01) أم في الحوكمة (CAP-12.04)؟ | CAP-12.01 كما تنسبها متطلباتها (REQ-AI-011، REQ-AI-013) | محسوم: اعتمد المالك الاقتراح (2026-10-02) |
| OQ-US-006 | الاحتفاظ والتجميد القانوني والإتلاف: في المعرفة (CAP-11.02) أم في الحوكمة (CAP-13)؟ | CAP-11.02 كما في خريطة القدرات | محسوم: اعتمد المالك الاقتراح (2026-10-02) |
| OQ-US-007 | النتائج التحليلية (تسجيل، تعديل، قبول، سحب، قائمة): في الثقة والأصل (CAP-03.07) أم في التقييم (CAP-04.03)؟ | CAP-04.03 `FEAT-ANL-FINDINGS`، لأنها تُسجَّل داخل حالة التحليل | محسوم: اعتمد المالك الاقتراح (2026-10-02) |
| OQ-US-008 | إعادة بناء الفهارس ونسخها: في إدارة المعلومات (CAP-03.01) أم في تشغيل المنصة (CAP-14)؟ | CAP-03.01 كما ينسبها متطلبها | محسوم: اعتمد المالك الاقتراح (2026-10-02) |
| OQ-US-009 | التصعيد اليدوي للمهمة: مع «مهامي» أم مع «متابعة المهام والتدخل»؟ ينفذه المسندة إليه أو المالك أو المخطط | «متابعة المهام والتدخل» `FEAT-OPS-TASK-CONTROL`. و«مهامي» فيها التصعيد التلقائي فقط | محسوم: اعتمد المالك الاقتراح (2026-10-02) |
| OQ-US-010 | استعلام استخدام الذكاء الاصطناعي وتكلفته: متطلبه في CAP-12.01، والشاشة (SCR-51) مع مراقبة النماذج | CAP-12.04 `FEAT-AI-MODEL-MONITOR` | محسوم: اعتمد المالك الاقتراح (2026-10-02) |
| OQ-US-011 | التنبيهات العامة الصادرة (رسائل CAP): في الاتصال (CAP-10.01) أم في الوعي بالموقف (CAP-05)؟ | CAP-10.01 كما ينسبها متطلبها (REQ-INT-003) | محسوم: اعتمد المالك الاقتراح (2026-10-02) |
| OQ-US-012 | ميزات صغيرة يمكن دمجها: «تعريف الأدوار» مع «إسناد الأدوار» (7 قصص معًا)، و«الاستخراج» مع «الترجمة» بالذكاء الاصطناعي | تبقى منفصلة لأن لكل منها هدفًا مستقلًا | محسوم: اعتمد المالك الاقتراح (2026-10-02) |

## 3. فجوات: متطلبات بلا قصص

| المعرّف | الفجوة | المرجع | الميزة التي تستقبلها |
|---|---|---|---|
| GAP-US-001 | لا قصة لتحديث عضوية الموقف تلقائيًا حين يتغير ما يطابق معاييره | REQ-SIT-002 | `FEAT-SIT-CHANGES` |
| GAP-US-002 | استعلامات «كما كانت في وقت سابق» موجودة (ادعاءات الكيان، صورته الموحدة، سجل المهمة)، لكن لا قصة ترتبط بحالة الاستخدام التي تجمعها | UC-096 | `FEAT-INF-TIME-HISTORY` |
| GAP-US-003 | لا قصص للتحقق من صحة الأشكال الجغرافية وأنظمة الإحداثيات | REQ-INF-028، REQ-INF-029 | `FEAT-INF-GEO-LOCATION` |
| GAP-US-004 | لا قصص لتوحيد كتابة الأسماء العربية للبحث والمطابقة | REQ-SRC-003، REQ-INF-031 | `FEAT-INF-ENTITY-REGISTRY` |
| GAP-US-005 | لا قصة لضبط خطوات اعتماد الخطة على مستوى المستأجر | REQ-OPS-014 | `FEAT-OPS-TASK-TYPES` |
| GAP-US-006 | لا قصص للعمل 72 ساعة دون اتصال وتشفير بيانات الجهاز | REQ-OFF-001، REQ-OFF-005 | `FEAT-COL-OFFLINE-WORK` |
| GAP-US-007 | لا قصص لاستيراد طبقات الخرائط وبيانات الطقس | REQ-INF-008، REQ-INF-009 | `FEAT-COL-GEO-WEATHER` |
| GAP-US-008 | لا قصص للتكامل مع أنظمة الموارد البشرية والمالية والوثائق | REQ-INT-001 | `FEAT-COL-ENTERPRISE-INT` |
| GAP-US-009 | لا قصة للتصدير بعلامة مائية من مكتبة المنتجات | REQ-PRD-005 | `FEAT-COM-PRODUCT-LIBRARY` |

## 4. فجوات في الشاشات

| المعرّف | الفجوة | الأثر |
|---|---|---|
| GAP-UI-001 | لا شاشة لإدارة الاشتراكات | قصص الاشتراك بلا واجهة |
| GAP-UI-002 | لا شاشة لقوالب المنتجات | قصص القوالب بلا واجهة |
| GAP-UI-003 | شاشة مجمعات الموارد (SCR-41) بلا استعلام لعرض مجمع واحد | تُضاف قصة جلب أو يُعدَّل وصف الشاشة |
| GAP-UI-004 | لا شاشة لقواعد الربط | `FEAT-ANL-CORRELATION-RULES` بلا واجهة |

## 5. فجوات في المواصفة: قصص `US-DOM-`

متطلبات تطلب سلوكًا لا يقابله أمر أو استعلام أو انتقال في المواصفة. لكل منها قصة `US-DOM-` معلَّمة **[Derived]**، وتحتاج تصحيحًا في المواصفة يضيف مصدرها. الجدول مولَّد من `feature_map.csv`.

<!-- BEGIN GENERATED: dom-gaps -->
| القصة | الميزة | الوصف | المصدر |
|---|---|---|---|
| `US-DOM-ADP-LIST` | `FEAT-COL-ADAPTERS` | عرض المحوّلات المسجلة وحالاتها | REQ-INF-005، SCR-65، UC-094،  [Derived] |
| `US-DOM-AI-PROMPT-TEMPLATE` | `FEAT-AI-ROUTING` | إدارة نسخ قوالب التعليمات | 03-domain/contexts/BC07/aggregates/AGG-AI-ROUTING.md INV-RTG-02، REQ-AI-001، UC-077،  [Derived] |
| `US-DOM-AI-THRESHOLD-CALIBRATE` | `FEAT-AI-EVAL-SUITES` | معايرة عتبات التأريض باعتماد موثق | 03-domain/contexts/BC07/grounded-ai-spec.md §4، RSK-027، REQ-AI-003،  [Derived] |
| `US-DOM-AI-TRANSLATION-EVIDENCE` | `FEAT-AI-TRANSLATION` | اعتماد الترجمة دليلًا بعد مراجعة بشرية | 10-ai/autonomy-matrix.md AI-OP-05، REQ-AI-005، US-BC07-AIRS-ACCEPT،  [Derived] |
| `US-DOM-AI-TRANSLATION-LINK` | `FEAT-AI-TRANSLATION` | حفظ الترجمة مرتبطة بأصلها | REQ-AI-007، 13-verification/acceptance/SLC-10/invariants-slc10.md،  [Derived] |
| `US-DOM-ALC-OVERRUN-FLAG` | `FEAT-RES-CONSUMPTION` | وسم الاستهلاك الزائد للمراجعة بدل رفضه | REQ-RES-010، UC-055،  [Derived] |
| `US-DOM-ANL-ASM-REVIEW-QUEUE` | `FEAT-ANL-ASSESSMENT-REVIEW` | تقييمات مقدَّمة تنتظر مراجعتي | REQ-ANL-005، UC-015، SCR-06،  [Derived] |
| `US-DOM-ANL-CRR-LIST` | `FEAT-ANL-CORRELATION-RULES` | عرض قواعد الربط وإصداراتها | REQ-FUS-001، UC-132، 00-open-questions.md §4،  [Derived] |
| `US-DOM-ANL-FND-WITHDRAW-FLAG` | `FEAT-ANL-FINDINGS` | تعليم التقييمات المستشهدة بنتيجة مسحوبة للمراجعة | analysis-reproducibility-spec.md §6، REQ-ANL-005،  [Derived] |
| `US-DOM-ANL-RUN-RETRY` | `FEAT-ANL-RUNS` | إعادة محاولة تشغيل تحليل فشل | REQ-ANL-004، analysis-reproducibility-spec.md §3،  [Derived] |
| `US-DOM-ARL-DRY-RUN` | `FEAT-SIT-ALERT-RULES` | تجربة قاعدة التنبيه على أحداث آخر يوم | THR-S06-05، REQ-SIT-004،  [Derived] |
| `US-DOM-AST-CERT-EXPIRY` | `FEAT-RES-ASSET-SERVICE` | الأصل منتهي الشهادة لا يُسند من لحظة الانتهاء | REQ-RES-003، BRL-007،  [Derived] |
| `US-DOM-AST-LIST` | `FEAT-RES-ASSET-REGISTRY` | البحث في سجل الأصول وتصفيته | REQ-RES-001، SCR-40، UC-050،  [Derived] |
| `US-DOM-DEC-LIST` | `FEAT-DEC-RECORD-BASIS` | سجل القرارات للمدير والمدقق | REQ-DEC-003، QAS-TRC-001، UC-032،  [Derived] |
| `US-DOM-DEC-MY-REQUESTS` | `FEAT-DEC-REQUESTS` | طلبات القرار التي أعددتها وحالتها | REQ-DEC-001، UC-030،  [Derived] |
| `US-DOM-GEO-TRACK-SUMMARY` | `FEAT-INF-GEO-LOCATION` | تلخيص المواقع عالية التردد في ادعاء موقع | spatial-model.md §4، REQ-INF-030،  [Derived] |
| `US-DOM-IMP-LIST` | `FEAT-COL-IMPORT` | عرض دفعات الاستيراد حسب المحوّل والحالة | REQ-INF-006، SCR-64، UC-094،  [Derived] |
| `US-DOM-KNO-REVIEW-QUEUE` | `FEAT-KNW-KNOWLEDGE-REVIEW` | عرض المعرفة المنتظرة للمراجعة | REQ-KNW-001، UC-061، SCR-06، 21-ui-design.md §4.1،  [Derived] |
| `US-DOM-LEGALHOLD-BLOCK-MODIFY` | `FEAT-KNW-LEGAL-HOLD` | منع تعديل السجلات المجمدة | REQ-GOV-007، UC-103، 03-domain/contexts/BC01/aggregates/AGG-PERSON.md،  [Derived] |
| `US-DOM-LGR-LABEL` | `FEAT-RES-SUPPLY-REQUEST` | اشتقاق تصنيف طلب الإمداد والشحنة | 17-security-design.md §10، REQ-GOV-002،  [Derived] |
| `US-DOM-MRS-EVALUATE` | `FEAT-INF-MATCH-RULES` | تشغيل تقييم قواعد المطابقة على مجموعة الاختبار | QAS-ER-001، QAS-ER-002، REQ-INF-032،  [Derived] |
| `US-DOM-NTF-QUIET-HOURS` | `FEAT-COM-NOTIFY-DELIVERY` | تأجيل الدفع في ساعات الهدوء عدا الحرج | situation-alerting-spec.md §6، REQ-COM-001،  [Derived] |
| `US-DOM-OPS-APPROVAL-STEPS-GET` | `FEAT-OPS-TASK-TYPES` | عرض خطوات الاعتماد السارية وإصداراتها | REQ-OPS-014، 00-open-questions.md §3،  [Derived] |
| `US-DOM-OPS-APPROVAL-STEPS-SET` | `FEAT-OPS-TASK-TYPES` | ضبط خطوات اعتماد الخطط للمستأجر | REQ-OPS-014، 00-open-questions.md §3، UC-034،  [Derived] |
| `US-DOM-OPS-OUTCOME-FROM-TASK` | `FEAT-OPS-OUTCOMES` | تسجيل قياس من نتيجة مهمة | decision-plan-spec.md §4، REQ-OPS-013،  [Derived] |
| `US-DOM-OPS-PLAN-LIST` | `FEAT-OPS-PLAN-AUTHORING` | قائمة الخطط المرئية حسب الحالة والنوع | REQ-OPS-001، UC-033، SCR-34،  [Derived] |
| `US-DOM-OPS-PLAN-MULTI-APPROVAL` | `FEAT-OPS-PLAN-APPROVAL` | خطوة اعتماد ثانية للخطة حسب إعداد المستأجر | REQ-OPS-014، UC-034، 00-open-questions.md §3،  [Derived] |
| `US-DOM-OPS-PLAN-TASK-SYNC` | `FEAT-OPS-PLAN-APPROVAL` | مزامنة مهام الخطة عند اعتماد نسخة | decision-plan-spec.md §3، REQ-OPS-003، QAS-PERF-021، THR-S08-06،  [Derived] |
| `US-DOM-OPS-TASK-DEP-ESCALATE` | `FEAT-OPS-TASK-CONTROL` | تصعيد المهام التابعة عند إلغاء سابقتها | task-lifecycle-rules.md §4، REQ-OPS-012،  [Derived] |
| `US-DOM-OPS-TASK-MULTI-REVIEW` | `FEAT-OPS-TASK-REVIEW` | خطوة مراجعة ثانية للمهمة حسب نوعها | REQ-OPS-014، UC-044، US-BC04-TTY-EDIT،  [Derived] |
| `US-DOM-OPS-TTY-LIST` | `FEAT-OPS-TASK-TYPES` | قائمة أنواع المهام النشطة | REQ-OPS-007، SCR-66، UC-040،  [Derived] |
| `US-DOM-PER-LIST` | `FEAT-ORG-PERSONS` | عرض سجل الأشخاص والبحث فيه | REQ-FND-006، UC-084، SCR-62،  [Derived] |
| `US-DOM-PKG-LIST` | `FEAT-COL-PRELOAD` | عرض حزم مستخدم أو جهاز للمسؤول | REQ-OFF-002، AGG-PRELOAD-PACKAGE، CMD-PKG-REVOKE،  [Derived] |
| `US-DOM-PKG-TENANT-LIMITS` | `FEAT-COL-PRELOAD` | ضبط حدود حزم التحميل للمستأجر | REQ-OFF-002، AGG-PRELOAD-PACKAGE، POL-OFFLINE-PRELOAD،  [Derived] |
| `US-DOM-POL-HISTORY` | `FEAT-ORG-ACCESS-POLICY` | عرض تاريخ نسخ السياسات وأزمنة سريانها | REQ-GOV-009، SCR-68،  [Derived] |
| `US-DOM-PRD-EXPORT` | `FEAT-COM-PRODUCT-LIBRARY` | تصدير نسخة شخصية بعلامة مائية | REQ-PRD-005، UC-112، 00-open-questions.md §3،  [Derived] |
| `US-DOM-PTM-LIST` | `FEAT-COM-PRODUCT-TEMPLATES` | عرض قوالب المنتجات ونسخها | REQ-PRD-001، 00-open-questions.md §4،  [Derived] |
| `US-DOM-QUAL-EXPIRY-NOTICE` | `FEAT-RES-QUALIFICATIONS` | تنبيه الفرد ومديره قبل انتهاء المؤهل | REQ-RDY-001، UC-102،  [Derived] |
| `US-DOM-ROL-LIST` | `FEAT-ORG-ROLES` | عرض الأدوار وصلاحياتها | REQ-FND-014، UC-086، SCR-62،  [Derived] |
| `US-DOM-RPL-GET` | `FEAT-RES-RESOURCE-POOLS` | عرض تفاصيل مجمع موارد واحد | SCR-41، 21-ui-design.md §14، REQ-RES-006،  [Derived] |
| `US-DOM-RPL-LIST` | `FEAT-RES-RESOURCE-POOLS` | قائمة مجمعات الموارد ضمن نطاقي | SCR-41، REQ-RES-006،  [Derived] |
| `US-DOM-RRQ-LIST` | `FEAT-RES-ROLE-REQUIREMENTS` | عرض متطلبات الأدوار ونسخها | SCR-42، REQ-RES-013،  [Derived] |
| `US-DOM-SIT-BUFFER-FOLLOW` | `FEAT-SIT-CHANGES` | تحريك منطقة الموقف مع الكيان المرجعي | REQ-SIT-001، situation-alerting-spec.md §2،  [Derived] |
| `US-DOM-SIT-MEMBERSHIP-RECOMPUTE` | `FEAT-SIT-CHANGES` | إعادة حساب العضوية بعد تعديل التعريف أو الاستئناف | REQ-SIT-002، situation-alerting-spec.md §2،  [Derived] |
| `US-DOM-SIT-MEMBERSHIP-UPDATE` | `FEAT-SIT-CHANGES` | تحديث أعضاء الموقف تلقائيًا عند تغير الكائنات | REQ-SIT-002، QAS-PERF-006، ADR-P07، situation-alerting-spec.md §2،  [Derived] |
| `US-DOM-SRC-LIST` | `FEAT-COL-SOURCES` | عرض سجل المصادر وتصفيته | REQ-INF-001، UC-004، SCR-22،  [Derived] |
| `US-DOM-SUB-LIST` | `FEAT-COM-SUBSCRIPTIONS` | عرض قائمة اشتراكاتي | UC-099، 00-open-questions.md §4،  [Derived] |
| `US-DOM-SVC-LIST` | `FEAT-ORG-SERVICE-ACCOUNTS` | عرض حسابات الخدمة وحالة بيانات اعتمادها | REQ-FND-006، SCR-62، SCR-65،  [Derived] |
| `US-DOM-TEN-LIST` | `FEAT-ORG-TENANT-LIFECYCLE` | عرض قائمة المستأجرين لمشغل المنصة | UC-080، 21-ui-design.md §4.6، SCR-60،  [Derived] |
| `US-DOM-TRX-LABEL` | `FEAT-RES-EXERCISE-PLANNING` | اشتقاق تصنيف السيناريو والتمرين والمحاكاة | 17-security-design.md §10، REQ-GOV-002،  [Derived] |
<!-- END GENERATED: dom-gaps -->

## 6. تعارضات وفجوات ظهرت عند كتابة القدرة 7

ظهرت عند كتابة قصص «التخطيط والتنفيذ». كتبت القصص ما تؤيده المصادر، وعلّمت الباقي **[Needs Review]** أو **[Derived]**. وكل سطر هنا يحتاج قرار المالك أو تصحيحًا في المواصفة.

### 6.1 تعارض بين المصادر

| المعرّف | التعارض | القصص | الحالة |
|---|---|---|---|
| OQ-US-013 | المتطلب REQ-OPS-005 يسمح للمؤلف باعتماد إصدار خطته إن سمحت سياسة المستأجر صراحة، وشرط الأمر وسياسته يرفضان دائمًا | `US-BC04-PLV-APPROVE` | مفتوح |
| OQ-US-014 | غياب صلاحية اعتماد الخطة مصنَّف تحت «فصل المهام»، ورسالته لا تناسب هذه الحالة | `US-BC04-PLV-APPROVE` | مفتوح |
| OQ-US-015 | بدء المراجعة يشترط أن يكون المراجع غير المسند إليه دون استثناء، بينما الاعتماد يقبل استثناء سياسة المستأجر (REQ-OPS-009) | `US-BC04-TASK-START-REVIEW` | مفتوح |
| OQ-US-016 | تعديل المهمة: السياسة تقول المخطط أو المدير، والشرط يقول المنشئ أو المخطط | `US-BC04-TASK-EDIT` | مفتوح |
| OQ-US-017 | تغيير موعد المهمة: الشرط يقول المخطط أو المالك، والسياسة لا تذكر المالك | `US-BC04-TASK-SET-DUE` | مفتوح |
| OQ-US-018 | الأهلية المشروطة تحتاج مشرفًا مؤهلًا يُسمّى في أمر الإسناد، والأمر بلا حقل للمشرف (eligibility-rules.md §3) | `US-BC04-TASK-ASSIGN`، `US-UI-SCR02-ASSIGNEE-PICKER` | مفتوح |
| OQ-US-019 | زمن الإسناد: QAS-PERF-017 يعطي 500 ms مع فحص الأهلية، و19-runtime-scenarios يعطي 300 ms (QAS-PERF-001) | `US-PLT-TASK-ASSIGN-ELIG` | مفتوح |
| OQ-US-020 | المهمة المعلّقة ترفض كل تغيير عدا الإلغاء ورفع التعليق، وأوامر المجدول «تتبع الثوابت نفسها». فهل لا تنتهي المهمة المعلّقة ولا تُستبدل ولا تُغلق تلقائيًا ولا تُصعَّد؟ | `US-BC04-S-TASK-02`، `-03`، `-04`، `-05` | مفتوح |
| OQ-US-021 | شاشة الإغلاق مذكورة بين النماذج ذات السبب الإلزامي (21-ui-design.md §6.1)، وأمر إغلاق المهمة يجعل الملاحظة اختيارية. واتبعت القصة العقد | `US-UI-SCR02-CONTROL-ACTIONS` | مفتوح |
| OQ-US-022 | قاعدة إخفاء المجموعات الأصغر من 5 تنطبق على إحصاءات المستوى T1، وملف المهمة يذكر `tier: T1` و`importance_tier: T2` معًا | `US-UI-SCR35-EXEC-SUMMARY` | مفتوح |
| OQ-US-023 | قبول المهمة يذكر رمز «ليس المسند إليه»، والسياسة تقصر الأمر على المسند إليه أصلًا، فيتداخل مع «غير مسموح» | `US-BC04-TASK-ACCEPT` | مفتوح |
| OQ-US-024 | أوامر الحجب والرفض والاستئناف والإلغاء والتعليق والإعادة تذكر رمزين لغياب السبب: «السبب مطلوب» والبيانات غير الصالحة. واستخدمت القصص رمز السبب وحده | أوامر المهمة والخطة | مفتوح |
| OQ-US-038 | إغلاق الخطة يشترط أن تكون متتبّعات نتائجها مغلقة، والمتتبّعات لا تُغلق إلا عند إغلاق الخطة أو إلغائها، وإكمال الخطة لا يغلقها. فالخطة المكتملة لا يمكن إغلاقها أبدًا | `US-BC04-PLN-CLOSE`، `US-BC04-S-OUTCOME-TRACKER-03` | مفتوح |
| OQ-US-039 | المراجعة على خطوتين غير موجودة في المواصفة، وإن أُضيفت فرفض أن يكون المراجع الثاني هو الأول يحتاج رمزًا ورسالة خاصين، فرسالة «فصل المهام» الحالية تخص المقدِّم أو الطالب | `US-DOM-OPS-TASK-MULTI-REVIEW` | مفتوح |

### 6.2 قواعد بلا رمز رفض أو بلا عقد

| المعرّف | الفجوة | القصص | الحالة |
|---|---|---|---|
| OQ-US-025 | إغلاق الخطة يشترط إغلاق متتبّعات النتائج، ولا رمز رفض لذلك | `US-BC04-PLN-CLOSE` | مفتوح |
| OQ-US-026 | إعادة تصنيف الخطة إلى مستوى أدنى من القرارات التي تنفذها، وإعادة تصنيف المهمة إلى مستوى أعلى من تصريح المسند إليه: لا رمز رفض، ولا آلية لفرض إعادة الإسناد | `US-BC04-PLN-RECLASSIFY`، `US-BC04-TASK-RECLASSIFY` | مفتوح |
| OQ-US-027 | فتح مسودة إصدار لخطة مغلقة أو ملغاة، وإسقاط المسودة من غير مؤلفها: لا رمز رفض | `US-BC04-PLV-DRAFT`، `US-BC04-PLV-DISCARD` | مفتوح |
| OQ-US-028 | رفع التعليق يتطلب سببًا ولا رمز «السبب مطلوب» له، فاستُخدمت رسالة الحقل | `US-BC04-TASK-UNSUSPEND` | مفتوح |
| OQ-US-029 | قائمة المهام: العقد يعرّف المؤشر وحجم الصفحة فقط، والمرشحات مذكورة في وصف الاستعلام وحده | `US-BC04-Q-TASK-LIST` | مفتوح |
| OQ-US-030 | سجل المهمة وسلسلة القياسات «كما كانت معروفة في وقت ما» بلا معامل وقت في العقد. وتوفر السجل وتفاصيل المهمة كاملة دون اتصال غير واضح، فالمزامنة تنزّل ملخص المهام فقط | `US-BC04-Q-TASK-HISTORY`، `US-BC04-Q-TASK-GET`، `US-BC04-Q-OUT-SERIES` | مفتوح |
| OQ-US-031 | عرض نوع المهمة يعيد الإصدار الحالي فقط، فلا يُقرأ الإصدار الأقدم الذي ثبّتته مهمة | `US-BC04-Q-TTY-GET` | مفتوح |
| OQ-US-032 | مسودة نوع مهمة لا تُوقف ولا تُحذف، فلا طريقة للتخلص من مسودة غير مستخدمة | `US-BC04-TTY-RETIRE` | مفتوح |
| OQ-US-033 | تصحيح القياس لا يفحص قابلية تحويل الوحدة، بخلاف تسجيله | `US-BC04-OUT-CORRECT` | مفتوح |
| OQ-US-034 | رفض نتيجة المهمة يتطلب مدخل «إنشاء مهمة متابعة»، ولا يحدد المصدر متى وكيف تُنشأ | `US-BC04-TASK-REJECT` | مفتوح |
| OQ-US-035 | محتوى بند القياس في نتيجة المهمة غير معرَّف، ولا يُعرف أيُسجَّل القياس عند التقديم أم عند الاعتماد | `US-DOM-OPS-OUTCOME-FROM-TASK` | مفتوح |
| OQ-US-036 | حقل الأفعال المتاحة (`allowed_actions`) ما زال مقترحًا (21-ui-design.md §6.3)، ومتى يُرفع تنبيه المراجعة عن الخطة غير محدد | `US-UI-SCR01-ACTIONS`، `US-UI-SCR02-CONTROL-ACTIONS`، `US-UI-SCR34-REVIEW-FLAG` | مفتوح |
| OQ-US-037 | حالات الاستخدام UC-033 وUC-034 وUC-036 وUC-046 مذكورة بالاسم فقط، وفاعلوها وتدفقها «TBD». كُتبت قصصها من الكيانات والسياسات | قصص الخطة والتصعيد | مفتوح |

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | 2026-10-02 | المسودة الأولى: 12 قرارًا من بناء خريطة الميزات، و9 فجوات في القصص، و4 في الشاشات |
| 0.2 | 2026-10-02 | حسم القرارات الاثني عشر باعتماد المالك للخريطة؛ قسم مولَّد لفجوات المواصفة (قصص `US-DOM-`) |
| 0.3 | 2026-10-02 | 25 تعارضًا وفجوة ظهرت عند كتابة القدرة 7 (OQ-US-013 إلى 037) |
| 0.4 | 2026-10-03 | OQ-US-038 وOQ-US-039 وتوسيع OQ-US-030 (من المراجعة المستقلة) |
