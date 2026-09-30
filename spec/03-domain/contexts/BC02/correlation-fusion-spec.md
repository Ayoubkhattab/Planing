---
id: SPEC-FUSION
type: component-specification
title: Coordination Scoping, Correlation Engine and Fusion Rules
wave: W4
slice: SLC-15
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
traces: {requirements: [REQ-CRD-001, REQ-CRD-002, REQ-FUS-001, REQ-FUS-002], models: [CONFIDENCE-MODEL, LIB-CLAIMS-KERNEL], recalibrate_after_pilot: true}
---

# Coordination, Correlation & Fusion

## 1. نطاق المشاركين في التنسيق (REQ-CRD-001)
- التنسيق داخل مستأجر واحد فقط؛ بين المستأجرين عبر توزيع المنتجات (SLC-12) لا غير.
- كل مشارك يرى أقسام نطاق وصوله فقط (`briefing`، `own_responsibilities`، …) **و** الكائنات المرتبطة التي يراها أعضاؤه (قاعدة التسمية).
- الإجراء الذي يتطلب سلطة مؤسسة أخرى: يُنشئ طلب قرار (SLC-08) في نطاقها؛ لا يُعلَّم منجزاً قبل تسجيل القرار (INV-CRD-03).

## 2. محرك الربط (REQ-FUS-001)
```text
on validated observation / new position claim x:
  bucket(x) := (geohash6(location), floor(time / 10 min))
  candidates := items in bucket(x) and its 8 spatial neighbours × adjacent time buckets
  for rule r ACTIVE of each kind:
     for c in candidates with source(c) ≠ source(x):
        s := r.score(x, c)            -- distance normalised by (acc_x + acc_c), |Δt| / window, attribute similarity
        if s ≥ r.threshold and distinct_independent_sources(group) ≥ r.min_distinct_sources:
           upsert proposal (kind, group, score breakdown, rule version)
```
- المحرك بهوية نظام؛ تسمية الاقتراح = أعلى تسمية مدخلاته؛ المراجع يجب أن يرى كل المدخلات.
- الاستقلال: مدخلان من نفس المصدر، أو أحدهما مشتق من الآخر (lineage)، يُعدّان مصدراً واحداً (INV-CRP-04).

## 3. قواعد الدمج عند قبول "same_event" (REQ-FUS-002)
| العنصر | قاعدة الدمج | الوسم في الادعاء المشتق |
|---|---|---|
| زمن الحدث | تقاطع الفترات الغامضة إن وُجد، وإلا الاتحاد مع دقة أدنى | method = fusion-time-v1 |
| الموقع | متوسط موزون بعكس مربع الدقة؛ الدقة الناتجة = 1/√Σ(1/σ²) | method = fusion-location-v1 |
| النوع | الأغلبية بين المصادر؛ التعادل → DISPUTED (لا ترجيح آلي) | — |
| الثقة | information_confidence = "confirmed by other sources" عند ≥ 2 مصدرين مستقلين؛ موثوقية كل مصدر مسجلة وقت الدمج | — |

الادعاءات المدمجة **ادعاءات مشتقة** تستشهد بكل الملاحظات المساهمة (derived_from) — لا تحل محل الأصل ولا تغيره؛ الاختلاف مع ادعاءات قائمة يمر بمحرك التعارض (SLC-04).
