---
id: SPEC-ELIGIBILITY
type: component-specification
title: Eligibility Evaluation (R1)
wave: W4
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
slice: SLC-03
traces: {requirements: [REQ-RDY-001, REQ-RDY-002, REQ-OPS-007], rules: [BRL-007]}
---

# Eligibility Evaluation

`EligibilityCheck(person, task_type_version, at)` — يُقيّم كل متطلب تأهيل في نوع المهمة، ثم تُجمع النتائج بأسوأ حالة حسب الأسبقية.

## 1. تقييم متطلب واحد (code, min_level, supervision_allowed)
| الشرط (عند الزمن at) | النتيجة |
|---|---|
| سجل ACTIVE بنفس الرمز، level ≥ min_level، والزمن ضمن الصلاحية | ELIGIBLE |
| سجل بنفس الرمز، level = min_level − 1، والنوع يسمح بالإشراف | REQUIRES_SUPERVISION (= CONDITIONALLY_ELIGIBLE بشرط وجود مشرف مؤهل) |
| سجل بنفس الرمز لكن انتهت صلاحيته | EXPIRED |
| المتطلب من نوع certification ويوجد competency بنفس الرمز دون شهادة | REQUIRES_CERTIFICATION |
| لا سجل بنفس الرمز والشخص لديه سجلات أخرى | REQUIRES_TRAINING |
| الشخص بلا أي سجلات، أو تعذر التقييم | UNKNOWN |
| سجل SUSPENDED أو REVOKED | NOT_ELIGIBLE |

## 2. التجميع (الأسوأ يغلب)
`NOT_ELIGIBLE > EXPIRED > REQUIRES_CERTIFICATION > REQUIRES_TRAINING > UNKNOWN > REQUIRES_SUPERVISION > ELIGIBLE`
نوع مهمة بلا متطلبات → ELIGIBLE.

## 3. الاستخدام في الإسناد
- مسموح: ELIGIBLE؛ أو REQUIRES_SUPERVISION إذا حُدد في الأمر مشرف مؤهل (ELIGIBLE) → تُسجل الحالة CONDITIONALLY_ELIGIBLE.
- غير ذلك → ASSIGNEE_NOT_ELIGIBLE مع الأسباب.
- تعذر الوصول لـ BC05 → رفض `ELIGIBILITY_UNAVAILABLE` (fail-closed) — لا إسناد دون تحقق.
- نتيجة التحقق تُحفظ في المهمة (EligibilitySnapshot) لأغراض التدقيق والمراجعة التاريخية.
