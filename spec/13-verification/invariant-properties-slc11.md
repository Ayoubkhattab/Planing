---
id: PROP-SLC11
type: property-spec
title: Property-Based Invariant Specifications — SLC-11
wave: W6
slice: SLC-11
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Property-Based Invariants — SLC-11

لأي طابور أوامر Q، ولأي نمط انقطاع (قطع النقل عند مواضع عشوائية، إعادة تسليم، إعادة ترتيب الدفعات):

| ID | الخاصية |
|---|---|
| P-111 | الحالة النهائية على الخادم بعد المزامنة لا تعتمد على نقاط الانقطاع (نفس النتيجة كأن المزامنة تمت مرة واحدة) |
| P-112 | كل client_command_id يُطبق مرة واحدة على الأكثر |
| P-113 | لا أمر مغير للحالة يُطبق على إصدار غير base_version (لا LWW) |
| P-114 | كل أمر إما مطبق، أو في تعارض مزامنة، أو مرفوض بسبب مسجل — لا أمر مفقود |
| P-115 | recorded_from = زمن استلام الخادم دائماً؛ device_time الأصلي محفوظ |
| P-116 | لا محتوى في أي حزمة بتسمية أعلى من صلاحية المستخدم وقت البناء أو من مستوى المستأجر للعمل دون اتصال |
