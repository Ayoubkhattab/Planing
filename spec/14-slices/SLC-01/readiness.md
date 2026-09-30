---
id: G6-SLC-01
type: slice-readiness
title: Slice Readiness — SLC-01 (G6-SLC)
wave: W7
slice: SLC-01
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
traces: {approval: HAP-09, basis: [V6§2.2, V6§20.2]}
---

# G6-SLC-01 — Tenancy, Identity, Organization, Authorization, Audit

## الحكم: **READY FOR IMPLEMENTATION (delegated)**

## 1. الشروط المسبقة (V6§20.2)
| الشرط | الحالة |
|---|---|
| G3 للنواة PASS؛ ADR-P01/P02/P03 معتمدة | ✓ |
| كل Aggregate يستوفي البنود الأحد عشر | ✓ (الجدول 2) |
| قواعد الفحص بلا ERROR | ✓ (الجدول 3) |
| Threat Model وFMEA مكتملان؛ كل H معالج أو مقبول | ✓ 12 تهديداً، 9 أنماط فشل؛ خطران متبقيان M مقبولان صراحة |
| القبول يغطي المسار الطبيعي وكل انتقال ممنوع وقرارات الصلاحية وسيناريو استدلال | ✓ 78 انتقالاً + 255 رفضاً (مولدة) + 26 سيناريو ثوابت وأمن |
| لا UNK مفتوح يحجب الشريحة | ✓ |
| مراجعة مستقلة | ✓ ATAM-lite (`atam-lite.md`) |
| اعتماد | HAP-09 (delegated) |

## 2. البنود الأحد عشر لكل Aggregate (V6§2.2)
| Aggregate | 1 ثوابت | 2 جدول كامل | 3 أوامر | 4 أحداث بمخطط | 5 نموذج منطقي | 6 تزامن | 7 مستوى | 8 عقد API | 9 قبول | 10 جودة | 11 لا مجهولات | الحكم |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AGG-TENANT | ✓ 5 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ T2 | ✓ | ✓ | ✓ | ✓ | **PASS** |
| AGG-ORGANIZATION | ✓ 4 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ T2 | ✓ | ✓ | ✓ | ✓ | **PASS** |
| AGG-PERSON | ✓ 2 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ T2 | ✓ | ✓ | ✓ | ✓ | **PASS** |
| AGG-USER | ✓ 5 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ T2 | ✓ | ✓ | ✓ | ✓ | **PASS** |
| AGG-SERVICE-ACCOUNT | ✓ 3 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ T2 | ✓ | ✓ | ✓ | ✓ | **PASS** |
| AGG-ROLE | ✓ 3 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ T2 | ✓ | ✓ | ✓ | ✓ | **PASS** |
| AGG-ROLE-ASSIGNMENT | ✓ 3 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ T2 | ✓ | ✓ | ✓ | ✓ | **PASS** |
| AGG-AUTHORITY-GRANT | ✓ 4 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ T2 | ✓ | ✓ | ✓ | ✓ | **PASS** |
| AGG-CLEARANCE | ✓ 4 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ T2 | ✓ | ✓ | ✓ | ✓ | **PASS** |
| AGG-CLASSIFICATION-SCHEME | ✓ 4 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ T2 | ✓ | ✓ | ✓ | ✓ | **PASS** |
| AGG-POLICY-SET | ✓ 4 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ T2 | ✓ | ✓ | ✓ | ✓ | **PASS** |
| AGG-SECURITY-EXCEPTION | ✓ 3 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ T2 | ✓ | ✓ | ✓ | ✓ | **PASS** |

## 3. قواعد الفحص
| القاعدة | النتيجة |
|---|---|
| SL-01 مالك واحد | 0 مخالفات |
| SL-02 كل أمر له Aggregate وسياسة | 0 / 71 |
| SL-03 كل أمر مغير ينتج حدثاً | 0 |
| SL-04 كل انتقال له أمر وحدث وشرط | 0 |
| SL-05 جدول حالات × أوامر كامل | 0 (12 مصفوفة كاملة) |
| SL-06 الوصول لحالة نهائية | 0 (+1 استثناء مبرر: Organization) |
| SL-07 كل حدث له مخطط ومستهلك | 0 / 79 |
| SL-08 كل API مرتبط بأمر أو استعلام | 0 (العقود مولدة من الكتالوج) |
| SL-09 كل استعلام له سياسة ونطاق | 0 / 14 |
| SL-17 / SL-18 H معالج | 0 |
| SL-20 مراجع مكسورة | 0 |
| SL-22 مجهولات حاجبة | 0 |
| SL-24 حجم Aggregate | 0 |
| SL-28 fail-closed | PB-03 + FIT-16 |
| OpenAPI (3 وثائق، 85 عملية) | **valid** (openapi-spec-validator) |
| التتبع | 25 متطلباً، 0 بلا اختبار (`15-traceability/trace-slc01.md`) |

## 4. قرارات مفوضة اتُخذت في هذه الشريحة
| القرار | القيمة |
|---|---|
| عمق التفويض | ≤ 2 |
| عمر بيانات اعتماد حساب الخدمة | ≤ 90 يوماً |
| مدة الاستثناء الأمني | ≤ 30 يوماً، التجديد طلب جديد |
| تصريح أعلى مستوى | موافقة ضابطي أمن مختلفين |
| أدوار غير متوافقة افتراضياً | Auditor × Administrator، Auditor × Security Officer |
| رمز الجلسة / SecurityContext | ≤ 15 دقيقة / ≤ 60 ثانية + فحص الإصدار الأمني في كل طلب |
| عمر حزمة السياسات الأقصى | 5 دقائق، بعدها رفض الكتابة |
| التدقيق | 16 shard لكل مستأجر، تثبيت كل 5 دقائق، حد التراكم 24 ساعة / 80 % |
| حد الوحدات لكل مؤسسة | 5,000 |
| إنهاء المستأجر | موافقة مشغلَين مختلفين + فحص التجميد القانوني |
| محو الشخص | أمر CMD-PER-ERASE (ADR-P08) |
| الأدوار عبر SCIM | ممنوعة؛ SCIM ينشئ ويعطل فقط |

## 5. ما يُسلَّم للتنفيذ
| المخرج | المسار |
|---|---|
| 12 Aggregate | `03-domain/contexts/BC01|BC08/aggregates/` |
| كتالوجات الأوامر والاستعلامات والأحداث | `03-domain/contexts/BC01|BC08/*-slc01.md` |
| SecurityContext | `03-domain/contexts/BC01/security-context.md` |
| السياسات | `08-security/policies-slc01.md` |
| العقود | `05-contracts/openapi-*-slc01.md`، `asyncapi-slc01.md`، `errors-slc01.md` |
| البيانات | `06-data/logical-model/slc-01.md` |
| القبول | `13-verification/acceptance/SLC-01/`، `invariant-properties-slc01.md` |
| الجودة والتشغيل | `07-quality/workloads-slc01.md`، `08-security/threat-model-slc01.md`، `09-reliability/*-slc01.md` |

## 6. ما يبقى خارج هذه الشريحة (غير حاجب)
- اختيار محرك قاعدة البيانات والوسيط ومحرك السياسات (ADR-P05، W8). الواجهات والعقود مستقلة عنها.
- الاحتفاظ والتجميد القانوني (REQ-GOV-006/007) — شريحة SLC-12a ضمن R1 بعد SLC-03.
- تسجيل الأجهزة الميدانية (BO-DEVICE) — SLC-11.
