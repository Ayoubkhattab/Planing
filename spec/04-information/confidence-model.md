---
id: CONFIDENCE-MODEL
type: information-model
title: Confidence Model (7 dimensions)
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
wave: W3
tier: T0
traces: {requirements: [REQ-INF-026], corrects: [CR-03]}
---

# Confidence Model

لا توجد درجة مجمعة إلزامية. كل بُعد له مقياسه ومصدره. أي "شارة" مجمعة في الواجهة مشتقة وقابلة للتفسير بعرض الأبعاد.

| البُعد | المقياس | يُحسب/يُحدد من | على |
|---|---|---|---|
| source_reliability | A (موثوق تماماً) … E (غير موثوق)، F (لا يمكن الحكم) — مقياس Admiralty | تقييم المصدر كما كان معروفاً وقت تسجيل الادعاء | Claim |
| information_confidence | 1 (مؤكد من مصادر مستقلة) … 5 (غير محتمل)، 6 (لا يمكن الحكم) | المحلل أو المحول | Claim |
| data_quality | GOOD / ACCEPTABLE / POOR / UNKNOWN + قائمة issues | قواعد جودة البيانات | كل كائن T1 |
| verification_status | UNVERIFIED / PARTIALLY_VERIFIED / VERIFIED / DISPUTED / REFUTED | الأدلة والتعارضات والمراجعة | Claim |
| freshness | FRESH / AGING / STALE | محسوب: now − (observed_at أو valid_from) مقابل عتبة الـ predicate | Claim (محسوب عند القراءة) |
| completeness | نسبة 0–1 | السمات الإلزامية للنوع الموجودة / المطلوبة | Resolved Entity View |
| uncertainty | حسب النوع: ± للأرقام، `accuracy_m` للمكان، precision للزمن، احتمال تقديري للأحكام | المصدر أو التحليل | Claim، Assessment |

## الاحتمال التقديري (للتقييمات)
مصطلحات مرجعية (RD-ESTIMATIVE-PROBABILITY) مع نطاقات رقمية ثابتة، مثلاً: "مرجح جداً" = 80–95 %. تُعرض الكلمة والنطاق معاً لتجنب سوء الفهم.

## JSON Schema

```json
{
  "$id": "urn:platform:schema:confidence:1",
  "type": "object",
  "properties": {
    "source_reliability": {"enum": ["A","B","C","D","E","F"]},
    "information_confidence": {"enum": [1,2,3,4,5,6]},
    "data_quality": {"type": "object", "properties": {
        "grade": {"enum": ["GOOD","ACCEPTABLE","POOR","UNKNOWN"]},
        "issues": {"type": "array", "items": {"type": "string"}}}},
    "verification_status": {"enum": ["UNVERIFIED","PARTIALLY_VERIFIED","VERIFIED","DISPUTED","REFUTED"]},
    "freshness": {"enum": ["FRESH","AGING","STALE"], "description": "computed at read time"},
    "completeness": {"type": "number", "minimum": 0, "maximum": 1},
    "uncertainty": {"type": "object"}
  },
  "additionalProperties": false
}
```
