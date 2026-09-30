---
id: LIB-CLAIMS-KERNEL
type: library-specification
title: Claims & Temporal Kernel — shared library specification
wave: W4
slice: SLC-02
tier: T0
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
traces: {changed_in: [SLC-04], mitigates: [RSK-019], decided_by: [ADR-P01, ADR-P02, ADR-P03, ADR-P06, ADR-P13], models: [META-MODEL, TEMPORAL-MODEL, CONFIDENCE-MODEL], requirements: [REQ-INF-021, REQ-INF-022, REQ-INF-023, REQ-INF-024, REQ-INF-026]}
---

# Claims & Temporal Kernel — مواصفة المكتبة المشتركة

مكتبة واحدة داخل BC02 تنفذ كل منطق الادعاءات والزمن. **لا يعيد أي مكوّن تنفيذ هذا المنطق** (RSK-019). المكتبة لا تعرف HTTP ولا محرك التخزين (FIT-10)؛ تتعامل عبر منفذ مستودع (repository port).

## 1. الأنواع

```text
Instant        = UTC timestamp, microsecond precision
Interval       = { from: Instant, to: Instant | ∞ }            half-open [from, to)
FuzzyInterval  = { start?, end?, precision, uncertainty_before?, uncertainty_after? }
ClaimKey       = (tenant_id, subject_urn, predicate)
ClaimRecord    = { id, key, value, valid: Interval, record: Interval, sources[], supersedes?, confidence, label, status_hint }
Visibility     = function(label) → bool          -- built from the caller's allowed_scope (ADR-P06)
ResolvedValue  = { predicate, status: EMPTY | SINGLE | CORROBORATED | DISPUTED, values[], claims[], confidence }
```

## 2. العمليات (كلها داخل معاملة المستدعي)

| العملية | المدخل | الأثر | الأخطاء |
|---|---|---|---|
| `assert(input, now)` | ClaimInput | ينشئ سجلاً `record=[now, ∞)` | CLAIM_INVALID |
| `correct(claim_id, replacement, now)` | — | `recorded_to(old)=now` + سجل بديل بـ `supersedes=old` | CLAIM_INVALID_STATE_TRANSITION |
| `record_change(claim_id, t_change, new_value, now)` | t ∈ (valid.from, valid.to) | `recorded_to(old)=now`؛ نسخة من القديم `valid=[from, t)`؛ سجل جديد `valid=[t, old.to)` | CHANGE_TIME_INVALID |
| `retract(claim_id, now)` | — | `recorded_to(old)=now` | CLAIM_INVALID_STATE_TRANSITION |
| `resolve(key, valid_at, known_at, visible)` | — | ResolvedValue (§3) | — |
| `resolve_entity(subject, valid_at, known_at, visible)` | — | map predicate → ResolvedValue + completeness | — |
| `history(key, filters, visible)` | — | سجلات مرتبة (record.from) | — |
| `positions(subject, [from,to), known_at, visible, generalize?)` | — | مسار مرتب زمنياً | — |

`now` يُمرَّر من طبقة التطبيق من ساعة الخادم **فقط**؛ لا تقبل المكتبة زمن تسجيل من العميل (INV-CLM-02).

## 3. خوارزمية الحل (Resolve) — معيارية

```text
resolve(key, T, K, visible):
  C := { c ∈ claims(key) | c.valid.from ≤ T < c.valid.to
                          ∧ c.record.from ≤ K < c.record.to
                          ∧ visible(c.label) }
  C := C minus claims retracted-as-known-at-K           -- implied by record interval
  if C = ∅                      → EMPTY
  groups := partition C by normalized(value)            -- normalization per predicate: language-model for text,
                                                        --   unit conversion to canonical UCUM for numbers,
                                                        --   tolerance (RD-PREDICATES) for numbers and geometry
  if cardinality(predicate) = multi → SINGLE-or-CORROBORATED per group, return all groups
  if |groups| = 1:
       status := |C| > 1 ? CORROBORATED : SINGLE
  else:
       if conflict_resolution(key, T) known at K selects claim p and p ∈ C
            → SINGLE (value of p), with conflict ref           -- SLC-04
       else → DISPUTED, values = all groups (no automatic winner)
  confidence := per-group: max source_reliability (by Admiralty order), min information_confidence,
                verification from evidence links, freshness computed vs predicate threshold at T
  return ResolvedValue
```

**قاعدة ملزمة:** لا ترجيح تلقائي بالثقة بين قيم متعارضة (META-MODEL §3).
**قاعدة الرؤية:** الادعاءات غير المرئية تُستبعد قبل كل شيء، فلا تؤثر في الحالة أو العدد أو الاكتمال (INV-ENT-02، A21). هذا يعني أن مستخدمَين قد يريان `SINGLE` و`DISPUTED` لنفس السمة؛ وهذا صحيح ومقصود.

## 4. الاكتمال (completeness)
`completeness = |{p ∈ required(entity_type) : resolve(p).status ≠ EMPTY}| / |required(entity_type)|` محسوبة على **المرئي فقط**.

## 5. التعميم المكاني (obligation `generalize`)
عندما تعيد السياسة التزام `generalize(min_accuracy_m)`: تُستبدل الهندسة بمركز خلية شبكية بحجم ≥ `min_accuracy_m`، ويُضبط `accuracy_m = max(original, min_accuracy_m)`، ويُعلَّم الناتج `GENERALIZED`. التعميم حتمي (نفس المدخل → نفس الخلية) لمنع إعادة البناء بالتكرار.

## 6. متطلبات الأداء على المكتبة
| العملية | الهدف | الأساس |
|---|---|---|
| `resolve_entity` للحالة الحالية | p95 ≤ 50 ms داخل المكتبة (≤ 300 ms طرفاً لطرف، QAS-PERF-013) | جدول current مادي (المفتاح ClaimKey، record.to = ∞) |
| `resolve_entity` as-of | p95 ≤ 500 ms | فهرس على (key, valid, record) |
| `assert` | يدخل في ميزانية QAS-PERF-001 | إدراج + تحديث current لنفس المفتاح في نفس المعاملة |

**جدول current:** صف لكل ClaimRecord ساري التسجيل (record.to = ∞)؛ يُحدَّث في نفس معاملة الأمر، فيضمن قراءة ما كُتب (read-your-writes). العروض المحلولة المادية للبحث تُبنى لاحقاً من الأحداث (SLC-05).

## 7. الحل عبر عناقيد الهوية (أُضيف في SLC-04)
```text
claims(key) where key = (tenant, subject, predicate) is evaluated as:
  members := members(cluster(subject, K), K)            -- identity cluster as known at K (ER-MODEL)
  claims  := ⋃ claims((tenant, m, predicate)) for m ∈ members
```
- `resolve_entity(any member)` يعيد نفس النتيجة مع `canonical_urn` و`requested_urn`.
- أعضاء العنقود غير المرئيين للقارئ تُستبعد ادعاءاتهم كما يُستبعد أي ادعاء غير مرئي؛ ولا يُكشف وجودهم في `identity-cluster`.
- الأداء: جدول `identity_clusters` مادي؛ الحمل الإضافي على القراءة الحالية ≤ 20 % (QAS-PERF-015).

## 8. اختبارات المطابقة الإلزامية للمكتبة
- مجموعة oracle زمنية (QAS-TMP-001): 500 حالة (T, K) تشمل التصحيح، تغير الواقع، السحب، الفترات المفتوحة، الحدود الدقيقة `[from, to)`.
- خصائص: P-21..P-28 في `invariant-properties-slc02.md`، وP-41..P-48 في `invariant-properties-slc04.md`.
