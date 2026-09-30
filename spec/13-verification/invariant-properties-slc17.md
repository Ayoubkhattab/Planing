---
id: PROP-SLC17
type: property-spec
title: Property-Based Invariant Specifications — SLC-17
wave: W6
slice: SLC-17
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-27'
---

# Property-Based Invariants — SLC-17

| ID | الخاصية |
|---|---|
| P-165 | severity حادثة لا تنقص أبداً إلا عبر CMD-INC-DE-ESCALATE |
| P-166 | لا Plan بنوع CONTINGENCY يُنشأ أو يُفعَّل كأثر جانبي لأي أمر آخر غير CMD-INC-ACTIVATE-CONTINGENCY أو CMD-PLN-CREATE الصريح |
| P-167 | risk_score = likelihood × impact في كل قراءة، بلا استثناء |
| P-168 | كل Risk بحالة TREATED له ≥ 1 treatment_task_ref، أو أن استراتيجيته accept بموافقة مسجَّلة |
| P-169 | ربط حادثة بخطر (risk_ref) لا يغيّر حالة أو إصدار أو تصنيف ذلك الخطر أبداً |
