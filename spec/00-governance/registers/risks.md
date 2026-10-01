---
id: REG-RSK
type: register
title: Risk Register
wave: W0
tier: T3
owner_role: Orchestrator
status: DRAFT
approved_by: null
approved_at: null
consumers: []
---

# Risk Register

## risks

_28 items_

| id | description | probability | impact | mitigation | owner | residual_risk | status | note |
|---|---|---|---|---|---|---|---|---|
| RSK-001 | نطاق 26 مجالاً للإصدار الأول | H | H | شرائح رفيعة + HAP-02 | Sponsor | TBD | open | — |
| RSK-002 | غموض النموذج الزمني | M | H | ADR-P01 قبل التصميم المنطقي | BC02 | TBD | open | — |
| RSK-003 | تسرب صلاحيات عبر الإسقاطات/Cache/Tiles | M | H | ADR-P06 + اختبارات الاستدلال | Security | TBD | open | — |
| RSK-004 | إفراط في نموذج الأدلة | M | M | ADR-P03 | BC02 | TBD | open | — |
| RSK-005 | عبء تشغيلي يفوق قدرة الفريق | M | H | ADR-P05 | Platform | TBD | mitigated | operators + GitOps; ops team size still UNK-012 |
| RSK-006 | ضعف مطابقة الأسماء العربية | H | M | ADR-P15 | BC02 | TBD | open | — |
| RSK-007 | تعارض المحو القانوني مع الثبات | M | H | ADR-P08 | Privacy | TBD | open | — |
| RSK-008 | تعارضات المزامنة الميدانية | M | H | ADR-P09 | BC02 | TBD | open | — |
| RSK-009 | قدرات AI محدودة في بيئة معزولة | M | M | اختبار نماذج محلية مبكراً | AI | TBD | open | — |
| RSK-010 | الدراسة تتحول لوثائق بلا تنفيذ | M | H | A20 + معيار V6§2 + جاهزية بالشريحة | Orchestrator | TBD | open | — |
| RSK-011 | تأخر إجابات أصحاب القرار | H | H | بنك الأسئلة مبكراً | Sponsor | TBD | mitigated | answers provided by delegated decision |
| RSK-012 | تعدد معاني المصطلحات (Policy, Assessment, Decision…) يسبب نماذج متعارضة بين الفرق (W0) | H | M | glossary.md ملزم + SL-26 | Orchestrator | TBD | open | — |
| RSK-013 | أولوية التوسع تدفع إلى تعقيد مبكر (Premature Scale) يرفع التكلفة والعبء التشغيلي على فريق صغير | M | H | مبدأ Scale-Ready not Scale-First (SR-00): التوسع مصمم ومختبر، لا منشور مسبقاً | Architecture Board | L | open | — |
| RSK-014 | قرارات W1 مفوّضة لوكيل؛ قد تخالف واقع المؤسسة عند تعرّفها | M | M | مصادقة المالك عند G6؛ كل قرار قابل للمراجعة؛ أثر كل إجابة مسجل | Project Owner | L | open | — |
| RSK-015 | البيئة المعزولة كخط أساس تحد من جودة نماذج AI المتاحة | M | M | تقييم نماذج محلية مبكراً (SLC-10)؛ AIL≤2 في R1 يقلل الاعتماد | AI Stream | M | open | — |
| RSK-016 | أهداف أداء مفوّضة (QAS-PERF-001/002/007، QAS-USA-001) بلا قياس فعلي؛ قد تكون صارمة أكثر من اللازم أو متساهلة | M | M | قياس في Pilot وإعادة معايرة (ASM-010) | Performance Stream | L | open | — |
| RSK-017 | عناقيد SameAs كبيرة تبطئ حل الكيانات (إغلاق متعدٍ) | M | M | cluster id مادي تزايدي + حد 50 عضواً للمراجعة | BC02 | L | open | — |
| RSK-018 | PDP في المسار الحرج لكل طلب؛ تعطله مع fail-closed يوقف المنصة | M | H | PDP critical tier متعدد النسخ + ذاكرة قرارات ≤ 60 ث بإصدار أمني | BC08 | M | open | — |
| RSK-019 | تعقيد نموذج الادعاءات على مطوري الشرائح | M | M | مكتبة نواة مشتركة واحدة (Claims/Temporal) تُبنى أولاً في SLC-02 بعقود واضحة | BC02 | L | open | — |
| RSK-020 | انحراف جدول claims_current عن التاريخ | L | H | تحديث في نفس المعاملة + مطابقة ليلية + خاصية P-26 + إعادة بناء | BC02 | L | open | — |
| RSK-021 | مجموعة تقييم المطابقة لا تمثل بيانات المستأجر الفعلية | M | M | عينة موسومة من بيانات كل مستأجر في Pilot قبل تفعيل Ruleset إنتاجي | BC02 | L | open | — |
| RSK-022 | تكلفة الفهرسة المتداخلة على مستوى الحقيقة (1e8) قد تتجاوز قدرة خيار PostgreSQL وحده | M | M | قياس في W8/Pilot مقابل SPEC-DISCOVERY §8؛ محرك مخصص إن لزم (SR-10) | Platform | L | closed | decided by capability: OpenSearch (TD-02) |
| RSK-023 | الدفع للأجهزة الجوالة في بيئة معزولة دون خدمات عامة قد لا يكون موثوقاً | M | M | قناة داخلية/مرحّل MDM + سحب احتياطي ≤ 60 ث؛ قرار تقني في W8 | Platform | L | open | TD-16 + MDM relay; site MDM choice pending |
| RSK-024 | نمو سجل صور التنفيذ وأصول نتائج التشغيل مع الزمن | M | L | احتفاظ للأصول غير المستشهد بها؛ حماية ما يسند عملاً منشوراً؛ تخزين بارد | BC03 | L | open | — |
| RSK-025 | الاعتماد الحرج على KMS ومخزن المفاتيح؛ فقدانه يعني فقدان البيانات | L | H | HSM مكرر؛ نسخ KEK خارج الخط بإجراء شخصين؛ تدريبات استعادة (FIT-19) | Platform / Security | L | open | — |
| RSK-026 | البصمة التشغيلية (8 خدمات ذات حالة لكل خلية) قد تتجاوز قدرة فريق تشغيل صغير | M | H | operators, GitOps, Zarf, runbooks; تأكيد حجم الفريق قبل G8؛ بديل NATS JetStream موثق | Platform | M | open | — |
| RSK-027 | تصميم R2 قبل قياسات Pilot للإصدار الأول قد يبني على أرقام غير معايرة | M | M | كل قيمة رقمية في R2 موسومة 'recalibrate after R1 pilot'؛ بوابة G6 لأي شريحة R2 تتطلب مراجعة بعد نتائج Pilot | Orchestrator | L | open | — |
| RSK-028 | تكرار مخاطرة RSK-027 مع R3: نطاق R3 حُدِّد (W1/W2) قبل تجربة R1 **وقبل مراجعة R2 نفسها**؛ أي تصميم فعلي لشرائح R3 سيبني على افتراضات BC04/BC05 غير مقاسة على طبقتين (R1 وR2 معاً) | M | M | **لا تصميم شرائح R3 (Aggregates/عقود) قبل مراجعة Pilot R1؛ لا G6 لأي شريحة R3 قبل مراجعة تجربة R2 أيضاً** — بوابة أشد من RSK-027 عمداً | Orchestrator | L | open | scope-only (W1/W2) هذه الجولة؛ لا تصميم تفصيلي. **تحديث (CR-81):** شرائح R3 (SLC-17..19) صُمِّمت لاحقًا بقرار CR-67/CR-70 (DESIGN_COMPLETE)، فالجزء الأول من التخفيف تجاوزته الأحداث؛ يبقى قيد G6 لشرائح R3 حتى مراجعة تجربة R2، وأرقامها موسومة «تُعاد معايرته بعد Pilot R1/R2» |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
risks:
- id: RSK-001
  description: نطاق 26 مجالاً للإصدار الأول
  probability: H
  impact: H
  mitigation: شرائح رفيعة + HAP-02
  owner: Sponsor
  residual_risk: TBD
  status: open
- id: RSK-002
  description: غموض النموذج الزمني
  probability: M
  impact: H
  mitigation: ADR-P01 قبل التصميم المنطقي
  owner: BC02
  residual_risk: TBD
  status: open
- id: RSK-003
  description: تسرب صلاحيات عبر الإسقاطات/Cache/Tiles
  probability: M
  impact: H
  mitigation: ADR-P06 + اختبارات الاستدلال
  owner: Security
  residual_risk: TBD
  status: open
- id: RSK-004
  description: إفراط في نموذج الأدلة
  probability: M
  impact: M
  mitigation: ADR-P03
  owner: BC02
  residual_risk: TBD
  status: open
- id: RSK-005
  description: عبء تشغيلي يفوق قدرة الفريق
  probability: M
  impact: H
  mitigation: ADR-P05
  owner: Platform
  residual_risk: TBD
  status: mitigated
  note: operators + GitOps; ops team size still UNK-012
- id: RSK-006
  description: ضعف مطابقة الأسماء العربية
  probability: H
  impact: M
  mitigation: ADR-P15
  owner: BC02
  residual_risk: TBD
  status: open
- id: RSK-007
  description: تعارض المحو القانوني مع الثبات
  probability: M
  impact: H
  mitigation: ADR-P08
  owner: Privacy
  residual_risk: TBD
  status: open
- id: RSK-008
  description: تعارضات المزامنة الميدانية
  probability: M
  impact: H
  mitigation: ADR-P09
  owner: BC02
  residual_risk: TBD
  status: open
- id: RSK-009
  description: قدرات AI محدودة في بيئة معزولة
  probability: M
  impact: M
  mitigation: اختبار نماذج محلية مبكراً
  owner: AI
  residual_risk: TBD
  status: open
- id: RSK-010
  description: الدراسة تتحول لوثائق بلا تنفيذ
  probability: M
  impact: H
  mitigation: A20 + معيار V6§2 + جاهزية بالشريحة
  owner: Orchestrator
  residual_risk: TBD
  status: open
- id: RSK-011
  description: تأخر إجابات أصحاب القرار
  probability: H
  impact: H
  mitigation: بنك الأسئلة مبكراً
  owner: Sponsor
  residual_risk: TBD
  status: mitigated
  note: answers provided by delegated decision
- id: RSK-012
  description: تعدد معاني المصطلحات (Policy, Assessment, Decision…) يسبب نماذج متعارضة بين الفرق (W0)
  probability: H
  impact: M
  mitigation: glossary.md ملزم + SL-26
  owner: Orchestrator
  residual_risk: TBD
  status: open
- id: RSK-013
  description: أولوية التوسع تدفع إلى تعقيد مبكر (Premature Scale) يرفع التكلفة والعبء التشغيلي على فريق صغير
  probability: M
  impact: H
  mitigation: 'مبدأ Scale-Ready not Scale-First (SR-00): التوسع مصمم ومختبر، لا منشور مسبقاً'
  owner: Architecture Board
  residual_risk: L
  status: open
- id: RSK-014
  description: قرارات W1 مفوّضة لوكيل؛ قد تخالف واقع المؤسسة عند تعرّفها
  probability: M
  impact: M
  mitigation: مصادقة المالك عند G6؛ كل قرار قابل للمراجعة؛ أثر كل إجابة مسجل
  owner: Project Owner
  residual_risk: L
  status: open
- id: RSK-015
  description: البيئة المعزولة كخط أساس تحد من جودة نماذج AI المتاحة
  probability: M
  impact: M
  mitigation: تقييم نماذج محلية مبكراً (SLC-10)؛ AIL≤2 في R1 يقلل الاعتماد
  owner: AI Stream
  residual_risk: M
  status: open
- id: RSK-016
  description: أهداف أداء مفوّضة (QAS-PERF-001/002/007، QAS-USA-001) بلا قياس فعلي؛ قد تكون صارمة أكثر من اللازم أو متساهلة
  probability: M
  impact: M
  mitigation: قياس في Pilot وإعادة معايرة (ASM-010)
  owner: Performance Stream
  residual_risk: L
  status: open
- id: RSK-017
  description: عناقيد SameAs كبيرة تبطئ حل الكيانات (إغلاق متعدٍ)
  probability: M
  impact: M
  mitigation: cluster id مادي تزايدي + حد 50 عضواً للمراجعة
  owner: BC02
  residual_risk: L
  status: open
- id: RSK-018
  description: PDP في المسار الحرج لكل طلب؛ تعطله مع fail-closed يوقف المنصة
  probability: M
  impact: H
  mitigation: PDP critical tier متعدد النسخ + ذاكرة قرارات ≤ 60 ث بإصدار أمني
  owner: BC08
  residual_risk: M
  status: open
- id: RSK-019
  description: تعقيد نموذج الادعاءات على مطوري الشرائح
  probability: M
  impact: M
  mitigation: مكتبة نواة مشتركة واحدة (Claims/Temporal) تُبنى أولاً في SLC-02 بعقود واضحة
  owner: BC02
  residual_risk: L
  status: open
- id: RSK-020
  description: انحراف جدول claims_current عن التاريخ
  probability: L
  impact: H
  mitigation: تحديث في نفس المعاملة + مطابقة ليلية + خاصية P-26 + إعادة بناء
  owner: BC02
  residual_risk: L
  status: open
- id: RSK-021
  description: مجموعة تقييم المطابقة لا تمثل بيانات المستأجر الفعلية
  probability: M
  impact: M
  mitigation: عينة موسومة من بيانات كل مستأجر في Pilot قبل تفعيل Ruleset إنتاجي
  owner: BC02
  residual_risk: L
  status: open
- id: RSK-022
  description: تكلفة الفهرسة المتداخلة على مستوى الحقيقة (1e8) قد تتجاوز قدرة خيار PostgreSQL وحده
  probability: M
  impact: M
  mitigation: قياس في W8/Pilot مقابل SPEC-DISCOVERY §8؛ محرك مخصص إن لزم (SR-10)
  owner: Platform
  residual_risk: L
  status: closed
  note: 'decided by capability: OpenSearch (TD-02)'
- id: RSK-023
  description: الدفع للأجهزة الجوالة في بيئة معزولة دون خدمات عامة قد لا يكون موثوقاً
  probability: M
  impact: M
  mitigation: قناة داخلية/مرحّل MDM + سحب احتياطي ≤ 60 ث؛ قرار تقني في W8
  owner: Platform
  residual_risk: L
  status: open
  note: TD-16 + MDM relay; site MDM choice pending
- id: RSK-024
  description: نمو سجل صور التنفيذ وأصول نتائج التشغيل مع الزمن
  probability: M
  impact: L
  mitigation: احتفاظ للأصول غير المستشهد بها؛ حماية ما يسند عملاً منشوراً؛ تخزين بارد
  owner: BC03
  residual_risk: L
  status: open
- id: RSK-025
  description: الاعتماد الحرج على KMS ومخزن المفاتيح؛ فقدانه يعني فقدان البيانات
  probability: L
  impact: H
  mitigation: HSM مكرر؛ نسخ KEK خارج الخط بإجراء شخصين؛ تدريبات استعادة (FIT-19)
  owner: Platform / Security
  residual_risk: L
  status: open
- id: RSK-026
  description: البصمة التشغيلية (8 خدمات ذات حالة لكل خلية) قد تتجاوز قدرة فريق تشغيل صغير
  probability: M
  impact: H
  mitigation: operators, GitOps, Zarf, runbooks; تأكيد حجم الفريق قبل G8؛ بديل NATS JetStream موثق
  owner: Platform
  residual_risk: M
  status: open
- id: RSK-027
  description: تصميم R2 قبل قياسات Pilot للإصدار الأول قد يبني على أرقام غير معايرة
  probability: M
  impact: M
  mitigation: كل قيمة رقمية في R2 موسومة 'recalibrate after R1 pilot'؛ بوابة G6 لأي شريحة R2 تتطلب مراجعة بعد نتائج Pilot
  owner: Orchestrator
  residual_risk: L
  status: open
- id: RSK-028
  description: تكرار مخاطرة RSK-027 مع R3، مركّبة على طبقتين غير مقاستين (R1 وR2 معاً)
  probability: M
  impact: M
  mitigation: لا تصميم شرائح R3 قبل مراجعة Pilot R1؛ لا G6 لأي شريحة R3 قبل مراجعة تجربة R2 أيضاً؛ هذه الجولة scope-only (W1/W2)، بلا تصميم تفصيلي
  update: 'CR-81: R3 slices SLC-17..19 were designed later under CR-67/CR-70 (DESIGN_COMPLETE), so the first part of the mitigation was overtaken; the G6 gate for R3 slices still waits for the R2 pilot review, and R3 numbers are tagged recalibrate after Pilot R1/R2'
  owner: Orchestrator
  residual_risk: L
  status: open
```

</details>
