---
id: SPEC-INTEGRATION
type: component-specification
title: Enterprise Integrations — patterns per system kind, sensors, HR proposals, CAP release
wave: W4
slice: SLC-16
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
traces: {requirements: [REQ-INT-001, REQ-INT-002, REQ-INT-003, REQ-INT-004], quality: [QAS-INT-001, QAS-PERF-012], rules: [BRL-013], unknowns: [UNK-021], recalibrate_after_pilot: true}
---

# Enterprise Integrations

## 1. المبدأ
الأنظمة الخارجية **مصادر لا مستودعات حقيقة** (BRL-013). كل ما يدخل يمر عبر محول مسجل (SLC-02 AGG-ADAPTER) بإصدار تحويل واختبارات وسلالة، ويصبح ادعاءات أو ملاحظات أو أدلة تحمل موثوقية مصدرها. لا كتابة إلى ERP/HRIS/DMS/CMMS في R2. الأنظمة الفعلية لكل مستأجر مجهولة (UNK-021)؛ هذه أنماط، والمحولات تُبنى عند التهيئة.

## 2. الأنماط حسب نوع النظام
| النظام | ما يدخل | كيف | ملاحظات |
|---|---|---|---|
| ERP | بيانات رئيسية: مواقع، مرافق، موردون، مخزون | دفعات استيراد → ادعاءات على كيانات (External ID) | القيم المتعارضة → تعارضات (SLC-04)، لا كتابة فوق |
| HRIS | أشخاص، وحدات، مناصب، التحاق/مغادرة | Person (BC01) + **مقترحات** تغيير أدوار (AGG-HR-SYNC-PROPOSAL) | لا تغيير صلاحيات آلياً؛ المغادرة تُصعَّد؛ SCIM يبقى المسار الفوري لتعطيل الحسابات |
| DMS | وثائق وبياناتها الوصفية | مرفقات (فحص محلي) + أدلة + External ID للوثيقة | تسمية الوثيقة من تصنيف DMS بعد تحويله عبر جدول مقابلة؛ غير المطابق = أعلى مستوى افتراضي حتى المراجعة |
| CMMS | أوامر الصيانة وحالتها | المحول يستدعي أوامر AGG-MAINTENANCE-ORDER بهوية خدمة، بمرجع CMMS | CMMS نظام سجل التنفيذ؛ المنصة تعكس الحالة مع سلالة |
| بوابة حساسات | قراءات | AGG-SENSOR-STREAM → دفعات ملاحظات (≤ 1,000، idempotent) | فحوص الجودة تعلّم لا تحذف |
| CAP (وارد) | تنبيهات جهات أخرى | محول → ملاحظات مصدر CAP | قد تطلق قواعد تنبيه (SLC-06) |
| CAP (صادر) | تنبيهات قابلة للإصدار | AGG-CAP-MESSAGE بقرار إصدار | المخرج الوحيد في R2 |

## 3. الانقطاع والتراكم (QAS-INT-001)
- المحول يحتفظ بنقطة تقدم (cursor/watermark) لكل اتصال؛ عند DEGRADED يُوقف السحب ولا يفقد شيئاً.
- عند العودة: إعادة السحب من آخر نقطة مؤكدة؛ دفعات idempotent بـ batch_key؛ الهدف معالجة تراكم 4 ساعات خلال ساعة.

## 4. الإصدار الخارجي (CAP)
```text
prepare(alert A):
  require tenant.cap_enabled ∧ label(A) ≤ tenant.external_release_level
  payload := template(CAP 1.2) filled from A's releasable fields only (category, event, urgency, severity, certainty, area polygon generalized per policy, headline from safe list)
  validate against CAP 1.2 schema
release: by release authority ≠ preparer → send via cap_endpoint connection → record ack
```

## 5. الشبكة
كل اتصال له قاعدة سماح واحدة في بوابة الخروج/الدخول (CELL-ARCHITECTURE §3)، يعتمدها ضابط أمن غير الطالب؛ التعليق يعطل القاعدة فوراً.
