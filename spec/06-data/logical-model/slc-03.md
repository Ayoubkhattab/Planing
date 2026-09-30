---
id: LDM-SLC03
type: logical-data-model
title: Logical Data Model — SLC-03
wave: W6
slice: SLC-03
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Logical Data Model — SLC-03 (schemas `operations` BC04, `readiness` BC05)

القواعد العامة من LDM-SLC01. `task_events` في PRJ§70 **محذوف** (ADR-P02، CR-16): التاريخ في `tasks_history`، والأحداث في outbox.

## BC04 — operations
| الجدول | المفتاح | أعمدة | قيود وفهارس |
|---|---|---|---|
| tasks | (tenant_id, task_id) | task_type_id, task_type_version, title(json), description(json), plan_ref?, ad_hoc_reason?, owner, org_scope, assignee?, reviewer?, state, suspended, due_at?, follow_up_of?, label, eligibility_snapshot(json), version | CHECK(plan_ref IS NOT NULL OR (ad_hoc_reason IS NOT NULL AND owner IS NOT NULL)); index (tenant, assignee, state, due_at); index (tenant, plan_ref, state) |
| task_criteria | (tenant_id, task_id, criterion_id) | kind, spec(json), satisfied, satisfied_by, satisfied_at | frozen after ASSIGNED (trigger/app) |
| task_result_items | (tenant_id, task_id, seq) | kind, ref?, note(json)?, measurement(json)?, added_by, added_at | append-only |
| task_dependencies | (tenant_id, task_id, predecessor_id) | — | acyclic (checked in aggregate) |
| tasks_history | (tenant_id, task_id, version) | snapshot, command_id, actor, recorded_at, correlation_id | insert-only; source for QRY-TASK-HISTORY |
| task_timers | (tenant_id, due_bucket, task_id, kind) | fire_at, lease_owner, lease_until | partitioned by tenant; minute buckets |
| task_types | (tenant_id, task_type_id, version) | code, name(json), qualification_requirements(json), criteria_templates(json), escalation(json), expires_on_due, review_steps, state | UNIQUE(tenant, code, version) |

## BC05 — readiness
| الجدول | المفتاح | أعمدة | قيود |
|---|---|---|---|
| qualification_records | (tenant_id, record_id) | person_id, kind, code, level, valid_from, valid_to, issuer, evidence?, state, version | index (tenant, person_id, code) |
| qualification_records_history | (tenant_id, record_id, version) | snapshot, recorded_at | insert-only (as-of eligibility) |
