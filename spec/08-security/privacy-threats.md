---
id: PRIVACY-THREATS
type: privacy-threat-model
title: Privacy Threat Model (LINDDUN)
wave: W3
tier: T0
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Privacy Threat Model (LINDDUN)

## threats

_7 items_

| id | category | threat | control |
|---|---|---|---|
| PRV-01 | Linkability | ربط سجلات شخص عبر مصادر يكشف أكثر مما أذن به الغرض | تقييد الغرض في السياسة؛ REDACT؛ مراجعة مطابقة الكيانات للأشخاص |
| PRV-02 | Identifiability | إعادة تعريف من إحصاءات صغيرة | AGGREGATE بحد أدنى 5 |
| PRV-03 | Non-repudiation (as privacy threat) | تتبع مفرط لنشاط المستخدمين | تدقيق القراءة فقط فوق العتبة؛ وصول مقيد لسجلات التدقيق |
| PRV-04 | Detectability | معرفة أن شخصاً ما في النظام | نفس شكل not-found لمن لا يحق له رؤية الشخص (ADR-P06 §5 كما عدّله ADR-P19)؛ لا اقتراحات بحث خارج النطاق |
| PRV-05 | Disclosure | بيانات شخصية في السجلات التقنية | إخفاء آلي؛ URN فقط |
| PRV-06 | Unawareness | أصحاب البيانات لا يعرفون المعالجة | خارج نطاق التقنية: سياسة المستأجر (UNK-002) |
| PRV-07 | Non-compliance | احتفاظ أطول من المسموح | جداول احتفاظ + crypto-shredding (ADR-P08) |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
threats:
- id: PRV-01
  category: Linkability
  threat: ربط سجلات شخص عبر مصادر يكشف أكثر مما أذن به الغرض
  control: تقييد الغرض في السياسة؛ REDACT؛ مراجعة مطابقة الكيانات للأشخاص
- id: PRV-02
  category: Identifiability
  threat: إعادة تعريف من إحصاءات صغيرة
  control: AGGREGATE بحد أدنى 5
- id: PRV-03
  category: Non-repudiation (as privacy threat)
  threat: تتبع مفرط لنشاط المستخدمين
  control: تدقيق القراءة فقط فوق العتبة؛ وصول مقيد لسجلات التدقيق
- id: PRV-04
  category: Detectability
  threat: معرفة أن شخصاً ما في النظام
  control: نفس شكل not-found لمن لا يحق له رؤية الشخص (ADR-P06 §5 كما عدّله ADR-P19)؛ لا اقتراحات بحث خارج النطاق
- id: PRV-05
  category: Disclosure
  threat: بيانات شخصية في السجلات التقنية
  control: إخفاء آلي؛ URN فقط
- id: PRV-06
  category: Unawareness
  threat: أصحاب البيانات لا يعرفون المعالجة
  control: 'خارج نطاق التقنية: سياسة المستأجر (UNK-002)'
- id: PRV-07
  category: Non-compliance
  threat: احتفاظ أطول من المسموح
  control: جداول احتفاظ + crypto-shredding (ADR-P08)
```

</details>
