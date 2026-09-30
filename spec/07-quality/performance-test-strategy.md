---
id: PERF-TEST-STRATEGY
type: verification-strategy
title: Performance, Capacity & Scalability Test Strategy
tier: T2
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
wave: W8
traces: {quality: [QAS-PERF-001, QAS-PERF-002, QAS-PERF-003, QAS-PERF-005, QAS-PERF-007, QAS-PERF-009, QAS-PERF-012, QAS-PERF-013, QAS-SCAL-001, QAS-SCAL-002, QAS-OFF-003]}
---

# Performance, Capacity & Scalability Test Strategy

## 1. المبدأ
كل رقم في نطاق التصميم فرضية حتى يُقاس. الاختبار يسبق الإنتاج (G7) ويُكرر في Pilot على بيانات فعلية، والنتائج تعيد معايرة CELL-ARCHITECTURE §2.

## 2. مزيج الحمل المرجعي (مشتق من WL-*)
| المسار | النسبة من الطلبات | المصدر |
|---|---|---|
| قراءة كيان محلول | 30 % | WL-01h |
| قوائم وخرائط (bbox + زمن) | 20 % | WL-03a |
| بحث | 20 % | WL-02a |
| أوامر (مهام، ملاحظات فردية، ادعاءات) | 15 % | WL-01, WL-01i |
| مهامي / تقدم / مواقف | 10 % | WL-01j, QAS-PERF-019 |
| أخرى | 5 % | — |
| + تدفق ملاحظات منفصل | 5,000/ث مستدام، دفعات 50,000/ث × 60 ث | WL-06a |

## 3. الاختبارات
| الاختبار | الهدف | معيار النجاح |
|---|---|---|
| Baseline (pilot load 100 مستخدم) | خط أساس | كل QAS-PERF ضمن الهدف |
| 10× (1,000) ثم التصميم (5,000) | QAS-SCAL-001 | الأهداف تتحقق بالتوسع الأفقي فقط |
| Burst ingestion | QAS-SCAL-002 | 0 فقد؛ تنبيه حرج p95 ≤ 30 ث أثناء الدفعة؛ عودة ≤ 5 د |
| Soak 24 ساعة | تسرب ذاكرة، تأخر الإسقاطات | تأخر الفهرس p95 ≤ 30 ث طوال المدة |
| Noisy tenant | QAS-SCAL-005 | المستأجرون الآخرون ضمن QAS-PERF-001 |
| Reconnect storm | QAS-OFF-003 | 5,000 جهاز ≤ 30 د |
| Inference suite تحت الحمل | QAS-SEC-002/011 | 0 تسرب، ولا فروق توقيت ذات دلالة |
| Chaos (PDP، KV، broker، KMS) | FMEA | السلوك يطابق مصفوفات التدهور |

## 4. البيانات والأدوات
- بيانات اصطناعية بحجم التصميم (1e8 ادعاء، 1e9 ملاحظة، أسماء عربية بتنوعات) + عينة Pilot حقيقية.
- مولّد حمل قابل للبرمجة (k6 أو Gatling)؛ القياس عبر OpenTelemetry (TD-14).
- كل نتيجة تُسجل مقابل QAS-ID وتُحدّث `07-quality/workloads-*`.
