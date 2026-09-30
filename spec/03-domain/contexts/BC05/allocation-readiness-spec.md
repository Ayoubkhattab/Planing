---
id: SPEC-ALLOCATION
type: component-specification
title: Allocation Checks, Capacity Ledger, Contention, Pre-emption, Availability & Readiness
wave: W4
slice: SLC-09
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
traces: {requirements: [REQ-RES-003, REQ-RES-004, REQ-RES-006, REQ-RES-007, REQ-RES-008, REQ-RES-009, REQ-RES-010, REQ-RES-011, REQ-RES-012, REQ-RES-013, REQ-RES-014], quality: [QAS-RES-001, QAS-RES-002], closes: [DEBT-001], recalibrate_after_pilot: true}
---

# Allocation & Readiness

## 1. فحوص التخصيص (PRJ§63 — بالترتيب، كل فحص برمز فشل خاص)
| # | الفحص | رمز الفشل |
|---|---|---|
| 1 | الصلاحية: PDP على (requester, allocate, pool) | AUTHZ_DENIED |
| 2 | النوع: نوع المورد يطابق احتياج الهدف (task type / activity) | RESOURCE_TYPE_MISMATCH |
| 3 | الحالة: المجمع ACTIVE | POOL_NOT_ACTIVE |
| 4 | الزمن: النافذة ضمن نافذة الهدف | WINDOW_OUTSIDE_TARGET |
| 5 | الجغرافيا: نطاق المجمع يغطي موقع الهدف (إن حُدد) | GEOGRAPHY_MISMATCH |
| 6 | السياسة: التزامات PDP (مثل REQUIRE_APPROVAL) | POLICY_DENIED |
| 7 | السعة والتوفر والالتزامات: حجز في دفتر السعة (§2) | CAPACITY_UNAVAILABLE |

## 2. دفتر السعة وحل التنافس (INV-RPL-02، INV-ALC-02)
```text
ledger bucket = (tenant, pool, hour) { capacity, committed }
commit(alloc):  for each hour h in alloc.window:
                   require bucket(h).committed + q ≤ bucket(h).capacity
                   bucket(h).committed += q            -- one transaction, buckets locked in ascending h order (no deadlock)
ordering:       requests for the same pool are collected in 250 ms windows,
                sorted by (priority desc, requested_at asc), then committed one by one
```
- الترتيب داخل النافذة يحقق REQ-RES-008 (الأولوية ثم الوقت) بشكل حتمي؛ الكلفة ≤ 250 ms إضافية على طلب التخصيص.
- الإفراج يعيد الكمية غير المستهلكة لكل ساعة متبقية.
- **الدقة الساعية** قرار مفوض؛ يُعاد النظر بعد Pilot (RSK-027).

## 3. الاستباق (REQ-RES-009)
لا استباق آلي. تخصيص بأولوية أعلى لا يجد سعة يُرفض مع قائمة التخصيصات الأدنى أولوية التي تحجز السعة. الاستباق = قرار (BC04 Decision من نوع `resource-preemption`) من سلطة نطاق المجمع، ثم `CMD-ALC-PREEMPT` لكل تخصيص متأثر، وإشعار أصحاب المهام.

## 4. التوفر (INV-AST-01، QAS-RES-002)
```text
available(asset, [t1,t2)) =
   state = IN_SERVICE
 ∧ ∀ required cert c: c.valid ⊇ [t1,t2)
 ∧ ¬∃ maintenance(PLANNED|IN_PROGRESS) overlapping
 ∧ ¬∃ reservation(HELD|CONFIRMED) overlapping (unless the caller's own)
 ∧ ¬∃ assignment(ACTIVE) overlapping
```
عرض توفر مادي لكل أصل بفترات مشغولة (interval index)، يُحدث من الأحداث؛ الأوامر تعيد الفحص على المصدر.

## 5. الجاهزية (REQ-RES-013)
`readiness(subject, role, t)` يوسّع SPEC-ELIGIBILITY: لكل بند في متطلبات الدور النشطة — كفاءة/مؤهل/شهادة (كما في الأهلية) + **حداثة التدريب** (آخر تدريب ضمن `recency`) + **الخبرة** (مدة أداء الدور من سجل التعيينات). الناتج: حالة مجمعة بنفس ترتيب الأسبقية + قائمة الفجوات. للوحدة: نسبة الأعضاء الجاهزين لكل دور.

## 6. إغلاق DEBT-001
ملاحظات الموارد النصية في R1 (`resource_notes` في إصدارات الخطط وحقل المهمة) تُرحّل:
1. محاولة مطابقة آلية لأسماء الأصول والمجمعات → اقتراح مراجع.
2. المخطط يقبل أو يرفض؛ غير المطابق يبقى ملاحظة موسومة `legacy_note`.
3. تقرير ترحيل لكل مستأجر. لا تُحذف الملاحظة الأصلية (تاريخ).
