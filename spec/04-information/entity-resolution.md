---
id: ER-MODEL
type: information-model
title: Entity Resolution (merge / split without id rewrite)
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
wave: W3
tier: T0
traces: {requirements: [REQ-INF-032, REQ-INF-033, REQ-INF-034], corrects: [CR-15], decided_by: [ADR-P13], closes: [OQ-013]}
---

# Entity Resolution

## 1. الملكية (يغلق OQ-013)
مطابقة الكيانات في **BC02**، لأن الدمج يغير هوية الكيانات التي يملكها BC02، ولا يغير حالة كائن إلا مالكه (A04). BC03 (DOM-07) يحتفظ بالربط والدمج التحليلي (Correlation / Fusion) ويقترح مطابقات فقط.

## 2. التصميم الجوهري: الدمج = رابط، لا إعادة كتابة

```text
SameAsLink
  id, left_ref, right_ref            entity URNs
  decision                           MATCH | NOT_A_MATCH
  case_ref                           EntityResolutionCase
  record [recorded_from, recorded_to)
  decided_by, rationale

Identity cluster = connected component of MATCH links current at known_at K
Canonical id     = smallest ULID in the cluster (deterministic)
```

- **الادعاءات لا تُنقل.** تبقى على `subject_ref` الأصلي.
- الكيان المحلول = اتحاد ادعاءات أعضاء العنقود، ثم قاعدة القيمة الحالية (meta-model §3). التعارضات بين الأعضاء تُكشف بالقواعد نفسها.
- **الفصل (Split)** = إغلاق `recorded_to` لرابط MATCH. كل كيان يعود بادعاءاته تلقائياً (REQ-INF-034).
- لأن الروابط ثنائية الزمن، يمكن السؤال "كم كياناً كنا نظن أنهم واحد في تاريخ K؟".
- `NOT_A_MATCH` يمنع إعادة اقتراح نفس الزوج.

## 3. حالة المطابقة
```text
EntityResolutionCase
  candidates[], matching_method, features{name_forms, phonetic_keys, dates, locations, identifiers}
  score, evidence[], status
  CANDIDATE → UNDER_REVIEW → MATCHED | NOT_A_MATCH | POSSIBLE_DUPLICATE
  MATCHED → SPLIT_REQUIRED → (split) → CANDIDATE
```
`MERGED` في PRJ§13 يُمثل بوجود رابط MATCH ساري (لا حالة منفصلة).

## 4. المعرفات بعد الدمج
طلب بمعرّف عضو في عنقود يعيد الكيان المحلول مع `canonical_urn` و`requested_urn`. لا تحويل صامت للمعرف.

## 5. الأداء (RSK-017)
العناقيد الكبيرة تُحسب تزايدياً وتُخزن مادياً (cluster id لكل كيان، بإصدار record time). حد تحذيري: عنقود > 50 عضواً يتطلب مراجعة (غالباً دمج خاطئ).
