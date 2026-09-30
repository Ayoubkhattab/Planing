---
id: SPEC-ER-CANDIDATES
type: component-specification
title: Entity Resolution Candidate Generation
wave: W4
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
slice: SLC-04
traces: {requirements: [REQ-INF-032, REQ-SRC-003], models: [ER-MODEL, LANGUAGE-MODEL], quality: [QAS-ER-001, QAS-ER-002, QAS-ER-003]}
---

# Entity Resolution — Candidate Generation

## 1. المبدأ
المولّد **يقترح فقط** (CANDIDATE)؛ لا دمج آلي أبداً (INV-ER-04). الهدف أعلى استدعاء (recall) عند مرحلة الاقتراح، مع دقة كافية لعدم إغراق طابور المراجعة.

## 2. الحجب (Blocking) — لتجنب المقارنة O(n²)
لكل كيان تُحسب مفاتيح حجب من الادعاءات الحالية (كل المستويات؛ المولّد يعمل بهوية نظام):
| المفتاح | المصدر |
|---|---|
| NAME_TOKEN | كل رمز من الاسم المطبّع (language-model N1–N10) بعد حذف الروابط (بن/ابن/bin) |
| PHONETIC | المفتاح الصوتي لكل مكوّن اسم |
| TRANSLIT | صيغ النقحرة المطبّعة |
| GEOHASH6 | خلية geohash بدقة 6 (~1.2 كم) للموقع الحالي والمواقع التاريخية |
| IDENT | معرفات رسمية (رقم هوية، سجل تجاري) إن وُجدت كادعاءات |
| YEAR | سنة الميلاد / التأسيس ± 1 |

المرشحون = الكيانات من نفس النوع (أو نوع متوافق) التي تشترك في مفتاحين على الأقل، أو في IDENT واحد.

## 3. التقييم
`score = Σ weight_f × similarity_f` على السمات المعرفة في Match Ruleset:
| السمة | التشابه |
|---|---|
| الاسم | أفضل تطابق بين كل الصيغ (Jaro-Winkler على المطبّع + تطابق صوتي + تطابق نقحرة) |
| الموقع | 1 − min(1, distance / (acc₁ + acc₂ + d₀)) |
| التواريخ | تداخل الفترات الغامضة (CERTAIN / POSSIBLE / NO) |
| المعرفات | 1 عند التطابق التام، و−∞ عند تعارض معرف فريد |
| العلاقات | Jaccard على الجيران المشتركين |

## 4. العتبات والحدود
- `score ≥ propose_threshold` → CANDIDATE (EVT-ER-PROPOSED) مع كل المقارنات مسجلة.
- حد أقصى 10 مرشحين لكل كيان في كل تشغيل (أعلى الدرجات).
- لا اقتراح إذا وُجد NOT_A_MATCH بين العنقودين، أو كانا في نفس العنقود، أو توجد حالة غير نهائية للزوج.

## 5. التشغيل
- تزايدي على EVT-ENT-REGISTERED وتغير ادعاءات الاسم/الموقع/المعرف؛ مفتاح التقسيم (tenant, entity_type, blocking bucket).
- إعادة تشغيل كاملة مجدولة عند تفعيل Ruleset جديد (دفعات، أولوية منخفضة).
- الهدف: من تسجيل الكيان إلى ظهور المرشحين p95 ≤ 60 ث (QAS-ER-003).

## 6. التقييم الإلزامي قبل التفعيل (INV-MRS-03)
مجموعة اختبار موسومة (أزواج مطابقة وغير مطابقة) عربية وإنجليزية ومختلطة، تشمل: الهمزات، الألقاب، سلاسل النسب، النقحرة المتعددة، الأسماء الشائعة. مقاييس: استدعاء المرشحين ≥ 95 % (QAS-ER-001)، دقة المقترحات ≥ 60 % (QAS-ER-002).
