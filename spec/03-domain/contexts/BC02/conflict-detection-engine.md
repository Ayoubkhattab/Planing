---
id: SPEC-CONFLICT-DETECTION
type: component-specification
title: Conflict Detection Engine
wave: W4
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
slice: SLC-04
traces: {requirements: [REQ-INF-025], models: [CONFLICT-MODEL, LIB-CLAIMS-KERNEL], quality: [QAS-CNF-001]}
---

# Conflict Detection Engine

## 1. المشغلات
| الحدث | النطاق المُعاد فحصه |
|---|---|
| EVT-CLM-ASSERTED / CORRECTED / CHANGED | (cluster(subject), predicate) للادعاء |
| EVT-CLM-RETRACTED | نفس المفتاح → قد يصبح تعارض SUPERSEDED |
| EVT-ER-MATCHED / MATCH-CONFIRMED | كل predicates لأعضاء العنقود الجديد |
| EVT-ER-SPLIT | كل predicates للعنقودين الناتجين |
| EVT-MRS/predicate tolerance change (RD-CONFLICT-RULES) | إعادة فحص مجدولة بدفعات |

## 2. الخوارزمية
```text
detect(cluster C, predicate p):
  X := CURRENT claims whose subject ∈ members(C, now) and predicate = p      -- all labels (engine runs as system)
  if cardinality(p) = multi: return                                          -- no single-value conflicts (CF-01 n/a)
  pairs := { (a, b) ∈ X² | overlap(a.valid, b.valid) ∧ incompatible(a, b, p) }  -- CF-01..CF-04 via LIB normalization
  groups := connected components of pairs, split by overlapping window
  for g in groups:
     existing := non-terminal conflict on (C, p) whose window overlaps window(g)
     if existing: add missing members (EVT-CNF-CLAIM-ADDED)
     else: open conflict with members g (EVT-CNF-DETECTED)
  for each non-terminal conflict k on (C, p) not covered by any group:
     SUPERSEDE k (EVT-CNF-SUPERSEDED)
```

## 3. قواعد عدم التوافق (من RD-CONFLICT-RULES)
| القاعدة | incompatible(a, b) إذا |
|---|---|
| CF-01 | predicate أحادي، والقيمتان المطبعتان مختلفتان (نص: language-model؛ أرقام: UCUM + تسامح) |
| CF-02 | فرق رقمي > tolerance(p) |
| CF-03 | مسافة(a, b) > (accuracy_a + accuracy_b) × factor(p) |
| CF-04 | استحالة زمنية/حركية (سرعة ضمنية بين موقعين > max_speed(entity_type)) |
| CF-05 | محجوز لتعارضات المزامنة الميدانية (SLC-11) |

## 4. الخصائص التشغيلية
- المحرك idempotent: إعادة تشغيله على نفس الحالة لا تنتج أحداثاً (inbox + مقارنة المجموعات).
- يعمل بهوية نظام ويرى كل الادعاءات؛ **الرؤية تُطبق عند القراءة** (INV-CNF-04)، لا عند الكشف.
- التوازي: مفتاح التقسيم (tenant, cluster_id, predicate) — لا تعارض بين العمال.
- الهدف: من الالتزام إلى فتح التعارض p95 ≤ 30 ث (QAS-CNF-001).
