---
id: LDM-SLC16
type: logical-data-model
title: Logical Data Model — SLC-16
wave: W6
slice: SLC-16
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Logical Data Model — SLC-16

| الجدول | المفتاح | أعمدة | قيود |
|---|---|---|---|
| integration_connections (integration) | (tenant_id, connection_id) | name, system_kind, endpoint, protocol, direction, credentials_ref, allow_list(json), state, health(json) | outbound only for cap_endpoint (R2) |
| connection_cursors | (tenant_id, connection_id, feed) | watermark, last_success_at | replay point |
| sensor_streams | (tenant_id, stream_id) | connection_id, source_urn, quantity, unit, expected_rate, location?, linked_entity?, quality_rules(json), state, last_reading_at | — |
| dms_classification_map | (tenant_id, dms_code) | platform_level, compartments[] | unmapped → highest default |
| hr_sync_proposals (foundation) | (tenant_id, proposal_id) | person_id, change_kind, hr_payload(enc), proposed_changes(json), state, decided_by? | personal data encrypted with subject key |
| hr_role_mapping | (tenant_id, hr_position_code) | role_ids[], org_scope_rule | tenant-maintained |
| cap_messages (intelligence) | (tenant_id, message_id) | alert_id, template, payload(xml), connection_id, state, preparer, releaser?, ack? | payload validated against CAP 1.2 |
