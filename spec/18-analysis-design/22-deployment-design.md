---
id: AD-22-DEPLOYMENT-DESIGN
type: deployment-design
title: "تصميم النشر — الخلية، Kubernetes، التثبيت المعزول، البيئات، التعافي"
status: DRAFT
phase: "Phase 3.8 — 18-analysis-design (المرحلة 4)"
sources: [12-solution/cell-architecture.md, 12-solution/deployment-units.md, 12-solution/technology-decisions.md, 12-solution/release-configuration-migration.md, 12-solution/c4-context.md, 12-solution/cost-model.md, 09-reliability/dr-and-continuity.md, 08-security/trust-boundaries.md, 07-quality/scale-envelope.md, 07-quality/workloads*.md, 07-quality/performance-test-strategy.md, 00-governance/decisions/ADR-P04.md, 00-governance/decisions/ADR-P05.md, 00-governance/decisions/ADR-P18.md, 00-governance/decisions/ADR-P20.md, 05-contracts/asyncapi-*.md, 13-verification/fitness-functions.md]
---

# تصميم النشر

أين تعمل وحدات النشر الست عشرة وخدماتها ذات الحالة، وكيف تصل إلى موقع معزول عن الإنترنت، وكيف تُرقّى وتُستعاد. ما تحدده المصادر ينقل بمرجعه. وما لا تحدده (مساحات الأسماء، مجمعات العقد، البيئات، أقسام Kafka، خطوات break-glass) مقترح بعلامة **[Derived]** أو **[Missing]**، ويُجمع في §13.

## 1. المبادئ

| المبدأ | القاعدة | المصدر |
|---|---|---|
| الخلية وحدة النشر الكبرى | الخلية = عنقود Kubernetes + كل الخدمات ذات الحالة + كل وحدات النشر، في موقع واحد وولاية واحدة؛ لا مسار بيانات بين الخلايا | `cell-architecture.md`؛ TB-05 |
| البيئة المعزولة خط الأساس | التثبيت والترقية والتشغيل دون إنترنت؛ لا اعتماد على أي خدمة عامة | REQ-PLT-001؛ FIT-12؛ W1-answers |
| ملف الخلية تهيئة لا كود | المشتركة والمخصصة والسيادية قيم تهيئة لنفس الحزمة، ونفس مجموعة اختبارات القبول تعمل على الثلاثة | `release-configuration-migration.md` |
| إصدار واحد = حزمة واحدة | وسم المستودع = إصدار المنصة = حزمة Zarf واحدة | ADR-P18 |
| GitOps داخل الموقع | Argo CD يطبق ما في Git المحلي بمراجعة شخصين؛ لا تعديل يدوي على العنقود | TD-17؛ `release-configuration-migration.md` |

## 2. الخلية

```mermaid
flowchart TB
  subgraph CELL["خلية — عنقود RKE2 واحد، موقع واحد، ولاية واحدة"]
    ING["Ingress — TLS 1.3"] --> DU01["DU-01 Gateway / BFF"]
    DU01 --> APPS["DU-02..DU-13 (R1) — DU-14..DU-16 (R2)"]
    DEV["الأجهزة الميدانية"] --> DU01
    subgraph DATA["الخدمات ذات الحالة (operators)"]
      PG[("PostgreSQL — CloudNativePG: primary + 2 replicas")]
      KF[("Kafka KRaft — Strimzi: 3 brokers")]
      OS[("OpenSearch: 3 master + 6 data")]
      VK[("Valkey: 3 nodes")]
      S3[("S3 — Ceph RGW / MinIO، Object Lock")]
    end
    subgraph SEC["الأمن"]
      KC["Keycloak — وسيط OIDC/SAML"]
      BAO["OpenBao Transit"]
      HSM["HSM — PKCS#11"]
    end
    subgraph PLAT["المنصة"]
      HAR["Harbor — سجل الصور الداخلي"]
      ARGO["Argo CD"]
      OBS["OTel Collector، VictoriaMetrics، VictoriaLogs، Jaeger، Grafana، OpenCost"]
      KQ["Kueue — مهام التحليل"]
      GPU["مجمع GPU — vLLM (R2)"]
    end
    EG["Egress gateway — قائمة سماح لكل خلية"]
    APPS --> DATA
    APPS --> SEC
    BAO --> HSM
    APPS --> EG
  end
  IDP["مزوّد هوية المؤسسة"] --> KC
  EXT["أنظمة المؤسسة"] --> EG
  OPER["مستوى المشغل — break-glass فقط لبيانات المستأجر"] -.-> CELL
```

### 2.1 ملفات الخلية

| الملف | المستأجرون | متى | المصدر |
|---|---|---|---|
| مشتركة | ≤ 50 لكل خلية، أو حتى 80 % من السعة | الافتراضي | `cell-architecture.md` |
| مخصصة | مستأجر واحد | حمل > 20 % من سعة خلية، أو أعلى مستوى تصنيف | ADR-P04 |
| سيادية | مستأجر واحد بموقع ومشغلين محليين | النشر السيادي | ADR-P04؛ `cell-architecture.md` |

نطاق التصميم 100 مستأجر، والنمو إلى أكثر من 1,000 يكون بالخلايا (`scale-envelope.md`). الترقية من مشتركة إلى مخصصة بتصدير واستيراد على مستوى المستأجر دون تغيير كود (ADR-P04). توجيه المستخدم إلى خليته **[Missing]**: لا موجّه خلايا في المصادر. المقترح: نطاق DNS لكل خلية، يعرفه المستأجر عند التهيئة (`cell_id` في سجل المستأجر)، فلا مكوّن مشترك بين الخلايا **[Derived]** من TB-05.

### 2.2 الحجم التصميمي للخلية

5,000 مستخدم متزامن، 7,500 طلب/ث، 5,000 ملاحظة/ث، 500 بحث/ث (`cell-architecture.md`). PostgreSQL نحو 32 vCPU / 256 GB، ومخزن الكائنات نحو 100 TB في البداية، ونحو 60–120 pod في الذروة. كل رقم فرضية حتى اختبار الأداء، ويُعاد معايرته إذا تجاوز الحمل الفعلي 50 % من النطاق (ASM-010). خطة الاختبار: خط الأساس، 10×، الاندفاع، 24 ساعة متصلة، المستأجر المزعج، عاصفة إعادة الاتصال (5,000 جهاز ≤ 30 دقيقة)، الفوضى (`performance-test-strategy.md`).

## 3. تخطيط Kubernetes

RKE2 مع operators (CloudNativePG، Strimzi، OpenSearch)، عنقود واحد لكل خلية (TD-05؛ ADR-P05). التقسيم داخل العنقود لا تحدده المصادر **[Missing]**، والمقترح **[Derived]**:

| العنصر | المقترح | المبرر |
|---|---|---|
| مساحات الأسماء | واحدة لكل وحدة نشر (`du-01-gateway` … `du-16-ai-serving`)، ومساحات للمنصة: `data`، `security`، `observability`، `gitops`، `jobs` | حدود NetworkPolicy وحصص وكلفة لكل وحدة (OpenCost لكل namespace، `cost-model.md`) |
| مجمعات العقد | `system`؛ `apps` لوحدات بلا حالة؛ `data` للخدمات ذات الحالة بأقراص محلية؛ `jobs` لـKueue؛ `gpu` لـvLLM في R2 | ملفات حمل مختلفة (`deployment-units.md`)؛ عزل التحليل عن التشغيل (SR-11) |
| التوسع | HPA على الوحدات الأفقية بمقياس الطلبات أو تأخر المستهلك؛ DU-07 حسب أقسام الأحداث؛ DU-13 حسب حصص Kueue؛ DU-16 حسب حصة GPU | عمود التوسع في `deployment-units.md` |
| الحد الأدنى | ≥ 2 نسخة لكل وحدة critical مع PodDisruptionBudget، وتوزيع على عقد مختلفة | هدف 99.9 % (QAS-AVL-001) |
| الشبكة | NetworkPolicy افتراضية تمنع كل خروج، والاستثناءات عبر egress gateway بقائمة سماح لكل خلية؛ مخالفة الخروج تنبيه أمني P1 | `cell-architecture.md` |
| بين الخدمات | mTLS وهوية عبء عمل لكل تطبيق (TB-02)؛ منتج الشبكة الخدمية (service mesh) **[Missing]** | `authorization-model.md`؛ `trust-boundaries.md` |

## 4. وحدات النشر في الخلية

| الوحدة | الطبقة | التوسع | التوفر / RPO / RTO | الإصدار |
|---|---|---|---|---|
| DU-01 Gateway/BFF | critical | أفقي، بلا حالة | 99.9 % / ≤ 5 د / ≤ 1 س | R1 |
| DU-02 Foundation | critical | أفقي | 99.9 % / ≤ 5 د / ≤ 1 س | R1 |
| DU-03 Governance | critical | أفقي؛ عمّال الإتلاف مجدولون | 99.9 % / ≤ 5 د / ≤ 1 س | R1 |
| DU-04 Information | critical | أفقي | 99.9 % / ≤ 5 د / ≤ 1 س | R1 |
| DU-05 Ingestion | critical | أفقي حسب الطابور | 99.9 % / ≤ 5 د / ≤ 1 س | R1 |
| DU-06 Intelligence | important | أفقي | 99.5 % / ≤ 15 د / ≤ 4 س | R1 |
| DU-07 Evaluators | critical | حسب أقسام الأحداث (≤ 5 ث) | 99.9 % / ≤ 5 د / ≤ 1 س | R1 |
| DU-08 Operations | critical (المهام) | أفقي | 99.9 % / ≤ 5 د / ≤ 1 س | R1 |
| DU-09 Discovery | important | أفقي؛ البناة حسب الأقسام | 99.5 % / ≤ 15 د / ≤ 4 س | R1 |
| DU-10 Field sync | critical | أفقي | 99.9 % / ≤ 5 د / ≤ 1 س | R1 |
| DU-11 Adapters | standard | لكل محوّل | 99 % / ≤ 24 س / ≤ 24 س | R1 (+R2) |
| DU-12 Tiles | important | أفقي | 99.5 % / ≤ 15 د / ≤ 4 س | R1 |
| DU-13 Analysis jobs | important | حسب الحصص | 99.5 % / ≤ 15 د / ≤ 4 س | R1 |
| DU-14 Readiness | critical (التخصيص) | أفقي بنطاق المجمع، قفل على مستوى المجمع | 99.9 % / ≤ 5 د / ≤ 1 س | R2 |
| DU-15 Knowledge | important | أفقي؛ تخزين بارد منفصل | 99.5 % / ≤ 15 د / ≤ 4 س | R2 |
| DU-16 AI Serving | important | حصص GPU لكل خلية | 99.5 % / ≤ 15 د / ≤ 4 س | R2 |

المصادر: `deployment-units.md`؛ `dr-and-continuity.md`؛ QAS-AVL/REC. الوحدات DU-14..16 تصميم فقط: لا تُنشر قبل مراجعة Pilot R1 وحسم UNK-012 (حجم مجمع GPU). أرقام DU-14..16 بمطابقة طبقتها **[Derived]**.

## 5. الخدمات ذات الحالة: التوفر والنسخ والتعافي

| الخدمة | التوفر العالي | النسخ الاحتياطي والتعافي | المصدر |
|---|---|---|---|
| PostgreSQL (CloudNativePG) | primary + نسخة متزامنة + نسخة غير متزامنة؛ schema ودور لكل سياق | شحن WAL مستمر بتأخر ≤ 5 د؛ نسخة كاملة يومية؛ استعادة آلية أسبوعية | TD-01؛ `dr-and-continuity.md` |
| Kafka (Strimzi، KRaft) | 3 brokers، replication factor 3 | MirrorMaker 2 للمواضيع الحرجة إلى موقع التعافي | TD-04؛ `dr-and-continuity.md` |
| OpenSearch | 3 master + 6 data؛ عنقود منفصل عن سجلات المراقبة | لقطات كل 15 د إلى مخزن الكائنات؛ استعادة ≤ 4 س، أو إعادة بناء من المالكين (FIT-11) | TD-02؛ CR-54 |
| مخزن الكائنات | Ceph RGW أو MinIO؛ Object Lock (WORM) | ترميز المحو (erasure coding) + نسخ غير متزامن | TD-06 |
| OpenBao + مخزن المفاتيح | HA؛ KEK في HSM | يُنسخ مع سجل الإتلاف؛ النسخ ≤ 35 يومًا؛ بوابة الاستعادة FIT-19 (لا تُعاد مفاتيح أُتلفت) | TD-07؛ `key-hierarchy-and-disposition.md` |
| Valkey | 3 عقد | لا نسخة تعافي؛ يعاد بناؤه من BC01 | TD-11 |
| Keycloak | **[Missing]** — مقترح: نسختان على الأقل وقاعدته في عنقود PostgreSQL الخلية فيرث نسخه | انقطاع مزوّد الهوية: الجلسات القائمة ≤ 15 د، ثم break-glass | TD-09؛ `dr-and-continuity.md` |

- كل النسخ الاحتياطية مشفرة بمفاتيح المستأجرين (TB-10)، والتحقق من الاستعادة آلي (REQ-PLT-012). موقع التعافي في الولاية نفسها (REQ-GOV-005).
- **تمارين التعافي:** استعادة آلية أسبوعية وتمرين تعافٍ ربع سنوي (`dr-and-continuity.md`).

## 6. Kafka

| البند | القاعدة | المصدر |
|---|---|---|
| التسمية | `{cell}.<domain>.events` لكل سياق: foundation، governance، information، intelligence، operations، readiness، knowledge، integration، discovery، field، ai | `asyncapi-*.md` |
| موضوع الأولوية | `{cell}.security.versions` (مفتاحه `tenant_id + subject_urn`) | `asyncapi-slc01.md`؛ TD-04 |
| الرسائل الميتة | `{cell}.<domain>.events.dlq`، احتفاظه ≥ احتفاظ الموضوع المصدر | ADR-P20 |
| الاحتفاظ والتكرار | 7 أيام، replication factor 3 | `cell-architecture.md`؛ `dr-and-continuity.md` |
| مفتاح التقسيم | `tenant_id + aggregate.id` | كل رسالة AsyncAPI |
| عدد الأقسام | **[Missing]** — مقترح **[Derived]**: 24 لمواضيع information وoperations والـsecurity.versions (أعلى حمل: 5,000 ملاحظة/ث)، و12 لغيرها. الزيادة ممكنة دون كسر الترتيب لكل مفتاح فقط إذا أُوقف الاستهلاك أثناءها، فتُحدد مبكرًا بهامش | WL-06؛ SR-03 |
| الاحتفاظ والإسقاطات | الإسقاطات تُبنى من المالكين لا من Kafka، فلا حاجة لاحتفاظ طويل (FIT-11) | `15-event-design.md` §5 |

## 7. خط التثبيت المعزول وسلسلة التوريد

```mermaid
flowchart LR
  subgraph BUILD["خارج الموقع — CI"]
    SRC["وسم المستودع vX.Y.Z"] --> IMG["بناء الصور (digest-pinned)"]
    IMG --> SBOM["SBOM — Syft"]
    IMG --> SIGN["توقيع — cosign"]
    SBOM --> ZARF["حزمة Zarf: صور موقعة + SBOM + Helm + ترحيلات + حزم السياسات الأساسية + نموذج AI موقّع"]
    SIGN --> ZARF
    ZARF --> AIRT["مرحلة CI بشبكة معزولة (FIT-12)"]
  end
  AIRT --> MEDIA["نقل بوسيط غير متصل"]
  subgraph SITE["داخل الموقع"]
    MEDIA --> VERIFY["تحقق التوقيع وSBOM"]
    VERIFY --> HARBOR["Harbor الداخلي"]
    HARBOR --> GIT["Git المحلي — تغيير القيم بمراجعة شخصين"]
    GIT --> ARGO["Argo CD"]
    ARGO --> MIG["ترحيلات expand/contract"]
    MIG --> BG["blue/green للوحدات بلا حالة"]
  end
  BG --> RB["رجوع ≤ 1 ساعة (QAS-OPS-001)"]
```

| البند | القاعدة | المصدر |
|---|---|---|
| الصور | موقعة بـcosign ومثبتة بالـdigest، مع SBOM (Syft)؛ Harbor داخلي | TD-12؛ TD-17 |
| الحزمة | Zarf واحدة لكل إصدار: صور، SBOM، مخططات Helm، ترحيلات، حزم السياسات الأساسية | `release-configuration-migration.md` |
| الترحيلات | أمامية فقط (forward-only)، بنمط expand/contract، فالنسخة السابقة تعمل على الـschema الجديد أثناء blue/green | TD-17 |
| العقود | الإصدار الرئيسي السابق مدعوم ≥ 6 أشهر | QAS-EVO-001 |
| نموذج AI | يُجمَّد على نسخة موقعة عند الترقية | `deployment-units.md` (DU-16) |
| الرجوع | ≤ 1 ساعة من الحزمة وحدها | QAS-OPS-001 |

## 8. البيئات

المصادر تسمي بوابة الإنتاج G8 ومرحلة اختبار الأداء قبل G7، ولا تعرّف البيئات **[Missing]**. المقترح **[Derived]**:

| البيئة | الغرض | البيانات | الملف |
|---|---|---|---|
| التطوير | تطوير الوحدات واختبارات الحلقات | اصطناعية | خلية مشتركة مصغرة |
| التكامل | العقود (FIT-14)، واختبارات القبول، ومرحلة الشبكة المعزولة (FIT-12) | اصطناعية | الملفات الثلاثة بالتناوب (نفس مجموعة القبول) |
| ما قبل الإنتاج | اختبار الأداء والفوضى قبل G7، وتمرين الترقية والرجوع | اصطناعية بحجم الإنتاج | مطابقة لملف خلية الإنتاج المستهدفة |
| الإنتاج | خلايا المستأجرين بعد G8 | حقيقية | مشتركة / مخصصة / سيادية |

- **الترقية بين البيئات** بالحزمة نفسها (وسم واحد = حزمة واحدة). لا تُبنى حزمة جديدة للإنتاج.
- **لا بيانات مستأجر خارج الإنتاج.** نقل بيانات من الإنتاج إلى بيئة أخرى يعني مسار بيانات بين الخلايا، وهذا ممنوع (TB-05).

## 9. الشبكة وحدود الثقة

| الحد | القاعدة | المصدر |
|---|---|---|
| TB-01 المستخدم ↔ البوابة | OIDC/SAML، TLS 1.3، رموز قصيرة العمر، حدود معدل | `trust-boundaries.md` |
| TB-02 البوابة ↔ الوحدات | mTLS + هوية عبء العمل؛ SecurityContext موقّع | المصدر نفسه |
| TB-03 الوحدة ↔ قاعدة البيانات | حساب خدمة لكل سياق + RLS | المصدر نفسه |
| TB-05 خلية ↔ خلية | لا مسار بيانات | المصدر نفسه |
| TB-06 الأنظمة الخارجية | المحوّل وطبقة مكافحة الفساد والحجر | `20-integration-design.md` |
| TB-09 مستوى المشغل | المشغل لا يقرأ بيانات المستأجر؛ break-glass (§10) | المصدر نفسه |
| TB-10 النسخ الاحتياطية | مشفرة بمفاتيح المستأجرين | المصدر نفسه |
| الخروج | منع افتراضي + egress gateway بقائمة سماح | `cell-architecture.md` |

## 10. Break-glass

المصادر تقول: بموافقة شخصين ومدة محددة وتدقيق (TB-09، THR-014)، وحسابات طوارئ عند انقطاع مزوّد الهوية (`dr-and-continuity.md`). الخطوات نفسها **[Missing]**، والمقترح **[Derived]**:

```mermaid
sequenceDiagram
  participant R as المشغل الطالب
  participant A as معتمِد ثانٍ (≠ الطالب)
  participant B as OpenBao
  participant C as الخلية
  participant AU as سجل التدقيق
  R->>B: طلب وصول طارئ (السبب، النطاق، المستأجر، المدة ≤ 4 س)
  B->>A: طلب موافقة
  A->>B: موافقة
  B->>AU: break-glass granted (الطالب، المعتمِد، النطاق، المدة)
  B->>R: اعتماد مؤقت بنطاق محدد
  R->>C: الوصول — كل عملية مدققة ومسجلة الجلسة
  B-->>R: سحب تلقائي عند انتهاء المدة
  B->>AU: break-glass expired
  AU->>A: مراجعة لاحقة خلال يوم عمل
```

- الحساب لا يملك وصولًا قائمًا: الاعتماد يصدر عند الموافقة وينتهي بالمدة.
- إشعار مسؤول الأمن في المستأجر المعني فور المنح، لأن الوصول يمس بيانات المستأجر (TB-09).

## 11. المراقبة والاحتفاظ التشغيلي

مكدس المراقبة لكل خلية (TD-14)، ولا يخرج من الخلية. احتفاظ السجلات والتتبع والمقاييس التقنية **[Missing]**. المقترح: سجلات تقنية 30 يومًا، وتتبع 7 أيام، ومقاييس 13 شهرًا لمقارنة سنوية. السجلات بلا بيانات شخصية (`data-protection.md`)، فلا يخضع احتفاظها لجدول الإتلاف. سجل التدقيق منفصل ويخضع لـBC08.

## 12. الكلفة

OpenCost يوزع الكلفة لكل namespace وتسمية (`cost-model.md`؛ TD-14). تسمية `tenant_id` على أحمال المهام (Kueue) والتخزين المقسّم بالمستأجر تسمح بتوزيع الكلفة المشتركة على المستأجرين **[Derived]**.

## 13. فجوات ومقترحات

| البند | الحالة |
|---|---|
| موجّه الخلايا | **[Missing]** — مقترح: نطاق DNS لكل خلية (§2.1) |
| مساحات الأسماء ومجمعات العقد والحد الأدنى للنسخ | **[Missing]** — مقترح §3 |
| منتج الشبكة الخدمية لـmTLS | **[Missing]** — قرار تقني جديد |
| التوفر العالي لـKeycloak | **[Missing]** — مقترح §5 |
| عدد أقسام Kafka | **[Missing]** — مقترح §6 |
| البيئات والترقية بينها | **[Missing]** — مقترح §8 |
| خطوات break-glass | **[Missing]** — مقترح §10 |
| احتفاظ المراقبة التقنية | **[Missing]** — مقترح §11 |
| الولاية الفعلية (UNK-002) وحجم مجمع GPU (UNK-012) | مفتوحان — يحسمان قبل G8 وقبل R2 |
