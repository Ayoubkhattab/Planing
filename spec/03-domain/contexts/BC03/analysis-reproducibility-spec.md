---
id: SPEC-ANALYSIS
type: component-specification
title: Analytical Work — Reproducibility, Execution, Estimative Language, Citations
wave: W4
slice: SLC-07
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
traces: {requirements: [REQ-ANL-001, REQ-ANL-002, REQ-ANL-003, REQ-ANL-004, REQ-ANL-005, REQ-ANL-006, REQ-ANL-007, REQ-ANL-008, REQ-INF-035], quality: [QAS-TRC-001, QAS-TRC-002], corrects: [CR-29]}
---

# Analytical Work

## 1. سلسلة العمل
```text
Analysis Case (question, scope, hypotheses, assumptions, pinned evidence, scenarios)
   └─ Analysis Run (method version + image digest + parameters + seed + inputs pinned by known_at)  ── LineageRecord
         └─ Finding (statement + uncertainty, sources = runs | evidence)                          ── peer-accepted
               └─ Assessment Version (key judgments with estimative probability + confidence,
                                      citations pinned by version, methodology, limitations)       ── reviewed, published, immutable
                     └─ Decision Request / Decision (SLC-08) references URN + version
```
حل CR-29: الحالة لا تحتوي التشغيلات والنتائج والتقييمات؛ كل منها Aggregate مستقل بدورة حياته.

## 2. قابلية إعادة الإنتاج (REQ-ANL-003، QAS-TRC-002)
تُعاد النتيجة نفسها إذا ثبتت العناصر الخمسة:
| العنصر | كيف يُثبت |
|---|---|
| البيانات | كل مدخل مثبت بـ `known_at` = زمن الإرسال (الخادم)، فتُقرأ الحالة كما كانت معروفة حينها (TEMPORAL-MODEL §4) |
| الطريقة | إصدار طريقة ثابت (كود + مخطط معاملات) |
| البيئة | بصمة صورة التنفيذ (image digest) من سجل داخلي؛ لا تحميل خارجي أثناء التشغيل (FIT-12) |
| المعاملات | مخزنة كما أُرسلت ومتحقق منها بالمخطط |
| العشوائية | `seed` مسجل؛ الطرق غير الحتمية تُعلَّم `deterministic = false` ولا يُطلب تطابقها بالبايت، بل ضمن تسامح تعلنه الطريقة |

**تقرير إعادة الإنتاج:** مقارنة بصمات النتائج → `REPRODUCED` أو `DIFFERENT` مع قائمة ما اختلف (مدخل، إصدار طريقة، صورة). يُسمح بإعادة الإنتاج فقط لمن هو مصرح بتسمية التشغيل الأصلي، فلا يكشف التقرير مدخلات مخفية.

## 3. التنفيذ
- التشغيلات مهام غير متزامنة (REQ-ANL-004) على عمال حوسبة عديمي الحالة، بطابور لكل مستأجر وحصة تنفيذ متزامن (TenantQuotas.concurrent_jobs)، وتوزيع عادل بين المستأجرين.
- **التشغيل يقرأ بصلاحيات مقدمه، لا بصلاحيات النظام** (INV-RUN-02): العامل يحمل SecurityContext مقدم الطلب (مفوّض ومحدود بمدة التشغيل ≤ 24 ساعة)، وكل قراءة تمر بـ PEP.
- النواتج (جداول، طبقات، نقطيات COG) تُخزن كأصول معنونة بالمحتوى، مع lineage إلى المدخلات والطريقة.
- المهلة الافتراضية 6 ساعات لكل تشغيل (قابلة للتهيئة لكل طريقة).

## 4. اللغة التقديرية (Estimative language)
- كل حكم رئيسي = عبارة + **مصطلح احتمال** من RD-ESTIMATIVE-PROBABILITY (مصطلح بنطاق رقمي ثابت، يُعرض المصطلح والنطاق معاً) + **ثقة تحليلية** (منخفضة / متوسطة / عالية) تعكس جودة الأساس، لا الاحتمال.
- الخلط بينهما ممنوع: الاحتمال يصف الحدث، والثقة تصف الأدلة والمنهج.

## 5. الاستشهادات والحجب (REQ-ANL-008)
- كل استشهاد يثبت الإصدار (URN + version). تغيير الأصل لاحقاً لا يغير ما استند إليه التقييم.
- قارئ غير مصرح لبعض الاستشهادات: تُحجب تلك الاستشهادات (معرفاتها ومحتواها). إظهار "استشهاد محجوب" من عدمه سياسة مستأجر (افتراضياً: لا يُظهر).
- تسمية التقييم ≥ أعلى تسمية بين نتائجه وأدلته، فالقارئ المصرح بالتقييم مصرح عادة بكل ما فيه؛ الحجب يعالج حالات الأقسام (compartments) المختلفة.

## 6. سحب النتائج والتقييمات
- سحب Finding → تُعلَّم التقييمات التي تستشهد بها للمراجعة (لا تتغير تلقائياً).
- سحب Assessment → إشعار أصحاب القرارات والمنتجات المرتبطة؛ القرارات السابقة تبقى مرتبطة بالإصدار الذي استندت إليه.
