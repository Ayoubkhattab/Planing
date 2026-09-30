---
id: SLICE-SOURCES
type: specification-source
title: Slice source data (authoritative input to the generators)
wave: W9 + R2 + R3
status: BASELINED (R1) / DESIGN (R2) / DESIGN, G6 held per RSK-028 (R3)
---

# بيانات مصدر الشرائح

**المصدر المعتمد** لكل Aggregate وأمر واستعلام وحدث وإثراء عقود. أي تغيير سلوكي يبدأ هنا ثم يُعاد التوليد.

## slc01_data.py

```python
# -*- coding: utf-8 -*-
# SLC-01 — Tenancy, Identity, Organization, Authorization, Audit
# Transition tuple: (from_states | "∅" for create | "*NT" any non-terminal, command, to_state | "=" unchanged, guard, event, error_if_guard_fails)

SLICE = "SLC-01"
AGGS = {}
def agg(id_, bc, name, tier, purpose, states, terminal, transitions, invariants, entities, reqs, notes=None, personal=False):
    AGGS[id_] = dict(id=id_, bc=bc, name=name, tier=tier, purpose=purpose, states=states, terminal=terminal,
                     transitions=transitions, invariants=invariants, entities=entities, requirements=reqs,
                     notes=notes, personal_data=personal)

# ---------------- BC01 ----------------
agg("AGG-TENANT","BC01","Tenant","T2","وحدة العزل العليا؛ تُربط بخلية واحدة",
 ["PROVISIONING","PROVISIONING_FAILED","ACTIVE","SUSPENDED","MIGRATING","DECOMMISSIONING","DECOMMISSIONED"],["DECOMMISSIONED"],
 [("∅","CMD-TEN-PROVISION","PROVISIONING","namespace unique; cell_mode valid for tenant profile (INV-TEN-03)","EVT-TEN-PROVISIONING-STARTED","TENANT_NAMESPACE_TAKEN"),
  (["PROVISIONING"],"CMD-TEN-COMPLETE-PROVISIONING","ACTIVE","system; all provisioning steps confirmed (isolation, keys, scheme, roles, quotas, audit stream)","EVT-TEN-ACTIVATED","TENANT_PROVISIONING_INCOMPLETE"),
  (["PROVISIONING"],"CMD-TEN-FAIL-PROVISIONING","PROVISIONING_FAILED","system; compensation completed","EVT-TEN-PROVISIONING-FAILED",None),
  (["PROVISIONING_FAILED"],"CMD-TEN-RETRY-PROVISIONING","PROVISIONING","actor = platform operator","EVT-TEN-PROVISIONING-STARTED",None),
  (["ACTIVE"],"CMD-TEN-SUSPEND","SUSPENDED","reason provided","EVT-TEN-SUSPENDED","REASON_REQUIRED"),
  (["SUSPENDED"],"CMD-TEN-REACTIVATE","ACTIVE","—","EVT-TEN-REACTIVATED",None),
  (["ACTIVE"],"CMD-TEN-START-CELL-MIGRATION","MIGRATING","target cell exists and has capacity","EVT-TEN-MIGRATION-STARTED","CELL_UNAVAILABLE"),
  (["MIGRATING"],"CMD-TEN-COMPLETE-CELL-MIGRATION","ACTIVE","system; export/import reconciled","EVT-TEN-MIGRATED","MIGRATION_NOT_RECONCILED"),
  (["ACTIVE","SUSPENDED"],"CMD-TEN-START-DECOMMISSION","DECOMMISSIONING","no active legal hold (BC08 query); two-person approval","EVT-TEN-DECOMMISSION-STARTED","LEGAL_HOLD_ACTIVE"),
  (["DECOMMISSIONING"],"CMD-TEN-COMPLETE-DECOMMISSION","DECOMMISSIONED","system; keys destroyed, stores removed","EVT-TEN-DECOMMISSIONED",None),
  (["ACTIVE","SUSPENDED"],"CMD-TEN-UPDATE-QUOTAS","=","quotas ≤ cell capacity","EVT-TEN-QUOTAS-UPDATED","QUOTA_EXCEEDS_CAPACITY")],
 ["INV-TEN-01: users of a tenant can authenticate only while the tenant is ACTIVE",
  "INV-TEN-02: a tenant is bound to exactly one cell at any time",
  "INV-TEN-03: cell_mode = dedicated if sovereign, or top classification level enabled, or load > 20 % of cell (ADR-P04)",
  "INV-TEN-04: namespace is unique across the platform and immutable",
  "INV-TEN-05: decommission cannot start while any legal hold is active"],
 ["TenantQuotas (value object)","ProvisioningStep (value object list)"],["REQ-FND-001","REQ-FND-003","REQ-FND-004","REQ-FND-018"],
 "Provisioning is a saga orchestrated by BC01; each step idempotent and compensable.")

agg("AGG-ORGANIZATION","BC01","Organization (with unit tree)","T2","مؤسسة داخل مستأجر مع شجرة وحداتها",
 ["ACTIVE","INACTIVE"],[],
 [("∅","CMD-ORG-CREATE","ACTIVE","tenant ACTIVE; name unique in tenant; creates root unit","EVT-ORG-CREATED","ORG_NAME_TAKEN"),
  (["ACTIVE"],"CMD-ORG-RENAME","=","name unique in tenant","EVT-ORG-RENAMED","ORG_NAME_TAKEN"),
  (["ACTIVE"],"CMD-ORG-ADD-UNIT","=","parent unit ACTIVE; sibling name unique","EVT-ORG-UNIT-ADDED","ORG_UNIT_INVALID_PARENT"),
  (["ACTIVE"],"CMD-ORG-RENAME-UNIT","=","sibling name unique","EVT-ORG-UNIT-RENAMED","ORG_UNIT_NAME_TAKEN"),
  (["ACTIVE"],"CMD-ORG-MOVE-UNIT","=","new parent ACTIVE, same org, not a descendant (no cycle); root cannot move","EVT-ORG-UNIT-MOVED","ORG_UNIT_CYCLE"),
  (["ACTIVE"],"CMD-ORG-DEACTIVATE-UNIT","=","no active children; no active role assignments, grants or clearances scoped only to it (BC01 query)","EVT-ORG-UNIT-DEACTIVATED","ORG_UNIT_IN_USE"),
  (["ACTIVE"],"CMD-ORG-DEACTIVATE","INACTIVE","all non-root units inactive; no active assignments","EVT-ORG-DEACTIVATED","ORG_IN_USE"),
  (["INACTIVE"],"CMD-ORG-REACTIVATE","ACTIVE","tenant ACTIVE","EVT-ORG-REACTIVATED",None)],
 ["INV-ORG-01: the unit tree is acyclic with exactly one root",
  "INV-ORG-02: sibling unit names are unique (after language-model normalization)",
  "INV-ORG-03: an inactive unit cannot receive children, assignments or grants",
  "INV-ORG-04: unit count per organization ≤ 5,000 (aggregate size bound; larger orgs split into organizations)"],
 ["OrgUnit (entity, with own state ACTIVE/INACTIVE)"],["REQ-FND-002"],
 "Unit-level lifecycle: ACTIVE → INACTIVE via CMD-ORG-DEACTIVATE-UNIT; reactivation via CMD-ORG-ADD-UNIT is not allowed (create new unit) to keep history clear.")

agg("AGG-PERSON","BC01","Person","T2","سجل الشخص في المنصة (ليس كيان معلومات من نوع شخص)",
 ["ACTIVE","INACTIVE","ERASED"],["ERASED"],
 [("∅","CMD-PER-REGISTER","ACTIVE","names per language-model; no duplicate HR id","EVT-PER-REGISTERED","PERSON_DUPLICATE"),
  (["ACTIVE"],"CMD-PER-UPDATE-DETAILS","=","—","EVT-PER-DETAILS-UPDATED",None),
  (["ACTIVE"],"CMD-PER-DEACTIVATE","INACTIVE","—","EVT-PER-DEACTIVATED",None),
  (["INACTIVE"],"CMD-PER-REACTIVATE","ACTIVE","—","EVT-PER-REACTIVATED",None),
  (["INACTIVE"],"CMD-PER-ERASE","ERASED","erasure order recorded; no legal hold; destroys subject key (ADR-P08)","EVT-PER-ERASED","LEGAL_HOLD_ACTIVE")],
 ["INV-PER-01: personal attributes are flagged personal_data (crypto-shredding, ADR-P08)",
  "INV-PER-02: external HR identifier unique per tenant when present"],
 [],["REQ-FND-006","REQ-GOV-008"],"Distinct from information Entity of type person (BC02).",personal=True)

agg("AGG-USER","BC01","User Account","T2","حساب دخول مرتبط بهويات خارجية",
 ["PENDING","ACTIVE","LOCKED","DISABLED","CLOSED"],["CLOSED"],
 [("∅","CMD-USR-PROVISION","PENDING","tenant ACTIVE; via SCIM or admin","EVT-USR-PROVISIONED","TENANT_NOT_ACTIVE"),
  ("*NT","CMD-USR-LINK-IDENTITY","=","(issuer, subject) unique in tenant; issuer is a configured IdP","EVT-USR-IDENTITY-LINKED","IDENTITY_ALREADY_LINKED"),
  ("*NT","CMD-USR-UNLINK-IDENTITY","=","if ACTIVE, at least one identity remains","EVT-USR-IDENTITY-UNLINKED","LAST_IDENTITY"),
  ("*NT","CMD-USR-LINK-PERSON","=","person ACTIVE, not linked to another user","EVT-USR-PERSON-LINKED","PERSON_ALREADY_LINKED"),
  (["PENDING"],"CMD-USR-RECORD-FIRST-SIGN-IN","ACTIVE","system; ≥ 1 identity; tenant ACTIVE","EVT-USR-ACTIVATED",None),
  (["ACTIVE"],"CMD-USR-LOCK","LOCKED","security officer or system anomaly rule; reason","EVT-USR-LOCKED","REASON_REQUIRED"),
  (["LOCKED"],"CMD-USR-UNLOCK","ACTIVE","security officer","EVT-USR-UNLOCKED",None),
  (["PENDING","ACTIVE","LOCKED"],"CMD-USR-DISABLE","DISABLED","SCIM deactivate or administrator","EVT-USR-DISABLED",None),
  (["DISABLED"],"CMD-USR-ENABLE","ACTIVE","≥ 1 identity; tenant ACTIVE","EVT-USR-ENABLED","LAST_IDENTITY"),
  (["DISABLED"],"CMD-USR-CLOSE","CLOSED","administrator; audit history retained","EVT-USR-CLOSED",None)],
 ["INV-USR-01: a user belongs to exactly one tenant",
  "INV-USR-02: (issuer, subject) is unique within the tenant",
  "INV-USR-03: an ACTIVE user has ≥ 1 identity and belongs to an ACTIVE tenant",
  "INV-USR-04: every change that affects authorization increments the subject security_version",
  "INV-USR-05: DISABLED, LOCKED and CLOSED users cannot obtain a SecurityContext"],
 ["Identity (entity: issuer, subject, linked_at)"],["REQ-FND-005","REQ-FND-006"])

agg("AGG-SERVICE-ACCOUNT","BC01","Service Account","T2","هوية لنظام أو محول، ليست لشخص",
 ["ACTIVE","DISABLED","CLOSED"],["CLOSED"],
 [("∅","CMD-SVC-CREATE","ACTIVE","owner user ACTIVE; purpose stated","EVT-SVC-CREATED","OWNER_REQUIRED"),
  (["ACTIVE"],"CMD-SVC-ROTATE-CREDENTIAL","=","new credential expiry ≤ 90 days","EVT-SVC-CREDENTIAL-ROTATED","CREDENTIAL_LIFETIME_EXCEEDED"),
  (["ACTIVE"],"CMD-SVC-DISABLE","DISABLED","—","EVT-SVC-DISABLED",None),
  (["DISABLED"],"CMD-SVC-ENABLE","ACTIVE","owner still ACTIVE","EVT-SVC-ENABLED","OWNER_REQUIRED"),
  (["DISABLED"],"CMD-SVC-CLOSE","CLOSED","—","EVT-SVC-CLOSED",None)],
 ["INV-SVC-01: a service account is never linked to a Person",
  "INV-SVC-02: every service account has an ACTIVE accountable owner user",
  "INV-SVC-03: credential lifetime ≤ 90 days (W4 delegated decision)"],
 ["Credential (entity: id, fingerprint, expires_at)"],["REQ-FND-006"])

agg("AGG-ROLE","BC01","Role","T2","تعريف دور = مجموعة صلاحيات (action × resource type)",
 ["DRAFT","ACTIVE","RETIRED"],["RETIRED"],
 [("∅","CMD-ROL-DEFINE","DRAFT","code unique in tenant","EVT-ROL-DEFINED","ROLE_CODE_TAKEN"),
  (["DRAFT","ACTIVE"],"CMD-ROL-SET-PERMISSIONS","=","permissions exist in catalog; system roles are locked; ACTIVE → new version","EVT-ROL-PERMISSIONS-CHANGED","SYSTEM_ROLE_LOCKED"),
  (["DRAFT"],"CMD-ROL-ACTIVATE","ACTIVE","≥ 1 permission","EVT-ROL-ACTIVATED","ROLE_EMPTY"),
  (["ACTIVE"],"CMD-ROL-RETIRE","RETIRED","not a system role; no active assignments","EVT-ROL-RETIRED","ROLE_IN_USE")],
 ["INV-ROL-01: the 15 platform roles (PRJ§45 actors) exist in every tenant and cannot be retired or edited",
  "INV-ROL-02: permissions are separate grants (View, Edit, Export, Share, Approve, Delete, Retain, Archive, command codes) — REQ-FND-014",
  "INV-ROL-03: permission changes to an ACTIVE role increment security_version of all its holders"],
 ["Permission (value object: action, resource_type)"],["REQ-FND-014"])

agg("AGG-ROLE-ASSIGNMENT","BC01","Role Assignment","T2","إسناد دور لمستخدم ضمن نطاق وحدة تنظيمية لفترة",
 ["ACTIVE","EXPIRED","REVOKED"],["EXPIRED","REVOKED"],
 [("∅","CMD-RAS-ASSIGN","ACTIVE","role ACTIVE; user not CLOSED; scope unit ACTIVE; assigner administers the scope; no SoD-incompatible active role","EVT-RAS-ASSIGNED","SOD_ROLE_CONFLICT"),
  (["ACTIVE"],"CMD-RAS-REVOKE","REVOKED","assigner administers the scope; reason","EVT-RAS-REVOKED","REASON_REQUIRED"),
  (["ACTIVE"],"SYS:valid_to reached","EXPIRED","system scheduler","EVT-RAS-EXPIRED",None)],
 ["INV-RAS-01: an assigner cannot assign a role outside units they administer, nor to themselves",
  "INV-RAS-02: SoD-incompatible roles cannot be active together for one user (default: Auditor × Administrator, Auditor × Security Officer)",
  "INV-RAS-03: assignment and revocation increment the user's security_version"],
 [],["REQ-FND-011","REQ-OPS-005","REQ-OPS-009"])

agg("AGG-AUTHORITY-GRANT","BC01","Authority Grant (incl. delegation)","T2","حق تقرير نوع قرار ضمن نطاق وحدود وفترة",
 ["PENDING_APPROVAL","ACTIVE","SUSPENDED","EXPIRED","REVOKED","REJECTED"],["EXPIRED","REVOKED","REJECTED"],
 [("∅","CMD-AUT-GRANT","PENDING_APPROVAL","actor has authority.grant permission; decision type exists; scope unit ACTIVE","EVT-AUT-GRANT-REQUESTED","PERMISSION_DENIED"),
  (["PENDING_APPROVAL"],"CMD-AUT-APPROVE-GRANT","ACTIVE","approver is Executive in scope; approver ≠ requester","EVT-AUT-GRANTED","SEGREGATION_OF_DUTIES"),
  (["PENDING_APPROVAL"],"CMD-AUT-REJECT-GRANT","REJECTED","reason","EVT-AUT-GRANT-REJECTED","REASON_REQUIRED"),
  ("∅","CMD-AUT-DELEGATE","ACTIVE","parent grant effective and delegable; scope ⊆ parent; limits ≤ parent; period ⊆ parent; depth ≤ 2; delegate ≠ delegator","EVT-AUT-DELEGATED","AUTHORITY_EXCEEDS_DELEGATOR"),
  (["ACTIVE"],"CMD-AUT-SUSPEND","SUSPENDED","reason","EVT-AUT-SUSPENDED","REASON_REQUIRED"),
  (["SUSPENDED"],"CMD-AUT-RESUME","ACTIVE","period not ended","EVT-AUT-RESUMED","GRANT_EXPIRED"),
  (["PENDING_APPROVAL","ACTIVE","SUSPENDED"],"CMD-AUT-REVOKE","REVOKED","granter, delegator or Executive in scope; reason","EVT-AUT-REVOKED","REASON_REQUIRED"),
  (["ACTIVE","SUSPENDED"],"SYS:valid_to reached","EXPIRED","system scheduler","EVT-AUT-EXPIRED",None)],
 ["INV-AUT-01: a delegation never exceeds its parent in decision types, scope, limits or period",
  "INV-AUT-02: delegation depth ≤ 2 (W4 delegated decision)",
  "INV-AUT-03: a grant is EFFECTIVE at t ⇔ state ACTIVE at t ∧ t ∈ validity ∧ (no parent ∨ parent EFFECTIVE at t) — revoking a parent makes children ineffective without writing to them",
  "INV-AUT-04: root grants require approval by an Executive other than the requester"],
 [],["REQ-FND-007","REQ-FND-008","REQ-FND-009"],
 "Holder may be a user or a role. AuthorityCheck (QRY-AUT-CHECK) evaluates INV-AUT-03 as of any time t, so decisions can be audited later.")

agg("AGG-CLEARANCE","BC01","Clearance","T2","مستوى التصريح والأقسام لمستخدم",
 ["PENDING_APPROVAL","ACTIVE","SUSPENDED","EXPIRED","REVOKED"],["EXPIRED","REVOKED"],
 [("∅","CMD-CLR-GRANT","PENDING_APPROVAL","Security Officer; level and compartments exist in ACTIVE scheme; subject has no other non-terminal clearance","EVT-CLR-REQUESTED","CLEARANCE_EXISTS"),
  (["PENDING_APPROVAL"],"CMD-CLR-APPROVE","ACTIVE","second Security Officer ≠ requester when level is top rank; else requester may self-confirm","EVT-CLR-GRANTED","SEGREGATION_OF_DUTIES"),
  (["ACTIVE"],"CMD-CLR-MODIFY","=","same rules as grant; creates new version","EVT-CLR-MODIFIED","CLEARANCE_INVALID"),
  (["ACTIVE"],"CMD-CLR-SUSPEND","SUSPENDED","reason","EVT-CLR-SUSPENDED","REASON_REQUIRED"),
  (["SUSPENDED"],"CMD-CLR-REINSTATE","ACTIVE","period not ended","EVT-CLR-REINSTATED",None),
  (["PENDING_APPROVAL","ACTIVE","SUSPENDED"],"CMD-CLR-REVOKE","REVOKED","reason","EVT-CLR-REVOKED","REASON_REQUIRED"),
  (["ACTIVE","SUSPENDED"],"SYS:valid_to reached","EXPIRED","system","EVT-CLR-EXPIRED",None)],
 ["INV-CLR-01: at most one non-terminal clearance per user",
  "INV-CLR-02: no one grants or approves their own clearance",
  "INV-CLR-03: top-rank clearance requires two distinct Security Officers (W4 delegated decision)",
  "INV-CLR-04: every change increments the user's security_version"],
 [],["REQ-GOV-003","REQ-GOV-004"])

# ---------------- BC08 ----------------
agg("AGG-CLASSIFICATION-SCHEME","BC08","Classification Scheme Version","T2","نظام التصنيف لكل مستأجر بإصدارات",
 ["DRAFT","ACTIVE","SUPERSEDED","DISCARDED"],["SUPERSEDED","DISCARDED"],
 [("∅","CMD-CLS-DRAFT","DRAFT","Security Officer; at most one DRAFT per tenant","EVT-CLS-DRAFTED","DRAFT_EXISTS"),
  (["DRAFT"],"CMD-CLS-EDIT","=","codes immutable once used; ranks strictly ordered; removal not allowed, only deprecation","EVT-CLS-EDITED","SCHEME_INVALID"),
  (["DRAFT"],"CMD-CLS-ACTIVATE","ACTIVE","validation passes; effective_from ≥ now; approver ≠ drafter; previous ACTIVE → SUPERSEDED in same transaction","EVT-CLS-ACTIVATED","SCHEME_INVALID"),
  (["DRAFT"],"CMD-CLS-DISCARD","DISCARDED","—","EVT-CLS-DISCARDED",None),
  (["ACTIVE"],"SYS:successor activated","SUPERSEDED","system","EVT-CLS-SUPERSEDED",None)],
 ["INV-CLS-01: exactly one ACTIVE scheme version per tenant",
  "INV-CLS-02: level ranks strictly ordered and unique; codes immutable",
  "INV-CLS-03: levels, compartments and caveats can be deprecated, never removed",
  "INV-CLS-04: activation increments the security_version of all subjects in the tenant"],
 ["Level, Compartment, Caveat (value objects)"],["REQ-GOV-001","REQ-GOV-004","REQ-GOV-009"],
 "REQ-GOV-004 added to satisfies by CR-65 (2026-09-29): CMD-CLS-ACTIVATE's guard (previous ACTIVE -> SUPERSEDED in same transaction) plus INV-CLS-04 (activation increments security_version of all subjects in the tenant) is the scheme-level enforcement mechanism for REQ-GOV-004's \"stop returning the object to newly unauthorized subjects from the moment of the change\" -- previously undeclared here despite UC-085 already being listed against REQ-GOV-004 in requirements.md (see CR-64 residual_note).")

agg("AGG-POLICY-SET","BC08","Policy Set Version","T2","مجموعة سياسات مستأجر (جداول قرار) بإصدارات",
 ["DRAFT","IN_REVIEW","APPROVED","ACTIVE","SUPERSEDED","REJECTED"],["SUPERSEDED","REJECTED"],
 [("∅","CMD-POL-DRAFT","DRAFT","Security Officer","EVT-POL-DRAFTED",None),
  (["DRAFT"],"CMD-POL-EDIT","=","tables validate against schema","EVT-POL-EDITED","POLICY_INVALID"),
  (["DRAFT"],"CMD-POL-SUBMIT","IN_REVIEW","embedded policy tests all pass; tenant rules only restrict platform baseline","EVT-POL-SUBMITTED","POLICY_TESTS_FAILED"),
  (["IN_REVIEW"],"CMD-POL-APPROVE","APPROVED","approver ≠ author; Security Officer","EVT-POL-APPROVED","SEGREGATION_OF_DUTIES"),
  (["IN_REVIEW"],"CMD-POL-REJECT","REJECTED","reason","EVT-POL-REJECTED","REASON_REQUIRED"),
  (["APPROVED"],"SYS:effective_from reached","ACTIVE","scheduler; previous ACTIVE → SUPERSEDED","EVT-POL-ACTIVATED",None),
  (["ACTIVE"],"SYS:successor activated","SUPERSEDED","system","EVT-POL-SUPERSEDED",None)],
 ["INV-POL-01: exactly one ACTIVE policy set version per tenant; platform baseline always applies on top",
  "INV-POL-02: tenant policies can only restrict the platform baseline, except parameters explicitly marked configurable (e.g. SoD toggle)",
  "INV-POL-03: a version cannot be approved by its author",
  "INV-POL-04: every version carries decision-table tests that must pass before review"],
 ["DecisionTable (value object)","PolicyTest (value object)"],["REQ-FND-011","REQ-FND-012","REQ-GOV-009"])

agg("AGG-SECURITY-EXCEPTION","BC08","Security Exception","T2","استثناء مؤقت من سياسة مستأجر بموافقة شخصين",
 ["REQUESTED","FIRST_APPROVED","ACTIVE","REJECTED","EXPIRED","REVOKED"],["REJECTED","EXPIRED","REVOKED"],
 [("∅","CMD-EXC-REQUEST","REQUESTED","targets a tenant policy rule (not platform baseline); duration ≤ 30 days; justification","EVT-EXC-REQUESTED","EXCEPTION_NOT_ALLOWED"),
  (["REQUESTED"],"CMD-EXC-APPROVE","FIRST_APPROVED","approver authorized; approver ≠ requester","EVT-EXC-FIRST-APPROVED","SEGREGATION_OF_DUTIES"),
  (["FIRST_APPROVED"],"CMD-EXC-APPROVE","ACTIVE","approver authorized; approver ∉ {requester, first approver}","EVT-EXC-ACTIVATED","SEGREGATION_OF_DUTIES"),
  (["REQUESTED","FIRST_APPROVED"],"CMD-EXC-REJECT","REJECTED","reason","EVT-EXC-REJECTED","REASON_REQUIRED"),
  (["ACTIVE"],"CMD-EXC-REVOKE","REVOKED","Security Officer; reason","EVT-EXC-REVOKED","REASON_REQUIRED"),
  (["ACTIVE"],"SYS:end reached","EXPIRED","scheduler","EVT-EXC-EXPIRED",None)],
 ["INV-EXC-01: activation requires two distinct approvers, both different from the requester (REQ-FND-017)",
  "INV-EXC-02: exceptions never apply to platform baseline rules (tenant isolation, classification rule, audit, fail-closed)",
  "INV-EXC-03: maximum duration 30 days; renewal = new request (W4 delegated decision)"],
 [],["REQ-FND-017"])

# ---------------- Queries ----------------
QUERIES = [
 ("QRY-TEN-GET","BC01","GET","/api/v1/foundation/tenants/{tenant_id}","Tenant state, cell, quotas","platform operator or tenant Administrator of that tenant","REQ-FND-001"),
 ("QRY-ORG-TREE","BC01","GET","/api/v1/foundation/organizations/{org_id}/units","Unit tree (cursor pagination on flattened order)","any user of tenant (view org structure)","REQ-FND-002"),
 ("QRY-USR-LIST","BC01","GET","/api/v1/foundation/users","Users filtered by state, unit, role","Administrator in scope","REQ-FND-006"),
 ("QRY-USR-GET","BC01","GET","/api/v1/foundation/users/{user_id}","User with identities (no secrets)","Administrator in scope or self","REQ-FND-006"),
 ("QRY-SEC-CONTEXT","BC01","GET","/api/v1/foundation/me/security-context","Caller's resolved SecurityContext","self","REQ-FND-010"),
 ("QRY-AUT-CHECK","BC01","POST","/api/v1/foundation/authority-checks","AuthorityCheck(actor, decision_type, scope, at, amount?)","internal services (workload identity) or self","REQ-FND-009"),
 ("QRY-AUT-LIST","BC01","GET","/api/v1/foundation/authority-grants","Grants by holder / scope / effective at t","Executive or Administrator in scope, or holder","REQ-FND-007"),
 ("QRY-CLR-GET","BC01","GET","/api/v1/foundation/users/{user_id}/clearance","Current clearance (level/compartments)","Security Officer or self","REQ-GOV-003"),
 ("QRY-CLS-ACTIVE","BC08","GET","/api/v1/governance/classification-scheme","Active scheme (labels only)","any user of tenant","REQ-GOV-001"),
 ("QRY-POL-GET","BC08","GET","/api/v1/governance/policy-sets/{version_id}","Policy set version with tables and tests","Security Officer, Auditor","REQ-GOV-009"),
 ("QRY-PDP-DECIDE","BC08","POST","/api/v1/governance/policy-decisions","DecisionRequest → DecisionResponse (authorization-model §2)","internal PEPs only (workload identity)","REQ-FND-010"),
 ("QRY-AUD-SEARCH","BC08","GET","/api/v1/governance/audit-records","Audit records by actor, resource, time, correlation id","Auditor, Security Officer (itself audited)","REQ-FND-015"),
 ("QRY-AUD-VERIFY","BC08","POST","/api/v1/governance/audit-integrity-checks","Start integrity verification job; returns job ref","Auditor","REQ-FND-016"),
 ("QRY-EXC-LIST","BC08","GET","/api/v1/governance/security-exceptions","Exceptions by state","Security Officer, Auditor","REQ-FND-017"),
]

# Command → actor roles & policy (defaults; system commands use scheduler/service identity)
ACTORS = {
 "TEN":"Platform Operator (provision, migrate, decommission) / Tenant Administrator (quotas view)",
 "ORG":"Administrator (in scope)","PER":"Administrator (in scope)","USR":"Administrator in scope / SCIM service account / Security Officer (lock)",
 "SVC":"Administrator","ROL":"Administrator","RAS":"Administrator (in scope, not self)","AUT":"holder of authority.grant; Executive approves",
 "CLR":"Security Officer","CLS":"Security Officer","POL":"Security Officer","EXC":"any authorized requester; Security Officers approve"}

PERPETUAL = {"AGG-ORGANIZATION":"Organizations are kept for institutional history; they become INACTIVE, never deleted (SL-06 exemption, justified)"}

# payload fields: name:type ; "!" = required
P = {
 "CMD-TEN-PROVISION":"namespace!:string display_name!:string cell_mode!:enum(shared,dedicated) sovereign!:boolean top_level_enabled!:boolean jurisdiction!:string quotas!:TenantQuotas",
 "CMD-TEN-COMPLETE-PROVISIONING":"steps!:array", "CMD-TEN-FAIL-PROVISIONING":"failed_step!:string reason!:string",
 "CMD-TEN-RETRY-PROVISIONING":"", "CMD-TEN-SUSPEND":"reason!:string", "CMD-TEN-REACTIVATE":"",
 "CMD-TEN-START-CELL-MIGRATION":"target_cell!:string", "CMD-TEN-COMPLETE-CELL-MIGRATION":"reconciliation_report!:string",
 "CMD-TEN-START-DECOMMISSION":"reason!:string second_approver!:urn", "CMD-TEN-COMPLETE-DECOMMISSION":"", "CMD-TEN-UPDATE-QUOTAS":"quotas!:TenantQuotas",
 "CMD-ORG-CREATE":"name!:LocalizedName root_unit_name!:LocalizedName", "CMD-ORG-RENAME":"name!:LocalizedName",
 "CMD-ORG-ADD-UNIT":"parent_unit!:urn name!:LocalizedName", "CMD-ORG-RENAME-UNIT":"unit!:urn name!:LocalizedName",
 "CMD-ORG-MOVE-UNIT":"unit!:urn new_parent!:urn", "CMD-ORG-DEACTIVATE-UNIT":"unit!:urn reason!:string",
 "CMD-ORG-DEACTIVATE":"reason!:string", "CMD-ORG-REACTIVATE":"",
 "CMD-PER-REGISTER":"names!:array hr_id:string contact:object", "CMD-PER-UPDATE-DETAILS":"names:array contact:object",
 "CMD-PER-DEACTIVATE":"reason!:string", "CMD-PER-REACTIVATE":"", "CMD-PER-ERASE":"erasure_order_ref!:string",
 "CMD-USR-PROVISION":"username!:string person:urn source!:enum(scim,admin)", "CMD-USR-LINK-IDENTITY":"issuer!:string subject!:string",
 "CMD-USR-UNLINK-IDENTITY":"issuer!:string subject!:string", "CMD-USR-LINK-PERSON":"person!:urn",
 "CMD-USR-RECORD-FIRST-SIGN-IN":"issuer!:string subject!:string", "CMD-USR-LOCK":"reason!:string", "CMD-USR-UNLOCK":"reason!:string",
 "CMD-USR-DISABLE":"reason:string", "CMD-USR-ENABLE":"", "CMD-USR-CLOSE":"reason!:string",
 "CMD-SVC-CREATE":"name!:string owner!:urn purpose!:string", "CMD-SVC-ROTATE-CREDENTIAL":"public_key!:string expires_at!:date-time",
 "CMD-SVC-DISABLE":"reason:string", "CMD-SVC-ENABLE":"", "CMD-SVC-CLOSE":"",
 "CMD-ROL-DEFINE":"code!:string name!:LocalizedName", "CMD-ROL-SET-PERMISSIONS":"permissions!:array", "CMD-ROL-ACTIVATE":"", "CMD-ROL-RETIRE":"reason!:string",
 "CMD-RAS-ASSIGN":"user!:urn role!:urn org_scope!:urn include_descendants!:boolean valid_from!:date-time valid_to:date-time",
 "CMD-RAS-REVOKE":"reason!:string",
 "CMD-AUT-GRANT":"holder!:urn decision_types!:array org_scope!:urn include_descendants!:boolean limits:object valid_from!:date-time valid_to:date-time delegable!:boolean",
 "CMD-AUT-APPROVE-GRANT":"", "CMD-AUT-REJECT-GRANT":"reason!:string",
 "CMD-AUT-DELEGATE":"delegate!:urn decision_types!:array org_scope!:urn include_descendants!:boolean limits:object valid_from!:date-time valid_to!:date-time delegable!:boolean",
 "CMD-AUT-SUSPEND":"reason!:string", "CMD-AUT-RESUME":"", "CMD-AUT-REVOKE":"reason!:string",
 "CMD-CLR-GRANT":"user!:urn level!:string compartments!:array caveat_attributes:object valid_to:date-time", "CMD-CLR-APPROVE":"",
 "CMD-CLR-MODIFY":"level!:string compartments!:array caveat_attributes:object", "CMD-CLR-SUSPEND":"reason!:string", "CMD-CLR-REINSTATE":"", "CMD-CLR-REVOKE":"reason!:string",
 "CMD-CLS-DRAFT":"based_on:urn", "CMD-CLS-EDIT":"levels!:array compartments!:array caveats!:array audit_threshold!:string default_level!:string",
 "CMD-CLS-ACTIVATE":"effective_from!:date-time", "CMD-CLS-DISCARD":"",
 "CMD-POL-DRAFT":"based_on:urn", "CMD-POL-EDIT":"decision_tables!:array tests!:array", "CMD-POL-SUBMIT":"effective_from!:date-time",
 "CMD-POL-APPROVE":"", "CMD-POL-REJECT":"reason!:string",
 "CMD-EXC-REQUEST":"policy_rule!:string subject_scope!:object justification!:string starts_at!:date-time ends_at!:date-time",
 "CMD-EXC-APPROVE":"note:string", "CMD-EXC-REJECT":"reason!:string", "CMD-EXC-REVOKE":"reason!:string",
}
SYSTEM_CMDS = {"CMD-TEN-COMPLETE-PROVISIONING","CMD-TEN-FAIL-PROVISIONING","CMD-TEN-COMPLETE-CELL-MIGRATION","CMD-TEN-COMPLETE-DECOMMISSION","CMD-USR-RECORD-FIRST-SIGN-IN"}
RESOURCE = {"AGG-TENANT":("foundation","tenants"),"AGG-ORGANIZATION":("foundation","organizations"),"AGG-PERSON":("foundation","persons"),
 "AGG-USER":("foundation","users"),"AGG-SERVICE-ACCOUNT":("foundation","service-accounts"),"AGG-ROLE":("foundation","roles"),
 "AGG-ROLE-ASSIGNMENT":("foundation","role-assignments"),"AGG-AUTHORITY-GRANT":("foundation","authority-grants"),"AGG-CLEARANCE":("foundation","clearances"),
 "AGG-CLASSIFICATION-SCHEME":("governance","classification-schemes"),"AGG-POLICY-SET":("governance","policy-sets"),"AGG-SECURITY-EXCEPTION":("governance","security-exceptions")}
SECURITY_AFFECTING = {"EVT-USR-DISABLED","EVT-USR-LOCKED","EVT-USR-CLOSED","EVT-USR-ENABLED","EVT-USR-UNLOCKED","EVT-USR-ACTIVATED","EVT-USR-IDENTITY-UNLINKED",
 "EVT-ROL-PERMISSIONS-CHANGED","EVT-RAS-ASSIGNED","EVT-RAS-REVOKED","EVT-RAS-EXPIRED","EVT-CLR-GRANTED","EVT-CLR-MODIFIED","EVT-CLR-SUSPENDED",
 "EVT-CLR-REINSTATED","EVT-CLR-REVOKED","EVT-CLR-EXPIRED","EVT-CLS-ACTIVATED","EVT-POL-ACTIVATED","EVT-EXC-ACTIVATED","EVT-EXC-REVOKED","EVT-EXC-EXPIRED",
 "EVT-TEN-SUSPENDED","EVT-TEN-REACTIVATED","EVT-ORG-UNIT-MOVED","EVT-ORG-UNIT-DEACTIVATED","EVT-AUT-GRANTED","EVT-AUT-REVOKED","EVT-AUT-SUSPENDED","EVT-AUT-RESUMED","EVT-AUT-EXPIRED","EVT-AUT-DELEGATED"}
```

## slc02_data.py

```python
# -*- coding: utf-8 -*-
# SLC-02 — Information Kernel: Source → Observation → Entity / Claim → Evidence (+ relationships, attachments, ingestion, external ids)
SLICE = "SLC-02"
AGGS = {}
def agg(id_, bc, name, tier, purpose, states, terminal, transitions, invariants, entities, reqs, notes=None, personal=False):
    AGGS[id_] = dict(id=id_, bc=bc, name=name, tier=tier, purpose=purpose, states=states, terminal=terminal,
                     transitions=transitions, invariants=invariants, entities=entities, requirements=reqs, notes=notes, personal_data=personal)
def RECLASS(pfx, states, evt):
    return (states, f"CMD-{pfx}-RECLASSIFY", "=", "authority per tenant policy (REQ-GOV-004); new version; bumps object security_version", evt, "CLASSIFICATION_CHANGE_NOT_AUTHORIZED")

agg("AGG-SOURCE","BC02","Source","T1 reliability / T2 profile","جهة أو نظام أو مستشعر ينتج معلومات، مع موثوقية مؤرخة وحماية هوية",
 ["ACTIVE","SUSPENDED","RETIRED"],["RETIRED"],
 [("∅","CMD-SRC-REGISTER","ACTIVE","type in RD-SOURCE-TYPES; initial reliability A–F; person-type sources get protection_level ≥ 1 and label ≥ tenant default + 1 rank","EVT-SRC-REGISTERED","SOURCE_INVALID"),
  (["ACTIVE","SUSPENDED"],"CMD-SRC-RATE-RELIABILITY","=","rating ∈ A–F; valid_from given; creates bitemporal reliability claim","EVT-SRC-RELIABILITY-RATED","RATING_INVALID"),
  (["ACTIVE","SUSPENDED"],"CMD-SRC-UPDATE-PROFILE","=","—","EVT-SRC-PROFILE-UPDATED",None),
  (["ACTIVE","SUSPENDED"],"CMD-SRC-SET-PROTECTION","=","Security Officer; decreasing protection requires a second Security Officer","EVT-SRC-PROTECTION-CHANGED","SEGREGATION_OF_DUTIES"),
  RECLASS("SRC",["ACTIVE","SUSPENDED"],"EVT-SRC-RECLASSIFIED"),
  (["ACTIVE"],"CMD-SRC-SUSPEND","SUSPENDED","reason","EVT-SRC-SUSPENDED","REASON_REQUIRED"),
  (["SUSPENDED"],"CMD-SRC-REINSTATE","ACTIVE","—","EVT-SRC-REINSTATED",None),
  (["ACTIVE","SUSPENDED"],"CMD-SRC-RETIRE","RETIRED","reason; history retained","EVT-SRC-RETIRED","REASON_REQUIRED")],
 ["INV-SRC-01: reliability is a bitemporal claim; a claim's source_reliability is the rating valid and known at the claim's recorded_from",
  "INV-SRC-02: identity attributes of person-type sources are visible only with the source-protection permission; others see type and reliability only",
  "INV-SRC-03: SUSPENDED or RETIRED sources cannot be cited by new claims or observations",
  "INV-SRC-04: retiring never alters past ratings or claims"],
 ["ReliabilityRating (bitemporal)","Profile (T2)"],["REQ-INF-001"])

agg("AGG-OBSERVATION","BC02","Observation","T1","ما رصده مصدر في زمن ومكان؛ غير قابل للتعديل بعد الاعتماد",
 ["RECORDED","VALIDATED","REJECTED"],["VALIDATED","REJECTED"],
 [("∅","CMD-OBS-RECORD","RECORDED","source ACTIVE; location with CRS + accuracy + valid geometry; UCUM units; observed_at ≤ server time + 5 min; recorded_from by server","EVT-OBS-RECORDED","OBSERVATION_INVALID"),
  (["RECORDED"],"CMD-OBS-AMEND","=","actor = observer or Analyst; new version; reason","EVT-OBS-AMENDED","REASON_REQUIRED"),
  (["RECORDED"],"CMD-OBS-ATTACH-EVIDENCE","=","evidence REGISTERED or SEALED","EVT-OBS-EVIDENCE-ATTACHED","EVIDENCE_INVALID"),
  RECLASS("OBS",["RECORDED","VALIDATED","REJECTED"],"EVT-OBS-RECLASSIFIED"),
  (["RECORDED"],"CMD-OBS-VALIDATE","VALIDATED","Analyst ≠ observer, or system auto-validation for sensor sources rated A/B under tenant policy","EVT-OBS-VALIDATED","SEGREGATION_OF_DUTIES"),
  (["RECORDED"],"CMD-OBS-REJECT","REJECTED","reason","EVT-OBS-REJECTED","REASON_REQUIRED")],
 ["INV-OBS-01: recorded_from is server-assigned; observed_at comes from the source/device",
  "INV-OBS-02: content is immutable once VALIDATED or REJECTED (reclassification versions the label only)",
  "INV-OBS-03: every derived claim references the observation in lineage",
  "INV-OBS-04: device clock skew > 5 min adds data_quality issue DEVICE_CLOCK_SUSPECT"],
 ["Measurement (quantity, value, UCUM unit, uncertainty)","Location (spatial envelope)"],["REQ-INF-002","REQ-INF-028"],
 "High-rate feeds send CMD-OBS-RECORD in batches of ≤ 1,000 items, each with its own idempotency key (QAS-PERF-012).")

agg("AGG-ENTITY","BC02","Entity (identity)","T2 identity; attributes T1 as claims","هوية كيان؛ سماته ادعاءات مستقلة",
 ["ACTIVE","RETIRED"],[],
 [("∅","CMD-ENT-REGISTER","ACTIVE","type in RD-ENTITY-TYPES; each initial claim valid as CMD-CLM-ASSERT; Entity + initial Claims created in one unit of work","EVT-ENT-REGISTERED","ENTITY_INVALID"),
  (["ACTIVE"],"CMD-ENT-CHANGE-TYPE","=","compatible type per RD-ENTITY-TYPES; new version; reason","EVT-ENT-TYPE-CHANGED","ENTITY_TYPE_INCOMPATIBLE"),
  RECLASS("ENT",["ACTIVE","RETIRED"],"EVT-ENT-RECLASSIFIED"),
  (["ACTIVE"],"CMD-ENT-RETIRE","RETIRED","reason (created in error / no longer tracked); claims untouched","EVT-ENT-RETIRED","REASON_REQUIRED"),
  (["RETIRED"],"CMD-ENT-REINSTATE","ACTIVE","reason","EVT-ENT-REINSTATED","REASON_REQUIRED")],
 ["INV-ENT-01: an entity holds no attribute values; all T1 attributes are claims",
  "INV-ENT-02: claims hidden from a reader are invisible everywhere, including completeness and counts",
  "INV-ENT-03: RETIRED entities remain resolvable for history and as-of queries"],
 [],["REQ-INF-020","REQ-INF-021","REQ-INF-036"])

agg("AGG-REALWORLD-EVENT","BC02","Real-World Event (identity)","T2 identity; attributes T1","حدث وقع في العالم (ليس Domain Event)",
 ["ACTIVE","RETIRED"],[],
 [("∅","CMD-RWE-REGISTER","ACTIVE","type in RD-EVENT-TYPES; initial claims include event_time (fuzzy) and location","EVT-RWE-REGISTERED","EVENT_INVALID"),
  (["ACTIVE"],"CMD-RWE-CHANGE-TYPE","=","compatible type; reason","EVT-RWE-TYPE-CHANGED","EVENT_TYPE_INCOMPATIBLE"),
  RECLASS("RWE",["ACTIVE","RETIRED"],"EVT-RWE-RECLASSIFIED"),
  (["ACTIVE"],"CMD-RWE-RETIRE","RETIRED","reason","EVT-RWE-RETIRED","REASON_REQUIRED"),
  (["RETIRED"],"CMD-RWE-REINSTATE","ACTIVE","reason","EVT-RWE-REINSTATED","REASON_REQUIRED")],
 ["INV-RWE-01: event_time is a fuzzy-interval claim with precision","INV-RWE-02: participants are relationships, not embedded lists"],
 [],["REQ-INF-020"])

agg("AGG-RELATIONSHIP","BC02","Relationship (identity)","T1","رابط موجّه بين كائنين؛ وجوده ادعاء",
 ["ACTIVE","RETIRED"],[],
 [("∅","CMD-REL-REGISTER","ACTIVE","type in RD-RELATIONSHIP-TYPES; endpoint types allowed; creates identity + existence claim (valid interval, sources ≥ 1)","EVT-REL-REGISTERED","RELATIONSHIP_INVALID"),
  RECLASS("REL",["ACTIVE","RETIRED"],"EVT-REL-RECLASSIFIED"),
  (["ACTIVE"],"CMD-REL-RETIRE","RETIRED","created in error only; ending in reality = CMD-CLM-RECORD-CHANGE on the existence claim","EVT-REL-RETIRED","REASON_REQUIRED"),
  (["RETIRED"],"CMD-REL-REINSTATE","ACTIVE","reason","EVT-REL-REINSTATED","REASON_REQUIRED")],
 ["INV-REL-01: validity comes from the existence claim; the identity carries type, endpoints and label",
  "INV-REL-02: a relationship may be labelled above both endpoints and is then invisible without clearance"],
 [],["REQ-INF-027"])

agg("AGG-CLAIM","BC02","Claim","T1","عبارة (موضوع، سمة، قيمة) مؤرخة ثنائياً ومسندة؛ قيمتها لا تتغير",
 ["CURRENT","CLOSED"],["CLOSED"],
 [("∅","CMD-CLM-ASSERT","CURRENT","subject exists; predicate in RD-PREDICATES; value matches predicate type/unit/cardinality; ≥ 1 source, all ACTIVE; valid_from < valid_to; geometry rules; confidence dims valid","EVT-CLM-ASSERTED","CLAIM_INVALID"),
  (["CURRENT"],"CMD-CLM-CORRECT","CLOSED","closes recorded_to = now and asserts the replacement (same subject/predicate) in the same transaction; reason","EVT-CLM-CORRECTED","REASON_REQUIRED"),
  (["CURRENT"],"CMD-CLM-RECORD-CHANGE","CLOSED","t_change ∈ (valid_from, valid_to): closes record, re-records old value with valid_to = t_change, asserts new value from t_change","EVT-CLM-CHANGED","CHANGE_TIME_INVALID"),
  (["CURRENT"],"CMD-CLM-RETRACT","CLOSED","reason; no replacement","EVT-CLM-RETRACTED","REASON_REQUIRED"),
  (["CURRENT"],"CMD-CLM-ASSESS","=","updates information_confidence / verification_status only (T2 versioned assessment); value and times untouched","EVT-CLM-ASSESSED","ASSESSMENT_INVALID"),
  RECLASS("CLM",["CURRENT","CLOSED"],"EVT-CLM-RECLASSIFIED")],
 ["INV-CLM-01: subject, predicate, value, valid interval and sources are immutable",
  "INV-CLM-02: recorded_from/recorded_to are server-assigned; CLOSED ⇔ recorded_to ≠ null",
  "INV-CLM-03: ≥ 1 source; each cited source was ACTIVE at assertion",
  "INV-CLM-04: successors reference their predecessor (supersedes chain)",
  "INV-CLM-05: source identity protection never leaks through the claim"],
 ["Value (typed)","ConfidenceAssessment (T2 versioned)"],["REQ-INF-021","REQ-INF-022","REQ-INF-024","REQ-INF-026","REQ-INF-037"],
 "CLOSED is terminal for content; re-labelling a CLOSED claim is allowed so history can be reclassified.")

agg("AGG-EVIDENCE","BC02","Evidence","T1","مادة تدعم أو تنفي ادعاءً، بسلسلة حيازة",
 ["REGISTERED","SEALED","WITHDRAWN"],["WITHDRAWN"],
 [("∅","CMD-EVD-REGISTER","REGISTERED","attachment STORED or observation_ref; type in RD-EVIDENCE-TYPES; source ACTIVE","EVT-EVD-REGISTERED","EVIDENCE_INVALID"),
  (["REGISTERED"],"CMD-EVD-UPDATE-LOCATOR","=","locator within attachment bounds","EVT-EVD-LOCATOR-UPDATED","LOCATOR_INVALID"),
  (["REGISTERED"],"CMD-EVD-SEAL","SEALED","integrity hash over metadata + attachment hash","EVT-EVD-SEALED",None),
  (["REGISTERED","SEALED"],"CMD-EVD-TRANSFER-CUSTODY","=","actor is current holder or custodian role; new holder named","EVT-EVD-CUSTODY-TRANSFERRED","CUSTODY_INVALID"),
  RECLASS("EVD",["REGISTERED","SEALED","WITHDRAWN"],"EVT-EVD-RECLASSIFIED"),
  (["REGISTERED","SEALED"],"CMD-EVD-WITHDRAW","WITHDRAWN","reason (e.g. forged); links kept and flagged; dependent verification re-evaluated","EVT-EVD-WITHDRAWN","REASON_REQUIRED")],
 ["INV-EVD-01: evidence is never deleted; withdrawal keeps it and its links","INV-EVD-02: after SEALED only custody and label change","INV-EVD-03: custody chain is gapless"],
 ["CustodyEntry","Locator"],["REQ-INF-003","REQ-INF-004"])

agg("AGG-EVIDENCE-LINK","BC02","Evidence Link","T1","ربط دليل بادعاء (يدعم / ينفي / سياق)",
 ["ACTIVE","REMOVED"],["REMOVED"],
 [("∅","CMD-EVL-LINK","ACTIVE","evidence not WITHDRAWN; claim exists; stance ∈ {SUPPORTS, REFUTES, CONTEXT}; no ACTIVE duplicate (evidence, claim, stance)","EVT-EVL-LINKED","LINK_DUPLICATE"),
  (["ACTIVE"],"CMD-EVL-UNLINK","REMOVED","reason; recorded_to closed","EVT-EVL-UNLINKED","REASON_REQUIRED")],
 ["INV-EVL-01: links are bitemporal records; removal closes recorded_to","INV-EVL-02: link label = max(evidence label, claim label)"],
 [],["REQ-INF-021"])

agg("AGG-ATTACHMENT","BC02","Attachment","T1 metadata","ملف في Object Storage، معنون بالمحتوى، يُرفع ويُنزّل مباشرة",
 ["PENDING","SCANNING","STORED","QUARANTINED","EXPIRED","ERASED"],["QUARANTINED","EXPIRED","ERASED"],
 [("∅","CMD-ATT-INITIATE-UPLOAD","PENDING","size ≤ tenant limit; mime allowed; returns direct upload target (≤ 5 min); same sha256 already STORED in tenant → returns existing","EVT-ATT-UPLOAD-INITIATED","ATTACHMENT_REJECTED"),
  (["PENDING"],"CMD-ATT-COMPLETE-UPLOAD","SCANNING","stored bytes hash = declared sha256; size matches","EVT-ATT-UPLOADED","HASH_MISMATCH"),
  (["SCANNING"],"SYS:scan passed","STORED","offline content scanner + format validation","EVT-ATT-STORED",None),
  (["SCANNING"],"SYS:scan failed","QUARANTINED","scanner verdict","EVT-ATT-QUARANTINED",None),
  (["PENDING"],"SYS:upload window 24 h elapsed","EXPIRED","scheduler","EVT-ATT-EXPIRED",None),
  (["STORED"],"CMD-ATT-ERASE","ERASED","erasure order or disposition; no legal hold; key destroyed (ADR-P08)","EVT-ATT-ERASED","LEGAL_HOLD_ACTIVE")],
 ["INV-ATT-01: (tenant, sha256) unique among non-terminal attachments",
  "INV-ATT-02: bytes never pass through application servers (direct transfer, signed targets ≤ 5 min)",
  "INV-ATT-03: only STORED attachments can back evidence or observations","INV-ATT-04: every download is authorized per request and audited"],
 [],["REQ-INF-003","REQ-INF-004","REQ-GOV-008"],"Direct-to-storage transfer removes the application tier from the bandwidth path (SR-05).")

agg("AGG-IMPORT-BATCH","BC02","Import Batch","T2","دفعة استيراد من محول أو ملف، مع حجر وlineage",
 ["RECEIVED","PROCESSING","COMPLETED","COMPLETED_WITH_QUARANTINE","FAILED","CANCELLED"],["COMPLETED","FAILED","CANCELLED"],
 [("∅","CMD-IMP-SUBMIT","RECEIVED","adapter ACTIVE (or authorized manual import); batch_key unique per adapter: same key + same content hash returns the existing batch; different hash → rejected","EVT-IMP-RECEIVED","BATCH_KEY_REUSED"),
  (["RECEIVED"],"SYS:processing started","PROCESSING","worker lease acquired","EVT-IMP-PROCESSING-STARTED",None),
  (["PROCESSING"],"SYS:all records applied","COMPLETED","each record applied idempotently with lineage (adapter, batch, mapping version)","EVT-IMP-COMPLETED",None),
  (["PROCESSING"],"SYS:finished with invalid records","COMPLETED_WITH_QUARANTINE","invalid records quarantined with reason codes","EVT-IMP-COMPLETED-WITH-QUARANTINE",None),
  (["PROCESSING"],"SYS:unrecoverable error","FAILED","applied records remain; re-submit resumes idempotently","EVT-IMP-FAILED",None),
  (["COMPLETED_WITH_QUARANTINE"],"CMD-IMP-REPROCESS-QUARANTINE","PROCESSING","new mapping version or corrected records","EVT-IMP-REPROCESSING",None),
  (["COMPLETED_WITH_QUARANTINE"],"CMD-IMP-ACCEPT-QUARANTINE","COMPLETED","reason; quarantined records dropped, record kept","EVT-IMP-QUARANTINE-ACCEPTED","REASON_REQUIRED"),
  (["RECEIVED"],"CMD-IMP-CANCEL","CANCELLED","reason","EVT-IMP-CANCELLED","REASON_REQUIRED")],
 ["INV-IMP-01: re-submitting the same batch never duplicates records","INV-IMP-02: no quarantined record appears in queries or projections",
  "INV-IMP-03: every applied record has lineage to batch + mapping version","INV-IMP-04: imported values are claims citing the adapter's source (BRL-013)"],
 ["QuarantineRecord (raw, reason codes)"],["REQ-INF-005","REQ-INF-006","REQ-INF-007","REQ-INF-008","REQ-INF-009"],
 "Records match entities via AGG-EXTERNAL-ID; unmatched records create new entities and an ER candidate (SLC-04).")

agg("AGG-EXTERNAL-ID","BC02","External Identifier Mapping","T2","ربط معرّف نظام خارجي بكائن داخلي لفترة",
 ["ACTIVE","ENDED"],["ENDED"],
 [("∅","CMD-EXT-MAP","ACTIVE","(system, external_id) has no ACTIVE mapping; target exists","EVT-EXT-MAPPED","EXTERNAL_ID_TAKEN"),
  (["ACTIVE"],"CMD-EXT-END","ENDED","reason; valid_to set","EVT-EXT-ENDED","REASON_REQUIRED")],
 ["INV-EXT-01: at any time t, (tenant, system, external_id) maps to at most one object","INV-EXT-02: mappings are never deleted"],
 [],["REQ-INF-036"])

agg("AGG-ADAPTER","BC07","Adapter","T2","محول تكامل مسجل بمصدر وحساب خدمة وإصدار تحويل",
 ["DRAFT","ACTIVE","SUSPENDED","RETIRED"],["RETIRED"],
 [("∅","CMD-ADP-REGISTER","DRAFT","source ACTIVE; service account ACTIVE; mapping spec present","EVT-ADP-REGISTERED","ADAPTER_INVALID"),
  (["DRAFT","ACTIVE"],"CMD-ADP-UPDATE-MAPPING","=","mapping tests pass; new immutable mapping version","EVT-ADP-MAPPING-UPDATED","MAPPING_TESTS_FAILED"),
  (["DRAFT"],"CMD-ADP-ACTIVATE","ACTIVE","mapping tests pass; approver ≠ author","EVT-ADP-ACTIVATED","SEGREGATION_OF_DUTIES"),
  (["ACTIVE"],"CMD-ADP-SUSPEND","SUSPENDED","reason","EVT-ADP-SUSPENDED","REASON_REQUIRED"),
  (["SUSPENDED"],"CMD-ADP-RESUME","ACTIVE","—","EVT-ADP-RESUMED",None),
  (["DRAFT","ACTIVE","SUSPENDED"],"CMD-ADP-RETIRE","RETIRED","reason","EVT-ADP-RETIRED","REASON_REQUIRED")],
 ["INV-ADP-01: an adapter writes only through BC02 commands, as its service account","INV-ADP-02: mapping versions are immutable and referenced by lineage",
  "INV-ADP-03: an adapter is bound to exactly one Source"],
 ["MappingVersion (spec, tests)"],["REQ-INF-005","REQ-INF-008","REQ-INF-009"])

PERPETUAL = {"AGG-ENTITY":"identity persists for history and as-of queries; RETIRED is reversible (SL-06 exemption, justified)",
             "AGG-REALWORLD-EVENT":"same as Entity","AGG-RELATIONSHIP":"same as Entity; validity lives in the existence claim"}

QUERIES = [
 ("QRY-ENT-RESOLVED","BC02","GET","/api/v1/information/entities/{entity_id}","Resolved view per predicate at valid_at/known_at (value, CORROBORATED/DISPUTED candidates, confidence); resolves through the identity cluster and returns canonical_urn + requested_urn (SLC-04)","any user; claims label-filtered (INV-ENT-02)","REQ-INF-023"),
 ("QRY-ENT-CLAIMS","BC02","GET","/api/v1/information/entities/{entity_id}/claims","Claim history (predicate, valid_at, known_at, include_closed)","any user; label-filtered","REQ-INF-022"),
 ("QRY-ENT-LIST","BC02","GET","/api/v1/information/entities","Entities by type, bbox/polygon of current location, valid_at","any user; allowed_scope pre-filter","REQ-INF-020"),
 ("QRY-ENT-POSITIONS","BC02","GET","/api/v1/information/entities/{entity_id}/positions","Position history in [from,to) as known_at","any user; label-filtered; geometry generalized by obligation","REQ-INF-030"),
 ("QRY-RWE-GET","BC02","GET","/api/v1/information/events/{event_id}","Resolved real-world event","any user; label-filtered","REQ-INF-020"),
 ("QRY-REL-LIST","BC02","GET","/api/v1/information/entities/{entity_id}/relationships","Relationships valid_at/known_at, both directions","any user; hidden relationships and endpoints omitted","REQ-INF-027"),
 ("QRY-CLM-GET","BC02","GET","/api/v1/information/claims/{claim_id}","Claim with sources (per protection), evidence links, supersession chain","any user; label-filtered","REQ-INF-021"),
 ("QRY-OBS-LIST","BC02","GET","/api/v1/information/observations","Observations by bbox, time window (mandatory, ≤ 31 days), source, state","any user; allowed_scope pre-filter","REQ-INF-002"),
 ("QRY-OBS-GET","BC02","GET","/api/v1/information/observations/{observation_id}","Observation with measurements and attachment refs","any user; label-filtered","REQ-INF-002"),
 ("QRY-SRC-GET","BC02","GET","/api/v1/information/sources/{source_id}","Source; identity only with source-protection permission","Analyst and above; protection policy","REQ-INF-001"),
 ("QRY-EVD-GET","BC02","GET","/api/v1/information/evidence/{evidence_id}","Evidence metadata and custody chain","any user; label-filtered","REQ-INF-004"),
 ("QRY-ATT-DOWNLOAD","BC02","POST","/api/v1/information/attachments/{attachment_id}/download-grants","Short-lived signed download target (≤ 5 min); audited","authorized on the owning evidence/observation","REQ-INF-004"),
 ("QRY-LIN-TRACE","BC02","GET","/api/v1/information/lineage/{object_urn}","Upstream/downstream lineage, depth ≤ 10; hidden nodes cut per policy","any user; per-node authorization","REQ-INF-035"),
 ("QRY-EXT-RESOLVE","BC02","GET","/api/v1/information/external-ids/{system}/{external_id}","Object URN mapped at time t (not-found shape if hidden)","adapter service accounts; Analyst","REQ-INF-036"),
 ("QRY-IMP-GET","BC02","GET","/api/v1/information/import-batches/{batch_id}","Batch status, counts, quarantine records (paged)","adapter owner; Administrator","REQ-INF-006"),
 ("QRY-ADP-GET","BC07","GET","/api/v1/integration/adapters/{adapter_id}","Adapter with mapping versions","Administrator","REQ-INF-005"),
]
ACTORS = {"SRC":"Analyst (register, rate, profile) · Security Officer (protection, reclassify)",
 "OBS":"Field User / Operator / Analyst / adapter service account (record) · Analyst (validate, reject)",
 "ENT":"Analyst · adapter service account","RWE":"Analyst · adapter service account","REL":"Analyst · adapter service account",
 "CLM":"Analyst · adapter service account · analysis-run identity (assert) · Analyst or verification re-evaluator system identity (assess) · Analyst (correct, change, retract)",
 "EVD":"Analyst · Field User (register) · custodian role (custody)","EVL":"Analyst","ATT":"user with write permission on the target object",
 "IMP":"adapter service account · Administrator","EXT":"adapter service account · Analyst","ADP":"Administrator (register, update) · second Administrator (activate)"}
P = {
 "CMD-SRC-REGISTER":"type!:string name!:LocalizedName owner_org!:urn reliability!:enum(A,B,C,D,E,F) valid_from!:date-time protection_level:integer label!:Label",
 "CMD-SRC-RATE-RELIABILITY":"reliability!:enum(A,B,C,D,E,F) valid_from!:date-time rationale!:string","CMD-SRC-UPDATE-PROFILE":"name:LocalizedName contact:object",
 "CMD-SRC-SET-PROTECTION":"protection_level!:integer second_approver:urn","CMD-SRC-RECLASSIFY":"label!:Label reason!:string",
 "CMD-SRC-SUSPEND":"reason!:string","CMD-SRC-REINSTATE":"","CMD-SRC-RETIRE":"reason!:string",
 "CMD-OBS-RECORD":"client_id:string source!:urn observer!:urn observed_at!:date-time event_time:FuzzyInterval location!:SpatialEnvelope method!:string measurements:array narrative:LocalizedName attachments:array label!:Label field_session:urn device:urn",
 "CMD-OBS-AMEND":"changes!:object reason!:string","CMD-OBS-ATTACH-EVIDENCE":"evidence!:urn","CMD-OBS-RECLASSIFY":"label!:Label reason!:string",
 "CMD-OBS-VALIDATE":"note:string","CMD-OBS-REJECT":"reason!:string",
 "CMD-ENT-REGISTER":"entity_type!:string label!:Label initial_claims:array external_ids:array","CMD-ENT-CHANGE-TYPE":"entity_type!:string reason!:string",
 "CMD-ENT-RECLASSIFY":"label!:Label reason!:string","CMD-ENT-RETIRE":"reason!:string","CMD-ENT-REINSTATE":"reason!:string",
 "CMD-RWE-REGISTER":"event_type!:string label!:Label initial_claims!:array","CMD-RWE-CHANGE-TYPE":"event_type!:string reason!:string",
 "CMD-RWE-RECLASSIFY":"label!:Label reason!:string","CMD-RWE-RETIRE":"reason!:string","CMD-RWE-REINSTATE":"reason!:string",
 "CMD-REL-REGISTER":"relationship_type!:string source_ref!:urn target_ref!:urn valid!:Interval source_refs!:array label!:Label",
 "CMD-REL-RECLASSIFY":"label!:Label reason!:string","CMD-REL-RETIRE":"reason!:string","CMD-REL-REINSTATE":"reason!:string",
 "CMD-CLM-ASSERT":"subject!:urn predicate!:string value!:ClaimValue valid!:Interval source_refs!:array derived_from:array confidence!:Confidence label!:Label",
 "CMD-CLM-CORRECT":"value!:ClaimValue valid:Interval source_refs!:array confidence!:Confidence reason!:string",
 "CMD-CLM-RECORD-CHANGE":"t_change!:date-time new_value!:ClaimValue source_refs!:array confidence!:Confidence",
 "CMD-CLM-RETRACT":"reason!:string","CMD-CLM-ASSESS":"information_confidence:enum(1,2,3,4,5,6) verification_status:enum(UNVERIFIED,PARTIALLY_VERIFIED,VERIFIED,DISPUTED,REFUTED) rationale!:string",
 "CMD-CLM-RECLASSIFY":"label!:Label reason!:string",
 "CMD-EVD-REGISTER":"client_id:string evidence_type!:string attachment:urn observation_ref:urn locator:object source!:urn collected_at!:date-time label!:Label",
 "CMD-EVD-UPDATE-LOCATOR":"locator!:object","CMD-EVD-SEAL":"","CMD-EVD-TRANSFER-CUSTODY":"new_holder!:urn action!:string",
 "CMD-EVD-RECLASSIFY":"label!:Label reason!:string","CMD-EVD-WITHDRAW":"reason!:string",
 "CMD-EVL-LINK":"evidence!:urn claim!:urn stance!:enum(SUPPORTS,REFUTES,CONTEXT) note:string","CMD-EVL-UNLINK":"reason!:string",
 "CMD-ATT-INITIATE-UPLOAD":"client_id:string sha256!:string size_bytes!:integer mime_type!:string file_name:string label!:Label","CMD-ATT-COMPLETE-UPLOAD":"",
 "CMD-ATT-ERASE":"erasure_order_ref!:string",
 "CMD-IMP-SUBMIT":"adapter!:urn batch_key!:string content_sha256!:string format!:string payload_attachment!:urn",
 "CMD-IMP-REPROCESS-QUARANTINE":"mapping_version:string corrections:array","CMD-IMP-ACCEPT-QUARANTINE":"reason!:string","CMD-IMP-CANCEL":"reason!:string",
 "CMD-EXT-MAP":"system!:string external_id!:string object!:urn valid_from!:date-time","CMD-EXT-END":"valid_to!:date-time reason!:string",
 "CMD-ADP-REGISTER":"name!:string source!:urn service_account!:urn mapping!:object","CMD-ADP-UPDATE-MAPPING":"mapping!:object tests!:array",
 "CMD-ADP-ACTIVATE":"","CMD-ADP-SUSPEND":"reason!:string","CMD-ADP-RESUME":"","CMD-ADP-RETIRE":"reason!:string",
}
SYSTEM_CMDS = set()
RESOURCE = {"AGG-SOURCE":("information","sources"),"AGG-OBSERVATION":("information","observations"),"AGG-ENTITY":("information","entities"),
 "AGG-REALWORLD-EVENT":("information","events"),"AGG-RELATIONSHIP":("information","relationships"),"AGG-CLAIM":("information","claims"),
 "AGG-EVIDENCE":("information","evidence"),"AGG-EVIDENCE-LINK":("information","evidence-links"),"AGG-ATTACHMENT":("information","attachments"),
 "AGG-IMPORT-BATCH":("information","import-batches"),"AGG-EXTERNAL-ID":("information","external-ids"),"AGG-ADAPTER":("integration","adapters")}
SECURITY_AFFECTING = {"EVT-SRC-RECLASSIFIED","EVT-OBS-RECLASSIFIED","EVT-ENT-RECLASSIFIED","EVT-RWE-RECLASSIFIED","EVT-REL-RECLASSIFIED",
 "EVT-CLM-RECLASSIFIED","EVT-EVD-RECLASSIFIED","EVT-SRC-PROTECTION-CHANGED","EVT-ATT-ERASED"}
CONSUMERS = {
 "AGG-CLAIM":["Current-view maintainer (async materialized resolved views)","Conflict detector (SLC-04)","Situation membership (SLC-06)","Search/Graph projections (SLC-05)"],
 "AGG-OBSERVATION":["Derived-claim processor (position summarization)","Situation membership (SLC-06)","Search projection (SLC-05)"],
 "AGG-ATTACHMENT":["Content scanner","Evidence registrar"],"AGG-IMPORT-BATCH":["Import worker","Adapter owner notification"],
 "AGG-EXTERNAL-ID":["Import worker cache"],
 "AGG-EVIDENCE":["Verification re-evaluator (on WITHDRAWN: issues CMD-CLM-ASSESS as system identity for linked claims, recomputing verification from remaining SUPPORTS links)","Search projection (SLC-05)"],"AGG-ADAPTER":["Import worker"],
 "AGG-ENTITY":["ER candidate generator (SLC-04)","Search/Graph projections (SLC-05)"],
 "default":["Search/Graph projections (SLC-05)"],
}
```

## slc03_data.py

```python
# -*- coding: utf-8 -*-
# SLC-03 — Task lifecycle (+ task types, qualification records & eligibility for R1)
SLICE = "SLC-03"
AGGS = {}
def agg(id_, bc, name, tier, purpose, states, terminal, transitions, invariants, entities, reqs, notes=None, personal=False):
    AGGS[id_] = dict(id=id_, bc=bc, name=name, tier=tier, purpose=purpose, states=states, terminal=terminal,
                     transitions=transitions, invariants=invariants, entities=entities, requirements=reqs, notes=notes, personal_data=personal)

NT_TASK = ["DRAFT","READY","ASSIGNED","ACCEPTED","IN_PROGRESS","BLOCKED","SUBMITTED","UNDER_REVIEW","APPROVED","COMPLETED"]
BEFORE_DONE = [s for s in NT_TASK if s not in ("APPROVED","COMPLETED")]
agg("AGG-TASK","BC04","Task","T2","وحدة عمل قابلة للإسناد والتنفيذ والمراجعة والقياس",
 NT_TASK+["CLOSED","CANCELLED","REJECTED","EXPIRED","SUPERSEDED"],["CLOSED","CANCELLED","REJECTED","EXPIRED","SUPERSEDED"],
 [("∅","CMD-TASK-CREATE","DRAFT","task type ACTIVE (version pinned); plan_ref (operations, collection or contingency plan — CR-59, CR-61) or incident_ref (direct response task under an Incident, SLC-17 — CR-61), or ad_hoc_reason + accountable owner (REQ-OPS-010); label ≤ creator clearance","EVT-TASK-CREATED","TASK_INVALID"),
  (["DRAFT","READY"],"CMD-TASK-EDIT","=","creator or Planner; completion criteria editable only in DRAFT/READY; new version","EVT-TASK-EDITED","TASK_INVALID"),
  (["DRAFT"],"CMD-TASK-MARK-READY","READY","title, ≥ 1 completion criterion, owner; dependencies reference existing tasks without cycle","EVT-TASK-READIED","TASK_NOT_READY"),
  (["READY"],"CMD-TASK-ASSIGN","ASSIGNED","assignee ACTIVE user; assignee clearance ≥ task label; EligibilityCheck(assignee, task type, now) ∈ {ELIGIBLE, CONDITIONALLY_ELIGIBLE with condition met} (REQ-OPS-007); actor authorized in scope","EVT-TASK-ASSIGNED","ASSIGNEE_NOT_ELIGIBLE"),
  (["ASSIGNED","ACCEPTED","IN_PROGRESS","BLOCKED"],"CMD-TASK-REASSIGN","ASSIGNED","same checks as assign for the new assignee; reason; previous assignee notified","EVT-TASK-REASSIGNED","ASSIGNEE_NOT_ELIGIBLE"),
  (["ASSIGNED"],"CMD-TASK-ACCEPT","ACCEPTED","actor = assignee","EVT-TASK-ACCEPTED","NOT_ASSIGNEE"),
  (["ASSIGNED"],"CMD-TASK-DECLINE","READY","actor = assignee; reason","EVT-TASK-DECLINED","REASON_REQUIRED"),
  (["ACCEPTED"],"CMD-TASK-START","IN_PROGRESS","actor = assignee; all predecessor tasks COMPLETED or CLOSED","EVT-TASK-STARTED","DEPENDENCIES_NOT_MET"),
  (["IN_PROGRESS"],"CMD-TASK-BLOCK","BLOCKED","actor = assignee; blocking reason","EVT-TASK-BLOCKED","REASON_REQUIRED"),
  (["BLOCKED"],"CMD-TASK-RESUME","IN_PROGRESS","actor = assignee; resolution note","EVT-TASK-RESUMED","REASON_REQUIRED"),
  (["IN_PROGRESS","BLOCKED"],"CMD-TASK-ADD-RESULT-ITEM","=","actor = assignee; item = note | evidence URN | observation URN | measurement","EVT-TASK-RESULT-ITEM-ADDED","RESULT_ITEM_INVALID"),
  (["IN_PROGRESS"],"CMD-TASK-SUBMIT","SUBMITTED","actor = assignee; result has ≥ 1 item","EVT-TASK-SUBMITTED","RESULT_REQUIRED"),
  (["SUBMITTED"],"CMD-TASK-START-REVIEW","UNDER_REVIEW","actor has review permission in scope; actor ≠ assignee","EVT-TASK-REVIEW-STARTED","SEGREGATION_OF_DUTIES"),
  (["UNDER_REVIEW"],"CMD-TASK-RETURN","IN_PROGRESS","reviewer; rework reason","EVT-TASK-RETURNED-FOR-REWORK","REASON_REQUIRED"),
  (["UNDER_REVIEW"],"CMD-TASK-APPROVE","APPROVED","reviewer ≠ assignee unless tenant policy disables SoD (REQ-OPS-009)","EVT-TASK-APPROVED","SEGREGATION_OF_DUTIES"),
  (["UNDER_REVIEW"],"CMD-TASK-REJECT","REJECTED","reviewer; reason; follow-up task may be created linked by follow_up_of (OQ-033)","EVT-TASK-REJECTED","REASON_REQUIRED"),
  (["APPROVED"],"SYS:all completion criteria satisfied","COMPLETED","system-checkable criteria evaluated at approval and whenever result evidence changes (BRL-006)","EVT-TASK-COMPLETED",None),
  (["APPROVED"],"CMD-TASK-COMPLETE","COMPLETED","attestation-type criteria confirmed by an authorized actor; all criteria satisfied (BRL-006)","EVT-TASK-COMPLETED","TASK_CRITERIA_NOT_MET"),
  (["COMPLETED"],"CMD-TASK-CLOSE","CLOSED","no open follow-up tasks","EVT-TASK-CLOSED","OPEN_FOLLOW_UPS"),
  (["COMPLETED"],"SYS:follow-up window (7 d) elapsed without open follow-ups","CLOSED","scheduler","EVT-TASK-CLOSED",None),
  (BEFORE_DONE+["APPROVED"],"CMD-TASK-CANCEL","CANCELLED","actor has cancel authority in scope; reason","EVT-TASK-CANCELLED","REASON_REQUIRED"),
  (BEFORE_DONE,"SYS:due passed and task type expires_on_due","EXPIRED","scheduler; only when the task type declares expires_on_due = true (OQ-032)","EVT-TASK-EXPIRED",None),
  (BEFORE_DONE+["APPROVED"],"SYS:plan version baselined without this task","SUPERSEDED","SLC-08 trigger","EVT-TASK-SUPERSEDED",None),
  ("*NT","CMD-TASK-ESCALATE","=","reason; notifies next authority level (REQ-OPS-012)","EVT-TASK-ESCALATED","REASON_REQUIRED"),
  ("*NT","SYS:due passed (escalation policy)","=","scheduler; at due and at due + grace from task type","EVT-TASK-ESCALATED",None),
  (["DRAFT","READY","ASSIGNED","ACCEPTED","IN_PROGRESS","BLOCKED"],"CMD-TASK-SET-DUE","=","Planner or owner; reason","EVT-TASK-DUE-CHANGED","REASON_REQUIRED"),
  ("*NT","CMD-TASK-SUSPEND","=","suspend authority; reason; sets suspended = true","EVT-TASK-SUSPENDED","REASON_REQUIRED"),
  ("*NT","CMD-TASK-UNSUSPEND","=","suspend authority; suspended = true","EVT-TASK-UNSUSPENDED","NOT_SUSPENDED"),
  ("*NT","CMD-TASK-RECLASSIFY","=","authority per tenant policy; assignee clearance ≥ new label, else reassignment required first","EVT-TASK-RECLASSIFIED","CLASSIFICATION_CHANGE_NOT_AUTHORIZED")],
 ["INV-TASK-01: no transition from COMPLETED or any terminal state to IN_PROGRESS",
  "INV-TASK-02: COMPLETED only when every completion criterion is satisfied (BRL-006)",
  "INV-TASK-03: every accepted command produces exactly one event and one audit record",
  "INV-TASK-04: terminal states accept no state-changing command",
  "INV-TASK-05: from ASSIGNED onwards the assignee was eligible and cleared at assignment time (recorded with the eligibility result)",
  "INV-TASK-06: while suspended = true, every state-changing command except UNSUSPEND and CANCEL is rejected with TASK_SUSPENDED (orthogonal flag, not a state)",
  "INV-TASK-07: approver ≠ assignee under default policy (REQ-OPS-009)",
  "INV-TASK-08: the dependency graph is acyclic",
  "INV-TASK-09: completion criteria are frozen from ASSIGNED onwards"],
 ["CompletionCriterion (kind: attestation | result_item | evidence_count ≥ n | measurement_recorded | checklist)","ResultItem","Dependency (predecessor URN)","EligibilitySnapshot"],
 ["REQ-OPS-006","REQ-OPS-007","REQ-OPS-008","REQ-OPS-009","REQ-OPS-010","REQ-OPS-011","REQ-OPS-012","REQ-OFF-001"],
 "SUSPENDED from V6§13.5 is modelled as an orthogonal flag (INV-TASK-06): resuming returns to the same state without storing a 'prior_state' (CR-46).")

agg("AGG-TASK-TYPE","BC04","Task Type","T2","قالب نوع مهمة: متطلبات الأهلية، معايير الإكمال، التصعيد، الانتهاء",
 ["DRAFT","ACTIVE","RETIRED"],["RETIRED"],
 [("∅","CMD-TTY-DEFINE","DRAFT","code unique in tenant","EVT-TTY-DEFINED","TASK_TYPE_CODE_TAKEN"),
  (["DRAFT","ACTIVE"],"CMD-TTY-EDIT","=","required qualifications exist in RD-COMPETENCIES; criteria templates valid; ACTIVE → new version (existing tasks keep their pinned version)","EVT-TTY-EDITED","TASK_TYPE_INVALID"),
  (["DRAFT"],"CMD-TTY-ACTIVATE","ACTIVE","≥ 1 completion criterion template","EVT-TTY-ACTIVATED","TASK_TYPE_INVALID"),
  (["ACTIVE"],"CMD-TTY-RETIRE","RETIRED","reason; existing tasks unaffected","EVT-TTY-RETIRED","REASON_REQUIRED")],
 ["INV-TTY-01: tasks pin the task-type version at creation","INV-TTY-02: expires_on_due defaults to false; escalation defaults: at due and due + 24 h",
  "INV-TTY-03: offline-capable commands are limited to ACCEPT, START, BLOCK, RESUME, ADD-RESULT-ITEM, SUBMIT"],
 ["QualificationRequirement (code, min_level, supervision_allowed)","CriterionTemplate","EscalationPolicy"],["REQ-OPS-007","REQ-OPS-014"])

agg("AGG-QUALIFICATION-RECORD","BC05","Qualification Record","T2","كفاءة أو تأهيل أو شهادة لشخص بفترة صلاحية",
 ["ACTIVE","SUSPENDED","EXPIRED","REVOKED"],["EXPIRED","REVOKED"],
 [("∅","CMD-QUAL-RECORD","ACTIVE","person ACTIVE; code in RD-COMPETENCIES; level valid; valid_from < valid_to; issuer; evidence ref optional","EVT-QUAL-RECORDED","QUALIFICATION_INVALID"),
  (["ACTIVE"],"CMD-QUAL-RENEW","=","new valid_to > old; evidence; new version","EVT-QUAL-RENEWED","QUALIFICATION_INVALID"),
  (["ACTIVE"],"CMD-QUAL-SUSPEND","SUSPENDED","reason","EVT-QUAL-SUSPENDED","REASON_REQUIRED"),
  (["SUSPENDED"],"CMD-QUAL-REINSTATE","ACTIVE","validity not ended","EVT-QUAL-REINSTATED","QUALIFICATION_EXPIRED"),
  (["ACTIVE","SUSPENDED"],"CMD-QUAL-REVOKE","REVOKED","reason","EVT-QUAL-REVOKED","REASON_REQUIRED"),
  (["ACTIVE","SUSPENDED"],"SYS:valid_to reached","EXPIRED","scheduler (eligibility also checks validity at read time)","EVT-QUAL-EXPIRED",None)],
 ["INV-QUAL-01: eligibility evaluates validity at the requested time even if the EXPIRED transition is late","INV-QUAL-02: records are never deleted; history supports as-of eligibility"],
 [],["REQ-RDY-001","REQ-RDY-002"],personal=True)

PERPETUAL = {}
EXTRA_ERRORS = {"AGG-TASK": ["TASK_SUSPENDED"]}
OFFLINE = {"CMD-TASK-ACCEPT","CMD-TASK-START","CMD-TASK-BLOCK","CMD-TASK-RESUME","CMD-TASK-ADD-RESULT-ITEM","CMD-TASK-SUBMIT"}

QUERIES = [
 ("QRY-TASK-GET","BC04","GET","/api/v1/operations/tasks/{task_id}","Task with criteria status, result, eligibility snapshot, dependencies","assignee, reviewer, Planner/Manager in scope; label rule","REQ-OPS-006"),
 ("QRY-TASK-LIST","BC04","GET","/api/v1/operations/tasks","Tasks by assignee (me), plan, state, due_before, unit","allowed_scope pre-filter","REQ-OPS-006"),
 ("QRY-TASK-HISTORY","BC04","GET","/api/v1/operations/tasks/{task_id}/history","State history; state as of t (RECONSTRUCTED)","same as QRY-TASK-GET","REQ-OPS-006"),
 ("QRY-TTY-GET","BC04","GET","/api/v1/operations/task-types/{task_type_id}","Task type version","any user of tenant","REQ-OPS-014"),
 ("QRY-QUAL-LIST","BC05","GET","/api/v1/readiness/persons/{person_id}/qualifications","Qualification records as of t","Manager/Resource Manager in scope; self","REQ-RDY-001"),
 ("QRY-ELIG-CHECK","BC05","POST","/api/v1/readiness/eligibility-checks","EligibilityCheck(person, task_type version, at) → status + reasons","Planner/Manager in scope; internal BC04 (workload identity)","REQ-RDY-002"),
]
ACTORS = {"TASK":"Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) · assignee (accept, decline, start, block, resume, add result, submit) · reviewer (review, return, approve, reject, complete)",
          "TTY":"Administrator / Planner lead","QUAL":"Resource Manager / Training Manager"}
P = {
 "CMD-TASK-CREATE":"task_type!:urn title!:LocalizedName description:LocalizedName plan_ref:urn incident_ref:urn ad_hoc_reason:string owner!:urn org_scope!:urn due_at:date-time dependencies:array follow_up_of:urn label!:Label",
 "CMD-TASK-EDIT":"title:LocalizedName description:LocalizedName criteria:array dependencies:array","CMD-TASK-MARK-READY":"",
 "CMD-TASK-ASSIGN":"assignee!:urn note:string","CMD-TASK-REASSIGN":"assignee!:urn reason!:string","CMD-TASK-ACCEPT":"","CMD-TASK-DECLINE":"reason!:string",
 "CMD-TASK-START":"","CMD-TASK-BLOCK":"reason!:string","CMD-TASK-RESUME":"note!:string","CMD-TASK-ADD-RESULT-ITEM":"kind!:enum(note,evidence,observation,measurement) ref:urn note:LocalizedName measurement:object",
 "CMD-TASK-SUBMIT":"summary!:LocalizedName","CMD-TASK-START-REVIEW":"","CMD-TASK-RETURN":"reason!:string","CMD-TASK-APPROVE":"note:string","CMD-TASK-REJECT":"reason!:string create_follow_up!:boolean",
 "CMD-TASK-COMPLETE":"attestations!:array","CMD-TASK-CLOSE":"note:string","CMD-TASK-CANCEL":"reason!:string","CMD-TASK-ESCALATE":"reason!:string",
 "CMD-TASK-SET-DUE":"due_at!:date-time reason!:string","CMD-TASK-SUSPEND":"reason!:string","CMD-TASK-UNSUSPEND":"reason!:string","CMD-TASK-RECLASSIFY":"label!:Label reason!:string",
 "CMD-TTY-DEFINE":"code!:string name!:LocalizedName","CMD-TTY-EDIT":"qualification_requirements!:array criteria_templates!:array escalation!:object expires_on_due!:boolean review_steps:integer",
 "CMD-TTY-ACTIVATE":"","CMD-TTY-RETIRE":"reason!:string",
 "CMD-QUAL-RECORD":"person!:urn kind!:enum(competency,qualification,certification) code!:string level!:integer valid_from!:date-time valid_to!:date-time issuer!:string evidence:urn",
 "CMD-QUAL-RENEW":"valid_to!:date-time evidence:urn","CMD-QUAL-SUSPEND":"reason!:string","CMD-QUAL-REINSTATE":"","CMD-QUAL-REVOKE":"reason!:string",
}
SYSTEM_CMDS = set()
RESOURCE = {"AGG-TASK":("operations","tasks"),"AGG-TASK-TYPE":("operations","task-types"),"AGG-QUALIFICATION-RECORD":("readiness","qualification-records")}
SECURITY_AFFECTING = {"EVT-TASK-RECLASSIFIED"}
CONSUMERS = {
 "AGG-TASK":["Notification service (SLC-06)","Plan progress (SLC-08)","Outcome measurement (SLC-08)","Search projection (SLC-05)","Resources release (SLC-09, R2)"],
 "AGG-TASK-TYPE":["Task command handler cache"],"AGG-QUALIFICATION-RECORD":["Eligibility cache invalidation","Task assignment re-check report"],
 "default":["Search projection (SLC-05)"],
}
```

## slc04_data.py

```python
# -*- coding: utf-8 -*-
# SLC-04 — Conflict Management + Entity Resolution (merge / split via same-as links)
SLICE = "SLC-04"
AGGS = {}
def agg(id_, bc, name, tier, purpose, states, terminal, transitions, invariants, entities, reqs, notes=None, personal=False):
    AGGS[id_] = dict(id=id_, bc=bc, name=name, tier=tier, purpose=purpose, states=states, terminal=terminal,
                     transitions=transitions, invariants=invariants, entities=entities, requirements=reqs, notes=notes, personal_data=personal)

agg("AGG-CONFLICT","BC02","Conflict","T2 (bitemporal resolution records)","تعارض بين ادعاءين أو أكثر حول نفس الموضوع والسمة في فترة متداخلة",
 ["OPEN","UNDER_REVIEW","RESOLVED","ACCEPTED_AS_CONFLICT","SUPERSEDED"],["SUPERSEDED"],
 [("∅","SYS:conflict rule matched","OPEN","rule CF-01..CF-04 on claims of the same identity cluster, same predicate, overlapping valid; no non-terminal conflict with the same (cluster, predicate, window) — otherwise the claim joins it","EVT-CNF-DETECTED",None),
  ("∅","CMD-CNF-RAISE","OPEN","analyst names ≥ 2 visible CURRENT claims on the same cluster and predicate with overlapping valid time","EVT-CNF-RAISED","CONFLICT_INVALID"),
  (["OPEN","UNDER_REVIEW"],"SYS:incompatible claim joined","=","new CURRENT claim incompatible with members (same key, overlapping window)","EVT-CNF-CLAIM-ADDED",None),
  (["OPEN","UNDER_REVIEW"],"CMD-CNF-ASSIGN","=","reviewer cleared for every member claim label","EVT-CNF-ASSIGNED","REVIEWER_NOT_CLEARED"),
  (["OPEN"],"CMD-CNF-START-REVIEW","UNDER_REVIEW","actor = assigned reviewer (or Analyst lead)","EVT-CNF-REVIEW-STARTED","NOT_ASSIGNED_REVIEWER"),
  (["UNDER_REVIEW"],"CMD-CNF-RESOLVE","RESOLVED","preferred claim ∈ CURRENT members; rationale; reviewer ≠ asserter of the preferred claim (SoD, default on); records resolution with recorded_from = now","EVT-CNF-RESOLVED","SEGREGATION_OF_DUTIES"),
  (["UNDER_REVIEW"],"CMD-CNF-ACCEPT","ACCEPTED_AS_CONFLICT","rationale (both accounts shown to users)","EVT-CNF-ACCEPTED","REASON_REQUIRED"),
  (["RESOLVED","ACCEPTED_AS_CONFLICT"],"CMD-CNF-REOPEN","UNDER_REVIEW","new evidence or reason; closes current resolution record (recorded_to = now)","EVT-CNF-REOPENED","REASON_REQUIRED"),
  (["OPEN","UNDER_REVIEW","RESOLVED","ACCEPTED_AS_CONFLICT"],"SYS:member set no longer conflicting","SUPERSEDED","fewer than 2 incompatible CURRENT members (claims closed, split, or corrected)","EVT-CNF-SUPERSEDED",None)],
 ["INV-CNF-01: a conflict never modifies, closes or re-labels any claim",
  "INV-CNF-02: at most one non-terminal conflict per (tenant, identity cluster, predicate, overlapping valid window)",
  "INV-CNF-03: resolutions are bitemporal records: resolve(T, K) uses the resolution known at K",
  "INV-CNF-04: label = max(member claim labels); a reader sees the conflict only if the reader sees ≥ 2 incompatible member claims (A21)",
  "INV-CNF-05: the preferred claim of a RESOLVED conflict is CURRENT; if it closes, the conflict is re-evaluated (SUPERSEDED or back to OPEN via detection)"],
 ["ResolutionRecord (preferred_claim, rationale, decided_by, recorded_from, recorded_to)","MemberClaim (claim_ref, joined_at)"],
 ["REQ-INF-025","REQ-INF-024"],
 "Detection runs on EVT-CLM-ASSERTED/CORRECTED/CHANGED and on identity-cluster changes (a merge can reveal conflicts between members' claims).")

agg("AGG-ER-CASE","BC02","Entity Resolution Case","T2","حالة مطابقة بين كيانين؛ قرارها ينشئ أو يغلق روابط التطابق",
 ["CANDIDATE","UNDER_REVIEW","MATCHED","POSSIBLE_DUPLICATE","SPLIT_REQUIRED","NOT_A_MATCH","SPLIT","WITHDRAWN"],["NOT_A_MATCH","SPLIT","WITHDRAWN"],
 [("∅","SYS:candidate generator score ≥ propose threshold","CANDIDATE","pair not already in the same cluster; no NOT_A_MATCH link between their clusters; no non-terminal case for the pair","EVT-ER-PROPOSED",None),
  ("∅","CMD-ER-PROPOSE","CANDIDATE","same conditions; proposer is Analyst or AI suggestion (AIL1, agent recorded)","EVT-ER-PROPOSED","ER_PAIR_INVALID"),
  (["CANDIDATE"],"CMD-ER-START-REVIEW","UNDER_REVIEW","reviewer cleared for both entity labels","EVT-ER-REVIEW-STARTED","REVIEWER_NOT_CLEARED"),
  (["UNDER_REVIEW"],"CMD-ER-DECIDE-MATCH","MATCHED","types compatible; neither entity RETIRED; merged cluster contains no NOT_A_MATCH pair; merged cluster size ≤ 50 or second reviewer; reviewer ≠ human proposer; creates MATCH link and recomputes cluster in the same transaction","EVT-ER-MATCHED","MATCH_CONTRADICTS_NOT_A_MATCH"),
  (["UNDER_REVIEW"],"CMD-ER-DECIDE-NOT-MATCH","NOT_A_MATCH","rationale; creates NOT_A_MATCH link (blocks re-proposal)","EVT-ER-NOT-MATCHED","REASON_REQUIRED"),
  (["UNDER_REVIEW"],"CMD-ER-PARK","POSSIBLE_DUPLICATE","rationale; insufficient evidence","EVT-ER-PARKED","REASON_REQUIRED"),
  (["POSSIBLE_DUPLICATE"],"CMD-ER-RESUME","UNDER_REVIEW","new evidence or reason","EVT-ER-RESUMED","REASON_REQUIRED"),
  (["POSSIBLE_DUPLICATE"],"CMD-ER-DECIDE-NOT-MATCH","NOT_A_MATCH","rationale","EVT-ER-NOT-MATCHED","REASON_REQUIRED"),
  (["MATCHED"],"CMD-ER-REQUEST-SPLIT","SPLIT_REQUIRED","reason + evidence; requester cleared for both entities","EVT-ER-SPLIT-REQUESTED","REASON_REQUIRED"),
  (["SPLIT_REQUIRED"],"CMD-ER-CONFIRM-MATCH","MATCHED","reviewer ≠ split requester; rationale","EVT-ER-MATCH-CONFIRMED","SEGREGATION_OF_DUTIES"),
  (["SPLIT_REQUIRED"],"CMD-ER-SPLIT","SPLIT","reviewer ≠ split requester; closes MATCH link (recorded_to = now); optional NOT_A_MATCH link; recomputes clusters in the same transaction","EVT-ER-SPLIT","SEGREGATION_OF_DUTIES"),
  (["CANDIDATE","UNDER_REVIEW","POSSIBLE_DUPLICATE"],"CMD-ER-WITHDRAW","WITHDRAWN","reason (e.g. entity retired, duplicate case)","EVT-ER-WITHDRAWN","REASON_REQUIRED")],
 ["INV-ER-01: claims are never moved or rewritten by merge or split (ER-MODEL §2)",
  "INV-ER-02: identity clusters are connected components of CURRENT MATCH links as known at K; canonical id = smallest ULID in the cluster",
  "INV-ER-03: no cluster may contain two entities joined by a CURRENT NOT_A_MATCH link",
  "INV-ER-04: no automatic merge: MATCHED requires a human decision (W1 Q26, AI-OP-06)",
  "INV-ER-05: a cluster > 50 members requires a second reviewer",
  "INV-ER-06: the decision records decision_basis_level = max label the reviewer could see; a higher-cleared reviewer may request a split"],
 ["SameAsLink (left, right, kind MATCH | NOT_A_MATCH, recorded_from, recorded_to)","FeatureComparison (per feature: values, similarity, weight)"],
 ["REQ-INF-032","REQ-INF-033","REQ-INF-034"],
 "Pairwise cases; clusters form transitively. Cluster table is bitemporal (record time) and maintained in the decision transaction (components ≤ 50 → cheap).")

agg("AGG-MATCH-RULESET","BC02","Match Ruleset","T2","قواعد توليد المرشحين (الحجب والسمات والأوزان والعتبات) لكل نوع كيان",
 ["DRAFT","ACTIVE","SUPERSEDED"],["SUPERSEDED"],
 [("∅","CMD-MRS-DRAFT","DRAFT","entity type exists","EVT-MRS-DRAFTED",None),
  (["DRAFT"],"CMD-MRS-EDIT","=","blocking keys, features, weights, thresholds valid; evaluation run on labelled test set attached","EVT-MRS-EDITED","RULESET_INVALID"),
  (["DRAFT"],"CMD-MRS-ACTIVATE","ACTIVE","evaluation meets QAS-ER-001 (candidate recall ≥ 95 %) and QAS-ER-002; approver ≠ author; previous ACTIVE → SUPERSEDED","EVT-MRS-ACTIVATED","RULESET_BELOW_TARGET"),
  (["ACTIVE"],"SYS:successor activated","SUPERSEDED","system","EVT-MRS-SUPERSEDED",None)],
 ["INV-MRS-01: exactly one ACTIVE ruleset per (tenant, entity type)","INV-MRS-02: every proposal records the ruleset version (lineage)",
  "INV-MRS-03: a ruleset cannot be activated without a passing evaluation on a labelled Arabic/English test set"],
 ["BlockingKey","Feature (name forms, phonetic key, dates, geohash, identifiers)","Thresholds (propose)"],["REQ-INF-032","REQ-SRC-003"])

PERPETUAL = {}
QUERIES = [
 ("QRY-CNF-LIST","BC02","GET","/api/v1/information/conflicts","Conflicts by subject, predicate, state, assignee","Analyst; only conflicts with ≥ 2 visible member claims","REQ-INF-025"),
 ("QRY-CNF-GET","BC02","GET","/api/v1/information/conflicts/{conflict_id}","Conflict with visible members, evidence, resolution history (as known_at)","Analyst; visibility rule INV-CNF-04","REQ-INF-025"),
 ("QRY-ER-QUEUE","BC02","GET","/api/v1/information/er-cases","Review queue by state, entity type, score, ruleset","Analyst; cases where both entities are visible","REQ-INF-032"),
 ("QRY-ER-GET","BC02","GET","/api/v1/information/er-cases/{case_id}","Case with side-by-side feature comparison (visible claims only)","Analyst; both entities visible","REQ-INF-032"),
 ("QRY-CLUSTER-GET","BC02","GET","/api/v1/information/entities/{entity_id}/identity-cluster","Cluster members, canonical URN, links, as known_at","Analyst; invisible members omitted","REQ-INF-033"),
 ("QRY-MRS-GET","BC02","GET","/api/v1/information/match-rulesets/{ruleset_id}","Ruleset with evaluation report","Analyst lead, Administrator","REQ-INF-032"),
]
ACTORS = {"CNF":"Analyst (raise, review, resolve, accept, reopen) · Analyst lead (assign)","ER":"Analyst (propose, review, decide, request split) · second Analyst (confirm/split, large clusters)",
          "MRS":"Analyst lead (draft, edit) · Administrator ≠ author (activate)"}
P = {
 "CMD-CNF-RAISE":"claims!:array predicate!:string note:string","CMD-CNF-ASSIGN":"reviewer!:urn","CMD-CNF-START-REVIEW":"",
 "CMD-CNF-RESOLVE":"preferred_claim!:urn rationale!:string evidence:array","CMD-CNF-ACCEPT":"rationale!:string","CMD-CNF-REOPEN":"reason!:string evidence:array",
 "CMD-ER-PROPOSE":"left!:urn right!:urn rationale!:string agent:urn","CMD-ER-START-REVIEW":"","CMD-ER-DECIDE-MATCH":"rationale!:string second_reviewer:urn",
 "CMD-ER-DECIDE-NOT-MATCH":"rationale!:string","CMD-ER-PARK":"rationale!:string","CMD-ER-RESUME":"reason!:string",
 "CMD-ER-REQUEST-SPLIT":"reason!:string evidence:array","CMD-ER-CONFIRM-MATCH":"rationale!:string","CMD-ER-SPLIT":"rationale!:string record_not_a_match!:boolean",
 "CMD-ER-WITHDRAW":"reason!:string",
 "CMD-MRS-DRAFT":"entity_type!:string based_on:urn","CMD-MRS-EDIT":"blocking_keys!:array features!:array thresholds!:object evaluation_attachment!:urn","CMD-MRS-ACTIVATE":"",
}
SYSTEM_CMDS = set()
RESOURCE = {"AGG-CONFLICT":("information","conflicts"),"AGG-ER-CASE":("information","er-cases"),"AGG-MATCH-RULESET":("information","match-rulesets")}
SECURITY_AFFECTING = set()
CONSUMERS = {
 "AGG-CONFLICT":["Resolved-view materializer (SLC-05)","Analyst notifications","Situation membership (SLC-06: DISPUTED markers)"],
 "AGG-ER-CASE":["Cluster maintainer (same transaction) → EVT cluster changed","Conflict detector (re-run on cluster change)","Search/Graph projections (canonical ids)","Situation membership (SLC-06)"],
 "AGG-MATCH-RULESET":["Candidate generator (reloads ruleset)"],
 "default":["Search/Graph projections (SLC-05)"],
}
```

## slc05_data.py

```python
# -*- coding: utf-8 -*-
# SLC-05 — Secured Search & Graph Projections (discovery)
SLICE = "SLC-05"
AGGS = {}
def agg(id_, bc, name, tier, purpose, states, terminal, transitions, invariants, entities, reqs, notes=None, personal=False):
    AGGS[id_] = dict(id=id_, bc=bc, name=name, tier=tier, purpose=purpose, states=states, terminal=terminal,
                     transitions=transitions, invariants=invariants, entities=entities, requirements=reqs, notes=notes, personal_data=personal)

agg("AGG-PROJECTION-VERSION","BC07","Projection Version","T3","إصدار فهرس بحث أو رسم يُبنى ويُرقّى بأسلوب blue/green",
 ["BUILDING","READY","ACTIVE","DEGRADED","FAILED","RETIRED"],["FAILED","RETIRED"],
 [("∅","CMD-PRJ-CREATE-VERSION","BUILDING","kind ∈ {search, graph, vector (R2, SLC-10)}; document schema version, embedding model version (vector), analyzer/normalization version and source checkpoint set; at most one BUILDING version per (tenant group, kind)","EVT-PRJ-BUILD-STARTED","PROJECTION_BUILD_IN_PROGRESS"),
  (["BUILDING"],"SYS:full rebuild reached live checkpoint","READY","all source streams replayed to current checkpoint; verification sample equals source (FIT-11)","EVT-PRJ-READY",None),
  (["BUILDING"],"SYS:build failed","FAILED","unrecoverable build error","EVT-PRJ-FAILED",None),
  (["READY"],"CMD-PRJ-PROMOTE","ACTIVE","operator; verification passed; previous ACTIVE of same kind → RETIRED in the same step (alias switch)","EVT-PRJ-PROMOTED","PROJECTION_NOT_VERIFIED"),
  (["ACTIVE"],"SYS:lag above threshold","DEGRADED","lag > 5 min or error rate > 1 % for 5 min","EVT-PRJ-DEGRADED",None),
  (["DEGRADED"],"SYS:lag back within target","ACTIVE","lag ≤ 30 s for 5 min","EVT-PRJ-RECOVERED",None),
  (["READY","ACTIVE","DEGRADED"],"CMD-PRJ-RETIRE","RETIRED","operator; not the only ACTIVE version of its kind","EVT-PRJ-RETIRED","LAST_ACTIVE_PROJECTION"),
  (["BUILDING"],"CMD-PRJ-CANCEL-BUILD","FAILED","operator; reason","EVT-PRJ-FAILED","REASON_REQUIRED")],
 ["INV-PRJ-01: a projection is never a source of truth; every document is reproducible from owner contexts (A07, FIT-11)",
  "INV-PRJ-02: exactly one ACTIVE version per (tenant group, kind) serves queries; promotion is atomic (alias switch)",
  "INV-PRJ-03: every document carries security labels (tenant, level, compartments, caveats, org_scope, security_version) — ADR-P06",
  "INV-PRJ-04: normalization, schema or embedding-model changes require a new version (no in-place re-analysis)"],
 ["SourceCheckpoint (stream, position)","VerificationReport"],["REQ-SRC-004"],
 "Operational aggregate (T3): the platform operator manages rebuilds; tenants never see projection versions.")

PERPETUAL = {}
QUERIES = [
 ("QRY-SRCH-QUERY","BC07","POST","/api/v1/discovery/search-queries","Unified search: text + types + polygon/bbox + time window + filters + facets; cursor paging; results and facets over visible facts only","any user; allowed_scope pre-filter + authoritative re-check","REQ-SRC-001"),
 ("QRY-SRCH-SUGGEST","BC07","GET","/api/v1/discovery/suggestions","Autocomplete from visible facts only","any user; same filter","REQ-SRC-003"),
 ("QRY-GRAPH-NEIGHBORHOOD","BC07","GET","/api/v1/discovery/graph/entities/{entity_id}/neighborhood","Nodes/edges within depth ≤ 3, valid_at/known_at; hidden nodes and edges cut","any user; per-node and per-edge authorization","REQ-INF-027"),
 ("QRY-GRAPH-PATHS","BC07","POST","/api/v1/discovery/graph/paths","Paths between two entities, ≤ 4 hops, only through visible nodes and edges","any user; per-node and per-edge authorization","REQ-INF-027"),
 ("QRY-PRJ-STATUS","BC07","GET","/api/v1/discovery/projection-versions","Projection versions, lag, state","platform operator","REQ-SRC-004"),
]
ACTORS = {"PRJ":"Platform Operator"}
P = {"CMD-PRJ-CREATE-VERSION":"kind!:enum(search,graph,vector) tenant_group!:string schema_version!:integer normalization_version!:integer reason!:string",
     "CMD-PRJ-PROMOTE":"","CMD-PRJ-RETIRE":"reason!:string","CMD-PRJ-CANCEL-BUILD":"reason!:string"}
SYSTEM_CMDS = set()
RESOURCE = {"AGG-PROJECTION-VERSION":("discovery","projection-versions")}
SECURITY_AFFECTING = set()
CONSUMERS = {"AGG-PROJECTION-VERSION":["Query router (alias switch)","Operations alerting"],"default":["Operations alerting"]}
CTX_OVERRIDE = {"BC07": ("discovery", "Discovery")}


def enrich(spec, bc):
    S = spec["components"]["schemas"]; P = spec["paths"]
    def js(ref): return {"application/json": {"schema": {"$ref": f"#/components/schemas/{ref}"}}}
    S.update({
     "GeoFilter": {"type": "object", "properties": {"bbox": {"type": "array", "items": {"type": "number"}, "minItems": 4, "maxItems": 4}, "polygon": {"type": "object"}}},
     "Interval": {"type": "object", "required": ["from"], "properties": {"from": {"type": "string", "format": "date-time"}, "to": {"type": ["string", "null"], "format": "date-time"}}},
     "SearchRequest": {"type": "object", "required": ["types"], "additionalProperties": False, "properties": {
        "text": {"type": "string", "maxLength": 500}, "types": {"type": "array", "minItems": 1, "items": {"enum": ["entity", "observation", "realworld_event", "document", "assessment", "plan", "task"]}},
        "geo": {"$ref": "#/components/schemas/GeoFilter"}, "time": {"$ref": "#/components/schemas/Interval"}, "valid_at": {"type": "string", "format": "date-time"},
        "filters": {"type": "array", "items": {"type": "object", "required": ["field", "op", "value"], "properties": {"field": {"type": "string"}, "op": {"enum": ["eq", "in", "range", "exists"]}, "value": {}}}},
        "facets": {"type": "array", "maxItems": 10, "items": {"type": "string"}}, "sort": {"enum": ["relevance", "time_desc", "time_asc", "distance"]},
        "cursor": {"type": ["string", "null"]}, "limit": {"type": "integer", "minimum": 1, "maximum": 100, "default": 20}}},
     "SearchHit": {"type": "object", "required": ["urn", "type", "title"], "properties": {"urn": {"$ref": "#/components/schemas/Urn"}, "canonical_urn": {"$ref": "#/components/schemas/Urn"},
        "type": {"type": "string"}, "title": {"type": "string"}, "snippet": {"type": "string"}, "location": {"type": ["object", "null"]}, "time": {"type": ["object", "null"]}, "score": {"type": "number"}}},
     "Facet": {"type": "object", "required": ["field", "buckets"], "properties": {"field": {"type": "string"}, "buckets": {"type": "array", "items": {"type": "object", "required": ["value", "count"], "properties": {"value": {"type": "string"}, "count": {"type": "integer", "minimum": 1}}}}}},
     "SearchResponse": {"type": "object", "required": ["hits", "facets", "next_cursor", "completeness"], "properties": {"hits": {"type": "array", "items": {"$ref": "#/components/schemas/SearchHit"}},
        "facets": {"type": "array", "items": {"$ref": "#/components/schemas/Facet"}}, "visible_total": {"type": "string"}, "next_cursor": {"type": ["string", "null"]}, "completeness": {"enum": ["complete", "partial_service_unavailable"]}}},
     "GraphNode": {"type": "object", "required": ["urn", "type", "label_text"], "properties": {"urn": {"$ref": "#/components/schemas/Urn"}, "type": {"type": "string"}, "label_text": {"type": "string"}, "depth": {"type": "integer"}}},
     "GraphEdge": {"type": "object", "required": ["urn", "type", "source", "target"], "properties": {"urn": {"$ref": "#/components/schemas/Urn"}, "type": {"type": "string"}, "source": {"$ref": "#/components/schemas/Urn"}, "target": {"$ref": "#/components/schemas/Urn"}, "valid": {"$ref": "#/components/schemas/Interval"}}},
     "GraphResponse": {"type": "object", "required": ["nodes", "edges", "truncated"], "properties": {"nodes": {"type": "array", "items": {"$ref": "#/components/schemas/GraphNode"}}, "edges": {"type": "array", "items": {"$ref": "#/components/schemas/GraphEdge"}}, "truncated": {"type": "boolean"}}},
     "PathRequest": {"type": "object", "required": ["from", "to"], "additionalProperties": False, "properties": {"from": {"$ref": "#/components/schemas/Urn"}, "to": {"$ref": "#/components/schemas/Urn"},
        "max_hops": {"type": "integer", "minimum": 1, "maximum": 4, "default": 3}, "relationship_types": {"type": "array", "items": {"type": "string"}}, "valid_at": {"type": "string", "format": "date-time"},
        "known_at": {"type": "string", "format": "date-time"}, "max_paths": {"type": "integer", "minimum": 1, "maximum": 20, "default": 5}}},
     "PathResponse": {"type": "object", "required": ["paths"], "properties": {"paths": {"type": "array", "items": {"type": "object", "properties": {"nodes": {"type": "array", "items": {"$ref": "#/components/schemas/Urn"}}, "edges": {"type": "array", "items": {"$ref": "#/components/schemas/Urn"}}}}}}},
     "LabelCheckRequest": {"type": "object", "required": ["urns"], "properties": {"urns": {"type": "array", "maxItems": 100, "items": {"$ref": "#/components/schemas/Urn"}}, "subject_security_version": {"type": "integer"}}},
     "LabelCheckResponse": {"type": "object", "required": ["results"], "properties": {"results": {"type": "array", "items": {"type": "object", "required": ["urn", "visible"], "properties": {"urn": {"$ref": "#/components/schemas/Urn"}, "visible": {"type": "boolean"}, "security_version": {"type": "integer"}}}}}},
    })
    P["/api/v1/discovery/search-queries"]["post"]["requestBody"] = {"required": True, "content": js("SearchRequest")}
    P["/api/v1/discovery/search-queries"]["post"]["responses"]["200"]["content"] = js("SearchResponse")
    op = P["/api/v1/discovery/suggestions"]["get"]; op["parameters"] += [{"name": "q", "in": "query", "required": True, "schema": {"type": "string", "minLength": 2, "maxLength": 100}}]
    op["responses"]["200"]["content"] = {"application/json": {"schema": {"type": "object", "properties": {"suggestions": {"type": "array", "maxItems": 10, "items": {"type": "string"}}}}}}
    op = P["/api/v1/discovery/graph/entities/{entity_id}/neighborhood"]["get"]
    op["parameters"] += [{"name": "depth", "in": "query", "required": False, "schema": {"type": "integer", "minimum": 1, "maximum": 3, "default": 1}},
                         {"name": "valid_at", "in": "query", "required": False, "schema": {"type": "string", "format": "date-time"}}, {"name": "known_at", "in": "query", "required": False, "schema": {"type": "string", "format": "date-time"}}]
    op["responses"]["200"]["content"] = js("GraphResponse")
    op = P["/api/v1/discovery/graph/paths"]["post"]; op["requestBody"] = {"required": True, "content": js("PathRequest")}; op["responses"]["200"]["content"] = js("PathResponse")
    P["/api/v1/{context}/label-checks"] = {"post": {"operationId": "QRY-LABEL-CHECK", "summary": "LabelCheck OHS contract implemented by each owning context; discovery workload identity only",
        "parameters": [{"name": "context", "in": "path", "required": True, "schema": {"type": "string"}}, {"$ref": "#/components/parameters/X-Correlation-Id"}],
        "requestBody": {"required": True, "content": js("LabelCheckRequest")}, "responses": {"200": {"description": "ok", "content": js("LabelCheckResponse")}}}}
```

## slc06_data.py

```python
# -*- coding: utf-8 -*-
# SLC-06 — Situation, Alerts, Notifications, Common Operational Picture (secured tiles)
SLICE = "SLC-06"
AGGS = {}
def agg(id_, bc, name, tier, purpose, states, terminal, transitions, invariants, entities, reqs, notes=None, personal=False):
    AGGS[id_] = dict(id=id_, bc=bc, name=name, tier=tier, purpose=purpose, states=states, terminal=terminal,
                     transitions=transitions, invariants=invariants, entities=entities, requirements=reqs, notes=notes, personal_data=personal)

agg("AGG-SITUATION","BC03","Situation","T2 definition; content is a projection","سياق تشغيلي بامتداد وزمن ومعايير عضوية؛ محتواه إسقاط (ADR-P07)",
 ["DRAFT","ACTIVE","PAUSED","CLOSED"],["CLOSED"],
 [("∅","CMD-SIT-CREATE","DRAFT","name; extent (polygon or buffer around an entity); time window; criteria valid per SPEC-SITUATION §2; owner; label","EVT-SIT-CREATED","SITUATION_INVALID"),
  (["DRAFT","ACTIVE","PAUSED"],"CMD-SIT-EDIT-DEFINITION","=","criteria/extent/window valid; new definition version; membership recomputed from the new version","EVT-SIT-DEFINITION-CHANGED","SITUATION_INVALID"),
  (["DRAFT"],"CMD-SIT-ACTIVATE","ACTIVE","definition complete; active situations per tenant ≤ quota","EVT-SIT-ACTIVATED","QUOTA_EXCEEDED"),
  (["ACTIVE"],"CMD-SIT-PAUSE","PAUSED","reason; membership frozen, alerts of its rules suspended","EVT-SIT-PAUSED","REASON_REQUIRED"),
  (["PAUSED"],"CMD-SIT-RESUME","ACTIVE","membership re-evaluated from current state","EVT-SIT-RESUMED",None),
  (["DRAFT","ACTIVE","PAUSED"],"CMD-SIT-CLOSE","CLOSED","reason; final membership snapshot recorded","EVT-SIT-CLOSED","REASON_REQUIRED"),
  (["DRAFT","ACTIVE","PAUSED"],"CMD-SIT-RECLASSIFY","=","authority per tenant policy; subscribers without clearance are unsubscribed","EVT-SIT-RECLASSIFIED","CLASSIFICATION_CHANGE_NOT_AUTHORIZED")],
 ["INV-SIT-01: members stay owned by their contexts; the situation stores only definition, membership records and change log",
  "INV-SIT-02: a reader sees a situation only if cleared for its label, and sees each member only if cleared for that member (per-member filtering)",
  "INV-SIT-03: membership is evaluated against the definition version that was ACTIVE at the evaluation time (history reproducible)",
  "INV-SIT-04: a CLOSED situation keeps its final snapshot and change log"],
 ["DefinitionVersion (extent, window, criteria)","MembershipRecord (member_urn, from, to, cause)","SituationChange"],
 ["REQ-SIT-001","REQ-SIT-002","REQ-SIT-003"])

agg("AGG-ALERT-RULE","BC03","Alert Rule","T2","قاعدة تنبيه على موقف أو على نطاق المستأجر",
 ["DRAFT","ACTIVE","DISABLED","RETIRED"],["RETIRED"],
 [("∅","CMD-ARL-DEFINE","DRAFT","condition kind in RD-ALERT-RULE-TYPES; parameters valid; severity; dedupe window; situation ACTIVE or tenant-wide scope","EVT-ARL-DEFINED","ALERT_RULE_INVALID"),
  (["DRAFT","DISABLED"],"CMD-ARL-EDIT","=","same validation; new version","EVT-ARL-EDITED","ALERT_RULE_INVALID"),
  (["DRAFT"],"CMD-ARL-ACTIVATE","ACTIVE","dry-run on last 24 h of events completed and reviewed (expected alert volume shown)","EVT-ARL-ACTIVATED","DRY_RUN_REQUIRED"),
  (["ACTIVE"],"CMD-ARL-DISABLE","DISABLED","reason","EVT-ARL-DISABLED","REASON_REQUIRED"),
  (["DISABLED"],"CMD-ARL-ENABLE","ACTIVE","—","EVT-ARL-ENABLED",None),
  (["DRAFT","ACTIVE","DISABLED"],"CMD-ARL-RETIRE","RETIRED","reason","EVT-ARL-RETIRED","REASON_REQUIRED")],
 ["INV-ARL-01: an ACTIVE rule is immutable; editing requires DISABLED (no silent change to what triggers alerts)",
  "INV-ARL-02: the rule's label ≥ labels of data it reads, enforced at evaluation by computing alert labels (INV-ALR-02)",
  "INV-ARL-03: rules of a PAUSED or CLOSED situation do not fire"],
 ["Condition (kind, parameters)","DedupePolicy","AutoResolve (bool)"],["REQ-SIT-004"])

agg("AGG-ALERT","BC03","Alert","T2","تنبيه صادر عن قاعدة، بدورة حياة مدققة",
 ["RAISED","ACKNOWLEDGED","RESOLVED","DISMISSED"],["RESOLVED","DISMISSED"],
 [("∅","SYS:rule condition met","RAISED","no non-terminal alert for (rule, subject) inside dedupe window; label = max(rule label, triggering object labels)","EVT-ALR-RAISED",None),
  (["RAISED","ACKNOWLEDGED"],"SYS:condition met again within dedupe window","=","occurrence counter + last_occurrence updated","EVT-ALR-REPEATED",None),
  (["RAISED"],"CMD-ALR-ACKNOWLEDGE","ACKNOWLEDGED","actor is a recipient","EVT-ALR-ACKNOWLEDGED","NOT_A_RECIPIENT"),
  (["RAISED"],"SYS:unacknowledged beyond escalation delay","=","escalates to the rule's escalation recipients","EVT-ALR-ESCALATED",None),
  (["RAISED","ACKNOWLEDGED"],"CMD-ALR-RESOLVE","RESOLVED","actor is a recipient; note","EVT-ALR-RESOLVED","NOT_A_RECIPIENT"),
  (["RAISED","ACKNOWLEDGED"],"SYS:condition cleared and rule auto_resolve","RESOLVED","system","EVT-ALR-RESOLVED",None),
  (["RAISED","ACKNOWLEDGED"],"CMD-ALR-DISMISS","DISMISSED","actor is a recipient; reason (REQ-SIT-005)","EVT-ALR-DISMISSED","REASON_REQUIRED")],
 ["INV-ALR-01: every transition is audited (REQ-SIT-005)",
  "INV-ALR-02: alert label = max(rule label, labels of triggering objects); only recipients cleared for that label receive it — others receive nothing, not a redacted alert (REQ-SIT-006)",
  "INV-ALR-03: dedupe: at most one non-terminal alert per (rule, subject) within the dedupe window"],
 ["Occurrence (at, trigger_ref)"],["REQ-SIT-004","REQ-SIT-005","REQ-SIT-006"])

agg("AGG-SUBSCRIPTION","BC04","Subscription","T3","اشتراك مستخدم في تنبيهات موقف أو قاعدة، بقنوات مفضلة",
 ["ACTIVE","PAUSED","ENDED"],["ENDED"],
 [("∅","CMD-SUB-SUBSCRIBE","ACTIVE","target (situation | alert rule) visible to subscriber; channels ⊆ {in_app, push}; one ACTIVE per (user, target)","EVT-SUB-SUBSCRIBED","SUBSCRIPTION_EXISTS"),
  (["ACTIVE","PAUSED"],"CMD-SUB-UPDATE-CHANNELS","=","channels valid; quiet hours valid (critical severity bypasses quiet hours)","EVT-SUB-CHANNELS-UPDATED","SUBSCRIPTION_INVALID"),
  (["ACTIVE"],"CMD-SUB-PAUSE","PAUSED","—","EVT-SUB-PAUSED",None),
  (["PAUSED"],"CMD-SUB-RESUME","ACTIVE","target still visible","EVT-SUB-RESUMED","TARGET_NOT_VISIBLE"),
  (["ACTIVE","PAUSED"],"CMD-SUB-UNSUBSCRIBE","ENDED","actor = subscriber or Administrator","EVT-SUB-ENDED",None),
  (["ACTIVE","PAUSED"],"SYS:subscriber lost visibility of target","ENDED","security-version change or reclassification","EVT-SUB-ENDED",None)],
 ["INV-SUB-01: a subscription never grants access; delivery re-checks authorization","INV-SUB-02: subscriptions end automatically when the target becomes invisible to the subscriber"],
 [],["REQ-COM-001"])

agg("AGG-NOTIFICATION","BC04","Notification","T3","رسالة لمستلم واحد؛ الحمولة مرجع فقط",
 ["QUEUED","SENT","READ","FAILED","WITHHELD","EXPIRED"],["READ","FAILED","WITHHELD","EXPIRED"],
 [("∅","SYS:notifiable event for recipient","QUEUED","recipient ACTIVE; recipient authorized for the referenced object at enqueue time","EVT-NTF-QUEUED",None),
  (["QUEUED"],"SYS:delivered to channel","SENT","re-check authorization at delivery (security_version); push payload = reference + classification-safe title template","EVT-NTF-SENT",None),
  (["QUEUED"],"SYS:recipient no longer authorized at delivery","WITHHELD","re-check failed","EVT-NTF-WITHHELD",None),
  (["QUEUED"],"SYS:delivery failed after retries","FAILED","5 attempts with exponential backoff; in-app copy remains","EVT-NTF-FAILED",None),
  (["SENT"],"CMD-NTF-MARK-READ","READ","actor = recipient; content fetched through normal authorized query","EVT-NTF-READ","NOT_RECIPIENT"),
  (["QUEUED","SENT"],"SYS:TTL (30 d) elapsed","EXPIRED","scheduler","EVT-NTF-EXPIRED",None)],
 ["INV-NTF-01: a notification is not a domain event and never carries business content (glossary)",
  "INV-NTF-02: push payloads contain no classified content: reference URN + template title chosen from a classification-safe list (REQ-COM-002)",
  "INV-NTF-03: opening a notification performs a normal authorized read; a revoked user sees not-found"],
 [],["REQ-COM-001","REQ-COM-002"])

PERPETUAL = {}
QUERIES = [
 ("QRY-SIT-LIST","BC03","GET","/api/v1/intelligence/situations","Situations by state, owner, extent intersecting bbox","any user; situation label rule","REQ-SIT-001"),
 ("QRY-SIT-GET","BC03","GET","/api/v1/intelligence/situations/{situation_id}","Definition (version at valid_at), counts of visible members by type","cleared for situation label","REQ-SIT-001"),
 ("QRY-SIT-COP","BC03","GET","/api/v1/intelligence/situations/{situation_id}/picture","Common operational picture: visible members (entities, events, observations, tasks, assessments, alerts) with resolved, possibly generalized geometry","cleared for situation; per-member filtering","REQ-SIT-003"),
 ("QRY-SIT-CHANGES","BC03","GET","/api/v1/intelligence/situations/{situation_id}/changes","Membership change log (visible members only) since cursor/time","cleared for situation; per-member filtering","REQ-SIT-002"),
 ("QRY-SIT-TILE","BC03","GET","/api/v1/intelligence/situations/{situation_id}/tiles/{layer}/{z}/{x}/{y}","Vector tile of operational layer for the caller's security scope","cleared for situation; scope-keyed cache (ADR-P06 §6)","REQ-SIT-007"),
 ("QRY-BASE-TILE","BC03","GET","/api/v1/intelligence/base-maps/{layer}/{z}/{x}/{y}","Base-map tile (layers marked unclassified only; shared cache)","any user of tenant","REQ-SIT-007"),
 ("QRY-ALR-LIST","BC03","GET","/api/v1/intelligence/alerts","My alerts by state, severity, situation","recipient; label rule","REQ-SIT-005"),
 ("QRY-NTF-INBOX","BC04","GET","/api/v1/operations/notifications","My notifications (references + templates)","recipient","REQ-COM-001"),
]
ACTORS = {"SIT":"Analyst / Manager (create, edit, activate, pause, close) · Security Officer (reclassify)","ARL":"Analyst lead / Manager","ALR":"recipient",
          "SUB":"any user (self) · Administrator (end)","NTF":"recipient"}
P = {
 "CMD-SIT-CREATE":"name!:LocalizedName extent!:object window!:Interval criteria!:object owner!:urn label!:Label",
 "CMD-SIT-EDIT-DEFINITION":"extent:object window:Interval criteria:object reason!:string","CMD-SIT-ACTIVATE":"","CMD-SIT-PAUSE":"reason!:string",
 "CMD-SIT-RESUME":"","CMD-SIT-CLOSE":"reason!:string","CMD-SIT-RECLASSIFY":"label!:Label reason!:string",
 "CMD-ARL-DEFINE":"situation:urn scope!:enum(situation,tenant) kind!:string parameters!:object severity!:enum(info,warning,critical) dedupe_window!:string escalation:object auto_resolve!:boolean label!:Label",
 "CMD-ARL-EDIT":"parameters!:object severity:enum(info,warning,critical) dedupe_window:string escalation:object","CMD-ARL-ACTIVATE":"dry_run_ref!:string",
 "CMD-ARL-DISABLE":"reason!:string","CMD-ARL-ENABLE":"","CMD-ARL-RETIRE":"reason!:string",
 "CMD-ALR-ACKNOWLEDGE":"note:string","CMD-ALR-RESOLVE":"note!:string","CMD-ALR-DISMISS":"reason!:string",
 "CMD-SUB-SUBSCRIBE":"target!:urn channels!:array quiet_hours:object","CMD-SUB-UPDATE-CHANNELS":"channels!:array quiet_hours:object",
 "CMD-SUB-PAUSE":"","CMD-SUB-RESUME":"","CMD-SUB-UNSUBSCRIBE":"reason:string","CMD-NTF-MARK-READ":"",
}
SYSTEM_CMDS = set()
RESOURCE = {"AGG-SITUATION":("intelligence","situations"),"AGG-ALERT-RULE":("intelligence","alert-rules"),"AGG-ALERT":("intelligence","alerts"),
            "AGG-SUBSCRIPTION":("operations","subscriptions"),"AGG-NOTIFICATION":("operations","notifications")}
SECURITY_AFFECTING = {"EVT-SIT-RECLASSIFIED"}
CONSUMERS = {
 "AGG-SITUATION":["Membership evaluator (reload definition)","Alert evaluator","Tile cache invalidation","Search projection (SLC-05)"],
 "AGG-ALERT-RULE":["Alert evaluator (reload rules)"],
 "AGG-ALERT":["Notification fan-out (recipients = cleared subscribers)","COP (alerts layer)","Escalation scheduler"],
 "AGG-SUBSCRIPTION":["Notification fan-out index"],"AGG-NOTIFICATION":["Push gateway","In-app inbox"],
 "default":["Search projection (SLC-05)"],
}


def enrich(spec, bc):
    if bc != "BC03": return
    S = spec["components"]["schemas"]
    S["SituationCriteria"] = {"type": "object", "additionalProperties": False, "required": ["object_types"], "properties": {
      "object_types": {"type": "array", "minItems": 1, "items": {"enum": ["entity", "realworld_event", "observation", "task", "assessment", "alert"]}},
      "entity_types": {"type": "array", "items": {"type": "string"}}, "event_types": {"type": "array", "items": {"type": "string"}},
      "predicate_filters": {"type": "array", "items": {"type": "object", "required": ["predicate", "op"], "properties": {"predicate": {"type": "string"}, "op": {"enum": ["eq", "in", "gte", "lte", "exists", "changed"]}, "value": {}}}},
      "observation_methods": {"type": "array", "items": {"type": "string"}}, "min_source_reliability": {"enum": ["A", "B", "C", "D", "E", "F"]},
      "include_disputed": {"type": "boolean", "default": True}, "include_unvalidated_observations": {"type": "boolean", "default": False}}}
    S["SituationExtent"] = {"type": "object", "oneOf": [{"required": ["polygon"], "properties": {"polygon": {"type": "object"}}},
      {"required": ["buffer_around", "radius_m"], "properties": {"buffer_around": {"$ref": "#/components/schemas/Urn"}, "radius_m": {"type": "number", "minimum": 1, "maximum": 500000}}}]}
    S["AlertCondition"] = {"type": "object", "required": ["kind"], "properties": {"kind": {"enum": ["measurement_threshold", "enters_extent", "leaves_extent", "new_observation_in_extent", "claim_changed", "conflict_opened", "task_overdue_in_situation"]},
      "quantity": {"type": "string"}, "op": {"enum": ["gt", "gte", "lt", "lte"]}, "threshold": {"type": "number"}, "unit": {"type": "string"}, "entity_types": {"type": "array", "items": {"type": "string"}},
      "predicate": {"type": "string"}, "observation_methods": {"type": "array", "items": {"type": "string"}}}}
    for name, sch in S.items():
        if name.endswith("Command") and "properties" in sch:
            pr = sch["properties"]
            if name.startswith(("SitCreate", "SitEditDefinition")):
                pr["criteria"] = {"$ref": "#/components/schemas/SituationCriteria"}; pr["extent"] = {"$ref": "#/components/schemas/SituationExtent"}
            if name.startswith(("ArlDefine", "ArlEdit")): pr["parameters"] = {"$ref": "#/components/schemas/AlertCondition"}
    tile = {"200": {"description": "vector tile for the caller's security scope", "headers": {"Cache-Control": {"schema": {"type": "string"}, "description": "private, max-age <= 60; shared caches keyed by scope hash only"},
            "ETag": {"schema": {"type": "string"}, "description": "hash(tile, layer, scope_hash, data_version)"}}, "content": {"application/vnd.mapbox-vector-tile": {"schema": {"type": "string", "format": "binary"}}}}}
    for path in ["/api/v1/intelligence/situations/{situation_id}/tiles/{layer}/{z}/{x}/{y}", "/api/v1/intelligence/base-maps/{layer}/{z}/{x}/{y}"]:
        op = spec["paths"][path]["get"]; op["responses"] = {**tile, **{k: v for k, v in op["responses"].items() if k != "200"}}
```

## slc07_data.py

```python
# -*- coding: utf-8 -*-
# SLC-07 — Analysis Case → Run → Finding → Assessment (reproducible analytical work)
SLICE = "SLC-07"
AGGS = {}
def agg(id_, bc, name, tier, purpose, states, terminal, transitions, invariants, entities, reqs, notes=None, personal=False):
    AGGS[id_] = dict(id=id_, bc=bc, name=name, tier=tier, purpose=purpose, states=states, terminal=terminal,
                     transitions=transitions, invariants=invariants, entities=entities, requirements=reqs, notes=notes, personal_data=personal)

agg("AGG-ANALYSIS-CASE","BC03","Analysis Case","T2 lifecycle; T1 selections","سؤال تحليلي بنطاق وفرضيات وافتراضات وأدلة مختارة مثبتة زمنياً",
 ["DRAFT","OPEN","CLOSED","CANCELLED"],["CANCELLED"],
 [("∅","CMD-ACS-CREATE","DRAFT","title; owner; label","EVT-ACS-CREATED","CASE_INVALID"),
  (["DRAFT","OPEN"],"CMD-ACS-DEFINE","=","question text; spatial extent (optional polygon); time window; new version","EVT-ACS-DEFINED","CASE_INVALID"),
  (["DRAFT"],"CMD-ACS-OPEN","OPEN","question and scope present (REQ-ANL-001)","EVT-ACS-OPENED","CASE_NOT_DEFINED"),
  (["OPEN"],"CMD-ACS-ADD-HYPOTHESIS","=","statement; hypotheses per case ≤ 20","EVT-ACS-HYPOTHESIS-ADDED","CASE_INVALID"),
  (["OPEN"],"CMD-ACS-UPDATE-HYPOTHESIS","=","status ∈ {PROPOSED, SUPPORTED, WEAKENED, REJECTED, UNRESOLVED}; rationale; supporting findings refs","EVT-ACS-HYPOTHESIS-UPDATED","REASON_REQUIRED"),
  (["OPEN"],"CMD-ACS-ADD-ASSUMPTION","=","statement; criticality (high/medium/low)","EVT-ACS-ASSUMPTION-ADDED","CASE_INVALID"),
  (["OPEN"],"CMD-ACS-RETIRE-ASSUMPTION","=","reason; runs using it are flagged","EVT-ACS-ASSUMPTION-RETIRED","REASON_REQUIRED"),
  (["OPEN"],"CMD-ACS-SELECT-EVIDENCE","=","items visible to actor; each pinned with known_at = now; item label ≤ case label","EVT-ACS-EVIDENCE-SELECTED","EVIDENCE_ABOVE_CASE_LABEL"),
  (["OPEN"],"CMD-ACS-DESELECT-EVIDENCE","=","reason; selection record closed, not deleted","EVT-ACS-EVIDENCE-DESELECTED","REASON_REQUIRED"),
  (["OPEN"],"CMD-ACS-DEFINE-SCENARIO","=","name; assumption set; parameter overrides (REQ-ANL-007)","EVT-ACS-SCENARIO-DEFINED","CASE_INVALID"),
  (["OPEN"],"CMD-ACS-CLOSE","CLOSED","reason; no QUEUED or RUNNING runs","EVT-ACS-CLOSED","RUNS_IN_PROGRESS"),
  (["CLOSED"],"CMD-ACS-REOPEN","OPEN","reason","EVT-ACS-REOPENED","REASON_REQUIRED"),
  (["DRAFT","OPEN"],"CMD-ACS-CANCEL","CANCELLED","reason; no PUBLISHED assessment references the case","EVT-ACS-CANCELLED","CASE_HAS_PUBLISHED_ASSESSMENT"),
  (["DRAFT","OPEN","CLOSED"],"CMD-ACS-RECLASSIFY","=","new label ≥ max label of selected evidence; authority per policy","EVT-ACS-RECLASSIFIED","CLASSIFICATION_CHANGE_NOT_AUTHORIZED")],
 ["INV-ACS-01: every evidence selection is pinned with known_at so its content is reproducible (TEMPORAL-MODEL §4)",
  "INV-ACS-02: case label ≥ max label of its selected items (no lower-labelled case exposing higher-labelled selections)",
  "INV-ACS-03: runs, findings and assessments are separate aggregates (CR-29: no God aggregate)",
  "INV-ACS-04: selections and assumptions are never deleted; deselection/retirement closes them with reason"],
 ["Question (VO)","Scope (VO)","Hypothesis","Assumption","EvidenceSelection (item_urn, known_at, selected_by, closed_at)","Scenario"],
 ["REQ-ANL-001","REQ-ANL-007"],"Closing CR-29 for AnalysisCase: PRJ§58 listed 12 components in one aggregate; here the case holds only definition-level parts.")

agg("AGG-ANALYSIS-METHOD","BC03","Analysis Method Version","T2","طريقة تحليل بإصدار وبيئة تنفيذ ثابتة",
 ["DRAFT","ACTIVE","DEPRECATED","RETIRED"],["RETIRED"],
 [("∅","CMD-AMT-REGISTER","DRAFT","code + version unique; parameter JSON schema; execution image digest from internal registry; deterministic flag","EVT-AMT-REGISTERED","METHOD_INVALID"),
  (["DRAFT"],"CMD-AMT-ACTIVATE","ACTIVE","validation suite passed; approver ≠ author","EVT-AMT-ACTIVATED","SEGREGATION_OF_DUTIES"),
  (["ACTIVE"],"CMD-AMT-DEPRECATE","DEPRECATED","reason; no new runs; reproduction still allowed","EVT-AMT-DEPRECATED","REASON_REQUIRED"),
  (["DEPRECATED"],"CMD-AMT-RETIRE","RETIRED","no run of this version backs a PUBLISHED or SUPERSEDED assessment (reproducibility preserved)","EVT-AMT-RETIRED","METHOD_BACKS_PUBLISHED_WORK")],
 ["INV-AMT-01: a method version is immutable (image digest, parameter schema, code)","INV-AMT-02: a version backing published work stays executable (DEPRECATED at most)"],
 ["ParameterSchema","ExecutionImage (digest)"],["REQ-ANL-002","REQ-ANL-003"])

agg("AGG-ANALYSIS-RUN","BC03","Analysis Run","T1 results / T2 lifecycle","تنفيذ طريقة على مدخلات مثبتة، كمهمة غير متزامنة",
 ["QUEUED","RUNNING","SUCCEEDED","FAILED","CANCELLED"],["SUCCEEDED","FAILED","CANCELLED"],
 [("∅","CMD-RUN-SUBMIT","QUEUED","case OPEN; method ACTIVE; parameters valid against schema; inputs pinned (dataset refs with known_at = submission time, filters, layers, extent, time window, assumptions); run label ≥ max input label; tenant job quota","EVT-RUN-QUEUED","RUN_INVALID"),
  ("∅","CMD-RUN-REPRODUCE","QUEUED","source run SUCCEEDED; reproducer cleared for source run label; method version ACTIVE or DEPRECATED; copies inputs/parameters/seed exactly","EVT-RUN-QUEUED","REPRODUCTION_NOT_ALLOWED"),
  (["QUEUED"],"SYS:worker lease acquired","RUNNING","executes with the submitter's authorization (visibility), never with system privileges","EVT-RUN-STARTED",None),
  (["RUNNING"],"SYS:completed","SUCCEEDED","results stored as hashed artifacts; steps log; lineage record written (inputs+known_at, method version, image digest, parameters, seed, actor, times)","EVT-RUN-SUCCEEDED",None),
  (["RUNNING"],"SYS:error or timeout","FAILED","error recorded; partial artifacts discarded","EVT-RUN-FAILED",None),
  (["QUEUED","RUNNING"],"CMD-RUN-CANCEL","CANCELLED","submitter or case owner; reason","EVT-RUN-CANCELLED","REASON_REQUIRED")],
 ["INV-RUN-01: inputs are pinned by known_at, so re-execution sees exactly the same data (REQ-ANL-003)",
  "INV-RUN-02: a run reads only what its submitter may see; results label ≥ max input label",
  "INV-RUN-03: a reproduction compares result hashes and reports REPRODUCED or DIFFERENT with the differing inputs/method/environment",
  "INV-RUN-04: SUCCEEDED results are immutable"],
 ["InputPin (ref, known_at, filters)","StepLog","ResultArtifact (hash, kind)","ReproductionReport"],
 ["REQ-ANL-002","REQ-ANL-003","REQ-ANL-004","REQ-INF-035"])

agg("AGG-FINDING","BC03","Finding","T1","نتيجة تحليلية مستخلصة من تشغيلات أو أدلة",
 ["DRAFT","ACCEPTED","WITHDRAWN"],["WITHDRAWN"],
 [("∅","CMD-FND-RECORD","DRAFT","statement; ≥ 1 source among SUCCEEDED runs of the case or selected evidence; uncertainty; label ≥ sources","EVT-FND-RECORDED","FINDING_INVALID"),
  (["DRAFT"],"CMD-FND-EDIT","=","same rules; new version","EVT-FND-EDITED","FINDING_INVALID"),
  (["DRAFT"],"CMD-FND-ACCEPT","ACCEPTED","reviewer ≠ author (peer review)","EVT-FND-ACCEPTED","SEGREGATION_OF_DUTIES"),
  (["DRAFT","ACCEPTED"],"CMD-FND-WITHDRAW","WITHDRAWN","reason; assessments citing it are flagged for review","EVT-FND-WITHDRAWN","REASON_REQUIRED")],
 ["INV-FND-01: an ACCEPTED finding is immutable","INV-FND-02: every finding traces to runs or evidence (lineage)"],
 ["FindingSource (run_urn | evidence_urn)"],["REQ-ANL-005","REQ-INF-035"])

agg("AGG-ASSESSMENT","BC03","Assessment Version","T1 content / T2 lifecycle","تقييم تحليلي بإصدارات؛ الإصدار المنشور ثابت",
 ["DRAFT","IN_REVIEW","PUBLISHED","SUPERSEDED","WITHDRAWN","DISCARDED"],["SUPERSEDED","WITHDRAWN","DISCARDED"],
 [("∅","CMD-ASM-DRAFT","DRAFT","case exists; either new assessment or revision of a PUBLISHED version (copies content); at most one DRAFT/IN_REVIEW per assessment","EVT-ASM-DRAFTED","DRAFT_EXISTS"),
  (["DRAFT"],"CMD-ASM-EDIT","=","key judgments use RD-ESTIMATIVE-PROBABILITY terms and analytic confidence (low/moderate/high)","EVT-ASM-EDITED","ASSESSMENT_INVALID"),
  (["DRAFT"],"CMD-ASM-SUBMIT","IN_REVIEW","findings ≥ 1 (ACCEPTED), evidence, assumptions, uncertainty, confidence, methodology, limitations all present (REQ-ANL-005)","EVT-ASM-SUBMITTED","ASSESSMENT_INCOMPLETE"),
  (["IN_REVIEW"],"CMD-ASM-RETURN","DRAFT","reviewer; reason","EVT-ASM-RETURNED","REASON_REQUIRED"),
  (["IN_REVIEW"],"CMD-ASM-PUBLISH","PUBLISHED","reviewer ≠ author; label ≥ max(findings, evidence); previous PUBLISHED version → SUPERSEDED in the same transaction","EVT-ASM-PUBLISHED","SEGREGATION_OF_DUTIES"),
  (["PUBLISHED"],"SYS:newer version published","SUPERSEDED","system","EVT-ASM-SUPERSEDED",None),
  (["PUBLISHED"],"CMD-ASM-WITHDRAW","WITHDRAWN","reason; decisions and products referencing it are notified","EVT-ASM-WITHDRAWN","REASON_REQUIRED"),
  (["DRAFT"],"CMD-ASM-DISCARD","DISCARDED","author; reason","EVT-ASM-DISCARDED","REASON_REQUIRED")],
 ["INV-ASM-01: a PUBLISHED version is immutable; changes are new versions (REQ-ANL-006)",
  "INV-ASM-02: exactly one PUBLISHED version per assessment at a time; history of versions retained",
  "INV-ASM-03: references from decisions pin the version (URN + version) — superseding never changes what a past decision relied on",
  "INV-ASM-04: readers not cleared for some cited evidence get the assessment with those references withheld per policy (REQ-ANL-008)"],
 ["KeyJudgment (statement, probability term, confidence)","Citation (finding | evidence, pinned version)"],
 ["REQ-ANL-005","REQ-ANL-006","REQ-ANL-008"])

PERPETUAL = {}
QUERIES = [
 ("QRY-ACS-GET","BC03","GET","/api/v1/intelligence/analysis-cases/{case_id}","Case with question, scope, hypotheses, assumptions, visible selections, scenarios","case label rule; selections filtered","REQ-ANL-001"),
 ("QRY-ACS-LIST","BC03","GET","/api/v1/intelligence/analysis-cases","Cases by owner, state, extent","allowed_scope","REQ-ANL-001"),
 ("QRY-RUN-GET","BC03","GET","/api/v1/intelligence/analysis-runs/{run_id}","Run with pins, parameters, steps, status, artifacts, reproduction report","run label rule","REQ-ANL-002"),
 ("QRY-RUN-ARTIFACT","BC03","POST","/api/v1/intelligence/analysis-runs/{run_id}/artifact-grants","Short-lived download target for a result artifact","run label rule; audited","REQ-ANL-002"),
 ("QRY-SCN-COMPARE","BC03","GET","/api/v1/intelligence/analysis-cases/{case_id}/scenario-comparison","Side-by-side results of runs per scenario with differing inputs","case label rule","REQ-ANL-007"),
 ("QRY-FND-LIST","BC03","GET","/api/v1/intelligence/analysis-cases/{case_id}/findings","Findings with sources","label rule","REQ-ANL-005"),
 ("QRY-ASM-GET","BC03","GET","/api/v1/intelligence/assessments/{assessment_id}","Assessment version (default: current PUBLISHED; or version / known_at)","label rule; REDACT obligation for uncleared citations","REQ-ANL-008"),
 ("QRY-ASM-VERSIONS","BC03","GET","/api/v1/intelligence/assessments/{assessment_id}/versions","Version history with states and times","label rule","REQ-ANL-006"),
 ("QRY-AMT-LIST","BC03","GET","/api/v1/intelligence/analysis-methods","Methods and versions","any analyst","REQ-ANL-002"),
]
ACTORS = {"ACS":"Analyst (owner) · Security Officer (reclassify)","AMT":"Analysis lead (register) · second lead or Administrator (activate)",
          "RUN":"Analyst (submit, reproduce, cancel)","FND":"Analyst (record, edit, withdraw) · peer Analyst (accept)",
          "ASM":"Analyst (draft, edit, submit, discard) · reviewer / Analysis lead (return, publish, withdraw)"}
P = {
 "CMD-ACS-CREATE":"title!:LocalizedName owner!:urn label!:Label","CMD-ACS-DEFINE":"question!:LocalizedName extent:object window!:Interval",
 "CMD-ACS-OPEN":"","CMD-ACS-ADD-HYPOTHESIS":"statement!:LocalizedName","CMD-ACS-UPDATE-HYPOTHESIS":"hypothesis_id!:string status!:enum(PROPOSED,SUPPORTED,WEAKENED,REJECTED,UNRESOLVED) rationale!:string findings:array",
 "CMD-ACS-ADD-ASSUMPTION":"statement!:LocalizedName criticality!:enum(high,medium,low)","CMD-ACS-RETIRE-ASSUMPTION":"assumption_id!:string reason!:string",
 "CMD-ACS-SELECT-EVIDENCE":"items!:array note:string","CMD-ACS-DESELECT-EVIDENCE":"selection_id!:string reason!:string",
 "CMD-ACS-DEFINE-SCENARIO":"name!:string assumptions!:array parameter_overrides:object","CMD-ACS-CLOSE":"reason!:string","CMD-ACS-REOPEN":"reason!:string",
 "CMD-ACS-CANCEL":"reason!:string","CMD-ACS-RECLASSIFY":"label!:Label reason!:string",
 "CMD-AMT-REGISTER":"code!:string version!:string parameter_schema!:object image_digest!:string deterministic!:boolean description!:LocalizedName",
 "CMD-AMT-ACTIVATE":"validation_report!:urn","CMD-AMT-DEPRECATE":"reason!:string","CMD-AMT-RETIRE":"reason!:string",
 "CMD-RUN-SUBMIT":"case!:urn method!:urn parameters!:object inputs!:array scenario:string assumptions:array seed:integer label!:Label",
 "CMD-RUN-REPRODUCE":"source_run!:urn","CMD-RUN-CANCEL":"reason!:string",
 "CMD-FND-RECORD":"case!:urn statement!:LocalizedName sources!:array uncertainty!:object label!:Label","CMD-FND-EDIT":"statement:LocalizedName sources:array uncertainty:object",
 "CMD-FND-ACCEPT":"note:string","CMD-FND-WITHDRAW":"reason!:string",
 "CMD-ASM-DRAFT":"case!:urn assessment:urn title!:LocalizedName label!:Label","CMD-ASM-EDIT":"key_judgments!:array citations!:array assumptions!:array uncertainty!:object confidence!:enum(low,moderate,high) methodology!:LocalizedName limitations!:LocalizedName",
 "CMD-ASM-SUBMIT":"","CMD-ASM-RETURN":"reason!:string","CMD-ASM-PUBLISH":"note:string","CMD-ASM-WITHDRAW":"reason!:string","CMD-ASM-DISCARD":"reason!:string",
}
SYSTEM_CMDS = set()
RESOURCE = {"AGG-ANALYSIS-CASE":("intelligence","analysis-cases"),"AGG-ANALYSIS-METHOD":("intelligence","analysis-methods"),"AGG-ANALYSIS-RUN":("intelligence","analysis-runs"),
            "AGG-FINDING":("intelligence","findings"),"AGG-ASSESSMENT":("intelligence","assessments")}
SECURITY_AFFECTING = {"EVT-ACS-RECLASSIFIED"}
CONSUMERS = {"AGG-ANALYSIS-RUN":["Job scheduler / compute workers","Lineage writer (BC02 LineageRecord)","Case owner notification"],
 "AGG-ASSESSMENT":["Decision requests (SLC-08: pinned references)","Situation membership (assessment layer)","Search projection (SLC-05)","Products (SLC-12, R2)"],
 "AGG-FINDING":["Assessment review flags"],"AGG-ANALYSIS-METHOD":["Job scheduler (image allow-list)"],
 "default":["Search projection (SLC-05)"]}

PATH_OVERRIDE = {"CMD-RUN-REPRODUCE": "/api/v1/intelligence/analysis-runs/{id}/actions/reproduce"}


def enrich(spec, bc):
    S = spec["components"]["schemas"]
    S["InputPin"] = {"type": "object", "required": ["ref", "known_at"], "properties": {"ref": {"$ref": "#/components/schemas/Urn"}, "known_at": {"type": "string", "format": "date-time", "description": "server sets = submission time"}, "valid_at": {"type": "string", "format": "date-time"}, "filters": {"type": "object"}, "layers": {"type": "array", "items": {"type": "string"}}}}
    S["Citation"] = {"type": "object", "required": ["ref", "version"], "properties": {"ref": {"$ref": "#/components/schemas/Urn"}, "version": {"type": "integer"}, "kind": {"enum": ["finding", "evidence", "claim", "run"]}}}
    S["KeyJudgment"] = {"type": "object", "required": ["statement", "probability_term", "confidence"], "properties": {"statement": {"$ref": "#/components/schemas/LocalizedName"}, "probability_term": {"type": "string"}, "confidence": {"enum": ["low", "moderate", "high"]}, "citations": {"type": "array", "items": {"$ref": "#/components/schemas/Citation"}}}}
    S["SelectionItem"] = {"type": "object", "required": ["ref"], "properties": {"ref": {"$ref": "#/components/schemas/Urn"}, "note": {"type": "string"}}}
    for name, sch in S.items():
        if not name.endswith("Command") or "properties" not in sch: continue
        pr = sch["properties"]
        if "inputs" in pr: pr["inputs"] = {"type": "array", "minItems": 1, "items": {"$ref": "#/components/schemas/InputPin"}}
        if "key_judgments" in pr: pr["key_judgments"] = {"type": "array", "minItems": 1, "items": {"$ref": "#/components/schemas/KeyJudgment"}}
        if "citations" in pr: pr["citations"] = {"type": "array", "items": {"$ref": "#/components/schemas/Citation"}}
        if name.startswith(("FndRecord", "FndEdit")): pr["sources"] = {"type": "array", "minItems": 1, "items": {"$ref": "#/components/schemas/Citation"}}
        if name.startswith("AcsSelectEvidence"): pr["items"] = {"type": "array", "minItems": 1, "maxItems": 200, "items": {"$ref": "#/components/schemas/SelectionItem"}}
```

## slc08_data.py

```python
# -*- coding: utf-8 -*-
# SLC-08 — Decision → Plan → Version → Baseline → Tasks (+ outcome measurement)
SLICE = "SLC-08"
AGGS = {}
def agg(id_, bc, name, tier, purpose, states, terminal, transitions, invariants, entities, reqs, notes=None, personal=False):
    AGGS[id_] = dict(id=id_, bc=bc, name=name, tier=tier, purpose=purpose, states=states, terminal=terminal,
                     transitions=transitions, invariants=invariants, entities=entities, requirements=reqs, notes=notes, personal_data=personal)

agg("AGG-DECISION-REQUEST","BC04","Decision Request","T2","طلب قرار بسؤال وخيارات وتقييمات مستشهد بها وسلطة مطلوبة",
 ["DRAFT","OPEN","DECIDED","WITHDRAWN"],["DECIDED","WITHDRAWN"],
 [("∅","CMD-DRQ-CREATE","DRAFT","question; required decision type (RD-DECISION-TYPES); scope unit; deadline; label","EVT-DRQ-CREATED","DECISION_REQUEST_INVALID"),
  (["DRAFT","OPEN"],"CMD-DRQ-ADD-OPTION","=","option text; expected impact; options ≤ 10","EVT-DRQ-OPTION-ADDED","DECISION_REQUEST_INVALID"),
  (["DRAFT","OPEN"],"CMD-DRQ-CITE","=","assessment or evidence visible; pinned URN + version; cited label ≤ request label","EVT-DRQ-CITED","CITATION_ABOVE_LABEL"),
  (["DRAFT"],"CMD-DRQ-OPEN","OPEN","≥ 2 options (one may be 'no action'); ≥ 1 citation (REQ-DEC-001, OUT-04)","EVT-DRQ-OPENED","DECISION_REQUEST_INCOMPLETE"),
  (["OPEN"],"SYS:deadline passed","=","escalates to holders of the required authority in scope","EVT-DRQ-ESCALATED",None),
  (["OPEN"],"SYS:decision recorded for this request","DECIDED","EVT-DEC-RECORDED references the request","EVT-DRQ-DECIDED",None),
  (["DRAFT","OPEN"],"CMD-DRQ-WITHDRAW","WITHDRAWN","reason","EVT-DRQ-WITHDRAWN","REASON_REQUIRED")],
 ["INV-DRQ-01: citations are pinned by version (INV-ASM-03)","INV-DRQ-02: request label ≥ labels of its citations","INV-DRQ-03: a request is decided by exactly one decision"],
 ["Option","Citation (pinned)"],["REQ-DEC-001"])

agg("AGG-DECISION","BC04","Decision","T2","قرار مسجل بسلطة مختصة وخيار ومبرر وسريان؛ غير قابل للتعديل",
 ["RECORDED","SUPERSEDED","ANNULLED"],["SUPERSEDED","ANNULLED"],
 [("∅","CMD-DEC-RECORD","RECORDED","AuthorityCheck(decider, decision type, scope, now) = authorized — grant chain stored as authority snapshot (BRL-003, REQ-DEC-002); request OPEN (or ad-hoc with rationale and ≥ 1 citation); selected option ∈ request options; rationale; effective_from ≥ now − 1 h; supersedes (optional) is RECORDED and same scope","EVT-DEC-RECORDED","AUTHORITY_REQUIRED"),
  (["RECORDED"],"SYS:superseding decision recorded","SUPERSEDED","new decision references this one in supersedes","EVT-DEC-SUPERSEDED",None),
  (["RECORDED"],"CMD-DEC-ANNUL","ANNULLED","recorded in error; actor holds authority for the same decision type at a higher scope; reason; plans implementing it are flagged","EVT-DEC-ANNULLED","AUTHORITY_REQUIRED")],
 ["INV-DEC-01: immutable after recording (REQ-DEC-004); changes are new decisions that supersede",
  "INV-DEC-02: authority snapshot (grant chain, delegation depth, limits) is stored and remains verifiable as-of recorded_at",
  "INV-DEC-03: every decision links to ≥ 1 assessment or evidence (REQ-DEC-003, OUT-04 target 100 %)",
  "INV-DEC-04: effective time and record time are distinct; retroactive effect limited to 1 h unless tenant policy allows longer"],
 ["AuthoritySnapshot","Citation (pinned)"],["REQ-DEC-002","REQ-DEC-003","REQ-DEC-004"])

agg("AGG-PLAN","BC04","Plan (identity)","T2","هوية الخطة ودورة حياتها؛ المحتوى في إصداراتها",
 ["DRAFT","ACTIVE","SUSPENDED","COMPLETED","CLOSED","CANCELLED"],["CLOSED","CANCELLED"],
 [("∅","CMD-PLN-CREATE","DRAFT","title; owner; org scope; implements ≥ 1 decision (RECORDED) or objective (REQ-OPS-002), or for plan_kind=CONTINGENCY a risk_ref or incident_ref trigger (CR-60, SLC-17); label ≥ implemented decisions or triggering scope's label","EVT-PLN-CREATED","PLAN_INVALID"),
  (["DRAFT"],"SYS:first version baselined","ACTIVE","EVT-PLV-BASELINED for this plan","EVT-PLN-ACTIVATED",None),
  (["ACTIVE"],"CMD-PLN-SUSPEND","SUSPENDED","reason; open tasks suspended (flag, INV-TASK-06)","EVT-PLN-SUSPENDED","REASON_REQUIRED"),
  (["SUSPENDED"],"CMD-PLN-RESUME","ACTIVE","reason; tasks unsuspended","EVT-PLN-RESUMED","REASON_REQUIRED"),
  (["ACTIVE"],"CMD-PLN-COMPLETE","COMPLETED","all plan tasks terminal; every outcome has ≥ 1 measurement","EVT-PLN-COMPLETED","PLAN_NOT_COMPLETABLE"),
  (["COMPLETED"],"CMD-PLN-CLOSE","CLOSED","after-action notes (optional in R1); outcome trackers closed","EVT-PLN-CLOSED",None),
  (["DRAFT","ACTIVE","SUSPENDED"],"CMD-PLN-CANCEL","CANCELLED","authority; reason; open tasks cancelled","EVT-PLN-CANCELLED","REASON_REQUIRED"),
  (["DRAFT","ACTIVE","SUSPENDED"],"CMD-PLN-RECLASSIFY","=","authority; new label ≥ implemented decisions; assignees without clearance → reassignment required","EVT-PLN-RECLASSIFIED","CLASSIFICATION_CHANGE_NOT_AUTHORIZED"),
  (["ACTIVE","SUSPENDED"],"SYS:implemented decision annulled or superseded","=","plan flagged for review (no automatic change)","EVT-PLN-REVIEW-FLAGGED",None)],
 ["INV-PLN-01: ACTIVE ⇔ exactly one BASELINED version exists","INV-PLN-02: a plan implements ≥ 1 decision or objective, or (plan_kind=CONTINGENCY) ≥ 1 risk or incident trigger (CR-60)",
  "INV-PLN-03: plan identity holds no content; content lives in versions (CR-29)",
  "INV-PLN-04: plan_kind ∈ {OPERATIONS, CONTINGENCY}, immutable after creation; only a CONTINGENCY plan may carry a triggered_by reference (CR-60, SLC-17)"],
 [],["REQ-OPS-001","REQ-OPS-002","REQ-OPS-003"])

agg("AGG-PLAN-VERSION","BC04","Plan Version","T2","محتوى الخطة: أهداف، نتائج، قيود، افتراضات، مراحل، أنشطة، معالم، جدول، اعتماديات، مقاييس",
 ["DRAFT","IN_REVIEW","BASELINED","SUPERSEDED","REJECTED","DISCARDED"],["SUPERSEDED","REJECTED","DISCARDED"],
 [("∅","CMD-PLV-DRAFT","DRAFT","plan not CLOSED/CANCELLED; new or revision copying the BASELINED version (activity ids preserved); ≤ 1 DRAFT/IN_REVIEW per plan","EVT-PLV-DRAFTED","DRAFT_EXISTS"),
  (["DRAFT"],"CMD-PLV-EDIT","=","objectives, outcomes (metric, unit, target, due), phases, activities (stable ids, task_generating flag, task type), milestones, schedule within plan window, acyclic dependencies","EVT-PLV-EDITED","PLAN_VERSION_INVALID"),
  (["DRAFT"],"CMD-PLV-SUBMIT","IN_REVIEW","complete per REQ-OPS-001; change classification computed vs current baseline (major/minor, BRL-005)","EVT-PLV-SUBMITTED","PLAN_VERSION_INCOMPLETE"),
  (["IN_REVIEW"],"CMD-PLV-RETURN","DRAFT","reviewer; reason","EVT-PLV-RETURNED","REASON_REQUIRED"),
  (["IN_REVIEW"],"CMD-PLV-APPROVE","BASELINED","approver ≠ author (REQ-OPS-005); AuthorityCheck(approver, plan-approval type, scope); previous BASELINED → SUPERSEDED in the same transaction; task synchronization started (SPEC-PLAN §3)","EVT-PLV-BASELINED","SEGREGATION_OF_DUTIES"),
  (["IN_REVIEW"],"CMD-PLV-REJECT","REJECTED","reason","EVT-PLV-REJECTED","REASON_REQUIRED"),
  (["BASELINED"],"CMD-PLV-AMEND-MINOR","=","only minor fields (descriptions, notes, attachments) per BRL-005; recorded as annotation, baseline content unchanged","EVT-PLV-MINOR-AMENDED","MAJOR_CHANGE_REQUIRES_VERSION"),
  (["BASELINED"],"SYS:newer version baselined","SUPERSEDED","system","EVT-PLV-SUPERSEDED",None),
  (["DRAFT"],"CMD-PLV-DISCARD","DISCARDED","author; reason","EVT-PLV-DISCARDED","REASON_REQUIRED")],
 ["INV-PLV-01: content is immutable from IN_REVIEW onwards; BASELINED content never changes (BRL-004, REQ-OPS-003)",
  "INV-PLV-02: exactly one BASELINED version per plan",
  "INV-PLV-03: activity ids are stable across versions, so task synchronization is a deterministic diff",
  "INV-PLV-04: a major change (objectives, outcomes, phases, milestone dates, resource commitments) is possible only through a new version (BRL-005)",
  "INV-PLV-05: dependencies acyclic; all dates inside the plan window"],
 ["Objective","Outcome (metric, unit, target, due)","Phase","Activity (stable id, task_generating, task_type)","Milestone","Dependency","ResourceNote (text, R1 — DEBT-001)"],
 ["REQ-OPS-001","REQ-OPS-003","REQ-OPS-004","REQ-OPS-005","REQ-OPS-014"],
 "CR-29 closed for Plan: the 14 components of PRJ§62 are version content (7 internal entity kinds, SL-24 ≤ 7).")

agg("AGG-OUTCOME-TRACKER","BC04","Outcome Tracker","T2","سلسلة قياسات لنتيجة خطة مقابل هدفها",
 ["ACTIVE","CLOSED"],["CLOSED"],
 [("∅","SYS:outcome baselined","ACTIVE","one tracker per (plan, outcome id); target copied from baseline","EVT-OUT-TRACKER-CREATED",None),
  (["ACTIVE"],"SYS:target changed by new baseline","=","target history appended (valid time = baseline time)","EVT-OUT-TARGET-CHANGED",None),
  (["ACTIVE"],"CMD-OUT-RECORD","=","value with unit convertible to metric unit (UCUM); measured_at; source = manual | task result | observation ref","EVT-OUT-MEASURED","MEASUREMENT_INVALID"),
  (["ACTIVE"],"CMD-OUT-CORRECT","=","corrects a measurement: previous record closed (recorded_to), corrected record added — no overwrite","EVT-OUT-MEASUREMENT-CORRECTED","REASON_REQUIRED"),
  (["ACTIVE"],"SYS:plan closed or cancelled","CLOSED","system","EVT-OUT-TRACKER-CLOSED",None)],
 ["INV-OUT-01: measurements are bitemporal records; corrections never overwrite","INV-OUT-02: progress = latest measurement known at K vs target valid at T"],
 ["Measurement (value, unit, measured_at, source, recorded_from/to)","TargetHistory"],["REQ-OPS-013"])

PERPETUAL = {}
QUERIES = [
 ("QRY-DRQ-GET","BC04","GET","/api/v1/operations/decision-requests/{request_id}","Request with options and pinned citations (withheld per policy)","label rule; required-authority holders in scope","REQ-DEC-001"),
 ("QRY-DRQ-LIST","BC04","GET","/api/v1/operations/decision-requests","My pending requests (as authority holder), by deadline","allowed_scope","REQ-DEC-001"),
 ("QRY-DEC-GET","BC04","GET","/api/v1/operations/decisions/{decision_id}","Decision with authority snapshot, citations (pinned) and supersession chain","label rule","REQ-DEC-003"),
 ("QRY-DEC-BASIS","BC04","GET","/api/v1/operations/decisions/{decision_id}/basis","What was known at decision time: cited assessments (pinned versions) and their key claims resolved known_at = decision.recorded_at","label rule; Auditor","REQ-DEC-003"),
 ("QRY-PLN-GET","BC04","GET","/api/v1/operations/plans/{plan_id}","Plan with current baseline, draft (if any), implemented decisions","label rule","REQ-OPS-001"),
 ("QRY-PLV-LIST","BC04","GET","/api/v1/operations/plans/{plan_id}/versions","Versions with states and times","label rule","REQ-OPS-003"),
 ("QRY-PLV-DIFF","BC04","GET","/api/v1/operations/plans/{plan_id}/versions/{version}/diff","Diff vs baseline with major/minor classification and task synchronization preview","label rule","REQ-OPS-004"),
 ("QRY-PLN-PROGRESS","BC04","GET","/api/v1/operations/plans/{plan_id}/progress","Tasks by activity and state, milestones, outcome progress vs targets","label rule; visible tasks only","REQ-OPS-013"),
 ("QRY-OUT-SERIES","BC04","GET","/api/v1/operations/plans/{plan_id}/outcomes/{outcome_id}/measurements","Measurement series as known_at","label rule","REQ-OPS-013"),
]
ACTORS = {"DRQ":"Analyst / Planner / Manager (create, add, cite, open, withdraw)","DEC":"authority holder (record) · higher authority (annul)",
          "PLN":"Planner / owner (create, suspend, resume, complete, close) · authority (cancel) · Security Officer (reclassify)",
          "PLV":"Planner (draft, edit, submit, discard, minor amend) · approver with plan-approval authority ≠ author (approve, return, reject)",
          "OUT":"Planner / owner (record, correct)"}
P = {
 "CMD-DRQ-CREATE":"question!:LocalizedName decision_type!:string scope!:urn deadline!:date-time context_refs:array label!:Label",
 "CMD-DRQ-ADD-OPTION":"text!:LocalizedName expected_impact:LocalizedName","CMD-DRQ-CITE":"citations!:array","CMD-DRQ-OPEN":"","CMD-DRQ-WITHDRAW":"reason!:string",
 "CMD-DEC-RECORD":"request:urn selected_option!:string rationale!:LocalizedName effective_from!:date-time citations:array supersedes:urn ad_hoc_reason:string label!:Label",
 "CMD-DEC-ANNUL":"reason!:string",
 "CMD-PLN-CREATE":"title!:LocalizedName owner!:urn org_scope!:urn implements:array plan_kind!:enum(OPERATIONS,CONTINGENCY) triggered_by:urn window!:Interval label!:Label","CMD-PLN-SUSPEND":"reason!:string","CMD-PLN-RESUME":"reason!:string",
 "CMD-PLN-COMPLETE":"note:string","CMD-PLN-CLOSE":"after_action_notes:LocalizedName","CMD-PLN-CANCEL":"reason!:string","CMD-PLN-RECLASSIFY":"label!:Label reason!:string",
 "CMD-PLV-DRAFT":"plan!:urn based_on:integer","CMD-PLV-EDIT":"objectives!:array outcomes!:array constraints:array assumptions:array phases!:array activities!:array milestones:array dependencies:array resource_notes:array",
 "CMD-PLV-SUBMIT":"","CMD-PLV-RETURN":"reason!:string","CMD-PLV-APPROVE":"note:string","CMD-PLV-REJECT":"reason!:string",
 "CMD-PLV-AMEND-MINOR":"annotations!:array","CMD-PLV-DISCARD":"reason!:string",
 "CMD-OUT-RECORD":"value!:number unit!:string measured_at!:date-time source!:enum(manual,task_result,observation) source_ref:urn note:string",
 "CMD-OUT-CORRECT":"measurement_id!:string value!:number unit!:string reason!:string",
}
SYSTEM_CMDS = set()
RESOURCE = {"AGG-DECISION-REQUEST":("operations","decision-requests"),"AGG-DECISION":("operations","decisions"),"AGG-PLAN":("operations","plans"),
            "AGG-PLAN-VERSION":("operations","plan-versions"),"AGG-OUTCOME-TRACKER":("operations","outcome-trackers")}
SECURITY_AFFECTING = {"EVT-PLN-RECLASSIFIED"}
CONSUMERS = {
 "AGG-DECISION":["Decision request (DECIDED)","Plans implementing it (review flag on supersede/annul)","Search projection (SLC-05)","Audit reports"],
 "AGG-PLAN-VERSION":["Task synchronizer (SPEC-PLAN §3)","Outcome trackers","Plan identity (activation)","Search projection (SLC-05)"],
 "AGG-PLAN":["Task synchronizer (suspend/cancel cascades)","Outcome trackers (close)","Notification (owners, assignees)"],
 "AGG-OUTCOME-TRACKER":["Plan progress view","Business telemetry (OUT-05)"],
 "default":["Search projection (SLC-05)"],
}


def enrich(spec, bc):
    S = spec["components"]["schemas"]
    S.update({
     "Citation": {"type": "object", "required": ["ref", "version"], "properties": {"ref": {"$ref": "#/components/schemas/Urn"}, "version": {"type": "integer"}, "kind": {"enum": ["assessment", "finding", "evidence", "claim"]}}},
     "Objective": {"type": "object", "required": ["id", "statement"], "properties": {"id": {"type": "string"}, "statement": {"$ref": "#/components/schemas/LocalizedName"}}},
     "PlanOutcome": {"type": "object", "required": ["id", "metric", "unit", "target", "due"], "properties": {"id": {"type": "string"}, "metric": {"type": "string"}, "unit": {"type": "string"}, "target": {"type": "number"}, "direction": {"enum": ["increase", "decrease", "reach"]}, "due": {"type": "string", "format": "date-time"}, "objective_ref": {"type": "string"}}},
     "Phase": {"type": "object", "required": ["id", "name", "window"], "properties": {"id": {"type": "string"}, "name": {"$ref": "#/components/schemas/LocalizedName"}, "window": {"$ref": "#/components/schemas/Interval"}}},
     "Activity": {"type": "object", "required": ["id", "phase_id", "name", "task_generating"], "properties": {"id": {"type": "string"}, "phase_id": {"type": "string"}, "name": {"$ref": "#/components/schemas/LocalizedName"}, "task_generating": {"type": "boolean"}, "task_type": {"$ref": "#/components/schemas/Urn"}, "org_scope": {"$ref": "#/components/schemas/Urn"}, "window": {"$ref": "#/components/schemas/Interval"}, "completion_criteria": {"type": "array", "items": {"type": "object"}}, "resource_note": {"type": "string"}}},
     "Milestone": {"type": "object", "required": ["id", "name", "date"], "properties": {"id": {"type": "string"}, "name": {"$ref": "#/components/schemas/LocalizedName"}, "date": {"type": "string", "format": "date-time"}, "activity_refs": {"type": "array", "items": {"type": "string"}}}},
     "PlanDependency": {"type": "object", "required": ["from", "to"], "properties": {"from": {"type": "string"}, "to": {"type": "string"}, "kind": {"enum": ["finish_to_start", "start_to_start"]}}},
    })
    for name, sch in S.items():
        if not name.endswith("Command") or "properties" not in sch: continue
        pr = sch["properties"]
        if "citations" in pr: pr["citations"] = {"type": "array", "items": {"$ref": "#/components/schemas/Citation"}}
        if name.startswith("PlvEdit"):
            for k, ref in [("objectives", "Objective"), ("outcomes", "PlanOutcome"), ("phases", "Phase"), ("activities", "Activity"), ("milestones", "Milestone"), ("dependencies", "PlanDependency")]:
                if k in pr: pr[k] = {"type": "array", "items": {"$ref": f"#/components/schemas/{ref}"}}
        if name.startswith("PlnCreate"): pr["implements"] = {"type": "array", "minItems": 1, "items": {"$ref": "#/components/schemas/Urn"}}
```

## slc09_data.py

```python
# -*- coding: utf-8 -*-
# SLC-09 — Assets, Resources, Allocation, Reservations, Readiness (R2)
SLICE = "SLC-09"
AGGS = {}
def agg(id_, bc, name, tier, purpose, states, terminal, transitions, invariants, entities, reqs, notes=None, personal=False):
    AGGS[id_] = dict(id=id_, bc=bc, name=name, tier=tier, purpose=purpose, states=states, terminal=terminal,
                     transitions=transitions, invariants=invariants, entities=entities, requirements=reqs, notes=notes, personal_data=personal)

agg("AGG-ASSET","BC05","Asset","T2 (location as T1 claims on the linked entity)","أصل مادي بملكية وحيازة وحالة وقدرات وشهادات وصيانة",
 ["IN_SERVICE","UNSERVICEABLE","UNDER_MAINTENANCE","LOST","DISPOSED"],["DISPOSED"],
 [("∅","CMD-AST-REGISTER","IN_SERVICE","type in RD-ASSET-TYPES; owner org; custody holder ACTIVE; linked information entity (entity_type asset-ref) created or referenced in BC02; capabilities; label","EVT-AST-REGISTERED","ASSET_INVALID"),
  (["IN_SERVICE","UNSERVICEABLE","UNDER_MAINTENANCE"],"CMD-AST-UPDATE-CONDITION","=","condition grade in RD-CONDITION-GRADES; inspector; unserviceable grades require CMD-AST-MARK-UNSERVICEABLE","EVT-AST-CONDITION-UPDATED","CONDITION_INVALID"),
  (["IN_SERVICE"],"CMD-AST-MARK-UNSERVICEABLE","UNSERVICEABLE","reason; active assignments are notified; future reservations flagged","EVT-AST-UNSERVICEABLE","REASON_REQUIRED"),
  (["IN_SERVICE","UNSERVICEABLE"],"CMD-AST-START-MAINTENANCE","UNDER_MAINTENANCE","maintenance order IN_PROGRESS for this asset","EVT-AST-MAINTENANCE-STARTED","MAINTENANCE_ORDER_REQUIRED"),
  (["UNDER_MAINTENANCE"],"CMD-AST-RETURN-TO-SERVICE","IN_SERVICE","maintenance order COMPLETED; condition serviceable; required certifications valid","EVT-AST-RETURNED-TO-SERVICE","ASSET_NOT_SERVICEABLE"),
  (["UNDER_MAINTENANCE"],"CMD-AST-FAIL-MAINTENANCE","UNSERVICEABLE","maintenance order COMPLETED with outcome failed; reason","EVT-AST-UNSERVICEABLE","REASON_REQUIRED"),
  (["IN_SERVICE","UNSERVICEABLE","UNDER_MAINTENANCE"],"CMD-AST-TRANSFER-CUSTODY","=","actor is current holder or custodian authority; new holder ACTIVE in scope; gapless chain","EVT-AST-CUSTODY-TRANSFERRED","CUSTODY_INVALID"),
  (["IN_SERVICE","UNSERVICEABLE","UNDER_MAINTENANCE"],"CMD-AST-SET-CERTIFICATION","=","certification code, issuer, valid_from/to; evidence","EVT-AST-CERTIFICATION-SET","CERTIFICATION_INVALID"),
  (["IN_SERVICE","UNSERVICEABLE"],"CMD-AST-REPORT-LOST","LOST","reason; active assignments ended; reservations cancelled","EVT-AST-REPORTED-LOST","REASON_REQUIRED"),
  (["LOST"],"CMD-AST-RECOVER","UNSERVICEABLE","found; inspection required before service","EVT-AST-RECOVERED",None),
  (["UNSERVICEABLE","LOST"],"CMD-AST-DISPOSE","DISPOSED","disposal authority (decision type asset-disposal); no active reservation or assignment; no legal hold","EVT-AST-DISPOSED","AUTHORITY_REQUIRED"),
  (["IN_SERVICE","UNSERVICEABLE","UNDER_MAINTENANCE","LOST"],"CMD-AST-RECLASSIFY","=","authority per policy","EVT-AST-RECLASSIFIED","CLASSIFICATION_CHANGE_NOT_AUTHORIZED")],
 ["INV-AST-01: available(asset, window) ⇔ IN_SERVICE ∧ required certifications valid throughout window ∧ no overlapping maintenance window, CONFIRMED/HELD reservation or ACTIVE assignment (REQ-RES-003/004/014)",
  "INV-AST-02: custody chain is gapless; each transfer by the current holder or custodian authority (REQ-RES-002)",
  "INV-AST-03: location lives as bitemporal claims on the linked information entity, never as a column (REQ-RES-005)",
  "INV-AST-04: an expired certification makes the asset unavailable for new assignments from that instant, evaluated at read time"],
 ["Certification","CustodyEntry","Capability (code, level)"],["REQ-RES-001","REQ-RES-002","REQ-RES-003","REQ-RES-005"])

agg("AGG-MAINTENANCE-ORDER","BC05","Maintenance Order","T2","أمر صيانة مجدول أو تصحيحي بنافذة زمنية تحجب التوفر",
 ["PLANNED","IN_PROGRESS","COMPLETED","CANCELLED"],["COMPLETED","CANCELLED"],
 [("∅","CMD-MNT-PLAN","PLANNED","asset not DISPOSED; kind ∈ {scheduled, corrective}; window; no overlap with another non-terminal order of the asset","EVT-MNT-PLANNED","MAINTENANCE_OVERLAP"),
  (["PLANNED"],"CMD-MNT-RESCHEDULE","=","new window without overlap; affected reservations flagged","EVT-MNT-RESCHEDULED","MAINTENANCE_OVERLAP"),
  (["PLANNED"],"CMD-MNT-START","IN_PROGRESS","technician; asset moves to UNDER_MAINTENANCE via its own command (policy)","EVT-MNT-STARTED",None),
  (["IN_PROGRESS"],"CMD-MNT-COMPLETE","COMPLETED","outcome ∈ {serviceable, failed}; work performed; parts consumed (optional allocation refs)","EVT-MNT-COMPLETED","OUTCOME_REQUIRED"),
  (["PLANNED"],"CMD-MNT-CANCEL","CANCELLED","reason","EVT-MNT-CANCELLED","REASON_REQUIRED")],
 ["INV-MNT-01: a PLANNED or IN_PROGRESS window blocks availability (INV-AST-01)","INV-MNT-02: no two non-terminal orders of one asset overlap"],
 [],["REQ-RES-004"],"Integration with an external CMMS goes through an adapter (R2-Q2).")

agg("AGG-ASSET-RESERVATION","BC05","Asset Reservation","T2","حجز أصل لنافذة زمنية قبل الاستخدام",
 ["HELD","CONFIRMED","RELEASED","EXPIRED","CANCELLED"],["RELEASED","EXPIRED","CANCELLED"],
 [("∅","CMD-RSV-HOLD","HELD","asset available for the window (INV-AST-01); purpose; requester authorized in asset owner scope","EVT-RSV-HELD","ASSET_RESERVED"),
  (["HELD"],"CMD-RSV-CONFIRM","CONFIRMED","linked to a task or plan activity","EVT-RSV-CONFIRMED","LINK_REQUIRED"),
  (["HELD"],"SYS:hold expiry (24 h) reached","EXPIRED","scheduler","EVT-RSV-EXPIRED",None),
  (["CONFIRMED"],"CMD-RSV-RELEASE","RELEASED","requester or linked task terminal","EVT-RSV-RELEASED",None),
  (["CONFIRMED"],"SYS:linked task or plan terminal","RELEASED","SLC-03/SLC-08 events","EVT-RSV-RELEASED",None),
  (["HELD","CONFIRMED"],"CMD-RSV-CANCEL","CANCELLED","requester or asset owner; reason","EVT-RSV-CANCELLED","REASON_REQUIRED")],
 ["INV-RSV-01: no two HELD/CONFIRMED reservations of one asset overlap in time (exclusion on (asset, window)) — REQ-RES-014",
  "INV-RSV-02: a HELD reservation expires after 24 h unless confirmed (W4 delegated decision)"],
 [],["REQ-RES-014"])

agg("AGG-ASSET-ASSIGNMENT","BC05","Asset Assignment","T2","استخدام فعلي لأصل في مهمة أو وحدة",
 ["ACTIVE","RETURNED","CANCELLED"],["RETURNED","CANCELLED"],
 [("∅","CMD-ASG-ASSIGN","ACTIVE","asset available (or covered by the caller's CONFIRMED reservation); asset certifications satisfy the task type's asset requirements; custody authorization; assignee cleared for asset label","EVT-ASG-ASSIGNED","ASSET_NOT_AVAILABLE"),
  (["ACTIVE"],"CMD-ASG-RETURN","RETURNED","condition report; asset condition updated accordingly","EVT-ASG-RETURNED","CONDITION_REPORT_REQUIRED"),
  (["ACTIVE"],"SYS:linked task terminal","RETURNED","condition report requested from last holder (follow-up task)","EVT-ASG-RETURNED",None),
  (["ACTIVE"],"CMD-ASG-CANCEL","CANCELLED","assigned in error; reason","EVT-ASG-CANCELLED","REASON_REQUIRED")],
 ["INV-ASG-01: at most one ACTIVE assignment per asset at a time","INV-ASG-02: assignment respects BRL-007 (asset certification and custody authorization)"],
 [],["REQ-RES-003","REQ-RES-012"])

agg("AGG-RESOURCE-POOL","BC05","Resource Pool","T2","مجمع موارد قابلة للعد أو القياس بسعة متغيرة زمنياً",
 ["ACTIVE","SUSPENDED","CLOSED"],["CLOSED"],
 [("∅","CMD-RPL-CREATE","ACTIVE","type in RD-RESOURCE-TYPES; unit (UCUM); org scope; initial capacity; label","EVT-RPL-CREATED","POOL_INVALID"),
  (["ACTIVE","SUSPENDED"],"CMD-RPL-ADJUST-CAPACITY","=","new capacity with valid_from; reason; a reduction below committed quantity requires pre-emption decisions first","EVT-RPL-CAPACITY-ADJUSTED","CAPACITY_BELOW_COMMITMENTS"),
  (["ACTIVE"],"CMD-RPL-SUSPEND","SUSPENDED","reason; no new allocations","EVT-RPL-SUSPENDED","REASON_REQUIRED"),
  (["SUSPENDED"],"CMD-RPL-RESUME","ACTIVE","—","EVT-RPL-RESUMED",None),
  (["ACTIVE","SUSPENDED"],"CMD-RPL-CLOSE","CLOSED","no COMMITTED or PENDING allocations","EVT-RPL-CLOSED","POOL_HAS_COMMITMENTS")],
 ["INV-RPL-01: capacity is a time series (valid_from); history kept (bitemporal record)",
  "INV-RPL-02: for every time bucket, Σ committed quantity ≤ capacity (enforced by the capacity ledger — SPEC-ALLOCATION §2)"],
 ["CapacitySeries","CapacityLedgerBucket (hour)"],["REQ-RES-006"])

agg("AGG-ALLOCATION","BC05","Resource Allocation","T2","التزام كمية من مجمع لمهمة أو نشاط في نافذة زمنية",
 ["REQUESTED","PENDING_APPROVAL","COMMITTED","REJECTED","PREEMPTED","RELEASED"],["REJECTED","PREEMPTED","RELEASED"],
 [("∅","CMD-ALC-REQUEST","REQUESTED","pool ACTIVE; quantity > 0 in pool unit; window; priority 1–5; target task/activity/logistics-request (CR-62, SLC-18); requester","EVT-ALC-REQUESTED","ALLOCATION_INVALID"),
  (["REQUESTED"],"SYS:all checks passed","COMMITTED","SPEC-ALLOCATION §1 checks + capacity ledger reserve in priority order (§2)","EVT-ALC-COMMITTED",None),
  (["REQUESTED"],"SYS:checks passed, policy requires approval","PENDING_APPROVAL","PDP obligation REQUIRE_APPROVAL; capacity provisionally held ≤ 1 h","EVT-ALC-APPROVAL-REQUIRED",None),
  (["REQUESTED"],"SYS:a check failed","REJECTED","reason codes per failed check","EVT-ALC-REJECTED",None),
  (["PENDING_APPROVAL"],"CMD-ALC-APPROVE","COMMITTED","approver with allocation authority ≠ requester; capacity still available","EVT-ALC-COMMITTED","CAPACITY_UNAVAILABLE"),
  (["PENDING_APPROVAL"],"CMD-ALC-REJECT","REJECTED","reason","EVT-ALC-REJECTED","REASON_REQUIRED"),
  (["PENDING_APPROVAL"],"SYS:provisional hold (1 h) elapsed","REJECTED","capacity released","EVT-ALC-REJECTED",None),
  (["COMMITTED"],"CMD-ALC-RECORD-CONSUMPTION","=","quantity in pool unit; time; consumption beyond commitment flagged (REQ-RES-010)","EVT-ALC-CONSUMED","CONSUMPTION_INVALID"),
  (["COMMITTED"],"CMD-ALC-PREEMPT","PREEMPTED","pre-emption decision (BC04 Decision) by an authority for the pool scope; higher-priority allocation reference; owners notified (REQ-RES-009)","EVT-ALC-PREEMPTED","AUTHORITY_REQUIRED"),
  (["COMMITTED"],"CMD-ALC-RELEASE","RELEASED","requester or task owner; unused quantity returned to the ledger","EVT-ALC-RELEASED",None),
  (["COMMITTED"],"SYS:linked task terminal","RELEASED","SLC-03 events (REQ-RES-011)","EVT-ALC-RELEASED",None)],
 ["INV-ALC-01: COMMITTED quantity is reserved in the capacity ledger for every hour of its window; release returns the unused part",
  "INV-ALC-02: contention is resolved by priority, then request time, inside each pool's ordering window (SPEC-ALLOCATION §2)",
  "INV-ALC-03: pre-emption only through a recorded decision with authority; never automatic",
  "INV-ALC-04: approver ≠ requester when approval is required"],
 ["CheckResult","ConsumptionRecord"],["REQ-RES-007","REQ-RES-008","REQ-RES-009","REQ-RES-010","REQ-RES-011","REQ-RES-012"])

agg("AGG-ROLE-REQUIREMENT","BC05","Role Requirement","T2","متطلبات جاهزية دور: كفاءات، مؤهلات، شهادات، تدريب حديث، خبرة",
 ["DRAFT","ACTIVE","RETIRED"],["RETIRED"],
 [("∅","CMD-RRQ-DEFINE","DRAFT","role exists (BC01); requirements reference RD-COMPETENCIES","EVT-RRQ-DEFINED","ROLE_REQUIREMENT_INVALID"),
  (["DRAFT","ACTIVE"],"CMD-RRQ-EDIT","=","requirements valid; ACTIVE → new version","EVT-RRQ-EDITED","ROLE_REQUIREMENT_INVALID"),
  (["DRAFT"],"CMD-RRQ-ACTIVATE","ACTIVE","approver ≠ author","EVT-RRQ-ACTIVATED","SEGREGATION_OF_DUTIES"),
  (["ACTIVE"],"CMD-RRQ-RETIRE","RETIRED","reason","EVT-RRQ-RETIRED","REASON_REQUIRED")],
 ["INV-RRQ-01: one ACTIVE requirement set per role","INV-RRQ-02: readiness is computed at a time t from records valid at t (as-of readiness)"],
 ["Requirement (kind, code, min_level, recency)"],["REQ-RES-013"])

PERPETUAL = {}
QUERIES = [
 ("QRY-AST-GET","BC05","GET","/api/v1/readiness/assets/{asset_id}","Asset with status, condition, certifications, custody chain, linked entity","label rule","REQ-RES-001"),
 ("QRY-AST-AVAILABILITY","BC05","POST","/api/v1/readiness/asset-availability-queries","Assets of type/capability available in a window (and optional bbox), with blocking reasons for others visible to caller","allowed_scope","REQ-RES-003"),
 ("QRY-MNT-SCHEDULE","BC05","GET","/api/v1/readiness/maintenance-orders","Maintenance orders by asset, window, state","asset owner scope","REQ-RES-004"),
 ("QRY-POL-TIMELINE","BC05","GET","/api/v1/readiness/resource-pools/{pool_id}/timeline","Capacity, committed and available quantity per hour in a window","pool scope","REQ-RES-006"),
 ("QRY-ALC-LIST","BC05","GET","/api/v1/readiness/allocations","Allocations by pool, task, plan, state","scope","REQ-RES-007"),
 ("QRY-READINESS","BC05","POST","/api/v1/readiness/readiness-checks","Readiness of a person or unit for a role at time t, with gaps","Manager / Training Manager in scope; self","REQ-RES-013"),
]
ACTORS = {"AST":"Resource Manager (register, condition, custody, certification, lost) · disposal authority (dispose) · Security Officer (reclassify)",
 "MNT":"Resource Manager / technician","RSV":"Planner / Resource Manager","ASG":"Resource Manager / Planner","RPL":"Resource Manager",
 "ALC":"Planner (request, release) · allocation authority (approve, reject, pre-empt) · task assignee (consumption)","RRQ":"Training Manager / Administrator"}
P = {
 "CMD-AST-REGISTER":"asset_type!:string name!:LocalizedName owner_org!:urn custody_holder!:urn linked_entity:urn capabilities!:array serial:string label!:Label",
 "CMD-AST-UPDATE-CONDITION":"grade!:string inspector!:urn notes:string","CMD-AST-MARK-UNSERVICEABLE":"reason!:string","CMD-AST-START-MAINTENANCE":"maintenance_order!:urn",
 "CMD-AST-RETURN-TO-SERVICE":"maintenance_order!:urn","CMD-AST-FAIL-MAINTENANCE":"maintenance_order!:urn reason!:string","CMD-AST-TRANSFER-CUSTODY":"new_holder!:urn reason!:string",
 "CMD-AST-SET-CERTIFICATION":"code!:string issuer!:string valid_from!:date-time valid_to!:date-time evidence:urn","CMD-AST-REPORT-LOST":"reason!:string",
 "CMD-AST-RECOVER":"note:string","CMD-AST-DISPOSE":"decision!:urn reason!:string","CMD-AST-RECLASSIFY":"label!:Label reason!:string",
 "CMD-MNT-PLAN":"asset!:urn kind!:enum(scheduled,corrective) window!:Interval description!:LocalizedName","CMD-MNT-RESCHEDULE":"window!:Interval reason!:string",
 "CMD-MNT-START":"technician!:urn","CMD-MNT-COMPLETE":"outcome!:enum(serviceable,failed) work!:LocalizedName parts:array","CMD-MNT-CANCEL":"reason!:string",
 "CMD-RSV-HOLD":"asset!:urn window!:Interval purpose!:string label!:Label","CMD-RSV-CONFIRM":"link!:urn","CMD-RSV-RELEASE":"note:string","CMD-RSV-CANCEL":"reason!:string",
 "CMD-ASG-ASSIGN":"asset!:urn task:urn unit:urn window!:Interval reservation:urn","CMD-ASG-RETURN":"condition_report!:object","CMD-ASG-CANCEL":"reason!:string",
 "CMD-RPL-CREATE":"resource_type!:string name!:LocalizedName unit!:string org_scope!:urn capacity!:number label!:Label",
 "CMD-RPL-ADJUST-CAPACITY":"capacity!:number valid_from!:date-time reason!:string","CMD-RPL-SUSPEND":"reason!:string","CMD-RPL-RESUME":"","CMD-RPL-CLOSE":"reason!:string",
 "CMD-ALC-REQUEST":"pool!:urn quantity!:number window!:Interval priority!:integer target!:urn justification:string","CMD-ALC-APPROVE":"note:string","CMD-ALC-REJECT":"reason!:string",
 "CMD-ALC-RECORD-CONSUMPTION":"quantity!:number at!:date-time note:string","CMD-ALC-PREEMPT":"decision!:urn preempting_allocation!:urn","CMD-ALC-RELEASE":"note:string",
 "CMD-RRQ-DEFINE":"role!:urn requirements!:array","CMD-RRQ-EDIT":"requirements!:array","CMD-RRQ-ACTIVATE":"","CMD-RRQ-RETIRE":"reason!:string",
}
SYSTEM_CMDS = set()
RESOURCE = {"AGG-ASSET":("readiness","assets"),"AGG-MAINTENANCE-ORDER":("readiness","maintenance-orders"),"AGG-ASSET-RESERVATION":("readiness","asset-reservations"),
 "AGG-ASSET-ASSIGNMENT":("readiness","asset-assignments"),"AGG-RESOURCE-POOL":("readiness","resource-pools"),"AGG-ALLOCATION":("readiness","allocations"),
 "AGG-ROLE-REQUIREMENT":("readiness","role-requirements")}
SECURITY_AFFECTING = {"EVT-AST-RECLASSIFIED"}
CONSUMERS = {"AGG-ASSET":["Availability view","Situation assets layer (SLC-06)","Search projection (SLC-05)","Reservations/assignments (flags)"],
 "AGG-ALLOCATION":["Capacity ledger","Task (SLC-03) notifications","Plan progress (SLC-08)"],"AGG-MAINTENANCE-ORDER":["Asset (start/return via policy)","Availability view"],
 "AGG-ASSET-RESERVATION":["Availability view"],"AGG-ASSET-ASSIGNMENT":["Availability view","Task (SLC-03)"],"AGG-RESOURCE-POOL":["Capacity ledger"],
 "AGG-ROLE-REQUIREMENT":["Readiness evaluator","Eligibility cache"],"default":["Search projection (SLC-05)"]}
CTX_OVERRIDE = {}

def enrich(spec, bc):
    S = spec["components"]["schemas"]
    S["Capability"] = {"type": "object", "required": ["code"], "properties": {"code": {"type": "string"}, "level": {"type": "integer"}}}
    S["RoleRequirementItem"] = {"type": "object", "required": ["kind", "code"], "properties": {"kind": {"enum": ["competency", "qualification", "certification", "training_recency", "experience"]},
        "code": {"type": "string"}, "min_level": {"type": "integer"}, "recency": {"type": "string", "description": "ISO 8601 duration"}, "min_experience": {"type": "string"}}}
    S["AvailabilityQuery"] = {"type": "object", "required": ["window"], "properties": {"asset_types": {"type": "array", "items": {"type": "string"}},
        "capabilities": {"type": "array", "items": {"$ref": "#/components/schemas/Capability"}}, "window": {"$ref": "#/components/schemas/Interval"}, "bbox": {"type": "array", "items": {"type": "number"}, "minItems": 4, "maxItems": 4}}}
    S["ReadinessQuery"] = {"type": "object", "required": ["subject", "role", "at"], "properties": {"subject": {"$ref": "#/components/schemas/Urn"}, "role": {"$ref": "#/components/schemas/Urn"}, "at": {"type": "string", "format": "date-time"}}}
    for name, sch in S.items():
        if not name.endswith("Command") or "properties" not in sch: continue
        pr = sch["properties"]
        if name.startswith("AstRegister"): pr["capabilities"] = {"type": "array", "items": {"$ref": "#/components/schemas/Capability"}}
        if name.startswith(("RrqDefine", "RrqEdit")): pr["requirements"] = {"type": "array", "minItems": 1, "items": {"$ref": "#/components/schemas/RoleRequirementItem"}}
        if name.startswith("AlcRequest"): pr["priority"] = {"type": "integer", "minimum": 1, "maximum": 5}
    P = spec["paths"]
    P["/api/v1/readiness/asset-availability-queries"]["post"]["requestBody"] = {"required": True, "content": {"application/json": {"schema": {"$ref": "#/components/schemas/AvailabilityQuery"}}}}
    P["/api/v1/readiness/readiness-checks"]["post"]["requestBody"] = {"required": True, "content": {"application/json": {"schema": {"$ref": "#/components/schemas/ReadinessQuery"}}}}
```

## slc10_data.py

```python
# -*- coding: utf-8 -*-
# SLC-10 — Grounded AI (R2)
SLICE = "SLC-10"
AGGS = {}
def agg(id_, bc, name, tier, purpose, states, terminal, transitions, invariants, entities, reqs, notes=None, personal=False):
    AGGS[id_] = dict(id=id_, bc=bc, name=name, tier=tier, purpose=purpose, states=states, terminal=terminal,
                     transitions=transitions, invariants=invariants, entities=entities, requirements=reqs, notes=notes, personal_data=personal)

agg("AGG-AI-REQUEST","BC07","AI Request","T1 (when its output is used) / T2","طلب ذكاء اصطناعي واحد بمساره الكامل: سياسة، استرجاع مصرّح، حزمة سياق، نموذج، تأريض",
 ["RECEIVED","RETRIEVING","GENERATING","COMPLETED","INSUFFICIENT_EVIDENCE","REFUSED","FAILED","CANCELLED"],["COMPLETED","INSUFFICIENT_EVIDENCE","REFUSED","FAILED","CANCELLED"],
 [("∅","CMD-AIR-SUBMIT","RECEIVED","operation ∈ AI autonomy matrix and allowed at the tenant's routing; user authenticated; purpose; input size ≤ limit; per-tenant AI quota","EVT-AIR-RECEIVED","AI_OPERATION_NOT_ALLOWED"),
  (["RECEIVED"],"SYS:policy denied","REFUSED","PDP on (user, ai.<operation>, scope) denied or AIL above matrix","EVT-AIR-REFUSED",None),
  (["RECEIVED"],"SYS:retrieval started","RETRIEVING","authorized hybrid retrieval as the user (SPEC-AI §2)","EVT-AIR-RETRIEVING",None),
  (["RETRIEVING"],"SYS:context package sealed","GENERATING","context items pinned (URN + version/known_at + label); package hash; token budget respected","EVT-AIR-CONTEXT-SEALED",None),
  (["RETRIEVING"],"SYS:no sufficient evidence retrieved","INSUFFICIENT_EVIDENCE","coverage below threshold (SPEC-AI §4)","EVT-AIR-INSUFFICIENT-EVIDENCE",None),
  (["GENERATING"],"SYS:output grounded","COMPLETED","every statement cites ≥ 1 context item; citation check passed; output label = max(context labels); guard checks passed (SPEC-AI §5)","EVT-AIR-COMPLETED",None),
  (["GENERATING"],"SYS:output not grounded","INSUFFICIENT_EVIDENCE","ungrounded statements removed leave no answer","EVT-AIR-INSUFFICIENT-EVIDENCE",None),
  (["RETRIEVING","GENERATING"],"SYS:error or timeout","FAILED","error recorded","EVT-AIR-FAILED",None),
  (["RECEIVED","RETRIEVING","GENERATING"],"CMD-AIR-CANCEL","CANCELLED","requester","EVT-AIR-CANCELLED",None)],
 ["INV-AIR-01: the context package contains only items the requesting user may see at request time (REQ-AI-002)",
  "INV-AIR-02: retrieved content is data: it can never add tools, change recipients, widen scope or raise AIL (REQ-AI-012)",
  "INV-AIR-03: every COMPLETED statement has ≥ 1 citation to a context item (REQ-AI-004)",
  "INV-AIR-04: request, context package hash, model version, prompt template version and output are recorded (REQ-AI-001, BRL-009)",
  "INV-AIR-05: classified context never goes to an external model (REQ-AI-011)"],
 ["ContextPackage (items, hash)","ContextItem (urn, version, known_at, label, score)","Statement (text, citations)","GuardResult"],
 ["REQ-AI-001","REQ-AI-002","REQ-AI-003","REQ-AI-004","REQ-AI-007","REQ-AI-008","REQ-AI-011","REQ-AI-012"])

agg("AGG-AI-RESULT","BC07","AI Result (reviewable)","T1","مخرج AI يحتاج مراجعة بشرية قبل أن يؤثر: مسودة، استخراج، ترجمة كدليل، اقتراح مطابقة",
 ["PROPOSED","UNDER_REVIEW","ACCEPTED","PARTIALLY_ACCEPTED","REJECTED"],["ACCEPTED","PARTIALLY_ACCEPTED","REJECTED"],
 [("∅","SYS:request COMPLETED for a reviewable operation","PROPOSED","operation ∈ {AI-OP-03 draft, AI-OP-04 extract, AI-OP-05 translation used as evidence, AI-OP-06 match suggestion}","EVT-AIRS-PROPOSED",None),
  (["PROPOSED"],"CMD-AIRS-START-REVIEW","UNDER_REVIEW","reviewer authorized for the target and cleared for the result label","EVT-AIRS-REVIEW-STARTED","REVIEWER_NOT_CLEARED"),
  (["UNDER_REVIEW"],"CMD-AIRS-ACCEPT","ACCEPTED","effects applied through owner commands as the reviewer, with agent = model version in lineage (e.g. CMD-CLM-ASSERT, product section, CMD-ER-PROPOSE)","EVT-AIRS-ACCEPTED","OWNER_REJECTED"),
  (["UNDER_REVIEW"],"CMD-AIRS-ACCEPT-PARTIALLY","PARTIALLY_ACCEPTED","selected items only; rejected items recorded with reasons","EVT-AIRS-PARTIALLY-ACCEPTED","OWNER_REJECTED"),
  (["PROPOSED","UNDER_REVIEW"],"CMD-AIRS-REJECT","REJECTED","reason (feeds evaluation)","EVT-AIRS-REJECTED","REASON_REQUIRED")],
 ["INV-AIRS-01: no AI result changes business state without an accepting human (AIL ≤ 3 in R2; REQ-AI-005/006/008)",
  "INV-AIRS-02: accepted effects keep lineage to request, context package and model version",
  "INV-AIRS-03: review outcomes are fed to the evaluation data set (human feedback)"],
 ["ResultItem (kind, payload, citations, decision)"],["REQ-AI-005","REQ-AI-006","REQ-AI-008"])

agg("AGG-MODEL-VERSION","BC07","Model Version","T2","نسخة نموذج بدورة حياة من التسجيل حتى التقاعد (PRJ§30)",
 ["REGISTERED","EVALUATING","EVALUATION_FAILED","APPROVED","STAGED","PRODUCTION","DEPRECATED","RETIRED"],["EVALUATION_FAILED","RETIRED"],
 [("∅","CMD-MDL-REGISTER","REGISTERED","family, version, weights digest in internal registry, licence reviewed, languages (must include ar and en for generative roles), context size, hosting ∈ {local, external_allowed}","EVT-MDL-REGISTERED","MODEL_INVALID"),
  (["REGISTERED"],"CMD-MDL-START-EVALUATION","EVALUATING","evaluation suite ACTIVE (AGG-EVAL-SUITE)","EVT-MDL-EVALUATION-STARTED","SUITE_NOT_ACTIVE"),
  (["EVALUATING"],"CMD-MDL-APPROVE","APPROVED","report meets thresholds: citation accuracy ≥ 95 %, hallucination ≤ 2 %, insufficient-evidence recall ≥ 95 %, 0 injection/exfiltration successes, latency and cost recorded (REQ-AI-010); AI governance authority ≠ registrar","EVT-MDL-APPROVED","EVALUATION_BELOW_THRESHOLD"),
  (["EVALUATING"],"CMD-MDL-FAIL-EVALUATION","EVALUATION_FAILED","report attached","EVT-MDL-EVALUATION-FAILED",None),
  (["APPROVED"],"CMD-MDL-STAGE","STAGED","canary share ≤ 10 % of the target operations","EVT-MDL-STAGED",None),
  (["STAGED"],"CMD-MDL-PROMOTE","PRODUCTION","canary metrics within thresholds for ≥ 7 days; approver ≠ stager","EVT-MDL-PROMOTED","CANARY_BELOW_THRESHOLD"),
  (["PRODUCTION"],"SYS:monitoring drift detected","=","weekly evaluation sample below threshold → alert, route review","EVT-MDL-DRIFT-DETECTED",None),
  (["PRODUCTION","STAGED","APPROVED"],"CMD-MDL-DEPRECATE","DEPRECATED","reason; routes using it must be switched first","EVT-MDL-DEPRECATED","MODEL_IN_ACTIVE_ROUTE"),
  (["DEPRECATED"],"CMD-MDL-REINSTATE","PRODUCTION","rollback; evaluation ≤ 90 days old","EVT-MDL-REINSTATED","EVALUATION_TOO_OLD"),
  (["DEPRECATED"],"CMD-MDL-RETIRE","RETIRED","weights archived (cold) if referenced by lineage of accepted results; record kept","EVT-MDL-RETIRED",None)],
 ["INV-MDL-01: only PRODUCTION versions serve production routes; STAGED serves canary share only",
  "INV-MDL-02: approval needs an evaluation report meeting thresholds; approver ≠ registrar (REQ-AI-010)",
  "INV-MDL-03: model records are never deleted; lineage always resolves the model version"],
 ["EvaluationReport","CanaryMetrics"],["REQ-AI-009","REQ-AI-010"])

agg("AGG-AI-ROUTING","BC07","AI Routing Configuration","T2","ربط كل عملية AI بنموذج إنتاجي وقالب تعليمات وحدود الاستقلالية لكل مستأجر",
 ["DRAFT","ACTIVE","SUPERSEDED","DISCARDED"],["SUPERSEDED","DISCARDED"],
 [("∅","CMD-RTG-DRAFT","DRAFT","AI governance authority; ≤ 1 DRAFT per tenant","EVT-RTG-DRAFTED","DRAFT_EXISTS"),
  (["DRAFT"],"CMD-RTG-EDIT","=","for each operation: model version in PRODUCTION (or STAGED with canary share), prompt template version, allowed tools, max AIL ≤ autonomy matrix, external model allowed only for unclassified and only if tenant policy allows","EVT-RTG-EDITED","ROUTING_INVALID"),
  (["DRAFT"],"CMD-RTG-ACTIVATE","ACTIVE","approver ≠ author; previous ACTIVE → SUPERSEDED","EVT-RTG-ACTIVATED","SEGREGATION_OF_DUTIES"),
  (["DRAFT"],"CMD-RTG-DISCARD","DISCARDED","reason","EVT-RTG-DISCARDED","REASON_REQUIRED"),
  (["ACTIVE"],"SYS:successor activated","SUPERSEDED","system","EVT-RTG-SUPERSEDED",None)],
 ["INV-RTG-01: max AIL per operation never exceeds the platform autonomy matrix (AIL5 unreachable) — REQ-AI-008",
  "INV-RTG-02: prompt templates are versioned and immutable once referenced",
  "INV-RTG-03: exactly one ACTIVE routing per tenant"],
 ["Route (operation, model version, prompt template, tools, max AIL, external_allowed)"],["REQ-AI-008","REQ-AI-011"])

agg("AGG-AI-TOOL","BC07","AI Tool","T2","أداة يمكن لتشغيل AI استدعاؤها، بصلاحية وأثر ومستوى استقلالية",
 ["DRAFT","ACTIVE","DISABLED","RETIRED"],["RETIRED"],
 [("∅","CMD-TOL-REGISTER","DRAFT","name; input JSON schema; underlying platform query or command; effect ∈ {read, propose}; required permission; max AIL","EVT-TOL-REGISTERED","TOOL_INVALID"),
  (["DRAFT"],"CMD-TOL-ACTIVATE","ACTIVE","security review passed (injection, exfiltration, scope); approver = Security Officer","EVT-TOL-ACTIVATED","SECURITY_REVIEW_REQUIRED"),
  (["ACTIVE"],"CMD-TOL-DISABLE","DISABLED","reason","EVT-TOL-DISABLED","REASON_REQUIRED"),
  (["DISABLED"],"CMD-TOL-ENABLE","ACTIVE","—","EVT-TOL-ENABLED",None),
  (["DRAFT","ACTIVE","DISABLED"],"CMD-TOL-RETIRE","RETIRED","reason","EVT-TOL-RETIRED","REASON_REQUIRED")],
 ["INV-TOL-01: in R2 no tool has effect 'write'; 'propose' tools create AI results for human review only (REQ-AI-013, INV-AIRS-01)",
  "INV-TOL-02: a tool executes with the requesting user's authority through the platform's own query/command APIs",
  "INV-TOL-03: tools cannot reach external networks (FIT-12)"],
 [],["REQ-AI-013","REQ-AI-012"])

agg("AGG-EVAL-SUITE","BC07","Evaluation Suite","T2","مجموعات تقييم مُصدرة: تأريض، استشهاد، أدلة غير كافية، حقن، تسريب، عربي/إنجليزي",
 ["DRAFT","ACTIVE","SUPERSEDED"],["SUPERSEDED"],
 [("∅","CMD-EVS-DRAFT","DRAFT","AI governance","EVT-EVS-DRAFTED",None),
  (["DRAFT"],"CMD-EVS-EDIT","=","sets: groundedness (≥ 500 items), citation, insufficient-evidence, prompt-injection, exfiltration, cross-tenant, Arabic/English/mixed; each item labelled with expected behaviour","EVT-EVS-EDITED","SUITE_INVALID"),
  (["DRAFT"],"CMD-EVS-ACTIVATE","ACTIVE","approver ≠ author; previous ACTIVE → SUPERSEDED","EVT-EVS-ACTIVATED","SEGREGATION_OF_DUTIES"),
  (["ACTIVE"],"SYS:successor activated","SUPERSEDED","system","EVT-EVS-SUPERSEDED",None)],
 ["INV-EVS-01: suites are immutable once ACTIVE; every evaluation report names its suite version",
  "INV-EVS-02: suites include tenant samples before a model serves that tenant (RSK-021 analogue for AI)"],
 ["EvalItem (set, input, expected, labels)"],["REQ-AI-010"])

PERPETUAL = {}
QUERIES = [
 ("QRY-AIR-GET","BC07","GET","/api/v1/ai/requests/{request_id}","Request with answer, statements and citations (visible only), status","requester; Auditor (metadata)","REQ-AI-001"),
 ("QRY-AIR-CONTEXT","BC07","GET","/api/v1/ai/requests/{request_id}/context","Context package items (URN, version, label) — for audit and review","requester if cleared; Auditor","REQ-AI-002"),
 ("QRY-AIRS-QUEUE","BC07","GET","/api/v1/ai/results","Reviewable AI results by state, operation, target","reviewers authorized on targets","REQ-AI-005"),
 ("QRY-MDL-LIST","BC07","GET","/api/v1/ai/models","Model versions with state, evaluation summary, hosting","AI governance, Auditor","REQ-AI-009"),
 ("QRY-RTG-ACTIVE","BC07","GET","/api/v1/ai/routing","Active routing for the tenant","AI governance, Security Officer","REQ-AI-008"),
 ("QRY-TOL-LIST","BC07","GET","/api/v1/ai/tools","Tool registry","AI governance, Security Officer","REQ-AI-013"),
 ("QRY-AI-USAGE","BC07","GET","/api/v1/ai/usage","GPU-hours, requests, cost indicators per tenant and operation","Administrator, finance","REQ-AI-001"),
]
ACTORS = {"AIR":"any authorized user (submit, cancel)","AIRS":"reviewer authorized on the target (review, accept, reject)",
 "MDL":"AI platform engineer (register, evaluate, stage, deprecate) · AI governance authority (approve, promote, reinstate)","RTG":"AI governance authority (draft, edit) · second authority (activate)",
 "TOL":"AI platform engineer (register) · Security Officer (activate, disable)","EVS":"AI governance (draft, edit) · second authority (activate)"}
P = {
 "CMD-AIR-SUBMIT":"operation!:string input!:LocalizedName scope:object purpose!:string target:urn","CMD-AIR-CANCEL":"",
 "CMD-AIRS-START-REVIEW":"","CMD-AIRS-ACCEPT":"note:string","CMD-AIRS-ACCEPT-PARTIALLY":"accepted_items!:array rejected_items!:array","CMD-AIRS-REJECT":"reason!:string",
 "CMD-MDL-REGISTER":"family!:string version!:string weights_digest!:string licence!:string languages!:array context_tokens!:integer hosting!:enum(local,external_allowed) roles!:array",
 "CMD-MDL-START-EVALUATION":"suite!:urn","CMD-MDL-APPROVE":"report!:urn","CMD-MDL-FAIL-EVALUATION":"report!:urn","CMD-MDL-STAGE":"canary_share!:number operations!:array",
 "CMD-MDL-PROMOTE":"canary_report!:urn","CMD-MDL-DEPRECATE":"reason!:string","CMD-MDL-REINSTATE":"reason!:string","CMD-MDL-RETIRE":"reason!:string",
 "CMD-RTG-DRAFT":"based_on:urn","CMD-RTG-EDIT":"routes!:array","CMD-RTG-ACTIVATE":"","CMD-RTG-DISCARD":"reason!:string",
 "CMD-TOL-REGISTER":"name!:string description!:LocalizedName input_schema!:object binding!:string effect!:enum(read,propose) permission!:string max_ail!:integer",
 "CMD-TOL-ACTIVATE":"review_ref!:string","CMD-TOL-DISABLE":"reason!:string","CMD-TOL-ENABLE":"","CMD-TOL-RETIRE":"reason!:string",
 "CMD-EVS-DRAFT":"based_on:urn","CMD-EVS-EDIT":"sets!:array","CMD-EVS-ACTIVATE":"",
}
SYSTEM_CMDS = set()
RESOURCE = {"AGG-AI-REQUEST":("ai","requests"),"AGG-AI-RESULT":("ai","results"),"AGG-MODEL-VERSION":("ai","models"),
 "AGG-AI-ROUTING":("ai","routings"),"AGG-AI-TOOL":("ai","tools"),"AGG-EVAL-SUITE":("ai","evaluation-suites")}
SECURITY_AFFECTING = {"EVT-RTG-ACTIVATED","EVT-TOL-DISABLED","EVT-TOL-ACTIVATED"}
CONSUMERS = {"AGG-AI-REQUEST":["AI result creator (reviewable operations)","Usage accounting","Audit (encrypted prompt/output log)"],
 "AGG-AI-RESULT":["Owner contexts (effects on acceptance)","Evaluation feedback store"],"AGG-MODEL-VERSION":["Inference servers (load/unload)","Routing validation"],
 "AGG-AI-ROUTING":["Model router","PEP cache"],"AGG-AI-TOOL":["Tool gateway"],"AGG-EVAL-SUITE":["Evaluation runner"],"default":["Audit"]}
CTX_OVERRIDE = {"BC07": ("ai", "AI")}

def enrich(spec, bc):
    S = spec["components"]["schemas"]
    S["Route"] = {"type": "object", "required": ["operation", "model", "prompt_template", "max_ail"], "properties": {"operation": {"type": "string", "description": "AI-OP-* from autonomy matrix"},
        "model": {"$ref": "#/components/schemas/Urn"}, "prompt_template": {"type": "string"}, "allowed_tools": {"type": "array", "items": {"type": "string"}},
        "max_ail": {"type": "integer", "minimum": 0, "maximum": 4}, "external_allowed": {"type": "boolean", "default": False}}}
    S["EvalSet"] = {"type": "object", "required": ["kind", "items_ref"], "properties": {"kind": {"enum": ["groundedness", "citation", "insufficient_evidence", "prompt_injection", "exfiltration", "cross_tenant", "language"]},
        "items_ref": {"$ref": "#/components/schemas/Urn"}, "size": {"type": "integer", "minimum": 1}}}
    for name, sch in S.items():
        if not name.endswith("Command") or "properties" not in sch: continue
        pr = sch["properties"]
        if name.startswith("RtgEdit"): pr["routes"] = {"type": "array", "minItems": 1, "items": {"$ref": "#/components/schemas/Route"}}
        if name.startswith("EvsEdit"): pr["sets"] = {"type": "array", "minItems": 1, "items": {"$ref": "#/components/schemas/EvalSet"}}
        if name.startswith("TolRegister"): pr["max_ail"] = {"type": "integer", "minimum": 0, "maximum": 3}
        if name.startswith("MdlStage"): pr["canary_share"] = {"type": "number", "minimum": 0, "maximum": 0.1}
```

## slc11_data.py

```python
# -*- coding: utf-8 -*-
# SLC-11 — Offline field capture & synchronization (ADR-P09)
SLICE = "SLC-11"
AGGS = {}
def agg(id_, bc, name, tier, purpose, states, terminal, transitions, invariants, entities, reqs, notes=None, personal=False):
    AGGS[id_] = dict(id=id_, bc=bc, name=name, tier=tier, purpose=purpose, states=states, terminal=terminal,
                     transitions=transitions, invariants=invariants, entities=entities, requirements=reqs, notes=notes, personal_data=personal)

agg("AGG-DEVICE","BC01","Field Device","T2","جهاز ميداني مسجل ومربوط بمستخدم ومفتاح",
 ["PENDING_ENROLLMENT","ACTIVE","SUSPENDED","LOST","WIPED","RETIRED"],["WIPED","RETIRED"],
 [("∅","CMD-DEV-ENROLL","PENDING_ENROLLMENT","user ACTIVE; device public key; platform; MDM reference; ≤ 3 active devices per user","EVT-DEV-ENROLL-REQUESTED","DEVICE_LIMIT_REACHED"),
  (["PENDING_ENROLLMENT"],"CMD-DEV-CONFIRM","ACTIVE","hardware attestation valid (or MDM compliance); Administrator or MDM policy","EVT-DEV-ACTIVATED","ATTESTATION_FAILED"),
  (["ACTIVE"],"CMD-DEV-ROTATE-KEY","=","signed by current key; new public key","EVT-DEV-KEY-ROTATED","SIGNATURE_INVALID"),
  (["ACTIVE"],"CMD-DEV-SUSPEND","SUSPENDED","reason; sync rejected while suspended","EVT-DEV-SUSPENDED","REASON_REQUIRED"),
  (["SUSPENDED"],"CMD-DEV-REINSTATE","ACTIVE","reason","EVT-DEV-REINSTATED","REASON_REQUIRED"),
  (["ACTIVE","SUSPENDED"],"CMD-DEV-REPORT-LOST","LOST","user or Security Officer; key revoked immediately; wipe instruction queued; queued commands from the device after the lost time require review","EVT-DEV-REPORTED-LOST",None),
  (["LOST"],"SYS:wipe confirmed by device","WIPED","device acknowledges wipe on next contact","EVT-DEV-WIPED",None),
  (["ACTIVE","SUSPENDED"],"CMD-DEV-RETIRE","RETIRED","device synced and wiped (confirmation) or Security Officer override","EVT-DEV-RETIRED","DEVICE_NOT_WIPED")],
 ["INV-DEV-01: only ACTIVE devices can open sync sessions or download preload packages",
  "INV-DEV-02: device key is bound to (user, device); every offline command is signed with it (THR-012)",
  "INV-DEV-03: LOST revokes the key at once; the next contact receives a wipe instruction and nothing else",
  "INV-DEV-04: ≤ 3 ACTIVE devices per user (W4 delegated decision)"],
 ["DeviceKey (public key, valid_from, revoked_at)"],["REQ-OFF-005"])

agg("AGG-PRELOAD-PACKAGE","BC07","Preload Package","T2","حزمة بيانات منطقة عمل للاستخدام دون اتصال، مفلترة بصلاحية المستخدم وقت البناء",
 ["REQUESTED","BUILDING","READY","DOWNLOADED","EXPIRED","REVOKED"],["EXPIRED","REVOKED"],
 [("∅","CMD-PKG-REQUEST","REQUESTED","device ACTIVE; area polygon ≤ tenant max area; layers; time window; requested level ≤ tenant offline max level (default INTERNAL, POL-OFFLINE-PRELOAD)","EVT-PKG-REQUESTED","PRELOAD_NOT_ALLOWED"),
  (["REQUESTED"],"SYS:build started","BUILDING","worker","EVT-PKG-BUILDING",None),
  (["BUILDING"],"SYS:build finished","READY","content = objects visible to the user at build time and ≤ requested level; manifest with hashes, labels, security_version, expires_at (≤ 72 h R1)","EVT-PKG-READY",None),
  (["READY"],"CMD-PKG-CONFIRM-DOWNLOAD","DOWNLOADED","device acknowledges manifest hash","EVT-PKG-DOWNLOADED","MANIFEST_MISMATCH"),
  (["READY","DOWNLOADED"],"SYS:expires_at reached","EXPIRED","device purges at expiry (local enforcement) and confirms on next contact","EVT-PKG-EXPIRED",None),
  (["REQUESTED","BUILDING","READY","DOWNLOADED"],"SYS:user security_version changed or device not ACTIVE","REVOKED","purge instruction on next contact","EVT-PKG-REVOKED",None),
  (["REQUESTED","BUILDING","READY","DOWNLOADED"],"CMD-PKG-REVOKE","REVOKED","user, Administrator or Security Officer; reason","EVT-PKG-REVOKED","REASON_REQUIRED")],
 ["INV-PKG-01: package content never exceeds the user's authorization at build time nor the tenant offline level (REQ-OFF-002)",
  "INV-PKG-02: packages expire; expired or revoked data becomes unreadable on the device (local key discarded)",
  "INV-PKG-03: any change of the user's security_version revokes all their packages"],
 ["Manifest (items, hashes, labels, expires_at)"],["REQ-OFF-002","REQ-OFF-005"])

agg("AGG-SYNC-SESSION","BC07","Sync Session","T2","جلسة مزامنة جهاز: مصافحة، رفع أوامر مرتبة، تطبيقها، ثم تنزيل الفروق",
 ["OPEN","APPLYING","COMPLETED","COMPLETED_WITH_CONFLICTS","FAILED","REJECTED"],["COMPLETED","COMPLETED_WITH_CONFLICTS","FAILED","REJECTED"],
 [("∅","CMD-SYN-OPEN","OPEN","device ACTIVE; user authenticated (fresh token); device signature on handshake; clock offset measured (server − device); resumes after last acknowledged seq","EVT-SYN-OPENED","DEVICE_NOT_ACTIVE"),
  ("∅","SYS:device LOST or SUSPENDED at handshake","REJECTED","returns wipe (LOST) or stop (SUSPENDED) instruction only","EVT-SYN-REJECTED",None),
  (["OPEN","APPLYING"],"CMD-SYN-UPLOAD-BATCH","APPLYING","≤ 200 commands; contiguous seq after last acknowledged; each envelope signed by device key; batch hash chain continues","EVT-SYN-BATCH-RECEIVED","SEQUENCE_GAP"),
  (["APPLYING"],"SYS:all uploaded commands processed without conflict","COMPLETED","device declared end of queue; every command applied or idempotently recognized","EVT-SYN-COMPLETED",None),
  (["APPLYING"],"SYS:all processed with ≥ 1 sync conflict","COMPLETED_WITH_CONFLICTS","conflicts opened as AGG-SYNC-CONFLICT","EVT-SYN-COMPLETED-WITH-CONFLICTS",None),
  (["OPEN","APPLYING"],"SYS:idle timeout (5 min) or transport loss","FAILED","acknowledged seq retained; next session resumes (REQ-OFF-006)","EVT-SYN-FAILED",None)],
 ["INV-SYN-01: commands are applied in device seq order; client_command_id makes re-delivery idempotent (REQ-OFF-006)",
  "INV-SYN-02: record time = server receipt; device time stored and corrected by the measured clock offset (REQ-OFF-003)",
  "INV-SYN-03: the gateway applies commands through owner-context APIs with the user's delegated SecurityContext — never bypassing owner guards or policies",
  "INV-SYN-04: no last-write-wins for T1/T2: a state-changing command whose base_version ≠ current becomes a sync conflict (REQ-OFF-004)"],
 ["CommandEnvelope (client_command_id, seq, target, base_version, device_time, payload, signature)","BatchReceipt"],
 ["REQ-OFF-001","REQ-OFF-003","REQ-OFF-004","REQ-OFF-006"])

agg("AGG-SYNC-CONFLICT","BC07","Sync Conflict","T2","أمر ميداني لم يُطبق لأن الحالة تغيرت؛ ينتظر قراراً بشرياً",
 ["OPEN","RESOLVED_APPLIED","RESOLVED_DISCARDED","RESOLVED_MANUAL"],["RESOLVED_APPLIED","RESOLVED_DISCARDED","RESOLVED_MANUAL"],
 [("∅","SYS:stale state-changing command","OPEN","rule CF-05: base_version ≠ current; stores original envelope, current state snapshot and owner rejection reason; reviewer = owner-context default (task: owner/Planner; observation: Analyst)","EVT-SCF-OPENED",None),
  (["OPEN"],"CMD-SCF-ASSIGN","=","assignee authorized on the target","EVT-SCF-ASSIGNED","REVIEWER_NOT_AUTHORIZED"),
  (["OPEN"],"CMD-SCF-REAPPLY","RESOLVED_APPLIED","reviewer re-sends the original intent against the current version; owner-context accepts (its guards still apply)","EVT-SCF-REAPPLIED","OWNER_REJECTED"),
  (["OPEN"],"CMD-SCF-DISCARD","RESOLVED_DISCARDED","reason; field user notified","EVT-SCF-DISCARDED","REASON_REQUIRED"),
  (["OPEN"],"CMD-SCF-RESOLVE-MANUALLY","RESOLVED_MANUAL","note + reference to the alternative action taken","EVT-SCF-RESOLVED-MANUALLY","REASON_REQUIRED")],
 ["INV-SCF-01: the original field command and device time are preserved as evidence of what the field user did",
  "INV-SCF-02: reapplying never bypasses the owner's state machine, guards or policies",
  "INV-SCF-03: commands recorded after a device's reported-lost time always open a conflict (never auto-applied)"],
 ["OriginalEnvelope","StateSnapshot"],["REQ-OFF-004"],
 "Claim-level disagreements are not sync conflicts: observations are append-only and their claims flow into BC02's conflict engine (CF-01..04). CF-05 is for stale state-changing commands only (CR-49).")

PERPETUAL = {}
QUERIES = [
 ("QRY-DEV-LIST","BC01","GET","/api/v1/foundation/devices","Devices of a user (self) or in scope (Administrator)","self; Administrator in scope","REQ-OFF-005"),
 ("QRY-PKG-GET","BC07","GET","/api/v1/field/preload-packages/{package_id}","Package manifest and download target (signed, ≤ 5 min)","package owner device + user","REQ-OFF-002"),
 ("QRY-SYN-DELTA","BC07","GET","/api/v1/field/sync-sessions/{session_id}/delta","Server → device: my task changes, package updates, purge list, conflict notices, wipe/stop instruction","device + user of the session","REQ-OFF-001"),
 ("QRY-SCF-LIST","BC07","GET","/api/v1/field/sync-conflicts","Open sync conflicts by target type, assignee","reviewers authorized on targets","REQ-OFF-004"),
 ("QRY-SCF-GET","BC07","GET","/api/v1/field/sync-conflicts/{conflict_id}","Original envelope, current state snapshot, owner rejection reason","reviewer authorized on target","REQ-OFF-004"),
]
ACTORS = {"DEV":"user (enroll, report lost) · Administrator / MDM policy (confirm, suspend, reinstate, retire) · Security Officer (lost, retire override)",
          "PKG":"field user (request, confirm download, revoke) · Administrator / Security Officer (revoke)","SYN":"field device + user (open, upload)",
          "SCF":"reviewer: task owner/Planner, Analyst for observations (assign, reapply, discard, resolve)"}
P = {
 "CMD-DEV-ENROLL":"user!:urn public_key!:string platform!:enum(android,ios) mdm_ref:string","CMD-DEV-CONFIRM":"attestation!:string","CMD-DEV-ROTATE-KEY":"new_public_key!:string signature!:string",
 "CMD-DEV-SUSPEND":"reason!:string","CMD-DEV-REINSTATE":"reason!:string","CMD-DEV-REPORT-LOST":"lost_at!:date-time note:string","CMD-DEV-RETIRE":"reason!:string override:boolean",
 "CMD-PKG-REQUEST":"device!:urn area!:object layers!:array window!:Interval level!:string","CMD-PKG-CONFIRM-DOWNLOAD":"manifest_sha256!:string","CMD-PKG-REVOKE":"reason!:string",
 "CMD-SYN-OPEN":"device!:urn device_time!:date-time last_acked_seq!:integer queue_length!:integer queue_head_hash!:string signature!:string",
 "CMD-SYN-UPLOAD-BATCH":"envelopes!:array end_of_queue!:boolean",
 "CMD-SCF-ASSIGN":"reviewer!:urn","CMD-SCF-REAPPLY":"note:string","CMD-SCF-DISCARD":"reason!:string","CMD-SCF-RESOLVE-MANUALLY":"note!:string action_ref:urn",
}
SYSTEM_CMDS = set()
RESOURCE = {"AGG-DEVICE":("foundation","devices"),"AGG-PRELOAD-PACKAGE":("field","preload-packages"),"AGG-SYNC-SESSION":("field","sync-sessions"),"AGG-SYNC-CONFLICT":("field","sync-conflicts")}
SECURITY_AFFECTING = {"EVT-DEV-REPORTED-LOST","EVT-DEV-SUSPENDED"}
CONSUMERS = {"AGG-DEVICE":["Sync gateway (device registry cache)","Preload packages (revoke on LOST/SUSPENDED)","Security-version service"],
 "AGG-PRELOAD-PACKAGE":["Package builder","Sync delta (purge list)"],"AGG-SYNC-SESSION":["Owner contexts (commands applied via their APIs)","Field telemetry"],
 "AGG-SYNC-CONFLICT":["Reviewer notification","Sync delta (conflict notice to field user)"],"default":["Field telemetry"]}
CTX_OVERRIDE = {"BC07": ("field", "Field")}


def enrich(spec, bc):
    if bc != "BC07": return
    S = spec["components"]["schemas"]
    S["CommandEnvelope"] = {"type": "object", "required": ["client_command_id", "seq", "target_command", "device_time", "payload", "signature"], "additionalProperties": False, "properties": {
      "client_command_id": {"type": "string", "pattern": "^[0-9A-HJKMNP-TV-Z]{26}$"}, "seq": {"type": "integer", "minimum": 1},
      "target_command": {"enum": ["CMD-OBS-RECORD", "CMD-ATT-INITIATE-UPLOAD", "CMD-ATT-COMPLETE-UPLOAD", "CMD-EVD-REGISTER", "CMD-OBS-ATTACH-EVIDENCE", "CMD-OBS-AMEND",
          "CMD-TASK-ACCEPT", "CMD-TASK-START", "CMD-TASK-BLOCK", "CMD-TASK-RESUME", "CMD-TASK-ADD-RESULT-ITEM", "CMD-TASK-SUBMIT"]},
      "target_urn": {"$ref": "#/components/schemas/Urn"}, "base_version": {"type": ["integer", "null"]}, "device_time": {"type": "string", "format": "date-time"},
      "payload": {"type": "object"}, "signature": {"type": "string"}, "prev_hash": {"type": "string"}}}
    S["SyncDelta"] = {"type": "object", "required": ["instructions", "tasks", "purge", "conflict_notices", "server_time"], "properties": {
      "server_time": {"type": "string", "format": "date-time"}, "instructions": {"type": "array", "items": {"enum": ["CONTINUE", "STOP", "WIPE", "REAUTHENTICATE"]}},
      "tasks": {"type": "array", "items": {"type": "object"}}, "packages": {"type": "array", "items": {"type": "object"}}, "purge": {"type": "array", "items": {"$ref": "#/components/schemas/Urn"}},
      "conflict_notices": {"type": "array", "items": {"type": "object"}}, "acked_seq": {"type": "integer"}}}
    for name, sch in S.items():
        if name.startswith("SynUploadBatch") and "properties" in sch:
            sch["properties"]["envelopes"] = {"type": "array", "minItems": 1, "maxItems": 200, "items": {"$ref": "#/components/schemas/CommandEnvelope"}}
    spec["paths"]["/api/v1/field/sync-sessions/{session_id}/delta"]["get"]["responses"]["200"]["content"] = {"application/json": {"schema": {"$ref": "#/components/schemas/SyncDelta"}}}
```

## slc12_data.py

```python
# -*- coding: utf-8 -*-
# SLC-12 — Products, Knowledge & Lessons, Archive, Historical Retrieval & Reconstruction (R2)
SLICE = "SLC-12"
AGGS = {}
def agg(id_, bc, name, tier, purpose, states, terminal, transitions, invariants, entities, reqs, notes=None, personal=False):
    AGGS[id_] = dict(id=id_, bc=bc, name=name, tier=tier, purpose=purpose, states=states, terminal=terminal,
                     transitions=transitions, invariants=invariants, entities=entities, requirements=reqs, notes=notes, personal_data=personal)

agg("AGG-PRODUCT-TEMPLATE","BC06","Product Template","T2","قالب منتج بأقسام وربط بيانات، بإصدارات",
 ["DRAFT","ACTIVE","RETIRED"],["RETIRED"],
 [("∅","CMD-PTM-DEFINE","DRAFT","code unique; product kind ∈ {report, briefing, map_product, analytical_product}","EVT-PTM-DEFINED","TEMPLATE_INVALID"),
  (["DRAFT","ACTIVE"],"CMD-PTM-EDIT","=","sections valid (text, map, chart, table, key_judgments, citations); every data binding is a declared platform query with typed parameters; ACTIVE → new version","EVT-PTM-EDITED","TEMPLATE_INVALID"),
  (["DRAFT"],"CMD-PTM-ACTIVATE","ACTIVE","sample generation succeeded; approver ≠ author","EVT-PTM-ACTIVATED","SEGREGATION_OF_DUTIES"),
  (["ACTIVE"],"CMD-PTM-RETIRE","RETIRED","reason; existing products keep their pinned version","EVT-PTM-RETIRED","REASON_REQUIRED")],
 ["INV-PTM-01: bindings call only declared queries (no free-form data access), so products obey the same authorization as the UI",
  "INV-PTM-02: products pin the template version"],
 ["Section","Binding (query id, parameters)"],["REQ-PRD-001"])

agg("AGG-PRODUCT","BC06","Product Version","T1 content / T2 lifecycle","منتج (تقرير، إحاطة، خريطة، منتج تحليلي) مولّد من قالب، يُراجع ويُعتمد ويُجمّد",
 ["DRAFT","GENERATING","GENERATED","GENERATION_FAILED","IN_REVIEW","APPROVED","SUPERSEDED","WITHDRAWN","DISCARDED"],["SUPERSEDED","WITHDRAWN","DISCARDED"],
 [("∅","CMD-PRD-CREATE","DRAFT","template ACTIVE (version pinned); parameters valid; audience (org units/roles); target label ≥ labels of scope objects referenced in parameters; optional revises = APPROVED version","EVT-PRD-CREATED","PRODUCT_INVALID"),
  (["DRAFT","GENERATED","GENERATION_FAILED"],"CMD-PRD-GENERATE","GENERATING","author; async job with the author's authority","EVT-PRD-GENERATION-STARTED",None),
  (["GENERATING"],"SYS:generation succeeded","GENERATED","every binding executed as known_at = generation time; content items with label > product label excluded; rendered artifacts hashed","EVT-PRD-GENERATED",None),
  (["GENERATING"],"SYS:generation failed","GENERATION_FAILED","error recorded","EVT-PRD-GENERATION-FAILED",None),
  (["GENERATED"],"CMD-PRD-EDIT-NARRATIVE","=","only narrative sections; data sections change only by regeneration","EVT-PRD-NARRATIVE-EDITED","SECTION_NOT_EDITABLE"),
  (["GENERATED"],"CMD-PRD-SUBMIT","IN_REVIEW","all required sections present; AI-drafted sections reviewed (REQ-AI-005)","EVT-PRD-SUBMITTED","PRODUCT_INCOMPLETE"),
  (["IN_REVIEW"],"CMD-PRD-RETURN","GENERATED","reviewer; reason","EVT-PRD-RETURNED","REASON_REQUIRED"),
  (["IN_REVIEW"],"CMD-PRD-APPROVE","APPROVED","reviewer ≠ author; content frozen with pinned citations; previous APPROVED version of the same product → SUPERSEDED","EVT-PRD-APPROVED","SEGREGATION_OF_DUTIES"),
  (["APPROVED"],"SYS:newer version approved","SUPERSEDED","system","EVT-PRD-SUPERSEDED",None),
  (["APPROVED"],"CMD-PRD-WITHDRAW","WITHDRAWN","reason; recipients notified","EVT-PRD-WITHDRAWN","REASON_REQUIRED"),
  (["DRAFT","GENERATED","GENERATION_FAILED"],"CMD-PRD-DISCARD","DISCARDED","author; reason","EVT-PRD-DISCARDED","REASON_REQUIRED")],
 ["INV-PRD-01: an APPROVED version is immutable; changes are new versions (REQ-PRD-003)",
  "INV-PRD-02: product label ≥ every included content label; content above the label is excluded, and exclusions are not counted in the product (REQ-PRD-002, A21)",
  "INV-PRD-03: data is pinned at generation (known_at), so the product reproduces exactly what was generated",
  "INV-PRD-04: approver ≠ author"],
 ["RenderedArtifact (format, hash)","Citation (pinned)","ExclusionRecord (internal, audit only)"],["REQ-PRD-001","REQ-PRD-002","REQ-PRD-003"])

agg("AGG-DISTRIBUTION","BC06","Distribution","T2","توزيع نسخة معتمدة لمستلمين بعلامة مائية لكل مستلم",
 ["PREPARING","COMPLETED","COMPLETED_WITH_EXCLUSIONS","CANCELLED"],["COMPLETED","COMPLETED_WITH_EXCLUSIONS","CANCELLED"],
 [("∅","CMD-DST-DISTRIBUTE","PREPARING","product APPROVED; recipients (users, org units); formats ⊆ {pdf, docx, in_app}; distributor authorized","EVT-DST-STARTED","PRODUCT_NOT_APPROVED"),
  (["PREPARING"],"SYS:all recipients authorized and delivered","COMPLETED","per-recipient watermark (recipient id, product version, time) embedded; delivery logged","EVT-DST-COMPLETED",None),
  (["PREPARING"],"SYS:some recipients not authorized","COMPLETED_WITH_EXCLUSIONS","unauthorized recipients excluded and listed to the distributor; others delivered","EVT-DST-COMPLETED-WITH-EXCLUSIONS",None),
  (["PREPARING"],"CMD-DST-CANCEL","CANCELLED","distributor; reason","EVT-DST-CANCELLED","REASON_REQUIRED")],
 ["INV-DST-01: a recipient receives a product only if cleared for its label and within its audience (REQ-PRD-004)",
  "INV-DST-02: every delivered copy carries a unique recipient watermark (REQ-PRD-005)",
  "INV-DST-03: withdrawn products stop being downloadable; recipients are notified"],
 ["Delivery (recipient, format, watermark id, delivered_at)"],["REQ-PRD-004","REQ-PRD-005"])

agg("AGG-KNOWLEDGE-OBJECT","BC06","Knowledge Object Version","T1 content / T2 lifecycle","إجراء أو درس أو ممارسة فضلى أو معرفة سياساتية، كعبارات بأدلة وعلاقات",
 ["DRAFT","IN_REVIEW","PUBLISHED","REJECTED","SUPERSEDED","RETIRED","DISCARDED"],["REJECTED","SUPERSEDED","RETIRED","DISCARDED"],
 [("∅","CMD-KNO-DRAFT","DRAFT","type ∈ {procedure, lesson, best_practice, policy_knowledge}; lessons reference a terminal source (task, plan, incident, or a completed exercise simulation — CR-63) and its evidence (REQ-KNW-002); label ≥ source label","EVT-KNO-DRAFTED","KNOWLEDGE_INVALID"),
  (["DRAFT"],"CMD-KNO-EDIT","=","statements with evidence links; relationships to task types, plan types, entity types, areas","EVT-KNO-EDITED","KNOWLEDGE_INVALID"),
  (["DRAFT"],"CMD-KNO-SUBMIT","IN_REVIEW","≥ 1 statement; lessons: ≥ 1 evidence link","EVT-KNO-SUBMITTED","KNOWLEDGE_INCOMPLETE"),
  (["IN_REVIEW"],"CMD-KNO-RETURN","DRAFT","reviewer; reason","EVT-KNO-RETURNED","REASON_REQUIRED"),
  (["IN_REVIEW"],"CMD-KNO-PUBLISH","PUBLISHED","reviewer ≠ author; procedures and policy knowledge require the owning authority (Knowledge Manager + domain authority); previous PUBLISHED → SUPERSEDED","EVT-KNO-PUBLISHED","SEGREGATION_OF_DUTIES"),
  (["IN_REVIEW"],"CMD-KNO-REJECT","REJECTED","reason","EVT-KNO-REJECTED","REASON_REQUIRED"),
  (["PUBLISHED"],"CMD-KNO-RECORD-REUSE","=","target plan/task/product visible; reuse counted (OUT-06)","EVT-KNO-REUSED","TARGET_INVALID"),
  (["PUBLISHED"],"SYS:newer version published","SUPERSEDED","system","EVT-KNO-SUPERSEDED",None),
  (["PUBLISHED"],"CMD-KNO-RETIRE","RETIRED","reason (obsolete, wrong)","EVT-KNO-RETIRED","REASON_REQUIRED"),
  (["DRAFT"],"CMD-KNO-DISCARD","DISCARDED","author; reason","EVT-KNO-DISCARDED","REASON_REQUIRED")],
 ["INV-KNO-01: published versions are immutable; one PUBLISHED version per knowledge object",
  "INV-KNO-02: knowledge statements are not claims about the world (they do not enter BC02 resolution); they cite claims and evidence",
  "INV-KNO-03: policy knowledge describes a policy but never changes authorization (the PDP ignores it) — glossary CR-33"],
 ["Statement","EvidenceLink","Relationship (to task type / plan type / entity type / area)"],["REQ-KNW-001","REQ-KNW-002","REQ-KNW-003"])

agg("AGG-ARCHIVE-PACKAGE","BC06","Archive Package (AIP)","T1","حزمة أرشيفية بمعيار OAIS: محتوى، بيانات وصفية، منشأ، بصمات، سجل وصول",
 ["INGESTING","INGEST_FAILED","ARCHIVED","INTEGRITY_FAILED","TRANSFERRED","DISPOSED"],["TRANSFERRED","DISPOSED"],
 [("∅","SYS:disposition action ARCHIVE for a bucket or record set","INGESTING","SIP assembled from owner exports: content, metadata, provenance, access history","EVT-ARC-INGEST-STARTED",None),
  (["INGESTING"],"SYS:package validated","ARCHIVED","BagIt structure valid; every file fixity (SHA-256) recorded; preservation formats (R2-Q6) produced alongside originals","EVT-ARC-ARCHIVED",None),
  (["INGESTING"],"SYS:validation failed","INGEST_FAILED","errors recorded","EVT-ARC-INGEST-FAILED",None),
  (["INGEST_FAILED"],"CMD-ARC-RETRY-INGEST","INGESTING","archivist; corrective note","EVT-ARC-INGEST-STARTED","REASON_REQUIRED"),
  (["ARCHIVED"],"SYS:integrity check failed","INTEGRITY_FAILED","fixity mismatch on any file","EVT-ARC-INTEGRITY-FAILED",None),
  (["INTEGRITY_FAILED"],"CMD-ARC-REPAIR","ARCHIVED","restored from replica; fixity re-verified","EVT-ARC-REPAIRED","FIXITY_MISMATCH"),
  (["ARCHIVED"],"CMD-ARC-MIGRATE-FORMAT","=","new preservation representation added; originals kept; preservation event recorded","EVT-ARC-FORMAT-MIGRATED","FORMAT_INVALID"),
  (["ARCHIVED"],"CMD-ARC-TRANSFER","TRANSFERRED","transfer authority decision; receipt from the receiving archive","EVT-ARC-TRANSFERRED","AUTHORITY_REQUIRED"),
  (["ARCHIVED","INTEGRITY_FAILED"],"SYS:disposition DESTROY executed for the package bucket","DISPOSED","SLC-12a key destruction; no active hold","EVT-ARC-DISPOSED",None)],
 ["INV-ARC-01: originals are never overwritten; format migration adds representations",
  "INV-ARC-02: every retrieval appends to the package's access history (REQ-ARC-003) and is audited",
  "INV-ARC-03: fixity verified at ingest, on every retrieval and at least yearly (REQ-ARC-002)",
  "INV-ARC-04: archive ≠ backup (BRL-011): packages are institutional records with their own retention"],
 ["BagManifest","PreservationEvent","Representation","AccessEntry"],["REQ-ARC-001","REQ-ARC-002","REQ-ARC-003"])

agg("AGG-RECONSTRUCTION","BC06","Historical Reconstruction","T2","إعادة بناء حالة نطاق كما كانت صحيحة في T وكما كانت معروفة في K",
 ["REQUESTED","RUNNING","COMPLETED","FAILED","CANCELLED"],["COMPLETED","FAILED","CANCELLED"],
 [("∅","CMD-REC-REQUEST","REQUESTED","scope (objects, situation, plan, decision basis); valid_at T; known_at K ≤ now; purpose (audit, legal, lessons); requester authorized","EVT-REC-REQUESTED","RECONSTRUCTION_INVALID"),
  (["REQUESTED"],"SYS:worker started","RUNNING","runs with the requester's authority","EVT-REC-STARTED",None),
  (["RUNNING"],"SYS:completed","COMPLETED","report: every element labelled RECORDED / RECONSTRUCTED / INFERRED (with rule) / UNKNOWN; archive retrievals included where needed","EVT-REC-COMPLETED",None),
  (["RUNNING"],"SYS:failed","FAILED","error recorded","EVT-REC-FAILED",None),
  (["REQUESTED","RUNNING"],"CMD-REC-CANCEL","CANCELLED","requester; reason","EVT-REC-CANCELLED","REASON_REQUIRED")],
 ["INV-REC-01: every element of the report carries its reconstruction label (PRJ§103, CR-25)",
  "INV-REC-02: the report is reproducible: same scope, T and K give the same result",
  "INV-REC-03: the report never exceeds the requester's authorization; hidden elements are absent, not marked"],
 ["ReconstructionElement (urn, value, label, rule?)"],["REQ-ARC-004"])

PERPETUAL = {}
QUERIES = [
 ("QRY-PRD-GET","BC06","GET","/api/v1/knowledge/products/{product_id}","Product version with rendered artifacts (download grants) and pinned citations","audience + label rule","REQ-PRD-003"),
 ("QRY-PRD-LIST","BC06","GET","/api/v1/knowledge/products","Products by kind, state, situation/case, date","allowed_scope","REQ-PRD-001"),
 ("QRY-DST-LOG","BC06","GET","/api/v1/knowledge/products/{product_id}/distributions","Distribution and delivery log with watermark ids","distributor, Security Officer, Auditor","REQ-PRD-004"),
 ("QRY-KNO-SEARCH","BC06","GET","/api/v1/knowledge/knowledge-objects","Published knowledge by type, text, relationships","any user; label rule","REQ-KNW-001"),
 ("QRY-KNO-SUGGEST","BC06","POST","/api/v1/knowledge/knowledge-suggestions","Published knowledge relevant to a task type / plan / area (by relationships)","planner; label rule","REQ-KNW-003"),
 ("QRY-ARC-SEARCH","BC06","GET","/api/v1/knowledge/archive-packages","Archive catalogue (metadata only) by class, period, org","Archivist; label rule","REQ-ARC-003"),
 ("QRY-ARC-RETRIEVE","BC06","POST","/api/v1/knowledge/archive-packages/{package_id}/retrievals","Retrieve package content (warm: signed grant; cold: staged job) — access logged","authorized by package label and purpose","REQ-ARC-003"),
 ("QRY-REC-REPORT","BC06","GET","/api/v1/knowledge/reconstructions/{reconstruction_id}/report","Labelled reconstruction report","requester, Auditor","REQ-ARC-004"),
]
ACTORS = {"PTM":"Knowledge Manager / Analysis lead (define, edit) · second approver (activate)","PRD":"Analyst / Planner (create, generate, edit, submit, discard) · reviewer (return, approve) · Manager (withdraw)",
 "DST":"Manager / product owner","KNO":"any user (draft lessons) · Knowledge Manager (review, publish, retire) · planner (record reuse)",
 "ARC":"Archivist (retry, repair, migrate) · transfer authority (transfer)","REC":"Auditor / Legal / Analyst (request, cancel)"}
P = {
 "CMD-PTM-DEFINE":"code!:string kind!:enum(report,briefing,map_product,analytical_product) name!:LocalizedName","CMD-PTM-EDIT":"sections!:array","CMD-PTM-ACTIVATE":"sample_ref!:urn","CMD-PTM-RETIRE":"reason!:string",
 "CMD-PRD-CREATE":"template!:urn parameters!:object audience!:array title!:LocalizedName revises:urn label!:Label","CMD-PRD-GENERATE":"","CMD-PRD-EDIT-NARRATIVE":"section_id!:string text!:LocalizedName",
 "CMD-PRD-SUBMIT":"","CMD-PRD-RETURN":"reason!:string","CMD-PRD-APPROVE":"note:string","CMD-PRD-WITHDRAW":"reason!:string","CMD-PRD-DISCARD":"reason!:string",
 "CMD-DST-DISTRIBUTE":"product!:urn recipients!:array formats!:array message:string","CMD-DST-CANCEL":"reason!:string",
 "CMD-KNO-DRAFT":"knowledge_type!:enum(procedure,lesson,best_practice,policy_knowledge) title!:LocalizedName source:urn revises:urn label!:Label",
 "CMD-KNO-EDIT":"statements!:array relationships:array","CMD-KNO-SUBMIT":"","CMD-KNO-RETURN":"reason!:string","CMD-KNO-PUBLISH":"note:string","CMD-KNO-REJECT":"reason!:string",
 "CMD-KNO-RECORD-REUSE":"target!:urn","CMD-KNO-RETIRE":"reason!:string","CMD-KNO-DISCARD":"reason!:string",
 "CMD-ARC-RETRY-INGEST":"note!:string","CMD-ARC-REPAIR":"replica_ref!:string","CMD-ARC-MIGRATE-FORMAT":"target_format!:string reason!:string","CMD-ARC-TRANSFER":"decision!:urn receiving_archive!:string receipt!:string",
 "CMD-REC-REQUEST":"scope!:object valid_at!:date-time known_at!:date-time purpose!:enum(audit,legal,lessons,analysis)","CMD-REC-CANCEL":"reason!:string",
}
SYSTEM_CMDS = set()
RESOURCE = {"AGG-PRODUCT-TEMPLATE":("knowledge","product-templates"),"AGG-PRODUCT":("knowledge","products"),"AGG-DISTRIBUTION":("knowledge","distributions"),
 "AGG-KNOWLEDGE-OBJECT":("knowledge","knowledge-objects"),"AGG-ARCHIVE-PACKAGE":("knowledge","archive-packages"),"AGG-RECONSTRUCTION":("knowledge","reconstructions")}
SECURITY_AFFECTING = set()
CONSUMERS = {"AGG-PRODUCT":["Distribution","Search projection (SLC-05)","Notification (reviewers)"],"AGG-DISTRIBUTION":["Notification (recipients)","Audit"],
 "AGG-KNOWLEDGE-OBJECT":["Knowledge suggestion index","Search projection (SLC-05)","Business telemetry (OUT-06)"],"AGG-ARCHIVE-PACKAGE":["Archive catalogue","Disposition (SLC-12a)","Audit"],
 "AGG-RECONSTRUCTION":["Requester notification","Audit"],"AGG-PRODUCT-TEMPLATE":["Product generator"],"default":["Search projection (SLC-05)"]}
CTX_OVERRIDE = {}

def enrich(spec, bc):
    S = spec["components"]["schemas"]
    S["TemplateSection"] = {"type": "object", "required": ["id", "kind"], "properties": {"id": {"type": "string"}, "kind": {"enum": ["text", "map", "chart", "table", "key_judgments", "citations"]},
        "editable": {"type": "boolean"}, "binding": {"type": "object", "properties": {"query": {"type": "string", "description": "declared platform query id"}, "parameters": {"type": "object"}}}}}
    S["Recipient"] = {"type": "object", "required": ["kind", "ref"], "properties": {"kind": {"enum": ["user", "org_unit"]}, "ref": {"$ref": "#/components/schemas/Urn"}}}
    S["KnowledgeStatement"] = {"type": "object", "required": ["text"], "properties": {"text": {"$ref": "#/components/schemas/LocalizedName"}, "evidence": {"type": "array", "items": {"$ref": "#/components/schemas/Urn"}}, "claims": {"type": "array", "items": {"$ref": "#/components/schemas/Urn"}}}}
    S["KnowledgeRelationship"] = {"type": "object", "required": ["kind", "ref"], "properties": {"kind": {"enum": ["task_type", "plan_type", "entity_type", "area", "knowledge"]}, "ref": {"type": "string"}}}
    S["ReconstructionScope"] = {"type": "object", "properties": {"objects": {"type": "array", "items": {"$ref": "#/components/schemas/Urn"}}, "situation": {"$ref": "#/components/schemas/Urn"},
        "plan": {"$ref": "#/components/schemas/Urn"}, "decision_basis": {"$ref": "#/components/schemas/Urn"}}}
    for name, sch in S.items():
        if not name.endswith("Command") or "properties" not in sch: continue
        pr = sch["properties"]
        if name.startswith("PtmEdit"): pr["sections"] = {"type": "array", "minItems": 1, "items": {"$ref": "#/components/schemas/TemplateSection"}}
        if name.startswith("DstDistribute"):
            pr["recipients"] = {"type": "array", "minItems": 1, "items": {"$ref": "#/components/schemas/Recipient"}}
            pr["formats"] = {"type": "array", "minItems": 1, "items": {"enum": ["pdf", "docx", "in_app"]}}
        if name.startswith("PrdCreate"): pr["audience"] = {"type": "array", "minItems": 1, "items": {"$ref": "#/components/schemas/Recipient"}}
        if name.startswith("KnoEdit"):
            pr["statements"] = {"type": "array", "minItems": 1, "items": {"$ref": "#/components/schemas/KnowledgeStatement"}}
            pr["relationships"] = {"type": "array", "items": {"$ref": "#/components/schemas/KnowledgeRelationship"}}
        if name.startswith("RecRequest"): pr["scope"] = {"$ref": "#/components/schemas/ReconstructionScope"}
```

## slc12a_data.py

```python
# -*- coding: utf-8 -*-
# SLC-12a — Retention, legal hold, disposition, erasure (R1 portion of SLC-12)
SLICE = "SLC-12a"
AGGS = {}
def agg(id_, bc, name, tier, purpose, states, terminal, transitions, invariants, entities, reqs, notes=None, personal=False):
    AGGS[id_] = dict(id=id_, bc=bc, name=name, tier=tier, purpose=purpose, states=states, terminal=terminal,
                     transitions=transitions, invariants=invariants, entities=entities, requirements=reqs, notes=notes, personal_data=personal)

agg("AGG-RETENTION-SCHEDULE","BC08","Retention Schedule Version","T2","جدول الاحتفاظ لكل مستأجر: لكل فئة سجلات مدة ومحفز وإجراء إتلاف وأساس قانوني",
 ["DRAFT","ACTIVE","SUPERSEDED","DISCARDED"],["SUPERSEDED","DISCARDED"],
 [("∅","CMD-RTS-DRAFT","DRAFT","Archivist; ≤ 1 DRAFT per tenant","EVT-RTS-DRAFTED","DRAFT_EXISTS"),
  (["DRAFT"],"CMD-RTS-EDIT","=","each rule: record class (RD-RECORD-CLASSES), period (ISO 8601 duration), trigger ∈ {recorded, closed, superseded, event}, action ∈ {DESTROY, REVIEW, ARCHIVE (R2)}, legal basis","EVT-RTS-EDITED","SCHEDULE_INVALID"),
  (["DRAFT"],"CMD-RTS-ACTIVATE","ACTIVE","every record class in RD-RECORD-CLASSES has exactly one rule (REQ-GOV-006); approver = Legal/Compliance authority ≠ drafter; previous ACTIVE → SUPERSEDED in the same transaction","EVT-RTS-ACTIVATED","SCHEDULE_INCOMPLETE"),
  (["DRAFT"],"CMD-RTS-DISCARD","DISCARDED","reason","EVT-RTS-DISCARDED","REASON_REQUIRED"),
  (["ACTIVE"],"SYS:successor activated","SUPERSEDED","system","EVT-RTS-SUPERSEDED",None)],
 ["INV-RTS-01: exactly one ACTIVE schedule version per tenant; every record class covered",
  "INV-RTS-02: shortening a period applies only to records whose trigger occurs after activation unless the approver explicitly marks it retroactive (legal decision recorded)",
  "INV-RTS-03: schedule versions are immutable once ACTIVE"],
 ["RetentionRule (record_class, period, trigger, action, legal_basis)"],["REQ-GOV-006"])

agg("AGG-LEGAL-HOLD","BC08","Legal Hold","T2","تجميد قانوني يمنع إتلاف ومحو ما يشمله",
 ["ACTIVE","RELEASE_REQUESTED","RELEASED"],["RELEASED"],
 [("∅","CMD-LHD-PLACE","ACTIVE","Legal/Compliance authority; scope = any of: record classes, object URNs, data subjects, org units, time range; legal reference","EVT-LHD-PLACED","HOLD_INVALID"),
  (["ACTIVE"],"CMD-LHD-EXTEND","=","added scope items; reason","EVT-LHD-EXTENDED","HOLD_INVALID"),
  (["ACTIVE"],"CMD-LHD-REQUEST-RELEASE","RELEASE_REQUESTED","reason; requester = Legal authority","EVT-LHD-RELEASE-REQUESTED","REASON_REQUIRED"),
  (["RELEASE_REQUESTED"],"CMD-LHD-APPROVE-RELEASE","RELEASED","second Legal authority ≠ requester","EVT-LHD-RELEASED","SEGREGATION_OF_DUTIES"),
  (["RELEASE_REQUESTED"],"CMD-LHD-CANCEL-RELEASE","ACTIVE","reason","EVT-LHD-RELEASE-CANCELLED","REASON_REQUIRED")],
 ["INV-LHD-01: while ACTIVE or RELEASE_REQUESTED, no matching record can be disposed, erased or have its key destroyed (REQ-GOV-007)",
  "INV-LHD-02: holds never block versioned changes (history is preserved); they block destructive actions only",
  "INV-LHD-03: scope can only grow while ACTIVE; narrowing = release + new hold",
  "INV-LHD-04: release needs two distinct Legal authorities"],
 ["HoldScopeItem"],["REQ-GOV-007"])

agg("AGG-DISPOSITION-RUN","BC08","Disposition Run","T2","دورة إتلاف: ترشيح، اعتماد، تنفيذ عبر إتلاف مفاتيح الحاويات، شهادة",
 ["PLANNED","AWAITING_APPROVAL","APPROVED","EXECUTING","COMPLETED","COMPLETED_WITH_EXCEPTIONS","CANCELLED"],["COMPLETED","COMPLETED_WITH_EXCEPTIONS","CANCELLED"],
 [("∅","SYS:scheduled evaluation (daily)","PLANNED","candidates = key buckets whose records are all past retention under the ACTIVE schedule; held items identified via HoldCheck","EVT-DSP-PLANNED",None),
  (["PLANNED"],"CMD-DSP-SUBMIT","AWAITING_APPROVAL","Archivist reviewed candidate summary (counts per class/bucket, REVIEW-action items listed)","EVT-DSP-SUBMITTED",None),
  (["AWAITING_APPROVAL"],"CMD-DSP-APPROVE","APPROVED","approver = Records/Legal authority ≠ submitter; re-run HoldCheck at approval","EVT-DSP-APPROVED","SEGREGATION_OF_DUTIES"),
  (["APPROVED"],"SYS:execution started","EXECUTING","held items in each bucket re-wrapped under hold keys first; then bucket keys destroyed; owners notified to purge plaintext caches and projections; tombstones written","EVT-DSP-EXECUTING",None),
  (["EXECUTING"],"SYS:all buckets processed","COMPLETED","certificate issued (buckets, key ids destroyed, counts, holds excluded)","EVT-DSP-COMPLETED",None),
  (["EXECUTING"],"SYS:some buckets failed","COMPLETED_WITH_EXCEPTIONS","failed buckets listed; retried next run","EVT-DSP-COMPLETED-WITH-EXCEPTIONS",None),
  (["PLANNED","AWAITING_APPROVAL","APPROVED"],"CMD-DSP-CANCEL","CANCELLED","reason","EVT-DSP-CANCELLED","REASON_REQUIRED")],
 ["INV-DSP-01: destruction is by key (crypto-shredding of time-bucketed class keys), reaching operational stores, projections, archives and backups (ADR-P08, CR-51)",
  "INV-DSP-02: no bucket key is destroyed while any record in it is under hold — held records are re-wrapped first",
  "INV-DSP-03: each destruction is recorded in the append-only key-destruction log used by the restore gate",
  "INV-DSP-04: tombstones keep non-personal facts (class, bucket, count, run, date); audit records are governed by their own class rule"],
 ["BucketCandidate","DispositionCertificate"],["REQ-GOV-006","REQ-GOV-007"])

agg("AGG-ERASURE-REQUEST","BC08","Erasure Request","T2","طلب محو البيانات الشخصية لصاحب بيانات عبر إتلاف مفتاحه",
 ["RECEIVED","SCOPED","APPROVED","BLOCKED_BY_HOLD","EXECUTING","COMPLETED","REJECTED"],["COMPLETED","REJECTED"],
 [("∅","CMD-ERS-REGISTER","RECEIVED","legal basis reference; subject identification (platform person URN and/or information entity URNs of type person); requester","EVT-ERS-RECEIVED","ERASURE_INVALID"),
  (["RECEIVED"],"SYS:subject scope resolved","SCOPED","subject keys located in BC01 (persons), BC02 (entities with personal_data claims) and BC05 (qualification records of that person, CR-69); affected record counts per context","EVT-ERS-SCOPED",None),
  (["SCOPED"],"CMD-ERS-APPROVE","APPROVED","Legal/Compliance authority ≠ registrar; decision recorded with basis","EVT-ERS-APPROVED","SEGREGATION_OF_DUTIES"),
  (["SCOPED"],"CMD-ERS-REJECT","REJECTED","reason (e.g. legal obligation to retain)","EVT-ERS-REJECTED","REASON_REQUIRED"),
  (["APPROVED"],"SYS:hold matches subject","BLOCKED_BY_HOLD","HoldCheck positive","EVT-ERS-BLOCKED",None),
  (["BLOCKED_BY_HOLD"],"SYS:hold released","APPROVED","HoldCheck negative","EVT-ERS-UNBLOCKED",None),
  (["APPROVED"],"SYS:execution started","EXECUTING","subject DEKs destroyed; owners purge plaintext caches/projections; pseudonymous reference kept for audit facts","EVT-ERS-EXECUTING",None),
  (["EXECUTING"],"SYS:all contexts confirmed","COMPLETED","confirmation from each owning context ≤ 24 h (QAS-PRV-001); certificate issued","EVT-ERS-COMPLETED",None)],
 ["INV-ERS-01: execution destroys keys, not rows; data becomes unreadable everywhere including backups via the restore gate (CR-51)",
  "INV-ERS-02: blocked while any hold covers the subject",
  "INV-ERS-03: audit facts remain with a pseudonymous subject reference",
  "INV-ERS-04: approval and registration by different persons"],
 ["SubjectKeyRef","ContextConfirmation"],["REQ-GOV-008"],personal=True)

PERPETUAL = {}
QUERIES = [
 ("QRY-RTS-ACTIVE","BC08","GET","/api/v1/governance/retention-schedule","Active schedule version with rules","Archivist, Legal, Auditor","REQ-GOV-006"),
 ("QRY-LHD-LIST","BC08","GET","/api/v1/governance/legal-holds","Holds by state and scope","Legal, Archivist, Auditor","REQ-GOV-007"),
 ("QRY-LHD-CHECK","BC08","POST","/api/v1/governance/hold-checks","HoldCheck OHS: URNs / subjects / (class, bucket) → held? with hold ids","owner contexts (workload identity); Archivist","REQ-GOV-007"),
 ("QRY-DSP-GET","BC08","GET","/api/v1/governance/disposition-runs/{run_id}","Run with candidate summary, exceptions and certificate","Archivist, Legal, Auditor","REQ-GOV-006"),
 ("QRY-ERS-GET","BC08","GET","/api/v1/governance/erasure-requests/{request_id}","Request with scope counts, confirmations and certificate (no personal data)","Legal, Auditor","REQ-GOV-008"),
]
ACTORS = {"RTS":"Archivist (draft, edit, discard) · Legal/Compliance authority (activate)","LHD":"Legal/Compliance authority (place, extend, request/approve/cancel release)",
          "DSP":"Archivist (submit, cancel) · Records/Legal authority ≠ submitter (approve)","ERS":"Privacy officer / Legal (register) · Legal authority ≠ registrar (approve, reject)"}
P = {
 "CMD-RTS-DRAFT":"based_on:urn","CMD-RTS-EDIT":"rules!:array","CMD-RTS-ACTIVATE":"effective_from!:date-time retroactive_classes:array","CMD-RTS-DISCARD":"reason!:string",
 "CMD-LHD-PLACE":"name!:string legal_reference!:string scope!:array","CMD-LHD-EXTEND":"scope!:array reason!:string","CMD-LHD-REQUEST-RELEASE":"reason!:string",
 "CMD-LHD-APPROVE-RELEASE":"note:string","CMD-LHD-CANCEL-RELEASE":"reason!:string",
 "CMD-DSP-SUBMIT":"note:string","CMD-DSP-APPROVE":"note:string","CMD-DSP-CANCEL":"reason!:string",
 "CMD-ERS-REGISTER":"legal_basis!:string person:urn entities:array requester!:string","CMD-ERS-APPROVE":"decision_note!:string","CMD-ERS-REJECT":"reason!:string",
}
SYSTEM_CMDS = set()
RESOURCE = {"AGG-RETENTION-SCHEDULE":("governance","retention-schedules"),"AGG-LEGAL-HOLD":("governance","legal-holds"),
            "AGG-DISPOSITION-RUN":("governance","disposition-runs"),"AGG-ERASURE-REQUEST":("governance","erasure-requests")}
SECURITY_AFFECTING = set()
CONSUMERS = {"AGG-RETENTION-SCHEDULE":["Disposition planner","Key-bucket policy (class period sizing)"],
 "AGG-LEGAL-HOLD":["HoldCheck cache (all owners)","Disposition planner","Erasure executor"],
 "AGG-DISPOSITION-RUN":["Key manager (bucket key destruction)","Owner contexts (purge plaintext caches, projections)","Audit"],
 "AGG-ERASURE-REQUEST":["Key manager (subject key destruction)","BC01 / BC02 / BC05 (scope + confirmation)","Projections (purge)"],
 "default":["Audit"]}


def enrich(spec, bc):
    S = spec["components"]["schemas"]
    S["RetentionRule"] = {"type": "object", "required": ["record_class", "period", "trigger", "action", "legal_basis"], "properties": {"record_class": {"type": "string"}, "period": {"type": "string"},
      "trigger": {"enum": ["recorded", "closed", "superseded", "event"]}, "trigger_event": {"type": "string"}, "action": {"enum": ["DESTROY", "REVIEW", "ARCHIVE"]}, "legal_basis": {"type": "string"}}}
    S["HoldScopeItem"] = {"type": "object", "required": ["kind"], "properties": {"kind": {"enum": ["record_class", "object", "subject", "org_unit", "time_range"]}, "record_class": {"type": "string"},
      "urn": {"$ref": "#/components/schemas/Urn"}, "org_unit": {"$ref": "#/components/schemas/Urn"}, "range": {"$ref": "#/components/schemas/Interval"}}}
    S["HoldCheckRequest"] = {"type": "object", "properties": {"urns": {"type": "array", "maxItems": 500, "items": {"$ref": "#/components/schemas/Urn"}}, "subjects": {"type": "array", "items": {"$ref": "#/components/schemas/Urn"}},
      "buckets": {"type": "array", "items": {"type": "object", "properties": {"record_class": {"type": "string"}, "bucket": {"type": "string"}}}}}}
    S["HoldCheckResponse"] = {"type": "object", "required": ["results"], "properties": {"results": {"type": "array", "items": {"type": "object", "required": ["ref", "held"], "properties": {"ref": {"type": "string"}, "held": {"type": "boolean"}, "holds": {"type": "array", "items": {"$ref": "#/components/schemas/Urn"}}}}}}}
    for name, sch in S.items():
        if not name.endswith("Command") or "properties" not in sch: continue
        pr = sch["properties"]
        if name.startswith("RtsEdit"): pr["rules"] = {"type": "array", "minItems": 1, "items": {"$ref": "#/components/schemas/RetentionRule"}}
        if name.startswith(("LhdPlace", "LhdExtend")): pr["scope"] = {"type": "array", "minItems": 1, "items": {"$ref": "#/components/schemas/HoldScopeItem"}}
        if name.startswith("ErsRegister"): pr["entities"] = {"type": "array", "items": {"$ref": "#/components/schemas/Urn"}}
    op = spec["paths"]["/api/v1/governance/hold-checks"]["post"]
    op["requestBody"] = {"required": True, "content": {"application/json": {"schema": {"$ref": "#/components/schemas/HoldCheckRequest"}}}}
    op["responses"]["200"]["content"] = {"application/json": {"schema": {"$ref": "#/components/schemas/HoldCheckResponse"}}}
```

## slc14_data.py

```python
# -*- coding: utf-8 -*-
# SLC-14 — Collection requirements & planning (CAP-02.01, R2)
SLICE = "SLC-14"
AGGS = {}
def agg(id_, bc, name, tier, purpose, states, terminal, transitions, invariants, entities, reqs, notes=None, personal=False):
    AGGS[id_] = dict(id=id_, bc=bc, name=name, tier=tier, purpose=purpose, states=states, terminal=terminal,
                     transitions=transitions, invariants=invariants, entities=entities, requirements=reqs, notes=notes, personal_data=personal)

agg("AGG-COLLECTION-REQUIREMENT","BC02","Collection Requirement","T2","حاجة معلوماتية موجهة للجمع: سؤال، منطقة، نافذة، أولوية، عناصر معلومات أساسية",
 ["DRAFT","SUBMITTED","APPROVED","REJECTED","SATISFIED","EXPIRED","CANCELLED"],["REJECTED","SATISFIED","EXPIRED","CANCELLED"],
 [("∅","CMD-CRQ-DRAFT","DRAFT","question; requester; label","EVT-CRQ-DRAFTED","REQUIREMENT_INVALID"),
  (["DRAFT"],"CMD-CRQ-EDIT","=","area polygon, window, priority 1–5, due, essential elements of information (EEIs)","EVT-CRQ-EDITED","REQUIREMENT_INVALID"),
  (["DRAFT"],"CMD-CRQ-SUBMIT","SUBMITTED","area, window, priority and ≥ 1 EEI present (REQ-COL-001)","EVT-CRQ-SUBMITTED","REQUIREMENT_INCOMPLETE"),
  (["SUBMITTED"],"CMD-CRQ-APPROVE","APPROVED","collection manager with authority in the area scope; approver ≠ requester","EVT-CRQ-APPROVED","SEGREGATION_OF_DUTIES"),
  (["SUBMITTED"],"CMD-CRQ-REJECT","REJECTED","reason (duplicate, out of scope, infeasible)","EVT-CRQ-REJECTED","REASON_REQUIRED"),
  (["APPROVED"],"CMD-CRQ-AMEND","=","approver; extend due, adjust area or EEIs; recorded as new version","EVT-CRQ-AMENDED","REQUIREMENT_INVALID"),
  (["APPROVED"],"SYS:validated observation matched","=","matching engine links observation to EEIs (SPEC-COLLECTION §2); fulfilment recomputed","EVT-CRQ-FULFILMENT-UPDATED",None),
  (["APPROVED"],"CMD-CRQ-MARK-SATISFIED","SATISFIED","requester; fulfilment as seen by the requester is ANSWERED, or PARTIAL with explicit acceptance note","EVT-CRQ-SATISFIED","FULFILMENT_INSUFFICIENT"),
  (["APPROVED"],"SYS:due passed","EXPIRED","scheduler; based on due date only (never on hidden fulfilment)","EVT-CRQ-EXPIRED",None),
  (["DRAFT","SUBMITTED","APPROVED"],"CMD-CRQ-CANCEL","CANCELLED","requester or approver; reason","EVT-CRQ-CANCELLED","REASON_REQUIRED")],
 ["INV-CRQ-01: fulfilment is computed per viewer over the observations that viewer may see (visibility first) — no leakage of hidden collection",
  "INV-CRQ-02: every fulfilment link points to a VALIDATED observation (or a claim derived from one) with lineage (QAS-COL-001)",
  "INV-CRQ-03: expiry depends only on the due date",
  "INV-CRQ-04: approver ≠ requester"],
 ["EEI (id, entity_types, predicates, observation_methods, quantities)","FulfilmentLink (eei, observation, matched_at)"],["REQ-COL-001","REQ-COL-003"])

agg("AGG-COLLECTION-PLAN","BC02","Collection Plan","T2","خطة جمع: أنشطة بأساليب ومصادر وفرق، تولّد مهام ميدانية",
 ["DRAFT","ACTIVE","COMPLETED","CANCELLED"],["COMPLETED","CANCELLED"],
 [("∅","CMD-CPL-CREATE","DRAFT","≥ 1 APPROVED collection requirement; planner in scope; label ≥ requirements","EVT-CPL-CREATED","REQUIREMENT_NOT_APPROVED"),
  (["DRAFT","ACTIVE"],"CMD-CPL-ADD-ACTIVITY","=","method in RD-COLLECTION-METHODS; source(s) ACTIVE; area ⊆ requirement areas; window ⊆ requirement windows; assigned unit; task type","EVT-CPL-ACTIVITY-ADDED","ACTIVITY_INVALID"),
  (["DRAFT"],"CMD-CPL-REMOVE-ACTIVITY","=","activity not yet tasked","EVT-CPL-ACTIVITY-REMOVED","ACTIVITY_ALREADY_TASKED"),
  (["DRAFT"],"CMD-CPL-ACTIVATE","ACTIVE","≥ 1 activity; creates one field task per activity through SLC-03 with plan_ref = this collection plan (CR-59)","EVT-CPL-ACTIVATED","PLAN_EMPTY"),
  (["ACTIVE"],"SYS:all activity tasks terminal","COMPLETED","SLC-03 events","EVT-CPL-COMPLETED",None),
  (["ACTIVE"],"CMD-CPL-COMPLETE","COMPLETED","planner; open tasks cancelled with reason","EVT-CPL-COMPLETED","REASON_REQUIRED"),
  (["DRAFT","ACTIVE"],"CMD-CPL-CANCEL","CANCELLED","reason; open tasks cancelled","EVT-CPL-CANCELLED","REASON_REQUIRED")],
 ["INV-CPL-01: every activity serves ≥ 1 EEI of an approved requirement","INV-CPL-02: tasks created by activation link back to the activity (REQ-COL-002)"],
 ["CollectionActivity (method, sources, area, window, unit, task_type, eei_refs, task_ref)"],["REQ-COL-002"])

PERPETUAL = {}
QUERIES = [
 ("QRY-CRQ-GET","BC02","GET","/api/v1/information/collection-requirements/{requirement_id}","Requirement with EEIs and fulfilment computed over observations visible to the caller","requester, collection managers; label rule","REQ-COL-003"),
 ("QRY-CRQ-BOARD","BC02","GET","/api/v1/information/collection-requirements","Requirements by area (bbox/polygon), state, priority, due","allowed_scope","REQ-COL-001"),
 ("QRY-CPL-GET","BC02","GET","/api/v1/information/collection-plans/{plan_id}","Plan with activities and linked tasks","planner scope","REQ-COL-002"),
 ("QRY-CRQ-EVIDENCE","BC02","GET","/api/v1/information/collection-requirements/{requirement_id}/fulfilment","Fulfilment links per EEI (visible observations only) with lineage","requester, collection managers","REQ-COL-003"),
]
ACTORS = {"CRQ":"Analyst / any requester (draft, edit, submit, satisfy, cancel) · collection manager (approve, reject, amend)","CPL":"collection planner"}
P = {
 "CMD-CRQ-DRAFT":"question!:LocalizedName label!:Label","CMD-CRQ-EDIT":"area!:object window!:Interval priority!:integer due!:date-time eeis!:array",
 "CMD-CRQ-SUBMIT":"","CMD-CRQ-APPROVE":"note:string","CMD-CRQ-REJECT":"reason!:string","CMD-CRQ-AMEND":"due:date-time area:object eeis:array reason!:string",
 "CMD-CRQ-MARK-SATISFIED":"acceptance_note:string","CMD-CRQ-CANCEL":"reason!:string",
 "CMD-CPL-CREATE":"requirements!:array title!:LocalizedName label!:Label","CMD-CPL-ADD-ACTIVITY":"method!:string sources!:array area!:object window!:Interval unit!:urn task_type!:urn eei_refs!:array",
 "CMD-CPL-REMOVE-ACTIVITY":"activity_id!:string","CMD-CPL-ACTIVATE":"","CMD-CPL-COMPLETE":"reason!:string","CMD-CPL-CANCEL":"reason!:string",
}
SYSTEM_CMDS = set()
RESOURCE = {"AGG-COLLECTION-REQUIREMENT":("information","collection-requirements"),"AGG-COLLECTION-PLAN":("information","collection-plans")}
SECURITY_AFFECTING = set()
CONSUMERS = {"AGG-COLLECTION-REQUIREMENT":["Matching engine (reload EEIs)","Collection board","Search projection (SLC-05)","Notification (requester)"],
 "AGG-COLLECTION-PLAN":["Task creation (SLC-03)","Notification (units)"],"default":["Search projection (SLC-05)"]}
CTX_OVERRIDE = {}

def enrich(spec, bc):
    S = spec["components"]["schemas"]
    S["EEI"] = {"type": "object", "required": ["id", "description"], "properties": {"id": {"type": "string"}, "description": {"$ref": "#/components/schemas/LocalizedName"},
        "entity_types": {"type": "array", "items": {"type": "string"}}, "predicates": {"type": "array", "items": {"type": "string"}},
        "observation_methods": {"type": "array", "items": {"type": "string"}}, "quantities": {"type": "array", "items": {"type": "string"}}}}
    for name, sch in S.items():
        if not name.endswith("Command") or "properties" not in sch: continue
        pr = sch["properties"]
        if name.startswith(("CrqEdit", "CrqAmend")): pr["eeis"] = {"type": "array", "minItems": 1, "items": {"$ref": "#/components/schemas/EEI"}}
        if name.startswith("CrqEdit"): pr["priority"] = {"type": "integer", "minimum": 1, "maximum": 5}
        if name.startswith("CplCreate"): pr["requirements"] = {"type": "array", "minItems": 1, "items": {"$ref": "#/components/schemas/Urn"}}
        if name.startswith("CplAddActivity"):
            pr["sources"] = {"type": "array", "minItems": 1, "items": {"$ref": "#/components/schemas/Urn"}}
            pr["eei_refs"] = {"type": "array", "minItems": 1, "items": {"type": "string"}}
```

## slc15_data.py

```python
# -*- coding: utf-8 -*-
# SLC-15 — Coordination cases (CAP-06.03) & Correlation / Fusion (CAP-04.04), R2
SLICE = "SLC-15"
AGGS = {}
def agg(id_, bc, name, tier, purpose, states, terminal, transitions, invariants, entities, reqs, notes=None, personal=False):
    AGGS[id_] = dict(id=id_, bc=bc, name=name, tier=tier, purpose=purpose, states=states, terminal=terminal,
                     transitions=transitions, invariants=invariants, entities=entities, requirements=reqs, notes=notes, personal_data=personal)

agg("AGG-COORDINATION-CASE","BC04","Coordination Case","T2","تنسيق بين وحدات/مؤسسات داخل المستأجر حول قرارات وخطط ومواقف مشتركة",
 ["OPEN","ACTIVE","CLOSED","CANCELLED"],["CLOSED","CANCELLED"],
 [("∅","CMD-CRD-OPEN","OPEN","title; purpose; lead organization; linked decisions/plans/situations visible to the opener; label","EVT-CRD-OPENED","COORDINATION_INVALID"),
  (["OPEN","ACTIVE"],"CMD-CRD-ADD-PARTICIPANT","=","org unit in the same tenant; participant role; access scope (sections); participant's members cleared for case label","EVT-CRD-PARTICIPANT-ADDED","PARTICIPANT_INVALID"),
  (["OPEN","ACTIVE"],"CMD-CRD-REMOVE-PARTICIPANT","=","not the lead; no open responsibilities","EVT-CRD-PARTICIPANT-REMOVED","PARTICIPANT_HAS_RESPONSIBILITIES"),
  (["OPEN"],"CMD-CRD-ACTIVATE","ACTIVE","≥ 2 participants","EVT-CRD-ACTIVATED","PARTICIPANTS_REQUIRED"),
  (["ACTIVE"],"CMD-CRD-ASSIGN-RESPONSIBILITY","=","participant exists; item, due; flag requires_authority (decision type) when the action needs that organization's authority","EVT-CRD-RESPONSIBILITY-ASSIGNED","RESPONSIBILITY_INVALID"),
  (["ACTIVE"],"CMD-CRD-UPDATE-RESPONSIBILITY","=","actor belongs to the responsible participant; status ∈ {in_progress, done, waived with reason}; items requiring authority cannot be done before the decision is recorded","EVT-CRD-RESPONSIBILITY-UPDATED","DECISION_PENDING"),
  (["ACTIVE"],"CMD-CRD-REQUEST-DECISION","=","responsibility requires authority; creates a Decision Request (SLC-08) in the participant's scope with the required decision type","EVT-CRD-DECISION-REQUESTED","RESPONSIBILITY_INVALID"),
  (["ACTIVE"],"SYS:linked decision recorded","=","decision references the request created by the case; outcome stored on the responsibility","EVT-CRD-DECISION-RECORDED",None),
  (["ACTIVE"],"CMD-CRD-CLOSE","CLOSED","all responsibilities done or waived; closing note","EVT-CRD-CLOSED","OPEN_RESPONSIBILITIES"),
  (["OPEN","ACTIVE"],"CMD-CRD-CANCEL","CANCELLED","lead; reason","EVT-CRD-CANCELLED","REASON_REQUIRED")],
 ["INV-CRD-01: coordination is within one tenant; cross-tenant coordination uses product distribution/export only (R2 decision)",
  "INV-CRD-02: each participant sees only its access scope (sections) and objects its members may see (REQ-CRD-001)",
  "INV-CRD-03: an action needing another organization's authority is never marked done without that authority's recorded decision (REQ-CRD-002, BRL-003)",
  "INV-CRD-04: the case links decisions and plans; it never replaces them"],
 ["Participant (org unit, role, access scope)","Responsibility (item, participant, due, requires_authority, decision_request, status)"],
 ["REQ-CRD-001","REQ-CRD-002"])

agg("AGG-CORRELATION-PROPOSAL","BC02","Correlation Proposal","T1","اقتراح ربط ملاحظات/ادعاءات من مصادر متعددة في المكان والزمان",
 ["PROPOSED","UNDER_REVIEW","ACCEPTED","REJECTED","EXPIRED"],["ACCEPTED","REJECTED","EXPIRED"],
 [("∅","SYS:correlation rule score ≥ threshold","PROPOSED","inputs from ≥ 2 distinct sources; no identical non-terminal proposal; label = max(input labels)","EVT-CRP-PROPOSED",None),
  ("∅","CMD-CRP-PROPOSE","PROPOSED","analyst; ≥ 2 visible inputs; kind; rationale","EVT-CRP-PROPOSED","CORRELATION_INVALID"),
  (["PROPOSED"],"CMD-CRP-START-REVIEW","UNDER_REVIEW","reviewer cleared for every input label","EVT-CRP-REVIEW-STARTED","REVIEWER_NOT_CLEARED"),
  (["UNDER_REVIEW"],"CMD-CRP-ACCEPT","ACCEPTED","effects through owner commands as the reviewer: same_event → Real-World Event + participation relationships + fused claims; co_location → relationship; same_entity → ER case (SLC-04); lineage lists every contributing source and its reliability","EVT-CRP-ACCEPTED","OWNER_REJECTED"),
  (["UNDER_REVIEW","PROPOSED"],"CMD-CRP-REJECT","REJECTED","reason (feeds rule evaluation)","EVT-CRP-REJECTED","REASON_REQUIRED"),
  (["PROPOSED"],"SYS:not reviewed within 30 days","EXPIRED","scheduler","EVT-CRP-EXPIRED",None)],
 ["INV-CRP-01: a proposal never changes claims, observations or entities; acceptance acts only through owner commands (REQ-FUS-001)",
  "INV-CRP-02: fused results record every contributing source and its reliability at fusion time (REQ-FUS-002)",
  "INV-CRP-03: no automatic acceptance",
  "INV-CRP-04: independence: two inputs derived from the same source (or one from the other) count as one source for corroboration"],
 ["ProposalInput (urn, source, reliability, label)","ScoreBreakdown"],["REQ-FUS-001","REQ-FUS-002"])

agg("AGG-CORRELATION-RULE","BC02","Correlation Rule","T2","قاعدة ربط زماني-مكاني بمعاملات وعتبة وتقييم",
 ["DRAFT","ACTIVE","RETIRED"],["RETIRED"],
 [("∅","CMD-CRR-DEFINE","DRAFT","kind ∈ {same_event, co_location, track_association, same_entity_hint}","EVT-CRR-DEFINED","RULE_INVALID"),
  (["DRAFT","ACTIVE"],"CMD-CRR-EDIT","=","parameters: max distance (m, accuracy-aware), time window, attribute similarity, min distinct sources, threshold; ACTIVE → new version","EVT-CRR-EDITED","RULE_INVALID"),
  (["DRAFT"],"CMD-CRR-ACTIVATE","ACTIVE","evaluation on a labelled set: precision ≥ 70 % of proposals (recalibrate after pilot); approver ≠ author","EVT-CRR-ACTIVATED","RULE_BELOW_TARGET"),
  (["ACTIVE"],"CMD-CRR-RETIRE","RETIRED","reason","EVT-CRR-RETIRED","REASON_REQUIRED")],
 ["INV-CRR-01: proposals record the rule version","INV-CRR-02: activation requires an evaluation report"],
 ["Parameters","EvaluationReport"],["REQ-FUS-001"])

PERPETUAL = {}
QUERIES = [
 ("QRY-CRD-GET","BC04","GET","/api/v1/operations/coordination-cases/{case_id}","Case filtered to the caller's participant scope","participants (scope-limited); lead","REQ-CRD-001"),
 ("QRY-CRD-LIST","BC04","GET","/api/v1/operations/coordination-cases","Cases where the caller's unit participates","allowed_scope","REQ-CRD-001"),
 ("QRY-CRP-QUEUE","BC02","GET","/api/v1/information/correlation-proposals","Proposals by kind, state, area, score (inputs all visible to caller)","Analyst","REQ-FUS-001"),
 ("QRY-CRP-GET","BC02","GET","/api/v1/information/correlation-proposals/{proposal_id}","Proposal with inputs, sources, reliabilities, score breakdown","reviewer cleared for all inputs","REQ-FUS-002"),
]
ACTORS = {"CRD":"lead organization Manager (open, participants, activate, assign, close, cancel) · participant members (update, request decision)",
          "CRP":"Analyst (propose, review, accept, reject)","CRR":"Analyst lead (define, edit) · second approver (activate)"}
P = {
 "CMD-CRD-OPEN":"title!:LocalizedName purpose!:LocalizedName lead_org!:urn links:array label!:Label","CMD-CRD-ADD-PARTICIPANT":"org_unit!:urn role!:string access_scope!:array",
 "CMD-CRD-REMOVE-PARTICIPANT":"org_unit!:urn reason!:string","CMD-CRD-ACTIVATE":"","CMD-CRD-ASSIGN-RESPONSIBILITY":"participant!:urn item!:LocalizedName due!:date-time requires_authority:string",
 "CMD-CRD-UPDATE-RESPONSIBILITY":"responsibility_id!:string status!:enum(in_progress,done,waived) note:string","CMD-CRD-REQUEST-DECISION":"responsibility_id!:string question!:LocalizedName options!:array",
 "CMD-CRD-CLOSE":"note!:LocalizedName","CMD-CRD-CANCEL":"reason!:string",
 "CMD-CRP-PROPOSE":"kind!:enum(same_event,co_location,track_association,same_entity_hint) inputs!:array rationale!:string","CMD-CRP-START-REVIEW":"",
 "CMD-CRP-ACCEPT":"note:string","CMD-CRP-REJECT":"reason!:string",
 "CMD-CRR-DEFINE":"kind!:enum(same_event,co_location,track_association,same_entity_hint) name!:string","CMD-CRR-EDIT":"parameters!:object","CMD-CRR-ACTIVATE":"evaluation_report!:urn","CMD-CRR-RETIRE":"reason!:string",
}
SYSTEM_CMDS = set()
RESOURCE = {"AGG-COORDINATION-CASE":("operations","coordination-cases"),"AGG-CORRELATION-PROPOSAL":("information","correlation-proposals"),"AGG-CORRELATION-RULE":("information","correlation-rules")}
SECURITY_AFFECTING = set()
CONSUMERS = {"AGG-COORDINATION-CASE":["Decision requests (SLC-08)","Notification (participants)","Search projection (SLC-05)"],
 "AGG-CORRELATION-PROPOSAL":["Owner commands on acceptance (BC02 events/relationships, SLC-04 ER)","Rule evaluation feedback"],
 "AGG-CORRELATION-RULE":["Correlation engine"],"default":["Search projection (SLC-05)"]}
CTX_OVERRIDE = {}

def enrich(spec, bc):
    S = spec["components"]["schemas"]
    if bc == "BC02":
        S["CorrelationParameters"] = {"type": "object", "required": ["time_window", "threshold"], "properties": {"max_distance_m": {"type": "number", "minimum": 0},
            "accuracy_aware": {"type": "boolean", "default": True}, "time_window": {"type": "string", "description": "ISO 8601 duration"},
            "attribute_similarity": {"type": "object"}, "min_distinct_sources": {"type": "integer", "minimum": 2, "default": 2}, "threshold": {"type": "number", "minimum": 0, "maximum": 1}}}
        for name, sch in S.items():
            if name.startswith("CrrEdit") and "properties" in sch: sch["properties"]["parameters"] = {"$ref": "#/components/schemas/CorrelationParameters"}
            if name.startswith("CrpPropose") and "properties" in sch: sch["properties"]["inputs"] = {"type": "array", "minItems": 2, "items": {"$ref": "#/components/schemas/Urn"}}
    if bc == "BC04":
        S["AccessScopeItem"] = {"type": "string", "enum": ["briefing", "own_responsibilities", "all_responsibilities", "linked_plans", "linked_decisions", "linked_situations"]}
        for name, sch in S.items():
            if name.startswith("CrdAddParticipant") and "properties" in sch: sch["properties"]["access_scope"] = {"type": "array", "minItems": 1, "items": {"$ref": "#/components/schemas/AccessScopeItem"}}
```

## slc16_data.py

```python
# -*- coding: utf-8 -*-
# SLC-16 — Enterprise integrations: ERP, HRIS, DMS, CMMS, sensors, CAP alerts (R2)
SLICE = "SLC-16"
AGGS = {}
def agg(id_, bc, name, tier, purpose, states, terminal, transitions, invariants, entities, reqs, notes=None, personal=False):
    AGGS[id_] = dict(id=id_, bc=bc, name=name, tier=tier, purpose=purpose, states=states, terminal=terminal,
                     transitions=transitions, invariants=invariants, entities=entities, requirements=reqs, notes=notes, personal_data=personal)

agg("AGG-INTEGRATION-CONNECTION","BC07","Integration Connection","T2","اتصال بنظام خارجي داخل حدود المؤسسة (ERP، HRIS، DMS، CMMS، بوابة حساسات، نقطة CAP)",
 ["DRAFT","TESTING","ACTIVE","DEGRADED","SUSPENDED","RETIRED"],["RETIRED"],
 [("∅","CMD-CON-REGISTER","DRAFT","system kind ∈ {erp, hris, dms, cmms, sensor_gateway, cap_endpoint}; endpoint on an internal network; protocol; direction ∈ {inbound, outbound}, outbound only for cap_endpoint in R2 (INV-CON-02); credentials stored in OpenBao (reference only)","EVT-CON-REGISTERED","CONNECTION_INVALID"),
  (["DRAFT"],"CMD-CON-TEST","TESTING","integration engineer; connectivity and schema probe run","EVT-CON-TEST-STARTED",None),
  (["TESTING"],"CMD-CON-ACTIVATE","ACTIVE","probe passed; egress allow-list entry approved by Security Officer ≠ requester (GOV-005)","EVT-CON-ACTIVATED","SEGREGATION_OF_DUTIES"),
  (["TESTING"],"CMD-CON-FAIL-TEST","DRAFT","probe failed; errors recorded","EVT-CON-TEST-FAILED",None),
  (["ACTIVE"],"SYS:health checks failing 5 min","DEGRADED","backlog buffered by adapters (QAS-INT-001)","EVT-CON-DEGRADED",None),
  (["DEGRADED"],"SYS:health restored","ACTIVE","backlog replayed","EVT-CON-RECOVERED",None),
  (["ACTIVE","DEGRADED"],"CMD-CON-SUSPEND","SUSPENDED","reason; egress rule disabled","EVT-CON-SUSPENDED","REASON_REQUIRED"),
  (["SUSPENDED"],"CMD-CON-RESUME","ACTIVE","egress rule re-enabled after re-check","EVT-CON-RESUMED",None),
  (["DRAFT","SUSPENDED"],"CMD-CON-RETIRE","RETIRED","no ACTIVE adapter or stream bound; egress rule removed","EVT-CON-RETIRED","CONNECTION_IN_USE")],
 ["INV-CON-01: every active connection has exactly one egress/ingress allow-list entry, approved by a Security Officer other than the requester",
  "INV-CON-02: no writes into ERP/HRIS/DMS/CMMS in R2 — external systems are sources, never sinks (BRL-013); the only outbound kind is CAP",
  "INV-CON-03: credentials never appear in specifications, logs or events — reference to OpenBao only"],
 ["HealthCheck","AllowListEntry"],["REQ-INT-001"])

agg("AGG-SENSOR-STREAM","BC07","Sensor Stream","T2","تدفق قياسات حساس مرتبط بمصدر وكمية ووحدة وفحوص جودة",
 ["DRAFT","ACTIVE","PAUSED","RETIRED"],["RETIRED"],
 [("∅","CMD-SNS-REGISTER","DRAFT","connection (sensor_gateway) exists; BC02 Source of type sensor ACTIVE; quantity + UCUM unit; expected rate; location or linked entity","EVT-SNS-REGISTERED","STREAM_INVALID"),
  (["DRAFT","ACTIVE","PAUSED"],"CMD-SNS-SET-QUALITY-RULES","=","range, rate-of-change, stale-after, duplicate window; violations become data_quality issues, not rejections","EVT-SNS-QUALITY-RULES-SET","QUALITY_RULES_INVALID"),
  (["DRAFT","PAUSED"],"CMD-SNS-ACTIVATE","ACTIVE","connection ACTIVE; mapping to CMD-OBS-RECORD batches tested","EVT-SNS-ACTIVATED","CONNECTION_NOT_ACTIVE"),
  (["ACTIVE"],"CMD-SNS-PAUSE","PAUSED","reason","EVT-SNS-PAUSED","REASON_REQUIRED"),
  (["ACTIVE"],"SYS:no data beyond stale-after","=","stream flagged STALE; alert to owner","EVT-SNS-STALE",None),
  (["DRAFT","PAUSED"],"CMD-SNS-RETIRE","RETIRED","reason","EVT-SNS-RETIRED","REASON_REQUIRED")],
 ["INV-SNS-01: sensor readings enter only as observations through BC02 batch commands (≤ 1,000 per batch, per-item idempotency) — REQ-INT-002",
  "INV-SNS-02: quality violations annotate data quality; they never silently drop readings",
  "INV-SNS-03: readings carry the sensor's own time as observed_at and server receipt as recorded_from"],
 ["QualityRules"],["REQ-INT-002"])

agg("AGG-HR-SYNC-PROPOSAL","BC01","HR Sync Proposal","T2","تغيير دور أو وحدة من HRIS يُقترح على المسؤول ولا يُطبق آلياً",
 ["PROPOSED","APPROVED","REJECTED","SUPERSEDED","EXPIRED"],["APPROVED","REJECTED","SUPERSEDED","EXPIRED"],
 [("∅","SYS:HRIS change received","PROPOSED","person matched to a platform Person by HR identifier; change ∈ {join, leave, move_unit, change_position}; mapped to proposed role-assignment changes by tenant mapping table","EVT-HRS-PROPOSED",None),
  (["PROPOSED"],"CMD-HRS-APPROVE","APPROVED","Administrator in scope of the affected units; applies CMD-RAS-ASSIGN / CMD-RAS-REVOKE and, for leave, CMD-USR-DISABLE — each through its own guards","EVT-HRS-APPROVED","OWNER_REJECTED"),
  (["PROPOSED"],"CMD-HRS-REJECT","REJECTED","reason","EVT-HRS-REJECTED","REASON_REQUIRED"),
  (["PROPOSED"],"SYS:newer HR change for the same person","SUPERSEDED","system","EVT-HRS-SUPERSEDED",None),
  (["PROPOSED"],"SYS:14 days without decision","EXPIRED","scheduler; escalated to Security Officer for leave events","EVT-HRS-EXPIRED",None)],
 ["INV-HRS-01: no role or access change is applied automatically from HRIS (REQ-INT-004, THR-S01-01)",
  "INV-HRS-02: 'leave' proposals are highlighted and escalated — access removal is time-critical",
  "INV-HRS-03: SCIM account disablement from the IdP remains immediate and independent of HR proposals (QAS-SEC-008)"],
 ["ProposedChange"],["REQ-INT-004"],personal=True)

agg("AGG-CAP-MESSAGE","BC03","CAP Message (outbound)","T2","رسالة تنبيه بصيغة CAP 1.2 تُصدر لنقطة خارجية مسموحة",
 ["PREPARED","SENT","FAILED","CANCELLED"],["SENT","CANCELLED"],
 [("∅","CMD-CAP-PREPARE","PREPARED","tenant CAP enabled; alert RAISED/ACKNOWLEDGED; alert label ≤ tenant external release level; content = CAP fields from a reviewed template (no free text from classified sources); target connection cap_endpoint ACTIVE","EVT-CAP-PREPARED","RELEASE_NOT_ALLOWED"),
  (["PREPARED"],"CMD-CAP-RELEASE","SENT","release authority ≠ preparer; valid CAP 1.2 (schema validated); delivery acknowledged","EVT-CAP-SENT","SEGREGATION_OF_DUTIES"),
  (["PREPARED"],"SYS:delivery failed after retries","FAILED","5 retries with backoff","EVT-CAP-FAILED",None),
  (["FAILED"],"CMD-CAP-RETRY","PREPARED","operator","EVT-CAP-RETRY",None),
  (["PREPARED","FAILED"],"CMD-CAP-CANCEL","CANCELLED","reason","EVT-CAP-CANCELLED","REASON_REQUIRED")],
 ["INV-CAP-01: nothing leaves the platform without a release decision by someone other than the preparer",
  "INV-CAP-02: CAP content is generated from a reviewed template and the alert's releasable fields only",
  "INV-CAP-03: inbound CAP messages arrive through an adapter as observations of a CAP source (SLC-02), never as direct alerts"],
 ["CapPayload"],["REQ-INT-003"])

PERPETUAL = {}
QUERIES = [
 ("QRY-CON-LIST","BC07","GET","/api/v1/integration/connections","Connections with state, health, allow-list entry","integration engineers, Security Officer","REQ-INT-001"),
 ("QRY-SNS-LIST","BC07","GET","/api/v1/integration/sensor-streams","Streams with rate, staleness, quality violation counts","integration engineers, Analyst","REQ-INT-002"),
 ("QRY-HRS-QUEUE","BC01","GET","/api/v1/foundation/hr-sync-proposals","Pending HR proposals by unit and change kind (leave first)","Administrator in scope, Security Officer","REQ-INT-004"),
 ("QRY-CAP-LIST","BC03","GET","/api/v1/intelligence/cap-messages","Outbound CAP messages by state","release authority, Auditor","REQ-INT-003"),
]
ACTORS = {"CON":"integration engineer (register, test) · Security Officer ≠ requester (activate) · Administrator (suspend, resume, retire)",
 "SNS":"integration engineer","HRS":"Administrator in scope","CAP":"alert recipient / duty officer (prepare) · release authority (release) · operator (retry, cancel)"}
P = {
 "CMD-CON-REGISTER":"name!:string system_kind!:enum(erp,hris,dms,cmms,sensor_gateway,cap_endpoint) endpoint!:string protocol!:string direction!:enum(inbound,outbound) credentials_ref!:string",
 "CMD-CON-TEST":"","CMD-CON-ACTIVATE":"allow_list_entry!:object","CMD-CON-FAIL-TEST":"errors!:array","CMD-CON-SUSPEND":"reason!:string","CMD-CON-RESUME":"","CMD-CON-RETIRE":"reason!:string",
 "CMD-SNS-REGISTER":"connection!:urn source!:urn quantity!:string unit!:string expected_rate!:number location:object linked_entity:urn",
 "CMD-SNS-SET-QUALITY-RULES":"rules!:object","CMD-SNS-ACTIVATE":"","CMD-SNS-PAUSE":"reason!:string","CMD-SNS-RETIRE":"reason!:string",
 "CMD-HRS-APPROVE":"note:string","CMD-HRS-REJECT":"reason!:string",
 "CMD-CAP-PREPARE":"alert!:urn template!:string connection!:urn","CMD-CAP-RELEASE":"note:string","CMD-CAP-RETRY":"","CMD-CAP-CANCEL":"reason!:string",
}
SYSTEM_CMDS = set()
RESOURCE = {"AGG-INTEGRATION-CONNECTION":("integration","connections"),"AGG-SENSOR-STREAM":("integration","sensor-streams"),
            "AGG-HR-SYNC-PROPOSAL":("foundation","hr-sync-proposals"),"AGG-CAP-MESSAGE":("intelligence","cap-messages")}
SECURITY_AFFECTING = {"EVT-HRS-APPROVED","EVT-CON-ACTIVATED","EVT-CON-SUSPENDED"}
CONSUMERS = {"AGG-INTEGRATION-CONNECTION":["Egress gateway (allow-list)","Adapters (bind/unbind)","Operations alerting"],
 "AGG-SENSOR-STREAM":["Ingestion workers (SLC-02 batches)","Operations alerting"],"AGG-HR-SYNC-PROPOSAL":["Role assignments / users (BC01)","Security Officer notification (leave)"],
 "AGG-CAP-MESSAGE":["CAP gateway","Audit"],"default":["Audit"]}
CTX_OVERRIDE = {}

def enrich(spec, bc):
    S = spec["components"]["schemas"]
    if bc == "BC07":
        S["AllowListEntry"] = {"type": "object", "required": ["host", "port", "direction"], "properties": {"host": {"type": "string"}, "port": {"type": "integer"}, "direction": {"enum": ["inbound", "outbound"]}, "justification": {"type": "string"}}}
        S["QualityRules"] = {"type": "object", "properties": {"min": {"type": "number"}, "max": {"type": "number"}, "max_rate_of_change": {"type": "number"},
            "stale_after": {"type": "string", "description": "ISO 8601 duration"}, "duplicate_window": {"type": "string"}}}
        for name, sch in S.items():
            if not name.endswith("Command") or "properties" not in sch: continue
            if name.startswith("ConActivate"): sch["properties"]["allow_list_entry"] = {"$ref": "#/components/schemas/AllowListEntry"}
            if name.startswith("SnsSetQualityRules"): sch["properties"]["rules"] = {"$ref": "#/components/schemas/QualityRules"}
```

## slc17_data.py

SLC-17 — Risk & Contingency (R3, scope-only design; G6 held per RSK-028)

```python
# -*- coding: utf-8 -*-
# SLC-17 — Risk & Contingency (CAP-09.01/02/03, DOM-17, BC04), R3 — scope-only design, G6 held (RSK-028)
SLICE = "SLC-17"
AGGS = {}
def agg(id_, bc, name, tier, purpose, states, terminal, transitions, invariants, entities, reqs, notes=None, personal=False):
    AGGS[id_] = dict(id=id_, bc=bc, name=name, tier=tier, purpose=purpose, states=states, terminal=terminal,
                     transitions=transitions, invariants=invariants, entities=entities, requirements=reqs, notes=notes, personal_data=personal)

agg("AGG-RISK","BC04","Risk","T2","تسجيل وتقييم ومعالجة مخاطر محتملة قبل وقوعها (استباقي، لا حادثة فعلية)",
 ["IDENTIFIED","ASSESSED","TREATED","CLOSED"],["CLOSED"],
 [("∅","CMD-RIS-IDENTIFY","IDENTIFIED","category_ref (RD-HAZARD-CATEGORIES، مرجع لكل مستأجر — نمط R2-Q1)؛ description؛ scope_refs ≥ 1 (أصل/منطقة/منظمة/خطة)؛ label ≥ تصنيف النطاق","EVT-RIS-IDENTIFIED","RISK_INVALID"),
  (["IDENTIFIED"],"CMD-RIS-ASSESS","ASSESSED","likelihood ∈ 1..5؛ impact ∈ 1..5؛ risk_score محسوب لا يُدخَل مباشرة (INV-RIS-02)؛ المقيّم ≠ المحدِّد عند سياسة فصل الواجبات (INV-RIS-01)","EVT-RIS-ASSESSED","SEGREGATION_OF_DUTIES"),
  (["ASSESSED"],"CMD-RIS-PLAN-TREATMENT","TREATED","treatment_strategy ∈ {avoid,reduce,transfer,accept}؛ ≥ 1 إجراء معالجة إلا عند accept (INV-RIS-03)؛ موافق مخوَّل","EVT-RIS-TREATMENT-PLANNED","TREATMENT_INVALID"),
  (["ASSESSED","TREATED"],"CMD-RIS-REASSESS","ASSESSED","likelihood/impact جديدان؛ سبب؛ المقيّم ≠ المحدِّد عند سياسة فصل الواجبات","EVT-RIS-REASSESSED","SEGREGATION_OF_DUTIES"),
  (["IDENTIFIED","ASSESSED","TREATED"],"CMD-RIS-CLOSE","CLOSED","rationale ∈ {retired,accepted_permanently,materialized}؛ إن كان materialized فـ incident_ref إلزامي (INV-RIS-04)؛ لا أمر لإعادة الفتح — الخطر المُعاد تحديده خطر جديد","EVT-RIS-CLOSED","RATIONALE_REQUIRED"),
  ("*NT","SYS:incident references this risk as risk_ref","=","رابط تلقائي عند تسجيل حادثة تحقَّق منها هذا الخطر؛ لا يغيّر حالة الخطر تلقائياً أبداً (INV-RIS-05)","EVT-RIS-MATERIALIZATION-LINKED",None)],
 ["INV-RIS-01: المقيّم ≠ المحدِّد عند سياسة المستأجر لفصل الواجبات (يماثل INV-TASK-07)",
  "INV-RIS-02: risk_score = likelihood × impact، محسوب عند كل تقييم، لا يُدخله الفاعل مباشرة",
  "INV-RIS-03: TREATED يتطلب ≥ 1 إجراء معالجة مرتبط إلا إذا كانت الاستراتيجية accept بموافقة مخوَّلة صريحة",
  "INV-RIS-04: CLOSED يتطلب rationale صريحاً دائماً؛ لا يوجد أمر لإعادة فتح خطر مُغلَق — إعادة تحديده تنشئ Risk جديداً",
  "INV-RIS-05: ربط حادثة متحقِّقة بهذا الخطر (risk_ref) لا يغيّر حالة الخطر تلقائياً أبداً؛ مالك الخطر يتصرف بأمر منفصل (لا أثر جانبي صامت — درس SLC-09)"],
 ["TreatmentAction (treatment_task_ref, status)"],
 ["REQ-RCM-001","REQ-RCM-002","REQ-RCM-003","REQ-RCM-004","REQ-RCM-005"])

agg("AGG-INCIDENT","BC04","Incident","T1","تتبّع حادثة فعلية من التبليغ حتى الإغلاق، بما فيها تصعيدها لطارئ/أزمة والاستجابة والتعافي",
 ["REPORTED","ASSESSED","RESPONDING","CONTAINED","RESOLVED"],["CLOSED","CANCELLED"],
 [("∅","CMD-INC-REPORT","REPORTED","category_ref (RD-HAZARD-CATEGORIES)؛ description؛ scope_refs ≥ 1؛ risk_ref اختياري (خطر تحقَّق)؛ severity ابتدائية MINOR؛ label ≥ تصنيف النطاق","EVT-INC-REPORTED","INCIDENT_INVALID"),
  (["REPORTED"],"CMD-INC-ASSESS","ASSESSED","severity ∈ {MINOR,MAJOR,EMERGENCY,CRISIS}؛ affected_scope_refs؛ مقيّم مخوَّل","EVT-INC-ASSESSED","INCIDENT_INVALID"),
  (["ASSESSED"],"CMD-INC-DISPATCH-RESPONSE","RESPONDING","commander؛ ≥ 1 response_task_ref (مهام SLC-03 مرتبطة عبر incident_ref — CR-61)","EVT-INC-RESPONSE-DISPATCHED","RESPONSE_REQUIRED"),
  (["RESPONDING"],"CMD-INC-CONTAIN","CONTAINED","القائد يؤكد الاحتواء؛ ملاحظة احتواء","EVT-INC-CONTAINED","REASON_REQUIRED"),
  (["CONTAINED"],"CMD-INC-RESOLVE","RESOLVED","كل مهام الاستجابة في حالة نهائية (INV-INC-02)؛ ملاحظة حل","EVT-INC-RESOLVED","RESPONSE_TASKS_OPEN"),
  (["RESOLVED"],"CMD-INC-CLOSE","CLOSED","ملاحظة إغلاق؛ after_action_ref اختياري (كائن معرفة، SLC-12 — R3-Q5)","EVT-INC-CLOSED","REASON_REQUIRED"),
  (["REPORTED"],"CMD-INC-CANCEL","CANCELLED","سبب (إنذار كاذب)","EVT-INC-CANCELLED","REASON_REQUIRED"),
  ("*NT","CMD-INC-ESCALATE","=","سبب؛ new_severity أعلى من الحالية فقط (INV-INC-01)؛ إشعار المستوى الأعلى","EVT-INC-ESCALATED","SEVERITY_MUST_INCREASE"),
  ("*NT","CMD-INC-DE-ESCALATE","=","سلطة؛ سبب؛ new_severity أدنى بمستوى واحد كحد أقصى (INV-INC-01)","EVT-INC-DE-ESCALATED","REASON_REQUIRED"),
  ("*NT","CMD-INC-ACTIVATE-CONTINGENCY","=","سلطة؛ ينشئ/يربط Plan (SLC-08، plan_kind=CONTINGENCY، triggered_by=هذه الحادثة — CR-60)؛ أمر صريح دائماً، ليس أثراً تلقائياً للتصعيد (INV-INC-03)","EVT-INC-CONTINGENCY-ACTIVATED","PLAN_LINK_INVALID"),
  ([ "REPORTED","ASSESSED"],"SYS:response SLA elapsed without dispatch","=","المجدول؛ SLA حسب severity، موسوم 'تُعاد معايرته بعد Pilot R1/R2' (RSK-028)","EVT-INC-SLA-BREACHED",None)],
 ["INV-INC-01: severity تزداد فقط عبر CMD-INC-ESCALATE وتنقص فقط عبر CMD-INC-DE-ESCALATE؛ لا تتغير كأثر جانبي لأي أمر آخر",
  "INV-INC-02: CLOSED فقط عندما تكون كل مهمة استجابة مرتبطة في حالة نهائية (يماثل PLAN.COMPLETE وTASK.CLOSE)",
  "INV-INC-03: تفعيل خطة الاستمرارية أمر صريح مخوَّل دائماً، ليس أثراً تلقائياً لتصعيد الخطورة وحده",
  "INV-INC-04: خطر مرتبط (risk_ref) لا تتغير حالته تلقائياً أبداً بإنشاء هذه الحادثة أو تصعيدها أو إغلاقها؛ مالك الخطر يتصرف بأمر منفصل (يماثل INV-RIS-05)",
  "INV-INC-05: كل أمر مقبول ينتج حدثاً واحداً بالضبط وسجل تدقيق واحداً"],
 ["SeverityHistory (from, to, at, reason)"],
 ["REQ-RCM-006","REQ-RCM-007","REQ-RCM-008","REQ-RCM-009","REQ-RCM-010","REQ-RCM-011","REQ-RCM-012","REQ-RCM-013"])

PERPETUAL = {}
QUERIES = [
 ("QRY-RIS-GET","BC04","GET","/api/v1/operations/risks/{risk_id}","Risk بنطاقه المرئي للطالب","مالك النطاق؛ مدير المخاطر","REQ-RCM-014"),
 ("QRY-RIS-REGISTER","BC04","GET","/api/v1/operations/risks","سجل المخاطر مصفّى بالفئة/النطاق/الدرجة","allowed_scope","REQ-RCM-014"),
 ("QRY-INC-GET","BC04","GET","/api/v1/operations/incidents/{incident_id}","Incident بنطاقه المرئي للطالب","allowed_scope","REQ-RCM-015"),
 ("QRY-INC-LIST","BC04","GET","/api/v1/operations/incidents","حوادث مصفّاة بالفئة/الخطورة/الحالة/النطاق","allowed_scope","REQ-RCM-015"),
 ("QRY-INC-RECOVERY-STATUS","BC04","GET","/api/v1/operations/incidents/{incident_id}/recovery-status","تقدم التعافي المحسوب من مهام خطة الاستمرارية المرتبطة مقابل زمن بدء الحادثة (RTO/RPO تقديرية)","القائد؛ مالك الاستمرارية","REQ-RCM-016"),
]
ACTORS = {"RIS":"محدِّد الخطر (تحديد) · مقيّم (تقييم، إعادة تقييم) · موافق المعالجة (تخطيط المعالجة) · مدير المخاطر (إغلاق)",
          "INC":"أي مُبلِّغ مخوَّل (تبليغ، إلغاء) · مقيّم الحادثة (تقييم) · قائد الحادثة (استجابة، احتواء، حل، إغلاق، تصعيد، تخفيض، تفعيل الاستمرارية)"}
P = {
 "CMD-RIS-IDENTIFY":"category_ref!:urn description!:LocalizedName scope_refs!:array label!:Label",
 "CMD-RIS-ASSESS":"likelihood!:integer impact!:integer",
 "CMD-RIS-PLAN-TREATMENT":"treatment_strategy!:enum(avoid,reduce,transfer,accept) treatment_task_refs:array approver!:urn",
 "CMD-RIS-REASSESS":"likelihood!:integer impact!:integer reason!:string",
 "CMD-RIS-CLOSE":"rationale!:enum(retired,accepted_permanently,materialized) incident_ref:urn",
 "CMD-INC-REPORT":"category_ref!:urn description!:LocalizedName scope_refs!:array risk_ref:urn label!:Label",
 "CMD-INC-ASSESS":"severity!:enum(MINOR,MAJOR,EMERGENCY,CRISIS) affected_scope_refs!:array",
 "CMD-INC-DISPATCH-RESPONSE":"commander!:urn response_task_refs!:array",
 "CMD-INC-CONTAIN":"containment_note!:string",
 "CMD-INC-RESOLVE":"resolution_note!:string",
 "CMD-INC-CLOSE":"closing_note!:string after_action_ref:urn",
 "CMD-INC-CANCEL":"reason!:string",
 "CMD-INC-ESCALATE":"reason!:string new_severity!:enum(MINOR,MAJOR,EMERGENCY,CRISIS)",
 "CMD-INC-DE-ESCALATE":"reason!:string new_severity!:enum(MINOR,MAJOR,EMERGENCY,CRISIS)",
 "CMD-INC-ACTIVATE-CONTINGENCY":"plan_template_ref!:urn",
}
SYSTEM_CMDS = set()
RESOURCE = {"AGG-RISK":("operations","risks"),"AGG-INCIDENT":("operations","incidents")}
SECURITY_AFFECTING = set()
CONSUMERS = {"AGG-RISK":["Search projection (SLC-05)","Coordination cases (SLC-15، عند ارتباط النطاق)"],
 "AGG-INCIDENT":["Search projection (SLC-05)","Notification (SLC-06)","اقتراحات كائن المعرفة (SLC-12، بعد الإغلاق — R3-Q5)"],
 "default":["Search projection (SLC-05)"]}
CTX_OVERRIDE = {}

def enrich(spec, bc):
    S = spec["components"]["schemas"]
    if bc == "BC04":
        for name, sch in S.items():
            if "properties" in sch:
                for f in ("scope_refs","affected_scope_refs","response_task_refs","treatment_task_refs"):
                    if f in sch["properties"] and sch["properties"][f].get("type") == "array":
                        sch["properties"][f]["items"] = {"$ref": "#/components/schemas/Urn"}

```

## slc18_data.py

SLC-18 — Logistics & Supply (R3, scope-only design; G6 held per RSK-028; reuses SLC-09's Resource Pool/Allocation for inventory per R3-Q3, corrected by CR-62)

```python
# -*- coding: utf-8 -*-
# SLC-18 — Logistics & Supply (CAP-08.03, DOM-16, BC05), R3 — scope-only design, G6 held (RSK-028)
SLICE = "SLC-18"
APPROVED_AT = "2026-09-27"
AGGS = {}
def agg(id_, bc, name, tier, purpose, states, terminal, transitions, invariants, entities, reqs, notes=None, personal=False):
    AGGS[id_] = dict(id=id_, bc=bc, name=name, tier=tier, purpose=purpose, states=states, terminal=terminal,
                     transitions=transitions, invariants=invariants, entities=entities, requirements=reqs, notes=notes, personal_data=personal)

agg("AGG-LOGISTICS-REQUEST","BC05","Logistics Request","T2","طلب كمية من صنف إمداد لوجهة؛ يقود إلى تخصيص من دفتر سعة المخزون (SLC-09) وشحنة تُنفّذه",
 ["REQUESTED","PENDING_APPROVAL","APPROVED","IN_TRANSIT"],["FULFILLED","PARTIALLY_FULFILLED","REJECTED","CANCELLED"],
 [("∅","CMD-LGR-REQUEST","REQUESTED","item pool ACTIVE (AGG-RESOURCE-POOL, resource_type in RD-LOGISTICS-ITEM-TYPES); quantity > 0 in pool unit; destination; needed_by; priority 1–5; requester; justification; system issues a linked allocation request in the same unit of work (CMD-ALC-REQUEST, target = this request — CR-62)","EVT-LGR-REQUESTED","LOGISTICS_REQUEST_INVALID"),
  (["REQUESTED"],"SYS:linked allocation committed","APPROVED","SLC-09 EVT-ALC-COMMITTED for the linked allocation","EVT-LGR-APPROVED",None),
  (["REQUESTED"],"SYS:linked allocation requires approval","PENDING_APPROVAL","SLC-09 EVT-ALC-APPROVAL-REQUIRED for the linked allocation","EVT-LGR-PENDING-APPROVAL",None),
  (["REQUESTED"],"SYS:linked allocation rejected","REJECTED","SLC-09 EVT-ALC-REJECTED for the linked allocation; reason codes carried over","EVT-LGR-REJECTED",None),
  (["PENDING_APPROVAL"],"SYS:linked allocation committed","APPROVED","SLC-09 EVT-ALC-COMMITTED for the linked allocation","EVT-LGR-APPROVED",None),
  (["PENDING_APPROVAL"],"SYS:linked allocation rejected","REJECTED","SLC-09 EVT-ALC-REJECTED for the linked allocation (approval denied or provisional hold elapsed)","EVT-LGR-REJECTED",None),
  (["APPROVED"],"CMD-LGR-DISPATCH","IN_TRANSIT","dispatcher; linked allocation still COMMITTED; creates a Shipment (AGG-SHIPMENT) referencing this request and the allocation; ship_quantity ≤ requested quantity","EVT-LGR-DISPATCHED","ALLOCATION_NOT_COMMITTED"),
  (["IN_TRANSIT"],"SYS:linked shipment delivered in full","FULFILLED","SLC-18 EVT-SHP-DELIVERED with delivered_quantity = requested quantity; records consumption on the linked allocation (CMD-ALC-RECORD-CONSUMPTION)","EVT-LGR-FULFILLED",None),
  (["IN_TRANSIT"],"SYS:linked shipment resolved short","PARTIALLY_FULFILLED","SLC-18 EVT-SHP-DELIVERED with delivered_quantity < requested quantity, or EVT-SHP-DAMAGED / EVT-SHP-LOST; records consumption for the quantity actually delivered before the incident (possibly zero)","EVT-LGR-PARTIALLY-FULFILLED",None),
  (["REQUESTED","PENDING_APPROVAL","APPROVED"],"CMD-LGR-CANCEL","CANCELLED","requester or logistics authority; reason; releases the linked allocation if COMMITTED (CMD-ALC-RELEASE), or leaves a PENDING_APPROVAL allocation to its own provisional-hold expiry","EVT-LGR-CANCELLED","REASON_REQUIRED")],
 ["INV-LGR-01: every REQUESTED logistics request creates exactly one linked resource allocation in the same unit of work, targeting this request (CR-62); the two never diverge except through each other's own system-driven events",
  "INV-LGR-02: dispatch (IN_TRANSIT) is only possible from APPROVED, only while the linked allocation is still COMMITTED, and only for a ship_quantity not exceeding the requested quantity",
  "INV-LGR-03: FULFILLED requires delivered_quantity = requested quantity; anything less, including a total loss, is PARTIALLY_FULFILLED — never silently marked FULFILLED",
  "INV-LGR-04: cancellation always releases or lets expire the linked allocation; a CANCELLED request never leaves a dangling COMMITTED allocation",
  "INV-LGR-05: consumption is recorded on the linked allocation only from confirmed shipment outcomes (SLC-18 EVT-SHP-DELIVERED/-DAMAGED/-LOST), never speculatively at dispatch time"],
 [],["REQ-LOG-001","REQ-LOG-002","REQ-LOG-003","REQ-LOG-008","REQ-LOG-009","REQ-LOG-013","REQ-LOG-014"])

agg("AGG-SHIPMENT","BC05","Shipment","T2","نقل كمية من صنف إمداد من موقع تخزين إلى وجهة تلبيةً لطلب إمداد، بتتبع نقاط حركة",
 ["PLANNED","IN_TRANSIT"],["DELIVERED","DAMAGED","LOST","CANCELLED"],
 [("∅","CMD-SHP-PLAN","PLANNED","logistics_request APPROVED; origin pool with sufficient COMMITTED allocation quantity for the linked request; destination; carrier; planned_quantity ≤ the linked allocation's committed quantity","EVT-SHP-PLANNED","SHIPMENT_INVALID"),
  (["PLANNED"],"CMD-SHP-DEPART","IN_TRANSIT","carrier confirmed; departure checkpoint recorded","EVT-SHP-DEPARTED","DEPARTURE_INVALID"),
  (["IN_TRANSIT"],"CMD-SHP-RECORD-CHECKPOINT","=","checkpoint strictly after the previous checkpoint in time (append-only, gapless — mirrors INV-AST-02); location; at; note","EVT-SHP-CHECKPOINT-RECORDED","CHECKPOINT_INVALID"),
  (["IN_TRANSIT"],"CMD-SHP-DELIVER","DELIVERED","receiving party confirms; delivered_quantity ≤ planned quantity; a shortfall is recorded, never hidden (INV-SHP-02)","EVT-SHP-DELIVERED","DELIVERY_INVALID"),
  (["IN_TRANSIT"],"CMD-SHP-REPORT-DAMAGE","DAMAGED","reason; damaged_quantity ≤ planned quantity; evidence","EVT-SHP-DAMAGED","REASON_REQUIRED"),
  (["IN_TRANSIT"],"CMD-SHP-REPORT-LOST","LOST","reason","EVT-SHP-LOST","REASON_REQUIRED"),
  (["PLANNED"],"CMD-SHP-CANCEL","CANCELLED","reason; only before departure","EVT-SHP-CANCELLED","REASON_REQUIRED")],
 ["INV-SHP-01: movement history (checkpoints) is append-only and chronologically gapless; no checkpoint is ever edited or removed (mirrors INV-AST-02's gapless custody chain)",
  "INV-SHP-02: delivered, damaged or lost quantity never exceeds the shipment's planned quantity; a shortfall at delivery is recorded on the event, never silently rounded up to delivered in full",
  "INV-SHP-03: departure (IN_TRANSIT) requires the linked logistics request's allocation to still be COMMITTED for at least the shipped quantity at that instant — no shipment ever moves against capacity that was never actually reserved",
  "INV-SHP-04: cancellation is only possible before departure (PLANNED); once IN_TRANSIT the shipment must resolve to DELIVERED, DAMAGED or LOST — never silently cancelled mid-transit"],
 ["MovementEvent (location, at, note)"],["REQ-LOG-004","REQ-LOG-005","REQ-LOG-006","REQ-LOG-007","REQ-LOG-009"])

PERPETUAL = {}
QUERIES = [
 ("QRY-LGR-GET","BC05","GET","/api/v1/readiness/logistics-requests/{request_id}","Logistics request with linked allocation and shipment refs","label rule; allowed_scope","REQ-LOG-010"),
 ("QRY-LGR-LIST","BC05","GET","/api/v1/readiness/logistics-requests","Logistics requests filtered by item, destination, state, priority","allowed_scope","REQ-LOG-010"),
 ("QRY-SHP-GET","BC05","GET","/api/v1/readiness/shipments/{shipment_id}","Shipment with current state and delivered/damaged/lost quantity","allowed_scope","REQ-LOG-011"),
 ("QRY-SHP-LIST","BC05","GET","/api/v1/readiness/shipments","Shipments filtered by logistics request, carrier, state, window","allowed_scope","REQ-LOG-011"),
 ("QRY-SHP-TRACKING","BC05","GET","/api/v1/readiness/shipments/{shipment_id}/checkpoints","Full checkpoint history of a shipment, in order","allowed_scope","REQ-LOG-012"),
]
ACTORS = {"LGR":"Logistics Officer / Planner (request, cancel) · dispatcher (dispatch)",
 "SHP":"dispatcher / carrier operator (plan, depart, checkpoint, deliver, report damage, report lost, cancel)"}
P = {
 "CMD-LGR-REQUEST":"item_pool!:urn quantity!:number destination!:LocalizedName needed_by!:date-time priority!:integer justification:string",
 "CMD-LGR-DISPATCH":"carrier!:string ship_quantity!:number",
 "CMD-LGR-CANCEL":"reason!:string",
 "CMD-SHP-PLAN":"logistics_request!:urn origin_pool!:urn destination!:LocalizedName carrier!:string planned_quantity!:number",
 "CMD-SHP-DEPART":"note:string",
 "CMD-SHP-RECORD-CHECKPOINT":"location!:LocalizedName at!:date-time note:string",
 "CMD-SHP-DELIVER":"delivered_quantity!:number received_by!:urn note:string",
 "CMD-SHP-REPORT-DAMAGE":"damaged_quantity!:number reason!:string evidence:urn",
 "CMD-SHP-REPORT-LOST":"reason!:string",
 "CMD-SHP-CANCEL":"reason!:string",
}
SYSTEM_CMDS = set()
RESOURCE = {"AGG-LOGISTICS-REQUEST":("readiness","logistics-requests"),"AGG-SHIPMENT":("readiness","shipments")}
SECURITY_AFFECTING = set()
CONSUMERS = {"AGG-LOGISTICS-REQUEST":["Capacity ledger (via linked allocation, SLC-09)","Search projection (SLC-05)"],
 "AGG-SHIPMENT":["Logistics Request (fulfillment status)","Search projection (SLC-05)"],
 "default":["Search projection (SLC-05)"]}
CTX_OVERRIDE = {}

def enrich(spec, bc):
    S = spec["components"]["schemas"]
    for name, sch in S.items():
        if not name.endswith("Command") or "properties" not in sch: continue
        pr = sch["properties"]
        if name.startswith("LgrRequest"): pr["priority"] = {"type": "integer", "minimum": 1, "maximum": 5}
```

## slc19_data.py

SLC-19 — Training, Competency & Exercises (R3, third and last R3 slice; G6 held per RSK-028; extends SLC-03's Qualification Record and SLC-09's Role Requirement unmodified, corrects SLC-12's Knowledge Object guard text only per CR-63)

```python
# -*- coding: utf-8 -*-
# SLC-19 — Training, Competency & Exercises (CAP-08.05, DOM-18+19, BC05), R3 — scope-only design, G6 held (RSK-028)
SLICE = "SLC-19"
AGGS = {}
def agg(id_, bc, name, tier, purpose, states, terminal, transitions, invariants, entities, reqs, notes=None, personal=False):
    AGGS[id_] = dict(id=id_, bc=bc, name=name, tier=tier, purpose=purpose, states=states, terminal=terminal,
                     transitions=transitions, invariants=invariants, entities=entities, requirements=reqs, notes=notes, personal_data=personal)

agg("AGG-SCENARIO","BC05","Scenario","T2","تعريف قابل لإعادة الاستخدام لتمرين تدريبي: موقف، أهداف، كفاءات مستهدفة، وحقن مرتبة زمنياً",
 ["DRAFT","ACTIVE","RETIRED"],["RETIRED"],
 [("∅","CMD-SCN-DEFINE","DRAFT","title; exercise_type_ref in RD-EXERCISE-TYPES; situation; target_competencies ⊆ RD-COMPETENCIES; injects ordered by strictly increasing offset (INV-SCN-01)","EVT-SCN-DEFINED","SCENARIO_INVALID"),
  (["DRAFT","ACTIVE"],"CMD-SCN-EDIT","=","same validations as DEFINE; editing an ACTIVE scenario creates a new version — exercises already planned against the prior version keep their frozen reference (INV-EXR-01)","EVT-SCN-EDITED","SCENARIO_INVALID"),
  (["DRAFT"],"CMD-SCN-ACTIVATE","ACTIVE","approver ≠ author","EVT-SCN-ACTIVATED","SEGREGATION_OF_DUTIES"),
  (["ACTIVE"],"CMD-SCN-RETIRE","RETIRED","reason","EVT-SCN-RETIRED","REASON_REQUIRED")],
 ["INV-SCN-01: injects are ordered by strictly increasing offset from exercise start; no simultaneous or decreasing offsets",
  "INV-SCN-02: target competencies reference RD-COMPETENCIES codes; no invented closed catalog"],
 ["Inject (offset_minutes, description, expected_response)"],
 ["REQ-TRX-001","REQ-TRX-002"])

agg("AGG-EXERCISE","BC05","Exercise","T2","حدث تدريبي/جاهزية مجدوَل ينفّذ سيناريو محدَّداً لمجموعة مشاركين",
 ["PLANNED","SCHEDULED","IN_PROGRESS","COMPLETED","ABORTED","CANCELLED"],["COMPLETED","ABORTED","CANCELLED"],
 [("∅","CMD-EXR-PLAN","PLANNED","scenario ACTIVE at this instant, frozen thereafter (INV-EXR-01); objectives; participants; purpose; role_ref optional (readiness comparison reuses SLC-09's AGG-ROLE-REQUIREMENT read-only, no new eligibility mechanism)","EVT-EXR-PLANNED","EXERCISE_INVALID"),
  (["PLANNED"],"CMD-EXR-SCHEDULE","SCHEDULED","window.from < window.to; location; participants confirmed","EVT-EXR-SCHEDULED","EXERCISE_INVALID"),
  (["SCHEDULED"],"CMD-EXR-START","IN_PROGRESS","scheduled window reached (or authorized override); system creates a linked Simulation in the same unit of work (CMD-SIM-START, exercise_ref = this, scenario_ref = the frozen scenario — mirrors the linked-creation pattern of CR-62)","EVT-EXR-STARTED","EXERCISE_INVALID"),
  (["IN_PROGRESS"],"SYS:linked simulation completed","COMPLETED","system; driven exclusively by the linked Simulation's own EVT-SIM-COMPLETED (INV-EXR-02)","EVT-EXR-COMPLETED",None),
  (["IN_PROGRESS"],"SYS:linked simulation aborted","ABORTED","system; driven exclusively by the linked Simulation's own EVT-SIM-ABORTED (INV-EXR-02)","EVT-EXR-ABORTED",None),
  (["PLANNED","SCHEDULED"],"CMD-EXR-CANCEL","CANCELLED","reason","EVT-EXR-CANCELLED","REASON_REQUIRED")],
 ["INV-EXR-01: an exercise is planned only against a scenario that is ACTIVE at that instant; the reference is frozen — later scenario edits (new versions) never retroactively change an already-planned exercise",
  "INV-EXR-02: an exercise's terminal outcome (COMPLETED vs ABORTED) is always driven exclusively by its linked simulation's own outcome; no human command sets either state directly"],
 [],
 ["REQ-TRX-003","REQ-TRX-004","REQ-TRX-005","REQ-TRX-006","REQ-TRX-007"])

agg("AGG-SIMULATION","BC05","Simulation","T2","تنفيذ فعلي واحد لتمرين: تسليم الحقن، تسجيل التقييمات، والانتهاء إلى نتيجة نهائية",
 ["IN_PROGRESS","PAUSED","COMPLETED","ABORTED"],["COMPLETED","ABORTED"],
 [("∅","CMD-SIM-START","IN_PROGRESS","system-issued in the same unit of work as CMD-EXR-START; exercise_ref SCHEDULED transitioning to IN_PROGRESS; scenario_ref = the exercise's frozen scenario; started_at","EVT-SIM-STARTED","SIMULATION_INVALID"),
  (["IN_PROGRESS"],"CMD-SIM-DELIVER-INJECT","=","inject_ref belongs to the linked scenario; delivered_at strictly after the previous delivery (INV-SIM-01)","EVT-SIM-INJECT-DELIVERED","INJECT_INVALID"),
  (["IN_PROGRESS","PAUSED"],"CMD-SIM-RECORD-EVALUATION","=","participant_ref is one of the linked exercise's participants; competency_code in RD-COMPETENCIES; result ∈ {MET, PARTIAL, NOT_MET}; evaluator ≠ participant (INV-SIM-03)","EVT-SIM-EVALUATION-RECORDED","SEGREGATION_OF_DUTIES"),
  (["IN_PROGRESS"],"CMD-SIM-PAUSE","PAUSED","reason","EVT-SIM-PAUSED","REASON_REQUIRED"),
  (["PAUSED"],"CMD-SIM-RESUME","IN_PROGRESS","—","EVT-SIM-RESUMED",None),
  (["IN_PROGRESS","PAUSED"],"CMD-SIM-COMPLETE","COMPLETED","every participant on the linked exercise has ≥ 1 recorded evaluation (INV-SIM-02)","EVT-SIM-COMPLETED","EVALUATION_MISSING"),
  (["IN_PROGRESS","PAUSED"],"CMD-SIM-ABORT","ABORTED","reason","EVT-SIM-ABORTED","REASON_REQUIRED")],
 ["INV-SIM-01: inject deliveries are append-only and strictly increasing in time (mirrors INV-SHP-01's checkpoint pattern); no edit or delete command exists",
  "INV-SIM-02: a simulation reaches COMPLETED only when every participant listed on its linked exercise has at least one recorded evaluation",
  "INV-SIM-03: an evaluator never evaluates themself (segregation of duties, mirrors CMD-RRQ-ACTIVATE/CMD-KNO-PUBLISH's reviewer ≠ author pattern)"],
 ["InjectDelivery (inject_ref, delivered_at, note)","Evaluation (participant_ref, competency_code, result, evaluator, notes)"],
 ["REQ-TRX-008","REQ-TRX-009","REQ-TRX-010","REQ-TRX-011"])

PERPETUAL = {}
QUERIES = [
 ("QRY-SCN-GET","BC05","GET","/api/v1/readiness/scenarios/{scenario_id}","Scenario with injects and target competencies","allowed_scope","REQ-TRX-014"),
 ("QRY-SCN-LIST","BC05","GET","/api/v1/readiness/scenarios","Scenarios filtered by exercise type, state","allowed_scope","REQ-TRX-014"),
 ("QRY-EXR-GET","BC05","GET","/api/v1/readiness/exercises/{exercise_id}","Exercise with frozen scenario reference, participants, current state","allowed_scope","REQ-TRX-014"),
 ("QRY-EXR-LIST","BC05","GET","/api/v1/readiness/exercises","Exercises filtered by scenario, state, window","allowed_scope","REQ-TRX-014"),
 ("QRY-SIM-GET","BC05","GET","/api/v1/readiness/simulations/{simulation_id}","Simulation with current state and evaluation summary","allowed_scope","REQ-TRX-014"),
 ("QRY-SIM-LIST","BC05","GET","/api/v1/readiness/simulations","Simulations filtered by exercise, state, window","allowed_scope","REQ-TRX-014"),
 ("QRY-SIM-TIMELINE","BC05","GET","/api/v1/readiness/simulations/{simulation_id}/timeline","Full, ordered timeline of inject deliveries and evaluations for a simulation","allowed_scope","REQ-TRX-015"),
]
ACTORS = {"SCN":"Training Manager (define, edit) · Exercise Director (activate, retire)",
 "EXR":"Exercise Director / Training Manager",
 "SIM":"Exercise Controller (start, deliver-inject, pause, resume, complete, abort) · Evaluator (record-evaluation)"}
P = {
 "CMD-SCN-DEFINE":"title!:LocalizedName exercise_type_ref!:urn situation!:string target_competencies!:array injects!:array",
 "CMD-SCN-EDIT":"title:LocalizedName situation:string target_competencies:array injects:array",
 "CMD-SCN-ACTIVATE":"",
 "CMD-SCN-RETIRE":"reason!:string",
 "CMD-EXR-PLAN":"scenario!:urn objectives!:string participants!:array purpose!:enum(drill,certification,assessment) role_ref:urn",
 "CMD-EXR-SCHEDULE":"window!:Interval location!:LocalizedName participants!:array",
 "CMD-EXR-START":"note:string",
 "CMD-EXR-CANCEL":"reason!:string",
 "CMD-SIM-START":"exercise!:urn scenario!:urn started_at!:date-time",
 "CMD-SIM-DELIVER-INJECT":"inject_ref!:urn delivered_at!:date-time note:string",
 "CMD-SIM-RECORD-EVALUATION":"participant!:urn competency_code!:string result!:enum(MET,PARTIAL,NOT_MET) notes:string",
 "CMD-SIM-PAUSE":"reason!:string",
 "CMD-SIM-RESUME":"",
 "CMD-SIM-COMPLETE":"",
 "CMD-SIM-ABORT":"reason!:string",
}
SYSTEM_CMDS = {"CMD-SIM-START"}
RESOURCE = {"AGG-SCENARIO":("readiness","scenarios"),"AGG-EXERCISE":("readiness","exercises"),"AGG-SIMULATION":("readiness","simulations")}
SECURITY_AFFECTING = set()
CONSUMERS = {"AGG-SCENARIO":["Search projection (SLC-05)"],
 "AGG-EXERCISE":["Simulation (creation trigger)","Search projection (SLC-05)"],
 "AGG-SIMULATION":["Exercise (outcome delegation)","Qualification Record (optional evidence source, SLC-03 — unmodified)","Knowledge Object (optional AAR terminal source, SLC-12 — CR-63)","Search projection (SLC-05)"],
 "default":["Search projection (SLC-05)"]}
CTX_OVERRIDE = {}

def enrich(spec, bc):
    S = spec["components"]["schemas"]
    if bc == "BC05":
        S["Inject"] = {"type": "object", "required": ["offset_minutes", "description"], "properties": {"offset_minutes": {"type": "integer", "minimum": 0}, "description": {"type": "string"}, "expected_response": {"type": "string"}}}
        for name, sch in S.items():
            if not name.endswith("Command") or "properties" not in sch: continue
            if name.startswith("ScnDefine") or name.startswith("ScnEdit"):
                sch["properties"]["injects"] = {"type": "array", "items": {"$ref": "#/components/schemas/Inject"}}
```
