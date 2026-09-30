---
id: LDM-SLC19
type: logical-data-model
title: Logical Data Model — SLC-19
wave: W6
slice: SLC-19
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-29'
---

# Logical Data Model — SLC-19

| الجدول | المفتاح | أعمدة | قيود |
|---|---|---|---|
| scenarios (readiness) | (tenant_id, scenario_id) | title(json), exercise_type_ref, situation, target_competencies(array), label, state, version | injects ordered by strictly increasing offset_minutes (INV-SCN-01) |
| scenario_injects | (tenant_id, scenario_id, inject_id) | offset_minutes, description, expected_response | offset_minutes strictly increasing per scenario version (INV-SCN-01) |
| exercises (readiness) | (tenant_id, exercise_id) | scenario_ref, scenario_version_frozen, objectives, participants(array), purpose, role_ref?, window(json)?, location(json)?, label, state, version | scenario_ref must reference an ACTIVE scenario at CMD-EXR-PLAN time; scenario_version_frozen never changes after creation (INV-EXR-01) |
| simulations (readiness) | (tenant_id, simulation_id) | exercise_ref, scenario_ref, started_at, ended_at?, label, state, version | exactly one simulation per exercise, created in the same unit of work as EVT-EXR-STARTED |
| simulation_inject_deliveries | (tenant_id, simulation_id, delivered_at) | inject_ref, note, actor | append-only; delivered_at strictly increasing per simulation (INV-SIM-01) |
| simulation_evaluations | (tenant_id, simulation_id, evaluation_id) | participant_ref, competency_code, result, evaluator_ref, notes, recorded_at | evaluator_ref ≠ participant_ref (INV-SIM-03); every exercise participant has ≥ 1 row before COMPLETED (INV-SIM-02) |
| qualification_records (readiness, unchanged — SLC-03) | (tenant_id, record_id) | ...existing SLC-03 columns..., evidence_ref? | evidence_ref may now reference a completed simulation's URN; column type (urn) unchanged |
| knowledge_objects (knowledge, extended guard only — CR-63) | (tenant_id, object_id, version) | ...existing SLC-12 columns..., source_ref | source_ref (lesson type) may now reference a completed simulation in addition to a task/plan/incident; column type (urn) unchanged |
