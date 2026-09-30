---
id: G6-SLC-02
type: slice-readiness
title: Slice Readiness — SLC-02 Information Kernel (G6-SLC)
wave: W7
slice: SLC-02
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
traces: {approval: HAP-09, basis: [V6§2.2, V6§20.2], depends_on: [G6-SLC-01]}
---

# G6-SLC-02 — Source → Observation → Entity / Claim → Evidence

## الحكم: **READY FOR IMPLEMENTATION (delegated)**

## 1. الشروط المسبقة
| الشرط | الحالة |
|---|---|
| G3 PASS؛ SLC-01 READY (SecurityContext، PDP، audit) | ✓ |
| البنود الأحد عشر لكل Aggregate | ✓ (الجدول 2) |
| قواعد الفحص بلا ERROR | ✓ (الجدول 3) |
| Threat Model / FMEA | ✓ 10 تهديدات (3 متبقية M مقبولة) / 8 أنماط فشل |
| القبول | ✓ 63 انتقالاً + 111 رفضاً (مولدة) + 28 سيناريو زمني وأمني وإدخال + 8 خصائص للمكتبة |
| مكتبة الادعاءات والزمن مواصفة بخوارزمية معيارية | ✓ `LIB-CLAIMS-KERNEL` |
| مجهولات حاجبة | 0 |

## 2. البنود الأحد عشر
| Aggregate | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | الحكم |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AGG-SOURCE | ✓ 4 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **PASS** |
| AGG-OBSERVATION | ✓ 4 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **PASS** |
| AGG-ENTITY | ✓ 3 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **PASS** |
| AGG-REALWORLD-EVENT | ✓ 2 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **PASS** |
| AGG-RELATIONSHIP | ✓ 2 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **PASS** |
| AGG-CLAIM | ✓ 5 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **PASS** |
| AGG-EVIDENCE | ✓ 3 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **PASS** |
| AGG-EVIDENCE-LINK | ✓ 2 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **PASS** |
| AGG-ATTACHMENT | ✓ 4 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **PASS** |
| AGG-IMPORT-BATCH | ✓ 4 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **PASS** |
| AGG-EXTERNAL-ID | ✓ 2 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **PASS** |
| AGG-ADAPTER | ✓ 3 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **PASS** |

## 3. الفحص
| القاعدة | النتيجة |
|---|---|
| SL-02 / SL-03 / SL-04 / SL-05 | 0 مخالفات (57 أمراً، 12 مصفوفة كاملة) |
| SL-06 | 0 (+3 استثناءات مبررة: Entity، Real-World Event، Relationship — هويات دائمة) |
| SL-07 | 0 / 64 حدثاً |
| SL-09 | 0 / 16 استعلاماً |
| SL-10 (T1 يحدد الأزمنة والدليل والثقة) | ✓ عبر المكتبة وحزمة الكائن |
| SL-11 (لا created_at كزمن عمل) | ✓ |
| SL-12 (CRS ودقة لكل سمة مكانية) | ✓ SpatialEnvelope إلزامي |
| OpenAPI (BC02 66 + BC07 7 عملية) | **valid** |
| التتبع | 24 متطلباً، 0 بلا اختبار؛ 4 متطلبات REQ-INF مُسندة لـ SLC-04 |

## 4. قرارات مفوضة في هذه الشريحة
| القرار | القيمة |
|---|---|
| تسامح انحراف ساعة الجهاز | 5 دقائق، وما زاد يُعلَّم DEVICE_CLOCK_SUSPECT |
| حجم دفعة الملاحظات | ≤ 1,000 عنصر بمفتاح عدم تكرار لكل عنصر |
| نافذة زمنية إلزامية لقوائم الملاحظات | ≤ 31 يوماً |
| عمق تتبع السلالة | ≤ 10 |
| نافذة الرفع / عمر روابط التنزيل | 24 ساعة / ≤ 5 دقائق |
| فحص الملفات | ماسح محلي إلزامي قبل الإتاحة |
| اعتماد الملاحظات | محلل ≠ المراقب؛ اعتماد آلي فقط لمستشعرات موثوقيتها A/B بسياسة مستأجر |
| التزام جديد | generalize(min_accuracy_m) للمواقع، حتمي |
| حماية المصادر البشرية | هوية بصلاحية خاصة فقط؛ تصنيف المصدر ≥ الافتراضي + 1 |
| الاستيراد | batch_key فريد لكل محول؛ نفس المفتاح بمحتوى مختلف مرفوض |

## 5. التسليم
Aggregates: `03-domain/contexts/BC02|BC07/aggregates/` · المكتبة: `03-domain/contexts/BC02/claims-temporal-kernel.md` · العقود: `05-contracts/*-slc02.md` · البيانات: `06-data/logical-model/slc-02.md` · القبول: `13-verification/acceptance/SLC-02/` · الجودة: `*-slc02.md` في 07/08/09.

## 6. ترتيب البناء المقترح داخل الشريحة
1. مكتبة الادعاءات والزمن مع مجموعة oracle الزمنية (قبل أي Aggregate).
2. Source، Attachment، Evidence، Evidence Link.
3. Observation (مفرد ثم دفعات).
4. Entity، Real-World Event، Relationship، Claim.
5. External ID، Adapter، Import Batch.
