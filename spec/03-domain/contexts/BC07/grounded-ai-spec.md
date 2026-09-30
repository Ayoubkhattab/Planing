---
id: SPEC-AI
type: component-specification
title: Grounded AI — pipeline, authorized retrieval, context packages, grounding, guards, serving
wave: W4
slice: SLC-10
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
traces: {requirements: [REQ-AI-001, REQ-AI-002, REQ-AI-003, REQ-AI-004, REQ-AI-005, REQ-AI-006, REQ-AI-007, REQ-AI-008, REQ-AI-011, REQ-AI-012, REQ-AI-014], quality: [QAS-AI-001, QAS-AI-002, QAS-AI-003, QAS-AI-004, QAS-AI-005], decided_by: [ADR-P06, ADR-P10], matrix: AI-AUTONOMY-MATRIX, recalibrate_after_pilot: true}
---

# Grounded AI

## 1. المسار (PRJ§25، REQ-AI-001)
```text
Submit(operation, input, purpose)                              -- as user U
 → PDP(U, ai.<operation>, scope) ∧ routing(max AIL) ∧ matrix     -- else REFUSED
 → authorized retrieval (§2)                                    -- as U, never as system
 → context package (§3) sealed + hashed
 → model (routing: operation → PRODUCTION model + prompt template version)
 → output guards (§5) → grounding check (§4)
 → COMPLETED | INSUFFICIENT_EVIDENCE
 → reviewable operations create an AI Result (human accepts effects)
```

## 2. الاسترجاع المصرّح (REQ-AI-002، REQ-AI-014)
- **هجين:** بحث نصي على حقائق البحث (SPEC-DISCOVERY §3.1) + متجهات على نفس الحقائق والمقاطع، في إسقاط `vector` (AGG-PROJECTION-VERSION، CR-58) بنفس تسميات الأمن.
- **نفس الضمانات:** فلترة مسبقة بنطاق PDP قبل حساب التشابه، ثم LabelCheck على العناصر المختارة (CR-47). الحقائق المخفية لا تُسترجع ولا تؤثر في الترتيب (P-51..P-53 تنطبق على الاسترجاع).
- المحتوى المسترجع = حقائق وادعاءات وملاحظات ومقاطع وثائق **مرئية للمستخدم الآن**، مثبتة بإصدارها.

## 3. حزمة السياق
| الحقل | القاعدة |
|---|---|
| items | ≤ ميزانية الرموز للمسار؛ لكل عنصر: URN، إصدار أو known_at، تسمية، درجة، نص |
| ترتيب | الأعلى صلة أولاً؛ عنصر واحد لكل ادعاء (بعد الحل: القيمة الحالية أو كل المرشحين إن كان DISPUTED مع وسم ذلك) |
| الختم | hash على العناصر + قالب التعليمات + معرّف النموذج |
| التسمية | label(package) = max(labels(items)) ≤ تصريح المستخدم |
| التخزين | مشفر بمفتاح المستأجر؛ فئة سجلات ai-logs بجدول احتفاظ |

## 4. التأريض والأدلة غير الكافية (REQ-AI-003/004، QAS-AI-001/002)
```text
coverage := fraction of the question's required facets matched by context items (retrieval stage)
if coverage < θ_cov (default 0.5) → INSUFFICIENT_EVIDENCE (no generation)
generate with instructions: answer only from items; cite item ids per statement; say "insufficient" otherwise
for each statement s:
   cited := items referenced by s
   supported(s) := entailment_check(s, cited) ≥ θ_ent (default 0.8)    -- verifier model, separate from generator
drop unsupported statements; if none remain → INSUFFICIENT_EVIDENCE
```
- الأحكام تُعرض مع استشهاداتها؛ الادعاءات المتنازع عليها تظهر كمتنازع عليها، لا كحقيقة.
- العتبات قرارات مفوضة تُعاير بالتقييم وبعد Pilot (RSK-027).

## 5. الحراسات (REQ-AI-012، QAS-AI-004)
| الخطر | الضابط |
|---|---|
| حقن تعليمات في المحتوى المسترجع | المحتوى يُمرر كبيانات معلّمة (delimited)؛ الأدوات المتاحة = قائمة العملية فقط؛ أي نداء أداة خارج القائمة أو بمعاملات تتجاوز النطاق يُرفض؛ المحتوى لا يغيّر المستلمين ولا AIL |
| تسريب | المخرج لا يُرسل لأي وجهة خارجية؛ روابط خارجية تُزال؛ النماذج الخارجية ممنوعة لأي سياق مصنف (REQ-AI-011) |
| تجاوز المستأجر | الاسترجاع وذاكرات السياق لكل مستأجر؛ لا مشاركة بين المستخدمين |
| تسمية المخرج | = تسمية الحزمة؛ نسخ المخرج إلى منتج يخضع لقاعدة المنتج (SPEC-PKA §1) |
| سجل | الطلب، hash الحزمة، النموذج، القالب، المخرج — في التدقيق المشفر |

## 6. الاستقلالية (REQ-AI-008)
الحد الأقصى في R2: AIL3 (مساعدة ضمن سير عمل مع موافقة بشرية). لا أداة "كتابة" في R2؛ أدوات "اقتراح" تنشئ AI Results فقط. AIL5 غير قابل للتمثيل في مخطط التوجيه (max 4) ولا في المصفوفة.

## 7. التشغيل (TD-18، TD-19)
- خادم استدلال محلي (vLLM) لكل خلية على مجمع GPU بحصص لكل مستأجر؛ مهام الاستخراج الدفعية عبر Kueue (TD-12).
- خادم تضمينات منفصل؛ نموذج التضمين نسخة نموذج بدورة حياتها؛ تغييره = إصدار إسقاط `vector` جديد.
- الأهداف: أول رمز ≤ 3 ث، إجابة كاملة p95 ≤ 20 ث عند 50 طلباً متزامناً لكل خلية (QAS-AI-003) — تُعاير بعد Pilot.
- محاسبة: GPU-hours وطلبات لكل مستأجر وعملية (QAS-AI-005، OpenCost).
