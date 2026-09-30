---
id: SPEC-DISCOVERY
type: component-specification
title: Discovery — Secured Search & Graph Projections
wave: W4
slice: SLC-05
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
traces: {decided_by: [ADR-P06, ADR-P15, ADR-P16], corrects: [CR-47], requirements: [REQ-SRC-001, REQ-SRC-002, REQ-SRC-003, REQ-SRC-004, REQ-FND-010, REQ-GOV-004, REQ-INF-027], quality: [QAS-SEC-002, QAS-SEC-003, QAS-SEC-011, QAS-PERF-003, QAS-PERF-004, QAS-PERF-018, QAS-USA-002, QAS-REL-002, QAS-REL-004]}
---

# Discovery — Secured Search & Graph

## 1. الموقع المعماري
Discovery خدمة قراءة في BC07. **لا تملك بيانات عمل** (INV-PRJ-01): كل وثيقة فيها مشتقة من سياق مالك ويمكن إعادة بنائها. لا تكتب في أي سياق، ولا تُسأل مباشرة من الواجهة إلا عبر واجهتها المعلنة بعد PEP.

## 2. خط البناء (Projection pipeline)
```text
Owner outbox events (SLC-01..04, later slices)
   → inbox (dedupe by event_id) → ordered per partition key (tenant + aggregate)
   → fetch current state from owner OHS with discovery workload identity (full labels)
   → build documents → upsert into ACTIVE (and BUILDING, if any) projection version
```
- **Notify + fetch:** الحدث يشير؛ المحتوى يُجلب من المالك. يمنع أحداثاً ضخمة ويضمن أحدث حالة.
- التأخر المستهدف p95 ≤ 30 ث (QAS-PERF-004).
- إعادة البناء الكاملة: عبر واجهات تصدير بالمؤشر من كل مالك (system-only)، ثم اللحاق بنقطة التحقق الحية، ثم ترقية (AGG-PROJECTION-VERSION). الهدف ≤ 24 ساعة عند نطاق التصميم (QAS-REL-004).

## 3. نموذج الوثائق
### 3.1 حقائق البحث (Search Facts) — المفتاح لمنع الاستدلال
كل ادعاء حالي قابل للبحث يصبح **حقيقة** مستقلة داخل وثيقة الكائن:
```text
EntityDoc {
  urn, canonical_urn, tenant, type, labels{level, compartments, caveats, org_scope}, security_version,
  facts[] (nested):
    { predicate, value_text_ar, value_text_en, value_norm, translit[], phonetic[], value_num?, unit?, geo?,
      valid_from, valid_to, labels{…}, claim_urn }
  current_location? (from visible-location resolution per level — see §4.3)
}
ObservationDoc { urn, tenant, labels, observed_at, geo, method, narrative forms, source_type, state (VALIDATED only by default) }
TaskDoc / later: PlanDoc, AssessmentDoc, DocumentDoc (same label rules)
```
**القاعدة:** الاستعلام يطابق فقط الحقائق المرئية للقارئ. الكيان يُعاد إذا كان مرئياً **و** طابقت حقيقة مرئية واحدة على الأقل. بهذا لا يُعثر على كيان عبر قيمة ادعاء مخفي (THR-S05-01).

### 3.2 الرسم (Graph)
عقد: الكيانات والأحداث الواقعية (بتسمياتها). حواف: العلاقات، ولكل حافة تسميات علاقتها وفترة صلاحيتها وزمن تسجيلها.

## 4. دلالات الاستعلام (معيارية)
### 4.1 البحث
```text
search(req, subject):
  scope   := PDP.allowed_scope(subject, action=view, resource=search)         -- ADR-P06 §2
  visible := λ labels. tenant = subject.tenant ∧ level ≤ clearance ∧ compartments ⊆ subject.compartments ∧ caveats ok ∧ org_scope ∈ scope
  hits    := engine.query(req, doc_filter = visible(doc.labels),
                               fact_filter = visible(fact.labels))           -- pre-filter BEFORE scoring, counting, faceting
  page    := first `limit` hits by sort
  recheck := LabelCheck(owner, page.urns, subject)                            -- CR-47: authoritative, per owning context, batched
  page    := page ∖ {h | ¬recheck(h).visible}
  refill  := if page shrank: fetch next hits until limit or exhausted (same filters)
  facets  := computed on pre-filtered hit set only; buckets with count 0 omitted
  total   := count(pre-filtered) exact ≤ 1,000 else "1000+"
  return page (titles/snippets rendered from visible facts only), facets, total, cursor
```
### 4.2 قواعد منع الاستدلال (QAS-SEC-002، QAS-SEC-011)
| القناة | القاعدة |
|---|---|
| العدد | من المجموعة المصفاة مسبقاً فقط؛ لا "N نتائج محجوبة" |
| Facets | من المجموعة المصفاة مسبقاً فقط |
| الاقتراحات | من الحقائق المرئية فقط |
| الترتيب | درجة الصلة تُحسب على الحقائق المرئية فقط (لا تأثير لحقيقة مخفية على الترتيب) |
| المؤشر (cursor) | موقع + بصمة نطاق الصلاحية؛ استخدامه بنطاق مختلف يُرفض |
| الأخطاء | not-found وforbidden نفس الشكل |
| الاكتمال | `partial_service_unavailable` يُحدد من صحة الخدمات فقط، لا من وجود نتائج |
| التوقيت | لا عمل إضافي مشروط بوجود وثائق مخفية؛ إعادة الفحص على الصفحة المعادة فقط |

### 4.3 الموقع في النتائج
الموقع المعروض = ناتج مكتبة الادعاءات (LIB §3) على الحقائق المرئية، مع التزام `generalize` إن وُجد. الفهرس يخزن مواقع لكل حقيقة؛ فلترة الخرائط الجغرافية تُطبق على الحقائق المرئية.

### 4.4 الرسم
- **الجوار (depth ≤ 3):** BFS؛ عند كل قفزة تُستبعد الحواف والعقد غير المرئية **قبل** التوسع. العقدة المخفية تقطع كل ما خلفها.
- **المسارات (≤ 4 قفزات، ≤ 20 مساراً):** بحث ثنائي الاتجاه على الرسم المرئي فقط. مسار يمر بعقدة أو حافة مخفية **غير موجود** بالنسبة للقارئ.
- **الكثافة:** حد 500 جار مرئي لكل قفزة بترتيب حتمي؛ `truncated = true` فقط إذا تجاوز **المرئي** الحد.
- **الزمن:** `valid_at` / `known_at` على الحواف (فترة صلاحية وجود العلاقة).

## 5. العربية (ADR-P15)
المحلل يطبق N1–N8 على الفهرسة والاستعلام؛ مطابقة الأسماء تبحث في `value_norm` و`translit` و`phonetic` معاً مع أوزان: تطابق مطبّع > نقحرة > صوتي. الإصدار (`normalization_version`) جزء من إصدار الإسقاط؛ تغييره = إصدار جديد (INV-PRJ-04).

## 6. التقسيم والحجم (SR-00)
| الوثائق | التنظيم |
|---|---|
| الكيانات والأحداث والمهام | فهرس لكل مجموعة مستأجرين، مقسم بـ hash(tenant) |
| الملاحظات | فهارس زمنية شهرية؛ آخر 13 شهراً "ساخنة"؛ الأقدم يُستعلم فقط عند طلب نافذة زمنية تشمله |
| الرسم | مقسم بالمستأجر |
| الخلايا المخصصة | إسقاطاتها داخل الخلية فقط |

## 7. التدهور (QAS-REL-002)
| الحالة | السلوك |
|---|---|
| الإسقاط DEGRADED (تأخر) | يُخدم مع `completeness = partial_service_unavailable` وتنبيه؛ القراءات المباشرة من المالكين تعمل |
| الإسقاط غير متاح | البحث يعيد 503؛ الأوامر والقراءات المباشرة والخرائط من المالكين تستمر |
| سياق مالك لا يرد على LabelCheck | تُستبعد نتائجه (fail-closed) ويُعلّم الاكتمال جزئياً بناءً على صحة الخدمة |

## 8. متطلبات القدرات على محرك البحث (مدخل لـ ADR-P05، W8)
1. فلترة متداخلة (nested) على مستوى الحقيقة مع تطبيقها قبل الحساب والتجميع.
2. محللات قابلة للتخصيص (العربية N1–N8، نقحرة، مفاتيح صوتية).
3. استعلامات جغرافية (polygon، bbox) مع فهرسة مكانية.
4. تقسيم زمني وأسماء مستعارة (aliases) لترقية ذرية.
5. ترقيم بالمؤشر مستقر.
6. أداء: 500 استعلام/ث مركب، p95 ≤ 1 ث على 1e8 حقيقة + فهارس ملاحظات شهرية.

هذه المتطلبات تُقارن في W8 بين خيار PostgreSQL وحده ومحرك بحث مخصص (ADR-P05). **أرجّح أن البحث المتداخل على مستوى الحقيقة بهذا الحجم هو أول دليل عبء عمل قد يبرر محرك بحث مخصصاً** — يُحسم بالقياس لا بالافتراض (SR-10).
