---
id: LDM-SLC17
type: logical-data-model
title: Logical Data Model — SLC-17
wave: W6
slice: SLC-17
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-27'
---

# Logical Data Model — SLC-17

| الجدول | المفتاح | أعمدة | قيود |
|---|---|---|---|
| risks (operations) | (tenant_id, risk_id) | category_ref, description(json), scope_refs[], likelihood, impact, risk_score(generated always as likelihood*impact stored), treatment_strategy?, treatment_task_refs[]?, rationale?, incident_ref?, label, state, version | risk_score is a generated column, never written directly |
| risk_treatment_actions | (tenant_id, risk_id, treatment_task_ref) | status | — |
| incidents (operations) | (tenant_id, incident_id) | category_ref, description(json), scope_refs[], risk_ref?, severity, affected_scope_refs[]?, commander?, response_task_refs[]?, after_action_ref?, label, state, version | severity change history kept in incident_severity_history, not overwritten |
| incident_severity_history | (tenant_id, incident_id, changed_at) | from_severity, to_severity, reason, actor | append-only |
| plans (operations, extended — CR-60) | (tenant_id, plan_id) | ...existing SLC-08 columns..., plan_kind, triggered_by? | triggered_by only set when plan_kind = CONTINGENCY (INV-PLN-04) |
| tasks (operations, extended — CR-61) | (tenant_id, task_id) | ...existing SLC-03 columns..., incident_ref? | exactly one of plan_ref / incident_ref / ad_hoc_reason set at creation |
