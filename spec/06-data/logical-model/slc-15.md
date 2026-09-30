---
id: LDM-SLC15
type: logical-data-model
title: Logical Data Model — SLC-15
wave: W6
slice: SLC-15
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Logical Data Model — SLC-15

| الجدول | المفتاح | أعمدة | قيود |
|---|---|---|---|
| coordination_cases (operations) | (tenant_id, case_id) | title(json), purpose(json), lead_org, links(json), label, state, version | — |
| coordination_participants | (tenant_id, case_id, org_unit) | role, access_scope[] | lead cannot be removed |
| coordination_responsibilities | (tenant_id, case_id, responsibility_id) | participant, item(json), due, requires_authority?, decision_request?, decision?, status | done requires decision when requires_authority |
| correlation_proposals (information) | (tenant_id, proposal_id) | kind, inputs(json: urn, source, reliability, label), score(json), rule_version, label, state, reviewer? | partial unique on (kind, sorted inputs) where non-terminal |
| correlation_rules | (tenant_id, rule_id, version) | kind, parameters(json), evaluation(json), state | — |
| correlation_buckets (ephemeral) | (tenant_id, geohash6, time_bucket, urn) | source | TTL = rule window |
