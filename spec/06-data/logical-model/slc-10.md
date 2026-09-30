---
id: LDM-SLC10
type: logical-data-model
title: Logical Data Model — SLC-10
wave: W6
slice: SLC-10
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Logical Data Model — SLC-10 (schema `ai`, BC07)

| الجدول | المفتاح | أعمدة | قيود |
|---|---|---|---|
| ai_requests | (tenant_id, request_id) | user, operation, purpose, input(enc), state, routing_version, model_version, prompt_template, package_hash, output(enc), label, created_at | prompts/outputs encrypted with tenant key; record class ai-logs |
| ai_context_items | (tenant_id, request_id, seq) | urn, version, known_at, label, score | pinned |
| ai_statements | (tenant_id, request_id, seq) | text(enc), citations[], entailment_score | — |
| ai_results | (tenant_id, result_id) | request_id, operation, target, items(json), state, reviewer, decisions(json) | — |
| model_versions | (model_id, version) | family, weights_digest, licence, languages[], context_tokens, hosting, roles[], state, evaluation_report?, canary(json)? | platform-level; never deleted |
| ai_routings | (tenant_id, routing_version) | routes(json), state, author, approver | one ACTIVE per tenant |
| ai_tools | (tool_id) | name, input_schema(json), binding, effect, permission, max_ail, state | effect ∈ {read, propose} in R2 |
| eval_suites | (suite_id, version) | sets(json), state | immutable once ACTIVE |
| eval_reports | (report_id) | model_version, suite_version, metrics(json), run_at | — |
| ai_usage | (tenant_id, day, operation) | requests, gpu_seconds, tokens_in, tokens_out | cost model input |
| vector projection docs | (projection_version, tenant, chunk_id) | urn, labels, embedding, text_ref | same labels as search facts (ADR-P06) |
