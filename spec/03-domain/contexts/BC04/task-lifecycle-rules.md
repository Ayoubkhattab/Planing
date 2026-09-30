---
id: SPEC-TASK-RULES
type: component-specification
title: Task Lifecycle Rules — decisions, criteria evaluation, scheduling, offline
wave: W4
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
slice: SLC-03
traces: {closes: [OQ-031, OQ-032, OQ-033], corrects: [CR-06, CR-46], requirements: [REQ-OPS-006, REQ-OPS-008, REQ-OPS-012, REQ-OFF-001]}
---

# Task Lifecycle Rules

## 1. حسم الأسئلة المفتوحة (قرارات مفوضة)
| السؤال | القرار |
|---|---|
| **OQ-031** الفرق بين APPROVED وCOMPLETED وCLOSED | **APPROVED** = المراجع قبل النتيجة (جودة). **COMPLETED** = كل معايير الإكمال مستوفاة (BRL-006)؛ يحدث آلياً عند الاعتماد إن كانت كل المعايير قابلة للفحص آلياً ومستوفاة، وإلا بأمر إكمال يثبت المعايير البشرية. **CLOSED** = إغلاق إداري بعد انتهاء المتابعات؛ يدوي، أو آلي بعد 7 أيام بلا متابعات مفتوحة. |
| **OQ-032** انتهاء المهلة | **التصعيد هو الافتراضي** (عند الموعد وعند الموعد + المهلة). الانتهاء EXPIRED فقط إذا أعلن نوع المهمة `expires_on_due = true` (مهام لا قيمة لها بعد وقتها). |
| **OQ-033** هل REJECTED نهائية؟ | **نعم.** إعادة المحاولة = مهمة جديدة مرتبطة `follow_up_of`، حفاظاً على تاريخ واضح. |
| التعليق (SUSPENDED) | **علم متعامد لا حالة** (INV-TASK-06): الاستئناف يعيد المهمة لنفس حالتها دون تخزين "الحالة السابقة" (CR-46). |
| الإسناد | لمستخدم واحد في R1؛ لا طوابير فرق (مؤجل). |
| إعادة الإسناد | مسموحة من ASSIGNED حتى BLOCKED مع نفس فحوص الأهلية والتصريح. |

## 2. معايير الإكمال
| النوع | يُفحص | متى يُستوفى |
|---|---|---|
| result_item | آلياً | يوجد ≥ 1 عنصر نتيجة من النوع المطلوب |
| evidence_count ≥ n | آلياً | ≥ n أدلة مرتبطة (غير مسحوبة) |
| measurement_recorded | آلياً | قياس للمقياس المحدد بعد بدء المهمة |
| checklist | بشرياً | كل البنود مؤكدة في الأمر COMPLETE |
| attestation | بشرياً | إقرار من دور محدد في الأمر COMPLETE |

**قاعدة:** المعايير مجمّدة من ASSIGNED فصاعداً (INV-TASK-09). تغيير المعايير بعد الإسناد = إلغاء وإنشاء مهمة جديدة، أو إصدار خطة جديد (SLC-08).

## 3. الجدولة
| المؤقت | الأثر | الهدف الزمني |
|---|---|---|
| `due_at` | EVT-TASK-ESCALATED (لا تغيير حالة) | ≤ 60 ث بعد الموعد (QAS-OPS-002) |
| `due_at + grace` | تصعيد ثان للمستوى الأعلى | ≤ 60 ث |
| `due_at` مع expires_on_due | EXPIRED | ≤ 60 ث |
| COMPLETED + 7 أيام | CLOSED إن لم توجد متابعات مفتوحة | يومياً |

القراءة تعرض `overdue = now > due_at` محسوبة، فلا تعتمد الواجهة على تأخر المجدول (FM-S03-01).

## 4. الاعتماديات
- رسم الاعتماديات لا دوري (INV-TASK-08)، ويُفحص عند MARK-READY وEDIT.
- START يتطلب أن كل السابقات COMPLETED أو CLOSED (فحص بالاستعلام وقت الأمر).
- إلغاء مهمة سابقة يصعّد المهام التابعة تلقائياً (EVT-TASK-CANCELLED → escalation).

## 5. العمل دون اتصال (عقد مع SLC-11)
- الأوامر المسموحة دون اتصال: ACCEPT، START، BLOCK، RESUME، ADD-RESULT-ITEM، SUBMIT (`x-offline-capable` في العقد).
- كل أمر يحمل `base_version` و`client_command_id` و`device_time`.
- عند الإعادة: إن كانت `base_version` = الحالية يُطبق؛ ADD-RESULT-ITEM إلحاقي فيُطبق دائماً إن كانت الحالة تسمح؛ غير ذلك → حالة تعارض مزامنة (CF-05) ولا Last-Write-Wins (ADR-P09).
