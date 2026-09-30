---
id: LANGUAGE-MODEL
type: information-model
title: Language, Names & Transliteration Model
wave: W3
tier: T0
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
traces: {decided_by: [ADR-P15], requirements: [REQ-INF-031, REQ-SRC-003, REQ-PLT-010], quality: [QAS-USA-002], corrects: [CR-18]}
---

# Language, Names & Transliteration Model

## 1. أشكال النص الأربعة
| الشكل | الاستخدام | قابل للتعديل؟ |
|---|---|---|
| `original` | العرض والأدلة | **لا أبداً** |
| `normalized` | المطابقة والبحث | يُعاد حسابه عند تغير إصدار التطبيع |
| `transliterations[]` | البحث عبر الكتابتين | يُضاف له |
| `phonetic_key` | اقتراح المطابقات | يُعاد حسابه |

كل نص يحمل `lang` (BCP 47، مثل `ar`, `en`, `ar-Latn`) و`normalization_version`.

## 2. قواعد تطبيع العربية (normalization v1)
| # | القاعدة |
|---|---|
| N1 | حذف التشكيل (U+064B–U+0652، U+0670) |
| N2 | حذف التطويل (U+0640) |
| N3 | أ إ آ ٱ → ا |
| N4 | ى → ي |
| N5 | ة → ه |
| N6 | ؤ → و ، ئ → ي ، ء المنفردة تُحذف في مفتاح المطابقة فقط |
| N7 | الأرقام العربية-الهندية (٠–٩) والفارسية → 0–9 |
| N8 | توحيد المسافات وحذف علامات الاتجاه غير المرئية (U+200E، U+200F، U+061C) |
| N9 | إزالة "ال" التعريف في مفتاح المطابقة للأسماء فقط، مع إبقاء صيغة بها |
| N10 | اللاتينية: case folding + إزالة العلامات الصوتية (NFKD) |

N4–N6 و N9 تُطبق على **مفتاح المطابقة** لا على العرض.

## 3. نموذج الاسم الشخصي
```text
PersonName
  original, lang
  components: given | father | grandfather | family | laqab | kunya (أبو/أم) | nisba | title
  connectors normalized: بن = ابن = bin = ibn = ben
  transliterations[]: {scheme, value}   e.g. Mohammed / Muhammad / Mohamed
  name_type: legal | known_as | alias | historical
```
الاسم نفسه ادعاء T1 (قد يتعدد ويتعارض، وله مصدر).

## 4. البحث
- المحلل العربي يطبق N1–N8 على الفهرس والاستعلام.
- البحث عن اسم يبحث في `normalized` و`transliterations` و`phonetic_key` معاً، مع ترتيب يفضل التطابق الأدق.
- مجموعة اختبار أسماء عربية معتمدة مطلوبة لـ QAS-USA-002 (تُبنى في W5).

## 5. الزمن والتقويم
التخزين UTC و ISO 8601 ميلادي. العرض الهجري اختياري (حسبة أم القرى أو حسابية حسب إعداد المستأجر)، ولا يُخزن كقيمة أصلية إلا إذا كان هو الأصل في مصدر، فيُحفظ في `original` ويُحوّل للقيمة الكانونية.
