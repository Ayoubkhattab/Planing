---
id: LDM-SLC01
type: logical-data-model
title: Logical Data Model — SLC-01
wave: W6
slice: SLC-01
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
traces: {decided_by: [ADR-P02, ADR-P04, ADR-P08, ADR-P13], fitness: [FIT-01, FIT-02, FIT-04, FIT-09]}
---

# Logical Data Model — SLC-01

نموذج منطقي مستقل عن المحرك (المحرك في ADR-P05). **قواعد عامة لكل جدول:**
- `tenant_id` أول عمود في كل مفتاح أساسي وكل فهرس (FIT-02، SR-02)؛ سياسة عزل على مستوى الصف كحاجز ثان (ADR-P04).
- كل Aggregate: جدول حالة + جدول `_history` (إصدار غير قابل للتعديل لكل تغيير) + `version` للتزامن.
- الأزمنة: `recorded_at` يعينه الخادم؛ لا `created_at/updated_at` كزمن عمل (FIT-09).
- الحقول الشخصية مشفرة بمفتاح صاحب البيانات (ADR-P08) ومعلمة `pii`.
- كل مخطط (schema) مملوك لسياق واحد؛ لا منح وصول عابر (FIT-01).

## BC01 — schema `foundation`

| الجدول | المفتاح | أعمدة أساسية | قيود |
|---|---|---|---|
| tenants | (tenant_id) | namespace, display_name, state, cell_id, cell_mode, sovereign, top_level_enabled, jurisdiction, quotas(json), version | namespace UNIQUE (platform) immutable; state ∈ SM |
| tenant_provisioning_steps | (tenant_id, step) | status, attempt, last_error, recorded_at | idempotent per step |
| organizations | (tenant_id, org_id) | name(json LocalizedName), state, version | UNIQUE(tenant_id, name.normalized) |
| org_units | (tenant_id, unit_id) | org_id, parent_unit_id, path (materialized), name(json), state | one root per org; UNIQUE(tenant_id, parent_unit_id, name.normalized); path used for subtree scope checks |
| persons | (tenant_id, person_id) | names(json, **pii**), hr_id(**pii**), contact(json, **pii**), state, subject_key_ref, version | UNIQUE(tenant_id, hr_id) when not null |
| users | (tenant_id, user_id) | username, person_id?, state, security_version, version | UNIQUE(tenant_id, username); UNIQUE(tenant_id, person_id) |
| user_identities | (tenant_id, issuer, subject) | user_id, linked_at | UNIQUE(tenant_id, issuer, subject) |
| service_accounts | (tenant_id, sa_id) | name, owner_user_id, purpose, state, security_version, version | owner NOT NULL |
| service_account_credentials | (tenant_id, sa_id, credential_id) | public_key_fingerprint, expires_at | expires_at ≤ issued + 90 d |
| roles | (tenant_id, role_id) | code, name(json), system_role, state, version | UNIQUE(tenant_id, code) |
| role_permissions | (tenant_id, role_id, role_version, action, resource_type) | — | per role version |
| role_assignments | (tenant_id, assignment_id) | user_id, role_id, org_scope_unit_id, include_descendants, valid_from, valid_to, state, version | no two ACTIVE SoD-incompatible roles per user (checked in aggregate + deferred constraint) |
| authority_grants | (tenant_id, grant_id) | holder_urn, parent_grant_id?, depth, decision_types[], org_scope_unit_id, include_descendants, limits(json), valid_from, valid_to, delegable, state, version | depth ≤ 2; CHECK(valid_from < valid_to); parent period ⊇ child (aggregate) |
| clearances | (tenant_id, clearance_id) | user_id, level_code, compartments[], caveat_attributes(json), valid_to, state, requested_by, approved_by, version | at most one non-terminal per user (partial unique index) |
| security_versions (KV) | (tenant_id, subject_urn) | security_version | replicated per cell; source of revocation truth for PEPs |
| *_history | (tenant_id, id, version) | full snapshot, recorded_at, actor, command_id, correlation_id | insert-only |
| outbox | (tenant_id, event_id) | event_type, aggregate_id, payload, recorded_at, published_at? | insert + mark published only |
| audit_outbox | (tenant_id, audit_id) | record(json), recorded_at, shipped_at? | **insert-only** for application role |
| inbox | (tenant_id, consumer, event_id) | processed_at | dedupe |
| idempotency_keys | (tenant_id, key) | command_id, request_hash, response, expires_at | TTL 24 h |

## BC08 — schema `governance`

| الجدول | المفتاح | أعمدة أساسية | قيود |
|---|---|---|---|
| classification_schemes | (tenant_id, scheme_version) | state, levels(json), compartments(json), caveats(json), audit_threshold, default_level, effective_from, drafted_by, activated_by | one ACTIVE per tenant; one DRAFT per tenant |
| policy_sets | (tenant_id, policy_version) | state, decision_tables(json), tests(json), effective_from, author, approver | one ACTIVE per tenant; approver ≠ author |
| policy_bundles | (tenant_id, bundle_id) | policy_version, scheme_version, signature, built_at | signed; distributed to evaluators |
| security_exceptions | (tenant_id, exception_id) | policy_rule, subject_scope(json), justification, starts_at, ends_at, state, requested_by, version | ends_at − starts_at ≤ 30 d |
| security_exception_approvals | (tenant_id, exception_id, approver) | approved_at | distinct approvers; approver ≠ requester |
| audit_records | (tenant_id, shard, seq) | audit_id (UNIQUE), source_context, actor, action, resource(json), purpose, policy_decision(json), outcome(json), correlation_id, occurred_at, prev_hash, hash | insert-only; partitioned by (tenant_id, month) |
| audit_anchors | (anchor_id) | tenant_id, period, merkle_root, shard_heads(json), anchored_at | write-once store |

## الأحجام التقديرية (INF، تُعاد معايرتها)
| الجدول | الحجم عند نطاق التصميم |
|---|---|
| users / persons | ≤ 50,000 × 100 مستأجر = 5 M صف (نطاق أقصى) |
| role_assignments | ~5 لكل مستخدم → 25 M |
| audit_records | ~17 GB/يوم خام عند 200 سجل/ث (WL-01d) → تقسيم شهري + ضغط + جدول احتفاظ |
