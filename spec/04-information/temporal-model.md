---
id: TEMPORAL-MODEL
type: architecture
title: Temporal Architecture
wave: W3
tier: T0
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
traces: {decided_by: [ADR-P01, ADR-P02], requirements: [REQ-INF-022, REQ-INF-023, REQ-INF-024, REQ-OFF-003], quality: [QAS-TMP-001]}
---

# Temporal Architecture

## 1. الأزمنة الخمسة

| الزمن | السؤال | من يحدده | يُخزن في | ينطبق على |
|---|---|---|---|---|
| Event Time | متى وقع الشيء في الواقع؟ | المصدر أو المحلل | `event_time` (فترة غامضة بدقة) | RealWorldEvent، Observation، Claim عند الحاجة |
| Observation Time | متى رُصد؟ | الجهاز أو المصدر | `observed_at` | Observation، Measurement |
| Record Time | متى عرف النظام؟ | **الخادم فقط** | `recorded_from/to` (T1)، `recorded_at` (T2) | كل الكائنات المسجلة |
| Valid Time | متى كانت المعلومة صحيحة في الواقع؟ | المصدر أو المحلل | `valid_from/to` | Claims، Relationships، SameAsLinks |
| Effective Time | متى يسري أثر قرار أو سياسة؟ | صاحب السلطة | `effective_from/to` | Decision، Plan، Policy، Authority grant |

**ممنوع (SL-11):** استخدام `created_at` أو `updated_at` كأي من هذه الأزمنة.

## 2. الفترات

- كل الفترات نصف مفتوحة `[from, to)` بتوقيت UTC ودقة ميكروثانية.
- `to = null` يعني ∞.
- لا تداخل لفترتي record لنفس الادعاء المنطقي.

## 3. العمليات على ادعاء T1

| العملية | الأثر على الادعاء القديم | الادعاء الجديد |
|---|---|---|
| Assert | — | `record=[now, ∞)` |
| Correct (قيمة خاطئة كانت مسجلة) | `recorded_to = now` | نفس الموضوع/السمة، قيمة مصححة، `record=[now, ∞)` |
| Change in reality (القيمة تغيرت فعلاً) | `recorded_to = now`، ثم إعادة تسجيله بـ `valid_to = t_change` | ادعاء جديد `valid=[t_change, ∞)` |
| Retract (سحب بلا بديل) | `recorded_to = now`، status `RETRACTED` | — |

الفرق بين "تصحيح" و"تغير الواقع" جوهري: الأول يغير ما نعرفه عن الماضي، والثاني يضيف حقيقة جديدة.

## 4. دلالات الاستعلام

```text
STATE(subject, predicate, valid_at = T, known_at = K) =
  claims where valid_from <= T < coalesce(valid_to, ∞)
         and recorded_from <= K < coalesce(recorded_to, ∞)
  → resolved by meta-model §3 using conflicts and same-as links as known at K
```

- الافتراضي: `T = now`، `K = now`.
- **As-Of-Valid** = "ماذا كان صحيحاً في T حسب معرفتنا الحالية".
- **As-Known-At** = "ماذا كنا نعتقد، في لحظة K، أنه صحيح في T". هذا ما تستخدمه مراجعة القرارات: `K = decision.recorded_at`.

## 5. مثال

```text
1 Mar   تسجيل: موقع الأصل X = A      valid=[1 Mar,∞)  record=[1 Mar,∞)
10 Mar  تصحيح: الموقع كان B منذ 1 Mar
        الادعاء الأول: record=[1 Mar,10 Mar)
        ادعاء جديد: B  valid=[1 Mar,∞)  record=[10 Mar,∞)

قرار اتُخذ في 5 Mar:
  STATE(X, location, valid_at=5 Mar, known_at=5 Mar)  = A   ← ما عرفه صاحب القرار
  STATE(X, location, valid_at=5 Mar, known_at=now)    = B   ← الحقيقة كما نعرفها الآن
```

## 6. الأزمنة القادمة من الأجهزة

- زمن الجهاز يُخزن كـ `observed_at` مع `clock_offset` المقاس عند مصافحة المزامنة (ADR-P09).
- `recorded_from` = زمن استلام الخادم دائماً.
- إذا تجاوز الانحراف حداً (افتراضياً 5 دقائق)، تُعلَّم الملاحظة `time_quality = DEVICE_CLOCK_SUSPECT` في بعد جودة البيانات.

## 7. التواريخ الغامضة

"صيف 1990" = `event_time {start: 1990-06-01, end: 1990-09-01, precision: month}`.
الاستعلام الزمني على فترة غامضة يعيد تطابقاً بثلاث حالات: `CERTAIN_OVERLAP | POSSIBLE_OVERLAP | NO_OVERLAP`.

## 8. إعادة البناء التاريخي (CR-25)

كل نتيجة إعادة بناء تحمل وسماً:

| الوسم | المعنى |
|---|---|
| RECORDED | مأخوذة مباشرة من ادعاءات أو إصدارات مسجلة |
| RECONSTRUCTED | مشتقة حتمياً من سجلات (مثل حالة مهمة من تاريخها) |
| INFERRED | مستنتجة بقاعدة أو نموذج، مع الإشارة للقاعدة |
| UNKNOWN | لا يوجد أساس |

## 9. التخزين (قيود منطقية، التقنية في W8)

- فهرسة الفترتين لكل ادعاءات T1.
- عرض مادي "للحالة الحالية" (`valid ∋ now` و`record ∋ now`) لخدمة 95 % من القراءات بسرعة (QAS-PERF-002).
- تقسيم زمني + مستأجري للملاحظات والادعاءات (SR-08).
