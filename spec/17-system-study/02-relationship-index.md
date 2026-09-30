---
id: SYS-STUDY-RELATIONSHIP-INDEX
type: relationship-index
title: Phase 2 — Typed Relationship Index
status: DRAFT
generated_by: Claude (Dynamic Engineering System Reconstruction, Phase 2)
generated_at: '2026-09-29'
notes: >
  This file does NOT duplicate the raw co-reference graph — that graph already
  exists as the defined_in / ext_ref_count / ext_files columns in
  01-entity-index.md, and re-deriving it here would create a second source of
  truth for the same data. This file is for the layer 01-entity-index.md
  cannot express: TYPED, directional, semantically-judged relationships
  (depends_on, enables, mitigates, triggers, ...), which require reading and
  understanding content, not just grep. It grows incrementally during Phase 3
  (one BC at a time) rather than being generated in one pass. Exception: §21
  (Phase 3.6) holds the full per-aggregate chains built from explicit table
  columns and front-matter by _build/build_relationships.py; regenerate it,
  never edit it by hand.
---

# Phase 2 — Typed Relationship Index

## 1. الفرق بين هذا الملف و`01-entity-index.md`

| | `01-entity-index.md` | `02-relationship-index.md` (هذا الملف) |
|---|---|---|
| **كيف يُبنى** | آليًا بالكامل (regex عبر 705 ملف) | يدويًا/تدريجيًا أثناء التعمّق في كل BC |
| **يجيب** | أين عُرِّف X؟ من يذكر X؟ (كم مرة) | **ما نوع** العلاقة بين X وY، ولماذا؟ |
| **مثال** | `QRY-AUT-CHECK` → مذكور في 8 ملفات | `QRY-AUT-CHECK` **--mitigates-->** `THR-S01-03` |
| **تصنيف المعرفة** | Explicit فقط (مطابقة نص حرفية) | Explicit / Derived / Inferred (يحتاج حكمًا) |

**القاعدة العملية:** إذا كان السؤال "أين يظهر هذا المعرّف؟" → الجواب في `01-entity-index.md` عمود `ext_files`. إذا كان السؤال "لماذا هذان العنصران مرتبطان، وبأي اتجاه؟" → الجواب هنا.

## 2. قاموس أنواع العلاقات (يُستخدم كمرجع موحّد لكل BC لاحقًا)

`depends_on` · `enables` · `feeds` · `consumes` · `produces` · `triggers` · `authorizes` · `constrains` · `mitigates` · `controls` (SoD) · `validates` · `extends` · `related_to` · `duplicate_of` · `similar_to` (غير مؤكد الدمج) · `contains` · `belongs_to`

كل علاقة جديدة يكتشفها أي BC تُضاف هنا فور اكتشافها، مع الإشارة إليها كنوع جديد إن لم تكن في القائمة (Dynamic Discovery Rule).

## 3. علاقات مؤكدة حتى الآن (Seed — من عمل BC01 السابق)

هذه العلاقات استُخرجت فعليًا (وليست افتراضية) أثناء التوسعة العميقة لميزتي Authority Grant وClearance، قبل بدء Phase 2 رسميًا. أُدرجها هنا كنقطة بداية لأنها Explicit ومُتحقَّق منها بالفعل:

| From | Relationship | To | النوع | Evidence |
|---|---|---|---|---|
| CAP-01.03 | `contains` | UC-082, UC-083 | Explicit | capabilities.md, use-cases.md |
| UC-082 / UC-083 | `realizes` | AGG-AUTHORITY-GRANT | Derived | لا سرد UC صريح، مُشتق من جدول الانتقالات |
| CMD-AUT-DELEGATE | `constrains_by` | INV-AUT-01, INV-AUT-02, INV-AUT-03 | Explicit | AGG-AUTHORITY-GRANT.md |
| QRY-AUT-CHECK | `mitigates` | THR-S01-03 (Delegation chain amplifies authority) | Explicit | threat-model-slc01.md |
| CMD-CLR-APPROVE | `controls` (Segregation of Duties) | — | Explicit | policies-slc01.md#POL-CLR-APPROVE |
| INV-CLR-02/03 | `mitigates` | THR-S01-04 (Security Officer grants own/colluding clearance) | Explicit | threat-model-slc01.md |
| AGG-AUTHORITY-GRANT | `feeds` | BRL-003 (business decision requires authority) | Explicit | business-rules.md |
| BRL-003 | `enables` | CAP-06 (إدارة القرار) | Derived | ربط منطقي، لا رابط مباشر بملف واحد |
| AGG-CLEARANCE | `depends_on` | AGG-CLASSIFICATION-SCHEME (BC08) | Explicit | "level and compartments exist in ACTIVE scheme" — AGG-CLEARANCE.md guard |
| UC-089 (جديدة، CR-64) | `realizes` | AGG-CLEARANCE (جانب المستخدم) | Explicit (بعد التصحيح) | CR-64 |
| UC-085 | `realizes` | AGG-CLASSIFICATION-SCHEME (جانب الكائن/المخطط) | Explicit | traces.satisfies |
| AGG-AUTHORITY-GRANT | `similar_to` (ليست duplicate) | AGG-CLEARANCE | Derived | نفس نمط state machine، أبعاد مختلفة تمامًا (من يقرر vs من يرى) |

## 4. اكتشاف عابر للـBC ظهر أثناء Phase 2 الآلي (يحتاج تصنيف علاقة رسمي في Phase 3)

من `03-data-quality.md` §3: ست فئات بيانات مرجعية (`RD-HAZARD-CATEGORIES`, `RD-LOGISTICS-ITEM-TYPES`, `RD-ASSET-TYPES`, `RD-RESOURCE-TYPES`, `RD-EXERCISE-TYPES`, `RD-CONDITION-GRADES`) **يعتمد عليها BC04/BC05 صراحة** (`depends_on` من عدة aggregates) لكنها **غير معرَّفة فعليًا** في `04-information/reference-data.md` (المصدر المفترض لكل RD-*). هذه علاقة `depends_on` حقيقية لكن **طرفها الثاني مفقود [Missing]** — ستُسجَّل رسميًا في `conflicts.md` عند الوصول لـBC04/BC05 في Phase 3، لا هنا.

## 5. BC01 — علاقات إضافية مؤكَّدة (اكتمال Phase 3 لـBC01)

| From | Relationship | To | Evidence |
|---|---|---|---|
| AGG-TENANT (decommission) | `depends_on` | BC08 (legal hold query) | AGG-TENANT.md guard |
| UC-085 (Manage Classification Scheme) | `realizes` | BC08 (AGG-CLASSIFICATION-SCHEME) | تأكيد سابق |
| UC-086 (Manage Access Policy) | `realizes` | BC08 (AGG-POLICY-SET) | تحقّق مباشر من وجود الملف في BC08 |
| UC-088 (Request & Approve Security Exception) | `realizes` | BC08 (AGG-SECURITY-EXCEPTION) | تحقّق مباشر من وجود الملف في BC08 |
| AGG-ROLE-ASSIGNMENT | `enables` | BC04 (SoD لاعتماد الخطة/المهمة، REQ-OPS-005/009) | traces.satisfies + REQ statements |
| AGG-HR-SYNC-PROPOSAL | `mitigates` | THR-S01-01 (SCIM يمنح أدوارًا مباشرة) | AGG-HR-SYNC-PROPOSAL.md + threat-model-slc01.md |
| QRY-AUT-CHECK | `mitigates` | THR-S01-03 (تسلسل تفويض يضخّم السلطة) | مؤكَّد سابقًا |
| INV-CLR-02/03 | `mitigates` | THR-S01-04 (تواطؤ ضباط أمن) | threat-model-slc01.md |

**نمط مكتشَف عابر لأكثر من علاقة واحدة:** ثلاث حالات استخدام على الأقل في نطاق UC-080..089 (UC-085, UC-086, UC-088) تُنفَّذ فعليًا عبر BC08 لا BC01، رغم ظهورها في نفس الكتالوج المتقاطع. هذا يستدعي عند بدء دراسة BC08 التحقق من وجود ازدواجية أو تكامل حقيقي مع ما وثّقناه هنا.

## 7. BC02 — اكتشاف مهم يُعيد فتح CONFLICT-01/OQ-034 بنطاق أوسع

أثناء دراسة BC02، وُجد أن **7 من 18 aggregate** (ENTITY, RELATIONSHIP, REALWORLD-EVENT, CLAIM, EVIDENCE, OBSERVATION, SOURCE) تحمل جميعًا أمر `CMD-*-RECLASSIFY` بنفس الحارس الحرفي: *"authority per tenant policy (**REQ-GOV-004**); new version; bumps object security_version"*.

**الأثر:** REQ-GOV-004 ليست مسؤولية aggregate أو BC واحد (كما افترضنا في CONFLICT-01 الأصلي بين BC01/BC08) — بل **نمط أمر مُكرَّر عبر عشرات الـaggregates في كل الـBCs على الأرجح**. هذا يعني:
- `use_cases` الصحيح لـREQ-GOV-004 في requirements.md قد يحتاج إعادة صياغة جذرية: ليس UC-085 أو UC-089 فقط، بل **كل واجهة "إعادة تصنيف" عبر كل الـBCs**.
- هذا **يوسّع نطاق OQ-034/CR-64** إلى ما هو أبعد من BC01 — القرار البشري النهائي بشأنها يجب أن يُؤجَّل حتى تُفحص بقية الـBCs (BC03..BC08) ويُعرف حجم النمط الكامل.

**لم أُعدِّل CR-64/OQ-034 بهذا بعد** — أسجّله هنا أولًا لأن القرار يمسّ نطاقًا يتجاوز صلاحية "قرار بشأن ميزة واحدة"؛ يحتاج تجميع الأدلة من كل الـBCs أولًا (Source Closure الحقيقي لهذه المسألة تحديدًا).

## 9. BC03 — اكتملت من أول جولة (بلا اكتشافات جديدة تمس CONFLICT-01)

BC03 (الوعي بالموقف + التحليل، 9 aggregates) أُغلقت هيكليًا وأمنيًا في جولة واحدة بتطبيق درس §7/§10 (فصل الشريحة عن BC). لا أوامر RECLASSIFY بنمط REQ-GOV-004 المكتشف في BC02 ظهرت هنا بنفس الكثافة (AGG-SITUATION فقط يحمل CMD-SIT-RECLASSIFY، وAGG-ANALYSIS-CASE يحمل CMD-ACS-RECLASSIFY) — يُضاف إلى قائمة الأدلة المتراكمة لصالح فرضية "RECLASSIFY نمط عابر لكل BC" دون تغيير القرار المعلَّق.

## 11. BC04 — اكتملت، مع تصحيح رجعي على BC03

BC04 (12 aggregate: Decision/Plan/Task/Risk/Incident/Coordination/Notification/Subscription، أكبر BC حتى الآن) اكتملت هيكليًا وأمنيًا. **اكتشاف أثناء هذه الجولة أدّى لتصحيح `bc03-situational-awareness.md` رجعيًا:** THR-S06-02 وTHR-S06-07 (ملف "threat-model-slc06.md") تخصان AGG-NOTIFICATION/AGG-SUBSCRIPTION (BC04) لا BC03 كما نُسِب أول مرة — نفس نمط AGG-ADAPTER (BC02→BC07) وTHR-S15-01/02 (BC02→BC04، مُؤكَّد نهائيًا هنا). أيضًا BRL-003 (لا قرار بلا سلطة) ظهرت مطبَّقة **حرفيًا مرتين**: AGG-DECISION (بين الأفراد) وAGG-COORDINATION-CASE (بين المنظمات) — نفس القاعدة التجارية، تطبيقان هندسيان مستقلان.

**تأكيد إضافي على فجوة RD-HAZARD-CATEGORIES:** AGG-RISK وAGG-INCIDENT كلاهما يستشهد بها كحارس إلزامي مباشر — من المصدر، لا استنتاجًا.

## 13. BC05 — اكتملت (بلا تصحيحات رجعية)

BC05 (13 aggregate: Asset/Allocation/Logistics/Shipment/Exercise/Simulation...) اكتملت. **تأكيد رابع متراكم لفجوة RD-*** — BC05 وحدها استشهدت بـ5 من 6 فئات مرجعية مفقودة من Phase 2. **نمط CR-62 (الإنشاء المرتبط بنفس المعاملة) مؤكَّد الآن كـنمط تصميم متكرر عمدًا** (3 حالات: Logistics→Allocation، Logistics→Shipment، Exercise→Simulation) لا حالة استثنائية واحدة.

## 15. BC06 — اكتملت (اعتماد معلَّق واحد على BC08)

BC06 (6 aggregates: Product/Template/Distribution/Knowledge-Object/Archive/Reconstruction، شريحة SLC-12 واحدة). **نمط "الإفصاح الصفري" (لا كشف لوجود شيء محجوب) مؤكَّد للمرة الرابعة** عبر BCs مختلفة (BC01 PB-01، BC03 INV-ALR-02، BC06 INV-DST-01/INV-REC-03) — مبدأ تصميمي مركزي للمنصة كلها. اعتماد صريح غير محلول: `AGG-ARCHIVE-PACKAGE` على "SLC-12a" (يُرجَّح BC08) — يُترَك معلَّقًا حتى BC08.

## 17. BC07 — اكتملت (أكبر BC من حيث الشرائح؛ تصحيحان رجعيان)

BC07 (13 aggregate: Adapter/Connection/Sensor/AI-*/Projection/Sync-*/Preload، 5 شرائح) اكتملت. **حسمت توزيع SLC-16 نهائيًا** بعد أن كان جزئيًا: BC01(1: HRIS) + BC03(1: Outbound CAP) + BC07(3: DMS/Connections/Sensors) = 5/5. **صححت رجعيًا `bc01-foundation.md`** (أضافت THR-S16-02 المفقود لـAGG-HR-SYNC-PROPOSAL). Platform Baselines أصبحت مكتملة: **PB-01..14** (01-07 BC01، 08-11 BC02، 12-14 BC07/AI). اكتُشف مبدأ أمني جديد خاص بالـLLM: "البيانات المسترجَعة لا يمكنها رفع الصلاحية أو توسيع النطاق أبدًا" (INV-AIR-02) — دفاع مباشر ضد Prompt Injection.

## 19. BC08 — اكتملت (آخر BC في Phase 3؛ يُغلق CONFLICT-01/OQ-034 نهائيًا)

BC08 (7 aggregates: Classification-Scheme/Policy-Set/Security-Exception (SLC-01، مشتركة مع BC01) + Retention-Schedule/Legal-Hold/Disposition-Run/Erasure-Request (SLC-12a، خالصة)) اكتملت.

**تصحيح رجعي ثانٍ على BC01 (بعد THR-S16-02 في §17):** `THR-S01-05` (Policy set) و`THR-S01-06` (Security exception) في `threat-model-slc01.md` تخصان BC08 لا BC01 — نفس نمط "الشريحة ≠ BC" يتكرر للمرة الثالثة (بعد AGG-ADAPTER §10 وTHR-S06 §11). صُحِّح `bc01-foundation.md` (13→11 تهديدًا لـBC01؛ 71→58 سياسة أمر). كذلك 6 من 14 query_policies في `policies-slc01.md` تخص BC08.

**إغلاق CONFLICT-01/OQ-034/CR-64 نهائيًا عبر CR-65:** `AGG-CLASSIFICATION-SCHEME.md` لم يكن يُعلن `REQ-GOV-004` في `traces.satisfies` رغم أن `INV-CLS-04` هو آلية إنفاذه على مستوى المخطط. أُضيف الآن (CR-65). REQ-GOV-004 له الآن **ثلاث نقاط إنفاذ موثَّقة صراحة**: AGG-CLASSIFICATION-SCHEME (مستوى المخطط)، نمط CMD-*-RECLASSIFY عبر BC02+ (مستوى الكائن، §7)، AGG-CLEARANCE (مستوى تصريح المستخدم، BC01، CR-64). اكتشاف §7 حول "نطاق REQ-GOV-004 عبر كل الـBCs" يبقى موثَّقًا كملاحظة توسّع نمطي مشروعة، لكنه لم يعد يمنع إغلاق CONFLICT-01 نفسها — الثلاث نقاط الموثَّقة تغطي كل الزوايا التي أثارها النزاع الأصلي (كائن BC08 × مستخدم BC01).

**إغلاق اعتماد BC06→SLC-12a:** مؤكَّد أن `AGG-ARCHIVE-PACKAGE.CMD-ARC-DISPOSE` يعتمد على `AGG-DISPOSITION-RUN` (BC08) عبر آلية تدمير المفتاح المشتركة (ADR-P08, CR-51) — رابط ضمني [Derived]، لا رابط صريح بين ملفي الـaggregate. صُحِّح `bc06-knowledge-products.md` (§4.3/§7/§8: CLOSED جزئيًا → CLOSED).

**اكتشاف جديد:** BC08 يحمل أعلى كثافة قيود SoD في كل الدراسة (كل أمر تغييري تقريبًا يحمل قيد فصل مهام صريح) — منطقي بصفته "الحارس الأخير" لعمليات لا رجعة فيها (إتلاف، محو، تجميد قانوني). Crypto-shredding (تدمير مفتاح لا صف) هو الآلية الموحَّدة عبر AGG-DISPOSITION-RUN وAGG-ERASURE-REQUEST معًا.

## 20. حالة هذا الملف

`CLOSED (Phase 3.6)` — **الطبقتان مكتملتان:**

- **§3–§19 (يدوية):** العلاقات المصنَّفة التي تحتاج حكمًا (`mitigates`، `controls`، `similar_to`...) واكتشافات كل BC بالترتيب الزمني. كل التصحيحات الرجعية مُطبَّقة وموثَّقة (BC01 ×2، BC03 ×1، BC06 ×1). CONFLICT-01/OQ-034 مُغلَق نهائيًا (CR-65).
- **§21 (مولَّدة آليًا، Phase 3.6):** السلسلة الكاملة CAP → UC → REQ → AGG → CMD → EVT → المستهلكون، مع INV وADR وQRY وTHR واختبار القبول، لكل Aggregate من الـ89. تُعاد بتشغيل `python3 spec/17-system-study/_build/build_relationships.py` بعد أي تعديل في المصادر، ولا تُحرَّر يدويًا.

**ما كشفه التوليد الآلي وطُبِّق:** رؤوس BC01 §7–§9 وصفت عدد SLC-01 وحده كأنه إجمالي BC01 (58 أمرًا بدل 67، وتوزيع أحداث مجموعه 55 بدل 60). صُحِّحت في [bc01-foundation.md](bc01-foundation.md). أعداد BC02–BC08 طابقت المصادر كما هي.

<!-- BEGIN GENERATED: build_relationships.py -->

## 21. السلاسل الكاملة لكل Aggregate (مولَّدة آليًا)

هذا القسم مولَّد بالكامل من المصادر بواسطة `_build/build_relationships.py`، ويُعاد توليده عند تغيّر أي مصدر، فلا يُحرَّر يدويًا. يجيب لكل Aggregate عن الأسئلة: ما القدرات والـUse Cases والمتطلبات المرتبطة؟ ما الأوامر، ومن ينفّذها، وأي سياسة تحكمها؟ ما الأحداث الناتجة، ومن يستهلكها؟ ما الثوابت والاستعلامات والتهديدات والاختبارات المرتبطة؟

**تصنيف المعرفة لكل حلقة في السلسلة:**

| الحلقة | المصدر | التصنيف |
|---|---|---|
| AGG → REQ، ADR، INV، الحالات | front-matter وجسم ملف الـAggregate | Explicit |
| AGG → CMD (الفاعل، السياسة، الأحداث) | عمود Aggregate في `commands-slcNN.md` | Explicit |
| AGG → EVT → المستهلكون | عمود Aggregate في `events-slcNN.md` | Explicit |
| REQ → UC | `use_cases` في المتطلب و`requirements` في الـUC | Explicit |
| REQ → CAP | حقل `capability` في المتطلب | Explicit |
| AGG → QRY | بادئة المعرّف (QRY-XXX- ↔ CMD-XXX-) داخل نفس الـBC | Derived |
| AGG → THR | تهديد يستشهد نصّه أو ضوابطه بمعرّف من هذا الـAggregate (AGG/CMD/QRY/INV) | Derived |
| AGG → اختبار القبول | `traces.state_machine` ↔ اسم ملف `13-verification/acceptance/*` | Derived |

**ما لا يُولَّد هنا:** طبقة Features غير موجودة في المصادر أصلًا (لا يوجد أي كيان `FEAT-*` في `spec/`)، فالسلسلة تنتقل مباشرة من CAP إلى UC. هذا **[Missing]** في المصدر لا في هذه الدراسة.

### 21.1 ملخص التغطية (محسوب)

| المقياس | القيمة |
|---|---|
| Aggregates | 89 |
| أوامر مرتبطة بـAggregate | 477 |
| أحداث مرتبطة بـAggregate | 584 |
| استعلامات مرتبطة بـAggregate (Derived) | 117 |
| استعلامات لم تُطابَق مع Aggregate بالبادئة | 16 |
| متطلبات يلبيها Aggregate واحد على الأقل (`traces.satisfies`) | 173 من 210 |
| Aggregates بلا أي UC عبر متطلباتها | 1 |
| Aggregates بلا أوامر | 0 |
| أحداث بلا مستهلك مُعلَن | 0 |
| Aggregates بلا ملف اختبار قبول مطابق | 0 |

**Aggregates بلا أي Use Case عبر حلقة REQ→UC:** `AGG-EXTERNAL-ID` (BC02)

هذه القائمة آلية وتتبع حلقة REQ→UC فقط. قد يربط ملف الـBC حالة استخدام بالـAggregate مباشرة (Derived، في §5 منه)، فراجعه قبل اعتبار البند فجوة. الفجوات المؤكَّدة يدويًا مسجَّلة في [05-conflicts.md §6](05-conflicts.md) (CONFLICT-05).

**حسب الـBC (محسوب من المصادر):**

| BC | Aggregates | أوامر | أحداث | استعلامات (Derived) | تهديدات مرتبطة بمعرّف (Derived) |
|---|---|---|---|---|---|
| BC01 | 11 | 67 | 73 | 9 | 6 |
| BC02 | 18 | 92 | 106 | 25 | 3 |
| BC03 | 9 | 52 | 59 | 15 | 1 |
| BC04 | 12 | 82 | 101 | 21 | 10 |
| BC05 | 13 | 69 | 78 | 17 | 10 |
| BC06 | 6 | 29 | 42 | 8 | 0 |
| BC07 | 13 | 58 | 82 | 14 | 2 |
| BC08 | 7 | 28 | 43 | 8 | 3 |

**تهديدات لا تستشهد بأي معرّف Aggregate** (80): ضوابطها وصفية (مثل «assign guard: clearance ≥ label») فلا يمكن ربطها آليًا. إسنادها إلى الـBC موثَّق يدويًا في §12 من ملف كل BC. THR-S01-06, THR-S01-07, THR-S01-08, THR-S01-09, THR-S01-10, THR-S01-11, THR-S02-01, THR-S02-02, THR-S02-03, THR-S02-04, THR-S02-05, THR-S02-06, THR-S02-07, THR-S02-08, THR-S02-09, THR-S02-10, THR-S03-03, THR-S03-04, THR-S03-05, THR-S03-06, THR-S04-01, THR-S04-02, THR-S04-04, THR-S04-05, THR-S04-06, THR-S04-07, THR-S05-01, THR-S05-02, THR-S05-03, THR-S05-04, THR-S05-05, THR-S05-06, THR-S05-07, THR-S05-08, THR-S06-03, THR-S06-04, THR-S06-05, THR-S06-06, THR-S06-07, THR-S07-01, THR-S07-02, THR-S07-03, THR-S07-04, THR-S07-05, THR-S07-06, THR-S08-01, THR-S08-02, THR-S08-03, THR-S08-04, THR-S08-05, THR-S08-06, THR-S09-01, THR-S09-02, THR-S09-03, THR-S09-04, THR-S10-01, THR-S10-03, THR-S10-04, THR-S10-05, THR-S10-06, THR-S11-01, THR-S11-02, THR-S11-03, THR-S11-05, THR-S11-06, THR-S12-01, THR-S12-03, THR-S12-04, THR-S12-05, THR-S12-P1, THR-S12-P2, THR-S12-P3, THR-S12-P4, THR-S12-P5, THR-S14-02, THR-S15-04, THR-S16-01, THR-S16-03, THR-S16-04, THR-S16-05

### 21.2 متطلبات لا يلبيها أي Aggregate

37 متطلبًا من 210 لا يظهر في `traces.satisfies` لأي Aggregate. بعضها متطلبات بنية تحتية أو جودة لا نموذج مجال (مثل REQ-GOV-005)، وبعضها من إصدارات لاحقة (R2/R3).

- **R1** (26): REQ-FND-010, REQ-FND-013, REQ-FND-015, REQ-FND-016, REQ-GOV-002, REQ-GOV-005, REQ-INF-023, REQ-INF-029, REQ-INF-030, REQ-INF-031, REQ-PLT-001, REQ-PLT-002, REQ-PLT-003, REQ-PLT-004, REQ-PLT-005, REQ-PLT-006, REQ-PLT-007, REQ-PLT-008, REQ-PLT-009, REQ-PLT-010, REQ-PLT-011, REQ-PLT-012, REQ-PLT-013, REQ-SIT-007, REQ-SRC-001, REQ-SRC-002
- **R2** (1): REQ-AI-014
- **R3** (10): REQ-LOG-010, REQ-LOG-011, REQ-LOG-012, REQ-RCM-014, REQ-RCM-015, REQ-RCM-016, REQ-TRX-012, REQ-TRX-013, REQ-TRX-014, REQ-TRX-015

### 21.3 مستهلكو الأحداث العابرون للـBCs

أحداث يذكر عمود «المستهلكون» فيها Bounded Context آخر غير الـBC المنتِج صراحةً (Explicit).

| الحدث | المنتِج | المستهلكون |
|---|---|---|
| EVT-RUN-QUEUED | BC03 · AGG-ANALYSIS-RUN | Job scheduler / compute workers; Lineage writer (BC02 LineageRecord); Case owner notification |
| EVT-RUN-STARTED | BC03 · AGG-ANALYSIS-RUN | Job scheduler / compute workers; Lineage writer (BC02 LineageRecord); Case owner notification |
| EVT-RUN-SUCCEEDED | BC03 · AGG-ANALYSIS-RUN | Job scheduler / compute workers; Lineage writer (BC02 LineageRecord); Case owner notification |
| EVT-RUN-FAILED | BC03 · AGG-ANALYSIS-RUN | Job scheduler / compute workers; Lineage writer (BC02 LineageRecord); Case owner notification |
| EVT-RUN-CANCELLED | BC03 · AGG-ANALYSIS-RUN | Job scheduler / compute workers; Lineage writer (BC02 LineageRecord); Case owner notification |
| EVT-CLS-DRAFTED | BC08 · AGG-CLASSIFICATION-SCHEME | Search/Directory projection (BC01 read model); PDP bundle distributor |
| EVT-CLS-EDITED | BC08 · AGG-CLASSIFICATION-SCHEME | Search/Directory projection (BC01 read model); PDP bundle distributor |
| EVT-CLS-ACTIVATED | BC08 · AGG-CLASSIFICATION-SCHEME | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model); PDP bundle distributor |
| EVT-CLS-DISCARDED | BC08 · AGG-CLASSIFICATION-SCHEME | Search/Directory projection (BC01 read model); PDP bundle distributor |
| EVT-CLS-SUPERSEDED | BC08 · AGG-CLASSIFICATION-SCHEME | Search/Directory projection (BC01 read model); PDP bundle distributor |
| EVT-ERS-RECEIVED | BC08 · AGG-ERASURE-REQUEST | Key manager (subject key destruction); BC01 / BC02 / BC05 (scope + confirmation); Projections (purge) |
| EVT-ERS-SCOPED | BC08 · AGG-ERASURE-REQUEST | Key manager (subject key destruction); BC01 / BC02 / BC05 (scope + confirmation); Projections (purge) |
| EVT-ERS-APPROVED | BC08 · AGG-ERASURE-REQUEST | Key manager (subject key destruction); BC01 / BC02 / BC05 (scope + confirmation); Projections (purge) |
| EVT-ERS-REJECTED | BC08 · AGG-ERASURE-REQUEST | Key manager (subject key destruction); BC01 / BC02 / BC05 (scope + confirmation); Projections (purge) |
| EVT-ERS-BLOCKED | BC08 · AGG-ERASURE-REQUEST | Key manager (subject key destruction); BC01 / BC02 / BC05 (scope + confirmation); Projections (purge) |
| EVT-ERS-UNBLOCKED | BC08 · AGG-ERASURE-REQUEST | Key manager (subject key destruction); BC01 / BC02 / BC05 (scope + confirmation); Projections (purge) |
| EVT-ERS-EXECUTING | BC08 · AGG-ERASURE-REQUEST | Key manager (subject key destruction); BC01 / BC02 / BC05 (scope + confirmation); Projections (purge) |
| EVT-ERS-COMPLETED | BC08 · AGG-ERASURE-REQUEST | Key manager (subject key destruction); BC01 / BC02 / BC05 (scope + confirmation); Projections (purge) |
| EVT-POL-DRAFTED | BC08 · AGG-POLICY-SET | Search/Directory projection (BC01 read model); PDP bundle distributor |
| EVT-POL-EDITED | BC08 · AGG-POLICY-SET | Search/Directory projection (BC01 read model); PDP bundle distributor |
| EVT-POL-SUBMITTED | BC08 · AGG-POLICY-SET | Search/Directory projection (BC01 read model); PDP bundle distributor |
| EVT-POL-APPROVED | BC08 · AGG-POLICY-SET | Search/Directory projection (BC01 read model); PDP bundle distributor |
| EVT-POL-REJECTED | BC08 · AGG-POLICY-SET | Search/Directory projection (BC01 read model); PDP bundle distributor |
| EVT-POL-ACTIVATED | BC08 · AGG-POLICY-SET | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model); PDP bundle distributor |
| EVT-POL-SUPERSEDED | BC08 · AGG-POLICY-SET | Search/Directory projection (BC01 read model); PDP bundle distributor |
| EVT-EXC-REQUESTED | BC08 · AGG-SECURITY-EXCEPTION | Search/Directory projection (BC01 read model) |
| EVT-EXC-FIRST-APPROVED | BC08 · AGG-SECURITY-EXCEPTION | Search/Directory projection (BC01 read model) |
| EVT-EXC-ACTIVATED | BC08 · AGG-SECURITY-EXCEPTION | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) |
| EVT-EXC-REJECTED | BC08 · AGG-SECURITY-EXCEPTION | Search/Directory projection (BC01 read model) |
| EVT-EXC-REVOKED | BC08 · AGG-SECURITY-EXCEPTION | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) |
| EVT-EXC-EXPIRED | BC08 · AGG-SECURITY-EXCEPTION | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) |

### 21.4 BC01 — [bc01-foundation.md](bc01-foundation.md)

11 Aggregate. التهديدات المرتبطة آليًا بـAggregates هذا الـBC: THR-S01-01, THR-S01-02, THR-S01-03, THR-S01-04, THR-S01-12, THR-S16-02. القائمة اليدوية الكاملة في §12 من ملفه.

استعلامات في ملفات BC01 لم تُطابَق مع Aggregate بالبادئة: QRY-SEC-CONTEXT.

#### AGG-AUTHORITY-GRANT — Authority Grant (incl. delegation)

`03-domain/contexts/BC01/aggregates/AGG-AUTHORITY-GRANT.md` · SLC-01 · T2 · بيانات شخصية: لا

```
CAP  CAP-01.03
 └ UC   UC-032, UC-035, UC-082, UC-083
    └ REQ  REQ-FND-007, REQ-FND-008, REQ-FND-009
       └ AGG-AUTHORITY-GRANT
          ├ INV  INV-AUT-01, INV-AUT-02, INV-AUT-03, INV-AUT-04
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-AUT-CHECK, QRY-AUT-LIST
          ├ THR  THR-S01-03, THR-S01-12
          └ TEST 13-verification/acceptance/SLC-01/authority-grant-state-machine.md
```

**الحالات:** غير نهائية: PENDING_APPROVAL, ACTIVE, SUSPENDED · نهائية: EXPIRED, REVOKED, REJECTED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-AUT-GRANT | holder of authority.grant; Executive approves | POL-AUT-GRANT | EVT-AUT-GRANT-REQUESTED | Search/Directory projection (BC01 read model); Notification (delegates informed on revoke/expire) |
| CMD-AUT-APPROVE-GRANT | holder of authority.grant; Executive approves | POL-AUT-APPROVE-GRANT | EVT-AUT-GRANTED | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model); Notification (delegates informed on revoke/expire) |
| CMD-AUT-REJECT-GRANT | holder of authority.grant; Executive approves | POL-AUT-REJECT-GRANT | EVT-AUT-GRANT-REJECTED | Search/Directory projection (BC01 read model); Notification (delegates informed on revoke/expire) |
| CMD-AUT-DELEGATE | holder of authority.grant; Executive approves | POL-AUT-DELEGATE | EVT-AUT-DELEGATED | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model); Notification (delegates informed on revoke/expire) |
| CMD-AUT-SUSPEND | holder of authority.grant; Executive approves | POL-AUT-SUSPEND | EVT-AUT-SUSPENDED | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model); Notification (delegates informed on revoke/expire) |
| CMD-AUT-RESUME | holder of authority.grant; Executive approves | POL-AUT-RESUME | EVT-AUT-RESUMED | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model); Notification (delegates informed on revoke/expire) |
| CMD-AUT-REVOKE | holder of authority.grant; Executive approves | POL-AUT-REVOKE | EVT-AUT-REVOKED | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model); Notification (delegates informed on revoke/expire) |

#### AGG-CLEARANCE — Clearance

`03-domain/contexts/BC01/aggregates/AGG-CLEARANCE.md` · SLC-01 · T2 · بيانات شخصية: لا

```
CAP  CAP-13.01
 └ UC   UC-085, UC-089
    └ REQ  REQ-GOV-003, REQ-GOV-004
       └ AGG-CLEARANCE
          ├ INV  INV-CLR-01, INV-CLR-02, INV-CLR-03, INV-CLR-04
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-CLR-GET
          ├ THR  THR-S01-04, THR-S01-12
          └ TEST 13-verification/acceptance/SLC-01/clearance-state-machine.md
```

**الحالات:** غير نهائية: PENDING_APPROVAL, ACTIVE, SUSPENDED · نهائية: EXPIRED, REVOKED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-CLR-GRANT | Security Officer | POL-CLR-GRANT | EVT-CLR-REQUESTED | Search/Directory projection (BC01 read model) |
| CMD-CLR-APPROVE | Security Officer | POL-CLR-APPROVE | EVT-CLR-GRANTED | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) |
| CMD-CLR-MODIFY | Security Officer | POL-CLR-MODIFY | EVT-CLR-MODIFIED | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) |
| CMD-CLR-SUSPEND | Security Officer | POL-CLR-SUSPEND | EVT-CLR-SUSPENDED | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) |
| CMD-CLR-REINSTATE | Security Officer | POL-CLR-REINSTATE | EVT-CLR-REINSTATED | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) |
| CMD-CLR-REVOKE | Security Officer | POL-CLR-REVOKE | EVT-CLR-REVOKED | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) |

#### AGG-DEVICE — Field Device

`03-domain/contexts/BC01/aggregates/AGG-DEVICE.md` · SLC-11 · T2 · بيانات شخصية: لا

```
CAP  CAP-02.03
 └ UC   UC-093
    └ REQ  REQ-OFF-005
       └ AGG-DEVICE
          ├ INV  INV-DEV-01, INV-DEV-02, INV-DEV-03, INV-DEV-04
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-DEV-LIST
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-11/device-state-machine.md
```

**الحالات:** غير نهائية: PENDING_ENROLLMENT, ACTIVE, SUSPENDED, LOST · نهائية: WIPED, RETIRED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-DEV-ENROLL | user (enroll, report lost) · Administrator / MDM policy (confirm, suspend, reinstate, retire) · Security Officer (lost, retire override) | POL-DEV-ENROLL | EVT-DEV-ENROLL-REQUESTED | Sync gateway (device registry cache); Preload packages (revoke on LOST/SUSPENDED); Security-version service |
| CMD-DEV-CONFIRM | user (enroll, report lost) · Administrator / MDM policy (confirm, suspend, reinstate, retire) · Security Officer (lost, retire override) | POL-DEV-CONFIRM | EVT-DEV-ACTIVATED | Sync gateway (device registry cache); Preload packages (revoke on LOST/SUSPENDED); Security-version service |
| CMD-DEV-ROTATE-KEY | user (enroll, report lost) · Administrator / MDM policy (confirm, suspend, reinstate, retire) · Security Officer (lost, retire override) | POL-DEV-ROTATE-KEY | EVT-DEV-KEY-ROTATED | Sync gateway (device registry cache); Preload packages (revoke on LOST/SUSPENDED); Security-version service |
| CMD-DEV-SUSPEND | user (enroll, report lost) · Administrator / MDM policy (confirm, suspend, reinstate, retire) · Security Officer (lost, retire override) | POL-DEV-SUSPEND | EVT-DEV-SUSPENDED | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Sync gateway (device registry cache); Preload packages (revoke on LOST/SUSPENDED); Security-version service |
| CMD-DEV-REINSTATE | user (enroll, report lost) · Administrator / MDM policy (confirm, suspend, reinstate, retire) · Security Officer (lost, retire override) | POL-DEV-REINSTATE | EVT-DEV-REINSTATED | Sync gateway (device registry cache); Preload packages (revoke on LOST/SUSPENDED); Security-version service |
| CMD-DEV-REPORT-LOST | user (enroll, report lost) · Administrator / MDM policy (confirm, suspend, reinstate, retire) · Security Officer (lost, retire override) | POL-DEV-REPORT-LOST | EVT-DEV-REPORTED-LOST | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Sync gateway (device registry cache); Preload packages (revoke on LOST/SUSPENDED); Security-version service |
| CMD-DEV-RETIRE | user (enroll, report lost) · Administrator / MDM policy (confirm, suspend, reinstate, retire) · Security Officer (lost, retire override) | POL-DEV-RETIRE | EVT-DEV-RETIRED | Sync gateway (device registry cache); Preload packages (revoke on LOST/SUSPENDED); Security-version service |

#### AGG-HR-SYNC-PROPOSAL — HR Sync Proposal

`03-domain/contexts/BC01/aggregates/AGG-HR-SYNC-PROPOSAL.md` · SLC-16 · T2 · بيانات شخصية: نعم

```
CAP  CAP-01.02
 └ UC   UC-084
    └ REQ  REQ-INT-004
       └ AGG-HR-SYNC-PROPOSAL
          ├ INV  INV-HRS-01, INV-HRS-02, INV-HRS-03
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-HRS-QUEUE
          ├ THR  THR-S16-02
          └ TEST 13-verification/acceptance/SLC-16/hr-sync-proposal-state-machine.md
```

**الحالات:** غير نهائية: PROPOSED · نهائية: APPROVED, REJECTED, SUPERSEDED, EXPIRED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-HRS-APPROVE | Administrator in scope | POL-HRS-APPROVE | EVT-HRS-APPROVED | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Role assignments / users (BC01); Security Officer notification (leave) |
| CMD-HRS-REJECT | Administrator in scope | POL-HRS-REJECT | EVT-HRS-REJECTED | Role assignments / users (BC01); Security Officer notification (leave) |

#### AGG-ORGANIZATION — Organization (with unit tree)

`03-domain/contexts/BC01/aggregates/AGG-ORGANIZATION.md` · SLC-01 · T2 · بيانات شخصية: لا

```
CAP  CAP-01.01
 └ UC   UC-081
    └ REQ  REQ-FND-002
       └ AGG-ORGANIZATION
          ├ INV  INV-ORG-01, INV-ORG-02, INV-ORG-03, INV-ORG-04
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-ORG-TREE
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-01/organization-state-machine.md
```

**الحالات:** غير نهائية: ACTIVE, INACTIVE · نهائية: — (perpetual)

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-ORG-CREATE | Administrator (in scope) | POL-ORG-CREATE | EVT-ORG-CREATED | Search/Directory projection (BC01 read model); All contexts' org-scope read models |
| CMD-ORG-RENAME | Administrator (in scope) | POL-ORG-RENAME | EVT-ORG-RENAMED | Search/Directory projection (BC01 read model); All contexts' org-scope read models |
| CMD-ORG-ADD-UNIT | Administrator (in scope) | POL-ORG-ADD-UNIT | EVT-ORG-UNIT-ADDED | Search/Directory projection (BC01 read model); All contexts' org-scope read models |
| CMD-ORG-RENAME-UNIT | Administrator (in scope) | POL-ORG-RENAME-UNIT | EVT-ORG-UNIT-RENAMED | Search/Directory projection (BC01 read model); All contexts' org-scope read models |
| CMD-ORG-MOVE-UNIT | Administrator (in scope) | POL-ORG-MOVE-UNIT | EVT-ORG-UNIT-MOVED | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model); All contexts' org-scope read models |
| CMD-ORG-DEACTIVATE-UNIT | Administrator (in scope) | POL-ORG-DEACTIVATE-UNIT | EVT-ORG-UNIT-DEACTIVATED | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model); All contexts' org-scope read models |
| CMD-ORG-DEACTIVATE | Administrator (in scope) | POL-ORG-DEACTIVATE | EVT-ORG-DEACTIVATED | Search/Directory projection (BC01 read model); All contexts' org-scope read models |
| CMD-ORG-REACTIVATE | Administrator (in scope) | POL-ORG-REACTIVATE | EVT-ORG-REACTIVATED | Search/Directory projection (BC01 read model); All contexts' org-scope read models |

#### AGG-PERSON — Person

`03-domain/contexts/BC01/aggregates/AGG-PERSON.md` · SLC-01 · T2 · بيانات شخصية: نعم

```
CAP  CAP-01.02, CAP-13.03
 └ UC   UC-084, UC-103
    └ REQ  REQ-FND-006, REQ-GOV-008
       └ AGG-PERSON
          ├ INV  INV-PER-01, INV-PER-02
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  —
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-01/person-state-machine.md
```

**الحالات:** غير نهائية: ACTIVE, INACTIVE · نهائية: ERASED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-PER-REGISTER | Administrator (in scope) | POL-PER-REGISTER | EVT-PER-REGISTERED | Search/Directory projection (BC01 read model) |
| CMD-PER-UPDATE-DETAILS | Administrator (in scope) | POL-PER-UPDATE-DETAILS | EVT-PER-DETAILS-UPDATED | Search/Directory projection (BC01 read model) |
| CMD-PER-DEACTIVATE | Administrator (in scope) | POL-PER-DEACTIVATE | EVT-PER-DEACTIVATED | Search/Directory projection (BC01 read model) |
| CMD-PER-REACTIVATE | Administrator (in scope) | POL-PER-REACTIVATE | EVT-PER-REACTIVATED | Search/Directory projection (BC01 read model) |
| CMD-PER-ERASE | Administrator (in scope) | POL-PER-ERASE | EVT-PER-ERASED | Search/Directory projection (BC01 read model) |

#### AGG-ROLE — Role

`03-domain/contexts/BC01/aggregates/AGG-ROLE.md` · SLC-01 · T2 · بيانات شخصية: لا

```
CAP  CAP-01.04
 └ UC   UC-086
    └ REQ  REQ-FND-014
       └ AGG-ROLE
          ├ INV  INV-ROL-01, INV-ROL-02, INV-ROL-03
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  —
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-01/role-state-machine.md
```

**الحالات:** غير نهائية: DRAFT, ACTIVE · نهائية: RETIRED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-ROL-DEFINE | Administrator | POL-ROL-DEFINE | EVT-ROL-DEFINED | Search/Directory projection (BC01 read model) |
| CMD-ROL-SET-PERMISSIONS | Administrator | POL-ROL-SET-PERMISSIONS | EVT-ROL-PERMISSIONS-CHANGED | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) |
| CMD-ROL-ACTIVATE | Administrator | POL-ROL-ACTIVATE | EVT-ROL-ACTIVATED | Search/Directory projection (BC01 read model) |
| CMD-ROL-RETIRE | Administrator | POL-ROL-RETIRE | EVT-ROL-RETIRED | Search/Directory projection (BC01 read model) |

#### AGG-ROLE-ASSIGNMENT — Role Assignment

`03-domain/contexts/BC01/aggregates/AGG-ROLE-ASSIGNMENT.md` · SLC-01 · T2 · بيانات شخصية: لا

```
CAP  CAP-01.04, CAP-07.02, CAP-07.03
 └ UC   UC-035, UC-044, UC-086
    └ REQ  REQ-FND-011, REQ-OPS-005, REQ-OPS-009
       └ AGG-ROLE-ASSIGNMENT
          ├ INV  INV-RAS-01, INV-RAS-02, INV-RAS-03
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  —
          ├ THR  THR-S01-01, THR-S01-02, THR-S01-12
          └ TEST 13-verification/acceptance/SLC-01/role-assignment-state-machine.md
```

**الحالات:** غير نهائية: ACTIVE · نهائية: EXPIRED, REVOKED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-RAS-ASSIGN | Administrator (in scope, not self) | POL-RAS-ASSIGN | EVT-RAS-ASSIGNED | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) |
| CMD-RAS-REVOKE | Administrator (in scope, not self) | POL-RAS-REVOKE | EVT-RAS-REVOKED | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) |

#### AGG-SERVICE-ACCOUNT — Service Account

`03-domain/contexts/BC01/aggregates/AGG-SERVICE-ACCOUNT.md` · SLC-01 · T2 · بيانات شخصية: لا

```
CAP  CAP-01.02
 └ UC   UC-084
    └ REQ  REQ-FND-006
       └ AGG-SERVICE-ACCOUNT
          ├ INV  INV-SVC-01, INV-SVC-02, INV-SVC-03
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  —
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-01/service-account-state-machine.md
```

**الحالات:** غير نهائية: ACTIVE, DISABLED · نهائية: CLOSED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-SVC-CREATE | Administrator | POL-SVC-CREATE | EVT-SVC-CREATED | Search/Directory projection (BC01 read model) |
| CMD-SVC-ROTATE-CREDENTIAL | Administrator | POL-SVC-ROTATE-CREDENTIAL | EVT-SVC-CREDENTIAL-ROTATED | Search/Directory projection (BC01 read model) |
| CMD-SVC-DISABLE | Administrator | POL-SVC-DISABLE | EVT-SVC-DISABLED | Search/Directory projection (BC01 read model) |
| CMD-SVC-ENABLE | Administrator | POL-SVC-ENABLE | EVT-SVC-ENABLED | Search/Directory projection (BC01 read model) |
| CMD-SVC-CLOSE | Administrator | POL-SVC-CLOSE | EVT-SVC-CLOSED | Search/Directory projection (BC01 read model) |

#### AGG-TENANT — Tenant

`03-domain/contexts/BC01/aggregates/AGG-TENANT.md` · SLC-01 · T2 · بيانات شخصية: لا

```
CAP  CAP-01.01, CAP-14.03
 └ UC   UC-080, UC-105
    └ REQ  REQ-FND-001, REQ-FND-003, REQ-FND-004, REQ-FND-018
       └ AGG-TENANT
          ├ INV  INV-TEN-01, INV-TEN-02, INV-TEN-03, INV-TEN-04, INV-TEN-05
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-TEN-GET
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-01/tenant-state-machine.md
```

**الحالات:** غير نهائية: PROVISIONING, PROVISIONING_FAILED, ACTIVE, SUSPENDED, MIGRATING, DECOMMISSIONING · نهائية: DECOMMISSIONED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-TEN-PROVISION | Platform Operator (provision, migrate, decommission) / Tenant Administrator (quotas view) | POL-TEN-PROVISION | EVT-TEN-PROVISIONING-STARTED | Search/Directory projection (BC01 read model); Provisioning saga / cell controller |
| CMD-TEN-COMPLETE-PROVISIONING | system (workload identity) | POL-TEN-COMPLETE-PROVISIONING | EVT-TEN-ACTIVATED | Search/Directory projection (BC01 read model); Provisioning saga / cell controller |
| CMD-TEN-FAIL-PROVISIONING | system (workload identity) | POL-TEN-FAIL-PROVISIONING | EVT-TEN-PROVISIONING-FAILED | Search/Directory projection (BC01 read model); Provisioning saga / cell controller |
| CMD-TEN-RETRY-PROVISIONING | Platform Operator (provision, migrate, decommission) / Tenant Administrator (quotas view) | POL-TEN-RETRY-PROVISIONING | EVT-TEN-PROVISIONING-STARTED | Search/Directory projection (BC01 read model); Provisioning saga / cell controller |
| CMD-TEN-SUSPEND | Platform Operator (provision, migrate, decommission) / Tenant Administrator (quotas view) | POL-TEN-SUSPEND | EVT-TEN-SUSPENDED | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model); Provisioning saga / cell controller |
| CMD-TEN-REACTIVATE | Platform Operator (provision, migrate, decommission) / Tenant Administrator (quotas view) | POL-TEN-REACTIVATE | EVT-TEN-REACTIVATED | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model); Provisioning saga / cell controller |
| CMD-TEN-START-CELL-MIGRATION | Platform Operator (provision, migrate, decommission) / Tenant Administrator (quotas view) | POL-TEN-START-CELL-MIGRATION | EVT-TEN-MIGRATION-STARTED | Search/Directory projection (BC01 read model); Provisioning saga / cell controller |
| CMD-TEN-COMPLETE-CELL-MIGRATION | system (workload identity) | POL-TEN-COMPLETE-CELL-MIGRATION | EVT-TEN-MIGRATED | Search/Directory projection (BC01 read model); Provisioning saga / cell controller |
| CMD-TEN-START-DECOMMISSION | Platform Operator (provision, migrate, decommission) / Tenant Administrator (quotas view) | POL-TEN-START-DECOMMISSION | EVT-TEN-DECOMMISSION-STARTED | Search/Directory projection (BC01 read model); Provisioning saga / cell controller |
| CMD-TEN-COMPLETE-DECOMMISSION | system (workload identity) | POL-TEN-COMPLETE-DECOMMISSION | EVT-TEN-DECOMMISSIONED | Search/Directory projection (BC01 read model); Provisioning saga / cell controller |
| CMD-TEN-UPDATE-QUOTAS | Platform Operator (provision, migrate, decommission) / Tenant Administrator (quotas view) | POL-TEN-UPDATE-QUOTAS | EVT-TEN-QUOTAS-UPDATED | Search/Directory projection (BC01 read model); Provisioning saga / cell controller |

#### AGG-USER — User Account

`03-domain/contexts/BC01/aggregates/AGG-USER.md` · SLC-01 · T2 · بيانات شخصية: لا

```
CAP  CAP-01.02
 └ UC   UC-084
    └ REQ  REQ-FND-005, REQ-FND-006
       └ AGG-USER
          ├ INV  INV-USR-01, INV-USR-02, INV-USR-03, INV-USR-04, INV-USR-05
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-USR-GET, QRY-USR-LIST
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-01/user-state-machine.md
```

**الحالات:** غير نهائية: PENDING, ACTIVE, LOCKED, DISABLED · نهائية: CLOSED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-USR-PROVISION | Administrator in scope / SCIM service account / Security Officer (lock) | POL-USR-PROVISION | EVT-USR-PROVISIONED | Search/Directory projection (BC01 read model) |
| CMD-USR-LINK-IDENTITY | Administrator in scope / SCIM service account / Security Officer (lock) | POL-USR-LINK-IDENTITY | EVT-USR-IDENTITY-LINKED | Search/Directory projection (BC01 read model) |
| CMD-USR-UNLINK-IDENTITY | Administrator in scope / SCIM service account / Security Officer (lock) | POL-USR-UNLINK-IDENTITY | EVT-USR-IDENTITY-UNLINKED | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) |
| CMD-USR-LINK-PERSON | Administrator in scope / SCIM service account / Security Officer (lock) | POL-USR-LINK-PERSON | EVT-USR-PERSON-LINKED | Search/Directory projection (BC01 read model) |
| CMD-USR-RECORD-FIRST-SIGN-IN | system (workload identity) | POL-USR-RECORD-FIRST-SIGN-IN | EVT-USR-ACTIVATED | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) |
| CMD-USR-LOCK | Administrator in scope / SCIM service account / Security Officer (lock) | POL-USR-LOCK | EVT-USR-LOCKED | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) |
| CMD-USR-UNLOCK | Administrator in scope / SCIM service account / Security Officer (lock) | POL-USR-UNLOCK | EVT-USR-UNLOCKED | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) |
| CMD-USR-DISABLE | Administrator in scope / SCIM service account / Security Officer (lock) | POL-USR-DISABLE | EVT-USR-DISABLED | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) |
| CMD-USR-ENABLE | Administrator in scope / SCIM service account / Security Officer (lock) | POL-USR-ENABLE | EVT-USR-ENABLED | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) |
| CMD-USR-CLOSE | Administrator in scope / SCIM service account / Security Officer (lock) | POL-USR-CLOSE | EVT-USR-CLOSED | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) |

### 21.5 BC02 — [bc02-information-core.md](bc02-information-core.md)

18 Aggregate. التهديدات المرتبطة آليًا بـAggregates هذا الـBC: THR-S04-03, THR-S14-01, THR-S15-03. القائمة اليدوية الكاملة في §12 من ملفه.

استعلامات في ملفات BC02 لم تُطابَق مع Aggregate بالبادئة: QRY-CLUSTER-GET, QRY-LIN-TRACE.

#### AGG-ATTACHMENT — Attachment

`03-domain/contexts/BC02/aggregates/AGG-ATTACHMENT.md` · SLC-02 · T1 metadata · بيانات شخصية: لا

```
CAP  CAP-02.03, CAP-13.03
 └ UC   UC-005, UC-006, UC-103
    └ REQ  REQ-GOV-008, REQ-INF-003, REQ-INF-004
       └ AGG-ATTACHMENT
          ├ INV  INV-ATT-01, INV-ATT-02, INV-ATT-03, INV-ATT-04
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-ATT-DOWNLOAD
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-02/attachment-state-machine.md
```

**الحالات:** غير نهائية: PENDING, SCANNING, STORED · نهائية: QUARANTINED, EXPIRED, ERASED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-ATT-INITIATE-UPLOAD | user with write permission on the target object | POL-ATT-INITIATE-UPLOAD | EVT-ATT-UPLOAD-INITIATED | Content scanner; Evidence registrar |
| CMD-ATT-COMPLETE-UPLOAD | user with write permission on the target object | POL-ATT-COMPLETE-UPLOAD | EVT-ATT-UPLOADED | Content scanner; Evidence registrar |
| CMD-ATT-ERASE | user with write permission on the target object | POL-ATT-ERASE | EVT-ATT-ERASED | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Content scanner; Evidence registrar |

#### AGG-CLAIM — Claim

`03-domain/contexts/BC02/aggregates/AGG-CLAIM.md` · SLC-02 · T1 · بيانات شخصية: لا

```
CAP  CAP-03.02, CAP-03.04, CAP-03.07
 └ UC   UC-006
    └ REQ  REQ-INF-021, REQ-INF-022, REQ-INF-024, REQ-INF-026, REQ-INF-037
       └ AGG-CLAIM
          ├ INV  INV-CLM-01, INV-CLM-02, INV-CLM-03, INV-CLM-04, INV-CLM-05
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-CLM-GET
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-02/claim-state-machine.md
```

**الحالات:** غير نهائية: CURRENT · نهائية: CLOSED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-CLM-ASSERT | Analyst · adapter service account · analysis-run identity (assert) · Analyst or verification re-evaluator system identity (assess) · Analyst (correct, change, retract) | POL-CLM-ASSERT | EVT-CLM-ASSERTED | Current-view maintainer (async materialized resolved views); Conflict detector (SLC-04); Situation membership (SLC-06); Search/Graph projections (SLC-05) |
| CMD-CLM-CORRECT | Analyst · adapter service account · analysis-run identity (assert) · Analyst or verification re-evaluator system identity (assess) · Analyst (correct, change, retract) | POL-CLM-CORRECT | EVT-CLM-CORRECTED | Current-view maintainer (async materialized resolved views); Conflict detector (SLC-04); Situation membership (SLC-06); Search/Graph projections (SLC-05) |
| CMD-CLM-RECORD-CHANGE | Analyst · adapter service account · analysis-run identity (assert) · Analyst or verification re-evaluator system identity (assess) · Analyst (correct, change, retract) | POL-CLM-RECORD-CHANGE | EVT-CLM-CHANGED | Current-view maintainer (async materialized resolved views); Conflict detector (SLC-04); Situation membership (SLC-06); Search/Graph projections (SLC-05) |
| CMD-CLM-RETRACT | Analyst · adapter service account · analysis-run identity (assert) · Analyst or verification re-evaluator system identity (assess) · Analyst (correct, change, retract) | POL-CLM-RETRACT | EVT-CLM-RETRACTED | Current-view maintainer (async materialized resolved views); Conflict detector (SLC-04); Situation membership (SLC-06); Search/Graph projections (SLC-05) |
| CMD-CLM-ASSESS | Analyst · adapter service account · analysis-run identity (assert) · Analyst or verification re-evaluator system identity (assess) · Analyst (correct, change, retract) | POL-CLM-ASSESS | EVT-CLM-ASSESSED | Current-view maintainer (async materialized resolved views); Conflict detector (SLC-04); Situation membership (SLC-06); Search/Graph projections (SLC-05) |
| CMD-CLM-RECLASSIFY | Analyst · adapter service account · analysis-run identity (assert) · Analyst or verification re-evaluator system identity (assess) · Analyst (correct, change, retract) | POL-CLM-RECLASSIFY | EVT-CLM-RECLASSIFIED | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Current-view maintainer (async materialized resolved views); Conflict detector (SLC-04); Situation membership (SLC-06); Search/Graph projections (SLC-05) |

#### AGG-COLLECTION-PLAN — Collection Plan

`03-domain/contexts/BC02/aggregates/AGG-COLLECTION-PLAN.md` · SLC-14 · T2 · بيانات شخصية: لا

```
CAP  CAP-02.01
 └ UC   UC-121
    └ REQ  REQ-COL-002
       └ AGG-COLLECTION-PLAN
          ├ INV  INV-CPL-01, INV-CPL-02
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-CPL-GET
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-14/collection-plan-state-machine.md
```

**الحالات:** غير نهائية: DRAFT, ACTIVE · نهائية: COMPLETED, CANCELLED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-CPL-CREATE | collection planner | POL-CPL-CREATE | EVT-CPL-CREATED | Task creation (SLC-03); Notification (units) |
| CMD-CPL-ADD-ACTIVITY | collection planner | POL-CPL-ADD-ACTIVITY | EVT-CPL-ACTIVITY-ADDED | Task creation (SLC-03); Notification (units) |
| CMD-CPL-REMOVE-ACTIVITY | collection planner | POL-CPL-REMOVE-ACTIVITY | EVT-CPL-ACTIVITY-REMOVED | Task creation (SLC-03); Notification (units) |
| CMD-CPL-ACTIVATE | collection planner | POL-CPL-ACTIVATE | EVT-CPL-ACTIVATED | Task creation (SLC-03); Notification (units) |
| CMD-CPL-COMPLETE | collection planner | POL-CPL-COMPLETE | EVT-CPL-COMPLETED | Task creation (SLC-03); Notification (units) |
| CMD-CPL-CANCEL | collection planner | POL-CPL-CANCEL | EVT-CPL-CANCELLED | Task creation (SLC-03); Notification (units) |

#### AGG-COLLECTION-REQUIREMENT — Collection Requirement

`03-domain/contexts/BC02/aggregates/AGG-COLLECTION-REQUIREMENT.md` · SLC-14 · T2 · بيانات شخصية: لا

```
CAP  CAP-02.01
 └ UC   UC-120, UC-122
    └ REQ  REQ-COL-001, REQ-COL-003
       └ AGG-COLLECTION-REQUIREMENT
          ├ INV  INV-CRQ-01, INV-CRQ-02, INV-CRQ-03, INV-CRQ-04
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-CRQ-BOARD, QRY-CRQ-EVIDENCE, QRY-CRQ-GET
          ├ THR  THR-S14-01
          └ TEST 13-verification/acceptance/SLC-14/collection-requirement-state-machine.md
```

**الحالات:** غير نهائية: DRAFT, SUBMITTED, APPROVED · نهائية: REJECTED, SATISFIED, EXPIRED, CANCELLED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-CRQ-DRAFT | Analyst / any requester (draft, edit, submit, satisfy, cancel) · collection manager (approve, reject, amend) | POL-CRQ-DRAFT | EVT-CRQ-DRAFTED | Matching engine (reload EEIs); Collection board; Search projection (SLC-05); Notification (requester) |
| CMD-CRQ-EDIT | Analyst / any requester (draft, edit, submit, satisfy, cancel) · collection manager (approve, reject, amend) | POL-CRQ-EDIT | EVT-CRQ-EDITED | Matching engine (reload EEIs); Collection board; Search projection (SLC-05); Notification (requester) |
| CMD-CRQ-SUBMIT | Analyst / any requester (draft, edit, submit, satisfy, cancel) · collection manager (approve, reject, amend) | POL-CRQ-SUBMIT | EVT-CRQ-SUBMITTED | Matching engine (reload EEIs); Collection board; Search projection (SLC-05); Notification (requester) |
| CMD-CRQ-APPROVE | Analyst / any requester (draft, edit, submit, satisfy, cancel) · collection manager (approve, reject, amend) | POL-CRQ-APPROVE | EVT-CRQ-APPROVED | Matching engine (reload EEIs); Collection board; Search projection (SLC-05); Notification (requester) |
| CMD-CRQ-REJECT | Analyst / any requester (draft, edit, submit, satisfy, cancel) · collection manager (approve, reject, amend) | POL-CRQ-REJECT | EVT-CRQ-REJECTED | Matching engine (reload EEIs); Collection board; Search projection (SLC-05); Notification (requester) |
| CMD-CRQ-AMEND | Analyst / any requester (draft, edit, submit, satisfy, cancel) · collection manager (approve, reject, amend) | POL-CRQ-AMEND | EVT-CRQ-AMENDED | Matching engine (reload EEIs); Collection board; Search projection (SLC-05); Notification (requester) |
| CMD-CRQ-MARK-SATISFIED | Analyst / any requester (draft, edit, submit, satisfy, cancel) · collection manager (approve, reject, amend) | POL-CRQ-MARK-SATISFIED | EVT-CRQ-SATISFIED | Matching engine (reload EEIs); Collection board; Search projection (SLC-05); Notification (requester) |
| CMD-CRQ-CANCEL | Analyst / any requester (draft, edit, submit, satisfy, cancel) · collection manager (approve, reject, amend) | POL-CRQ-CANCEL | EVT-CRQ-CANCELLED | Matching engine (reload EEIs); Collection board; Search projection (SLC-05); Notification (requester) |

#### AGG-CONFLICT — Conflict

`03-domain/contexts/BC02/aggregates/AGG-CONFLICT.md` · SLC-04 · T2 (bitemporal resolution records) · بيانات شخصية: لا

```
CAP  CAP-03.02, CAP-03.06
 └ UC   UC-008
    └ REQ  REQ-INF-024, REQ-INF-025
       └ AGG-CONFLICT
          ├ INV  INV-CNF-01, INV-CNF-02, INV-CNF-03, INV-CNF-04, INV-CNF-05
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-CNF-GET, QRY-CNF-LIST
          ├ THR  THR-S04-03
          └ TEST 13-verification/acceptance/SLC-04/conflict-state-machine.md
```

**الحالات:** غير نهائية: OPEN, UNDER_REVIEW, RESOLVED, ACCEPTED_AS_CONFLICT · نهائية: SUPERSEDED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-CNF-RAISE | Analyst (raise, review, resolve, accept, reopen) · Analyst lead (assign) | POL-CNF-RAISE | EVT-CNF-RAISED | Resolved-view materializer (SLC-05); Analyst notifications; Situation membership (SLC-06: DISPUTED markers) |
| CMD-CNF-ASSIGN | Analyst (raise, review, resolve, accept, reopen) · Analyst lead (assign) | POL-CNF-ASSIGN | EVT-CNF-ASSIGNED | Resolved-view materializer (SLC-05); Analyst notifications; Situation membership (SLC-06: DISPUTED markers) |
| CMD-CNF-START-REVIEW | Analyst (raise, review, resolve, accept, reopen) · Analyst lead (assign) | POL-CNF-START-REVIEW | EVT-CNF-REVIEW-STARTED | Resolved-view materializer (SLC-05); Analyst notifications; Situation membership (SLC-06: DISPUTED markers) |
| CMD-CNF-RESOLVE | Analyst (raise, review, resolve, accept, reopen) · Analyst lead (assign) | POL-CNF-RESOLVE | EVT-CNF-RESOLVED | Resolved-view materializer (SLC-05); Analyst notifications; Situation membership (SLC-06: DISPUTED markers) |
| CMD-CNF-ACCEPT | Analyst (raise, review, resolve, accept, reopen) · Analyst lead (assign) | POL-CNF-ACCEPT | EVT-CNF-ACCEPTED | Resolved-view materializer (SLC-05); Analyst notifications; Situation membership (SLC-06: DISPUTED markers) |
| CMD-CNF-REOPEN | Analyst (raise, review, resolve, accept, reopen) · Analyst lead (assign) | POL-CNF-REOPEN | EVT-CNF-REOPENED | Resolved-view materializer (SLC-05); Analyst notifications; Situation membership (SLC-06: DISPUTED markers) |

#### AGG-CORRELATION-PROPOSAL — Correlation Proposal

`03-domain/contexts/BC02/aggregates/AGG-CORRELATION-PROPOSAL.md` · SLC-15 · T1 · بيانات شخصية: لا

```
CAP  CAP-04.04
 └ UC   UC-132
    └ REQ  REQ-FUS-001, REQ-FUS-002
       └ AGG-CORRELATION-PROPOSAL
          ├ INV  INV-CRP-01, INV-CRP-02, INV-CRP-03, INV-CRP-04
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-CRP-GET, QRY-CRP-QUEUE
          ├ THR  THR-S15-03
          └ TEST 13-verification/acceptance/SLC-15/correlation-proposal-state-machine.md
```

**الحالات:** غير نهائية: PROPOSED, UNDER_REVIEW · نهائية: ACCEPTED, REJECTED, EXPIRED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-CRP-PROPOSE | Analyst (propose, review, accept, reject) | POL-CRP-PROPOSE | EVT-CRP-PROPOSED | Owner commands on acceptance (BC02 events/relationships, SLC-04 ER); Rule evaluation feedback |
| CMD-CRP-START-REVIEW | Analyst (propose, review, accept, reject) | POL-CRP-START-REVIEW | EVT-CRP-REVIEW-STARTED | Owner commands on acceptance (BC02 events/relationships, SLC-04 ER); Rule evaluation feedback |
| CMD-CRP-ACCEPT | Analyst (propose, review, accept, reject) | POL-CRP-ACCEPT | EVT-CRP-ACCEPTED | Owner commands on acceptance (BC02 events/relationships, SLC-04 ER); Rule evaluation feedback |
| CMD-CRP-REJECT | Analyst (propose, review, accept, reject) | POL-CRP-REJECT | EVT-CRP-REJECTED | Owner commands on acceptance (BC02 events/relationships, SLC-04 ER); Rule evaluation feedback |

#### AGG-CORRELATION-RULE — Correlation Rule

`03-domain/contexts/BC02/aggregates/AGG-CORRELATION-RULE.md` · SLC-15 · T2 · بيانات شخصية: لا

```
CAP  CAP-04.04
 └ UC   UC-132
    └ REQ  REQ-FUS-001
       └ AGG-CORRELATION-RULE
          ├ INV  INV-CRR-01, INV-CRR-02
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  —
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-15/correlation-rule-state-machine.md
```

**الحالات:** غير نهائية: DRAFT, ACTIVE · نهائية: RETIRED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-CRR-DEFINE | Analyst lead (define, edit) · second approver (activate) | POL-CRR-DEFINE | EVT-CRR-DEFINED | Correlation engine |
| CMD-CRR-EDIT | Analyst lead (define, edit) · second approver (activate) | POL-CRR-EDIT | EVT-CRR-EDITED | Correlation engine |
| CMD-CRR-ACTIVATE | Analyst lead (define, edit) · second approver (activate) | POL-CRR-ACTIVATE | EVT-CRR-ACTIVATED | Correlation engine |
| CMD-CRR-RETIRE | Analyst lead (define, edit) · second approver (activate) | POL-CRR-RETIRE | EVT-CRR-RETIRED | Correlation engine |

#### AGG-ENTITY — Entity (identity)

`03-domain/contexts/BC02/aggregates/AGG-ENTITY.md` · SLC-02 · T2 identity; attributes T1 as claims · بيانات شخصية: لا

```
CAP  CAP-03.01, CAP-03.02
 └ UC   UC-001, UC-002, UC-003, UC-006
    └ REQ  REQ-INF-020, REQ-INF-021, REQ-INF-036
       └ AGG-ENTITY
          ├ INV  INV-ENT-01, INV-ENT-02, INV-ENT-03
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-ENT-CLAIMS, QRY-ENT-LIST, QRY-ENT-POSITIONS, QRY-ENT-RESOLVED
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-02/entity-state-machine.md
```

**الحالات:** غير نهائية: ACTIVE, RETIRED · نهائية: — (perpetual)

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-ENT-REGISTER | Analyst · adapter service account | POL-ENT-REGISTER | EVT-ENT-REGISTERED | ER candidate generator (SLC-04); Search/Graph projections (SLC-05) |
| CMD-ENT-CHANGE-TYPE | Analyst · adapter service account | POL-ENT-CHANGE-TYPE | EVT-ENT-TYPE-CHANGED | ER candidate generator (SLC-04); Search/Graph projections (SLC-05) |
| CMD-ENT-RECLASSIFY | Analyst · adapter service account | POL-ENT-RECLASSIFY | EVT-ENT-RECLASSIFIED | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; ER candidate generator (SLC-04); Search/Graph projections (SLC-05) |
| CMD-ENT-RETIRE | Analyst · adapter service account | POL-ENT-RETIRE | EVT-ENT-RETIRED | ER candidate generator (SLC-04); Search/Graph projections (SLC-05) |
| CMD-ENT-REINSTATE | Analyst · adapter service account | POL-ENT-REINSTATE | EVT-ENT-REINSTATED | ER candidate generator (SLC-04); Search/Graph projections (SLC-05) |

#### AGG-ER-CASE — Entity Resolution Case

`03-domain/contexts/BC02/aggregates/AGG-ER-CASE.md` · SLC-04 · T2 · بيانات شخصية: لا

```
CAP  CAP-03.05
 └ UC   UC-007, UC-104
    └ REQ  REQ-INF-032, REQ-INF-033, REQ-INF-034
       └ AGG-ER-CASE
          ├ INV  INV-ER-01, INV-ER-02, INV-ER-03, INV-ER-04, INV-ER-05, INV-ER-06
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-ER-GET, QRY-ER-QUEUE
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-04/er-case-state-machine.md
```

**الحالات:** غير نهائية: CANDIDATE, UNDER_REVIEW, MATCHED, POSSIBLE_DUPLICATE, SPLIT_REQUIRED · نهائية: NOT_A_MATCH, SPLIT, WITHDRAWN

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-ER-PROPOSE | Analyst (propose, review, decide, request split) · second Analyst (confirm/split, large clusters) | POL-ER-PROPOSE | EVT-ER-PROPOSED | Cluster maintainer (same transaction) → EVT cluster changed; Conflict detector (re-run on cluster change); Search/Graph projections (canonical ids); Situation membership (SLC-06) |
| CMD-ER-START-REVIEW | Analyst (propose, review, decide, request split) · second Analyst (confirm/split, large clusters) | POL-ER-START-REVIEW | EVT-ER-REVIEW-STARTED | Cluster maintainer (same transaction) → EVT cluster changed; Conflict detector (re-run on cluster change); Search/Graph projections (canonical ids); Situation membership (SLC-06) |
| CMD-ER-DECIDE-MATCH | Analyst (propose, review, decide, request split) · second Analyst (confirm/split, large clusters) | POL-ER-DECIDE-MATCH | EVT-ER-MATCHED | Cluster maintainer (same transaction) → EVT cluster changed; Conflict detector (re-run on cluster change); Search/Graph projections (canonical ids); Situation membership (SLC-06) |
| CMD-ER-DECIDE-NOT-MATCH | Analyst (propose, review, decide, request split) · second Analyst (confirm/split, large clusters) | POL-ER-DECIDE-NOT-MATCH | EVT-ER-NOT-MATCHED | Cluster maintainer (same transaction) → EVT cluster changed; Conflict detector (re-run on cluster change); Search/Graph projections (canonical ids); Situation membership (SLC-06) |
| CMD-ER-PARK | Analyst (propose, review, decide, request split) · second Analyst (confirm/split, large clusters) | POL-ER-PARK | EVT-ER-PARKED | Cluster maintainer (same transaction) → EVT cluster changed; Conflict detector (re-run on cluster change); Search/Graph projections (canonical ids); Situation membership (SLC-06) |
| CMD-ER-RESUME | Analyst (propose, review, decide, request split) · second Analyst (confirm/split, large clusters) | POL-ER-RESUME | EVT-ER-RESUMED | Cluster maintainer (same transaction) → EVT cluster changed; Conflict detector (re-run on cluster change); Search/Graph projections (canonical ids); Situation membership (SLC-06) |
| CMD-ER-REQUEST-SPLIT | Analyst (propose, review, decide, request split) · second Analyst (confirm/split, large clusters) | POL-ER-REQUEST-SPLIT | EVT-ER-SPLIT-REQUESTED | Cluster maintainer (same transaction) → EVT cluster changed; Conflict detector (re-run on cluster change); Search/Graph projections (canonical ids); Situation membership (SLC-06) |
| CMD-ER-CONFIRM-MATCH | Analyst (propose, review, decide, request split) · second Analyst (confirm/split, large clusters) | POL-ER-CONFIRM-MATCH | EVT-ER-MATCH-CONFIRMED | Cluster maintainer (same transaction) → EVT cluster changed; Conflict detector (re-run on cluster change); Search/Graph projections (canonical ids); Situation membership (SLC-06) |
| CMD-ER-SPLIT | Analyst (propose, review, decide, request split) · second Analyst (confirm/split, large clusters) | POL-ER-SPLIT | EVT-ER-SPLIT | Cluster maintainer (same transaction) → EVT cluster changed; Conflict detector (re-run on cluster change); Search/Graph projections (canonical ids); Situation membership (SLC-06) |
| CMD-ER-WITHDRAW | Analyst (propose, review, decide, request split) · second Analyst (confirm/split, large clusters) | POL-ER-WITHDRAW | EVT-ER-WITHDRAWN | Cluster maintainer (same transaction) → EVT cluster changed; Conflict detector (re-run on cluster change); Search/Graph projections (canonical ids); Situation membership (SLC-06) |

#### AGG-EVIDENCE — Evidence

`03-domain/contexts/BC02/aggregates/AGG-EVIDENCE.md` · SLC-02 · T1 · بيانات شخصية: لا

```
CAP  CAP-02.03
 └ UC   UC-005, UC-006
    └ REQ  REQ-INF-003, REQ-INF-004
       └ AGG-EVIDENCE
          ├ INV  INV-EVD-01, INV-EVD-02, INV-EVD-03
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-EVD-GET
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-02/evidence-state-machine.md
```

**الحالات:** غير نهائية: REGISTERED, SEALED · نهائية: WITHDRAWN

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-EVD-REGISTER | Analyst · Field User (register) · custodian role (custody) | POL-EVD-REGISTER | EVT-EVD-REGISTERED | Verification re-evaluator (on WITHDRAWN: issues CMD-CLM-ASSESS as system identity for linked claims, recomputing verification from remaining SUPPORTS links); Search projection (SLC-05) |
| CMD-EVD-UPDATE-LOCATOR | Analyst · Field User (register) · custodian role (custody) | POL-EVD-UPDATE-LOCATOR | EVT-EVD-LOCATOR-UPDATED | Verification re-evaluator (on WITHDRAWN: issues CMD-CLM-ASSESS as system identity for linked claims, recomputing verification from remaining SUPPORTS links); Search projection (SLC-05) |
| CMD-EVD-SEAL | Analyst · Field User (register) · custodian role (custody) | POL-EVD-SEAL | EVT-EVD-SEALED | Verification re-evaluator (on WITHDRAWN: issues CMD-CLM-ASSESS as system identity for linked claims, recomputing verification from remaining SUPPORTS links); Search projection (SLC-05) |
| CMD-EVD-TRANSFER-CUSTODY | Analyst · Field User (register) · custodian role (custody) | POL-EVD-TRANSFER-CUSTODY | EVT-EVD-CUSTODY-TRANSFERRED | Verification re-evaluator (on WITHDRAWN: issues CMD-CLM-ASSESS as system identity for linked claims, recomputing verification from remaining SUPPORTS links); Search projection (SLC-05) |
| CMD-EVD-RECLASSIFY | Analyst · Field User (register) · custodian role (custody) | POL-EVD-RECLASSIFY | EVT-EVD-RECLASSIFIED | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Verification re-evaluator (on WITHDRAWN: issues CMD-CLM-ASSESS as system identity for linked claims, recomputing verification from remaining SUPPORTS links); Search projection (SLC-05) |
| CMD-EVD-WITHDRAW | Analyst · Field User (register) · custodian role (custody) | POL-EVD-WITHDRAW | EVT-EVD-WITHDRAWN | Verification re-evaluator (on WITHDRAWN: issues CMD-CLM-ASSESS as system identity for linked claims, recomputing verification from remaining SUPPORTS links); Search projection (SLC-05) |

#### AGG-EVIDENCE-LINK — Evidence Link

`03-domain/contexts/BC02/aggregates/AGG-EVIDENCE-LINK.md` · SLC-02 · T1 · بيانات شخصية: لا

```
CAP  CAP-03.02
 └ UC   UC-006
    └ REQ  REQ-INF-021
       └ AGG-EVIDENCE-LINK
          ├ INV  INV-EVL-01, INV-EVL-02
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  —
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-02/evidence-link-state-machine.md
```

**الحالات:** غير نهائية: ACTIVE · نهائية: REMOVED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-EVL-LINK | Analyst | POL-EVL-LINK | EVT-EVL-LINKED | Search/Graph projections (SLC-05) |
| CMD-EVL-UNLINK | Analyst | POL-EVL-UNLINK | EVT-EVL-UNLINKED | Search/Graph projections (SLC-05) |

#### AGG-EXTERNAL-ID — External Identifier Mapping

`03-domain/contexts/BC02/aggregates/AGG-EXTERNAL-ID.md` · SLC-02 · T2 · بيانات شخصية: لا

```
CAP  CAP-03.01
 └ UC   —
    └ REQ  REQ-INF-036
       └ AGG-EXTERNAL-ID
          ├ INV  INV-EXT-01, INV-EXT-02
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-EXT-RESOLVE
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-02/external-id-state-machine.md
```

**الحالات:** غير نهائية: ACTIVE · نهائية: ENDED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-EXT-MAP | adapter service account · Analyst | POL-EXT-MAP | EVT-EXT-MAPPED | Import worker cache |
| CMD-EXT-END | adapter service account · Analyst | POL-EXT-END | EVT-EXT-ENDED | Import worker cache |

> لا Use Case مرتبط بهذا الـAggregate عبر متطلباته. راجع §5 في [bc02-information-core.md](bc02-information-core.md) وCONFLICT-05 قبل اعتباره فجوة.

#### AGG-IMPORT-BATCH — Import Batch

`03-domain/contexts/BC02/aggregates/AGG-IMPORT-BATCH.md` · SLC-02 · T2 · بيانات شخصية: لا

```
CAP  CAP-02.04
 └ UC   UC-094
    └ REQ  REQ-INF-005, REQ-INF-006, REQ-INF-007, REQ-INF-008, REQ-INF-009
       └ AGG-IMPORT-BATCH
          ├ INV  INV-IMP-01, INV-IMP-02, INV-IMP-03, INV-IMP-04
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-IMP-GET
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-02/import-batch-state-machine.md
```

**الحالات:** غير نهائية: RECEIVED, PROCESSING, COMPLETED_WITH_QUARANTINE · نهائية: COMPLETED, FAILED, CANCELLED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-IMP-SUBMIT | adapter service account · Administrator | POL-IMP-SUBMIT | EVT-IMP-RECEIVED | Import worker; Adapter owner notification |
| CMD-IMP-REPROCESS-QUARANTINE | adapter service account · Administrator | POL-IMP-REPROCESS-QUARANTINE | EVT-IMP-REPROCESSING | Import worker; Adapter owner notification |
| CMD-IMP-ACCEPT-QUARANTINE | adapter service account · Administrator | POL-IMP-ACCEPT-QUARANTINE | EVT-IMP-QUARANTINE-ACCEPTED | Import worker; Adapter owner notification |
| CMD-IMP-CANCEL | adapter service account · Administrator | POL-IMP-CANCEL | EVT-IMP-CANCELLED | Import worker; Adapter owner notification |

#### AGG-MATCH-RULESET — Match Ruleset

`03-domain/contexts/BC02/aggregates/AGG-MATCH-RULESET.md` · SLC-04 · T2 · بيانات شخصية: لا

```
CAP  CAP-03.01, CAP-03.05
 └ UC   UC-007, UC-097
    └ REQ  REQ-INF-032, REQ-SRC-003
       └ AGG-MATCH-RULESET
          ├ INV  INV-MRS-01, INV-MRS-02, INV-MRS-03
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-MRS-GET
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-04/match-ruleset-state-machine.md
```

**الحالات:** غير نهائية: DRAFT, ACTIVE · نهائية: SUPERSEDED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-MRS-DRAFT | Analyst lead (draft, edit) · Administrator ≠ author (activate) | POL-MRS-DRAFT | EVT-MRS-DRAFTED | Candidate generator (reloads ruleset) |
| CMD-MRS-EDIT | Analyst lead (draft, edit) · Administrator ≠ author (activate) | POL-MRS-EDIT | EVT-MRS-EDITED | Candidate generator (reloads ruleset) |
| CMD-MRS-ACTIVATE | Analyst lead (draft, edit) · Administrator ≠ author (activate) | POL-MRS-ACTIVATE | EVT-MRS-ACTIVATED | Candidate generator (reloads ruleset) |

#### AGG-OBSERVATION — Observation

`03-domain/contexts/BC02/aggregates/AGG-OBSERVATION.md` · SLC-02 · T1 · بيانات شخصية: لا

```
CAP  CAP-02.03, CAP-03.03
 └ UC   UC-005
    └ REQ  REQ-INF-002, REQ-INF-028
       └ AGG-OBSERVATION
          ├ INV  INV-OBS-01, INV-OBS-02, INV-OBS-03, INV-OBS-04
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-OBS-GET, QRY-OBS-LIST
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-02/observation-state-machine.md
```

**الحالات:** غير نهائية: RECORDED · نهائية: VALIDATED, REJECTED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-OBS-RECORD | Field User / Operator / Analyst / adapter service account (record) · Analyst (validate, reject) | POL-OBS-RECORD | EVT-OBS-RECORDED | Derived-claim processor (position summarization); Situation membership (SLC-06); Search projection (SLC-05) |
| CMD-OBS-AMEND | Field User / Operator / Analyst / adapter service account (record) · Analyst (validate, reject) | POL-OBS-AMEND | EVT-OBS-AMENDED | Derived-claim processor (position summarization); Situation membership (SLC-06); Search projection (SLC-05) |
| CMD-OBS-ATTACH-EVIDENCE | Field User / Operator / Analyst / adapter service account (record) · Analyst (validate, reject) | POL-OBS-ATTACH-EVIDENCE | EVT-OBS-EVIDENCE-ATTACHED | Derived-claim processor (position summarization); Situation membership (SLC-06); Search projection (SLC-05) |
| CMD-OBS-RECLASSIFY | Field User / Operator / Analyst / adapter service account (record) · Analyst (validate, reject) | POL-OBS-RECLASSIFY | EVT-OBS-RECLASSIFIED | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Derived-claim processor (position summarization); Situation membership (SLC-06); Search projection (SLC-05) |
| CMD-OBS-VALIDATE | Field User / Operator / Analyst / adapter service account (record) · Analyst (validate, reject) | POL-OBS-VALIDATE | EVT-OBS-VALIDATED | Derived-claim processor (position summarization); Situation membership (SLC-06); Search projection (SLC-05) |
| CMD-OBS-REJECT | Field User / Operator / Analyst / adapter service account (record) · Analyst (validate, reject) | POL-OBS-REJECT | EVT-OBS-REJECTED | Derived-claim processor (position summarization); Situation membership (SLC-06); Search projection (SLC-05) |

#### AGG-REALWORLD-EVENT — Real-World Event (identity)

`03-domain/contexts/BC02/aggregates/AGG-REALWORLD-EVENT.md` · SLC-02 · T2 identity; attributes T1 · بيانات شخصية: لا

```
CAP  CAP-03.01
 └ UC   UC-001, UC-002, UC-003
    └ REQ  REQ-INF-020
       └ AGG-REALWORLD-EVENT
          ├ INV  INV-RWE-01, INV-RWE-02
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-RWE-GET
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-02/realworld-event-state-machine.md
```

**الحالات:** غير نهائية: ACTIVE, RETIRED · نهائية: — (perpetual)

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-RWE-REGISTER | Analyst · adapter service account | POL-RWE-REGISTER | EVT-RWE-REGISTERED | Search/Graph projections (SLC-05) |
| CMD-RWE-CHANGE-TYPE | Analyst · adapter service account | POL-RWE-CHANGE-TYPE | EVT-RWE-TYPE-CHANGED | Search/Graph projections (SLC-05) |
| CMD-RWE-RECLASSIFY | Analyst · adapter service account | POL-RWE-RECLASSIFY | EVT-RWE-RECLASSIFIED | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Graph projections (SLC-05) |
| CMD-RWE-RETIRE | Analyst · adapter service account | POL-RWE-RETIRE | EVT-RWE-RETIRED | Search/Graph projections (SLC-05) |
| CMD-RWE-REINSTATE | Analyst · adapter service account | POL-RWE-REINSTATE | EVT-RWE-REINSTATED | Search/Graph projections (SLC-05) |

#### AGG-RELATIONSHIP — Relationship (identity)

`03-domain/contexts/BC02/aggregates/AGG-RELATIONSHIP.md` · SLC-02 · T1 · بيانات شخصية: لا

```
CAP  CAP-03.01
 └ UC   UC-003
    └ REQ  REQ-INF-027
       └ AGG-RELATIONSHIP
          ├ INV  INV-REL-01, INV-REL-02
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-REL-LIST
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-02/relationship-state-machine.md
```

**الحالات:** غير نهائية: ACTIVE, RETIRED · نهائية: — (perpetual)

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-REL-REGISTER | Analyst · adapter service account | POL-REL-REGISTER | EVT-REL-REGISTERED | Search/Graph projections (SLC-05) |
| CMD-REL-RECLASSIFY | Analyst · adapter service account | POL-REL-RECLASSIFY | EVT-REL-RECLASSIFIED | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Graph projections (SLC-05) |
| CMD-REL-RETIRE | Analyst · adapter service account | POL-REL-RETIRE | EVT-REL-RETIRED | Search/Graph projections (SLC-05) |
| CMD-REL-REINSTATE | Analyst · adapter service account | POL-REL-REINSTATE | EVT-REL-REINSTATED | Search/Graph projections (SLC-05) |

#### AGG-SOURCE — Source

`03-domain/contexts/BC02/aggregates/AGG-SOURCE.md` · SLC-02 · T1 reliability / T2 profile · بيانات شخصية: لا

```
CAP  CAP-02.02
 └ UC   UC-004, UC-095
    └ REQ  REQ-INF-001
       └ AGG-SOURCE
          ├ INV  INV-SRC-01, INV-SRC-02, INV-SRC-03, INV-SRC-04
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-SRC-GET
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-02/source-state-machine.md
```

**الحالات:** غير نهائية: ACTIVE, SUSPENDED · نهائية: RETIRED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-SRC-REGISTER | Analyst (register, rate, profile) · Security Officer (protection, reclassify) | POL-SRC-REGISTER | EVT-SRC-REGISTERED | Search/Graph projections (SLC-05) |
| CMD-SRC-RATE-RELIABILITY | Analyst (register, rate, profile) · Security Officer (protection, reclassify) | POL-SRC-RATE-RELIABILITY | EVT-SRC-RELIABILITY-RATED | Search/Graph projections (SLC-05) |
| CMD-SRC-UPDATE-PROFILE | Analyst (register, rate, profile) · Security Officer (protection, reclassify) | POL-SRC-UPDATE-PROFILE | EVT-SRC-PROFILE-UPDATED | Search/Graph projections (SLC-05) |
| CMD-SRC-SET-PROTECTION | Analyst (register, rate, profile) · Security Officer (protection, reclassify) | POL-SRC-SET-PROTECTION | EVT-SRC-PROTECTION-CHANGED | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Graph projections (SLC-05) |
| CMD-SRC-RECLASSIFY | Analyst (register, rate, profile) · Security Officer (protection, reclassify) | POL-SRC-RECLASSIFY | EVT-SRC-RECLASSIFIED | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Graph projections (SLC-05) |
| CMD-SRC-SUSPEND | Analyst (register, rate, profile) · Security Officer (protection, reclassify) | POL-SRC-SUSPEND | EVT-SRC-SUSPENDED | Search/Graph projections (SLC-05) |
| CMD-SRC-REINSTATE | Analyst (register, rate, profile) · Security Officer (protection, reclassify) | POL-SRC-REINSTATE | EVT-SRC-REINSTATED | Search/Graph projections (SLC-05) |
| CMD-SRC-RETIRE | Analyst (register, rate, profile) · Security Officer (protection, reclassify) | POL-SRC-RETIRE | EVT-SRC-RETIRED | Search/Graph projections (SLC-05) |

### 21.6 BC03 — [bc03-situational-awareness.md](bc03-situational-awareness.md)

9 Aggregate. التهديدات المرتبطة آليًا بـAggregates هذا الـBC: THR-S06-01. القائمة اليدوية الكاملة في §12 من ملفه.

استعلامات في ملفات BC03 لم تُطابَق مع Aggregate بالبادئة: QRY-BASE-TILE, QRY-SCN-COMPARE.

#### AGG-ALERT — Alert

`03-domain/contexts/BC03/aggregates/AGG-ALERT.md` · SLC-06 · T2 · بيانات شخصية: لا

```
CAP  CAP-05.02
 └ UC   UC-023
    └ REQ  REQ-SIT-004, REQ-SIT-005, REQ-SIT-006
       └ AGG-ALERT
          ├ INV  INV-ALR-01, INV-ALR-02, INV-ALR-03
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-ALR-LIST
          ├ THR  THR-S06-01
          └ TEST 13-verification/acceptance/SLC-06/alert-state-machine.md
```

**الحالات:** غير نهائية: RAISED, ACKNOWLEDGED · نهائية: RESOLVED, DISMISSED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-ALR-ACKNOWLEDGE | recipient | POL-ALR-ACKNOWLEDGE | EVT-ALR-ACKNOWLEDGED | Notification fan-out (recipients = cleared subscribers); COP (alerts layer); Escalation scheduler |
| CMD-ALR-RESOLVE | recipient | POL-ALR-RESOLVE | EVT-ALR-RESOLVED | Notification fan-out (recipients = cleared subscribers); COP (alerts layer); Escalation scheduler |
| CMD-ALR-DISMISS | recipient | POL-ALR-DISMISS | EVT-ALR-DISMISSED | Notification fan-out (recipients = cleared subscribers); COP (alerts layer); Escalation scheduler |

#### AGG-ALERT-RULE — Alert Rule

`03-domain/contexts/BC03/aggregates/AGG-ALERT-RULE.md` · SLC-06 · T2 · بيانات شخصية: لا

```
CAP  CAP-05.02
 └ UC   UC-023
    └ REQ  REQ-SIT-004
       └ AGG-ALERT-RULE
          ├ INV  INV-ARL-01, INV-ARL-02, INV-ARL-03
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  —
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-06/alert-rule-state-machine.md
```

**الحالات:** غير نهائية: DRAFT, ACTIVE, DISABLED · نهائية: RETIRED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-ARL-DEFINE | Analyst lead / Manager | POL-ARL-DEFINE | EVT-ARL-DEFINED | Alert evaluator (reload rules) |
| CMD-ARL-EDIT | Analyst lead / Manager | POL-ARL-EDIT | EVT-ARL-EDITED | Alert evaluator (reload rules) |
| CMD-ARL-ACTIVATE | Analyst lead / Manager | POL-ARL-ACTIVATE | EVT-ARL-ACTIVATED | Alert evaluator (reload rules) |
| CMD-ARL-DISABLE | Analyst lead / Manager | POL-ARL-DISABLE | EVT-ARL-DISABLED | Alert evaluator (reload rules) |
| CMD-ARL-ENABLE | Analyst lead / Manager | POL-ARL-ENABLE | EVT-ARL-ENABLED | Alert evaluator (reload rules) |
| CMD-ARL-RETIRE | Analyst lead / Manager | POL-ARL-RETIRE | EVT-ARL-RETIRED | Alert evaluator (reload rules) |

#### AGG-ANALYSIS-CASE — Analysis Case

`03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-CASE.md` · SLC-07 · T2 lifecycle; T1 selections · بيانات شخصية: لا

```
CAP  CAP-04.01
 └ UC   UC-010, UC-011, UC-012, UC-016
    └ REQ  REQ-ANL-001, REQ-ANL-007
       └ AGG-ANALYSIS-CASE
          ├ INV  INV-ACS-01, INV-ACS-02, INV-ACS-03, INV-ACS-04
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-ACS-GET, QRY-ACS-LIST
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-07/analysis-case-state-machine.md
```

**الحالات:** غير نهائية: DRAFT, OPEN, CLOSED · نهائية: CANCELLED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-ACS-CREATE | Analyst (owner) · Security Officer (reclassify) | POL-ACS-CREATE | EVT-ACS-CREATED | Search projection (SLC-05) |
| CMD-ACS-DEFINE | Analyst (owner) · Security Officer (reclassify) | POL-ACS-DEFINE | EVT-ACS-DEFINED | Search projection (SLC-05) |
| CMD-ACS-OPEN | Analyst (owner) · Security Officer (reclassify) | POL-ACS-OPEN | EVT-ACS-OPENED | Search projection (SLC-05) |
| CMD-ACS-ADD-HYPOTHESIS | Analyst (owner) · Security Officer (reclassify) | POL-ACS-ADD-HYPOTHESIS | EVT-ACS-HYPOTHESIS-ADDED | Search projection (SLC-05) |
| CMD-ACS-UPDATE-HYPOTHESIS | Analyst (owner) · Security Officer (reclassify) | POL-ACS-UPDATE-HYPOTHESIS | EVT-ACS-HYPOTHESIS-UPDATED | Search projection (SLC-05) |
| CMD-ACS-ADD-ASSUMPTION | Analyst (owner) · Security Officer (reclassify) | POL-ACS-ADD-ASSUMPTION | EVT-ACS-ASSUMPTION-ADDED | Search projection (SLC-05) |
| CMD-ACS-RETIRE-ASSUMPTION | Analyst (owner) · Security Officer (reclassify) | POL-ACS-RETIRE-ASSUMPTION | EVT-ACS-ASSUMPTION-RETIRED | Search projection (SLC-05) |
| CMD-ACS-SELECT-EVIDENCE | Analyst (owner) · Security Officer (reclassify) | POL-ACS-SELECT-EVIDENCE | EVT-ACS-EVIDENCE-SELECTED | Search projection (SLC-05) |
| CMD-ACS-DESELECT-EVIDENCE | Analyst (owner) · Security Officer (reclassify) | POL-ACS-DESELECT-EVIDENCE | EVT-ACS-EVIDENCE-DESELECTED | Search projection (SLC-05) |
| CMD-ACS-DEFINE-SCENARIO | Analyst (owner) · Security Officer (reclassify) | POL-ACS-DEFINE-SCENARIO | EVT-ACS-SCENARIO-DEFINED | Search projection (SLC-05) |
| CMD-ACS-CLOSE | Analyst (owner) · Security Officer (reclassify) | POL-ACS-CLOSE | EVT-ACS-CLOSED | Search projection (SLC-05) |
| CMD-ACS-REOPEN | Analyst (owner) · Security Officer (reclassify) | POL-ACS-REOPEN | EVT-ACS-REOPENED | Search projection (SLC-05) |
| CMD-ACS-CANCEL | Analyst (owner) · Security Officer (reclassify) | POL-ACS-CANCEL | EVT-ACS-CANCELLED | Search projection (SLC-05) |
| CMD-ACS-RECLASSIFY | Analyst (owner) · Security Officer (reclassify) | POL-ACS-RECLASSIFY | EVT-ACS-RECLASSIFIED | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search projection (SLC-05) |

#### AGG-ANALYSIS-METHOD — Analysis Method Version

`03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-METHOD.md` · SLC-07 · T2 · بيانات شخصية: لا

```
CAP  CAP-04.02
 └ UC   UC-013
    └ REQ  REQ-ANL-002, REQ-ANL-003
       └ AGG-ANALYSIS-METHOD
          ├ INV  INV-AMT-01, INV-AMT-02
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-AMT-LIST
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-07/analysis-method-state-machine.md
```

**الحالات:** غير نهائية: DRAFT, ACTIVE, DEPRECATED · نهائية: RETIRED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-AMT-REGISTER | Analysis lead (register) · second lead or Administrator (activate) | POL-AMT-REGISTER | EVT-AMT-REGISTERED | Job scheduler (image allow-list) |
| CMD-AMT-ACTIVATE | Analysis lead (register) · second lead or Administrator (activate) | POL-AMT-ACTIVATE | EVT-AMT-ACTIVATED | Job scheduler (image allow-list) |
| CMD-AMT-DEPRECATE | Analysis lead (register) · second lead or Administrator (activate) | POL-AMT-DEPRECATE | EVT-AMT-DEPRECATED | Job scheduler (image allow-list) |
| CMD-AMT-RETIRE | Analysis lead (register) · second lead or Administrator (activate) | POL-AMT-RETIRE | EVT-AMT-RETIRED | Job scheduler (image allow-list) |

#### AGG-ANALYSIS-RUN — Analysis Run

`03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-RUN.md` · SLC-07 · T1 results / T2 lifecycle · بيانات شخصية: لا

```
CAP  CAP-03.07, CAP-04.02
 └ UC   UC-013
    └ REQ  REQ-ANL-002, REQ-ANL-003, REQ-ANL-004, REQ-INF-035
       └ AGG-ANALYSIS-RUN
          ├ INV  INV-RUN-01, INV-RUN-02, INV-RUN-03, INV-RUN-04
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-RUN-ARTIFACT, QRY-RUN-GET
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-07/analysis-run-state-machine.md
```

**الحالات:** غير نهائية: QUEUED, RUNNING · نهائية: SUCCEEDED, FAILED, CANCELLED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-RUN-SUBMIT | Analyst (submit, reproduce, cancel) | POL-RUN-SUBMIT | EVT-RUN-QUEUED | Job scheduler / compute workers; Lineage writer (BC02 LineageRecord); Case owner notification |
| CMD-RUN-REPRODUCE | Analyst (submit, reproduce, cancel) | POL-RUN-REPRODUCE | EVT-RUN-QUEUED | Job scheduler / compute workers; Lineage writer (BC02 LineageRecord); Case owner notification |
| CMD-RUN-CANCEL | Analyst (submit, reproduce, cancel) | POL-RUN-CANCEL | EVT-RUN-CANCELLED | Job scheduler / compute workers; Lineage writer (BC02 LineageRecord); Case owner notification |

#### AGG-ASSESSMENT — Assessment Version

`03-domain/contexts/BC03/aggregates/AGG-ASSESSMENT.md` · SLC-07 · T1 content / T2 lifecycle · بيانات شخصية: لا

```
CAP  CAP-04.03
 └ UC   UC-014, UC-015
    └ REQ  REQ-ANL-005, REQ-ANL-006, REQ-ANL-008
       └ AGG-ASSESSMENT
          ├ INV  INV-ASM-01, INV-ASM-02, INV-ASM-03, INV-ASM-04
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-ASM-GET, QRY-ASM-VERSIONS
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-07/assessment-state-machine.md
```

**الحالات:** غير نهائية: DRAFT, IN_REVIEW, PUBLISHED · نهائية: SUPERSEDED, WITHDRAWN, DISCARDED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-ASM-DRAFT | Analyst (draft, edit, submit, discard) · reviewer / Analysis lead (return, publish, withdraw) | POL-ASM-DRAFT | EVT-ASM-DRAFTED | Decision requests (SLC-08: pinned references); Situation membership (assessment layer); Search projection (SLC-05); Products (SLC-12, R2) |
| CMD-ASM-EDIT | Analyst (draft, edit, submit, discard) · reviewer / Analysis lead (return, publish, withdraw) | POL-ASM-EDIT | EVT-ASM-EDITED | Decision requests (SLC-08: pinned references); Situation membership (assessment layer); Search projection (SLC-05); Products (SLC-12, R2) |
| CMD-ASM-SUBMIT | Analyst (draft, edit, submit, discard) · reviewer / Analysis lead (return, publish, withdraw) | POL-ASM-SUBMIT | EVT-ASM-SUBMITTED | Decision requests (SLC-08: pinned references); Situation membership (assessment layer); Search projection (SLC-05); Products (SLC-12, R2) |
| CMD-ASM-RETURN | Analyst (draft, edit, submit, discard) · reviewer / Analysis lead (return, publish, withdraw) | POL-ASM-RETURN | EVT-ASM-RETURNED | Decision requests (SLC-08: pinned references); Situation membership (assessment layer); Search projection (SLC-05); Products (SLC-12, R2) |
| CMD-ASM-PUBLISH | Analyst (draft, edit, submit, discard) · reviewer / Analysis lead (return, publish, withdraw) | POL-ASM-PUBLISH | EVT-ASM-PUBLISHED | Decision requests (SLC-08: pinned references); Situation membership (assessment layer); Search projection (SLC-05); Products (SLC-12, R2) |
| CMD-ASM-WITHDRAW | Analyst (draft, edit, submit, discard) · reviewer / Analysis lead (return, publish, withdraw) | POL-ASM-WITHDRAW | EVT-ASM-WITHDRAWN | Decision requests (SLC-08: pinned references); Situation membership (assessment layer); Search projection (SLC-05); Products (SLC-12, R2) |
| CMD-ASM-DISCARD | Analyst (draft, edit, submit, discard) · reviewer / Analysis lead (return, publish, withdraw) | POL-ASM-DISCARD | EVT-ASM-DISCARDED | Decision requests (SLC-08: pinned references); Situation membership (assessment layer); Search projection (SLC-05); Products (SLC-12, R2) |

#### AGG-CAP-MESSAGE — CAP Message (outbound)

`03-domain/contexts/BC03/aggregates/AGG-CAP-MESSAGE.md` · SLC-16 · T2 · بيانات شخصية: لا

```
CAP  CAP-10.01
 └ UC   UC-023
    └ REQ  REQ-INT-003
       └ AGG-CAP-MESSAGE
          ├ INV  INV-CAP-01, INV-CAP-02, INV-CAP-03
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-CAP-LIST
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-16/cap-message-state-machine.md
```

**الحالات:** غير نهائية: PREPARED, FAILED · نهائية: SENT, CANCELLED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-CAP-PREPARE | alert recipient / duty officer (prepare) · release authority (release) · operator (retry, cancel) | POL-CAP-PREPARE | EVT-CAP-PREPARED | CAP gateway; Audit |
| CMD-CAP-RELEASE | alert recipient / duty officer (prepare) · release authority (release) · operator (retry, cancel) | POL-CAP-RELEASE | EVT-CAP-SENT | CAP gateway; Audit |
| CMD-CAP-RETRY | alert recipient / duty officer (prepare) · release authority (release) · operator (retry, cancel) | POL-CAP-RETRY | EVT-CAP-RETRY | CAP gateway; Audit |
| CMD-CAP-CANCEL | alert recipient / duty officer (prepare) · release authority (release) · operator (retry, cancel) | POL-CAP-CANCEL | EVT-CAP-CANCELLED | CAP gateway; Audit |

#### AGG-FINDING — Finding

`03-domain/contexts/BC03/aggregates/AGG-FINDING.md` · SLC-07 · T1 · بيانات شخصية: لا

```
CAP  CAP-03.07, CAP-04.03
 └ UC   UC-014, UC-015
    └ REQ  REQ-ANL-005, REQ-INF-035
       └ AGG-FINDING
          ├ INV  INV-FND-01, INV-FND-02
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-FND-LIST
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-07/finding-state-machine.md
```

**الحالات:** غير نهائية: DRAFT, ACCEPTED · نهائية: WITHDRAWN

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-FND-RECORD | Analyst (record, edit, withdraw) · peer Analyst (accept) | POL-FND-RECORD | EVT-FND-RECORDED | Assessment review flags |
| CMD-FND-EDIT | Analyst (record, edit, withdraw) · peer Analyst (accept) | POL-FND-EDIT | EVT-FND-EDITED | Assessment review flags |
| CMD-FND-ACCEPT | Analyst (record, edit, withdraw) · peer Analyst (accept) | POL-FND-ACCEPT | EVT-FND-ACCEPTED | Assessment review flags |
| CMD-FND-WITHDRAW | Analyst (record, edit, withdraw) · peer Analyst (accept) | POL-FND-WITHDRAW | EVT-FND-WITHDRAWN | Assessment review flags |

#### AGG-SITUATION — Situation

`03-domain/contexts/BC03/aggregates/AGG-SITUATION.md` · SLC-06 · T2 definition; content is a projection · بيانات شخصية: لا

```
CAP  CAP-05.01, CAP-05.02, CAP-05.03
 └ UC   UC-020, UC-021, UC-022, UC-024, UC-098
    └ REQ  REQ-SIT-001, REQ-SIT-002, REQ-SIT-003
       └ AGG-SITUATION
          ├ INV  INV-SIT-01, INV-SIT-02, INV-SIT-03, INV-SIT-04
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-SIT-CHANGES, QRY-SIT-COP, QRY-SIT-GET, QRY-SIT-LIST, QRY-SIT-TILE
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-06/situation-state-machine.md
```

**الحالات:** غير نهائية: DRAFT, ACTIVE, PAUSED · نهائية: CLOSED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-SIT-CREATE | Analyst / Manager (create, edit, activate, pause, close) · Security Officer (reclassify) | POL-SIT-CREATE | EVT-SIT-CREATED | Membership evaluator (reload definition); Alert evaluator; Tile cache invalidation; Search projection (SLC-05) |
| CMD-SIT-EDIT-DEFINITION | Analyst / Manager (create, edit, activate, pause, close) · Security Officer (reclassify) | POL-SIT-EDIT-DEFINITION | EVT-SIT-DEFINITION-CHANGED | Membership evaluator (reload definition); Alert evaluator; Tile cache invalidation; Search projection (SLC-05) |
| CMD-SIT-ACTIVATE | Analyst / Manager (create, edit, activate, pause, close) · Security Officer (reclassify) | POL-SIT-ACTIVATE | EVT-SIT-ACTIVATED | Membership evaluator (reload definition); Alert evaluator; Tile cache invalidation; Search projection (SLC-05) |
| CMD-SIT-PAUSE | Analyst / Manager (create, edit, activate, pause, close) · Security Officer (reclassify) | POL-SIT-PAUSE | EVT-SIT-PAUSED | Membership evaluator (reload definition); Alert evaluator; Tile cache invalidation; Search projection (SLC-05) |
| CMD-SIT-RESUME | Analyst / Manager (create, edit, activate, pause, close) · Security Officer (reclassify) | POL-SIT-RESUME | EVT-SIT-RESUMED | Membership evaluator (reload definition); Alert evaluator; Tile cache invalidation; Search projection (SLC-05) |
| CMD-SIT-CLOSE | Analyst / Manager (create, edit, activate, pause, close) · Security Officer (reclassify) | POL-SIT-CLOSE | EVT-SIT-CLOSED | Membership evaluator (reload definition); Alert evaluator; Tile cache invalidation; Search projection (SLC-05) |
| CMD-SIT-RECLASSIFY | Analyst / Manager (create, edit, activate, pause, close) · Security Officer (reclassify) | POL-SIT-RECLASSIFY | EVT-SIT-RECLASSIFIED | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Membership evaluator (reload definition); Alert evaluator; Tile cache invalidation; Search projection (SLC-05) |

### 21.7 BC04 — [bc04-planning-execution.md](bc04-planning-execution.md)

12 Aggregate. التهديدات المرتبطة آليًا بـAggregates هذا الـBC: THR-S03-01, THR-S03-02, THR-S06-02, THR-S15-01, THR-S15-02, THR-S17-01, THR-S17-02, THR-S17-03, THR-S17-04, THR-S17-05. القائمة اليدوية الكاملة في §12 من ملفه.

#### AGG-COORDINATION-CASE — Coordination Case

`03-domain/contexts/BC04/aggregates/AGG-COORDINATION-CASE.md` · SLC-15 · T2 · بيانات شخصية: لا

```
CAP  CAP-06.03
 └ UC   UC-130, UC-131
    └ REQ  REQ-CRD-001, REQ-CRD-002
       └ AGG-COORDINATION-CASE
          ├ INV  INV-CRD-01, INV-CRD-02, INV-CRD-03, INV-CRD-04
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-CRD-GET, QRY-CRD-LIST
          ├ THR  THR-S15-01, THR-S15-02
          └ TEST 13-verification/acceptance/SLC-15/coordination-case-state-machine.md
```

**الحالات:** غير نهائية: OPEN, ACTIVE · نهائية: CLOSED, CANCELLED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-CRD-OPEN | lead organization Manager (open, participants, activate, assign, close, cancel) · participant members (update, request decision) | POL-CRD-OPEN | EVT-CRD-OPENED | Decision requests (SLC-08); Notification (participants); Search projection (SLC-05) |
| CMD-CRD-ADD-PARTICIPANT | lead organization Manager (open, participants, activate, assign, close, cancel) · participant members (update, request decision) | POL-CRD-ADD-PARTICIPANT | EVT-CRD-PARTICIPANT-ADDED | Decision requests (SLC-08); Notification (participants); Search projection (SLC-05) |
| CMD-CRD-REMOVE-PARTICIPANT | lead organization Manager (open, participants, activate, assign, close, cancel) · participant members (update, request decision) | POL-CRD-REMOVE-PARTICIPANT | EVT-CRD-PARTICIPANT-REMOVED | Decision requests (SLC-08); Notification (participants); Search projection (SLC-05) |
| CMD-CRD-ACTIVATE | lead organization Manager (open, participants, activate, assign, close, cancel) · participant members (update, request decision) | POL-CRD-ACTIVATE | EVT-CRD-ACTIVATED | Decision requests (SLC-08); Notification (participants); Search projection (SLC-05) |
| CMD-CRD-ASSIGN-RESPONSIBILITY | lead organization Manager (open, participants, activate, assign, close, cancel) · participant members (update, request decision) | POL-CRD-ASSIGN-RESPONSIBILITY | EVT-CRD-RESPONSIBILITY-ASSIGNED | Decision requests (SLC-08); Notification (participants); Search projection (SLC-05) |
| CMD-CRD-UPDATE-RESPONSIBILITY | lead organization Manager (open, participants, activate, assign, close, cancel) · participant members (update, request decision) | POL-CRD-UPDATE-RESPONSIBILITY | EVT-CRD-RESPONSIBILITY-UPDATED | Decision requests (SLC-08); Notification (participants); Search projection (SLC-05) |
| CMD-CRD-REQUEST-DECISION | lead organization Manager (open, participants, activate, assign, close, cancel) · participant members (update, request decision) | POL-CRD-REQUEST-DECISION | EVT-CRD-DECISION-REQUESTED | Decision requests (SLC-08); Notification (participants); Search projection (SLC-05) |
| CMD-CRD-CLOSE | lead organization Manager (open, participants, activate, assign, close, cancel) · participant members (update, request decision) | POL-CRD-CLOSE | EVT-CRD-CLOSED | Decision requests (SLC-08); Notification (participants); Search projection (SLC-05) |
| CMD-CRD-CANCEL | lead organization Manager (open, participants, activate, assign, close, cancel) · participant members (update, request decision) | POL-CRD-CANCEL | EVT-CRD-CANCELLED | Decision requests (SLC-08); Notification (participants); Search projection (SLC-05) |

#### AGG-DECISION — Decision

`03-domain/contexts/BC04/aggregates/AGG-DECISION.md` · SLC-08 · T2 · بيانات شخصية: لا

```
CAP  CAP-06.02
 └ UC   UC-032
    └ REQ  REQ-DEC-002, REQ-DEC-003, REQ-DEC-004
       └ AGG-DECISION
          ├ INV  INV-DEC-01, INV-DEC-02, INV-DEC-03, INV-DEC-04
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-DEC-BASIS, QRY-DEC-GET
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-08/decision-state-machine.md
```

**الحالات:** غير نهائية: RECORDED · نهائية: SUPERSEDED, ANNULLED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-DEC-RECORD | authority holder (record) · higher authority (annul) | POL-DEC-RECORD | EVT-DEC-RECORDED | Decision request (DECIDED); Plans implementing it (review flag on supersede/annul); Search projection (SLC-05); Audit reports |
| CMD-DEC-ANNUL | authority holder (record) · higher authority (annul) | POL-DEC-ANNUL | EVT-DEC-ANNULLED | Decision request (DECIDED); Plans implementing it (review flag on supersede/annul); Search projection (SLC-05); Audit reports |

#### AGG-DECISION-REQUEST — Decision Request

`03-domain/contexts/BC04/aggregates/AGG-DECISION-REQUEST.md` · SLC-08 · T2 · بيانات شخصية: لا

```
CAP  CAP-06.01
 └ UC   UC-030, UC-031
    └ REQ  REQ-DEC-001
       └ AGG-DECISION-REQUEST
          ├ INV  INV-DRQ-01, INV-DRQ-02, INV-DRQ-03
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-DRQ-GET, QRY-DRQ-LIST
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-08/decision-request-state-machine.md
```

**الحالات:** غير نهائية: DRAFT, OPEN · نهائية: DECIDED, WITHDRAWN

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-DRQ-CREATE | Analyst / Planner / Manager (create, add, cite, open, withdraw) | POL-DRQ-CREATE | EVT-DRQ-CREATED | Search projection (SLC-05) |
| CMD-DRQ-ADD-OPTION | Analyst / Planner / Manager (create, add, cite, open, withdraw) | POL-DRQ-ADD-OPTION | EVT-DRQ-OPTION-ADDED | Search projection (SLC-05) |
| CMD-DRQ-CITE | Analyst / Planner / Manager (create, add, cite, open, withdraw) | POL-DRQ-CITE | EVT-DRQ-CITED | Search projection (SLC-05) |
| CMD-DRQ-OPEN | Analyst / Planner / Manager (create, add, cite, open, withdraw) | POL-DRQ-OPEN | EVT-DRQ-OPENED | Search projection (SLC-05) |
| CMD-DRQ-WITHDRAW | Analyst / Planner / Manager (create, add, cite, open, withdraw) | POL-DRQ-WITHDRAW | EVT-DRQ-WITHDRAWN | Search projection (SLC-05) |

#### AGG-INCIDENT — Incident

`03-domain/contexts/BC04/aggregates/AGG-INCIDENT.md` · SLC-17 · T1 · بيانات شخصية: لا

```
CAP  CAP-09.02, CAP-09.03
 └ UC   UC-142, UC-143, UC-144
    └ REQ  REQ-RCM-006, REQ-RCM-007, REQ-RCM-008, REQ-RCM-009, REQ-RCM-010, REQ-RCM-011, REQ-RCM-012, REQ-RCM-013
       └ AGG-INCIDENT
          ├ INV  INV-INC-01, INV-INC-02, INV-INC-03, INV-INC-04, INV-INC-05
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-INC-GET, QRY-INC-LIST, QRY-INC-RECOVERY-STATUS
          ├ THR  THR-S17-01, THR-S17-02, THR-S17-04
          └ TEST 13-verification/acceptance/SLC-17/incident-state-machine.md
```

**الحالات:** غير نهائية: REPORTED, ASSESSED, RESPONDING, CONTAINED, RESOLVED · نهائية: CLOSED, CANCELLED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-INC-REPORT | أي مُبلِّغ مخوَّل (تبليغ، إلغاء) · مقيّم الحادثة (تقييم) · قائد الحادثة (استجابة، احتواء، حل، إغلاق، تصعيد، تخفيض، تفعيل الاستمرارية) | POL-INC-REPORT | EVT-INC-REPORTED | Search projection (SLC-05); Notification (SLC-06); اقتراحات كائن المعرفة (SLC-12، بعد الإغلاق — R3-Q5) |
| CMD-INC-ASSESS | أي مُبلِّغ مخوَّل (تبليغ، إلغاء) · مقيّم الحادثة (تقييم) · قائد الحادثة (استجابة، احتواء، حل، إغلاق، تصعيد، تخفيض، تفعيل الاستمرارية) | POL-INC-ASSESS | EVT-INC-ASSESSED | Search projection (SLC-05); Notification (SLC-06); اقتراحات كائن المعرفة (SLC-12، بعد الإغلاق — R3-Q5) |
| CMD-INC-DISPATCH-RESPONSE | أي مُبلِّغ مخوَّل (تبليغ، إلغاء) · مقيّم الحادثة (تقييم) · قائد الحادثة (استجابة، احتواء، حل، إغلاق، تصعيد، تخفيض، تفعيل الاستمرارية) | POL-INC-DISPATCH-RESPONSE | EVT-INC-RESPONSE-DISPATCHED | Search projection (SLC-05); Notification (SLC-06); اقتراحات كائن المعرفة (SLC-12، بعد الإغلاق — R3-Q5) |
| CMD-INC-CONTAIN | أي مُبلِّغ مخوَّل (تبليغ، إلغاء) · مقيّم الحادثة (تقييم) · قائد الحادثة (استجابة، احتواء، حل، إغلاق، تصعيد، تخفيض، تفعيل الاستمرارية) | POL-INC-CONTAIN | EVT-INC-CONTAINED | Search projection (SLC-05); Notification (SLC-06); اقتراحات كائن المعرفة (SLC-12، بعد الإغلاق — R3-Q5) |
| CMD-INC-RESOLVE | أي مُبلِّغ مخوَّل (تبليغ، إلغاء) · مقيّم الحادثة (تقييم) · قائد الحادثة (استجابة، احتواء، حل، إغلاق، تصعيد، تخفيض، تفعيل الاستمرارية) | POL-INC-RESOLVE | EVT-INC-RESOLVED | Search projection (SLC-05); Notification (SLC-06); اقتراحات كائن المعرفة (SLC-12، بعد الإغلاق — R3-Q5) |
| CMD-INC-CLOSE | أي مُبلِّغ مخوَّل (تبليغ، إلغاء) · مقيّم الحادثة (تقييم) · قائد الحادثة (استجابة، احتواء، حل، إغلاق، تصعيد، تخفيض، تفعيل الاستمرارية) | POL-INC-CLOSE | EVT-INC-CLOSED | Search projection (SLC-05); Notification (SLC-06); اقتراحات كائن المعرفة (SLC-12، بعد الإغلاق — R3-Q5) |
| CMD-INC-CANCEL | أي مُبلِّغ مخوَّل (تبليغ، إلغاء) · مقيّم الحادثة (تقييم) · قائد الحادثة (استجابة، احتواء، حل، إغلاق، تصعيد، تخفيض، تفعيل الاستمرارية) | POL-INC-CANCEL | EVT-INC-CANCELLED | Search projection (SLC-05); Notification (SLC-06); اقتراحات كائن المعرفة (SLC-12، بعد الإغلاق — R3-Q5) |
| CMD-INC-ESCALATE | أي مُبلِّغ مخوَّل (تبليغ، إلغاء) · مقيّم الحادثة (تقييم) · قائد الحادثة (استجابة، احتواء، حل، إغلاق، تصعيد، تخفيض، تفعيل الاستمرارية) | POL-INC-ESCALATE | EVT-INC-ESCALATED | Search projection (SLC-05); Notification (SLC-06); اقتراحات كائن المعرفة (SLC-12، بعد الإغلاق — R3-Q5) |
| CMD-INC-DE-ESCALATE | أي مُبلِّغ مخوَّل (تبليغ، إلغاء) · مقيّم الحادثة (تقييم) · قائد الحادثة (استجابة، احتواء، حل، إغلاق، تصعيد، تخفيض، تفعيل الاستمرارية) | POL-INC-DE-ESCALATE | EVT-INC-DE-ESCALATED | Search projection (SLC-05); Notification (SLC-06); اقتراحات كائن المعرفة (SLC-12، بعد الإغلاق — R3-Q5) |
| CMD-INC-ACTIVATE-CONTINGENCY | أي مُبلِّغ مخوَّل (تبليغ، إلغاء) · مقيّم الحادثة (تقييم) · قائد الحادثة (استجابة، احتواء، حل، إغلاق، تصعيد، تخفيض، تفعيل الاستمرارية) | POL-INC-ACTIVATE-CONTINGENCY | EVT-INC-CONTINGENCY-ACTIVATED | Search projection (SLC-05); Notification (SLC-06); اقتراحات كائن المعرفة (SLC-12، بعد الإغلاق — R3-Q5) |

#### AGG-NOTIFICATION — Notification

`03-domain/contexts/BC04/aggregates/AGG-NOTIFICATION.md` · SLC-06 · T3 · بيانات شخصية: لا

```
CAP  CAP-10.01
 └ UC   UC-099
    └ REQ  REQ-COM-001, REQ-COM-002
       └ AGG-NOTIFICATION
          ├ INV  INV-NTF-01, INV-NTF-02, INV-NTF-03
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-NTF-INBOX
          ├ THR  THR-S06-02
          └ TEST 13-verification/acceptance/SLC-06/notification-state-machine.md
```

**الحالات:** غير نهائية: QUEUED, SENT · نهائية: READ, FAILED, WITHHELD, EXPIRED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-NTF-MARK-READ | recipient | POL-NTF-MARK-READ | EVT-NTF-READ | Push gateway; In-app inbox |

#### AGG-OUTCOME-TRACKER — Outcome Tracker

`03-domain/contexts/BC04/aggregates/AGG-OUTCOME-TRACKER.md` · SLC-08 · T2 · بيانات شخصية: لا

```
CAP  CAP-07.05
 └ UC   UC-101
    └ REQ  REQ-OPS-013
       └ AGG-OUTCOME-TRACKER
          ├ INV  INV-OUT-01, INV-OUT-02
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-OUT-SERIES
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-08/outcome-tracker-state-machine.md
```

**الحالات:** غير نهائية: ACTIVE · نهائية: CLOSED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-OUT-RECORD | Planner / owner (record, correct) | POL-OUT-RECORD | EVT-OUT-MEASURED | Plan progress view; Business telemetry (OUT-05) |
| CMD-OUT-CORRECT | Planner / owner (record, correct) | POL-OUT-CORRECT | EVT-OUT-MEASUREMENT-CORRECTED | Plan progress view; Business telemetry (OUT-05) |

#### AGG-PLAN — Plan (identity)

`03-domain/contexts/BC04/aggregates/AGG-PLAN.md` · SLC-08 · T2 · بيانات شخصية: لا

```
CAP  CAP-07.01, CAP-07.02
 └ UC   UC-033, UC-035, UC-036
    └ REQ  REQ-OPS-001, REQ-OPS-002, REQ-OPS-003
       └ AGG-PLAN
          ├ INV  INV-PLN-01, INV-PLN-02, INV-PLN-03, INV-PLN-04
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-PLN-GET, QRY-PLN-PROGRESS
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-08/plan-state-machine.md
```

**الحالات:** غير نهائية: DRAFT, ACTIVE, SUSPENDED, COMPLETED · نهائية: CLOSED, CANCELLED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-PLN-CREATE | Planner / owner (create, suspend, resume, complete, close) · authority (cancel) · Security Officer (reclassify) | POL-PLN-CREATE | EVT-PLN-CREATED | Task synchronizer (suspend/cancel cascades); Outcome trackers (close); Notification (owners, assignees) |
| CMD-PLN-SUSPEND | Planner / owner (create, suspend, resume, complete, close) · authority (cancel) · Security Officer (reclassify) | POL-PLN-SUSPEND | EVT-PLN-SUSPENDED | Task synchronizer (suspend/cancel cascades); Outcome trackers (close); Notification (owners, assignees) |
| CMD-PLN-RESUME | Planner / owner (create, suspend, resume, complete, close) · authority (cancel) · Security Officer (reclassify) | POL-PLN-RESUME | EVT-PLN-RESUMED | Task synchronizer (suspend/cancel cascades); Outcome trackers (close); Notification (owners, assignees) |
| CMD-PLN-COMPLETE | Planner / owner (create, suspend, resume, complete, close) · authority (cancel) · Security Officer (reclassify) | POL-PLN-COMPLETE | EVT-PLN-COMPLETED | Task synchronizer (suspend/cancel cascades); Outcome trackers (close); Notification (owners, assignees) |
| CMD-PLN-CLOSE | Planner / owner (create, suspend, resume, complete, close) · authority (cancel) · Security Officer (reclassify) | POL-PLN-CLOSE | EVT-PLN-CLOSED | Task synchronizer (suspend/cancel cascades); Outcome trackers (close); Notification (owners, assignees) |
| CMD-PLN-CANCEL | Planner / owner (create, suspend, resume, complete, close) · authority (cancel) · Security Officer (reclassify) | POL-PLN-CANCEL | EVT-PLN-CANCELLED | Task synchronizer (suspend/cancel cascades); Outcome trackers (close); Notification (owners, assignees) |
| CMD-PLN-RECLASSIFY | Planner / owner (create, suspend, resume, complete, close) · authority (cancel) · Security Officer (reclassify) | POL-PLN-RECLASSIFY | EVT-PLN-RECLASSIFIED | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Task synchronizer (suspend/cancel cascades); Outcome trackers (close); Notification (owners, assignees) |

#### AGG-PLAN-VERSION — Plan Version

`03-domain/contexts/BC04/aggregates/AGG-PLAN-VERSION.md` · SLC-08 · T2 · بيانات شخصية: لا

```
CAP  CAP-07.01, CAP-07.02, CAP-07.04
 └ UC   UC-033, UC-034, UC-035, UC-036, UC-044
    └ REQ  REQ-OPS-001, REQ-OPS-003, REQ-OPS-004, REQ-OPS-005, REQ-OPS-014
       └ AGG-PLAN-VERSION
          ├ INV  INV-PLV-01, INV-PLV-02, INV-PLV-03, INV-PLV-04, INV-PLV-05
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-PLV-DIFF, QRY-PLV-LIST
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-08/plan-version-state-machine.md
```

**الحالات:** غير نهائية: DRAFT, IN_REVIEW, BASELINED · نهائية: SUPERSEDED, REJECTED, DISCARDED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-PLV-DRAFT | Planner (draft, edit, submit, discard, minor amend) · approver with plan-approval authority ≠ author (approve, return, reject) | POL-PLV-DRAFT | EVT-PLV-DRAFTED | Task synchronizer (SPEC-PLAN §3); Outcome trackers; Plan identity (activation); Search projection (SLC-05) |
| CMD-PLV-EDIT | Planner (draft, edit, submit, discard, minor amend) · approver with plan-approval authority ≠ author (approve, return, reject) | POL-PLV-EDIT | EVT-PLV-EDITED | Task synchronizer (SPEC-PLAN §3); Outcome trackers; Plan identity (activation); Search projection (SLC-05) |
| CMD-PLV-SUBMIT | Planner (draft, edit, submit, discard, minor amend) · approver with plan-approval authority ≠ author (approve, return, reject) | POL-PLV-SUBMIT | EVT-PLV-SUBMITTED | Task synchronizer (SPEC-PLAN §3); Outcome trackers; Plan identity (activation); Search projection (SLC-05) |
| CMD-PLV-RETURN | Planner (draft, edit, submit, discard, minor amend) · approver with plan-approval authority ≠ author (approve, return, reject) | POL-PLV-RETURN | EVT-PLV-RETURNED | Task synchronizer (SPEC-PLAN §3); Outcome trackers; Plan identity (activation); Search projection (SLC-05) |
| CMD-PLV-APPROVE | Planner (draft, edit, submit, discard, minor amend) · approver with plan-approval authority ≠ author (approve, return, reject) | POL-PLV-APPROVE | EVT-PLV-BASELINED | Task synchronizer (SPEC-PLAN §3); Outcome trackers; Plan identity (activation); Search projection (SLC-05) |
| CMD-PLV-REJECT | Planner (draft, edit, submit, discard, minor amend) · approver with plan-approval authority ≠ author (approve, return, reject) | POL-PLV-REJECT | EVT-PLV-REJECTED | Task synchronizer (SPEC-PLAN §3); Outcome trackers; Plan identity (activation); Search projection (SLC-05) |
| CMD-PLV-AMEND-MINOR | Planner (draft, edit, submit, discard, minor amend) · approver with plan-approval authority ≠ author (approve, return, reject) | POL-PLV-AMEND-MINOR | EVT-PLV-MINOR-AMENDED | Task synchronizer (SPEC-PLAN §3); Outcome trackers; Plan identity (activation); Search projection (SLC-05) |
| CMD-PLV-DISCARD | Planner (draft, edit, submit, discard, minor amend) · approver with plan-approval authority ≠ author (approve, return, reject) | POL-PLV-DISCARD | EVT-PLV-DISCARDED | Task synchronizer (SPEC-PLAN §3); Outcome trackers; Plan identity (activation); Search projection (SLC-05) |

#### AGG-RISK — Risk

`03-domain/contexts/BC04/aggregates/AGG-RISK.md` · SLC-17 · T2 · بيانات شخصية: لا

```
CAP  CAP-09.01
 └ UC   UC-140, UC-141
    └ REQ  REQ-RCM-001, REQ-RCM-002, REQ-RCM-003, REQ-RCM-004, REQ-RCM-005
       └ AGG-RISK
          ├ INV  INV-RIS-01, INV-RIS-02, INV-RIS-03, INV-RIS-04, INV-RIS-05
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-RIS-GET, QRY-RIS-REGISTER
          ├ THR  THR-S17-03, THR-S17-04
          └ TEST 13-verification/acceptance/SLC-17/risk-state-machine.md
```

**الحالات:** غير نهائية: IDENTIFIED, ASSESSED, TREATED · نهائية: CLOSED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-RIS-IDENTIFY | محدِّد الخطر (تحديد) · مقيّم (تقييم، إعادة تقييم) · موافق المعالجة (تخطيط المعالجة) · مدير المخاطر (إغلاق) | POL-RIS-IDENTIFY | EVT-RIS-IDENTIFIED | Search projection (SLC-05); Coordination cases (SLC-15، عند ارتباط النطاق) |
| CMD-RIS-ASSESS | محدِّد الخطر (تحديد) · مقيّم (تقييم، إعادة تقييم) · موافق المعالجة (تخطيط المعالجة) · مدير المخاطر (إغلاق) | POL-RIS-ASSESS | EVT-RIS-ASSESSED | Search projection (SLC-05); Coordination cases (SLC-15، عند ارتباط النطاق) |
| CMD-RIS-PLAN-TREATMENT | محدِّد الخطر (تحديد) · مقيّم (تقييم، إعادة تقييم) · موافق المعالجة (تخطيط المعالجة) · مدير المخاطر (إغلاق) | POL-RIS-PLAN-TREATMENT | EVT-RIS-TREATMENT-PLANNED | Search projection (SLC-05); Coordination cases (SLC-15، عند ارتباط النطاق) |
| CMD-RIS-REASSESS | محدِّد الخطر (تحديد) · مقيّم (تقييم، إعادة تقييم) · موافق المعالجة (تخطيط المعالجة) · مدير المخاطر (إغلاق) | POL-RIS-REASSESS | EVT-RIS-REASSESSED | Search projection (SLC-05); Coordination cases (SLC-15، عند ارتباط النطاق) |
| CMD-RIS-CLOSE | محدِّد الخطر (تحديد) · مقيّم (تقييم، إعادة تقييم) · موافق المعالجة (تخطيط المعالجة) · مدير المخاطر (إغلاق) | POL-RIS-CLOSE | EVT-RIS-CLOSED | Search projection (SLC-05); Coordination cases (SLC-15، عند ارتباط النطاق) |

#### AGG-SUBSCRIPTION — Subscription

`03-domain/contexts/BC04/aggregates/AGG-SUBSCRIPTION.md` · SLC-06 · T3 · بيانات شخصية: لا

```
CAP  CAP-10.01
 └ UC   UC-099
    └ REQ  REQ-COM-001
       └ AGG-SUBSCRIPTION
          ├ INV  INV-SUB-01, INV-SUB-02
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  —
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-06/subscription-state-machine.md
```

**الحالات:** غير نهائية: ACTIVE, PAUSED · نهائية: ENDED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-SUB-SUBSCRIBE | any user (self) · Administrator (end) | POL-SUB-SUBSCRIBE | EVT-SUB-SUBSCRIBED | Notification fan-out index |
| CMD-SUB-UPDATE-CHANNELS | any user (self) · Administrator (end) | POL-SUB-UPDATE-CHANNELS | EVT-SUB-CHANNELS-UPDATED | Notification fan-out index |
| CMD-SUB-PAUSE | any user (self) · Administrator (end) | POL-SUB-PAUSE | EVT-SUB-PAUSED | Notification fan-out index |
| CMD-SUB-RESUME | any user (self) · Administrator (end) | POL-SUB-RESUME | EVT-SUB-RESUMED | Notification fan-out index |
| CMD-SUB-UNSUBSCRIBE | any user (self) · Administrator (end) | POL-SUB-UNSUBSCRIBE | EVT-SUB-ENDED | Notification fan-out index |

#### AGG-TASK — Task

`03-domain/contexts/BC04/aggregates/AGG-TASK.md` · SLC-03 · T2 · بيانات شخصية: لا

```
CAP  CAP-02.03, CAP-07.03
 └ UC   UC-040, UC-041, UC-042, UC-043, UC-044, UC-045, UC-046, UC-090, UC-102
    └ REQ  REQ-OFF-001, REQ-OPS-006, REQ-OPS-007, REQ-OPS-008, REQ-OPS-009, REQ-OPS-010, REQ-OPS-011, REQ-OPS-012
       └ AGG-TASK
          ├ INV  INV-TASK-01, INV-TASK-02, INV-TASK-03, INV-TASK-04, INV-TASK-05, INV-TASK-06, INV-TASK-07, INV-TASK-08, INV-TASK-09
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-TASK-GET, QRY-TASK-HISTORY, QRY-TASK-LIST
          ├ THR  THR-S03-01, THR-S03-02, THR-S17-05
          └ TEST 13-verification/acceptance/SLC-03/task-state-machine.md
```

**الحالات:** غير نهائية: DRAFT, READY, ASSIGNED, ACCEPTED, IN_PROGRESS, BLOCKED, SUBMITTED, UNDER_REVIEW, APPROVED, COMPLETED · نهائية: CLOSED, CANCELLED, REJECTED, EXPIRED, SUPERSEDED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-TASK-CREATE | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) · assignee (accept, decline, start, block, resume, add result, submit) · reviewer (review, return, approve, reject, complete) | POL-TASK-CREATE | EVT-TASK-CREATED | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) |
| CMD-TASK-EDIT | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) · assignee (accept, decline, start, block, resume, add result, submit) · reviewer (review, return, approve, reject, complete) | POL-TASK-EDIT | EVT-TASK-EDITED | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) |
| CMD-TASK-MARK-READY | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) · assignee (accept, decline, start, block, resume, add result, submit) · reviewer (review, return, approve, reject, complete) | POL-TASK-MARK-READY | EVT-TASK-READIED | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) |
| CMD-TASK-ASSIGN | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) · assignee (accept, decline, start, block, resume, add result, submit) · reviewer (review, return, approve, reject, complete) | POL-TASK-ASSIGN | EVT-TASK-ASSIGNED | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) |
| CMD-TASK-REASSIGN | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) · assignee (accept, decline, start, block, resume, add result, submit) · reviewer (review, return, approve, reject, complete) | POL-TASK-REASSIGN | EVT-TASK-REASSIGNED | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) |
| CMD-TASK-ACCEPT | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) · assignee (accept, decline, start, block, resume, add result, submit) · reviewer (review, return, approve, reject, complete) | POL-TASK-ACCEPT | EVT-TASK-ACCEPTED | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) |
| CMD-TASK-DECLINE | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) · assignee (accept, decline, start, block, resume, add result, submit) · reviewer (review, return, approve, reject, complete) | POL-TASK-DECLINE | EVT-TASK-DECLINED | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) |
| CMD-TASK-START | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) · assignee (accept, decline, start, block, resume, add result, submit) · reviewer (review, return, approve, reject, complete) | POL-TASK-START | EVT-TASK-STARTED | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) |
| CMD-TASK-BLOCK | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) · assignee (accept, decline, start, block, resume, add result, submit) · reviewer (review, return, approve, reject, complete) | POL-TASK-BLOCK | EVT-TASK-BLOCKED | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) |
| CMD-TASK-RESUME | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) · assignee (accept, decline, start, block, resume, add result, submit) · reviewer (review, return, approve, reject, complete) | POL-TASK-RESUME | EVT-TASK-RESUMED | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) |
| CMD-TASK-ADD-RESULT-ITEM | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) · assignee (accept, decline, start, block, resume, add result, submit) · reviewer (review, return, approve, reject, complete) | POL-TASK-ADD-RESULT-ITEM | EVT-TASK-RESULT-ITEM-ADDED | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) |
| CMD-TASK-SUBMIT | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) · assignee (accept, decline, start, block, resume, add result, submit) · reviewer (review, return, approve, reject, complete) | POL-TASK-SUBMIT | EVT-TASK-SUBMITTED | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) |
| CMD-TASK-START-REVIEW | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) · assignee (accept, decline, start, block, resume, add result, submit) · reviewer (review, return, approve, reject, complete) | POL-TASK-START-REVIEW | EVT-TASK-REVIEW-STARTED | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) |
| CMD-TASK-RETURN | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) · assignee (accept, decline, start, block, resume, add result, submit) · reviewer (review, return, approve, reject, complete) | POL-TASK-RETURN | EVT-TASK-RETURNED-FOR-REWORK | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) |
| CMD-TASK-APPROVE | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) · assignee (accept, decline, start, block, resume, add result, submit) · reviewer (review, return, approve, reject, complete) | POL-TASK-APPROVE | EVT-TASK-APPROVED | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) |
| CMD-TASK-REJECT | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) · assignee (accept, decline, start, block, resume, add result, submit) · reviewer (review, return, approve, reject, complete) | POL-TASK-REJECT | EVT-TASK-REJECTED | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) |
| CMD-TASK-COMPLETE | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) · assignee (accept, decline, start, block, resume, add result, submit) · reviewer (review, return, approve, reject, complete) | POL-TASK-COMPLETE | EVT-TASK-COMPLETED | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) |
| CMD-TASK-CLOSE | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) · assignee (accept, decline, start, block, resume, add result, submit) · reviewer (review, return, approve, reject, complete) | POL-TASK-CLOSE | EVT-TASK-CLOSED | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) |
| CMD-TASK-CANCEL | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) · assignee (accept, decline, start, block, resume, add result, submit) · reviewer (review, return, approve, reject, complete) | POL-TASK-CANCEL | EVT-TASK-CANCELLED | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) |
| CMD-TASK-ESCALATE | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) · assignee (accept, decline, start, block, resume, add result, submit) · reviewer (review, return, approve, reject, complete) | POL-TASK-ESCALATE | EVT-TASK-ESCALATED | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) |
| CMD-TASK-SET-DUE | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) · assignee (accept, decline, start, block, resume, add result, submit) · reviewer (review, return, approve, reject, complete) | POL-TASK-SET-DUE | EVT-TASK-DUE-CHANGED | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) |
| CMD-TASK-SUSPEND | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) · assignee (accept, decline, start, block, resume, add result, submit) · reviewer (review, return, approve, reject, complete) | POL-TASK-SUSPEND | EVT-TASK-SUSPENDED | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) |
| CMD-TASK-UNSUSPEND | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) · assignee (accept, decline, start, block, resume, add result, submit) · reviewer (review, return, approve, reject, complete) | POL-TASK-UNSUSPEND | EVT-TASK-UNSUSPENDED | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) |
| CMD-TASK-RECLASSIFY | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) · assignee (accept, decline, start, block, resume, add result, submit) · reviewer (review, return, approve, reject, complete) | POL-TASK-RECLASSIFY | EVT-TASK-RECLASSIFIED | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) |

#### AGG-TASK-TYPE — Task Type

`03-domain/contexts/BC04/aggregates/AGG-TASK-TYPE.md` · SLC-03 · T2 · بيانات شخصية: لا

```
CAP  CAP-07.03, CAP-07.04
 └ UC   UC-034, UC-041, UC-044, UC-102
    └ REQ  REQ-OPS-007, REQ-OPS-014
       └ AGG-TASK-TYPE
          ├ INV  INV-TTY-01, INV-TTY-02, INV-TTY-03
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-TTY-GET
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-03/task-type-state-machine.md
```

**الحالات:** غير نهائية: DRAFT, ACTIVE · نهائية: RETIRED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-TTY-DEFINE | Administrator / Planner lead | POL-TTY-DEFINE | EVT-TTY-DEFINED | Task command handler cache |
| CMD-TTY-EDIT | Administrator / Planner lead | POL-TTY-EDIT | EVT-TTY-EDITED | Task command handler cache |
| CMD-TTY-ACTIVATE | Administrator / Planner lead | POL-TTY-ACTIVATE | EVT-TTY-ACTIVATED | Task command handler cache |
| CMD-TTY-RETIRE | Administrator / Planner lead | POL-TTY-RETIRE | EVT-TTY-RETIRED | Task command handler cache |

### 21.8 BC05 — [bc05-resources-readiness.md](bc05-resources-readiness.md)

13 Aggregate. التهديدات المرتبطة آليًا بـAggregates هذا الـBC: THR-S18-01, THR-S18-02, THR-S18-03, THR-S18-04, THR-S18-05, THR-S19-01, THR-S19-02, THR-S19-03, THR-S19-04, THR-S19-05. القائمة اليدوية الكاملة في §12 من ملفه.

استعلامات في ملفات BC05 لم تُطابَق مع Aggregate بالبادئة: QRY-ELIG-CHECK, QRY-POL-TIMELINE, QRY-READINESS.

#### AGG-ALLOCATION — Resource Allocation

`03-domain/contexts/BC05/aggregates/AGG-ALLOCATION.md` · SLC-09 · T2 · بيانات شخصية: لا

```
CAP  CAP-08.02
 └ UC   UC-053, UC-054, UC-055
    └ REQ  REQ-RES-007, REQ-RES-008, REQ-RES-009, REQ-RES-010, REQ-RES-011, REQ-RES-012
       └ AGG-ALLOCATION
          ├ INV  INV-ALC-01, INV-ALC-02, INV-ALC-03, INV-ALC-04
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-ALC-LIST
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-09/allocation-state-machine.md
```

**الحالات:** غير نهائية: REQUESTED, PENDING_APPROVAL, COMMITTED · نهائية: REJECTED, PREEMPTED, RELEASED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-ALC-REQUEST | Planner (request, release) · allocation authority (approve, reject, pre-empt) · task assignee (consumption) | POL-ALC-REQUEST | EVT-ALC-REQUESTED | Capacity ledger; Task (SLC-03) notifications; Plan progress (SLC-08) |
| CMD-ALC-APPROVE | Planner (request, release) · allocation authority (approve, reject, pre-empt) · task assignee (consumption) | POL-ALC-APPROVE | EVT-ALC-COMMITTED | Capacity ledger; Task (SLC-03) notifications; Plan progress (SLC-08) |
| CMD-ALC-REJECT | Planner (request, release) · allocation authority (approve, reject, pre-empt) · task assignee (consumption) | POL-ALC-REJECT | EVT-ALC-REJECTED | Capacity ledger; Task (SLC-03) notifications; Plan progress (SLC-08) |
| CMD-ALC-RECORD-CONSUMPTION | Planner (request, release) · allocation authority (approve, reject, pre-empt) · task assignee (consumption) | POL-ALC-RECORD-CONSUMPTION | EVT-ALC-CONSUMED | Capacity ledger; Task (SLC-03) notifications; Plan progress (SLC-08) |
| CMD-ALC-PREEMPT | Planner (request, release) · allocation authority (approve, reject, pre-empt) · task assignee (consumption) | POL-ALC-PREEMPT | EVT-ALC-PREEMPTED | Capacity ledger; Task (SLC-03) notifications; Plan progress (SLC-08) |
| CMD-ALC-RELEASE | Planner (request, release) · allocation authority (approve, reject, pre-empt) · task assignee (consumption) | POL-ALC-RELEASE | EVT-ALC-RELEASED | Capacity ledger; Task (SLC-03) notifications; Plan progress (SLC-08) |

#### AGG-ASSET — Asset

`03-domain/contexts/BC05/aggregates/AGG-ASSET.md` · SLC-09 · T2 (location as T1 claims on the linked entity) · بيانات شخصية: لا

```
CAP  CAP-08.01
 └ UC   UC-050, UC-051, UC-053
    └ REQ  REQ-RES-001, REQ-RES-002, REQ-RES-003, REQ-RES-005
       └ AGG-ASSET
          ├ INV  INV-AST-01, INV-AST-02, INV-AST-03, INV-AST-04
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-AST-AVAILABILITY, QRY-AST-GET
          ├ THR  THR-S18-04
          └ TEST 13-verification/acceptance/SLC-09/asset-state-machine.md
```

**الحالات:** غير نهائية: IN_SERVICE, UNSERVICEABLE, UNDER_MAINTENANCE, LOST · نهائية: DISPOSED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-AST-REGISTER | Resource Manager (register, condition, custody, certification, lost) · disposal authority (dispose) · Security Officer (reclassify) | POL-AST-REGISTER | EVT-AST-REGISTERED | Availability view; Situation assets layer (SLC-06); Search projection (SLC-05); Reservations/assignments (flags) |
| CMD-AST-UPDATE-CONDITION | Resource Manager (register, condition, custody, certification, lost) · disposal authority (dispose) · Security Officer (reclassify) | POL-AST-UPDATE-CONDITION | EVT-AST-CONDITION-UPDATED | Availability view; Situation assets layer (SLC-06); Search projection (SLC-05); Reservations/assignments (flags) |
| CMD-AST-MARK-UNSERVICEABLE | Resource Manager (register, condition, custody, certification, lost) · disposal authority (dispose) · Security Officer (reclassify) | POL-AST-MARK-UNSERVICEABLE | EVT-AST-UNSERVICEABLE | Availability view; Situation assets layer (SLC-06); Search projection (SLC-05); Reservations/assignments (flags) |
| CMD-AST-START-MAINTENANCE | Resource Manager (register, condition, custody, certification, lost) · disposal authority (dispose) · Security Officer (reclassify) | POL-AST-START-MAINTENANCE | EVT-AST-MAINTENANCE-STARTED | Availability view; Situation assets layer (SLC-06); Search projection (SLC-05); Reservations/assignments (flags) |
| CMD-AST-RETURN-TO-SERVICE | Resource Manager (register, condition, custody, certification, lost) · disposal authority (dispose) · Security Officer (reclassify) | POL-AST-RETURN-TO-SERVICE | EVT-AST-RETURNED-TO-SERVICE | Availability view; Situation assets layer (SLC-06); Search projection (SLC-05); Reservations/assignments (flags) |
| CMD-AST-FAIL-MAINTENANCE | Resource Manager (register, condition, custody, certification, lost) · disposal authority (dispose) · Security Officer (reclassify) | POL-AST-FAIL-MAINTENANCE | EVT-AST-UNSERVICEABLE | Availability view; Situation assets layer (SLC-06); Search projection (SLC-05); Reservations/assignments (flags) |
| CMD-AST-TRANSFER-CUSTODY | Resource Manager (register, condition, custody, certification, lost) · disposal authority (dispose) · Security Officer (reclassify) | POL-AST-TRANSFER-CUSTODY | EVT-AST-CUSTODY-TRANSFERRED | Availability view; Situation assets layer (SLC-06); Search projection (SLC-05); Reservations/assignments (flags) |
| CMD-AST-SET-CERTIFICATION | Resource Manager (register, condition, custody, certification, lost) · disposal authority (dispose) · Security Officer (reclassify) | POL-AST-SET-CERTIFICATION | EVT-AST-CERTIFICATION-SET | Availability view; Situation assets layer (SLC-06); Search projection (SLC-05); Reservations/assignments (flags) |
| CMD-AST-REPORT-LOST | Resource Manager (register, condition, custody, certification, lost) · disposal authority (dispose) · Security Officer (reclassify) | POL-AST-REPORT-LOST | EVT-AST-REPORTED-LOST | Availability view; Situation assets layer (SLC-06); Search projection (SLC-05); Reservations/assignments (flags) |
| CMD-AST-RECOVER | Resource Manager (register, condition, custody, certification, lost) · disposal authority (dispose) · Security Officer (reclassify) | POL-AST-RECOVER | EVT-AST-RECOVERED | Availability view; Situation assets layer (SLC-06); Search projection (SLC-05); Reservations/assignments (flags) |
| CMD-AST-DISPOSE | Resource Manager (register, condition, custody, certification, lost) · disposal authority (dispose) · Security Officer (reclassify) | POL-AST-DISPOSE | EVT-AST-DISPOSED | Availability view; Situation assets layer (SLC-06); Search projection (SLC-05); Reservations/assignments (flags) |
| CMD-AST-RECLASSIFY | Resource Manager (register, condition, custody, certification, lost) · disposal authority (dispose) · Security Officer (reclassify) | POL-AST-RECLASSIFY | EVT-AST-RECLASSIFIED | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Availability view; Situation assets layer (SLC-06); Search projection (SLC-05); Reservations/assignments (flags) |

#### AGG-ASSET-ASSIGNMENT — Asset Assignment

`03-domain/contexts/BC05/aggregates/AGG-ASSET-ASSIGNMENT.md` · SLC-09 · T2 · بيانات شخصية: لا

```
CAP  CAP-08.01, CAP-08.02
 └ UC   UC-051, UC-053, UC-054
    └ REQ  REQ-RES-003, REQ-RES-012
       └ AGG-ASSET-ASSIGNMENT
          ├ INV  INV-ASG-01, INV-ASG-02
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  —
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-09/asset-assignment-state-machine.md
```

**الحالات:** غير نهائية: ACTIVE · نهائية: RETURNED, CANCELLED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-ASG-ASSIGN | Resource Manager / Planner | POL-ASG-ASSIGN | EVT-ASG-ASSIGNED | Availability view; Task (SLC-03) |
| CMD-ASG-RETURN | Resource Manager / Planner | POL-ASG-RETURN | EVT-ASG-RETURNED | Availability view; Task (SLC-03) |
| CMD-ASG-CANCEL | Resource Manager / Planner | POL-ASG-CANCEL | EVT-ASG-CANCELLED | Availability view; Task (SLC-03) |

#### AGG-ASSET-RESERVATION — Asset Reservation

`03-domain/contexts/BC05/aggregates/AGG-ASSET-RESERVATION.md` · SLC-09 · T2 · بيانات شخصية: لا

```
CAP  CAP-08.01
 └ UC   UC-052
    └ REQ  REQ-RES-014
       └ AGG-ASSET-RESERVATION
          ├ INV  INV-RSV-01, INV-RSV-02
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  —
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-09/asset-reservation-state-machine.md
```

**الحالات:** غير نهائية: HELD, CONFIRMED · نهائية: RELEASED, EXPIRED, CANCELLED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-RSV-HOLD | Planner / Resource Manager | POL-RSV-HOLD | EVT-RSV-HELD | Availability view |
| CMD-RSV-CONFIRM | Planner / Resource Manager | POL-RSV-CONFIRM | EVT-RSV-CONFIRMED | Availability view |
| CMD-RSV-RELEASE | Planner / Resource Manager | POL-RSV-RELEASE | EVT-RSV-RELEASED | Availability view |
| CMD-RSV-CANCEL | Planner / Resource Manager | POL-RSV-CANCEL | EVT-RSV-CANCELLED | Availability view |

#### AGG-EXERCISE — Exercise

`03-domain/contexts/BC05/aggregates/AGG-EXERCISE.md` · SLC-19 · T2 · بيانات شخصية: لا

```
CAP  CAP-08.05
 └ UC   UC-161, UC-162
    └ REQ  REQ-TRX-003, REQ-TRX-004, REQ-TRX-005, REQ-TRX-006, REQ-TRX-007
       └ AGG-EXERCISE
          ├ INV  INV-EXR-01, INV-EXR-02
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-EXR-GET, QRY-EXR-LIST
          ├ THR  THR-S19-01, THR-S19-02
          └ TEST 13-verification/acceptance/SLC-19/exercise-state-machine.md
```

**الحالات:** غير نهائية: PLANNED, SCHEDULED, IN_PROGRESS · نهائية: COMPLETED, ABORTED, CANCELLED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-EXR-PLAN | Exercise Director / Training Manager | POL-EXR-PLAN | EVT-EXR-PLANNED | Search projection (SLC-05) |
| CMD-EXR-SCHEDULE | Exercise Director / Training Manager | POL-EXR-SCHEDULE | EVT-EXR-SCHEDULED | Search projection (SLC-05) |
| CMD-EXR-START | Exercise Director / Training Manager | POL-EXR-START | EVT-EXR-STARTED | Simulation (creation trigger); Search projection (SLC-05) |
| CMD-EXR-CANCEL | Exercise Director / Training Manager | POL-EXR-CANCEL | EVT-EXR-CANCELLED | Search projection (SLC-05) |

#### AGG-LOGISTICS-REQUEST — Logistics Request

`03-domain/contexts/BC05/aggregates/AGG-LOGISTICS-REQUEST.md` · SLC-18 · T2 · بيانات شخصية: لا

```
CAP  CAP-08.03
 └ UC   UC-150, UC-152
    └ REQ  REQ-LOG-001, REQ-LOG-002, REQ-LOG-003, REQ-LOG-008, REQ-LOG-009, REQ-LOG-013, REQ-LOG-014
       └ AGG-LOGISTICS-REQUEST
          ├ INV  INV-LGR-01, INV-LGR-02, INV-LGR-03, INV-LGR-04, INV-LGR-05
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-LGR-GET, QRY-LGR-LIST
          ├ THR  THR-S18-01, THR-S18-02
          └ TEST 13-verification/acceptance/SLC-18/logistics-request-state-machine.md
```

**الحالات:** غير نهائية: REQUESTED, PENDING_APPROVAL, APPROVED, IN_TRANSIT · نهائية: FULFILLED, PARTIALLY_FULFILLED, REJECTED, CANCELLED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-LGR-REQUEST | Logistics Officer / Planner (request, cancel) · dispatcher (dispatch) | POL-LGR-REQUEST | EVT-LGR-REQUESTED | Capacity ledger (via linked allocation, SLC-09); Search projection (SLC-05) |
| CMD-LGR-DISPATCH | Logistics Officer / Planner (request, cancel) · dispatcher (dispatch) | POL-LGR-DISPATCH | EVT-LGR-DISPATCHED | Capacity ledger (via linked allocation, SLC-09); Search projection (SLC-05) |
| CMD-LGR-CANCEL | Logistics Officer / Planner (request, cancel) · dispatcher (dispatch) | POL-LGR-CANCEL | EVT-LGR-CANCELLED | Capacity ledger (via linked allocation, SLC-09); Search projection (SLC-05) |

#### AGG-MAINTENANCE-ORDER — Maintenance Order

`03-domain/contexts/BC05/aggregates/AGG-MAINTENANCE-ORDER.md` · SLC-09 · T2 · بيانات شخصية: لا

```
CAP  CAP-08.01
 └ UC   UC-051
    └ REQ  REQ-RES-004
       └ AGG-MAINTENANCE-ORDER
          ├ INV  INV-MNT-01, INV-MNT-02
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-MNT-SCHEDULE
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-09/maintenance-order-state-machine.md
```

**الحالات:** غير نهائية: PLANNED, IN_PROGRESS · نهائية: COMPLETED, CANCELLED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-MNT-PLAN | Resource Manager / technician | POL-MNT-PLAN | EVT-MNT-PLANNED | Asset (start/return via policy); Availability view |
| CMD-MNT-RESCHEDULE | Resource Manager / technician | POL-MNT-RESCHEDULE | EVT-MNT-RESCHEDULED | Asset (start/return via policy); Availability view |
| CMD-MNT-START | Resource Manager / technician | POL-MNT-START | EVT-MNT-STARTED | Asset (start/return via policy); Availability view |
| CMD-MNT-COMPLETE | Resource Manager / technician | POL-MNT-COMPLETE | EVT-MNT-COMPLETED | Asset (start/return via policy); Availability view |
| CMD-MNT-CANCEL | Resource Manager / technician | POL-MNT-CANCEL | EVT-MNT-CANCELLED | Asset (start/return via policy); Availability view |

#### AGG-QUALIFICATION-RECORD — Qualification Record

`03-domain/contexts/BC05/aggregates/AGG-QUALIFICATION-RECORD.md` · SLC-03 · T2 · بيانات شخصية: نعم

```
CAP  CAP-08.04
 └ UC   UC-102
    └ REQ  REQ-RDY-001, REQ-RDY-002
       └ AGG-QUALIFICATION-RECORD
          ├ INV  INV-QUAL-01, INV-QUAL-02
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-QUAL-LIST
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-03/qualification-record-state-machine.md
```

**الحالات:** غير نهائية: ACTIVE, SUSPENDED · نهائية: EXPIRED, REVOKED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-QUAL-RECORD | Resource Manager / Training Manager | POL-QUAL-RECORD | EVT-QUAL-RECORDED | Eligibility cache invalidation; Task assignment re-check report |
| CMD-QUAL-RENEW | Resource Manager / Training Manager | POL-QUAL-RENEW | EVT-QUAL-RENEWED | Eligibility cache invalidation; Task assignment re-check report |
| CMD-QUAL-SUSPEND | Resource Manager / Training Manager | POL-QUAL-SUSPEND | EVT-QUAL-SUSPENDED | Eligibility cache invalidation; Task assignment re-check report |
| CMD-QUAL-REINSTATE | Resource Manager / Training Manager | POL-QUAL-REINSTATE | EVT-QUAL-REINSTATED | Eligibility cache invalidation; Task assignment re-check report |
| CMD-QUAL-REVOKE | Resource Manager / Training Manager | POL-QUAL-REVOKE | EVT-QUAL-REVOKED | Eligibility cache invalidation; Task assignment re-check report |

#### AGG-RESOURCE-POOL — Resource Pool

`03-domain/contexts/BC05/aggregates/AGG-RESOURCE-POOL.md` · SLC-09 · T2 · بيانات شخصية: لا

```
CAP  CAP-08.02
 └ UC   UC-054
    └ REQ  REQ-RES-006
       └ AGG-RESOURCE-POOL
          ├ INV  INV-RPL-01, INV-RPL-02
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  —
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-09/resource-pool-state-machine.md
```

**الحالات:** غير نهائية: ACTIVE, SUSPENDED · نهائية: CLOSED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-RPL-CREATE | Resource Manager | POL-RPL-CREATE | EVT-RPL-CREATED | Capacity ledger |
| CMD-RPL-ADJUST-CAPACITY | Resource Manager | POL-RPL-ADJUST-CAPACITY | EVT-RPL-CAPACITY-ADJUSTED | Capacity ledger |
| CMD-RPL-SUSPEND | Resource Manager | POL-RPL-SUSPEND | EVT-RPL-SUSPENDED | Capacity ledger |
| CMD-RPL-RESUME | Resource Manager | POL-RPL-RESUME | EVT-RPL-RESUMED | Capacity ledger |
| CMD-RPL-CLOSE | Resource Manager | POL-RPL-CLOSE | EVT-RPL-CLOSED | Capacity ledger |

#### AGG-ROLE-REQUIREMENT — Role Requirement

`03-domain/contexts/BC05/aggregates/AGG-ROLE-REQUIREMENT.md` · SLC-09 · T2 · بيانات شخصية: لا

```
CAP  CAP-08.04
 └ UC   UC-102
    └ REQ  REQ-RES-013
       └ AGG-ROLE-REQUIREMENT
          ├ INV  INV-RRQ-01, INV-RRQ-02
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  —
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-09/role-requirement-state-machine.md
```

**الحالات:** غير نهائية: DRAFT, ACTIVE · نهائية: RETIRED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-RRQ-DEFINE | Training Manager / Administrator | POL-RRQ-DEFINE | EVT-RRQ-DEFINED | Readiness evaluator; Eligibility cache |
| CMD-RRQ-EDIT | Training Manager / Administrator | POL-RRQ-EDIT | EVT-RRQ-EDITED | Readiness evaluator; Eligibility cache |
| CMD-RRQ-ACTIVATE | Training Manager / Administrator | POL-RRQ-ACTIVATE | EVT-RRQ-ACTIVATED | Readiness evaluator; Eligibility cache |
| CMD-RRQ-RETIRE | Training Manager / Administrator | POL-RRQ-RETIRE | EVT-RRQ-RETIRED | Readiness evaluator; Eligibility cache |

#### AGG-SCENARIO — Scenario

`03-domain/contexts/BC05/aggregates/AGG-SCENARIO.md` · SLC-19 · T2 · بيانات شخصية: لا

```
CAP  CAP-08.05
 └ UC   UC-160
    └ REQ  REQ-TRX-001, REQ-TRX-002
       └ AGG-SCENARIO
          ├ INV  INV-SCN-01, INV-SCN-02
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-SCN-GET, QRY-SCN-LIST
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-19/scenario-state-machine.md
```

**الحالات:** غير نهائية: DRAFT, ACTIVE · نهائية: RETIRED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-SCN-DEFINE | Training Manager (define, edit) · Exercise Director (activate, retire) | POL-SCN-DEFINE | EVT-SCN-DEFINED | Search projection (SLC-05) |
| CMD-SCN-EDIT | Training Manager (define, edit) · Exercise Director (activate, retire) | POL-SCN-EDIT | EVT-SCN-EDITED | Search projection (SLC-05) |
| CMD-SCN-ACTIVATE | Training Manager (define, edit) · Exercise Director (activate, retire) | POL-SCN-ACTIVATE | EVT-SCN-ACTIVATED | Exercise (frozen scenario reference on plan); Search projection (SLC-05) |
| CMD-SCN-RETIRE | Training Manager (define, edit) · Exercise Director (activate, retire) | POL-SCN-RETIRE | EVT-SCN-RETIRED | Search projection (SLC-05) |

#### AGG-SHIPMENT — Shipment

`03-domain/contexts/BC05/aggregates/AGG-SHIPMENT.md` · SLC-18 · T2 · بيانات شخصية: لا

```
CAP  CAP-08.03
 └ UC   UC-151, UC-152
    └ REQ  REQ-LOG-004, REQ-LOG-005, REQ-LOG-006, REQ-LOG-007, REQ-LOG-009
       └ AGG-SHIPMENT
          ├ INV  INV-SHP-01, INV-SHP-02, INV-SHP-03, INV-SHP-04
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-SHP-GET, QRY-SHP-LIST, QRY-SHP-TRACKING
          ├ THR  THR-S18-02, THR-S18-03, THR-S18-04, THR-S18-05, THR-S19-05
          └ TEST 13-verification/acceptance/SLC-18/shipment-state-machine.md
```

**الحالات:** غير نهائية: PLANNED, IN_TRANSIT · نهائية: DELIVERED, DAMAGED, LOST, CANCELLED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-SHP-PLAN | dispatcher / carrier operator (plan, depart, checkpoint, deliver, report damage, report lost, cancel) | POL-SHP-PLAN | EVT-SHP-PLANNED | Logistics Request (fulfillment status); Search projection (SLC-05) |
| CMD-SHP-DEPART | dispatcher / carrier operator (plan, depart, checkpoint, deliver, report damage, report lost, cancel) | POL-SHP-DEPART | EVT-SHP-DEPARTED | Logistics Request (fulfillment status); Search projection (SLC-05) |
| CMD-SHP-RECORD-CHECKPOINT | dispatcher / carrier operator (plan, depart, checkpoint, deliver, report damage, report lost, cancel) | POL-SHP-RECORD-CHECKPOINT | EVT-SHP-CHECKPOINT-RECORDED | Logistics Request (fulfillment status); Search projection (SLC-05) |
| CMD-SHP-DELIVER | dispatcher / carrier operator (plan, depart, checkpoint, deliver, report damage, report lost, cancel) | POL-SHP-DELIVER | EVT-SHP-DELIVERED | Logistics Request (fulfillment status); Search projection (SLC-05) |
| CMD-SHP-REPORT-DAMAGE | dispatcher / carrier operator (plan, depart, checkpoint, deliver, report damage, report lost, cancel) | POL-SHP-REPORT-DAMAGE | EVT-SHP-DAMAGED | Logistics Request (fulfillment status); Search projection (SLC-05) |
| CMD-SHP-REPORT-LOST | dispatcher / carrier operator (plan, depart, checkpoint, deliver, report damage, report lost, cancel) | POL-SHP-REPORT-LOST | EVT-SHP-LOST | Logistics Request (fulfillment status); Search projection (SLC-05) |
| CMD-SHP-CANCEL | dispatcher / carrier operator (plan, depart, checkpoint, deliver, report damage, report lost, cancel) | POL-SHP-CANCEL | EVT-SHP-CANCELLED | Logistics Request (fulfillment status); Search projection (SLC-05) |

#### AGG-SIMULATION — Simulation

`03-domain/contexts/BC05/aggregates/AGG-SIMULATION.md` · SLC-19 · T2 · بيانات شخصية: لا

```
CAP  CAP-08.05
 └ UC   UC-162
    └ REQ  REQ-TRX-008, REQ-TRX-009, REQ-TRX-010, REQ-TRX-011
       └ AGG-SIMULATION
          ├ INV  INV-SIM-01, INV-SIM-02, INV-SIM-03
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-SIM-GET, QRY-SIM-LIST, QRY-SIM-TIMELINE
          ├ THR  THR-S19-03, THR-S19-04, THR-S19-05
          └ TEST 13-verification/acceptance/SLC-19/simulation-state-machine.md
```

**الحالات:** غير نهائية: IN_PROGRESS, PAUSED · نهائية: COMPLETED, ABORTED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-SIM-START | system (workload identity, invoked by CMD-EXR-START in the same unit of work) | POL-SIM-START | EVT-SIM-STARTED | Exercise (IN_PROGRESS trigger); Search projection (SLC-05) |
| CMD-SIM-DELIVER-INJECT | Exercise Controller (start, deliver-inject, pause, resume, complete, abort) · Evaluator (record-evaluation) | POL-SIM-DELIVER-INJECT | EVT-SIM-INJECT-DELIVERED | Search projection (SLC-05) |
| CMD-SIM-RECORD-EVALUATION | Exercise Controller (start, deliver-inject, pause, resume, complete, abort) · Evaluator (record-evaluation) | POL-SIM-RECORD-EVALUATION | EVT-SIM-EVALUATION-RECORDED | Qualification Record (optional evidence source, SLC-03 — unmodified, evidence:urn already generic); Search projection (SLC-05) |
| CMD-SIM-PAUSE | Exercise Controller (start, deliver-inject, pause, resume, complete, abort) · Evaluator (record-evaluation) | POL-SIM-PAUSE | EVT-SIM-PAUSED | Search projection (SLC-05) |
| CMD-SIM-RESUME | Exercise Controller (start, deliver-inject, pause, resume, complete, abort) · Evaluator (record-evaluation) | POL-SIM-RESUME | EVT-SIM-RESUMED | Search projection (SLC-05) |
| CMD-SIM-COMPLETE | Exercise Controller (start, deliver-inject, pause, resume, complete, abort) · Evaluator (record-evaluation) | POL-SIM-COMPLETE | EVT-SIM-COMPLETED | Exercise (COMPLETED trigger); Knowledge Object (optional AAR terminal source, SLC-12 — CR-63); Search projection (SLC-05) |
| CMD-SIM-ABORT | Exercise Controller (start, deliver-inject, pause, resume, complete, abort) · Evaluator (record-evaluation) | POL-SIM-ABORT | EVT-SIM-ABORTED | Exercise (ABORTED trigger); Search projection (SLC-05) |

### 21.9 BC06 — [bc06-knowledge-products.md](bc06-knowledge-products.md)

6 Aggregate. التهديدات المرتبطة آليًا بـAggregates هذا الـBC: —. القائمة اليدوية الكاملة في §12 من ملفه.

#### AGG-ARCHIVE-PACKAGE — Archive Package (AIP)

`03-domain/contexts/BC06/aggregates/AGG-ARCHIVE-PACKAGE.md` · SLC-12 · T1 · بيانات شخصية: لا

```
CAP  CAP-11.03
 └ UC   UC-063, UC-064
    └ REQ  REQ-ARC-001, REQ-ARC-002, REQ-ARC-003
       └ AGG-ARCHIVE-PACKAGE
          ├ INV  INV-ARC-01, INV-ARC-02, INV-ARC-03, INV-ARC-04
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-ARC-RETRIEVE, QRY-ARC-SEARCH
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-12/archive-package-state-machine.md
```

**الحالات:** غير نهائية: INGESTING, INGEST_FAILED, ARCHIVED, INTEGRITY_FAILED · نهائية: TRANSFERRED, DISPOSED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-ARC-RETRY-INGEST | Archivist (retry, repair, migrate) · transfer authority (transfer) | POL-ARC-RETRY-INGEST | EVT-ARC-INGEST-STARTED | Archive catalogue; Disposition (SLC-12a); Audit |
| CMD-ARC-REPAIR | Archivist (retry, repair, migrate) · transfer authority (transfer) | POL-ARC-REPAIR | EVT-ARC-REPAIRED | Archive catalogue; Disposition (SLC-12a); Audit |
| CMD-ARC-MIGRATE-FORMAT | Archivist (retry, repair, migrate) · transfer authority (transfer) | POL-ARC-MIGRATE-FORMAT | EVT-ARC-FORMAT-MIGRATED | Archive catalogue; Disposition (SLC-12a); Audit |
| CMD-ARC-TRANSFER | Archivist (retry, repair, migrate) · transfer authority (transfer) | POL-ARC-TRANSFER | EVT-ARC-TRANSFERRED | Archive catalogue; Disposition (SLC-12a); Audit |

#### AGG-DISTRIBUTION — Distribution

`03-domain/contexts/BC06/aggregates/AGG-DISTRIBUTION.md` · SLC-12 · T2 · بيانات شخصية: لا

```
CAP  CAP-10.02
 └ UC   UC-112
    └ REQ  REQ-PRD-004, REQ-PRD-005
       └ AGG-DISTRIBUTION
          ├ INV  INV-DST-01, INV-DST-02, INV-DST-03
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-DST-LOG
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-12/distribution-state-machine.md
```

**الحالات:** غير نهائية: PREPARING · نهائية: COMPLETED, COMPLETED_WITH_EXCLUSIONS, CANCELLED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-DST-DISTRIBUTE | Manager / product owner | POL-DST-DISTRIBUTE | EVT-DST-STARTED | Notification (recipients); Audit |
| CMD-DST-CANCEL | Manager / product owner | POL-DST-CANCEL | EVT-DST-CANCELLED | Notification (recipients); Audit |

#### AGG-KNOWLEDGE-OBJECT — Knowledge Object Version

`03-domain/contexts/BC06/aggregates/AGG-KNOWLEDGE-OBJECT.md` · SLC-12 · T1 content / T2 lifecycle · بيانات شخصية: لا

```
CAP  CAP-11.01
 └ UC   UC-060, UC-061, UC-062
    └ REQ  REQ-KNW-001, REQ-KNW-002, REQ-KNW-003
       └ AGG-KNOWLEDGE-OBJECT
          ├ INV  INV-KNO-01, INV-KNO-02, INV-KNO-03
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-KNO-SEARCH, QRY-KNO-SUGGEST
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-12/knowledge-object-state-machine.md
```

**الحالات:** غير نهائية: DRAFT, IN_REVIEW, PUBLISHED · نهائية: REJECTED, SUPERSEDED, RETIRED, DISCARDED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-KNO-DRAFT | any user (draft lessons) · Knowledge Manager (review, publish, retire) · planner (record reuse) | POL-KNO-DRAFT | EVT-KNO-DRAFTED | Knowledge suggestion index; Search projection (SLC-05); Business telemetry (OUT-06) |
| CMD-KNO-EDIT | any user (draft lessons) · Knowledge Manager (review, publish, retire) · planner (record reuse) | POL-KNO-EDIT | EVT-KNO-EDITED | Knowledge suggestion index; Search projection (SLC-05); Business telemetry (OUT-06) |
| CMD-KNO-SUBMIT | any user (draft lessons) · Knowledge Manager (review, publish, retire) · planner (record reuse) | POL-KNO-SUBMIT | EVT-KNO-SUBMITTED | Knowledge suggestion index; Search projection (SLC-05); Business telemetry (OUT-06) |
| CMD-KNO-RETURN | any user (draft lessons) · Knowledge Manager (review, publish, retire) · planner (record reuse) | POL-KNO-RETURN | EVT-KNO-RETURNED | Knowledge suggestion index; Search projection (SLC-05); Business telemetry (OUT-06) |
| CMD-KNO-PUBLISH | any user (draft lessons) · Knowledge Manager (review, publish, retire) · planner (record reuse) | POL-KNO-PUBLISH | EVT-KNO-PUBLISHED | Knowledge suggestion index; Search projection (SLC-05); Business telemetry (OUT-06) |
| CMD-KNO-REJECT | any user (draft lessons) · Knowledge Manager (review, publish, retire) · planner (record reuse) | POL-KNO-REJECT | EVT-KNO-REJECTED | Knowledge suggestion index; Search projection (SLC-05); Business telemetry (OUT-06) |
| CMD-KNO-RECORD-REUSE | any user (draft lessons) · Knowledge Manager (review, publish, retire) · planner (record reuse) | POL-KNO-RECORD-REUSE | EVT-KNO-REUSED | Knowledge suggestion index; Search projection (SLC-05); Business telemetry (OUT-06) |
| CMD-KNO-RETIRE | any user (draft lessons) · Knowledge Manager (review, publish, retire) · planner (record reuse) | POL-KNO-RETIRE | EVT-KNO-RETIRED | Knowledge suggestion index; Search projection (SLC-05); Business telemetry (OUT-06) |
| CMD-KNO-DISCARD | any user (draft lessons) · Knowledge Manager (review, publish, retire) · planner (record reuse) | POL-KNO-DISCARD | EVT-KNO-DISCARDED | Knowledge suggestion index; Search projection (SLC-05); Business telemetry (OUT-06) |

#### AGG-PRODUCT — Product Version

`03-domain/contexts/BC06/aggregates/AGG-PRODUCT.md` · SLC-12 · T1 content / T2 lifecycle · بيانات شخصية: لا

```
CAP  CAP-10.02
 └ UC   UC-110, UC-111
    └ REQ  REQ-PRD-001, REQ-PRD-002, REQ-PRD-003
       └ AGG-PRODUCT
          ├ INV  INV-PRD-01, INV-PRD-02, INV-PRD-03, INV-PRD-04
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-PRD-GET, QRY-PRD-LIST
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-12/product-state-machine.md
```

**الحالات:** غير نهائية: DRAFT, GENERATING, GENERATED, GENERATION_FAILED, IN_REVIEW, APPROVED · نهائية: SUPERSEDED, WITHDRAWN, DISCARDED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-PRD-CREATE | Analyst / Planner (create, generate, edit, submit, discard) · reviewer (return, approve) · Manager (withdraw) | POL-PRD-CREATE | EVT-PRD-CREATED | Distribution; Search projection (SLC-05); Notification (reviewers) |
| CMD-PRD-GENERATE | Analyst / Planner (create, generate, edit, submit, discard) · reviewer (return, approve) · Manager (withdraw) | POL-PRD-GENERATE | EVT-PRD-GENERATION-STARTED | Distribution; Search projection (SLC-05); Notification (reviewers) |
| CMD-PRD-EDIT-NARRATIVE | Analyst / Planner (create, generate, edit, submit, discard) · reviewer (return, approve) · Manager (withdraw) | POL-PRD-EDIT-NARRATIVE | EVT-PRD-NARRATIVE-EDITED | Distribution; Search projection (SLC-05); Notification (reviewers) |
| CMD-PRD-SUBMIT | Analyst / Planner (create, generate, edit, submit, discard) · reviewer (return, approve) · Manager (withdraw) | POL-PRD-SUBMIT | EVT-PRD-SUBMITTED | Distribution; Search projection (SLC-05); Notification (reviewers) |
| CMD-PRD-RETURN | Analyst / Planner (create, generate, edit, submit, discard) · reviewer (return, approve) · Manager (withdraw) | POL-PRD-RETURN | EVT-PRD-RETURNED | Distribution; Search projection (SLC-05); Notification (reviewers) |
| CMD-PRD-APPROVE | Analyst / Planner (create, generate, edit, submit, discard) · reviewer (return, approve) · Manager (withdraw) | POL-PRD-APPROVE | EVT-PRD-APPROVED | Distribution; Search projection (SLC-05); Notification (reviewers) |
| CMD-PRD-WITHDRAW | Analyst / Planner (create, generate, edit, submit, discard) · reviewer (return, approve) · Manager (withdraw) | POL-PRD-WITHDRAW | EVT-PRD-WITHDRAWN | Distribution; Search projection (SLC-05); Notification (reviewers) |
| CMD-PRD-DISCARD | Analyst / Planner (create, generate, edit, submit, discard) · reviewer (return, approve) · Manager (withdraw) | POL-PRD-DISCARD | EVT-PRD-DISCARDED | Distribution; Search projection (SLC-05); Notification (reviewers) |

#### AGG-PRODUCT-TEMPLATE — Product Template

`03-domain/contexts/BC06/aggregates/AGG-PRODUCT-TEMPLATE.md` · SLC-12 · T2 · بيانات شخصية: لا

```
CAP  CAP-10.02
 └ UC   UC-110
    └ REQ  REQ-PRD-001
       └ AGG-PRODUCT-TEMPLATE
          ├ INV  INV-PTM-01, INV-PTM-02
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  —
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-12/product-template-state-machine.md
```

**الحالات:** غير نهائية: DRAFT, ACTIVE · نهائية: RETIRED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-PTM-DEFINE | Knowledge Manager / Analysis lead (define, edit) · second approver (activate) | POL-PTM-DEFINE | EVT-PTM-DEFINED | Product generator |
| CMD-PTM-EDIT | Knowledge Manager / Analysis lead (define, edit) · second approver (activate) | POL-PTM-EDIT | EVT-PTM-EDITED | Product generator |
| CMD-PTM-ACTIVATE | Knowledge Manager / Analysis lead (define, edit) · second approver (activate) | POL-PTM-ACTIVATE | EVT-PTM-ACTIVATED | Product generator |
| CMD-PTM-RETIRE | Knowledge Manager / Analysis lead (define, edit) · second approver (activate) | POL-PTM-RETIRE | EVT-PTM-RETIRED | Product generator |

#### AGG-RECONSTRUCTION — Historical Reconstruction

`03-domain/contexts/BC06/aggregates/AGG-RECONSTRUCTION.md` · SLC-12 · T2 · بيانات شخصية: لا

```
CAP  CAP-11.03
 └ UC   UC-065
    └ REQ  REQ-ARC-004
       └ AGG-RECONSTRUCTION
          ├ INV  INV-REC-01, INV-REC-02, INV-REC-03
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-REC-REPORT
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-12/reconstruction-state-machine.md
```

**الحالات:** غير نهائية: REQUESTED, RUNNING · نهائية: COMPLETED, FAILED, CANCELLED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-REC-REQUEST | Auditor / Legal / Analyst (request, cancel) | POL-REC-REQUEST | EVT-REC-REQUESTED | Requester notification; Audit |
| CMD-REC-CANCEL | Auditor / Legal / Analyst (request, cancel) | POL-REC-CANCEL | EVT-REC-CANCELLED | Requester notification; Audit |

### 21.10 BC07 — [bc07-integration-ai-discovery.md](bc07-integration-ai-discovery.md)

13 Aggregate. التهديدات المرتبطة آليًا بـAggregates هذا الـBC: THR-S10-02, THR-S11-04. القائمة اليدوية الكاملة في §12 من ملفه.

استعلامات في ملفات BC07 لم تُطابَق مع Aggregate بالبادئة: QRY-AI-USAGE, QRY-GRAPH-NEIGHBORHOOD, QRY-GRAPH-PATHS, QRY-SRCH-QUERY, QRY-SRCH-SUGGEST.

#### AGG-ADAPTER — Adapter

`03-domain/contexts/BC07/aggregates/AGG-ADAPTER.md` · SLC-02 · T2 · بيانات شخصية: لا

```
CAP  CAP-02.04
 └ UC   UC-094
    └ REQ  REQ-INF-005, REQ-INF-008, REQ-INF-009
       └ AGG-ADAPTER
          ├ INV  INV-ADP-01, INV-ADP-02, INV-ADP-03
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-ADP-GET
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-02/adapter-state-machine.md
```

**الحالات:** غير نهائية: DRAFT, ACTIVE, SUSPENDED · نهائية: RETIRED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-ADP-REGISTER | Administrator (register, update) · second Administrator (activate) | POL-ADP-REGISTER | EVT-ADP-REGISTERED | Import worker |
| CMD-ADP-UPDATE-MAPPING | Administrator (register, update) · second Administrator (activate) | POL-ADP-UPDATE-MAPPING | EVT-ADP-MAPPING-UPDATED | Import worker |
| CMD-ADP-ACTIVATE | Administrator (register, update) · second Administrator (activate) | POL-ADP-ACTIVATE | EVT-ADP-ACTIVATED | Import worker |
| CMD-ADP-SUSPEND | Administrator (register, update) · second Administrator (activate) | POL-ADP-SUSPEND | EVT-ADP-SUSPENDED | Import worker |
| CMD-ADP-RESUME | Administrator (register, update) · second Administrator (activate) | POL-ADP-RESUME | EVT-ADP-RESUMED | Import worker |
| CMD-ADP-RETIRE | Administrator (register, update) · second Administrator (activate) | POL-ADP-RETIRE | EVT-ADP-RETIRED | Import worker |

#### AGG-AI-REQUEST — AI Request

`03-domain/contexts/BC07/aggregates/AGG-AI-REQUEST.md` · SLC-10 · T1 (when its output is used) / T2 · بيانات شخصية: لا

```
CAP  CAP-12.01, CAP-12.03
 └ UC   UC-070, UC-071, UC-072, UC-074, UC-077
    └ REQ  REQ-AI-001, REQ-AI-002, REQ-AI-003, REQ-AI-004, REQ-AI-007, REQ-AI-008, REQ-AI-011, REQ-AI-012
       └ AGG-AI-REQUEST
          ├ INV  INV-AIR-01, INV-AIR-02, INV-AIR-03, INV-AIR-04, INV-AIR-05
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-AIR-CONTEXT, QRY-AIR-GET
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-10/ai-request-state-machine.md
```

**الحالات:** غير نهائية: RECEIVED, RETRIEVING, GENERATING · نهائية: COMPLETED, INSUFFICIENT_EVIDENCE, REFUSED, FAILED, CANCELLED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-AIR-SUBMIT | any authorized user (submit, cancel) | POL-AIR-SUBMIT | EVT-AIR-RECEIVED | AI result creator (reviewable operations); Usage accounting; Audit (encrypted prompt/output log) |
| CMD-AIR-CANCEL | any authorized user (submit, cancel) | POL-AIR-CANCEL | EVT-AIR-CANCELLED | AI result creator (reviewable operations); Usage accounting; Audit (encrypted prompt/output log) |

#### AGG-AI-RESULT — AI Result (reviewable)

`03-domain/contexts/BC07/aggregates/AGG-AI-RESULT.md` · SLC-10 · T1 · بيانات شخصية: لا

```
CAP  CAP-12.01, CAP-12.02, CAP-12.03
 └ UC   UC-072, UC-073, UC-074
    └ REQ  REQ-AI-005, REQ-AI-006, REQ-AI-008
       └ AGG-AI-RESULT
          ├ INV  INV-AIRS-01, INV-AIRS-02, INV-AIRS-03
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-AIRS-QUEUE
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-10/ai-result-state-machine.md
```

**الحالات:** غير نهائية: PROPOSED, UNDER_REVIEW · نهائية: ACCEPTED, PARTIALLY_ACCEPTED, REJECTED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-AIRS-START-REVIEW | reviewer authorized on the target (review, accept, reject) | POL-AIRS-START-REVIEW | EVT-AIRS-REVIEW-STARTED | Owner contexts (effects on acceptance); Evaluation feedback store |
| CMD-AIRS-ACCEPT | reviewer authorized on the target (review, accept, reject) | POL-AIRS-ACCEPT | EVT-AIRS-ACCEPTED | Owner contexts (effects on acceptance); Evaluation feedback store |
| CMD-AIRS-ACCEPT-PARTIALLY | reviewer authorized on the target (review, accept, reject) | POL-AIRS-ACCEPT-PARTIALLY | EVT-AIRS-PARTIALLY-ACCEPTED | Owner contexts (effects on acceptance); Evaluation feedback store |
| CMD-AIRS-REJECT | reviewer authorized on the target (review, accept, reject) | POL-AIRS-REJECT | EVT-AIRS-REJECTED | Owner contexts (effects on acceptance); Evaluation feedback store |

#### AGG-AI-ROUTING — AI Routing Configuration

`03-domain/contexts/BC07/aggregates/AGG-AI-ROUTING.md` · SLC-10 · T2 · بيانات شخصية: لا

```
CAP  CAP-12.01
 └ UC   UC-074, UC-077
    └ REQ  REQ-AI-008, REQ-AI-011
       └ AGG-AI-ROUTING
          ├ INV  INV-RTG-01, INV-RTG-02, INV-RTG-03
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-RTG-ACTIVE
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-10/ai-routing-state-machine.md
```

**الحالات:** غير نهائية: DRAFT, ACTIVE · نهائية: SUPERSEDED, DISCARDED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-RTG-DRAFT | AI governance authority (draft, edit) · second authority (activate) | POL-RTG-DRAFT | EVT-RTG-DRAFTED | Model router; PEP cache |
| CMD-RTG-EDIT | AI governance authority (draft, edit) · second authority (activate) | POL-RTG-EDIT | EVT-RTG-EDITED | Model router; PEP cache |
| CMD-RTG-ACTIVATE | AI governance authority (draft, edit) · second authority (activate) | POL-RTG-ACTIVATE | EVT-RTG-ACTIVATED | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Model router; PEP cache |
| CMD-RTG-DISCARD | AI governance authority (draft, edit) · second authority (activate) | POL-RTG-DISCARD | EVT-RTG-DISCARDED | Model router; PEP cache |

#### AGG-AI-TOOL — AI Tool

`03-domain/contexts/BC07/aggregates/AGG-AI-TOOL.md` · SLC-10 · T2 · بيانات شخصية: لا

```
CAP  CAP-12.01
 └ UC   UC-071, UC-077
    └ REQ  REQ-AI-012, REQ-AI-013
       └ AGG-AI-TOOL
          ├ INV  INV-TOL-01, INV-TOL-02, INV-TOL-03
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-TOL-LIST
          ├ THR  THR-S10-02
          └ TEST 13-verification/acceptance/SLC-10/ai-tool-state-machine.md
```

**الحالات:** غير نهائية: DRAFT, ACTIVE, DISABLED · نهائية: RETIRED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-TOL-REGISTER | AI platform engineer (register) · Security Officer (activate, disable) | POL-TOL-REGISTER | EVT-TOL-REGISTERED | Tool gateway |
| CMD-TOL-ACTIVATE | AI platform engineer (register) · Security Officer (activate, disable) | POL-TOL-ACTIVATE | EVT-TOL-ACTIVATED | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Tool gateway |
| CMD-TOL-DISABLE | AI platform engineer (register) · Security Officer (activate, disable) | POL-TOL-DISABLE | EVT-TOL-DISABLED | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Tool gateway |
| CMD-TOL-ENABLE | AI platform engineer (register) · Security Officer (activate, disable) | POL-TOL-ENABLE | EVT-TOL-ENABLED | Tool gateway |
| CMD-TOL-RETIRE | AI platform engineer (register) · Security Officer (activate, disable) | POL-TOL-RETIRE | EVT-TOL-RETIRED | Tool gateway |

#### AGG-EVAL-SUITE — Evaluation Suite

`03-domain/contexts/BC07/aggregates/AGG-EVAL-SUITE.md` · SLC-10 · T2 · بيانات شخصية: لا

```
CAP  CAP-12.04
 └ UC   UC-075, UC-076
    └ REQ  REQ-AI-010
       └ AGG-EVAL-SUITE
          ├ INV  INV-EVS-01, INV-EVS-02
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  —
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-10/eval-suite-state-machine.md
```

**الحالات:** غير نهائية: DRAFT, ACTIVE · نهائية: SUPERSEDED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-EVS-DRAFT | AI governance (draft, edit) · second authority (activate) | POL-EVS-DRAFT | EVT-EVS-DRAFTED | Evaluation runner |
| CMD-EVS-EDIT | AI governance (draft, edit) · second authority (activate) | POL-EVS-EDIT | EVT-EVS-EDITED | Evaluation runner |
| CMD-EVS-ACTIVATE | AI governance (draft, edit) · second authority (activate) | POL-EVS-ACTIVATE | EVT-EVS-ACTIVATED | Evaluation runner |

#### AGG-INTEGRATION-CONNECTION — Integration Connection

`03-domain/contexts/BC07/aggregates/AGG-INTEGRATION-CONNECTION.md` · SLC-16 · T2 · بيانات شخصية: لا

```
CAP  CAP-02.04
 └ UC   UC-094
    └ REQ  REQ-INT-001
       └ AGG-INTEGRATION-CONNECTION
          ├ INV  INV-CON-01, INV-CON-02, INV-CON-03
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-CON-LIST
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-16/integration-connection-state-machine.md
```

**الحالات:** غير نهائية: DRAFT, TESTING, ACTIVE, DEGRADED, SUSPENDED · نهائية: RETIRED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-CON-REGISTER | integration engineer (register, test) · Security Officer ≠ requester (activate) · Administrator (suspend, resume, retire) | POL-CON-REGISTER | EVT-CON-REGISTERED | Egress gateway (allow-list); Adapters (bind/unbind); Operations alerting |
| CMD-CON-TEST | integration engineer (register, test) · Security Officer ≠ requester (activate) · Administrator (suspend, resume, retire) | POL-CON-TEST | EVT-CON-TEST-STARTED | Egress gateway (allow-list); Adapters (bind/unbind); Operations alerting |
| CMD-CON-ACTIVATE | integration engineer (register, test) · Security Officer ≠ requester (activate) · Administrator (suspend, resume, retire) | POL-CON-ACTIVATE | EVT-CON-ACTIVATED | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Egress gateway (allow-list); Adapters (bind/unbind); Operations alerting |
| CMD-CON-FAIL-TEST | integration engineer (register, test) · Security Officer ≠ requester (activate) · Administrator (suspend, resume, retire) | POL-CON-FAIL-TEST | EVT-CON-TEST-FAILED | Egress gateway (allow-list); Adapters (bind/unbind); Operations alerting |
| CMD-CON-SUSPEND | integration engineer (register, test) · Security Officer ≠ requester (activate) · Administrator (suspend, resume, retire) | POL-CON-SUSPEND | EVT-CON-SUSPENDED | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Egress gateway (allow-list); Adapters (bind/unbind); Operations alerting |
| CMD-CON-RESUME | integration engineer (register, test) · Security Officer ≠ requester (activate) · Administrator (suspend, resume, retire) | POL-CON-RESUME | EVT-CON-RESUMED | Egress gateway (allow-list); Adapters (bind/unbind); Operations alerting |
| CMD-CON-RETIRE | integration engineer (register, test) · Security Officer ≠ requester (activate) · Administrator (suspend, resume, retire) | POL-CON-RETIRE | EVT-CON-RETIRED | Egress gateway (allow-list); Adapters (bind/unbind); Operations alerting |

#### AGG-MODEL-VERSION — Model Version

`03-domain/contexts/BC07/aggregates/AGG-MODEL-VERSION.md` · SLC-10 · T2 · بيانات شخصية: لا

```
CAP  CAP-12.04
 └ UC   UC-075, UC-076
    └ REQ  REQ-AI-009, REQ-AI-010
       └ AGG-MODEL-VERSION
          ├ INV  INV-MDL-01, INV-MDL-02, INV-MDL-03
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-MDL-LIST
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-10/model-version-state-machine.md
```

**الحالات:** غير نهائية: REGISTERED, EVALUATING, APPROVED, STAGED, PRODUCTION, DEPRECATED · نهائية: EVALUATION_FAILED, RETIRED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-MDL-REGISTER | AI platform engineer (register, evaluate, stage, deprecate) · AI governance authority (approve, promote, reinstate) | POL-MDL-REGISTER | EVT-MDL-REGISTERED | Inference servers (load/unload); Routing validation |
| CMD-MDL-START-EVALUATION | AI platform engineer (register, evaluate, stage, deprecate) · AI governance authority (approve, promote, reinstate) | POL-MDL-START-EVALUATION | EVT-MDL-EVALUATION-STARTED | Inference servers (load/unload); Routing validation |
| CMD-MDL-APPROVE | AI platform engineer (register, evaluate, stage, deprecate) · AI governance authority (approve, promote, reinstate) | POL-MDL-APPROVE | EVT-MDL-APPROVED | Inference servers (load/unload); Routing validation |
| CMD-MDL-FAIL-EVALUATION | AI platform engineer (register, evaluate, stage, deprecate) · AI governance authority (approve, promote, reinstate) | POL-MDL-FAIL-EVALUATION | EVT-MDL-EVALUATION-FAILED | Inference servers (load/unload); Routing validation |
| CMD-MDL-STAGE | AI platform engineer (register, evaluate, stage, deprecate) · AI governance authority (approve, promote, reinstate) | POL-MDL-STAGE | EVT-MDL-STAGED | Inference servers (load/unload); Routing validation |
| CMD-MDL-PROMOTE | AI platform engineer (register, evaluate, stage, deprecate) · AI governance authority (approve, promote, reinstate) | POL-MDL-PROMOTE | EVT-MDL-PROMOTED | Inference servers (load/unload); Routing validation |
| CMD-MDL-DEPRECATE | AI platform engineer (register, evaluate, stage, deprecate) · AI governance authority (approve, promote, reinstate) | POL-MDL-DEPRECATE | EVT-MDL-DEPRECATED | Inference servers (load/unload); Routing validation |
| CMD-MDL-REINSTATE | AI platform engineer (register, evaluate, stage, deprecate) · AI governance authority (approve, promote, reinstate) | POL-MDL-REINSTATE | EVT-MDL-REINSTATED | Inference servers (load/unload); Routing validation |
| CMD-MDL-RETIRE | AI platform engineer (register, evaluate, stage, deprecate) · AI governance authority (approve, promote, reinstate) | POL-MDL-RETIRE | EVT-MDL-RETIRED | Inference servers (load/unload); Routing validation |

#### AGG-PRELOAD-PACKAGE — Preload Package

`03-domain/contexts/BC07/aggregates/AGG-PRELOAD-PACKAGE.md` · SLC-11 · T2 · بيانات شخصية: لا

```
CAP  CAP-02.03
 └ UC   UC-090, UC-093
    └ REQ  REQ-OFF-002, REQ-OFF-005
       └ AGG-PRELOAD-PACKAGE
          ├ INV  INV-PKG-01, INV-PKG-02, INV-PKG-03
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-PKG-GET
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-11/preload-package-state-machine.md
```

**الحالات:** غير نهائية: REQUESTED, BUILDING, READY, DOWNLOADED · نهائية: EXPIRED, REVOKED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-PKG-REQUEST | field user (request, confirm download, revoke) · Administrator / Security Officer (revoke) | POL-PKG-REQUEST | EVT-PKG-REQUESTED | Package builder; Sync delta (purge list) |
| CMD-PKG-CONFIRM-DOWNLOAD | field user (request, confirm download, revoke) · Administrator / Security Officer (revoke) | POL-PKG-CONFIRM-DOWNLOAD | EVT-PKG-DOWNLOADED | Package builder; Sync delta (purge list) |
| CMD-PKG-REVOKE | field user (request, confirm download, revoke) · Administrator / Security Officer (revoke) | POL-PKG-REVOKE | EVT-PKG-REVOKED | Package builder; Sync delta (purge list) |

#### AGG-PROJECTION-VERSION — Projection Version

`03-domain/contexts/BC07/aggregates/AGG-PROJECTION-VERSION.md` · SLC-05 · T3 · بيانات شخصية: لا

```
CAP  CAP-03.01
 └ UC   UC-078
    └ REQ  REQ-SRC-004
       └ AGG-PROJECTION-VERSION
          ├ INV  INV-PRJ-01, INV-PRJ-02, INV-PRJ-03, INV-PRJ-04
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-PRJ-STATUS
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-05/projection-version-state-machine.md
```

**الحالات:** غير نهائية: BUILDING, READY, ACTIVE, DEGRADED · نهائية: FAILED, RETIRED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-PRJ-CREATE-VERSION | Platform Operator | POL-PRJ-CREATE-VERSION | EVT-PRJ-BUILD-STARTED | Query router (alias switch); Operations alerting |
| CMD-PRJ-PROMOTE | Platform Operator | POL-PRJ-PROMOTE | EVT-PRJ-PROMOTED | Query router (alias switch); Operations alerting |
| CMD-PRJ-RETIRE | Platform Operator | POL-PRJ-RETIRE | EVT-PRJ-RETIRED | Query router (alias switch); Operations alerting |
| CMD-PRJ-CANCEL-BUILD | Platform Operator | POL-PRJ-CANCEL-BUILD | EVT-PRJ-FAILED | Query router (alias switch); Operations alerting |

#### AGG-SENSOR-STREAM — Sensor Stream

`03-domain/contexts/BC07/aggregates/AGG-SENSOR-STREAM.md` · SLC-16 · T2 · بيانات شخصية: لا

```
CAP  CAP-02.04
 └ UC   UC-094
    └ REQ  REQ-INT-002
       └ AGG-SENSOR-STREAM
          ├ INV  INV-SNS-01, INV-SNS-02, INV-SNS-03
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-SNS-LIST
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-16/sensor-stream-state-machine.md
```

**الحالات:** غير نهائية: DRAFT, ACTIVE, PAUSED · نهائية: RETIRED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-SNS-REGISTER | integration engineer | POL-SNS-REGISTER | EVT-SNS-REGISTERED | Ingestion workers (SLC-02 batches); Operations alerting |
| CMD-SNS-SET-QUALITY-RULES | integration engineer | POL-SNS-SET-QUALITY-RULES | EVT-SNS-QUALITY-RULES-SET | Ingestion workers (SLC-02 batches); Operations alerting |
| CMD-SNS-ACTIVATE | integration engineer | POL-SNS-ACTIVATE | EVT-SNS-ACTIVATED | Ingestion workers (SLC-02 batches); Operations alerting |
| CMD-SNS-PAUSE | integration engineer | POL-SNS-PAUSE | EVT-SNS-PAUSED | Ingestion workers (SLC-02 batches); Operations alerting |
| CMD-SNS-RETIRE | integration engineer | POL-SNS-RETIRE | EVT-SNS-RETIRED | Ingestion workers (SLC-02 batches); Operations alerting |

#### AGG-SYNC-CONFLICT — Sync Conflict

`03-domain/contexts/BC07/aggregates/AGG-SYNC-CONFLICT.md` · SLC-11 · T2 · بيانات شخصية: لا

```
CAP  CAP-02.03
 └ UC   UC-092
    └ REQ  REQ-OFF-004
       └ AGG-SYNC-CONFLICT
          ├ INV  INV-SCF-01, INV-SCF-02, INV-SCF-03
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-SCF-GET, QRY-SCF-LIST
          ├ THR  THR-S11-04
          └ TEST 13-verification/acceptance/SLC-11/sync-conflict-state-machine.md
```

**الحالات:** غير نهائية: OPEN · نهائية: RESOLVED_APPLIED, RESOLVED_DISCARDED, RESOLVED_MANUAL

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-SCF-ASSIGN | reviewer: task owner/Planner, Analyst for observations (assign, reapply, discard, resolve) | POL-SCF-ASSIGN | EVT-SCF-ASSIGNED | Reviewer notification; Sync delta (conflict notice to field user) |
| CMD-SCF-REAPPLY | reviewer: task owner/Planner, Analyst for observations (assign, reapply, discard, resolve) | POL-SCF-REAPPLY | EVT-SCF-REAPPLIED | Reviewer notification; Sync delta (conflict notice to field user) |
| CMD-SCF-DISCARD | reviewer: task owner/Planner, Analyst for observations (assign, reapply, discard, resolve) | POL-SCF-DISCARD | EVT-SCF-DISCARDED | Reviewer notification; Sync delta (conflict notice to field user) |
| CMD-SCF-RESOLVE-MANUALLY | reviewer: task owner/Planner, Analyst for observations (assign, reapply, discard, resolve) | POL-SCF-RESOLVE-MANUALLY | EVT-SCF-RESOLVED-MANUALLY | Reviewer notification; Sync delta (conflict notice to field user) |

#### AGG-SYNC-SESSION — Sync Session

`03-domain/contexts/BC07/aggregates/AGG-SYNC-SESSION.md` · SLC-11 · T2 · بيانات شخصية: لا

```
CAP  CAP-02.03
 └ UC   UC-090, UC-091, UC-092
    └ REQ  REQ-OFF-001, REQ-OFF-003, REQ-OFF-004, REQ-OFF-006
       └ AGG-SYNC-SESSION
          ├ INV  INV-SYN-01, INV-SYN-02, INV-SYN-03, INV-SYN-04
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-SYN-DELTA
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-11/sync-session-state-machine.md
```

**الحالات:** غير نهائية: OPEN, APPLYING · نهائية: COMPLETED, COMPLETED_WITH_CONFLICTS, FAILED, REJECTED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-SYN-OPEN | field device + user (open, upload) | POL-SYN-OPEN | EVT-SYN-OPENED | Owner contexts (commands applied via their APIs); Field telemetry |
| CMD-SYN-UPLOAD-BATCH | field device + user (open, upload) | POL-SYN-UPLOAD-BATCH | EVT-SYN-BATCH-RECEIVED | Owner contexts (commands applied via their APIs); Field telemetry |

### 21.11 BC08 — [bc08-governance-security.md](bc08-governance-security.md)

7 Aggregate. التهديدات المرتبطة آليًا بـAggregates هذا الـBC: THR-S01-05, THR-S01-12, THR-S12-02. القائمة اليدوية الكاملة في §12 من ملفه.

استعلامات في ملفات BC08 لم تُطابَق مع Aggregate بالبادئة: QRY-AUD-SEARCH, QRY-AUD-VERIFY, QRY-PDP-DECIDE.

#### AGG-CLASSIFICATION-SCHEME — Classification Scheme Version

`03-domain/contexts/BC08/aggregates/AGG-CLASSIFICATION-SCHEME.md` · SLC-01 · T2 · بيانات شخصية: لا

```
CAP  CAP-13.01
 └ UC   UC-085, UC-086, UC-089
    └ REQ  REQ-GOV-001, REQ-GOV-004, REQ-GOV-009
       └ AGG-CLASSIFICATION-SCHEME
          ├ INV  INV-CLS-01, INV-CLS-02, INV-CLS-03, INV-CLS-04
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-CLS-ACTIVE
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-01/classification-scheme-state-machine.md
```

**الحالات:** غير نهائية: DRAFT, ACTIVE · نهائية: SUPERSEDED, DISCARDED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-CLS-DRAFT | Security Officer | POL-CLS-DRAFT | EVT-CLS-DRAFTED | Search/Directory projection (BC01 read model); PDP bundle distributor |
| CMD-CLS-EDIT | Security Officer | POL-CLS-EDIT | EVT-CLS-EDITED | Search/Directory projection (BC01 read model); PDP bundle distributor |
| CMD-CLS-ACTIVATE | Security Officer | POL-CLS-ACTIVATE | EVT-CLS-ACTIVATED | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model); PDP bundle distributor |
| CMD-CLS-DISCARD | Security Officer | POL-CLS-DISCARD | EVT-CLS-DISCARDED | Search/Directory projection (BC01 read model); PDP bundle distributor |

#### AGG-DISPOSITION-RUN — Disposition Run

`03-domain/contexts/BC08/aggregates/AGG-DISPOSITION-RUN.md` · SLC-12a · T2 · بيانات شخصية: لا

```
CAP  CAP-11.02
 └ UC   UC-103
    └ REQ  REQ-GOV-006, REQ-GOV-007
       └ AGG-DISPOSITION-RUN
          ├ INV  INV-DSP-01, INV-DSP-02, INV-DSP-03, INV-DSP-04
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-DSP-GET
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-12a/disposition-run-state-machine.md
```

**الحالات:** غير نهائية: PLANNED, AWAITING_APPROVAL, APPROVED, EXECUTING · نهائية: COMPLETED, COMPLETED_WITH_EXCEPTIONS, CANCELLED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-DSP-SUBMIT | Archivist (submit, cancel) · Records/Legal authority ≠ submitter (approve) | POL-DSP-SUBMIT | EVT-DSP-SUBMITTED | Key manager (bucket key destruction); Owner contexts (purge plaintext caches, projections); Audit |
| CMD-DSP-APPROVE | Archivist (submit, cancel) · Records/Legal authority ≠ submitter (approve) | POL-DSP-APPROVE | EVT-DSP-APPROVED | Key manager (bucket key destruction); Owner contexts (purge plaintext caches, projections); Audit |
| CMD-DSP-CANCEL | Archivist (submit, cancel) · Records/Legal authority ≠ submitter (approve) | POL-DSP-CANCEL | EVT-DSP-CANCELLED | Key manager (bucket key destruction); Owner contexts (purge plaintext caches, projections); Audit |

#### AGG-ERASURE-REQUEST — Erasure Request

`03-domain/contexts/BC08/aggregates/AGG-ERASURE-REQUEST.md` · SLC-12a · T2 · بيانات شخصية: نعم

```
CAP  CAP-13.03
 └ UC   UC-103
    └ REQ  REQ-GOV-008
       └ AGG-ERASURE-REQUEST
          ├ INV  INV-ERS-01, INV-ERS-02, INV-ERS-03, INV-ERS-04
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-ERS-GET
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-12a/erasure-request-state-machine.md
```

**الحالات:** غير نهائية: RECEIVED, SCOPED, APPROVED, BLOCKED_BY_HOLD, EXECUTING · نهائية: COMPLETED, REJECTED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-ERS-REGISTER | Privacy officer / Legal (register) · Legal authority ≠ registrar (approve, reject) | POL-ERS-REGISTER | EVT-ERS-RECEIVED | Key manager (subject key destruction); BC01 / BC02 / BC05 (scope + confirmation); Projections (purge) |
| CMD-ERS-APPROVE | Privacy officer / Legal (register) · Legal authority ≠ registrar (approve, reject) | POL-ERS-APPROVE | EVT-ERS-APPROVED | Key manager (subject key destruction); BC01 / BC02 / BC05 (scope + confirmation); Projections (purge) |
| CMD-ERS-REJECT | Privacy officer / Legal (register) · Legal authority ≠ registrar (approve, reject) | POL-ERS-REJECT | EVT-ERS-REJECTED | Key manager (subject key destruction); BC01 / BC02 / BC05 (scope + confirmation); Projections (purge) |

#### AGG-LEGAL-HOLD — Legal Hold

`03-domain/contexts/BC08/aggregates/AGG-LEGAL-HOLD.md` · SLC-12a · T2 · بيانات شخصية: لا

```
CAP  CAP-11.02
 └ UC   UC-103
    └ REQ  REQ-GOV-007
       └ AGG-LEGAL-HOLD
          ├ INV  INV-LHD-01, INV-LHD-02, INV-LHD-03, INV-LHD-04
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-LHD-CHECK, QRY-LHD-LIST
          ├ THR  THR-S12-02
          └ TEST 13-verification/acceptance/SLC-12a/legal-hold-state-machine.md
```

**الحالات:** غير نهائية: ACTIVE, RELEASE_REQUESTED · نهائية: RELEASED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-LHD-PLACE | Legal/Compliance authority (place, extend, request/approve/cancel release) | POL-LHD-PLACE | EVT-LHD-PLACED | HoldCheck cache (all owners); Disposition planner; Erasure executor |
| CMD-LHD-EXTEND | Legal/Compliance authority (place, extend, request/approve/cancel release) | POL-LHD-EXTEND | EVT-LHD-EXTENDED | HoldCheck cache (all owners); Disposition planner; Erasure executor |
| CMD-LHD-REQUEST-RELEASE | Legal/Compliance authority (place, extend, request/approve/cancel release) | POL-LHD-REQUEST-RELEASE | EVT-LHD-RELEASE-REQUESTED | HoldCheck cache (all owners); Disposition planner; Erasure executor |
| CMD-LHD-APPROVE-RELEASE | Legal/Compliance authority (place, extend, request/approve/cancel release) | POL-LHD-APPROVE-RELEASE | EVT-LHD-RELEASED | HoldCheck cache (all owners); Disposition planner; Erasure executor |
| CMD-LHD-CANCEL-RELEASE | Legal/Compliance authority (place, extend, request/approve/cancel release) | POL-LHD-CANCEL-RELEASE | EVT-LHD-RELEASE-CANCELLED | HoldCheck cache (all owners); Disposition planner; Erasure executor |

#### AGG-POLICY-SET — Policy Set Version

`03-domain/contexts/BC08/aggregates/AGG-POLICY-SET.md` · SLC-01 · T2 · بيانات شخصية: لا

```
CAP  CAP-01.04, CAP-13.01
 └ UC   UC-086
    └ REQ  REQ-FND-011, REQ-FND-012, REQ-GOV-009
       └ AGG-POLICY-SET
          ├ INV  INV-POL-01, INV-POL-02, INV-POL-03, INV-POL-04
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-POL-GET
          ├ THR  THR-S01-05, THR-S01-12
          └ TEST 13-verification/acceptance/SLC-01/policy-set-state-machine.md
```

**الحالات:** غير نهائية: DRAFT, IN_REVIEW, APPROVED, ACTIVE · نهائية: SUPERSEDED, REJECTED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-POL-DRAFT | Security Officer | POL-POL-DRAFT | EVT-POL-DRAFTED | Search/Directory projection (BC01 read model); PDP bundle distributor |
| CMD-POL-EDIT | Security Officer | POL-POL-EDIT | EVT-POL-EDITED | Search/Directory projection (BC01 read model); PDP bundle distributor |
| CMD-POL-SUBMIT | Security Officer | POL-POL-SUBMIT | EVT-POL-SUBMITTED | Search/Directory projection (BC01 read model); PDP bundle distributor |
| CMD-POL-APPROVE | Security Officer | POL-POL-APPROVE | EVT-POL-APPROVED | Search/Directory projection (BC01 read model); PDP bundle distributor |
| CMD-POL-REJECT | Security Officer | POL-POL-REJECT | EVT-POL-REJECTED | Search/Directory projection (BC01 read model); PDP bundle distributor |

#### AGG-RETENTION-SCHEDULE — Retention Schedule Version

`03-domain/contexts/BC08/aggregates/AGG-RETENTION-SCHEDULE.md` · SLC-12a · T2 · بيانات شخصية: لا

```
CAP  CAP-11.02
 └ UC   UC-103
    └ REQ  REQ-GOV-006
       └ AGG-RETENTION-SCHEDULE
          ├ INV  INV-RTS-01, INV-RTS-02, INV-RTS-03
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-RTS-ACTIVE
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-12a/retention-schedule-state-machine.md
```

**الحالات:** غير نهائية: DRAFT, ACTIVE · نهائية: SUPERSEDED, DISCARDED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-RTS-DRAFT | Archivist (draft, edit, discard) · Legal/Compliance authority (activate) | POL-RTS-DRAFT | EVT-RTS-DRAFTED | Disposition planner; Key-bucket policy (class period sizing) |
| CMD-RTS-EDIT | Archivist (draft, edit, discard) · Legal/Compliance authority (activate) | POL-RTS-EDIT | EVT-RTS-EDITED | Disposition planner; Key-bucket policy (class period sizing) |
| CMD-RTS-ACTIVATE | Archivist (draft, edit, discard) · Legal/Compliance authority (activate) | POL-RTS-ACTIVATE | EVT-RTS-ACTIVATED | Disposition planner; Key-bucket policy (class period sizing) |
| CMD-RTS-DISCARD | Archivist (draft, edit, discard) · Legal/Compliance authority (activate) | POL-RTS-DISCARD | EVT-RTS-DISCARDED | Disposition planner; Key-bucket policy (class period sizing) |

#### AGG-SECURITY-EXCEPTION — Security Exception

`03-domain/contexts/BC08/aggregates/AGG-SECURITY-EXCEPTION.md` · SLC-01 · T2 · بيانات شخصية: لا

```
CAP  CAP-13.01
 └ UC   UC-088
    └ REQ  REQ-FND-017
       └ AGG-SECURITY-EXCEPTION
          ├ INV  INV-EXC-01, INV-EXC-02, INV-EXC-03
          ├ ADR  ADR-P01, ADR-P02, ADR-P03, ADR-P13
          ├ QRY  QRY-EXC-LIST
          ├ THR  —
          └ TEST 13-verification/acceptance/SLC-01/security-exception-state-machine.md
```

**الحالات:** غير نهائية: REQUESTED, FIRST_APPROVED, ACTIVE · نهائية: REJECTED, EXPIRED, REVOKED

| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |
|---|---|---|---|---|
| CMD-EXC-REQUEST | any authorized requester; Security Officers approve | POL-EXC-REQUEST | EVT-EXC-REQUESTED | Search/Directory projection (BC01 read model) |
| CMD-EXC-APPROVE | any authorized requester; Security Officers approve | POL-EXC-APPROVE | EVT-EXC-ACTIVATED | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) |
| ″ | ″ | ″ | EVT-EXC-FIRST-APPROVED | Search/Directory projection (BC01 read model) |
| CMD-EXC-REJECT | any authorized requester; Security Officers approve | POL-EXC-REJECT | EVT-EXC-REJECTED | Search/Directory projection (BC01 read model) |
| CMD-EXC-REVOKE | any authorized requester; Security Officers approve | POL-EXC-REVOKE | EVT-EXC-REVOKED | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) |

<!-- END GENERATED: build_relationships.py -->
