---
id: SPEC-LOGISTICS
type: component-specification
title: Logistics & Supply Rules — item catalog, reuse of Resource Pool/Allocation, movement
wave: W4
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-27'
slice: SLC-18
traces: {closes: [R3-Q3], corrects: [CR-62], requirements: [REQ-LOG-001, REQ-LOG-002, REQ-LOG-008, REQ-LOG-013, REQ-LOG-014]}
recalibrate_after_pilot: true
---

# Logistics & Supply Rules

## 1. كتالوج أصناف الإمداد (RD-LOGISTICS-ITEM-TYPES)
مثل RD-ASSET-TYPES/RD-RESOURCE-TYPES (R2-Q1) وRD-HAZARD-CATEGORIES (SLC-17): كتالوج مرجعي واحد لكل مستأجر، لا أصناف مثبَّتة في الكود. `item_pool` في `CMD-LGR-REQUEST` يشير إلى AGG-RESOURCE-POOL بـ `resource_type` من هذا الكتالوج (وقود، غذاء، معدات طبية، قطع غيار، ...). لا افتراض قائمة مغلقة.

## 2. لماذا لا يوجد Aggregate منفصل للمخزون (Inventory)
قرار R3-Q3: **المخزون هو AGG-RESOURCE-POOL من SLC-09، بلا تعديل على تعريفه**. مجمع الموارد كان مصمَّماً أصلاً لأي مورد "قابل للعد أو القياس بسعة متغيرة زمنياً" — صنف إمداد في مستودع يطابق هذا التعريف حرفياً دون أي حقل إضافي. السعة، دفتر السعة بدقة الساعة، وقيد قاعدة البيانات الذي يمنع تجاوزها (INV-RPL-02) تنطبق دون تغيير. **لا محرك تخصيص ثانٍ**: كل التزام كمية — سواء لمهمة (SLC-03/08) أو لطلب إمداد (SLC-18) — يمر عبر نفس AGG-ALLOCATION ونفس فحوصات SPEC-ALLOCATION §1 وترتيب التنافس بالأولوية ثم الوقت (§2، REQ-LOG-014). هذا يمنع تكرار "Aggregate Fragmentation" الذي حذّر منه SPEC-RISK-CONTINGENCY §2، بشكله المعاكس هنا: بناء نموذج مخزون مواز بدل التوسع في نموذج قائم.

## 3. الربط بين Logistics Request وAllocation (CR-62)
`CMD-ALC-REQUEST` كان يقبل `target` كـ URN عام موصوفاً بأنه "task/activity" فقط. **CR-62** يوسّع نص الشرط (لا صيغة الحمولة — `target!:urn` كانت عامة أصلاً) ليشمل `logistics-request` كبديل ثالث. AGG-LOGISTICS-REQUEST **لا ينشئ حالته الخاصة بشكل مستقل** بعد الطلب الأولي — كل انتقال لاحق (APPROVED، PENDING_APPROVAL، REJECTED) مدفوع بحدث نظامي من AGG-ALLOCATION نفسه (EVT-ALC-COMMITTED/-APPROVAL-REQUIRED/-REJECTED). هذا **ليس أثراً جانبياً صامتاً** بمعنى درس SLC-09/SLC-17: الحدث موثّق، معروف الاستهلاك، ومسجَّل في المصفوفة الكاملة لـ AGG-LOGISTICS-REQUEST (SL-05) — لا تغيير خفي، بل تفويض صريح لحكم القبول/الرفض لنفس الآلية المعتمدة أصلاً في SLC-09 بدل تكرارها.

## 4. لماذا Movement ليس Aggregate منفصلاً
DOM-16 يذكر Movement كعنصر مستقل، لكنه — كما SLC-17 مع Emergency/Crisis — **ليس له دورة حياة أو هوية خاصة به**؛ هو تاريخ نقاط تتبع (checkpoints) لشحنة واحدة. القرار: `MovementEvent` كمكوّن داخلي append-only ضمن AGG-SHIPMENT (`CMD-SHP-RECORD-CHECKPOINT`)، بنفس منطق `CustodyEntry` الخاص بـ AGG-ASSET (INV-AST-02) وSeverityHistory الخاص بـ AGG-INCIDENT — سجل تاريخي لا يُكتب فوقه، لا كيان مستقل.

## 5. لماذا Storage ليس Aggregate منفصلاً
"موقع التخزين" هو ببساطة **نطاق** (scope) لمجمع موارد قائم (AGG-RESOURCE-POOL بمعرّف يتضمن الموقع) وليس بحاجة إلى مفهوم مستقل — يماثل §2 أعلاه: لا تكرار للنمذجة.

## 6. لماذا "Supply" ليس Aggregate منفصلاً
"الإمداد" هو الاسم العام لعملية تلبية طلب — أي **AGG-LOGISTICS-REQUEST + AGG-SHIPMENT معاً**، لا كائن ثالث. تسمية الشريحة (Logistics & Supply) تصف القدرة (CAP-08.03)، لا تستلزم Aggregate بذلك الاسم.

## 7. قواعد التسليم الجزئي
| القاعدة | التفصيل |
|---|---|
| لا تقريب للأعلى | `delivered_quantity` المسجَّلة عند `CMD-SHP-DELIVER` هي الكمية الفعلية المستلمة دائماً؛ إن قلَّت عن الكمية المخطَّطة فالحدث ينص على ذلك صراحة (INV-SHP-02) |
| قرار AGG-LOGISTICS-REQUEST | `FULFILLED` فقط عندما `delivered_quantity = requested quantity`؛ أي نقص — بما فيه فقدان كامل (DAMAGED/LOST) — ينتج `PARTIALLY_FULFILLED` (INV-LGR-03) |
| لا إعادة إرسال تلقائية | الكمية الناقصة في `PARTIALLY_FULFILLED` لا تُعاد جدولتها تلقائياً؛ تغطيتها تتطلب `CMD-LGR-REQUEST` جديداً صريحاً — تبسيط متعمَّد (A17)، لا خلل |
| الاستهلاك | يُسجَّل على AGG-ALLOCATION فقط من نتيجة شحن مؤكَّدة (تسليم، تلف، فقدان)، أبداً عند الإرسال (INV-LGR-05) — يمنع اعتبار كمية "في الطريق" مستهلكة قبل تأكيد وصولها فعلياً |

## 8. قيم إشارية غير مقاسة
مثل SLC-17 (RSK-028، أشد من RSK-027 الخاص بـ R2 نفسها): أي هدف زمني (مدة الشحن، زمن الاستجابة للطلب) في هذه الشريحة **إشاري غير مقاس** — SLC-18 تعتمد مباشرة على AGG-RESOURCE-POOL/AGG-ALLOCATION المصمَّمين في SLC-09 (R2)، وهما نفسهما لم يُقاسا بعد بتجربة Pilot R2. هذا يجعل SLC-18 أكثر تعرضاً فعلياً لمخاطرة RSK-028 من SLC-17 (التي اعتمدت على R1 المُصادَق عليه فقط) — انظر `14-slices/SLC-18/readiness.md`.
