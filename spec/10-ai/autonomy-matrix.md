---
id: AI-AUTONOMY-MATRIX
type: autonomy-matrix
title: AI Autonomy Matrix (AIL) — HAP-06
wave: W3
tier: T0
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
notes: AI في R2. هذه المصفوفة تحكم أي تنفيذ لاحق. AIL0 Assistive، AIL1 Suggestive، AIL2 Drafting، AIL3 Workflow-assisted with
  human approval، AIL4 Policy-bounded automation، AIL5 Autonomous (ممنوع).
---

# AI Autonomy Matrix (AIL) — HAP-06

> AI في R2. هذه المصفوفة تحكم أي تنفيذ لاحق. AIL0 Assistive، AIL1 Suggestive، AIL2 Drafting، AIL3 Workflow-assisted with human approval، AIL4 Policy-bounded automation، AIL5 Autonomous (ممنوع).

## operations

_14 items_

| id | operation | max_AIL_R2 | max_AIL_later | human_review | rule |
|---|---|---|---|---|---|
| AI-OP-01 | Grounded Q&A over authorized data with citations | AIL1 | AIL1 | no | يرفض الإجابة عند عدم كفاية الأدلة (Insufficient Evidence) |
| AI-OP-02 | Summarize documents / situations | AIL2 | AIL2 | no | ملخص مسودة يُعلَّم كمخرج AI |
| AI-OP-03 | Draft report / briefing sections | AIL2 | AIL3 | before publication | النشر قرار بشري دائماً |
| AI-OP-04 | Extract entities, locations, dates from documents | AIL2 | AIL3 | before claims become ASSERTED | المستخرج يدخل كادعاءات مقترحة بمصدر = الوثيقة وagent = النموذج |
| AI-OP-05 | Translate AR↔EN | AIL2 | AIL4 (policy-bound) | no for display; yes if used as evidence | الترجمة لا تستبدل الأصل أبداً |
| AI-OP-06 | Suggest entity matches | AIL1 | AIL1 | match decision always human | يُنشئ Resolution Case فقط |
| AI-OP-07 | Highlight anomalies | AIL1 | AIL1 | n/a | تنبيه مقترح، لا Alert رسمي إلا بقاعدة معتمدة |
| AI-OP-08 | Auto-tag / classify content topics (not security classification) | AIL2 | AIL4 (policy-bound) | sampled review | — |
| AI-OP-F1 | Record or approve a decision | forbidden | forbidden | — | ممنوع مطلقاً |
| AI-OP-F2 | Change security classification | forbidden | forbidden | — | ممنوع مطلقاً |
| AI-OP-F3 | Delete or retract data | forbidden | forbidden | — | ممنوع مطلقاً |
| AI-OP-F4 | Allocate resources / assign tasks | forbidden | AIL3 suggestion only | — | اقتراح فقط، التنفيذ بشري |
| AI-OP-F5 | Send external communications | forbidden | forbidden | — | ممنوع مطلقاً |
| AI-OP-F6 | Any AIL5 autonomous execution | forbidden | forbidden | — | ممنوع على مستوى المنصة |

## global_rules

- AI يرث صلاحيات المستخدم الطالب فقط، ولا يملك صلاحيات خاصة (BRL-008)
- كل مخرج AI يحمل lineage: context package، model، version (BRL-009)
- النماذج محلية افتراضياً؛ الخارجية بسياسة مستأجر وللبيانات غير المصنفة فقط (W1 Q28)
- رفع AIL لأي عملية = ADR جديد + HAP

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
operations:
- id: AI-OP-01
  operation: Grounded Q&A over authorized data with citations
  max_AIL_R2: AIL1
  max_AIL_later: AIL1
  human_review: 'no'
  rule: يرفض الإجابة عند عدم كفاية الأدلة (Insufficient Evidence)
- id: AI-OP-02
  operation: Summarize documents / situations
  max_AIL_R2: AIL2
  max_AIL_later: AIL2
  human_review: 'no'
  rule: ملخص مسودة يُعلَّم كمخرج AI
- id: AI-OP-03
  operation: Draft report / briefing sections
  max_AIL_R2: AIL2
  max_AIL_later: AIL3
  human_review: before publication
  rule: النشر قرار بشري دائماً
- id: AI-OP-04
  operation: Extract entities, locations, dates from documents
  max_AIL_R2: AIL2
  max_AIL_later: AIL3
  human_review: before claims become ASSERTED
  rule: المستخرج يدخل كادعاءات مقترحة بمصدر = الوثيقة وagent = النموذج
- id: AI-OP-05
  operation: Translate AR↔EN
  max_AIL_R2: AIL2
  max_AIL_later: AIL4 (policy-bound)
  human_review: no for display; yes if used as evidence
  rule: الترجمة لا تستبدل الأصل أبداً
- id: AI-OP-06
  operation: Suggest entity matches
  max_AIL_R2: AIL1
  max_AIL_later: AIL1
  human_review: match decision always human
  rule: يُنشئ Resolution Case فقط
- id: AI-OP-07
  operation: Highlight anomalies
  max_AIL_R2: AIL1
  max_AIL_later: AIL1
  human_review: n/a
  rule: تنبيه مقترح، لا Alert رسمي إلا بقاعدة معتمدة
- id: AI-OP-08
  operation: Auto-tag / classify content topics (not security classification)
  max_AIL_R2: AIL2
  max_AIL_later: AIL4 (policy-bound)
  human_review: sampled review
  rule: —
- id: AI-OP-F1
  operation: Record or approve a decision
  max_AIL_R2: forbidden
  max_AIL_later: forbidden
  human_review: —
  rule: ممنوع مطلقاً
- id: AI-OP-F2
  operation: Change security classification
  max_AIL_R2: forbidden
  max_AIL_later: forbidden
  human_review: —
  rule: ممنوع مطلقاً
- id: AI-OP-F3
  operation: Delete or retract data
  max_AIL_R2: forbidden
  max_AIL_later: forbidden
  human_review: —
  rule: ممنوع مطلقاً
- id: AI-OP-F4
  operation: Allocate resources / assign tasks
  max_AIL_R2: forbidden
  max_AIL_later: AIL3 suggestion only
  human_review: —
  rule: اقتراح فقط، التنفيذ بشري
- id: AI-OP-F5
  operation: Send external communications
  max_AIL_R2: forbidden
  max_AIL_later: forbidden
  human_review: —
  rule: ممنوع مطلقاً
- id: AI-OP-F6
  operation: Any AIL5 autonomous execution
  max_AIL_R2: forbidden
  max_AIL_later: forbidden
  human_review: —
  rule: ممنوع على مستوى المنصة
global_rules:
- AI يرث صلاحيات المستخدم الطالب فقط، ولا يملك صلاحيات خاصة (BRL-008)
- 'كل مخرج AI يحمل lineage: context package، model، version (BRL-009)'
- النماذج محلية افتراضياً؛ الخارجية بسياسة مستأجر وللبيانات غير المصنفة فقط (W1 Q28)
- رفع AIL لأي عملية = ADR جديد + HAP
```

</details>
