---
id: META-MODEL
type: information-model
title: Canonical Meta-Model
wave: W3
tier: T0
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
traces: {decided_by: [ADR-P01, ADR-P02, ADR-P03, ADR-P13], corrects: [CR-02, CR-27, CR-44]}
---

# Canonical Meta-Model

## 1. الطبقات

```text
Object Envelope (مشترك لكل الكائنات — object-envelope.md)
  └── Object Kind
        ├── Entity                 شيء له هوية مستمرة (شخص، منظمة، موقع، أصل، وثيقة…)
        ├── RealWorldEvent         شيء وقع في العالم (فيضان، اجتماع، حادث) — ليس Domain Event
        ├── Relationship           رابط موجّه ومؤرخ بين كائنين
        ├── Observation            ما رصده مصدر في زمن ومكان
        ├── Claim                  عبارة (subject, predicate, value) مؤرخة ثنائياً ومسندة لمصدر
        ├── Evidence               مادة تدعم أو تنفي ادعاءً
        ├── Source                 جهة/نظام/مستشعر أنتج معلومة
        ├── Conflict               تعارض بين ادعاءين أو أكثر
        ├── SameAsLink             قرار أن معرّفين يشيران لنفس الكيان
        └── Governed Objects (T2)  Decision, Plan, Task, Assessment, Policy, Product…
```

## 2. القاعدة الجوهرية: الكيان = هوية + ادعاءات

```text
Entity (identity only: id, urn, type, security, lifecycle)
   ▲ subject_ref
Claim ──source_refs──▶ Source
   │   └─evidence_links──▶ Evidence ──attachment──▶ Object Storage
   └── valid [from,to) × record [from,to)

Resolved Entity View  = projection over current, non-retracted claims
                        + conflict resolutions + same-as clusters
```

- لا تُخزن سمات T1 كأعمدة قابلة للتعديل على الكيان. تُخزن كادعاءات، و"القيمة الحالية" إسقاط محسوب.
- سمات T2/T3 تبقى سمات مباشرة على الكائن (بإصدارات لـ T2).

## 3. قاعدة تحديد القيمة الحالية (Resolved Value)

لكل `predicate` نوع تعدد من الكتالوج المرجعي: `single` أو `multi`.

| الحالة (للـ predicate أحادي القيمة، في لحظة التقييم) | القيمة المعروضة | حالة التحقق |
|---|---|---|
| لا ادعاء ساري | فارغة | — |
| ادعاء واحد ساري | قيمته | من الادعاء |
| عدة ادعاءات بقيم متطابقة | القيمة | `CORROBORATED` |
| ادعاءات بقيم متعارضة، تعارض مفتوح | كل المرشحين، مع علامة `DISPUTED` | `DISPUTED` |
| ادعاءات متعارضة، التعارض محلول بادعاء مفضل | قيمة الادعاء المفضل، مع رابط للتعارض | من الادعاء المفضل |

للـ predicate متعدد القيم: اتحاد القيم السارية، مع إزالة التكرار بعد التطبيع.

**لا يوجد اختيار تلقائي بأعلى ثقة.** الاختيار بين قيم متعارضة قرار بشري أو قاعدة معتمدة مسجلة (PRJ§3.4).

## 4. تمييز المصطلحات (CR-44)

| المصطلح | المعنى | أين |
|---|---|---|
| **RealWorldEvent** | شيء وقع في العالم | BO-EVENT (BC02) |
| **Domain Event** | سجل نظامي بأن تغييراً حدث في Aggregate | Outbox / Event Bus |
| **Integration Event** | نسخة عامة من Domain Event للخارج | Adapters |
| **Notification** | رسالة لمستخدم | BC04 |

## 5. ما هو Aggregate وما هو غير ذلك

حدود الـ Aggregates تُصمم في W4 لكل شريحة. قيود W3 عليها:
- Claim لا يتعدل بعد إنشائه إلا بإغلاق `recorded_to` (سحب/تصحيح) — تغيير صغير يصلح كـ Aggregate مستقل.
- Entity لا يحتوي ادعاءاته داخل حدوده، لتجنب God Aggregate وتضارب التزامن.
- SameAsLink وConflict كائنات مستقلة، لأنها قرارات لها مراجِع وزمن.
