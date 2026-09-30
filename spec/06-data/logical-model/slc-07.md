---
id: LDM-SLC07
type: logical-data-model
title: Logical Data Model — SLC-07
wave: W6
slice: SLC-07
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Logical Data Model — SLC-07 (schema `intelligence`, BC03)

| الجدول | المفتاح | أعمدة | قيود |
|---|---|---|---|
| analysis_cases | (tenant_id, case_id) | title(json), owner, question(json), extent(json)?, window_from, window_to, state, label, version | — |
| case_hypotheses | (tenant_id, case_id, hypothesis_id) | statement(json), status, rationale, findings[] | history in cases_history |
| case_assumptions | (tenant_id, case_id, assumption_id) | statement(json), criticality, retired_at?, retired_reason | never deleted |
| case_selections | (tenant_id, case_id, selection_id) | item_urn, known_at, selected_by, selected_at, closed_at?, close_reason | item label ≤ case label |
| case_scenarios | (tenant_id, case_id, scenario_id) | name, assumptions[], parameter_overrides(json) | — |
| analysis_methods | (tenant_id, method_code, method_version) | parameter_schema(json), image_digest, deterministic, tolerance(json)?, state, author, approver | immutable content |
| analysis_runs | (tenant_id, run_id) | case_id, method_code, method_version, image_digest, parameters(json), inputs(json pins), scenario?, seed?, label, submitted_by, submitted_at, state, lease(json), started_at, ended_at, error? | — |
| run_steps | (tenant_id, run_id, seq) | step, at, detail(json) | append-only |
| run_artifacts | (tenant_id, run_id, artifact_id) | kind, sha256, attachment_ref | immutable |
| reproduction_reports | (tenant_id, run_id) | source_run_id, outcome (REPRODUCED/DIFFERENT), differences(json) | — |
| findings | (tenant_id, finding_id, version) | case_id, statement(json), sources(json pinned), uncertainty(json), label, author, reviewer, state | ACCEPTED immutable |
| assessment_versions | (tenant_id, assessment_id, version) | case_id, title(json), key_judgments(json), citations(json pinned), assumptions(json), uncertainty(json), confidence, methodology(json), limitations(json), label, author, reviewer, state, published_at | one PUBLISHED per assessment_id (partial unique) |
