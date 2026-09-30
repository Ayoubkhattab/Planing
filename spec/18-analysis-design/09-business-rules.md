---
id: AD-09-BUSINESS-RULES
type: business-rules
title: "قواعد العمل — الثوابت وشروط الانتقال وفصل المهام"
status: DRAFT
phase: "Phase 3.8 — 18-analysis-design (المرحلة 2)"
sources: [01-business/business-rules.md, 03-domain/contexts/BC*/aggregates/AGG-*.md, 08-security/policies-slc*.md, 04-information/reference-data.md]
generator: 17-system-study/_build/build_analysis_design.py
---

# قواعد العمل

كل قاعدة تحكم سلوك النظام، مجمعة من المصادر المعتمدة ومرتبة بحيث يعرف المنفّذ **أين** تُطبَّق كل قاعدة في المعمارية.

## أنواع القواعد وموقع تنفيذها

| النوع | المصدر | مثال | أين تُطبَّق (ADR-P17) | الخطأ عند المخالفة |
|---|---|---|---|---|
| قاعدة عمل عليا (BRL) | `01-business/business-rules.md` | BRL-002: لا يُكتب فوق ادعاء T1 لحل تعارض | تتحقق عبر المتطلبات التي تنفذها ثم الـAggregates (العمود الأخير في §1) | حسب القاعدة المنفِّذة |
| ثابت (Invariant) | `INV-*` في ملف الـAggregate | INV-TASK-07: المعتمِد ≠ المنفِّذ | **حلقة المجال**: تُفحص بعد كل انتقال، ولا يُحفظ Aggregate يخالفها | خطأ الشرط المرتبط، أو رفض الأمر |
| شرط انتقال (Guard) | عمود «الشرط» في جدول الانتقالات | START: كل المهام السابقة مكتملة | **حلقة المجال** قبل الانتقال؛ ما يحتاج بيانات من سياق آخر يُجلب عبر منفذ عميل ذلك السياق قبل التنفيذ | عمود «خطأ فشل الشرط» (غالبًا 422) |
| الحالة المسموحة | مصفوفة الحالة × الأمر | لا `ACCEPT` من `DRAFT` | **حلقة المجال** | `*_INVALID_STATE_TRANSITION` (409) |
| فصل المهام (SoD) | `segregation_of_duties` في سياسة الأمر، ويتكرر في شرط الانتقال أو الثابت (33 أمرًا، مثل INV-TASK-07) | اعتماد المهمة بغير منفّذها | **في الطبقتين عمدًا:** منفذ التخويل بعد تحميل المورد (ADR-P17، الخطوة 5) هو خط الدفاع الأول، والمجال يعيد الفحص عند الانتقال لأن الثابت يجب أن يصمد حتى لو تغيرت السياسة **[Derived]** | `SEGREGATION_OF_DUTIES` (422) |
| شروط السياق والالتزامات | `context_conditions`، `obligations` في السياسة | MFA، موافقة، تدقيق | **منفذ التخويل** وخط الأوامر (الخطوتان 6 و10) | شروط السياق: `AUTHZ_DENIED` (403→404 وفق `errors-*.md`). التزام قبل التنفيذ غير مستوفى: لا رمز ولا مسار موحد بعد (`11-hexagonal-reference.md` §3) **[Needs Review]** |
| البيانات المرجعية (`RD-*`) | `04-information/reference-data.md` | قيم مسموحة لنوع أو مستوى | لا منفذ مخصص في كتالوج المنافذ (`11-hexagonal-reference.md` §5): القيم تُقرأ عبر منفذ المستودع إن كانت في schema السياق، أو عبر منفذ عميل السياق المالك لها، بإصدارها وقت الأمر **[Derived]** | `VALIDATION_FAILED` أو خطأ الشرط |

**قاعدة تنفيذ:** القاعدة تُكتب مرة واحدة في موقعها أعلاه. التحقق في الواجهة (العميل أو المحوّل) لتحسين التجربة فقط ولا يغني عن التحقق في المجال.

## ما يحتويه الملف

1. قواعد العمل العليا (15) وربطها بالمتطلبات والـAggregates.
2. لكل Aggregate: ثوابته، ثم شروط انتقالاته مع خطأ كل شرط، ثم فصل المهام من سياسات أوامره، ثم البيانات المرجعية المذكورة في شروطه.

المحتوى أدناه مولَّد؛ التعديل يكون في المصدر ثم يُعاد التوليد.

<!-- BEGIN GENERATED: build_analysis_design.py -->

## 1. قواعد العمل العليا (BRL)

«يُنفِّذها» من حقل `enforced_by` في القاعدة؛ «متطلبات تذكرها كمصدر» متطلبات حقل `source` فيها يسمّي القاعدة ولا يذكرها `enforced_by` (فجوة ربط في المصدر **[Needs Review]**)؛ الـAggregates **[Derived]**: ما يحقق أحد هذه المتطلبات، أو يذكر القاعدة نصًا.

| القاعدة | النص | يُنفِّذها | متطلبات تذكرها كمصدر | الـAggregates |
|---|---|---|---|---|
| BRL-001 | Every T1 information item shall be traceable to at least one source and, where available, evidence. (T1 as defined in ADR-P03 / W1 Q12) | REQ-INF-021, REQ-INF-037 | — | AGG-CLAIM, AGG-ENTITY, AGG-EVIDENCE-LINK |
| BRL-002 | A T1 claim shall never be overwritten or deleted to resolve a conflict; conflicts are resolved through a conflict case. | REQ-INF-024, REQ-INF-025 | — | AGG-CLAIM, AGG-CONFLICT |
| BRL-003 | A business decision shall be recorded only if the decider holds, at decision time, an authority grant (directly or by delegation) for that decision type and scope, as held in BC01. | REQ-DEC-002 | REQ-CRD-002, REQ-RES-009 | AGG-ALLOCATION, AGG-COORDINATION-CASE, AGG-DECISION |
| BRL-004 | Approved Plan has Baseline. | REQ-OPS-003 | — | AGG-PLAN, AGG-PLAN-VERSION |
| BRL-005 | A change to a baselined plan's objectives, outcomes, phases, milestone dates or resource commitments is a major change and creates a new plan version; changes to descriptions, notes or attachments are minor. | REQ-OPS-004 | — | AGG-PLAN-VERSION |
| BRL-006 | Task completes only when completion requirements met. | REQ-OPS-008 | — | AGG-TASK |
| BRL-007 | A task assignment requires eligibility when the task type declares required competencies, qualifications or authorizations; an asset assignment requires the asset's valid certification and custody authorization (R2). | REQ-OPS-007 | REQ-RES-003 | AGG-ASSET, AGG-ASSET-ASSIGNMENT, AGG-TASK, AGG-TASK-TYPE |
| BRL-008 | AI never bypasses Authorization. | REQ-FND-010 | REQ-AI-002 | AGG-AI-REQUEST |
| BRL-009 | Every AI result used as input to a decision, assessment or product shall be traceable to its context package, model, model version and inputs. | — | REQ-AI-005 | AGG-AI-REQUEST, AGG-AI-RESULT |
| BRL-010 | Search cannot expose unauthorized data existence. | REQ-FND-010, REQ-ANL-008, REQ-SIT-006, REQ-SRC-002 | — | AGG-ALERT, AGG-ASSESSMENT |
| BRL-011 | Archive ≠ Backup. | — | — | AGG-ARCHIVE-PACKAGE |
| BRL-012 | Historical Reconstruction distinguishes recorded / reconstructed / inferred. | — | — | — |
| BRL-013 | External systems are not automatically Source of Truth. | — | REQ-INT-001 | AGG-IMPORT-BATCH, AGG-INTEGRATION-CONNECTION |
| BRL-014 | Each Domain owns its state. | — | — | — |
| BRL-015 | Every state-changing command, and every read of data at or above the tenant audit threshold, shall be audited. | REQ-FND-015 | — | — |

## 2. القواعد حسب الـAggregate (302 ثابتًا)

### BC01 — Foundation — الأساس

#### AGG-AUTHORITY-GRANT — منح السلطة

**الثوابت:**

- **INV-AUT-01** — a delegation never exceeds its parent in decision types, scope, limits or period
- **INV-AUT-02** — delegation depth ≤ 2 (W4 delegated decision)
- **INV-AUT-03** — a grant is EFFECTIVE at t ⇔ state ACTIVE at t ∧ t ∈ validity ∧ (no parent ∨ parent EFFECTIVE at t) — revoking a parent makes children ineffective without writing to them
- **INV-AUT-04** — root grants require approval by an Executive other than the requester

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-AUT-GRANT | ∅ | actor has authority.grant permission; decision type exists; scope unit ACTIVE | PERMISSION_DENIED |
| CMD-AUT-APPROVE-GRANT | PENDING_APPROVAL | approver is Executive in scope; approver ≠ requester | SEGREGATION_OF_DUTIES |
| CMD-AUT-REJECT-GRANT | PENDING_APPROVAL | reason | REASON_REQUIRED |
| CMD-AUT-DELEGATE | ∅ | parent grant effective and delegable; scope ⊆ parent; limits ≤ parent; period ⊆ parent; depth ≤ 2; delegate ≠ delegator | AUTHORITY_EXCEEDS_DELEGATOR |
| CMD-AUT-SUSPEND | ACTIVE | reason | REASON_REQUIRED |
| CMD-AUT-RESUME | SUSPENDED | period not ended | GRANT_EXPIRED |
| CMD-AUT-REVOKE | PENDING_APPROVAL, ACTIVE, SUSPENDED | granter, delegator or Executive in scope; reason | REASON_REQUIRED |
| SYS:valid_to reached | ACTIVE, SUSPENDED | system scheduler | — |

**فصل المهام:** CMD-AUT-APPROVE-GRANT: approver ≠ requester؛ CMD-AUT-DELEGATE: delegate ≠ delegator

#### AGG-CLEARANCE — التصريح الأمني

**الثوابت:**

- **INV-CLR-01** — at most one non-terminal clearance per user
- **INV-CLR-02** — no one grants or approves their own clearance
- **INV-CLR-03** — top-rank clearance requires two distinct Security Officers (W4 delegated decision)
- **INV-CLR-04** — every change increments the user's security_version

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-CLR-GRANT | ∅ | Security Officer; level and compartments exist in ACTIVE scheme; subject has no other non-terminal clearance | CLEARANCE_EXISTS |
| CMD-CLR-APPROVE | PENDING_APPROVAL | second Security Officer ≠ requester when level is top rank; else requester may self-confirm | SEGREGATION_OF_DUTIES |
| CMD-CLR-MODIFY | ACTIVE | same rules as grant; creates new version | CLEARANCE_INVALID |
| CMD-CLR-SUSPEND | ACTIVE | reason | REASON_REQUIRED |
| CMD-CLR-REINSTATE | SUSPENDED | period not ended | — |
| CMD-CLR-REVOKE | PENDING_APPROVAL, ACTIVE, SUSPENDED | reason | REASON_REQUIRED |
| SYS:valid_to reached | ACTIVE, SUSPENDED | system | — |

**فصل المهام:** CMD-CLR-APPROVE: approver ≠ requester ≠ subject (top rank)؛ CMD-CLR-GRANT: requester ≠ subject

#### AGG-DEVICE — الجهاز الميداني

**الثوابت:**

- **INV-DEV-01** — only ACTIVE devices can open sync sessions or download preload packages
- **INV-DEV-02** — device key is bound to (user, device); every offline command is signed with it (THR-012)
- **INV-DEV-03** — LOST revokes the key at once; the next contact receives a wipe instruction and nothing else
- **INV-DEV-04** — ≤ 3 ACTIVE devices per user (W4 delegated decision)

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-DEV-ENROLL | ∅ | user ACTIVE; device public key; platform; MDM reference; ≤ 3 active devices per user | DEVICE_LIMIT_REACHED |
| CMD-DEV-CONFIRM | PENDING_ENROLLMENT | hardware attestation valid (or MDM compliance); Administrator or MDM policy | ATTESTATION_FAILED |
| CMD-DEV-ROTATE-KEY | ACTIVE | signed by current key; new public key | SIGNATURE_INVALID |
| CMD-DEV-SUSPEND | ACTIVE | reason; sync rejected while suspended | REASON_REQUIRED |
| CMD-DEV-REINSTATE | SUSPENDED | reason | REASON_REQUIRED |
| CMD-DEV-REPORT-LOST | ACTIVE, SUSPENDED | user or Security Officer; key revoked immediately; wipe instruction queued; queued commands from the device after the lost time require review | — |
| SYS:wipe confirmed by device | LOST | device acknowledges wipe on next contact | — |
| CMD-DEV-RETIRE | ACTIVE, SUSPENDED | device synced and wiped (confirmation) or Security Officer override | DEVICE_NOT_WIPED |

#### AGG-HR-SYNC-PROPOSAL — مقترح مزامنة الموارد البشرية

**الثوابت:**

- **INV-HRS-01** — no role or access change is applied automatically from HRIS (REQ-INT-004, THR-S01-01)
- **INV-HRS-02** — 'leave' proposals are highlighted and escalated — access removal is time-critical
- **INV-HRS-03** — SCIM account disablement from the IdP remains immediate and independent of HR proposals (QAS-SEC-008)

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| SYS:HRIS change received | ∅ | person matched to a platform Person by HR identifier; change ∈ {join, leave, move_unit, change_position}; mapped to proposed role-assignment changes by tenant mapping table | — |
| CMD-HRS-APPROVE | PROPOSED | Administrator in scope of the affected units; applies CMD-RAS-ASSIGN / CMD-RAS-REVOKE and, for leave, CMD-USR-DISABLE — each through its own guards | OWNER_REJECTED |
| CMD-HRS-REJECT | PROPOSED | reason | REASON_REQUIRED |
| SYS:newer HR change for the same person | PROPOSED | system | — |
| SYS:14 days without decision | PROPOSED | scheduler; escalated to Security Officer for leave events | — |

#### AGG-ORGANIZATION — المؤسسة

**الثوابت:**

- **INV-ORG-01** — the unit tree is acyclic with exactly one root
- **INV-ORG-02** — sibling unit names are unique (after language-model normalization)
- **INV-ORG-03** — an inactive unit cannot receive children, assignments or grants
- **INV-ORG-04** — unit count per organization ≤ 5,000 (aggregate size bound; larger orgs split into organizations)

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-ORG-CREATE | ∅ | tenant ACTIVE; name unique in tenant; creates root unit | ORG_NAME_TAKEN |
| CMD-ORG-RENAME | ACTIVE | name unique in tenant | ORG_NAME_TAKEN |
| CMD-ORG-ADD-UNIT | ACTIVE | parent unit ACTIVE; sibling name unique | ORG_UNIT_INVALID_PARENT |
| CMD-ORG-RENAME-UNIT | ACTIVE | sibling name unique | ORG_UNIT_NAME_TAKEN |
| CMD-ORG-MOVE-UNIT | ACTIVE | new parent ACTIVE, same org, not a descendant (no cycle); root cannot move | ORG_UNIT_CYCLE |
| CMD-ORG-DEACTIVATE-UNIT | ACTIVE | no active children; no active role assignments, grants or clearances scoped only to it (BC01 query) | ORG_UNIT_IN_USE |
| CMD-ORG-DEACTIVATE | ACTIVE | all non-root units inactive; no active assignments | ORG_IN_USE |
| CMD-ORG-REACTIVATE | INACTIVE | tenant ACTIVE | — |

#### AGG-PERSON — الشخص

**الثوابت:**

- **INV-PER-01** — personal attributes are flagged personal_data (crypto-shredding, ADR-P08)
- **INV-PER-02** — external HR identifier unique per tenant when present

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-PER-REGISTER | ∅ | names per language-model; no duplicate HR id | PERSON_DUPLICATE |
| CMD-PER-ERASE | INACTIVE | erasure order recorded; no legal hold; destroys subject key (ADR-P08) | LEGAL_HOLD_ACTIVE |

#### AGG-ROLE — الدور

**الثوابت:**

- **INV-ROL-01** — the 15 platform roles (PRJ§45 actors) exist in every tenant and cannot be retired or edited
- **INV-ROL-02** — permissions are separate grants (View, Edit, Export, Share, Approve, Delete, Retain, Archive, command codes) — REQ-FND-014
- **INV-ROL-03** — permission changes to an ACTIVE role increment security_version of all its holders

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-ROL-DEFINE | ∅ | code unique in tenant | ROLE_CODE_TAKEN |
| CMD-ROL-SET-PERMISSIONS | DRAFT, ACTIVE | permissions exist in catalog; system roles are locked; ACTIVE → new version | SYSTEM_ROLE_LOCKED |
| CMD-ROL-ACTIVATE | DRAFT | ≥ 1 permission | ROLE_EMPTY |
| CMD-ROL-RETIRE | ACTIVE | not a system role; no active assignments | ROLE_IN_USE |

#### AGG-ROLE-ASSIGNMENT — إسناد الدور

**الثوابت:**

- **INV-RAS-01** — an assigner cannot assign a role outside units they administer, nor to themselves
- **INV-RAS-02** — SoD-incompatible roles cannot be active together for one user (default: Auditor × Administrator, Auditor × Security Officer)
- **INV-RAS-03** — assignment and revocation increment the user's security_version

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-RAS-ASSIGN | ∅ | role ACTIVE; user not CLOSED; scope unit ACTIVE; assigner administers the scope; no SoD-incompatible active role | SOD_ROLE_CONFLICT |
| CMD-RAS-REVOKE | ACTIVE | assigner administers the scope; reason | REASON_REQUIRED |
| SYS:valid_to reached | ACTIVE | system scheduler | — |

**فصل المهام:** CMD-RAS-ASSIGN: assigner ≠ user; SoD role pairs

#### AGG-SERVICE-ACCOUNT — حساب الخدمة

**الثوابت:**

- **INV-SVC-01** — a service account is never linked to a Person
- **INV-SVC-02** — every service account has an ACTIVE accountable owner user
- **INV-SVC-03** — credential lifetime ≤ 90 days (W4 delegated decision)

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-SVC-CREATE | ∅ | owner user ACTIVE; purpose stated | OWNER_REQUIRED |
| CMD-SVC-ROTATE-CREDENTIAL | ACTIVE | new credential expiry ≤ 90 days | CREDENTIAL_LIFETIME_EXCEEDED |
| CMD-SVC-ENABLE | DISABLED | owner still ACTIVE | OWNER_REQUIRED |

#### AGG-TENANT — المستأجر

**الثوابت:**

- **INV-TEN-01** — users of a tenant can authenticate only while the tenant is ACTIVE
- **INV-TEN-02** — a tenant is bound to exactly one cell at any time
- **INV-TEN-03** — cell_mode = dedicated if sovereign, or top classification level enabled, or load > 20 % of cell (ADR-P04)
- **INV-TEN-04** — namespace is unique across the platform and immutable
- **INV-TEN-05** — decommission cannot start while any legal hold is active

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-TEN-PROVISION | ∅ | namespace unique; cell_mode valid for tenant profile (INV-TEN-03) | TENANT_NAMESPACE_TAKEN |
| CMD-TEN-COMPLETE-PROVISIONING | PROVISIONING | system; all provisioning steps confirmed (isolation, keys, scheme, roles, quotas, audit stream) | TENANT_PROVISIONING_INCOMPLETE |
| CMD-TEN-FAIL-PROVISIONING | PROVISIONING | system; compensation completed | — |
| CMD-TEN-RETRY-PROVISIONING | PROVISIONING_FAILED | actor = platform operator | — |
| CMD-TEN-SUSPEND | ACTIVE | reason provided | REASON_REQUIRED |
| CMD-TEN-START-CELL-MIGRATION | ACTIVE | target cell exists and has capacity | CELL_UNAVAILABLE |
| CMD-TEN-COMPLETE-CELL-MIGRATION | MIGRATING | system; export/import reconciled | MIGRATION_NOT_RECONCILED |
| CMD-TEN-START-DECOMMISSION | ACTIVE, SUSPENDED | no active legal hold (BC08 query); two-person approval | LEGAL_HOLD_ACTIVE |
| CMD-TEN-COMPLETE-DECOMMISSION | DECOMMISSIONING | system; keys destroyed, stores removed | — |
| CMD-TEN-UPDATE-QUOTAS | ACTIVE, SUSPENDED | quotas ≤ cell capacity | QUOTA_EXCEEDS_CAPACITY |

**فصل المهام:** CMD-TEN-START-DECOMMISSION: two distinct platform operators

#### AGG-USER — حساب المستخدم

**الثوابت:**

- **INV-USR-01** — a user belongs to exactly one tenant
- **INV-USR-02** — (issuer, subject) is unique within the tenant
- **INV-USR-03** — an ACTIVE user has ≥ 1 identity and belongs to an ACTIVE tenant
- **INV-USR-04** — every change that affects authorization increments the subject security_version
- **INV-USR-05** — DISABLED, LOCKED and CLOSED users cannot obtain a SecurityContext

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-USR-PROVISION | ∅ | tenant ACTIVE; via SCIM or admin | TENANT_NOT_ACTIVE |
| CMD-USR-LINK-IDENTITY | أي حالة غير نهائية | (issuer, subject) unique in tenant; issuer is a configured IdP | IDENTITY_ALREADY_LINKED |
| CMD-USR-UNLINK-IDENTITY | أي حالة غير نهائية | if ACTIVE, at least one identity remains | LAST_IDENTITY |
| CMD-USR-LINK-PERSON | أي حالة غير نهائية | person ACTIVE, not linked to another user | PERSON_ALREADY_LINKED |
| CMD-USR-RECORD-FIRST-SIGN-IN | PENDING | system; ≥ 1 identity; tenant ACTIVE | — |
| CMD-USR-LOCK | ACTIVE | security officer or system anomaly rule; reason | REASON_REQUIRED |
| CMD-USR-UNLOCK | LOCKED | security officer | — |
| CMD-USR-DISABLE | PENDING, ACTIVE, LOCKED | SCIM deactivate or administrator | — |
| CMD-USR-ENABLE | DISABLED | ≥ 1 identity; tenant ACTIVE | LAST_IDENTITY |
| CMD-USR-CLOSE | DISABLED | administrator; audit history retained | — |

### BC02 — Information — نواة المعلومات

#### AGG-ATTACHMENT — المرفق

**الثوابت:**

- **INV-ATT-01** — (tenant, sha256) unique among non-terminal attachments
- **INV-ATT-02** — bytes never pass through application servers (direct transfer, signed targets ≤ 5 min)
- **INV-ATT-03** — only STORED attachments can back evidence or observations
- **INV-ATT-04** — every download is authorized per request and audited

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-ATT-INITIATE-UPLOAD | ∅ | size ≤ tenant limit; mime allowed; returns direct upload target (≤ 5 min); same sha256 already STORED in tenant → returns existing | ATTACHMENT_REJECTED |
| CMD-ATT-COMPLETE-UPLOAD | PENDING | stored bytes hash = declared sha256; size matches | HASH_MISMATCH |
| SYS:scan passed | SCANNING | offline content scanner + format validation | — |
| SYS:scan failed | SCANNING | scanner verdict | — |
| SYS:upload window 24 h elapsed | PENDING | scheduler | — |
| CMD-ATT-ERASE | STORED | erasure order or disposition; no legal hold; key destroyed (ADR-P08) | LEGAL_HOLD_ACTIVE |

#### AGG-CLAIM — الادعاء

**الثوابت:**

- **INV-CLM-01** — subject, predicate, value, valid interval and sources are immutable
- **INV-CLM-02** — recorded_from/recorded_to are server-assigned; CLOSED ⇔ recorded_to ≠ null
- **INV-CLM-03** — ≥ 1 source; each cited source was ACTIVE at assertion
- **INV-CLM-04** — successors reference their predecessor (supersedes chain)
- **INV-CLM-05** — source identity protection never leaks through the claim

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-CLM-ASSERT | ∅ | subject exists; predicate in RD-PREDICATES; value matches predicate type/unit/cardinality; ≥ 1 source, all ACTIVE; valid_from < valid_to; geometry rules; confidence dims valid | CLAIM_INVALID |
| CMD-CLM-CORRECT | CURRENT | closes recorded_to = now and asserts the replacement (same subject/predicate) in the same transaction; reason | REASON_REQUIRED |
| CMD-CLM-RECORD-CHANGE | CURRENT | t_change ∈ (valid_from, valid_to): closes record, re-records old value with valid_to = t_change, asserts new value from t_change | CHANGE_TIME_INVALID |
| CMD-CLM-RETRACT | CURRENT | reason; no replacement | REASON_REQUIRED |
| CMD-CLM-ASSESS | CURRENT | updates information_confidence / verification_status only (T2 versioned assessment); value and times untouched | ASSESSMENT_INVALID |
| CMD-CLM-RECLASSIFY | CURRENT, CLOSED | authority per tenant policy (REQ-GOV-004); new version; bumps object security_version | CLASSIFICATION_CHANGE_NOT_AUTHORIZED |

**بيانات مرجعية مستخدمة:** RD-PREDICATES (`04-information/reference-data.md`)

#### AGG-COLLECTION-PLAN — خطة الجمع

**الثوابت:**

- **INV-CPL-01** — every activity serves ≥ 1 EEI of an approved requirement
- **INV-CPL-02** — tasks created by activation link back to the activity (REQ-COL-002)

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-CPL-CREATE | ∅ | ≥ 1 APPROVED collection requirement; planner in scope; label ≥ requirements | REQUIREMENT_NOT_APPROVED |
| CMD-CPL-ADD-ACTIVITY | DRAFT, ACTIVE | method in RD-COLLECTION-METHODS; source(s) ACTIVE; area ⊆ requirement areas; window ⊆ requirement windows; assigned unit; task type | ACTIVITY_INVALID |
| CMD-CPL-REMOVE-ACTIVITY | DRAFT | activity not yet tasked | ACTIVITY_ALREADY_TASKED |
| CMD-CPL-ACTIVATE | DRAFT | ≥ 1 activity; creates one field task per activity through SLC-03 with plan_ref = this collection plan (CR-59) | PLAN_EMPTY |
| SYS:all activity tasks terminal | ACTIVE | SLC-03 events | — |
| CMD-CPL-COMPLETE | ACTIVE | planner; open tasks cancelled with reason | REASON_REQUIRED |
| CMD-CPL-CANCEL | DRAFT, ACTIVE | reason; open tasks cancelled | REASON_REQUIRED |

**بيانات مرجعية مستخدمة:** غير معرَّفة في `reference-data.md` **[Missing]**: RD-COLLECTION-METHODS

#### AGG-COLLECTION-REQUIREMENT — متطلب الجمع

**الثوابت:**

- **INV-CRQ-01** — fulfilment is computed per viewer over the observations that viewer may see (visibility first) — no leakage of hidden collection
- **INV-CRQ-02** — every fulfilment link points to a VALIDATED observation (or a claim derived from one) with lineage (QAS-COL-001)
- **INV-CRQ-03** — expiry depends only on the due date
- **INV-CRQ-04** — approver ≠ requester

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-CRQ-DRAFT | ∅ | question; requester; label | REQUIREMENT_INVALID |
| CMD-CRQ-EDIT | DRAFT | area polygon, window, priority 1–5, due, essential elements of information (EEIs) | REQUIREMENT_INVALID |
| CMD-CRQ-SUBMIT | DRAFT | area, window, priority and ≥ 1 EEI present (REQ-COL-001) | REQUIREMENT_INCOMPLETE |
| CMD-CRQ-APPROVE | SUBMITTED | collection manager with authority in the area scope; approver ≠ requester | SEGREGATION_OF_DUTIES |
| CMD-CRQ-REJECT | SUBMITTED | reason (duplicate, out of scope, infeasible) | REASON_REQUIRED |
| CMD-CRQ-AMEND | APPROVED | approver; extend due, adjust area or EEIs; recorded as new version | REQUIREMENT_INVALID |
| SYS:validated observation matched | APPROVED | matching engine links observation to EEIs (SPEC-COLLECTION §2); fulfilment recomputed | — |
| CMD-CRQ-MARK-SATISFIED | APPROVED | requester; fulfilment as seen by the requester is ANSWERED, or PARTIAL with explicit acceptance note | FULFILMENT_INSUFFICIENT |
| SYS:due passed | APPROVED | scheduler; based on due date only (never on hidden fulfilment) | — |
| CMD-CRQ-CANCEL | DRAFT, SUBMITTED, APPROVED | requester or approver; reason | REASON_REQUIRED |

**فصل المهام:** CMD-CRQ-APPROVE: approver ≠ requester

#### AGG-CONFLICT — التعارض

**الثوابت:**

- **INV-CNF-01** — a conflict never modifies, closes or re-labels any claim
- **INV-CNF-02** — at most one non-terminal conflict per (tenant, identity cluster, predicate, overlapping valid window)
- **INV-CNF-03** — resolutions are bitemporal records: resolve(T, K) uses the resolution known at K
- **INV-CNF-04** — label = max(member claim labels); a reader sees the conflict only if the reader sees ≥ 2 incompatible member claims (A21)
- **INV-CNF-05** — the preferred claim of a RESOLVED conflict is CURRENT; if it closes, the conflict is re-evaluated (SUPERSEDED or back to OPEN via detection)

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| SYS:conflict rule matched | ∅ | rule CF-01..CF-04 on claims of the same identity cluster, same predicate, overlapping valid; no non-terminal conflict with the same (cluster, predicate, window) — otherwise the claim joins it | — |
| CMD-CNF-RAISE | ∅ | analyst names ≥ 2 visible CURRENT claims on the same cluster and predicate with overlapping valid time | CONFLICT_INVALID |
| SYS:incompatible claim joined | OPEN, UNDER_REVIEW | new CURRENT claim incompatible with members (same key, overlapping window) | — |
| CMD-CNF-ASSIGN | OPEN, UNDER_REVIEW | reviewer cleared for every member claim label | REVIEWER_NOT_CLEARED |
| CMD-CNF-START-REVIEW | OPEN | actor = assigned reviewer (or Analyst lead) | NOT_ASSIGNED_REVIEWER |
| CMD-CNF-RESOLVE | UNDER_REVIEW | preferred claim ∈ CURRENT members; rationale; reviewer ≠ asserter of the preferred claim (SoD, default on); records resolution with recorded_from = now | SEGREGATION_OF_DUTIES |
| CMD-CNF-ACCEPT | UNDER_REVIEW | rationale (both accounts shown to users) | REASON_REQUIRED |
| CMD-CNF-REOPEN | RESOLVED, ACCEPTED_AS_CONFLICT | new evidence or reason; closes current resolution record (recorded_to = now) | REASON_REQUIRED |
| SYS:member set no longer conflicting | OPEN, UNDER_REVIEW, RESOLVED, ACCEPTED_AS_CONFLICT | fewer than 2 incompatible CURRENT members (claims closed, split, or corrected) | — |

**فصل المهام:** CMD-CNF-RESOLVE: reviewer ≠ asserter of preferred claim

#### AGG-CORRELATION-PROPOSAL — مقترح الربط

**الثوابت:**

- **INV-CRP-01** — a proposal never changes claims, observations or entities; acceptance acts only through owner commands (REQ-FUS-001)
- **INV-CRP-02** — fused results record every contributing source and its reliability at fusion time (REQ-FUS-002)
- **INV-CRP-03** — no automatic acceptance
- **INV-CRP-04** — independence: two inputs derived from the same source (or one from the other) count as one source for corroboration

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| SYS:correlation rule score ≥ threshold | ∅ | inputs from ≥ 2 distinct sources; no identical non-terminal proposal; label = max(input labels) | — |
| CMD-CRP-PROPOSE | ∅ | analyst; ≥ 2 visible inputs; kind; rationale | CORRELATION_INVALID |
| CMD-CRP-START-REVIEW | PROPOSED | reviewer cleared for every input label | REVIEWER_NOT_CLEARED |
| CMD-CRP-ACCEPT | UNDER_REVIEW | effects through owner commands as the reviewer: same_event → Real-World Event + participation relationships + fused claims; co_location → relationship; same_entity → ER case (SLC-04); lineage lists every contributing source and its reliability | OWNER_REJECTED |
| CMD-CRP-REJECT | UNDER_REVIEW, PROPOSED | reason (feeds rule evaluation) | REASON_REQUIRED |
| SYS:not reviewed within 30 days | PROPOSED | scheduler | — |

**فصل المهام:** CMD-CRP-ACCEPT: reviewer cleared for all inputs

#### AGG-CORRELATION-RULE — قاعدة الربط

**الثوابت:**

- **INV-CRR-01** — proposals record the rule version
- **INV-CRR-02** — activation requires an evaluation report

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-CRR-DEFINE | ∅ | kind ∈ {same_event, co_location, track_association, same_entity_hint} | RULE_INVALID |
| CMD-CRR-EDIT | DRAFT, ACTIVE | parameters: max distance (m, accuracy-aware), time window, attribute similarity, min distinct sources, threshold; ACTIVE → new version | RULE_INVALID |
| CMD-CRR-ACTIVATE | DRAFT | evaluation on a labelled set: precision ≥ 70 % of proposals (recalibrate after pilot); approver ≠ author | RULE_BELOW_TARGET |
| CMD-CRR-RETIRE | ACTIVE | reason | REASON_REQUIRED |

**فصل المهام:** CMD-CRR-ACTIVATE: approver ≠ author

#### AGG-ENTITY — الكيان

**الثوابت:**

- **INV-ENT-01** — an entity holds no attribute values; all T1 attributes are claims
- **INV-ENT-02** — claims hidden from a reader are invisible everywhere, including completeness and counts
- **INV-ENT-03** — RETIRED entities remain resolvable for history and as-of queries

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-ENT-REGISTER | ∅ | type in RD-ENTITY-TYPES; each initial claim valid as CMD-CLM-ASSERT; Entity + initial Claims created in one unit of work | ENTITY_INVALID |
| CMD-ENT-CHANGE-TYPE | ACTIVE | compatible type per RD-ENTITY-TYPES; new version; reason | ENTITY_TYPE_INCOMPATIBLE |
| CMD-ENT-RECLASSIFY | ACTIVE, RETIRED | authority per tenant policy (REQ-GOV-004); new version; bumps object security_version | CLASSIFICATION_CHANGE_NOT_AUTHORIZED |
| CMD-ENT-RETIRE | ACTIVE | reason (created in error / no longer tracked); claims untouched | REASON_REQUIRED |
| CMD-ENT-REINSTATE | RETIRED | reason | REASON_REQUIRED |

**بيانات مرجعية مستخدمة:** RD-ENTITY-TYPES (`04-information/reference-data.md`)

#### AGG-ER-CASE — حالة مطابقة الكيانات

**الثوابت:**

- **INV-ER-01** — claims are never moved or rewritten by merge or split (ER-MODEL §2)
- **INV-ER-02** — identity clusters are connected components of CURRENT MATCH links as known at K; canonical id = smallest ULID in the cluster
- **INV-ER-03** — no cluster may contain two entities joined by a CURRENT NOT_A_MATCH link
- **INV-ER-04** — no automatic merge: MATCHED requires a human decision (W1 Q26, AI-OP-06)
- **INV-ER-05** — a cluster > 50 members requires a second reviewer
- **INV-ER-06** — the decision records decision_basis_level = max label the reviewer could see; a higher-cleared reviewer may request a split

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| SYS:candidate generator score ≥ propose threshold | ∅ | pair not already in the same cluster; no NOT_A_MATCH link between their clusters; no non-terminal case for the pair | — |
| CMD-ER-PROPOSE | ∅ | same conditions; proposer is Analyst or AI suggestion (AIL1, agent recorded) | ER_PAIR_INVALID |
| CMD-ER-START-REVIEW | CANDIDATE | reviewer cleared for both entity labels | REVIEWER_NOT_CLEARED |
| CMD-ER-DECIDE-MATCH | UNDER_REVIEW | types compatible; neither entity RETIRED; merged cluster contains no NOT_A_MATCH pair; merged cluster size ≤ 50 or second reviewer; reviewer ≠ human proposer; creates MATCH link and recomputes cluster in the same transaction | MATCH_CONTRADICTS_NOT_A_MATCH |
| CMD-ER-DECIDE-NOT-MATCH | UNDER_REVIEW | rationale; creates NOT_A_MATCH link (blocks re-proposal) | REASON_REQUIRED |
| CMD-ER-PARK | UNDER_REVIEW | rationale; insufficient evidence | REASON_REQUIRED |
| CMD-ER-RESUME | POSSIBLE_DUPLICATE | new evidence or reason | REASON_REQUIRED |
| CMD-ER-DECIDE-NOT-MATCH | POSSIBLE_DUPLICATE | rationale | REASON_REQUIRED |
| CMD-ER-REQUEST-SPLIT | MATCHED | reason + evidence; requester cleared for both entities | REASON_REQUIRED |
| CMD-ER-CONFIRM-MATCH | SPLIT_REQUIRED | reviewer ≠ split requester; rationale | SEGREGATION_OF_DUTIES |
| CMD-ER-SPLIT | SPLIT_REQUIRED | reviewer ≠ split requester; closes MATCH link (recorded_to = now); optional NOT_A_MATCH link; recomputes clusters in the same transaction | SEGREGATION_OF_DUTIES |
| CMD-ER-WITHDRAW | CANDIDATE, UNDER_REVIEW, POSSIBLE_DUPLICATE | reason (e.g. entity retired, duplicate case) | REASON_REQUIRED |

**فصل المهام:** CMD-ER-CONFIRM-MATCH: reviewer ≠ split requester؛ CMD-ER-DECIDE-MATCH: reviewer ≠ human proposer; second reviewer if cluster > 50؛ CMD-ER-SPLIT: reviewer ≠ split requester

#### AGG-EVIDENCE — الدليل

**الثوابت:**

- **INV-EVD-01** — evidence is never deleted; withdrawal keeps it and its links
- **INV-EVD-02** — after SEALED only custody and label change
- **INV-EVD-03** — custody chain is gapless

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-EVD-REGISTER | ∅ | attachment STORED or observation_ref; type in RD-EVIDENCE-TYPES; source ACTIVE | EVIDENCE_INVALID |
| CMD-EVD-UPDATE-LOCATOR | REGISTERED | locator within attachment bounds | LOCATOR_INVALID |
| CMD-EVD-SEAL | REGISTERED | integrity hash over metadata + attachment hash | — |
| CMD-EVD-TRANSFER-CUSTODY | REGISTERED, SEALED | actor is current holder or custodian role; new holder named | CUSTODY_INVALID |
| CMD-EVD-RECLASSIFY | REGISTERED, SEALED, WITHDRAWN | authority per tenant policy (REQ-GOV-004); new version; bumps object security_version | CLASSIFICATION_CHANGE_NOT_AUTHORIZED |
| CMD-EVD-WITHDRAW | REGISTERED, SEALED | reason (e.g. forged); links kept and flagged; dependent verification re-evaluated | REASON_REQUIRED |

**بيانات مرجعية مستخدمة:** RD-EVIDENCE-TYPES (`04-information/reference-data.md`)

#### AGG-EVIDENCE-LINK — رابط الدليل

**الثوابت:**

- **INV-EVL-01** — links are bitemporal records; removal closes recorded_to
- **INV-EVL-02** — link label = max(evidence label, claim label)

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-EVL-LINK | ∅ | evidence not WITHDRAWN; claim exists; stance ∈ {SUPPORTS, REFUTES, CONTEXT}; no ACTIVE duplicate (evidence, claim, stance) | LINK_DUPLICATE |
| CMD-EVL-UNLINK | ACTIVE | reason; recorded_to closed | REASON_REQUIRED |

#### AGG-EXTERNAL-ID — ربط المعرّف الخارجي

**الثوابت:**

- **INV-EXT-01** — at any time t, (tenant, system, external_id) maps to at most one object
- **INV-EXT-02** — mappings are never deleted

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-EXT-MAP | ∅ | (system, external_id) has no ACTIVE mapping; target exists | EXTERNAL_ID_TAKEN |
| CMD-EXT-END | ACTIVE | reason; valid_to set | REASON_REQUIRED |

#### AGG-IMPORT-BATCH — دفعة الاستيراد

**الثوابت:**

- **INV-IMP-01** — re-submitting the same batch never duplicates records
- **INV-IMP-02** — no quarantined record appears in queries or projections
- **INV-IMP-03** — every applied record has lineage to batch + mapping version
- **INV-IMP-04** — imported values are claims citing the adapter's source (BRL-013)

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-IMP-SUBMIT | ∅ | adapter ACTIVE (or authorized manual import); batch_key unique per adapter: same key + same content hash returns the existing batch; different hash → rejected | BATCH_KEY_REUSED |
| SYS:processing started | RECEIVED | worker lease acquired | — |
| SYS:all records applied | PROCESSING | each record applied idempotently with lineage (adapter, batch, mapping version) | — |
| SYS:finished with invalid records | PROCESSING | invalid records quarantined with reason codes | — |
| SYS:unrecoverable error | PROCESSING | applied records remain; re-submit resumes idempotently | — |
| CMD-IMP-REPROCESS-QUARANTINE | COMPLETED_WITH_QUARANTINE | new mapping version or corrected records | — |
| CMD-IMP-ACCEPT-QUARANTINE | COMPLETED_WITH_QUARANTINE | reason; quarantined records dropped, record kept | REASON_REQUIRED |
| CMD-IMP-CANCEL | RECEIVED | reason | REASON_REQUIRED |

#### AGG-MATCH-RULESET — مجموعة قواعد المطابقة

**الثوابت:**

- **INV-MRS-01** — exactly one ACTIVE ruleset per (tenant, entity type)
- **INV-MRS-02** — every proposal records the ruleset version (lineage)
- **INV-MRS-03** — a ruleset cannot be activated without a passing evaluation on a labelled Arabic/English test set

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-MRS-DRAFT | ∅ | entity type exists | — |
| CMD-MRS-EDIT | DRAFT | blocking keys, features, weights, thresholds valid; evaluation run on labelled test set attached | RULESET_INVALID |
| CMD-MRS-ACTIVATE | DRAFT | evaluation meets QAS-ER-001 (candidate recall ≥ 95 %) and QAS-ER-002; approver ≠ author; previous ACTIVE → SUPERSEDED | RULESET_BELOW_TARGET |
| SYS:successor activated | ACTIVE | system | — |

**فصل المهام:** CMD-MRS-ACTIVATE: approver ≠ author

#### AGG-OBSERVATION — الملاحظة

**الثوابت:**

- **INV-OBS-01** — recorded_from is server-assigned; observed_at comes from the source/device
- **INV-OBS-02** — content is immutable once VALIDATED or REJECTED (reclassification versions the label only)
- **INV-OBS-03** — every derived claim references the observation in lineage
- **INV-OBS-04** — device clock skew > 5 min adds data_quality issue DEVICE_CLOCK_SUSPECT

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-OBS-RECORD | ∅ | source ACTIVE; location with CRS + accuracy + valid geometry; UCUM units; observed_at ≤ server time + 5 min; recorded_from by server | OBSERVATION_INVALID |
| CMD-OBS-AMEND | RECORDED | actor = observer or Analyst; new version; reason | REASON_REQUIRED |
| CMD-OBS-ATTACH-EVIDENCE | RECORDED | evidence REGISTERED or SEALED | EVIDENCE_INVALID |
| CMD-OBS-RECLASSIFY | RECORDED, VALIDATED, REJECTED | authority per tenant policy (REQ-GOV-004); new version; bumps object security_version | CLASSIFICATION_CHANGE_NOT_AUTHORIZED |
| CMD-OBS-VALIDATE | RECORDED | Analyst ≠ observer, or system auto-validation for sensor sources rated A/B under tenant policy | SEGREGATION_OF_DUTIES |
| CMD-OBS-REJECT | RECORDED | reason | REASON_REQUIRED |

**فصل المهام:** CMD-OBS-VALIDATE: validator ≠ observer (unless system auto-validation policy)

#### AGG-REALWORLD-EVENT — الحدث الواقعي

**الثوابت:**

- **INV-RWE-01** — event_time is a fuzzy-interval claim with precision
- **INV-RWE-02** — participants are relationships, not embedded lists

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-RWE-REGISTER | ∅ | type in RD-EVENT-TYPES; initial claims include event_time (fuzzy) and location | EVENT_INVALID |
| CMD-RWE-CHANGE-TYPE | ACTIVE | compatible type; reason | EVENT_TYPE_INCOMPATIBLE |
| CMD-RWE-RECLASSIFY | ACTIVE, RETIRED | authority per tenant policy (REQ-GOV-004); new version; bumps object security_version | CLASSIFICATION_CHANGE_NOT_AUTHORIZED |
| CMD-RWE-RETIRE | ACTIVE | reason | REASON_REQUIRED |
| CMD-RWE-REINSTATE | RETIRED | reason | REASON_REQUIRED |

**بيانات مرجعية مستخدمة:** RD-EVENT-TYPES (`04-information/reference-data.md`)

#### AGG-RELATIONSHIP — العلاقة

**الثوابت:**

- **INV-REL-01** — validity comes from the existence claim; the identity carries type, endpoints and label
- **INV-REL-02** — a relationship may be labelled above both endpoints and is then invisible without clearance

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-REL-REGISTER | ∅ | type in RD-RELATIONSHIP-TYPES; endpoint types allowed; creates identity + existence claim (valid interval, sources ≥ 1) | RELATIONSHIP_INVALID |
| CMD-REL-RECLASSIFY | ACTIVE, RETIRED | authority per tenant policy (REQ-GOV-004); new version; bumps object security_version | CLASSIFICATION_CHANGE_NOT_AUTHORIZED |
| CMD-REL-RETIRE | ACTIVE | created in error only; ending in reality = CMD-CLM-RECORD-CHANGE on the existence claim | REASON_REQUIRED |
| CMD-REL-REINSTATE | RETIRED | reason | REASON_REQUIRED |

**بيانات مرجعية مستخدمة:** RD-RELATIONSHIP-TYPES (`04-information/reference-data.md`)

#### AGG-SOURCE — المصدر

**الثوابت:**

- **INV-SRC-01** — reliability is a bitemporal claim; a claim's source_reliability is the rating valid and known at the claim's recorded_from
- **INV-SRC-02** — identity attributes of person-type sources are visible only with the source-protection permission; others see type and reliability only
- **INV-SRC-03** — SUSPENDED or RETIRED sources cannot be cited by new claims or observations
- **INV-SRC-04** — retiring never alters past ratings or claims

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-SRC-REGISTER | ∅ | type in RD-SOURCE-TYPES; initial reliability A–F; person-type sources get protection_level ≥ 1 and label ≥ tenant default + 1 rank | SOURCE_INVALID |
| CMD-SRC-RATE-RELIABILITY | ACTIVE, SUSPENDED | rating ∈ A–F; valid_from given; creates bitemporal reliability claim | RATING_INVALID |
| CMD-SRC-SET-PROTECTION | ACTIVE, SUSPENDED | Security Officer; decreasing protection requires a second Security Officer | SEGREGATION_OF_DUTIES |
| CMD-SRC-RECLASSIFY | ACTIVE, SUSPENDED | authority per tenant policy (REQ-GOV-004); new version; bumps object security_version | CLASSIFICATION_CHANGE_NOT_AUTHORIZED |
| CMD-SRC-SUSPEND | ACTIVE | reason | REASON_REQUIRED |
| CMD-SRC-RETIRE | ACTIVE, SUSPENDED | reason; history retained | REASON_REQUIRED |

**فصل المهام:** CMD-SRC-SET-PROTECTION: decrease needs second Security Officer

**بيانات مرجعية مستخدمة:** RD-SOURCE-TYPES (`04-information/reference-data.md`)

### BC03 — Intelligence — الوعي والتحليل

#### AGG-ALERT — التنبيه

**الثوابت:**

- **INV-ALR-01** — every transition is audited (REQ-SIT-005)
- **INV-ALR-02** — alert label = max(rule label, labels of triggering objects); only recipients cleared for that label receive it — others receive nothing, not a redacted alert (REQ-SIT-006)
- **INV-ALR-03** — dedupe: at most one non-terminal alert per (rule, subject) within the dedupe window

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| SYS:rule condition met | ∅ | no non-terminal alert for (rule, subject) inside dedupe window; label = max(rule label, triggering object labels) | — |
| SYS:condition met again within dedupe window | RAISED, ACKNOWLEDGED | occurrence counter + last_occurrence updated | — |
| CMD-ALR-ACKNOWLEDGE | RAISED | actor is a recipient | NOT_A_RECIPIENT |
| SYS:unacknowledged beyond escalation delay | RAISED | escalates to the rule's escalation recipients | — |
| CMD-ALR-RESOLVE | RAISED, ACKNOWLEDGED | actor is a recipient; note | NOT_A_RECIPIENT |
| SYS:condition cleared and rule auto_resolve | RAISED, ACKNOWLEDGED | system | — |
| CMD-ALR-DISMISS | RAISED, ACKNOWLEDGED | actor is a recipient; reason (REQ-SIT-005) | REASON_REQUIRED |

#### AGG-ALERT-RULE — قاعدة التنبيه

**الثوابت:**

- **INV-ARL-01** — an ACTIVE rule is immutable; editing requires DISABLED (no silent change to what triggers alerts)
- **INV-ARL-02** — the rule's label ≥ labels of data it reads, enforced at evaluation by computing alert labels (INV-ALR-02)
- **INV-ARL-03** — rules of a PAUSED or CLOSED situation do not fire

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-ARL-DEFINE | ∅ | condition kind in RD-ALERT-RULE-TYPES; parameters valid; severity; dedupe window; situation ACTIVE or tenant-wide scope | ALERT_RULE_INVALID |
| CMD-ARL-EDIT | DRAFT, DISABLED | same validation; new version | ALERT_RULE_INVALID |
| CMD-ARL-ACTIVATE | DRAFT | dry-run on last 24 h of events completed and reviewed (expected alert volume shown) | DRY_RUN_REQUIRED |
| CMD-ARL-DISABLE | ACTIVE | reason | REASON_REQUIRED |
| CMD-ARL-RETIRE | DRAFT, ACTIVE, DISABLED | reason | REASON_REQUIRED |

**بيانات مرجعية مستخدمة:** RD-ALERT-RULE-TYPES (`04-information/reference-data.md`)

#### AGG-ANALYSIS-CASE — حالة التحليل

**الثوابت:**

- **INV-ACS-01** — every evidence selection is pinned with known_at so its content is reproducible (TEMPORAL-MODEL §4)
- **INV-ACS-02** — case label ≥ max label of its selected items (no lower-labelled case exposing higher-labelled selections)
- **INV-ACS-03** — runs, findings and assessments are separate aggregates (CR-29: no God aggregate)
- **INV-ACS-04** — selections and assumptions are never deleted; deselection/retirement closes them with reason

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-ACS-CREATE | ∅ | title; owner; label | CASE_INVALID |
| CMD-ACS-DEFINE | DRAFT, OPEN | question text; spatial extent (optional polygon); time window; new version | CASE_INVALID |
| CMD-ACS-OPEN | DRAFT | question and scope present (REQ-ANL-001) | CASE_NOT_DEFINED |
| CMD-ACS-ADD-HYPOTHESIS | OPEN | statement; hypotheses per case ≤ 20 | CASE_INVALID |
| CMD-ACS-UPDATE-HYPOTHESIS | OPEN | status ∈ {PROPOSED, SUPPORTED, WEAKENED, REJECTED, UNRESOLVED}; rationale; supporting findings refs | REASON_REQUIRED |
| CMD-ACS-ADD-ASSUMPTION | OPEN | statement; criticality (high/medium/low) | CASE_INVALID |
| CMD-ACS-RETIRE-ASSUMPTION | OPEN | reason; runs using it are flagged | REASON_REQUIRED |
| CMD-ACS-SELECT-EVIDENCE | OPEN | items visible to actor; each pinned with known_at = now; item label ≤ case label | EVIDENCE_ABOVE_CASE_LABEL |
| CMD-ACS-DESELECT-EVIDENCE | OPEN | reason; selection record closed, not deleted | REASON_REQUIRED |
| CMD-ACS-DEFINE-SCENARIO | OPEN | name; assumption set; parameter overrides (REQ-ANL-007) | CASE_INVALID |
| CMD-ACS-CLOSE | OPEN | reason; no QUEUED or RUNNING runs | RUNS_IN_PROGRESS |
| CMD-ACS-REOPEN | CLOSED | reason | REASON_REQUIRED |
| CMD-ACS-CANCEL | DRAFT, OPEN | reason; no PUBLISHED assessment references the case | CASE_HAS_PUBLISHED_ASSESSMENT |
| CMD-ACS-RECLASSIFY | DRAFT, OPEN, CLOSED | new label ≥ max label of selected evidence; authority per policy | CLASSIFICATION_CHANGE_NOT_AUTHORIZED |

#### AGG-ANALYSIS-METHOD — طريقة التحليل

**الثوابت:**

- **INV-AMT-01** — a method version is immutable (image digest, parameter schema, code)
- **INV-AMT-02** — a version backing published work stays executable (DEPRECATED at most)

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-AMT-REGISTER | ∅ | code + version unique; parameter JSON schema; execution image digest from internal registry; deterministic flag | METHOD_INVALID |
| CMD-AMT-ACTIVATE | DRAFT | validation suite passed; approver ≠ author | SEGREGATION_OF_DUTIES |
| CMD-AMT-DEPRECATE | ACTIVE | reason; no new runs; reproduction still allowed | REASON_REQUIRED |
| CMD-AMT-RETIRE | DEPRECATED | no run of this version backs a PUBLISHED or SUPERSEDED assessment (reproducibility preserved) | METHOD_BACKS_PUBLISHED_WORK |

**فصل المهام:** CMD-AMT-ACTIVATE: approver ≠ author

#### AGG-ANALYSIS-RUN — تشغيل التحليل

**الثوابت:**

- **INV-RUN-01** — inputs are pinned by known_at, so re-execution sees exactly the same data (REQ-ANL-003)
- **INV-RUN-02** — a run reads only what its submitter may see; results label ≥ max input label
- **INV-RUN-03** — a reproduction compares result hashes and reports REPRODUCED or DIFFERENT with the differing inputs/method/environment
- **INV-RUN-04** — SUCCEEDED results are immutable

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-RUN-SUBMIT | ∅ | case OPEN; method ACTIVE; parameters valid against schema; inputs pinned (dataset refs with known_at = submission time, filters, layers, extent, time window, assumptions); run label ≥ max input label; tenant job quota | RUN_INVALID |
| CMD-RUN-REPRODUCE | ∅ | source run SUCCEEDED; reproducer cleared for source run label; method version ACTIVE or DEPRECATED; copies inputs/parameters/seed exactly | REPRODUCTION_NOT_ALLOWED |
| SYS:worker lease acquired | QUEUED | executes with the submitter's authorization (visibility), never with system privileges | — |
| SYS:completed | RUNNING | results stored as hashed artifacts; steps log; lineage record written (inputs+known_at, method version, image digest, parameters, seed, actor, times) | — |
| SYS:error or timeout | RUNNING | error recorded; partial artifacts discarded | — |
| CMD-RUN-CANCEL | QUEUED, RUNNING | submitter or case owner; reason | REASON_REQUIRED |

**فصل المهام:** CMD-RUN-REPRODUCE: reproducer cleared for source run label

#### AGG-ASSESSMENT — التقييم

**الثوابت:**

- **INV-ASM-01** — a PUBLISHED version is immutable; changes are new versions (REQ-ANL-006)
- **INV-ASM-02** — exactly one PUBLISHED version per assessment at a time; history of versions retained
- **INV-ASM-03** — references from decisions pin the version (URN + version) — superseding never changes what a past decision relied on
- **INV-ASM-04** — readers not cleared for some cited evidence get the assessment with those references withheld per policy (REQ-ANL-008)

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-ASM-DRAFT | ∅ | case exists; either new assessment or revision of a PUBLISHED version (copies content); at most one DRAFT/IN_REVIEW per assessment | DRAFT_EXISTS |
| CMD-ASM-EDIT | DRAFT | key judgments use RD-ESTIMATIVE-PROBABILITY terms and analytic confidence (low/moderate/high) | ASSESSMENT_INVALID |
| CMD-ASM-SUBMIT | DRAFT | findings ≥ 1 (ACCEPTED), evidence, assumptions, uncertainty, confidence, methodology, limitations all present (REQ-ANL-005) | ASSESSMENT_INCOMPLETE |
| CMD-ASM-RETURN | IN_REVIEW | reviewer; reason | REASON_REQUIRED |
| CMD-ASM-PUBLISH | IN_REVIEW | reviewer ≠ author; label ≥ max(findings, evidence); previous PUBLISHED version → SUPERSEDED in the same transaction | SEGREGATION_OF_DUTIES |
| SYS:newer version published | PUBLISHED | system | — |
| CMD-ASM-WITHDRAW | PUBLISHED | reason; decisions and products referencing it are notified | REASON_REQUIRED |
| CMD-ASM-DISCARD | DRAFT | author; reason | REASON_REQUIRED |

**فصل المهام:** CMD-ASM-PUBLISH: reviewer ≠ author

**بيانات مرجعية مستخدمة:** RD-ESTIMATIVE-PROBABILITY (`04-information/reference-data.md`)

#### AGG-CAP-MESSAGE — رسالة CAP الصادرة

**الثوابت:**

- **INV-CAP-01** — nothing leaves the platform without a release decision by someone other than the preparer
- **INV-CAP-02** — CAP content is generated from a reviewed template and the alert's releasable fields only
- **INV-CAP-03** — inbound CAP messages arrive through an adapter as observations of a CAP source (SLC-02), never as direct alerts

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-CAP-PREPARE | ∅ | tenant CAP enabled; alert RAISED/ACKNOWLEDGED; alert label ≤ tenant external release level; content = CAP fields from a reviewed template (no free text from classified sources); target connection cap_endpoint ACTIVE | RELEASE_NOT_ALLOWED |
| CMD-CAP-RELEASE | PREPARED | release authority ≠ preparer; valid CAP 1.2 (schema validated); delivery acknowledged | SEGREGATION_OF_DUTIES |
| SYS:delivery failed after retries | PREPARED | 5 retries with backoff | — |
| CMD-CAP-RETRY | FAILED | operator | — |
| CMD-CAP-CANCEL | PREPARED, FAILED | reason | REASON_REQUIRED |

**فصل المهام:** CMD-CAP-RELEASE: release authority ≠ preparer

#### AGG-FINDING — النتيجة التحليلية

**الثوابت:**

- **INV-FND-01** — an ACCEPTED finding is immutable
- **INV-FND-02** — every finding traces to runs or evidence (lineage)

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-FND-RECORD | ∅ | statement; ≥ 1 source among SUCCEEDED runs of the case or selected evidence; uncertainty; label ≥ sources | FINDING_INVALID |
| CMD-FND-EDIT | DRAFT | same rules; new version | FINDING_INVALID |
| CMD-FND-ACCEPT | DRAFT | reviewer ≠ author (peer review) | SEGREGATION_OF_DUTIES |
| CMD-FND-WITHDRAW | DRAFT, ACCEPTED | reason; assessments citing it are flagged for review | REASON_REQUIRED |

**فصل المهام:** CMD-FND-ACCEPT: reviewer ≠ author

#### AGG-SITUATION — الموقف

**الثوابت:**

- **INV-SIT-01** — members stay owned by their contexts; the situation stores only definition, membership records and change log
- **INV-SIT-02** — a reader sees a situation only if cleared for its label, and sees each member only if cleared for that member (per-member filtering)
- **INV-SIT-03** — membership is evaluated against the definition version that was ACTIVE at the evaluation time (history reproducible)
- **INV-SIT-04** — a CLOSED situation keeps its final snapshot and change log

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-SIT-CREATE | ∅ | name; extent (polygon or buffer around an entity); time window; criteria valid per SPEC-SITUATION §2; owner; label | SITUATION_INVALID |
| CMD-SIT-EDIT-DEFINITION | DRAFT, ACTIVE, PAUSED | criteria/extent/window valid; new definition version; membership recomputed from the new version | SITUATION_INVALID |
| CMD-SIT-ACTIVATE | DRAFT | definition complete; active situations per tenant ≤ quota | QUOTA_EXCEEDED |
| CMD-SIT-PAUSE | ACTIVE | reason; membership frozen, alerts of its rules suspended | REASON_REQUIRED |
| CMD-SIT-RESUME | PAUSED | membership re-evaluated from current state | — |
| CMD-SIT-CLOSE | DRAFT, ACTIVE, PAUSED | reason; final membership snapshot recorded | REASON_REQUIRED |
| CMD-SIT-RECLASSIFY | DRAFT, ACTIVE, PAUSED | authority per tenant policy; subscribers without clearance are unsubscribed | CLASSIFICATION_CHANGE_NOT_AUTHORIZED |

### BC04 — Operations — التخطيط والتنفيذ

#### AGG-COORDINATION-CASE — حالة التنسيق

**الثوابت:**

- **INV-CRD-01** — coordination is within one tenant; cross-tenant coordination uses product distribution/export only (R2 decision)
- **INV-CRD-02** — each participant sees only its access scope (sections) and objects its members may see (REQ-CRD-001)
- **INV-CRD-03** — an action needing another organization's authority is never marked done without that authority's recorded decision (REQ-CRD-002, BRL-003)
- **INV-CRD-04** — the case links decisions and plans; it never replaces them

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-CRD-OPEN | ∅ | title; purpose; lead organization; linked decisions/plans/situations visible to the opener; label | COORDINATION_INVALID |
| CMD-CRD-ADD-PARTICIPANT | OPEN, ACTIVE | org unit in the same tenant; participant role; access scope (sections); participant's members cleared for case label | PARTICIPANT_INVALID |
| CMD-CRD-REMOVE-PARTICIPANT | OPEN, ACTIVE | not the lead; no open responsibilities | PARTICIPANT_HAS_RESPONSIBILITIES |
| CMD-CRD-ACTIVATE | OPEN | ≥ 2 participants | PARTICIPANTS_REQUIRED |
| CMD-CRD-ASSIGN-RESPONSIBILITY | ACTIVE | participant exists; item, due; flag requires_authority (decision type) when the action needs that organization's authority | RESPONSIBILITY_INVALID |
| CMD-CRD-UPDATE-RESPONSIBILITY | ACTIVE | actor belongs to the responsible participant; status ∈ {in_progress, done, waived with reason}; items requiring authority cannot be done before the decision is recorded | DECISION_PENDING |
| CMD-CRD-REQUEST-DECISION | ACTIVE | responsibility requires authority; creates a Decision Request (SLC-08) in the participant's scope with the required decision type | RESPONSIBILITY_INVALID |
| SYS:linked decision recorded | ACTIVE | decision references the request created by the case; outcome stored on the responsibility | — |
| CMD-CRD-CLOSE | ACTIVE | all responsibilities done or waived; closing note | OPEN_RESPONSIBILITIES |
| CMD-CRD-CANCEL | OPEN, ACTIVE | lead; reason | REASON_REQUIRED |

#### AGG-DECISION — القرار

**الثوابت:**

- **INV-DEC-01** — immutable after recording (REQ-DEC-004); changes are new decisions that supersede
- **INV-DEC-02** — authority snapshot (grant chain, delegation depth, limits) is stored and remains verifiable as-of recorded_at
- **INV-DEC-03** — every decision links to ≥ 1 assessment or evidence (REQ-DEC-003, OUT-04 target 100 %)
- **INV-DEC-04** — effective time and record time are distinct; retroactive effect limited to 1 h unless tenant policy allows longer

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-DEC-RECORD | ∅ | AuthorityCheck(decider, decision type, scope, now) = authorized — grant chain stored as authority snapshot (BRL-003, REQ-DEC-002); request OPEN (or ad-hoc with rationale and ≥ 1 citation); selected option ∈ request options; rationale; effective_from ≥ now − 1 h; supersedes (optional) is RECORDED and same scope | AUTHORITY_REQUIRED |
| SYS:superseding decision recorded | RECORDED | new decision references this one in supersedes | — |
| CMD-DEC-ANNUL | RECORDED | recorded in error; actor holds authority for the same decision type at a higher scope; reason; plans implementing it are flagged | AUTHORITY_REQUIRED |

**فصل المهام:** CMD-DEC-ANNUL: authority at higher scope؛ CMD-DEC-RECORD: AuthorityCheck (BRL-003)

#### AGG-DECISION-REQUEST — طلب القرار

**الثوابت:**

- **INV-DRQ-01** — citations are pinned by version (INV-ASM-03)
- **INV-DRQ-02** — request label ≥ labels of its citations
- **INV-DRQ-03** — a request is decided by exactly one decision

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-DRQ-CREATE | ∅ | question; required decision type (RD-DECISION-TYPES); scope unit; deadline; label | DECISION_REQUEST_INVALID |
| CMD-DRQ-ADD-OPTION | DRAFT, OPEN | option text; expected impact; options ≤ 10 | DECISION_REQUEST_INVALID |
| CMD-DRQ-CITE | DRAFT, OPEN | assessment or evidence visible; pinned URN + version; cited label ≤ request label | CITATION_ABOVE_LABEL |
| CMD-DRQ-OPEN | DRAFT | ≥ 2 options (one may be 'no action'); ≥ 1 citation (REQ-DEC-001, OUT-04) | DECISION_REQUEST_INCOMPLETE |
| SYS:deadline passed | OPEN | escalates to holders of the required authority in scope | — |
| SYS:decision recorded for this request | OPEN | EVT-DEC-RECORDED references the request | — |
| CMD-DRQ-WITHDRAW | DRAFT, OPEN | reason | REASON_REQUIRED |

**بيانات مرجعية مستخدمة:** RD-DECISION-TYPES (`04-information/reference-data.md`)

#### AGG-INCIDENT — الحادثة

**الثوابت:**

- **INV-INC-01** — severity تزداد فقط عبر CMD-INC-ESCALATE وتنقص فقط عبر CMD-INC-DE-ESCALATE؛ لا تتغير كأثر جانبي لأي أمر آخر
- **INV-INC-02** — CLOSED فقط عندما تكون كل مهمة استجابة مرتبطة في حالة نهائية (يماثل PLAN.COMPLETE وTASK.CLOSE)
- **INV-INC-03** — تفعيل خطة الاستمرارية أمر صريح مخوَّل دائماً، ليس أثراً تلقائياً لتصعيد الخطورة وحده
- **INV-INC-04** — خطر مرتبط (risk_ref) لا تتغير حالته تلقائياً أبداً بإنشاء هذه الحادثة أو تصعيدها أو إغلاقها؛ مالك الخطر يتصرف بأمر منفصل (يماثل INV-RIS-05)
- **INV-INC-05** — كل أمر مقبول ينتج حدثاً واحداً بالضبط وسجل تدقيق واحداً

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-INC-REPORT | ∅ | category_ref (RD-HAZARD-CATEGORIES)؛ description؛ scope_refs ≥ 1؛ risk_ref اختياري (خطر تحقَّق)؛ severity ابتدائية MINOR؛ label ≥ تصنيف النطاق | INCIDENT_INVALID |
| CMD-INC-ASSESS | REPORTED | severity ∈ {MINOR,MAJOR,EMERGENCY,CRISIS}؛ affected_scope_refs؛ مقيّم مخوَّل | INCIDENT_INVALID |
| CMD-INC-DISPATCH-RESPONSE | ASSESSED | commander؛ ≥ 1 response_task_ref (مهام SLC-03 مرتبطة عبر incident_ref — CR-61) | RESPONSE_REQUIRED |
| CMD-INC-CONTAIN | RESPONDING | القائد يؤكد الاحتواء؛ ملاحظة احتواء | REASON_REQUIRED |
| CMD-INC-RESOLVE | CONTAINED | كل مهام الاستجابة في حالة نهائية (INV-INC-02)؛ ملاحظة حل | RESPONSE_TASKS_OPEN |
| CMD-INC-CLOSE | RESOLVED | ملاحظة إغلاق؛ after_action_ref اختياري (كائن معرفة، SLC-12 — R3-Q5) | REASON_REQUIRED |
| CMD-INC-CANCEL | REPORTED | سبب (إنذار كاذب) | REASON_REQUIRED |
| CMD-INC-ESCALATE | أي حالة غير نهائية | سبب؛ new_severity أعلى من الحالية فقط (INV-INC-01)؛ إشعار المستوى الأعلى | SEVERITY_MUST_INCREASE |
| CMD-INC-DE-ESCALATE | أي حالة غير نهائية | سلطة؛ سبب؛ new_severity أدنى بمستوى واحد كحد أقصى (INV-INC-01) | REASON_REQUIRED |
| CMD-INC-ACTIVATE-CONTINGENCY | أي حالة غير نهائية | سلطة؛ ينشئ/يربط Plan (SLC-08، plan_kind=CONTINGENCY، triggered_by=هذه الحادثة — CR-60)؛ أمر صريح دائماً، ليس أثراً تلقائياً للتصعيد (INV-INC-03) | PLAN_LINK_INVALID |
| SYS:response SLA elapsed without dispatch | REPORTED, ASSESSED | المجدول؛ SLA حسب severity، موسوم 'تُعاد معايرته بعد Pilot R1/R2' (RSK-028) | — |

**بيانات مرجعية مستخدمة:** RD-HAZARD-CATEGORIES (`04-information/reference-data.md`)

#### AGG-NOTIFICATION — الإشعار

**الثوابت:**

- **INV-NTF-01** — a notification is not a domain event and never carries business content (glossary)
- **INV-NTF-02** — push payloads contain no classified content: reference URN + template title chosen from a classification-safe list (REQ-COM-002)
- **INV-NTF-03** — opening a notification performs a normal authorized read; a revoked user sees not-found

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| SYS:notifiable event for recipient | ∅ | recipient ACTIVE; recipient authorized for the referenced object at enqueue time | — |
| SYS:delivered to channel | QUEUED | re-check authorization at delivery (security_version); push payload = reference + classification-safe title template | — |
| SYS:recipient no longer authorized at delivery | QUEUED | re-check failed | — |
| SYS:delivery failed after retries | QUEUED | 5 attempts with exponential backoff; in-app copy remains | — |
| CMD-NTF-MARK-READ | SENT | actor = recipient; content fetched through normal authorized query | NOT_RECIPIENT |
| SYS:TTL (30 d) elapsed | QUEUED, SENT | scheduler | — |

#### AGG-OUTCOME-TRACKER — متتبّع النتائج

**الثوابت:**

- **INV-OUT-01** — measurements are bitemporal records; corrections never overwrite
- **INV-OUT-02** — progress = latest measurement known at K vs target valid at T

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| SYS:outcome baselined | ∅ | one tracker per (plan, outcome id); target copied from baseline | — |
| SYS:target changed by new baseline | ACTIVE | target history appended (valid time = baseline time) | — |
| CMD-OUT-RECORD | ACTIVE | value with unit convertible to metric unit (UCUM); measured_at; source = manual \| task result \| observation ref | MEASUREMENT_INVALID |
| CMD-OUT-CORRECT | ACTIVE | corrects a measurement: previous record closed (recorded_to), corrected record added — no overwrite | REASON_REQUIRED |
| SYS:plan closed or cancelled | ACTIVE | system | — |

#### AGG-PLAN — الخطة

**الثوابت:**

- **INV-PLN-01** — ACTIVE ⇔ exactly one BASELINED version exists
- **INV-PLN-02** — a plan implements ≥ 1 decision or objective, or (plan_kind=CONTINGENCY) ≥ 1 risk or incident trigger (CR-60)
- **INV-PLN-03** — plan identity holds no content; content lives in versions (CR-29)
- **INV-PLN-04** — plan_kind ∈ {OPERATIONS, CONTINGENCY}, immutable after creation; only a CONTINGENCY plan may carry a triggered_by reference (CR-60, SLC-17)

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-PLN-CREATE | ∅ | title; owner; org scope; implements ≥ 1 decision (RECORDED) or objective (REQ-OPS-002), or for plan_kind=CONTINGENCY a risk_ref or incident_ref trigger (CR-60, SLC-17); label ≥ implemented decisions or triggering scope's label | PLAN_INVALID |
| SYS:first version baselined | DRAFT | EVT-PLV-BASELINED for this plan | — |
| CMD-PLN-SUSPEND | ACTIVE | reason; open tasks suspended (flag, INV-TASK-06) | REASON_REQUIRED |
| CMD-PLN-RESUME | SUSPENDED | reason; tasks unsuspended | REASON_REQUIRED |
| CMD-PLN-COMPLETE | ACTIVE | all plan tasks terminal; every outcome has ≥ 1 measurement | PLAN_NOT_COMPLETABLE |
| CMD-PLN-CLOSE | COMPLETED | after-action notes (optional in R1); outcome trackers closed | — |
| CMD-PLN-CANCEL | DRAFT, ACTIVE, SUSPENDED | authority; reason; open tasks cancelled | REASON_REQUIRED |
| CMD-PLN-RECLASSIFY | DRAFT, ACTIVE, SUSPENDED | authority; new label ≥ implemented decisions; assignees without clearance → reassignment required | CLASSIFICATION_CHANGE_NOT_AUTHORIZED |
| SYS:implemented decision annulled or superseded | ACTIVE, SUSPENDED | plan flagged for review (no automatic change) | — |

#### AGG-PLAN-VERSION — إصدار الخطة

**الثوابت:**

- **INV-PLV-01** — content is immutable from IN_REVIEW onwards; BASELINED content never changes (BRL-004, REQ-OPS-003)
- **INV-PLV-02** — exactly one BASELINED version per plan
- **INV-PLV-03** — activity ids are stable across versions, so task synchronization is a deterministic diff
- **INV-PLV-04** — a major change (objectives, outcomes, phases, milestone dates, resource commitments) is possible only through a new version (BRL-005)
- **INV-PLV-05** — dependencies acyclic; all dates inside the plan window

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-PLV-DRAFT | ∅ | plan not CLOSED/CANCELLED; new or revision copying the BASELINED version (activity ids preserved); ≤ 1 DRAFT/IN_REVIEW per plan | DRAFT_EXISTS |
| CMD-PLV-EDIT | DRAFT | objectives, outcomes (metric, unit, target, due), phases, activities (stable ids, task_generating flag, task type), milestones, schedule within plan window, acyclic dependencies | PLAN_VERSION_INVALID |
| CMD-PLV-SUBMIT | DRAFT | complete per REQ-OPS-001; change classification computed vs current baseline (major/minor, BRL-005) | PLAN_VERSION_INCOMPLETE |
| CMD-PLV-RETURN | IN_REVIEW | reviewer; reason | REASON_REQUIRED |
| CMD-PLV-APPROVE | IN_REVIEW | approver ≠ author (REQ-OPS-005); AuthorityCheck(approver, plan-approval type, scope); previous BASELINED → SUPERSEDED in the same transaction; task synchronization started (SPEC-PLAN §3) | SEGREGATION_OF_DUTIES |
| CMD-PLV-REJECT | IN_REVIEW | reason | REASON_REQUIRED |
| CMD-PLV-AMEND-MINOR | BASELINED | only minor fields (descriptions, notes, attachments) per BRL-005; recorded as annotation, baseline content unchanged | MAJOR_CHANGE_REQUIRES_VERSION |
| SYS:newer version baselined | BASELINED | system | — |
| CMD-PLV-DISCARD | DRAFT | author; reason | REASON_REQUIRED |

**فصل المهام:** CMD-PLV-APPROVE: approver ≠ author (REQ-OPS-005); AuthorityCheck plan-approval

#### AGG-RISK — الخطر

**الثوابت:**

- **INV-RIS-01** — المقيّم ≠ المحدِّد عند سياسة المستأجر لفصل الواجبات (يماثل INV-TASK-07)
- **INV-RIS-02** — risk_score = likelihood × impact، محسوب عند كل تقييم، لا يُدخله الفاعل مباشرة
- **INV-RIS-03** — TREATED يتطلب ≥ 1 إجراء معالجة مرتبط إلا إذا كانت الاستراتيجية accept بموافقة مخوَّلة صريحة
- **INV-RIS-04** — CLOSED يتطلب rationale صريحاً دائماً؛ لا يوجد أمر لإعادة فتح خطر مُغلَق — إعادة تحديده تنشئ Risk جديداً
- **INV-RIS-05** — ربط حادثة متحقِّقة بهذا الخطر (risk_ref) لا يغيّر حالة الخطر تلقائياً أبداً؛ مالك الخطر يتصرف بأمر منفصل (لا أثر جانبي صامت — درس SLC-09)

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-RIS-IDENTIFY | ∅ | category_ref (RD-HAZARD-CATEGORIES، مرجع لكل مستأجر — نمط R2-Q1)؛ description؛ scope_refs ≥ 1 (أصل/منطقة/منظمة/خطة)؛ label ≥ تصنيف النطاق | RISK_INVALID |
| CMD-RIS-ASSESS | IDENTIFIED | likelihood ∈ 1..5؛ impact ∈ 1..5؛ risk_score محسوب لا يُدخَل مباشرة (INV-RIS-02)؛ المقيّم ≠ المحدِّد عند سياسة فصل الواجبات (INV-RIS-01) | SEGREGATION_OF_DUTIES |
| CMD-RIS-PLAN-TREATMENT | ASSESSED | treatment_strategy ∈ {avoid,reduce,transfer,accept}؛ ≥ 1 إجراء معالجة إلا عند accept (INV-RIS-03)؛ موافق مخوَّل | TREATMENT_INVALID |
| CMD-RIS-REASSESS | ASSESSED, TREATED | likelihood/impact جديدان؛ سبب؛ المقيّم ≠ المحدِّد عند سياسة فصل الواجبات | SEGREGATION_OF_DUTIES |
| CMD-RIS-CLOSE | IDENTIFIED, ASSESSED, TREATED | rationale ∈ {retired,accepted_permanently,materialized}؛ إن كان materialized فـ incident_ref إلزامي (INV-RIS-04)؛ لا أمر لإعادة الفتح — الخطر المُعاد تحديده خطر جديد | RATIONALE_REQUIRED |
| SYS:incident references this risk as risk_ref | أي حالة غير نهائية | رابط تلقائي عند تسجيل حادثة تحقَّق منها هذا الخطر؛ لا يغيّر حالة الخطر تلقائياً أبداً (INV-RIS-05) | — |

**فصل المهام:** CMD-RIS-ASSESS: assessor ≠ identifier when tenant policy requires it (INV-RIS-01)؛ CMD-RIS-REASSESS: assessor ≠ identifier when tenant policy requires it (INV-RIS-01)

**بيانات مرجعية مستخدمة:** RD-HAZARD-CATEGORIES (`04-information/reference-data.md`)

#### AGG-SUBSCRIPTION — الاشتراك

**الثوابت:**

- **INV-SUB-01** — a subscription never grants access; delivery re-checks authorization
- **INV-SUB-02** — subscriptions end automatically when the target becomes invisible to the subscriber

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-SUB-SUBSCRIBE | ∅ | target (situation \| alert rule) visible to subscriber; channels ⊆ {in_app, push}; one ACTIVE per (user, target) | SUBSCRIPTION_EXISTS |
| CMD-SUB-UPDATE-CHANNELS | ACTIVE, PAUSED | channels valid; quiet hours valid (critical severity bypasses quiet hours) | SUBSCRIPTION_INVALID |
| CMD-SUB-RESUME | PAUSED | target still visible | TARGET_NOT_VISIBLE |
| CMD-SUB-UNSUBSCRIBE | ACTIVE, PAUSED | actor = subscriber or Administrator | — |
| SYS:subscriber lost visibility of target | ACTIVE, PAUSED | security-version change or reclassification | — |

#### AGG-TASK — المهمة

**الثوابت:**

- **INV-TASK-01** — no transition from COMPLETED or any terminal state to IN_PROGRESS
- **INV-TASK-02** — COMPLETED only when every completion criterion is satisfied (BRL-006)
- **INV-TASK-03** — every accepted command produces exactly one event and one audit record
- **INV-TASK-04** — terminal states accept no state-changing command
- **INV-TASK-05** — from ASSIGNED onwards the assignee was eligible and cleared at assignment time (recorded with the eligibility result)
- **INV-TASK-06** — while suspended = true, every state-changing command except UNSUSPEND and CANCEL is rejected with TASK_SUSPENDED (orthogonal flag, not a state)
- **INV-TASK-07** — approver ≠ assignee under default policy (REQ-OPS-009)
- **INV-TASK-08** — the dependency graph is acyclic
- **INV-TASK-09** — completion criteria are frozen from ASSIGNED onwards

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-TASK-CREATE | ∅ | task type ACTIVE (version pinned); plan_ref (operations, collection or contingency plan — CR-59, CR-61) or incident_ref (direct response task under an Incident, SLC-17 — CR-61), or ad_hoc_reason + accountable owner (REQ-OPS-010); label ≤ creator clearance | TASK_INVALID |
| CMD-TASK-EDIT | DRAFT, READY | creator or Planner; completion criteria editable only in DRAFT/READY; new version | TASK_INVALID |
| CMD-TASK-MARK-READY | DRAFT | title, ≥ 1 completion criterion, owner; dependencies reference existing tasks without cycle | TASK_NOT_READY |
| CMD-TASK-ASSIGN | READY | assignee ACTIVE user; assignee clearance ≥ task label; EligibilityCheck(assignee, task type, now) ∈ {ELIGIBLE, CONDITIONALLY_ELIGIBLE with condition met} (REQ-OPS-007); actor authorized in scope | ASSIGNEE_NOT_ELIGIBLE |
| CMD-TASK-REASSIGN | ASSIGNED, ACCEPTED, IN_PROGRESS, BLOCKED | same checks as assign for the new assignee; reason; previous assignee notified | ASSIGNEE_NOT_ELIGIBLE |
| CMD-TASK-ACCEPT | ASSIGNED | actor = assignee | NOT_ASSIGNEE |
| CMD-TASK-DECLINE | ASSIGNED | actor = assignee; reason | REASON_REQUIRED |
| CMD-TASK-START | ACCEPTED | actor = assignee; all predecessor tasks COMPLETED or CLOSED | DEPENDENCIES_NOT_MET |
| CMD-TASK-BLOCK | IN_PROGRESS | actor = assignee; blocking reason | REASON_REQUIRED |
| CMD-TASK-RESUME | BLOCKED | actor = assignee; resolution note | REASON_REQUIRED |
| CMD-TASK-ADD-RESULT-ITEM | IN_PROGRESS, BLOCKED | actor = assignee; item = note \| evidence URN \| observation URN \| measurement | RESULT_ITEM_INVALID |
| CMD-TASK-SUBMIT | IN_PROGRESS | actor = assignee; result has ≥ 1 item | RESULT_REQUIRED |
| CMD-TASK-START-REVIEW | SUBMITTED | actor has review permission in scope; actor ≠ assignee | SEGREGATION_OF_DUTIES |
| CMD-TASK-RETURN | UNDER_REVIEW | reviewer; rework reason | REASON_REQUIRED |
| CMD-TASK-APPROVE | UNDER_REVIEW | reviewer ≠ assignee unless tenant policy disables SoD (REQ-OPS-009) | SEGREGATION_OF_DUTIES |
| CMD-TASK-REJECT | UNDER_REVIEW | reviewer; reason; follow-up task may be created linked by follow_up_of (OQ-033) | REASON_REQUIRED |
| SYS:all completion criteria satisfied | APPROVED | system-checkable criteria evaluated at approval and whenever result evidence changes (BRL-006) | — |
| CMD-TASK-COMPLETE | APPROVED | attestation-type criteria confirmed by an authorized actor; all criteria satisfied (BRL-006) | TASK_CRITERIA_NOT_MET |
| CMD-TASK-CLOSE | COMPLETED | no open follow-up tasks | OPEN_FOLLOW_UPS |
| SYS:follow-up window (7 d) elapsed without open follow-ups | COMPLETED | scheduler | — |
| CMD-TASK-CANCEL | DRAFT, READY, ASSIGNED, ACCEPTED, IN_PROGRESS, BLOCKED, SUBMITTED, UNDER_REVIEW, APPROVED | actor has cancel authority in scope; reason | REASON_REQUIRED |
| SYS:due passed and task type expires_on_due | DRAFT, READY, ASSIGNED, ACCEPTED, IN_PROGRESS, BLOCKED, SUBMITTED, UNDER_REVIEW | scheduler; only when the task type declares expires_on_due = true (OQ-032) | — |
| SYS:plan version baselined without this task | DRAFT, READY, ASSIGNED, ACCEPTED, IN_PROGRESS, BLOCKED, SUBMITTED, UNDER_REVIEW, APPROVED | SLC-08 trigger | — |
| CMD-TASK-ESCALATE | أي حالة غير نهائية | reason; notifies next authority level (REQ-OPS-012) | REASON_REQUIRED |
| SYS:due passed (escalation policy) | أي حالة غير نهائية | scheduler; at due and at due + grace from task type | — |
| CMD-TASK-SET-DUE | DRAFT, READY, ASSIGNED, ACCEPTED, IN_PROGRESS, BLOCKED | Planner or owner; reason | REASON_REQUIRED |
| CMD-TASK-SUSPEND | أي حالة غير نهائية | suspend authority; reason; sets suspended = true | REASON_REQUIRED |
| CMD-TASK-UNSUSPEND | أي حالة غير نهائية | suspend authority; suspended = true | NOT_SUSPENDED |
| CMD-TASK-RECLASSIFY | أي حالة غير نهائية | authority per tenant policy; assignee clearance ≥ new label, else reassignment required first | CLASSIFICATION_CHANGE_NOT_AUTHORIZED |

**فصل المهام:** CMD-TASK-APPROVE: reviewer ≠ assignee (PB-06)؛ CMD-TASK-ASSIGN: assignee clearance ≥ task label؛ CMD-TASK-REASSIGN: assignee clearance ≥ task label؛ CMD-TASK-START-REVIEW: reviewer ≠ assignee

#### AGG-TASK-TYPE — نوع المهمة

**الثوابت:**

- **INV-TTY-01** — tasks pin the task-type version at creation
- **INV-TTY-02** — expires_on_due defaults to false; escalation defaults: at due and due + 24 h
- **INV-TTY-03** — offline-capable commands are limited to ACCEPT, START, BLOCK, RESUME, ADD-RESULT-ITEM, SUBMIT

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-TTY-DEFINE | ∅ | code unique in tenant | TASK_TYPE_CODE_TAKEN |
| CMD-TTY-EDIT | DRAFT, ACTIVE | required qualifications exist in RD-COMPETENCIES; criteria templates valid; ACTIVE → new version (existing tasks keep their pinned version) | TASK_TYPE_INVALID |
| CMD-TTY-ACTIVATE | DRAFT | ≥ 1 completion criterion template | TASK_TYPE_INVALID |
| CMD-TTY-RETIRE | ACTIVE | reason; existing tasks unaffected | REASON_REQUIRED |

**بيانات مرجعية مستخدمة:** RD-COMPETENCIES (`04-information/reference-data.md`)

### BC05 — Readiness — الموارد والجاهزية

#### AGG-ALLOCATION — تخصيص الموارد

**الثوابت:**

- **INV-ALC-01** — COMMITTED quantity is reserved in the capacity ledger for every hour of its window; release returns the unused part
- **INV-ALC-02** — contention is resolved by priority, then request time, inside each pool's ordering window (SPEC-ALLOCATION §2)
- **INV-ALC-03** — pre-emption only through a recorded decision with authority; never automatic
- **INV-ALC-04** — approver ≠ requester when approval is required

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-ALC-REQUEST | ∅ | pool ACTIVE; quantity > 0 in pool unit; window; priority 1–5; target task/activity/logistics-request (CR-62, SLC-18); requester | ALLOCATION_INVALID |
| SYS:all checks passed | REQUESTED | SPEC-ALLOCATION §1 checks + capacity ledger reserve in priority order (§2) | — |
| SYS:checks passed, policy requires approval | REQUESTED | PDP obligation REQUIRE_APPROVAL; capacity provisionally held ≤ 1 h | — |
| SYS:a check failed | REQUESTED | reason codes per failed check | — |
| CMD-ALC-APPROVE | PENDING_APPROVAL | approver with allocation authority ≠ requester; capacity still available | CAPACITY_UNAVAILABLE |
| CMD-ALC-REJECT | PENDING_APPROVAL | reason | REASON_REQUIRED |
| SYS:provisional hold (1 h) elapsed | PENDING_APPROVAL | capacity released | — |
| CMD-ALC-RECORD-CONSUMPTION | COMMITTED | quantity in pool unit; time; consumption beyond commitment flagged (REQ-RES-010) | CONSUMPTION_INVALID |
| CMD-ALC-PREEMPT | COMMITTED | pre-emption decision (BC04 Decision) by an authority for the pool scope; higher-priority allocation reference; owners notified (REQ-RES-009) | AUTHORITY_REQUIRED |
| CMD-ALC-RELEASE | COMMITTED | requester or task owner; unused quantity returned to the ledger | — |
| SYS:linked task terminal | COMMITTED | SLC-03 events (REQ-RES-011) | — |

**فصل المهام:** CMD-ALC-APPROVE: approver ≠ requester؛ CMD-ALC-PREEMPT: decision by pool-scope authority

#### AGG-ASSET — الأصل

**الثوابت:**

- **INV-AST-01** — available(asset, window) ⇔ IN_SERVICE ∧ required certifications valid throughout window ∧ no overlapping maintenance window, CONFIRMED/HELD reservation or ACTIVE assignment (REQ-RES-003/004/014)
- **INV-AST-02** — custody chain is gapless; each transfer by the current holder or custodian authority (REQ-RES-002)
- **INV-AST-03** — location lives as bitemporal claims on the linked information entity, never as a column (REQ-RES-005)
- **INV-AST-04** — an expired certification makes the asset unavailable for new assignments from that instant, evaluated at read time

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-AST-REGISTER | ∅ | type in RD-ASSET-TYPES; owner org; custody holder ACTIVE; linked information entity (entity_type asset-ref) created or referenced in BC02; capabilities; label | ASSET_INVALID |
| CMD-AST-UPDATE-CONDITION | IN_SERVICE, UNSERVICEABLE, UNDER_MAINTENANCE | condition grade in RD-CONDITION-GRADES; inspector; unserviceable grades require CMD-AST-MARK-UNSERVICEABLE | CONDITION_INVALID |
| CMD-AST-MARK-UNSERVICEABLE | IN_SERVICE | reason; active assignments are notified; future reservations flagged | REASON_REQUIRED |
| CMD-AST-START-MAINTENANCE | IN_SERVICE, UNSERVICEABLE | maintenance order IN_PROGRESS for this asset | MAINTENANCE_ORDER_REQUIRED |
| CMD-AST-RETURN-TO-SERVICE | UNDER_MAINTENANCE | maintenance order COMPLETED; condition serviceable; required certifications valid | ASSET_NOT_SERVICEABLE |
| CMD-AST-FAIL-MAINTENANCE | UNDER_MAINTENANCE | maintenance order COMPLETED with outcome failed; reason | REASON_REQUIRED |
| CMD-AST-TRANSFER-CUSTODY | IN_SERVICE, UNSERVICEABLE, UNDER_MAINTENANCE | actor is current holder or custodian authority; new holder ACTIVE in scope; gapless chain | CUSTODY_INVALID |
| CMD-AST-SET-CERTIFICATION | IN_SERVICE, UNSERVICEABLE, UNDER_MAINTENANCE | certification code, issuer, valid_from/to; evidence | CERTIFICATION_INVALID |
| CMD-AST-REPORT-LOST | IN_SERVICE, UNSERVICEABLE | reason; active assignments ended; reservations cancelled | REASON_REQUIRED |
| CMD-AST-RECOVER | LOST | found; inspection required before service | — |
| CMD-AST-DISPOSE | UNSERVICEABLE, LOST | disposal authority (decision type asset-disposal); no active reservation or assignment; no legal hold | AUTHORITY_REQUIRED |
| CMD-AST-RECLASSIFY | IN_SERVICE, UNSERVICEABLE, UNDER_MAINTENANCE, LOST | authority per policy | CLASSIFICATION_CHANGE_NOT_AUTHORIZED |

**فصل المهام:** CMD-AST-DISPOSE: asset-disposal authority

**بيانات مرجعية مستخدمة:** RD-ASSET-TYPES, RD-CONDITION-GRADES (`04-information/reference-data.md`)

#### AGG-ASSET-ASSIGNMENT — إسناد الأصل

**الثوابت:**

- **INV-ASG-01** — at most one ACTIVE assignment per asset at a time
- **INV-ASG-02** — assignment respects BRL-007 (asset certification and custody authorization)

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-ASG-ASSIGN | ∅ | asset available (or covered by the caller's CONFIRMED reservation); asset certifications satisfy the task type's asset requirements; custody authorization; assignee cleared for asset label | ASSET_NOT_AVAILABLE |
| CMD-ASG-RETURN | ACTIVE | condition report; asset condition updated accordingly | CONDITION_REPORT_REQUIRED |
| SYS:linked task terminal | ACTIVE | condition report requested from last holder (follow-up task) | — |
| CMD-ASG-CANCEL | ACTIVE | assigned in error; reason | REASON_REQUIRED |

#### AGG-ASSET-RESERVATION — حجز الأصل

**الثوابت:**

- **INV-RSV-01** — no two HELD/CONFIRMED reservations of one asset overlap in time (exclusion on (asset, window)) — REQ-RES-014
- **INV-RSV-02** — a HELD reservation expires after 24 h unless confirmed (W4 delegated decision)

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-RSV-HOLD | ∅ | asset available for the window (INV-AST-01); purpose; requester authorized in asset owner scope | ASSET_RESERVED |
| CMD-RSV-CONFIRM | HELD | linked to a task or plan activity | LINK_REQUIRED |
| SYS:hold expiry (24 h) reached | HELD | scheduler | — |
| CMD-RSV-RELEASE | CONFIRMED | requester or linked task terminal | — |
| SYS:linked task or plan terminal | CONFIRMED | SLC-03/SLC-08 events | — |
| CMD-RSV-CANCEL | HELD, CONFIRMED | requester or asset owner; reason | REASON_REQUIRED |

#### AGG-EXERCISE — التمرين

**الثوابت:**

- **INV-EXR-01** — an exercise is planned only against a scenario that is ACTIVE at that instant; the reference is frozen — later scenario edits (new versions) never retroactively change an already-planned exercise
- **INV-EXR-02** — an exercise's terminal outcome (COMPLETED vs ABORTED) is always driven exclusively by its linked simulation's own outcome; no human command sets either state directly

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-EXR-PLAN | ∅ | scenario ACTIVE at this instant, frozen thereafter (INV-EXR-01); objectives; participants; purpose; role_ref optional (readiness comparison reuses SLC-09's AGG-ROLE-REQUIREMENT read-only, no new eligibility mechanism) | EXERCISE_INVALID |
| CMD-EXR-SCHEDULE | PLANNED | window.from < window.to; location; participants confirmed | EXERCISE_INVALID |
| CMD-EXR-START | SCHEDULED | scheduled window reached (or authorized override); system creates a linked Simulation in the same unit of work (CMD-SIM-START, exercise_ref = this, scenario_ref = the frozen scenario — mirrors the linked-creation pattern of CR-62) | EXERCISE_INVALID |
| SYS:linked simulation completed | IN_PROGRESS | system; driven exclusively by the linked Simulation's own EVT-SIM-COMPLETED (INV-EXR-02) | — |
| SYS:linked simulation aborted | IN_PROGRESS | system; driven exclusively by the linked Simulation's own EVT-SIM-ABORTED (INV-EXR-02) | — |
| CMD-EXR-CANCEL | PLANNED, SCHEDULED | reason | REASON_REQUIRED |

#### AGG-LOGISTICS-REQUEST — طلب الإمداد

**الثوابت:**

- **INV-LGR-01** — every REQUESTED logistics request creates exactly one linked resource allocation in the same unit of work, targeting this request (CR-62); the two never diverge except through each other's own system-driven events
- **INV-LGR-02** — dispatch (IN_TRANSIT) is only possible from APPROVED, only while the linked allocation is still COMMITTED, and only for a ship_quantity not exceeding the requested quantity
- **INV-LGR-03** — FULFILLED requires delivered_quantity = requested quantity; anything less, including a total loss, is PARTIALLY_FULFILLED — never silently marked FULFILLED
- **INV-LGR-04** — cancellation always releases or lets expire the linked allocation; a CANCELLED request never leaves a dangling COMMITTED allocation
- **INV-LGR-05** — consumption is recorded on the linked allocation only from confirmed shipment outcomes (SLC-18 EVT-SHP-DELIVERED/-DAMAGED/-LOST), never speculatively at dispatch time

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-LGR-REQUEST | ∅ | item pool ACTIVE (AGG-RESOURCE-POOL, resource_type in RD-LOGISTICS-ITEM-TYPES); quantity > 0 in pool unit; destination; needed_by; priority 1–5; requester; justification; system issues a linked allocation request in the same unit of work (CMD-ALC-REQUEST, target = this request — CR-62) | LOGISTICS_REQUEST_INVALID |
| SYS:linked allocation committed | REQUESTED | SLC-09 EVT-ALC-COMMITTED for the linked allocation | — |
| SYS:linked allocation requires approval | REQUESTED | SLC-09 EVT-ALC-APPROVAL-REQUIRED for the linked allocation | — |
| SYS:linked allocation rejected | REQUESTED | SLC-09 EVT-ALC-REJECTED for the linked allocation; reason codes carried over | — |
| SYS:linked allocation committed | PENDING_APPROVAL | SLC-09 EVT-ALC-COMMITTED for the linked allocation | — |
| SYS:linked allocation rejected | PENDING_APPROVAL | SLC-09 EVT-ALC-REJECTED for the linked allocation (approval denied or provisional hold elapsed) | — |
| CMD-LGR-DISPATCH | APPROVED | dispatcher; linked allocation still COMMITTED; creates a Shipment (AGG-SHIPMENT) referencing this request and the allocation; ship_quantity ≤ requested quantity | ALLOCATION_NOT_COMMITTED |
| SYS:linked shipment delivered in full | IN_TRANSIT | SLC-18 EVT-SHP-DELIVERED with delivered_quantity = requested quantity; records consumption on the linked allocation (CMD-ALC-RECORD-CONSUMPTION) | — |
| SYS:linked shipment resolved short | IN_TRANSIT | SLC-18 EVT-SHP-DELIVERED with delivered_quantity < requested quantity, or EVT-SHP-DAMAGED / EVT-SHP-LOST; records consumption for the quantity actually delivered before the incident (possibly zero) | — |
| CMD-LGR-CANCEL | REQUESTED, PENDING_APPROVAL, APPROVED | requester or logistics authority; reason; releases the linked allocation if COMMITTED (CMD-ALC-RELEASE), or leaves a PENDING_APPROVAL allocation to its own provisional-hold expiry | REASON_REQUIRED |

**بيانات مرجعية مستخدمة:** RD-LOGISTICS-ITEM-TYPES (`04-information/reference-data.md`)

#### AGG-MAINTENANCE-ORDER — أمر الصيانة

**الثوابت:**

- **INV-MNT-01** — a PLANNED or IN_PROGRESS window blocks availability (INV-AST-01)
- **INV-MNT-02** — no two non-terminal orders of one asset overlap

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-MNT-PLAN | ∅ | asset not DISPOSED; kind ∈ {scheduled, corrective}; window; no overlap with another non-terminal order of the asset | MAINTENANCE_OVERLAP |
| CMD-MNT-RESCHEDULE | PLANNED | new window without overlap; affected reservations flagged | MAINTENANCE_OVERLAP |
| CMD-MNT-START | PLANNED | technician; asset moves to UNDER_MAINTENANCE via its own command (policy) | — |
| CMD-MNT-COMPLETE | IN_PROGRESS | outcome ∈ {serviceable, failed}; work performed; parts consumed (optional allocation refs) | OUTCOME_REQUIRED |
| CMD-MNT-CANCEL | PLANNED | reason | REASON_REQUIRED |

#### AGG-QUALIFICATION-RECORD — سجل التأهيل

**الثوابت:**

- **INV-QUAL-01** — eligibility evaluates validity at the requested time even if the EXPIRED transition is late
- **INV-QUAL-02** — records are never deleted; history supports as-of eligibility

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-QUAL-RECORD | ∅ | person ACTIVE; code in RD-COMPETENCIES; level valid; valid_from < valid_to; issuer; evidence ref optional | QUALIFICATION_INVALID |
| CMD-QUAL-RENEW | ACTIVE | new valid_to > old; evidence; new version | QUALIFICATION_INVALID |
| CMD-QUAL-SUSPEND | ACTIVE | reason | REASON_REQUIRED |
| CMD-QUAL-REINSTATE | SUSPENDED | validity not ended | QUALIFICATION_EXPIRED |
| CMD-QUAL-REVOKE | ACTIVE, SUSPENDED | reason | REASON_REQUIRED |
| SYS:valid_to reached | ACTIVE, SUSPENDED | scheduler (eligibility also checks validity at read time) | — |

**بيانات مرجعية مستخدمة:** RD-COMPETENCIES (`04-information/reference-data.md`)

#### AGG-RESOURCE-POOL — مجمع الموارد

**الثوابت:**

- **INV-RPL-01** — capacity is a time series (valid_from); history kept (bitemporal record)
- **INV-RPL-02** — for every time bucket, Σ committed quantity ≤ capacity (enforced by the capacity ledger — SPEC-ALLOCATION §2)

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-RPL-CREATE | ∅ | type in RD-RESOURCE-TYPES; unit (UCUM); org scope; initial capacity; label | POOL_INVALID |
| CMD-RPL-ADJUST-CAPACITY | ACTIVE, SUSPENDED | new capacity with valid_from; reason; a reduction below committed quantity requires pre-emption decisions first | CAPACITY_BELOW_COMMITMENTS |
| CMD-RPL-SUSPEND | ACTIVE | reason; no new allocations | REASON_REQUIRED |
| CMD-RPL-CLOSE | ACTIVE, SUSPENDED | no COMMITTED or PENDING allocations | POOL_HAS_COMMITMENTS |

**بيانات مرجعية مستخدمة:** RD-RESOURCE-TYPES (`04-information/reference-data.md`)

#### AGG-ROLE-REQUIREMENT — متطلبات الدور

**الثوابت:**

- **INV-RRQ-01** — one ACTIVE requirement set per role
- **INV-RRQ-02** — readiness is computed at a time t from records valid at t (as-of readiness)

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-RRQ-DEFINE | ∅ | role exists (BC01); requirements reference RD-COMPETENCIES | ROLE_REQUIREMENT_INVALID |
| CMD-RRQ-EDIT | DRAFT, ACTIVE | requirements valid; ACTIVE → new version | ROLE_REQUIREMENT_INVALID |
| CMD-RRQ-ACTIVATE | DRAFT | approver ≠ author | SEGREGATION_OF_DUTIES |
| CMD-RRQ-RETIRE | ACTIVE | reason | REASON_REQUIRED |

**فصل المهام:** CMD-RRQ-ACTIVATE: approver ≠ author

**بيانات مرجعية مستخدمة:** RD-COMPETENCIES (`04-information/reference-data.md`)

#### AGG-SCENARIO — سيناريو التدريب

**الثوابت:**

- **INV-SCN-01** — injects are ordered by strictly increasing offset from exercise start; no simultaneous or decreasing offsets
- **INV-SCN-02** — target competencies reference RD-COMPETENCIES codes; no invented closed catalog

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-SCN-DEFINE | ∅ | title; exercise_type_ref in RD-EXERCISE-TYPES; situation; target_competencies ⊆ RD-COMPETENCIES; injects ordered by strictly increasing offset (INV-SCN-01) | SCENARIO_INVALID |
| CMD-SCN-EDIT | DRAFT, ACTIVE | same validations as DEFINE; editing an ACTIVE scenario creates a new version — exercises already planned against the prior version keep their frozen reference (INV-EXR-01) | SCENARIO_INVALID |
| CMD-SCN-ACTIVATE | DRAFT | approver ≠ author | SEGREGATION_OF_DUTIES |
| CMD-SCN-RETIRE | ACTIVE | reason | REASON_REQUIRED |

**فصل المهام:** CMD-SCN-ACTIVATE: approver ≠ author

**بيانات مرجعية مستخدمة:** RD-COMPETENCIES, RD-EXERCISE-TYPES (`04-information/reference-data.md`)

#### AGG-SHIPMENT — الشحنة

**الثوابت:**

- **INV-SHP-01** — movement history (checkpoints) is append-only and chronologically gapless; no checkpoint is ever edited or removed (mirrors INV-AST-02's gapless custody chain)
- **INV-SHP-02** — delivered, damaged or lost quantity never exceeds the shipment's planned quantity; a shortfall at delivery is recorded on the event, never silently rounded up to delivered in full
- **INV-SHP-03** — departure (IN_TRANSIT) requires the linked logistics request's allocation to still be COMMITTED for at least the shipped quantity at that instant — no shipment ever moves against capacity that was never actually reserved
- **INV-SHP-04** — cancellation is only possible before departure (PLANNED); once IN_TRANSIT the shipment must resolve to DELIVERED, DAMAGED or LOST — never silently cancelled mid-transit

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-SHP-PLAN | ∅ | logistics_request APPROVED; origin pool with sufficient COMMITTED allocation quantity for the linked request; destination; carrier; planned_quantity ≤ the linked allocation's committed quantity | SHIPMENT_INVALID |
| CMD-SHP-DEPART | PLANNED | carrier confirmed; departure checkpoint recorded | DEPARTURE_INVALID |
| CMD-SHP-RECORD-CHECKPOINT | IN_TRANSIT | checkpoint strictly after the previous checkpoint in time (append-only, gapless — mirrors INV-AST-02); location; at; note | CHECKPOINT_INVALID |
| CMD-SHP-DELIVER | IN_TRANSIT | receiving party confirms; delivered_quantity ≤ planned quantity; a shortfall is recorded, never hidden (INV-SHP-02) | DELIVERY_INVALID |
| CMD-SHP-REPORT-DAMAGE | IN_TRANSIT | reason; damaged_quantity ≤ planned quantity; evidence | REASON_REQUIRED |
| CMD-SHP-REPORT-LOST | IN_TRANSIT | reason | REASON_REQUIRED |
| CMD-SHP-CANCEL | PLANNED | reason; only before departure | REASON_REQUIRED |

#### AGG-SIMULATION — تشغيل المحاكاة

**الثوابت:**

- **INV-SIM-01** — inject deliveries are append-only and strictly increasing in time (mirrors INV-SHP-01's checkpoint pattern); no edit or delete command exists
- **INV-SIM-02** — a simulation reaches COMPLETED only when every participant listed on its linked exercise has at least one recorded evaluation
- **INV-SIM-03** — an evaluator never evaluates themself (segregation of duties, mirrors CMD-RRQ-ACTIVATE/CMD-KNO-PUBLISH's reviewer ≠ author pattern)

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-SIM-START | ∅ | system-issued in the same unit of work as CMD-EXR-START; exercise_ref SCHEDULED transitioning to IN_PROGRESS; scenario_ref = the exercise's frozen scenario; started_at | SIMULATION_INVALID |
| CMD-SIM-DELIVER-INJECT | IN_PROGRESS | inject_ref belongs to the linked scenario; delivered_at strictly after the previous delivery (INV-SIM-01) | INJECT_INVALID |
| CMD-SIM-RECORD-EVALUATION | IN_PROGRESS, PAUSED | participant_ref is one of the linked exercise's participants; competency_code in RD-COMPETENCIES; result ∈ {MET, PARTIAL, NOT_MET}; evaluator ≠ participant (INV-SIM-03) | SEGREGATION_OF_DUTIES |
| CMD-SIM-PAUSE | IN_PROGRESS | reason | REASON_REQUIRED |
| CMD-SIM-COMPLETE | IN_PROGRESS, PAUSED | every participant on the linked exercise has ≥ 1 recorded evaluation (INV-SIM-02) | EVALUATION_MISSING |
| CMD-SIM-ABORT | IN_PROGRESS, PAUSED | reason | REASON_REQUIRED |

**فصل المهام:** CMD-SIM-RECORD-EVALUATION: evaluator ≠ participant

**بيانات مرجعية مستخدمة:** RD-COMPETENCIES (`04-information/reference-data.md`)

### BC06 — Knowledge — المعرفة والمنتجات

#### AGG-ARCHIVE-PACKAGE — الحزمة الأرشيفية

**الثوابت:**

- **INV-ARC-01** — originals are never overwritten; format migration adds representations
- **INV-ARC-02** — every retrieval appends to the package's access history (REQ-ARC-003) and is audited
- **INV-ARC-03** — fixity verified at ingest, on every retrieval and at least yearly (REQ-ARC-002)
- **INV-ARC-04** — archive ≠ backup (BRL-011): packages are institutional records with their own retention

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| SYS:disposition action ARCHIVE for a bucket or record set | ∅ | SIP assembled from owner exports: content, metadata, provenance, access history | — |
| SYS:package validated | INGESTING | BagIt structure valid; every file fixity (SHA-256) recorded; preservation formats (R2-Q6) produced alongside originals | — |
| SYS:validation failed | INGESTING | errors recorded | — |
| CMD-ARC-RETRY-INGEST | INGEST_FAILED | archivist; corrective note | REASON_REQUIRED |
| SYS:integrity check failed | ARCHIVED | fixity mismatch on any file | — |
| CMD-ARC-REPAIR | INTEGRITY_FAILED | restored from replica; fixity re-verified | FIXITY_MISMATCH |
| CMD-ARC-MIGRATE-FORMAT | ARCHIVED | new preservation representation added; originals kept; preservation event recorded | FORMAT_INVALID |
| CMD-ARC-TRANSFER | ARCHIVED | transfer authority decision; receipt from the receiving archive | AUTHORITY_REQUIRED |
| SYS:disposition DESTROY executed for the package bucket | ARCHIVED, INTEGRITY_FAILED | SLC-12a key destruction; no active hold | — |

**فصل المهام:** CMD-ARC-TRANSFER: transfer authority decision

#### AGG-DISTRIBUTION — التوزيع

**الثوابت:**

- **INV-DST-01** — a recipient receives a product only if cleared for its label and within its audience (REQ-PRD-004)
- **INV-DST-02** — every delivered copy carries a unique recipient watermark (REQ-PRD-005)
- **INV-DST-03** — withdrawn products stop being downloadable; recipients are notified

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-DST-DISTRIBUTE | ∅ | product APPROVED; recipients (users, org units); formats ⊆ {pdf, docx, in_app}; distributor authorized | PRODUCT_NOT_APPROVED |
| SYS:all recipients authorized and delivered | PREPARING | per-recipient watermark (recipient id, product version, time) embedded; delivery logged | — |
| SYS:some recipients not authorized | PREPARING | unauthorized recipients excluded and listed to the distributor; others delivered | — |
| CMD-DST-CANCEL | PREPARING | distributor; reason | REASON_REQUIRED |

#### AGG-KNOWLEDGE-OBJECT — كائن المعرفة

**الثوابت:**

- **INV-KNO-01** — published versions are immutable; one PUBLISHED version per knowledge object
- **INV-KNO-02** — knowledge statements are not claims about the world (they do not enter BC02 resolution); they cite claims and evidence
- **INV-KNO-03** — policy knowledge describes a policy but never changes authorization (the PDP ignores it) — glossary CR-33

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-KNO-DRAFT | ∅ | type ∈ {procedure, lesson, best_practice, policy_knowledge}; lessons reference a terminal source (task, plan, incident, or a completed exercise simulation — CR-63) and its evidence (REQ-KNW-002); label ≥ source label | KNOWLEDGE_INVALID |
| CMD-KNO-EDIT | DRAFT | statements with evidence links; relationships to task types, plan types, entity types, areas | KNOWLEDGE_INVALID |
| CMD-KNO-SUBMIT | DRAFT | ≥ 1 statement; lessons: ≥ 1 evidence link | KNOWLEDGE_INCOMPLETE |
| CMD-KNO-RETURN | IN_REVIEW | reviewer; reason | REASON_REQUIRED |
| CMD-KNO-PUBLISH | IN_REVIEW | reviewer ≠ author; procedures and policy knowledge require the owning authority (Knowledge Manager + domain authority); previous PUBLISHED → SUPERSEDED | SEGREGATION_OF_DUTIES |
| CMD-KNO-REJECT | IN_REVIEW | reason | REASON_REQUIRED |
| CMD-KNO-RECORD-REUSE | PUBLISHED | target plan/task/product visible; reuse counted (OUT-06) | TARGET_INVALID |
| SYS:newer version published | PUBLISHED | system | — |
| CMD-KNO-RETIRE | PUBLISHED | reason (obsolete, wrong) | REASON_REQUIRED |
| CMD-KNO-DISCARD | DRAFT | author; reason | REASON_REQUIRED |

**فصل المهام:** CMD-KNO-PUBLISH: reviewer ≠ author; domain authority for procedures/policy knowledge

#### AGG-PRODUCT — المنتج

**الثوابت:**

- **INV-PRD-01** — an APPROVED version is immutable; changes are new versions (REQ-PRD-003)
- **INV-PRD-02** — product label ≥ every included content label; content above the label is excluded, and exclusions are not counted in the product (REQ-PRD-002, A21)
- **INV-PRD-03** — data is pinned at generation (known_at), so the product reproduces exactly what was generated
- **INV-PRD-04** — approver ≠ author

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-PRD-CREATE | ∅ | template ACTIVE (version pinned); parameters valid; audience (org units/roles); target label ≥ labels of scope objects referenced in parameters; optional revises = APPROVED version | PRODUCT_INVALID |
| CMD-PRD-GENERATE | DRAFT, GENERATED, GENERATION_FAILED | author; async job with the author's authority | — |
| SYS:generation succeeded | GENERATING | every binding executed as known_at = generation time; content items with label > product label excluded; rendered artifacts hashed | — |
| SYS:generation failed | GENERATING | error recorded | — |
| CMD-PRD-EDIT-NARRATIVE | GENERATED | only narrative sections; data sections change only by regeneration | SECTION_NOT_EDITABLE |
| CMD-PRD-SUBMIT | GENERATED | all required sections present; AI-drafted sections reviewed (REQ-AI-005) | PRODUCT_INCOMPLETE |
| CMD-PRD-RETURN | IN_REVIEW | reviewer; reason | REASON_REQUIRED |
| CMD-PRD-APPROVE | IN_REVIEW | reviewer ≠ author; content frozen with pinned citations; previous APPROVED version of the same product → SUPERSEDED | SEGREGATION_OF_DUTIES |
| SYS:newer version approved | APPROVED | system | — |
| CMD-PRD-WITHDRAW | APPROVED | reason; recipients notified | REASON_REQUIRED |
| CMD-PRD-DISCARD | DRAFT, GENERATED, GENERATION_FAILED | author; reason | REASON_REQUIRED |

**فصل المهام:** CMD-PRD-APPROVE: reviewer ≠ author

#### AGG-PRODUCT-TEMPLATE — قالب المنتج

**الثوابت:**

- **INV-PTM-01** — bindings call only declared queries (no free-form data access), so products obey the same authorization as the UI
- **INV-PTM-02** — products pin the template version

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-PTM-DEFINE | ∅ | code unique; product kind ∈ {report, briefing, map_product, analytical_product} | TEMPLATE_INVALID |
| CMD-PTM-EDIT | DRAFT, ACTIVE | sections valid (text, map, chart, table, key_judgments, citations); every data binding is a declared platform query with typed parameters; ACTIVE → new version | TEMPLATE_INVALID |
| CMD-PTM-ACTIVATE | DRAFT | sample generation succeeded; approver ≠ author | SEGREGATION_OF_DUTIES |
| CMD-PTM-RETIRE | ACTIVE | reason; existing products keep their pinned version | REASON_REQUIRED |

**فصل المهام:** CMD-PTM-ACTIVATE: approver ≠ author

#### AGG-RECONSTRUCTION — إعادة البناء التاريخي

**الثوابت:**

- **INV-REC-01** — every element of the report carries its reconstruction label (PRJ§103, CR-25)
- **INV-REC-02** — the report is reproducible: same scope, T and K give the same result
- **INV-REC-03** — the report never exceeds the requester's authorization; hidden elements are absent, not marked

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-REC-REQUEST | ∅ | scope (objects, situation, plan, decision basis); valid_at T; known_at K ≤ now; purpose (audit, legal, lessons); requester authorized | RECONSTRUCTION_INVALID |
| SYS:worker started | REQUESTED | runs with the requester's authority | — |
| SYS:completed | RUNNING | report: every element labelled RECORDED / RECONSTRUCTED / INFERRED (with rule) / UNKNOWN; archive retrievals included where needed | — |
| SYS:failed | RUNNING | error recorded | — |
| CMD-REC-CANCEL | REQUESTED, RUNNING | requester; reason | REASON_REQUIRED |

### BC07 — Platform Intelligence — التكامل والذكاء الاصطناعي

#### AGG-ADAPTER — المحوّل

**الثوابت:**

- **INV-ADP-01** — an adapter writes only through BC02 commands, as its service account
- **INV-ADP-02** — mapping versions are immutable and referenced by lineage
- **INV-ADP-03** — an adapter is bound to exactly one Source

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-ADP-REGISTER | ∅ | source ACTIVE; service account ACTIVE; mapping spec present | ADAPTER_INVALID |
| CMD-ADP-UPDATE-MAPPING | DRAFT, ACTIVE | mapping tests pass; new immutable mapping version | MAPPING_TESTS_FAILED |
| CMD-ADP-ACTIVATE | DRAFT | mapping tests pass; approver ≠ author | SEGREGATION_OF_DUTIES |
| CMD-ADP-SUSPEND | ACTIVE | reason | REASON_REQUIRED |
| CMD-ADP-RETIRE | DRAFT, ACTIVE, SUSPENDED | reason | REASON_REQUIRED |

**فصل المهام:** CMD-ADP-ACTIVATE: approver ≠ author

#### AGG-AI-REQUEST — طلب الذكاء الاصطناعي

**الثوابت:**

- **INV-AIR-01** — the context package contains only items the requesting user may see at request time (REQ-AI-002)
- **INV-AIR-02** — retrieved content is data: it can never add tools, change recipients, widen scope or raise AIL (REQ-AI-012)
- **INV-AIR-03** — every COMPLETED statement has ≥ 1 citation to a context item (REQ-AI-004)
- **INV-AIR-04** — request, context package hash, model version, prompt template version and output are recorded (REQ-AI-001, BRL-009)
- **INV-AIR-05** — classified context never goes to an external model (REQ-AI-011)

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-AIR-SUBMIT | ∅ | operation ∈ AI autonomy matrix and allowed at the tenant's routing; user authenticated; purpose; input size ≤ limit; per-tenant AI quota | AI_OPERATION_NOT_ALLOWED |
| SYS:policy denied | RECEIVED | PDP on (user, ai.<operation>, scope) denied or AIL above matrix | — |
| SYS:retrieval started | RECEIVED | authorized hybrid retrieval as the user (SPEC-AI §2) | — |
| SYS:context package sealed | RETRIEVING | context items pinned (URN + version/known_at + label); package hash; token budget respected | — |
| SYS:no sufficient evidence retrieved | RETRIEVING | coverage below threshold (SPEC-AI §4) | — |
| SYS:output grounded | GENERATING | every statement cites ≥ 1 context item; citation check passed; output label = max(context labels); guard checks passed (SPEC-AI §5) | — |
| SYS:output not grounded | GENERATING | ungrounded statements removed leave no answer | — |
| SYS:error or timeout | RETRIEVING, GENERATING | error recorded | — |
| CMD-AIR-CANCEL | RECEIVED, RETRIEVING, GENERATING | requester | — |

#### AGG-AI-RESULT — نتيجة الذكاء الاصطناعي

**الثوابت:**

- **INV-AIRS-01** — no AI result changes business state without an accepting human (AIL ≤ 3 in R2; REQ-AI-005/006/008)
- **INV-AIRS-02** — accepted effects keep lineage to request, context package and model version
- **INV-AIRS-03** — review outcomes are fed to the evaluation data set (human feedback)

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| SYS:request COMPLETED for a reviewable operation | ∅ | operation ∈ {AI-OP-03 draft, AI-OP-04 extract, AI-OP-05 translation used as evidence, AI-OP-06 match suggestion} | — |
| CMD-AIRS-START-REVIEW | PROPOSED | reviewer authorized for the target and cleared for the result label | REVIEWER_NOT_CLEARED |
| CMD-AIRS-ACCEPT | UNDER_REVIEW | effects applied through owner commands as the reviewer, with agent = model version in lineage (e.g. CMD-CLM-ASSERT, product section, CMD-ER-PROPOSE) | OWNER_REJECTED |
| CMD-AIRS-ACCEPT-PARTIALLY | UNDER_REVIEW | selected items only; rejected items recorded with reasons | OWNER_REJECTED |
| CMD-AIRS-REJECT | PROPOSED, UNDER_REVIEW | reason (feeds evaluation) | REASON_REQUIRED |

#### AGG-AI-ROUTING — توجيه الذكاء الاصطناعي

**الثوابت:**

- **INV-RTG-01** — max AIL per operation never exceeds the platform autonomy matrix (AIL5 unreachable) — REQ-AI-008
- **INV-RTG-02** — prompt templates are versioned and immutable once referenced
- **INV-RTG-03** — exactly one ACTIVE routing per tenant

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-RTG-DRAFT | ∅ | AI governance authority; ≤ 1 DRAFT per tenant | DRAFT_EXISTS |
| CMD-RTG-EDIT | DRAFT | for each operation: model version in PRODUCTION (or STAGED with canary share), prompt template version, allowed tools, max AIL ≤ autonomy matrix, external model allowed only for unclassified and only if tenant policy allows | ROUTING_INVALID |
| CMD-RTG-ACTIVATE | DRAFT | approver ≠ author; previous ACTIVE → SUPERSEDED | SEGREGATION_OF_DUTIES |
| CMD-RTG-DISCARD | DRAFT | reason | REASON_REQUIRED |
| SYS:successor activated | ACTIVE | system | — |

**فصل المهام:** CMD-RTG-ACTIVATE: approver ≠ author

#### AGG-AI-TOOL — أداة الذكاء الاصطناعي

**الثوابت:**

- **INV-TOL-01** — in R2 no tool has effect 'write'; 'propose' tools create AI results for human review only (REQ-AI-013, INV-AIRS-01)
- **INV-TOL-02** — a tool executes with the requesting user's authority through the platform's own query/command APIs
- **INV-TOL-03** — tools cannot reach external networks (FIT-12)

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-TOL-REGISTER | ∅ | name; input JSON schema; underlying platform query or command; effect ∈ {read, propose}; required permission; max AIL | TOOL_INVALID |
| CMD-TOL-ACTIVATE | DRAFT | security review passed (injection, exfiltration, scope); approver = Security Officer | SECURITY_REVIEW_REQUIRED |
| CMD-TOL-DISABLE | ACTIVE | reason | REASON_REQUIRED |
| CMD-TOL-RETIRE | DRAFT, ACTIVE, DISABLED | reason | REASON_REQUIRED |

**فصل المهام:** CMD-TOL-ACTIVATE: Security Officer

#### AGG-EVAL-SUITE — حزمة التقييم

**الثوابت:**

- **INV-EVS-01** — suites are immutable once ACTIVE; every evaluation report names its suite version
- **INV-EVS-02** — suites include tenant samples before a model serves that tenant (RSK-021 analogue for AI)

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-EVS-DRAFT | ∅ | AI governance | — |
| CMD-EVS-EDIT | DRAFT | sets: groundedness (≥ 500 items), citation, insufficient-evidence, prompt-injection, exfiltration, cross-tenant, Arabic/English/mixed; each item labelled with expected behaviour | SUITE_INVALID |
| CMD-EVS-ACTIVATE | DRAFT | approver ≠ author; previous ACTIVE → SUPERSEDED | SEGREGATION_OF_DUTIES |
| SYS:successor activated | ACTIVE | system | — |

**فصل المهام:** CMD-EVS-ACTIVATE: approver ≠ author

#### AGG-INTEGRATION-CONNECTION — اتصال التكامل

**الثوابت:**

- **INV-CON-01** — every active connection has exactly one egress/ingress allow-list entry, approved by a Security Officer other than the requester
- **INV-CON-02** — no writes into ERP/HRIS/DMS/CMMS in R2 — external systems are sources, never sinks (BRL-013); the only outbound kind is CAP
- **INV-CON-03** — credentials never appear in specifications, logs or events — reference to OpenBao only

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-CON-REGISTER | ∅ | system kind ∈ {erp, hris, dms, cmms, sensor_gateway, cap_endpoint}; endpoint on an internal network; protocol; direction ∈ {inbound, outbound}, outbound only for cap_endpoint in R2 (INV-CON-02); credentials stored in OpenBao (reference only) | CONNECTION_INVALID |
| CMD-CON-TEST | DRAFT | integration engineer; connectivity and schema probe run | — |
| CMD-CON-ACTIVATE | TESTING | probe passed; egress allow-list entry approved by Security Officer ≠ requester (GOV-005) | SEGREGATION_OF_DUTIES |
| CMD-CON-FAIL-TEST | TESTING | probe failed; errors recorded | — |
| SYS:health checks failing 5 min | ACTIVE | backlog buffered by adapters (QAS-INT-001) | — |
| SYS:health restored | DEGRADED | backlog replayed | — |
| CMD-CON-SUSPEND | ACTIVE, DEGRADED | reason; egress rule disabled | REASON_REQUIRED |
| CMD-CON-RESUME | SUSPENDED | egress rule re-enabled after re-check | — |
| CMD-CON-RETIRE | DRAFT, SUSPENDED | no ACTIVE adapter or stream bound; egress rule removed | CONNECTION_IN_USE |

**فصل المهام:** CMD-CON-ACTIVATE: Security Officer ≠ requester

#### AGG-MODEL-VERSION — إصدار النموذج

**الثوابت:**

- **INV-MDL-01** — only PRODUCTION versions serve production routes; STAGED serves canary share only
- **INV-MDL-02** — approval needs an evaluation report meeting thresholds; approver ≠ registrar (REQ-AI-010)
- **INV-MDL-03** — model records are never deleted; lineage always resolves the model version

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-MDL-REGISTER | ∅ | family, version, weights digest in internal registry, licence reviewed, languages (must include ar and en for generative roles), context size, hosting ∈ {local, external_allowed} | MODEL_INVALID |
| CMD-MDL-START-EVALUATION | REGISTERED | evaluation suite ACTIVE (AGG-EVAL-SUITE) | SUITE_NOT_ACTIVE |
| CMD-MDL-APPROVE | EVALUATING | report meets thresholds: citation accuracy ≥ 95 %, hallucination ≤ 2 %, insufficient-evidence recall ≥ 95 %, 0 injection/exfiltration successes, latency and cost recorded (REQ-AI-010); AI governance authority ≠ registrar | EVALUATION_BELOW_THRESHOLD |
| CMD-MDL-FAIL-EVALUATION | EVALUATING | report attached | — |
| CMD-MDL-STAGE | APPROVED | canary share ≤ 10 % of the target operations | — |
| CMD-MDL-PROMOTE | STAGED | canary metrics within thresholds for ≥ 7 days; approver ≠ stager | CANARY_BELOW_THRESHOLD |
| SYS:monitoring drift detected | PRODUCTION | weekly evaluation sample below threshold → alert, route review | — |
| CMD-MDL-DEPRECATE | PRODUCTION, STAGED, APPROVED | reason; routes using it must be switched first | MODEL_IN_ACTIVE_ROUTE |
| CMD-MDL-REINSTATE | DEPRECATED | rollback; evaluation ≤ 90 days old | EVALUATION_TOO_OLD |
| CMD-MDL-RETIRE | DEPRECATED | weights archived (cold) if referenced by lineage of accepted results; record kept | — |

**فصل المهام:** CMD-MDL-APPROVE: approver ≠ registrar؛ CMD-MDL-PROMOTE: approver ≠ stager

#### AGG-PRELOAD-PACKAGE — حزمة التحميل المسبق

**الثوابت:**

- **INV-PKG-01** — package content never exceeds the user's authorization at build time nor the tenant offline level (REQ-OFF-002)
- **INV-PKG-02** — packages expire; expired or revoked data becomes unreadable on the device (local key discarded)
- **INV-PKG-03** — any change of the user's security_version revokes all their packages

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-PKG-REQUEST | ∅ | device ACTIVE; area polygon ≤ tenant max area; layers; time window; requested level ≤ tenant offline max level (default INTERNAL, POL-OFFLINE-PRELOAD) | PRELOAD_NOT_ALLOWED |
| SYS:build started | REQUESTED | worker | — |
| SYS:build finished | BUILDING | content = objects visible to the user at build time and ≤ requested level; manifest with hashes, labels, security_version, expires_at (≤ 72 h R1) | — |
| CMD-PKG-CONFIRM-DOWNLOAD | READY | device acknowledges manifest hash | MANIFEST_MISMATCH |
| SYS:expires_at reached | READY, DOWNLOADED | device purges at expiry (local enforcement) and confirms on next contact | — |
| SYS:user security_version changed or device not ACTIVE | REQUESTED, BUILDING, READY, DOWNLOADED | purge instruction on next contact | — |
| CMD-PKG-REVOKE | REQUESTED, BUILDING, READY, DOWNLOADED | user, Administrator or Security Officer; reason | REASON_REQUIRED |

#### AGG-PROJECTION-VERSION — إصدار الإسقاط

**الثوابت:**

- **INV-PRJ-01** — a projection is never a source of truth; every document is reproducible from owner contexts (A07, FIT-11)
- **INV-PRJ-02** — exactly one ACTIVE version per (tenant group, kind) serves queries; promotion is atomic (alias switch)
- **INV-PRJ-03** — every document carries security labels (tenant, level, compartments, caveats, org_scope, security_version) — ADR-P06
- **INV-PRJ-04** — normalization, schema or embedding-model changes require a new version (no in-place re-analysis)

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-PRJ-CREATE-VERSION | ∅ | kind ∈ {search, graph, vector (R2, SLC-10)}; document schema version, embedding model version (vector), analyzer/normalization version and source checkpoint set; at most one BUILDING version per (tenant group, kind) | PROJECTION_BUILD_IN_PROGRESS |
| SYS:full rebuild reached live checkpoint | BUILDING | all source streams replayed to current checkpoint; verification sample equals source (FIT-11) | — |
| SYS:build failed | BUILDING | unrecoverable build error | — |
| CMD-PRJ-PROMOTE | READY | operator; verification passed; previous ACTIVE of same kind → RETIRED in the same step (alias switch) | PROJECTION_NOT_VERIFIED |
| SYS:lag above threshold | ACTIVE | lag > 5 min or error rate > 1 % for 5 min | — |
| SYS:lag back within target | DEGRADED | lag ≤ 30 s for 5 min | — |
| CMD-PRJ-RETIRE | READY, ACTIVE, DEGRADED | operator; not the only ACTIVE version of its kind | LAST_ACTIVE_PROJECTION |
| CMD-PRJ-CANCEL-BUILD | BUILDING | operator; reason | REASON_REQUIRED |

#### AGG-SENSOR-STREAM — تدفق الحسّاس

**الثوابت:**

- **INV-SNS-01** — sensor readings enter only as observations through BC02 batch commands (≤ 1,000 per batch, per-item idempotency) — REQ-INT-002
- **INV-SNS-02** — quality violations annotate data quality; they never silently drop readings
- **INV-SNS-03** — readings carry the sensor's own time as observed_at and server receipt as recorded_from

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-SNS-REGISTER | ∅ | connection (sensor_gateway) exists; BC02 Source of type sensor ACTIVE; quantity + UCUM unit; expected rate; location or linked entity | STREAM_INVALID |
| CMD-SNS-SET-QUALITY-RULES | DRAFT, ACTIVE, PAUSED | range, rate-of-change, stale-after, duplicate window; violations become data_quality issues, not rejections | QUALITY_RULES_INVALID |
| CMD-SNS-ACTIVATE | DRAFT, PAUSED | connection ACTIVE; mapping to CMD-OBS-RECORD batches tested | CONNECTION_NOT_ACTIVE |
| CMD-SNS-PAUSE | ACTIVE | reason | REASON_REQUIRED |
| SYS:no data beyond stale-after | ACTIVE | stream flagged STALE; alert to owner | — |
| CMD-SNS-RETIRE | DRAFT, PAUSED | reason | REASON_REQUIRED |

#### AGG-SYNC-CONFLICT — تعارض المزامنة

**الثوابت:**

- **INV-SCF-01** — the original field command and device time are preserved as evidence of what the field user did
- **INV-SCF-02** — reapplying never bypasses the owner's state machine, guards or policies
- **INV-SCF-03** — commands recorded after a device's reported-lost time always open a conflict (never auto-applied)

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| SYS:stale state-changing command | ∅ | rule CF-05: base_version ≠ current; stores original envelope, current state snapshot and owner rejection reason; reviewer = owner-context default (task: owner/Planner; observation: Analyst) | — |
| CMD-SCF-ASSIGN | OPEN | assignee authorized on the target | REVIEWER_NOT_AUTHORIZED |
| CMD-SCF-REAPPLY | OPEN | reviewer re-sends the original intent against the current version; owner-context accepts (its guards still apply) | OWNER_REJECTED |
| CMD-SCF-DISCARD | OPEN | reason; field user notified | REASON_REQUIRED |
| CMD-SCF-RESOLVE-MANUALLY | OPEN | note + reference to the alternative action taken | REASON_REQUIRED |

#### AGG-SYNC-SESSION — جلسة المزامنة

**الثوابت:**

- **INV-SYN-01** — commands are applied in device seq order; client_command_id makes re-delivery idempotent (REQ-OFF-006)
- **INV-SYN-02** — record time = server receipt; device time stored and corrected by the measured clock offset (REQ-OFF-003)
- **INV-SYN-03** — the gateway applies commands through owner-context APIs with the user's delegated SecurityContext — never bypassing owner guards or policies
- **INV-SYN-04** — no last-write-wins for T1/T2: a state-changing command whose base_version ≠ current becomes a sync conflict (REQ-OFF-004)

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-SYN-OPEN | ∅ | device ACTIVE; user authenticated (fresh token); device signature on handshake; clock offset measured (server − device); resumes after last acknowledged seq | DEVICE_NOT_ACTIVE |
| SYS:device LOST or SUSPENDED at handshake | ∅ | returns wipe (LOST) or stop (SUSPENDED) instruction only | — |
| CMD-SYN-UPLOAD-BATCH | OPEN, APPLYING | ≤ 200 commands; contiguous seq after last acknowledged; each envelope signed by device key; batch hash chain continues | SEQUENCE_GAP |
| SYS:all uploaded commands processed without conflict | APPLYING | device declared end of queue; every command applied or idempotently recognized | — |
| SYS:all processed with ≥ 1 sync conflict | APPLYING | conflicts opened as AGG-SYNC-CONFLICT | — |
| SYS:idle timeout (5 min) or transport loss | OPEN, APPLYING | acknowledged seq retained; next session resumes (REQ-OFF-006) | — |

### BC08 — Governance — الحوكمة والأمن

#### AGG-CLASSIFICATION-SCHEME — مخطط التصنيف

**الثوابت:**

- **INV-CLS-01** — exactly one ACTIVE scheme version per tenant
- **INV-CLS-02** — level ranks strictly ordered and unique; codes immutable
- **INV-CLS-03** — levels, compartments and caveats can be deprecated, never removed
- **INV-CLS-04** — activation increments the security_version of all subjects in the tenant

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-CLS-DRAFT | ∅ | Security Officer; at most one DRAFT per tenant | DRAFT_EXISTS |
| CMD-CLS-EDIT | DRAFT | codes immutable once used; ranks strictly ordered; removal not allowed, only deprecation | SCHEME_INVALID |
| CMD-CLS-ACTIVATE | DRAFT | validation passes; effective_from ≥ now; approver ≠ drafter; previous ACTIVE → SUPERSEDED in same transaction | SCHEME_INVALID |
| SYS:successor activated | ACTIVE | system | — |

**فصل المهام:** CMD-CLS-ACTIVATE: approver ≠ drafter

#### AGG-DISPOSITION-RUN — تشغيل الإتلاف

**الثوابت:**

- **INV-DSP-01** — destruction is by key (crypto-shredding of time-bucketed class keys), reaching operational stores, projections, archives and backups (ADR-P08, CR-51)
- **INV-DSP-02** — no bucket key is destroyed while any record in it is under hold — held records are re-wrapped first
- **INV-DSP-03** — each destruction is recorded in the append-only key-destruction log used by the restore gate
- **INV-DSP-04** — tombstones keep non-personal facts (class, bucket, count, run, date); audit records are governed by their own class rule

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| SYS:scheduled evaluation (daily) | ∅ | candidates = key buckets whose records are all past retention under the ACTIVE schedule; held items identified via HoldCheck | — |
| CMD-DSP-SUBMIT | PLANNED | Archivist reviewed candidate summary (counts per class/bucket, REVIEW-action items listed) | — |
| CMD-DSP-APPROVE | AWAITING_APPROVAL | approver = Records/Legal authority ≠ submitter; re-run HoldCheck at approval | SEGREGATION_OF_DUTIES |
| SYS:execution started | APPROVED | held items in each bucket re-wrapped under hold keys first; then bucket keys destroyed; owners notified to purge plaintext caches and projections; tombstones written | — |
| SYS:all buckets processed | EXECUTING | certificate issued (buckets, key ids destroyed, counts, holds excluded) | — |
| SYS:some buckets failed | EXECUTING | failed buckets listed; retried next run | — |
| CMD-DSP-CANCEL | PLANNED, AWAITING_APPROVAL, APPROVED | reason | REASON_REQUIRED |

**فصل المهام:** CMD-DSP-APPROVE: approver ≠ submitter

#### AGG-ERASURE-REQUEST — طلب المحو

**الثوابت:**

- **INV-ERS-01** — execution destroys keys, not rows; data becomes unreadable everywhere including backups via the restore gate (CR-51)
- **INV-ERS-02** — blocked while any hold covers the subject
- **INV-ERS-03** — audit facts remain with a pseudonymous subject reference
- **INV-ERS-04** — approval and registration by different persons

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-ERS-REGISTER | ∅ | legal basis reference; subject identification (platform person URN and/or information entity URNs of type person); requester | ERASURE_INVALID |
| SYS:subject scope resolved | RECEIVED | subject keys located in BC01 (persons), BC02 (entities with personal_data claims) and BC05 (qualification records of that person, CR-69); affected record counts per context | — |
| CMD-ERS-APPROVE | SCOPED | Legal/Compliance authority ≠ registrar; decision recorded with basis | SEGREGATION_OF_DUTIES |
| CMD-ERS-REJECT | SCOPED | reason (e.g. legal obligation to retain) | REASON_REQUIRED |
| SYS:hold matches subject | APPROVED | HoldCheck positive | — |
| SYS:hold released | BLOCKED_BY_HOLD | HoldCheck negative | — |
| SYS:execution started | APPROVED | subject DEKs destroyed; owners purge plaintext caches/projections; pseudonymous reference kept for audit facts | — |
| SYS:all contexts confirmed | EXECUTING | confirmation from each owning context ≤ 24 h (QAS-PRV-001); certificate issued | — |

**فصل المهام:** CMD-ERS-APPROVE: approver ≠ registrar

#### AGG-LEGAL-HOLD — التجميد القانوني

**الثوابت:**

- **INV-LHD-01** — while ACTIVE or RELEASE_REQUESTED, no matching record can be disposed, erased or have its key destroyed (REQ-GOV-007)
- **INV-LHD-02** — holds never block versioned changes (history is preserved); they block destructive actions only
- **INV-LHD-03** — scope can only grow while ACTIVE; narrowing = release + new hold
- **INV-LHD-04** — release needs two distinct Legal authorities

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-LHD-PLACE | ∅ | Legal/Compliance authority; scope = any of: record classes, object URNs, data subjects, org units, time range; legal reference | HOLD_INVALID |
| CMD-LHD-EXTEND | ACTIVE | added scope items; reason | HOLD_INVALID |
| CMD-LHD-REQUEST-RELEASE | ACTIVE | reason; requester = Legal authority | REASON_REQUIRED |
| CMD-LHD-APPROVE-RELEASE | RELEASE_REQUESTED | second Legal authority ≠ requester | SEGREGATION_OF_DUTIES |
| CMD-LHD-CANCEL-RELEASE | RELEASE_REQUESTED | reason | REASON_REQUIRED |

**فصل المهام:** CMD-LHD-APPROVE-RELEASE: approver ≠ requester

#### AGG-POLICY-SET — مجموعة السياسات

**الثوابت:**

- **INV-POL-01** — exactly one ACTIVE policy set version per tenant; platform baseline always applies on top
- **INV-POL-02** — tenant policies can only restrict the platform baseline, except parameters explicitly marked configurable (e.g. SoD toggle)
- **INV-POL-03** — a version cannot be approved by its author
- **INV-POL-04** — every version carries decision-table tests that must pass before review

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-POL-DRAFT | ∅ | Security Officer | — |
| CMD-POL-EDIT | DRAFT | tables validate against schema | POLICY_INVALID |
| CMD-POL-SUBMIT | DRAFT | embedded policy tests all pass; tenant rules only restrict platform baseline | POLICY_TESTS_FAILED |
| CMD-POL-APPROVE | IN_REVIEW | approver ≠ author; Security Officer | SEGREGATION_OF_DUTIES |
| CMD-POL-REJECT | IN_REVIEW | reason | REASON_REQUIRED |
| SYS:effective_from reached | APPROVED | scheduler; previous ACTIVE → SUPERSEDED | — |
| SYS:successor activated | ACTIVE | system | — |

**فصل المهام:** CMD-POL-APPROVE: approver ≠ author

#### AGG-RETENTION-SCHEDULE — جدول الاحتفاظ

**الثوابت:**

- **INV-RTS-01** — exactly one ACTIVE schedule version per tenant; every record class covered
- **INV-RTS-02** — shortening a period applies only to records whose trigger occurs after activation unless the approver explicitly marks it retroactive (legal decision recorded)
- **INV-RTS-03** — schedule versions are immutable once ACTIVE

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-RTS-DRAFT | ∅ | Archivist; ≤ 1 DRAFT per tenant | DRAFT_EXISTS |
| CMD-RTS-EDIT | DRAFT | each rule: record class (RD-RECORD-CLASSES), period (ISO 8601 duration), trigger ∈ {recorded, closed, superseded, event}, action ∈ {DESTROY, REVIEW, ARCHIVE (R2)}, legal basis | SCHEDULE_INVALID |
| CMD-RTS-ACTIVATE | DRAFT | every record class in RD-RECORD-CLASSES has exactly one rule (REQ-GOV-006); approver = Legal/Compliance authority ≠ drafter; previous ACTIVE → SUPERSEDED in the same transaction | SCHEDULE_INCOMPLETE |
| CMD-RTS-DISCARD | DRAFT | reason | REASON_REQUIRED |
| SYS:successor activated | ACTIVE | system | — |

**فصل المهام:** CMD-RTS-ACTIVATE: approver ≠ drafter

**بيانات مرجعية مستخدمة:** RD-RECORD-CLASSES (`04-information/reference-data.md`)

#### AGG-SECURITY-EXCEPTION — الاستثناء الأمني

**الثوابت:**

- **INV-EXC-01** — activation requires two distinct approvers, both different from the requester (REQ-FND-017)
- **INV-EXC-02** — exceptions never apply to platform baseline rules (tenant isolation, classification rule, audit, fail-closed)
- **INV-EXC-03** — maximum duration 30 days; renewal = new request (W4 delegated decision)

**شروط الانتقال (قواعد التحقق):**

| الأمر / المحفِّز | من | الشرط | خطأ الفشل |
|---|---|---|---|
| CMD-EXC-REQUEST | ∅ | targets a tenant policy rule (not platform baseline); duration ≤ 30 days; justification | EXCEPTION_NOT_ALLOWED |
| CMD-EXC-APPROVE | REQUESTED | approver authorized; approver ≠ requester | SEGREGATION_OF_DUTIES |
| CMD-EXC-APPROVE | FIRST_APPROVED | approver authorized; approver ∉ {requester, first approver} | SEGREGATION_OF_DUTIES |
| CMD-EXC-REJECT | REQUESTED, FIRST_APPROVED | reason | REASON_REQUIRED |
| CMD-EXC-REVOKE | ACTIVE | Security Officer; reason | REASON_REQUIRED |
| SYS:end reached | ACTIVE | scheduler | — |

**فصل المهام:** CMD-EXC-APPROVE: approver ∉ {requester, first approver}

<!-- END GENERATED: build_analysis_design.py -->
