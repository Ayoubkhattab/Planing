---
id: SPEC-SITUATION
type: component-specification
title: Situation Membership, Alert Evaluation, COP & Secured Tiles, Notification Delivery
wave: W4
slice: SLC-06
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
traces: {decided_by: [ADR-P06, ADR-P07, ADR-P12], requirements: [REQ-SIT-001, REQ-SIT-002, REQ-SIT-003, REQ-SIT-004, REQ-SIT-005, REQ-SIT-006, REQ-SIT-007, REQ-COM-001, REQ-COM-002], quality: [QAS-PERF-005, QAS-PERF-006, QAS-PERF-007, QAS-SEC-004, QAS-SCAL-002]}
---

# Situation, Alerts, COP & Notifications

## 1. المكونات
```text
Owner events (BC02 observations/claims, BC02 conflicts, BC04 tasks, BC03 assessments)
   ├──► Alert evaluator (critical path, direct on streams)  ─► Alert (AGG-ALERT) ─► Notification fan-out ─► in-app / push
   └──► Membership evaluator ─► Situation membership + change log ─► COP queries, tile invalidation
```
المُقيّمان منفصلان عمداً: التنبيه الحرج لا ينتظر تحديث العضوية (QAS-PERF-005 ≤ 5 ث مقابل QAS-PERF-006 ≤ 10 ث).

## 2. معايير العضوية (SituationCriteria)
كائن X عضو في موقف S عند زمن t إذا:
```text
X.type ∈ S.criteria.object_types
∧ type filters (entity_types / event_types / observation_methods) match
∧ every predicate filter holds on X's resolved view (system visibility, LIB §3)
∧ location(X, t) intersects S.extent(t)              -- buffer extents follow the anchor entity's location
∧ time(X) overlaps S.window                           -- observation: observed_at; event: event_time; entity: valid at t
∧ (include_disputed ∨ no DISPUTED status on filtered predicates)
∧ (include_unvalidated_observations ∨ X.state = VALIDATED)
∧ source reliability ≥ min_source_reliability (when set)
```
- التقييم **بهوية نظام** (كل التسميات)؛ الرؤية تُطبق عند القراءة لكل عضو (INV-SIT-02).
- فهرس مكاني للامتدادات النشطة لكل مستأجر؛ كل حدث يُطابق فقط مع المواقف التي يتقاطع امتدادها مع موقع الكائن.
- كل تغيير عضوية = سجل (member, from/to, cause event, definition_version) → يمكن إعادة إنتاج العضوية تاريخياً (INV-SIT-03).
- تعديل التعريف يعيد حساب العضوية بالكامل كمهمة غير متزامنة، والنتيجة تُنشر كتغييرات عادية.

## 3. تقييم التنبيهات
| النوع | المدخل | الشرط |
|---|---|---|
| measurement_threshold | ملاحظات | قيمة الكمية (بعد تحويل UCUM) تتجاوز العتبة داخل الامتداد |
| enters_extent / leaves_extent | ادعاءات الموقع | تغير الانتماء للامتداد |
| new_observation_in_extent | ملاحظات | ملاحظة جديدة بالأساليب المحددة |
| claim_changed | ادعاءات | تغير قيمة predicate لعضو |
| conflict_opened | تعارضات | تعارض على عضو |
| task_overdue_in_situation | مهام | EVT-TASK-ESCALATED لمهمة مرتبطة بعضو |

- **إزالة التكرار:** (rule, subject) داخل نافذة → زيادة عداد لا تنبيه جديد (INV-ALR-03).
- **التسمية:** max(تسمية القاعدة، تسميات الكائنات المسببة).
- **المستلمون:** مشتركو القاعدة/الموقف **المصرح لهم بتسمية التنبيه فقط**. غيرهم لا يستلم شيئاً (INV-ALR-02) — لا تنبيه منقوص يكشف أن "شيئاً ما" حدث.
- **الضغط:** عند دفعات 50,000 حدث/ث، المُقيّم يعالج القواعد الحرجة أولاً (طابور أولوية)؛ p95 للحرج ≤ 30 ث أثناء الدفعة (QAS-SCAL-002).

## 4. صورة العمليات المشتركة (COP)
- `picture` = أعضاء الموقف المرئيون للقارئ، مع الهندسة من LIB (بعد التزام generalize إن وُجد) وحالة الثقة/النزاع.
- الأعداد في الواجهة على المرئي فقط.
- الطبقات: entities، events، observations، tasks، alerts، assessments (R1: الأربع الأولى + alerts).

## 5. البلاطات المؤمّنة (ADR-P06 §6، ADR-P12)
```text
scope_hash   = H(tenant, clearance.level, sorted(compartments), caveat attrs, org_scope set, generalize params)
data_version = membership version of the situation for that layer (increments on membership/geometry change)
cache_key    = (situation, layer, z, x, y, scope_hash, data_version)
```
- البلاطة تُولد من الأعضاء المرئيين لنطاق الصلاحية فقط. مستخدمون بنفس النطاق يتشاركون الذاكرة؛ نطاقات مختلفة لا تتشارك أبداً (QAS-SEC-004).
- سحب صلاحية يغير `security_version` → يُعاد حساب النطاق للطلب التالي؛ البلاطة القديمة لا تُخدم لأن مفتاحها مختلف.
- الطبقات الأساسية (خرائط أساس) تُخدم من مسار منفصل وتُخزن مشتركة فقط إن وُسمت unclassified.
- هدف الأداء: p95 ≤ 500 ms (QAS-PERF-007)؛ حد ≤ 5,000 عنصر لكل بلاطة مع تجميع (clustering) عند التصغير.

## 6. تسليم الإشعارات
| البند | القاعدة |
|---|---|
| المحتوى | مرجع URN + عنوان من قائمة قوالب آمنة التصنيف (مثل "تنبيه حرج جديد في موقف تتابعه")؛ لا أسماء ولا مواقع (INV-NTF-02) |
| إعادة الفحص | عند الإرسال: security_version للمستلم وتسمية المرجع؛ الفشل → WITHHELD |
| الإعادة | 5 محاولات بتراجع أسي؛ النسخة داخل التطبيق تبقى دائماً |
| ساعات الهدوء | تُحترم إلا للخطورة critical |
| **الدفع في بيئة معزولة** | لا اعتماد على خدمات دفع عامة. قناة دفع داخلية: اتصال دائم من تطبيق الجوال عند توفر شبكة المؤسسة (أو مرحّل MDM داخلي)، مع سحب دوري احتياطي. الاختيار التقني في W8 (مسجل في w8-inputs). |
