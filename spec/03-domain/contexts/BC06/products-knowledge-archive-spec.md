---
id: SPEC-PKA
type: component-specification
title: Product Generation, Distribution, Knowledge Suggestion, Archive Packages, Historical Reconstruction
wave: W4
slice: SLC-12
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
traces: {requirements: [REQ-PRD-001, REQ-PRD-002, REQ-PRD-003, REQ-PRD-004, REQ-PRD-005, REQ-KNW-001, REQ-KNW-002, REQ-KNW-003, REQ-ARC-001, REQ-ARC-002, REQ-ARC-003, REQ-ARC-004], quality: [QAS-PRD-001, QAS-PRD-002, QAS-KNW-001, QAS-ARC-001, QAS-ARC-002, QAS-ARC-003], recalibrate_after_pilot: true}
---

# Products, Knowledge & Archive

## 1. توليد المنتج (REQ-PRD-001..003)
```text
generate(product P, author A):
  K := now                                             -- pin
  for section s in template(P).sections:
     rows := declared_query(s.binding.query, s.binding.parameters ⊕ P.parameters, as A, known_at = K)
     rows := rows where label(row) ≤ P.label            -- never above the product label
     render s (maps via DU-12 tiles for A's scope; charts; tables; key judgments with estimative terms)
  artifacts := PDF (+ DOCX if template allows), each SHA-256 hashed
  citations := every object used, pinned (URN + version / known_at)
```
- **مهمة غير متزامنة** (REQ-PLT-005)؛ الهدف ≤ دقيقتين لـ 30 صفحة و10 خرائط (QAS-PRD-001).
- المحتوى الأعلى من تسمية المنتج يُستبعد ويُسجل داخلياً للتدقيق فقط؛ **لا يظهر في المنتج أي عدّ أو إشارة للمستبعد** (A21، QAS-PRD-002).
- الأقسام السردية وحدها تُحرّر يدوياً؛ الأقسام المرتبطة ببيانات تتغير بإعادة التوليد فقط.
- الأقسام التي صاغها AI (R2، SLC-10) تحمل وسم "AI draft" ولا يُقدم المنتج دون مراجعتها.

## 2. التوزيع (REQ-PRD-004/005)
- لكل مستلم: فحص (تصريح ≥ تسمية المنتج) ∧ (ضمن الجمهور المعتمد).
- **علامة مائية لكل نسخة:** مرئية (اسم/معرّف المستلم، الإصدار، الوقت) + غير مرئية (معرّف توزيع في بيانات الملف الوصفية وتشفير خفيف في هوامش الصفحات). كشف تسرب نسخة يدل على مستلمها.
- المستلمون غير المصرح لهم يُستبعدون ويُبلغ الموزِّع بأسمائهم (لا يكشف ذلك محتوى).
- السحب يوقف التنزيل ويُبلغ المستلمين.

## 3. اقتراح المعرفة (REQ-KNW-003، QAS-KNW-001)
```text
suggest(context: task_type | plan | area, user U):
  candidates := PUBLISHED knowledge with a relationship to context.task_type,
                plan activities' task types, plan area (spatial intersection) or entity types in scope
  rank by: exact task-type match > plan-type match > area overlap > entity type; then reuse count; then recency
  return visible to U only, top 10
```
استخدام اقتراح في خطة أو مهمة يُسجل `CMD-KNO-RECORD-REUSE` (مؤشر OUT-06).

## 4. الحزم الأرشيفية (REQ-ARC-001..003)
| البند | القرار (R2-Q6) |
|---|---|
| البنية | **BagIt (RFC 8493)**: `data/` + manifests SHA-256 + `bag-info.txt` |
| البيانات الوصفية | وصف السجل + المنشأ + سجل الوصول + أحداث الحفظ (على نمط PREMIS) |
| الصيغ | الأصل دائماً + تمثيل حفظ: PDF/A-2b للوثائق، GeoTIFF/COG وGeoPackage للمكاني، CSV/JSON موثقة للبيانات |
| السلامة | عند الاستيعاب، عند كل استرجاع، ودورياً (≥ سنوياً) |
| التخزين | Object Storage بقفل WORM؛ نسخة ثانية في موقع DR |
| الطبقات | warm: استرجاع ≤ دقيقة؛ cold/offline: طلب مرحلي ≤ 24 ساعة (QAS-ARC-001) |

## 5. إعادة البناء التاريخي (REQ-ARC-004، QAS-ARC-002)
| مصدر العنصر | كيف | الوسم |
|---|---|---|
| ادعاءات T1 | LIB-CLAIMS-KERNEL resolve(T, K) | RECORDED |
| إصدارات T2 (خطة، قرار، سياسة، تقييم) | الإصدار الساري عند T والمسجل قبل K | RECORDED |
| حالة Aggregate من تاريخه (مهمة في لحظة) | إعادة تشغيل `*_history` حتى K ثم اختيار الحالة عند T | RECONSTRUCTED |
| عضوية موقف، توفر أصل | إعادة تقييم القواعد على الحالات المعاد بناؤها | RECONSTRUCTED |
| مواقع بين ملاحظتين | استيفاء بقاعدة معلنة (خطي، حد سرعة) | INFERRED (rule id) |
| بيانات مُتلفة أو غير مسجلة | لا شيء | UNKNOWN |
| بيانات مؤرشفة | استرجاع من الحزمة | RECORDED (archive ref) |

التقرير يعمل بصلاحيات طالبه (INV-REC-03)؛ العناصر غير المرئية غائبة، لا موسومة.
