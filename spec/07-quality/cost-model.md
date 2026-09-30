---
id: COST-MODEL
type: cost-model
title: Cost Model (unit economics)
tier: T0/T2
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
wave: W8
traces: {requirements: [REQ-PLT-013], quality: [QAS-COST-001], unknowns: [UNK-012]}
---

# Cost Model

الميزانية والأسعار الفعلية مجهولة (UNK-012)، فلا أرقام نقدية هنا. النموذج يحدد **ماذا** يُقاس و**كيف** يُوزع، لتُحسب التكلفة من القياس لا من التقدير.

## 1. محركات التكلفة
| المحرك | الوحدة | مصدر القياس |
|---|---|---|
| حوسبة الوحدات بلا حالة | vCPU-hour، GB-hour | OpenCost لكل namespace/label |
| PostgreSQL | vCPU، ذاكرة، TB تخزين ساخن | مقاييس العنقود + حجم المخططات لكل مستأجر |
| OpenSearch | عقد بيانات، TB فهارس | حجم الفهارس لكل مجموعة مستأجرين |
| Kafka | brokers، TB احتفاظ | حجم المواضيع حسب المستأجر (مفتاح التقسيم) |
| Object storage | TB مخزن، TB نقل داخلي | مسارات المستأجر |
| Analysis jobs | vCPU-hour لكل مستأجر | Kueue accounting |
| HSM/KMS | عمليات لف/فك | عدادات OpenBao |
| تشغيل بشري | ساعات فريق التشغيل | خارج النظام (إدخال يدوي) |

## 2. التوزيع على المستأجرين
`cost(tenant, month) = Σ_driver usage(tenant, driver) × unit_cost(driver) + share(tenant) × fixed_cell_cost`
حيث `share` = نسبة الاستخدام المرجح للخلية. الخلية المخصصة: كل تكلفتها على مستأجرها.

## 3. التكلفة لكل عملية (مؤشرات)
تكلفة 1,000 ملاحظة، 1,000 بحث، ساعة تحليل، GB مرفقات شهرياً — تُحسب شهرياً من القياس وتُعرض في تقرير المستأجر (QAS-COST-001).

## 4. قواعد التصميم المتناسبة مع التكلفة (W1 Q29)
- الخلية المشتركة للمستأجرين الصغار (ADR-P04).
- لا مكوّن جديد قبل دليل (SR-10) — حُذف محرك الرسم (TD-03).
- تقادم البيانات ساخن/دافئ/بارد (SR-08).
- التحليل بحصص.
