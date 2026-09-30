---
id: THREAT-MODEL
type: threat-model
title: Threat Model — Kernel (STRIDE per trust boundary)
wave: W3
tier: T0
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
notes: النماذج التفصيلية لكل شريحة في W5.
---

# Threat Model — Kernel (STRIDE per trust boundary)

> النماذج التفصيلية لكل شريحة في W5.

## threats

_20 items_

| id | boundary | stride | threat | likelihood | impact | controls | residual_risk |
|---|---|---|---|---|---|---|---|
| THR-001 | TB-01 | Spoofing | سرقة رمز جلسة | M | H | رموز قصيرة العمر، ربط بالجهاز، MFA لعمليات حساسة | L |
| THR-002 | TB-01 | Tampering | تعديل الطلب لتغيير tenant أو urn | M | H | الخادم يشتق tenant من الرمز لا من الطلب؛ تحقق مخطط | L |
| THR-003 | TB-02 | Elevation | خدمة داخلية تنتحل صلاحيات أعلى | L | H | mTLS + هوية عبء العمل؛ SecurityContext موقّع | L |
| THR-004 | TB-03 | Info Disclosure | استعلام ينسى فلتر المستأجر | M | H | RLS حاجز ثان؛ FIT-02؛ اختبار عزل | L |
| THR-005 | TB-04 | Info Disclosure | استدلال على الوجود عبر العدد/الـ Facets/التوقيت | H | H | ADR-P06 pre-filter؛ QAS-SEC-002 | L |
| THR-006 | TB-04 | Info Disclosure | إسقاط متأخر يعيد كائناً بعد سحب الصلاحية | H | H | إعادة فحص security_version (ADR-P06 §3) | L |
| THR-007 | TB-04 | Info Disclosure | بلاطة خريطة مخزنة تُقدم لمستخدم بصلاحية أقل | M | H | مفتاح cache بنطاق الصلاحية (ADR-P12) | L |
| THR-008 | TB-05 | Info Disclosure | تسرب بين الخلايا | L | H | لا مسارات بيانات بين الخلايا | L |
| THR-009 | TB-06 | Tampering | بيانات خارجية مسممة أو مزيفة | M | M | ACL، حجر، مصدر وموثوقية، لا ثقة تلقائية | M |
| THR-010 | TB-06 | DoS | فيضان بيانات من محول | M | M | حصص، backpressure (QAS-SCAL-002) | L |
| THR-011 | TB-07 | Info Disclosure | سرقة جهاز ميداني | M | H | تشفير، انتهاء صلاحية، مسح عن بعد، منع preload فوق INTERNAL | L |
| THR-012 | TB-07 | Repudiation | إنكار ملاحظة سُجلت دون اتصال | L | M | توقيع الأوامر بمفتاح الجهاز+المستخدم؛ تدقيق | L |
| THR-013 | TB-08 | Info Disclosure | حقن أوامر غير مباشر عبر وثيقة يدفع AI لتسريب سياق | M | H | AI بصلاحيات الطالب فقط؛ AIL≤2؛ لا أدوات كتابة؛ R2 تفصيل | M |
| THR-014 | TB-09 | Elevation | مشغل منصة يقرأ بيانات مستأجر | L | H | فصل المفاتيح؛ break-glass بشخصين وتدقيق | L |
| THR-015 | TB-10 | Info Disclosure | نسخة احتياطية مسروقة | L | H | تشفير بمفاتيح المستأجر | L |
| THR-016 | audit | Tampering | تعديل سجل التدقيق | L | H | سلسلة hash + anchor (QAS-SEC-006) | L |
| THR-017 | PDP | DoS | تعطل PDP يوقف المنصة | M | H | PDP في critical tier، نسخ متعددة، ذاكرة قرارات قصيرة؛ fail-closed مقبول كخطر متبقٍ | M |
| THR-018 | ER | Tampering | دمج كيانات خاطئ متعمد لإخفاء معلومة | L | M | الدمج قرار مدقق وقابل للعكس؛ حد العنقود | L |
| THR-019 | supply chain | Tampering | مكتبة أو صورة حاوية ملوثة | M | H | SBOM، توقيع الصور، مرآة داخلية للحزم (بيئة معزولة) | M |
| THR-020 | TB-01 | Info Disclosure | رسالة خطأ تكشف وجود كائن | M | M | نفس شكل not-found/forbidden (ADR-P06 §5) | L |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
threats:
- id: THR-001
  boundary: TB-01
  stride: Spoofing
  threat: سرقة رمز جلسة
  likelihood: M
  impact: H
  controls: رموز قصيرة العمر، ربط بالجهاز، MFA لعمليات حساسة
  residual_risk: L
- id: THR-002
  boundary: TB-01
  stride: Tampering
  threat: تعديل الطلب لتغيير tenant أو urn
  likelihood: M
  impact: H
  controls: الخادم يشتق tenant من الرمز لا من الطلب؛ تحقق مخطط
  residual_risk: L
- id: THR-003
  boundary: TB-02
  stride: Elevation
  threat: خدمة داخلية تنتحل صلاحيات أعلى
  likelihood: L
  impact: H
  controls: mTLS + هوية عبء العمل؛ SecurityContext موقّع
  residual_risk: L
- id: THR-004
  boundary: TB-03
  stride: Info Disclosure
  threat: استعلام ينسى فلتر المستأجر
  likelihood: M
  impact: H
  controls: RLS حاجز ثان؛ FIT-02؛ اختبار عزل
  residual_risk: L
- id: THR-005
  boundary: TB-04
  stride: Info Disclosure
  threat: استدلال على الوجود عبر العدد/الـ Facets/التوقيت
  likelihood: H
  impact: H
  controls: ADR-P06 pre-filter؛ QAS-SEC-002
  residual_risk: L
- id: THR-006
  boundary: TB-04
  stride: Info Disclosure
  threat: إسقاط متأخر يعيد كائناً بعد سحب الصلاحية
  likelihood: H
  impact: H
  controls: إعادة فحص security_version (ADR-P06 §3)
  residual_risk: L
- id: THR-007
  boundary: TB-04
  stride: Info Disclosure
  threat: بلاطة خريطة مخزنة تُقدم لمستخدم بصلاحية أقل
  likelihood: M
  impact: H
  controls: مفتاح cache بنطاق الصلاحية (ADR-P12)
  residual_risk: L
- id: THR-008
  boundary: TB-05
  stride: Info Disclosure
  threat: تسرب بين الخلايا
  likelihood: L
  impact: H
  controls: لا مسارات بيانات بين الخلايا
  residual_risk: L
- id: THR-009
  boundary: TB-06
  stride: Tampering
  threat: بيانات خارجية مسممة أو مزيفة
  likelihood: M
  impact: M
  controls: ACL، حجر، مصدر وموثوقية، لا ثقة تلقائية
  residual_risk: M
- id: THR-010
  boundary: TB-06
  stride: DoS
  threat: فيضان بيانات من محول
  likelihood: M
  impact: M
  controls: حصص، backpressure (QAS-SCAL-002)
  residual_risk: L
- id: THR-011
  boundary: TB-07
  stride: Info Disclosure
  threat: سرقة جهاز ميداني
  likelihood: M
  impact: H
  controls: تشفير، انتهاء صلاحية، مسح عن بعد، منع preload فوق INTERNAL
  residual_risk: L
- id: THR-012
  boundary: TB-07
  stride: Repudiation
  threat: إنكار ملاحظة سُجلت دون اتصال
  likelihood: L
  impact: M
  controls: توقيع الأوامر بمفتاح الجهاز+المستخدم؛ تدقيق
  residual_risk: L
- id: THR-013
  boundary: TB-08
  stride: Info Disclosure
  threat: حقن أوامر غير مباشر عبر وثيقة يدفع AI لتسريب سياق
  likelihood: M
  impact: H
  controls: AI بصلاحيات الطالب فقط؛ AIL≤2؛ لا أدوات كتابة؛ R2 تفصيل
  residual_risk: M
- id: THR-014
  boundary: TB-09
  stride: Elevation
  threat: مشغل منصة يقرأ بيانات مستأجر
  likelihood: L
  impact: H
  controls: فصل المفاتيح؛ break-glass بشخصين وتدقيق
  residual_risk: L
- id: THR-015
  boundary: TB-10
  stride: Info Disclosure
  threat: نسخة احتياطية مسروقة
  likelihood: L
  impact: H
  controls: تشفير بمفاتيح المستأجر
  residual_risk: L
- id: THR-016
  boundary: audit
  stride: Tampering
  threat: تعديل سجل التدقيق
  likelihood: L
  impact: H
  controls: سلسلة hash + anchor (QAS-SEC-006)
  residual_risk: L
- id: THR-017
  boundary: PDP
  stride: DoS
  threat: تعطل PDP يوقف المنصة
  likelihood: M
  impact: H
  controls: PDP في critical tier، نسخ متعددة، ذاكرة قرارات قصيرة؛ fail-closed مقبول كخطر متبقٍ
  residual_risk: M
- id: THR-018
  boundary: ER
  stride: Tampering
  threat: دمج كيانات خاطئ متعمد لإخفاء معلومة
  likelihood: L
  impact: M
  controls: الدمج قرار مدقق وقابل للعكس؛ حد العنقود
  residual_risk: L
- id: THR-019
  boundary: supply chain
  stride: Tampering
  threat: مكتبة أو صورة حاوية ملوثة
  likelihood: M
  impact: H
  controls: SBOM، توقيع الصور، مرآة داخلية للحزم (بيئة معزولة)
  residual_risk: M
- id: THR-020
  boundary: TB-01
  stride: Info Disclosure
  threat: رسالة خطأ تكشف وجود كائن
  likelihood: M
  impact: M
  controls: نفس شكل not-found/forbidden (ADR-P06 §5)
  residual_risk: L
```

</details>
