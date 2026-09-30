---
id: LDM-SLC08
type: logical-data-model
title: Logical Data Model — SLC-08
wave: W6
slice: SLC-08
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Logical Data Model — SLC-08 (schema `operations`, BC04)

| الجدول | المفتاح | أعمدة | قيود |
|---|---|---|---|
| decision_requests | (tenant_id, request_id) | question(json), decision_type, scope_unit, deadline, options(json), citations(json pinned), label, state, version | — |
| decisions | (tenant_id, decision_id) | request_id?, selected_option, rationale(json), effective_from, recorded_at, decider, authority_snapshot(json), citations(json pinned), supersedes?, label, state | immutable except state; CHECK(citations non-empty) |
| plans | (tenant_id, plan_id) | title(json), owner, org_scope, implements[], window, label, state, baselined_version?, version | — |
| plan_versions | (tenant_id, plan_id, plan_version) | content(json: objectives, outcomes, constraints, assumptions, phases, activities, milestones, dependencies, resource_notes), author, approver?, change_class, state, submitted_at, baselined_at | content immutable from IN_REVIEW; partial unique one BASELINED per plan |
| plan_version_annotations | (tenant_id, plan_id, plan_version, seq) | annotation(json), by, at | minor amendments |
| task_sync_runs | (tenant_id, plan_id, from_version, to_version) | status, expected(json), applied(json), started_at, ended_at | unique run per transition (idempotency) |
| activity_task_map | (tenant_id, plan_id, activity_id, task_id) | created_in_version, superseded_in_version? | — |
| outcome_trackers | (tenant_id, plan_id, outcome_id) | metric, unit, state, targets(json history) | one per (plan, outcome) |
| outcome_measurements | (tenant_id, plan_id, outcome_id, measurement_id, recorded_from) | value, unit, measured_at, source, source_ref?, recorded_to? | bitemporal; corrections close and add |
