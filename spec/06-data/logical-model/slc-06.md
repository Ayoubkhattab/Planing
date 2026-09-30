---
id: LDM-SLC06
type: logical-data-model
title: Logical Data Model — SLC-06
wave: W6
slice: SLC-06
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Logical Data Model — SLC-06 (schemas `intelligence` BC03, `operations` BC04)

## BC03
| الجدول | المفتاح | أعمدة | قيود |
|---|---|---|---|
| situations | (tenant_id, situation_id) | name(json), owner, state, label, current_definition_version, membership_version, version | — |
| situation_definitions | (tenant_id, situation_id, def_version) | extent(json, EPSG:4326), window_from, window_to, criteria(json), recorded_at | immutable |
| situation_members | (tenant_id, situation_id, member_urn, member_from) | member_to, cause_event_id, def_version, member_label | index (tenant, situation_id, member_to IS NULL) |
| situation_changes | (tenant_id, situation_id, seq) | member_urn, change (joined/left/updated), at, cause_event_id | append-only; cursor for QRY-SIT-CHANGES |
| alert_rules | (tenant_id, rule_id, version) | situation_id?, scope, kind, parameters(json), severity, dedupe_window, escalation(json), auto_resolve, label, state | ACTIVE versions immutable |
| alerts | (tenant_id, alert_id) | rule_id, rule_version, subject_urn, label, severity, occurrences, first_at, last_at, state, version | partial unique (tenant, rule_id, subject_urn) where non-terminal and last_at within window |
| tile_cache (ephemeral) | (situation, layer, z, x, y, scope_hash, data_version) | bytes, created_at | TTL ≤ 10 min; never shared across scope_hash |

## BC04
| الجدول | المفتاح | أعمدة | قيود |
|---|---|---|---|
| subscriptions | (tenant_id, subscription_id) | user_id, target_urn, channels[], quiet_hours(json), state, version | partial unique (tenant, user, target) where ACTIVE/PAUSED |
| notifications | (tenant_id, recipient_id, notification_id) | ref_urn, template_code, severity, state, attempts, queued_at, sent_at, read_at | partition by (tenant, month); TTL 30 d → EXPIRED |
| notification_templates | (template_code, lang) | text | classification-safe list (reviewed by Security Officer) |
