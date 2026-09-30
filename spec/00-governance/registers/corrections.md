---
id: REG-CR
type: register
title: Baseline Corrections Register
wave: W0
tier: T3
owner_role: Orchestrator
status: DRAFT
approved_by: null
approved_at: null
consumers: []
---

# Baseline Corrections Register

## corrections

_74 items_ (CR-66..CR-72 added in Phase 3.7; CR-73..CR-74 in Phase 3.8 — 18-analysis-design)

### CR-01

- **issue:** Geometry له مالكان في PRJ§9
- **correction:** المالك BC02 وحده
- **target_wave:** W3
- **origin:** V6§14
- **status:** APPLIED (W3): ownership + spatial-model

### CR-02

- **issue:** كائنات بلا مالك
- **correction:** إكمال ownership.md
- **target_wave:** W3
- **origin:** V6§14
- **status:** APPLIED (W3): ownership (0 unowned)

### CR-03

- **issue:** Envelope يحمل score واحداً
- **correction:** ثقة بسبعة أبعاد
- **target_wave:** W3
- **origin:** V6§14
- **status:** APPLIED (W3): object-envelope + confidence-model

### CR-04

- **issue:** Envelope ينقصه Event/Effective Time وRecord Time لحظة
- **correction:** ADR-P01
- **target_wave:** W3
- **origin:** V6§14
- **status:** APPLIED (W3): object-envelope + temporal-model

### CR-05

- **issue:** Situation: View أم Aggregate
- **correction:** ADR-P07
- **target_wave:** W3
- **origin:** V6§14
- **status:** APPLIED (W3): ADR-P07

### CR-06

- **issue:** حالات Task تخلط الحالات بالانتقالات
- **correction:** جدول V6§13.5
- **target_wave:** W4
- **origin:** V6§14
- **status:** APPLIED (SLC-03): AGG-TASK state machine, SPEC-TASK-RULES

### CR-07

- **issue:** البادئة BR لنوعين
- **correction:** BRL / BRQ
- **target_wave:** W0
- **origin:** V6§14
- **status:** APPLIED_IN_SPEC (pending approval)

### CR-08

- **issue:** PRJ§47 يخلط الطبقات بسلسلة القيمة
- **correction:** C4 منفصل عن Value Stream
- **target_wave:** W8
- **origin:** V6§14
- **status:** APPLIED (W8): C4 views separate from value streams

### CR-09

- **issue:** Use Cases ناقصة لـ VS04/VS05 ومجالات أخرى
- **correction:** إكمال للنطاق
- **target_wave:** W2
- **origin:** V6§14
- **status:** APPLIED (W2) for R1; R2/R3 gaps scheduled

### CR-10

- **issue:** 'مهم' غير معرّف
- **correction:** ADR-P03
- **target_wave:** W3
- **origin:** V6§14
- **status:** APPLIED (W3): ADR-P03 + importance-tiers

### CR-11

- **issue:** لا مخزن متجهات
- **correction:** Vector Projection مؤمّنة
- **target_wave:** W3
- **origin:** V6§14
- **status:** APPLIED (W3): ADR-P06 (vector projection labels)

### CR-12

- **issue:** الجانب الجغرافي بلا خرائط/Tiles/OGC/مسارات
- **correction:** ADR-P12
- **target_wave:** W3
- **origin:** V6§14
- **status:** APPLIED (W3): ADR-P12 + spatial-model

### CR-13

- **issue:** Offline بلا تصميم
- **correction:** ADR-P09
- **target_wave:** W3
- **origin:** V6§14
- **status:** APPLIED (W3): ADR-P09

### CR-14

- **issue:** عزل المستأجرين غير محدد
- **correction:** ADR-P04
- **target_wave:** W3
- **origin:** V6§14
- **status:** APPLIED (W3): ADR-P04

### CR-15

- **issue:** لا Split/Unmerge
- **correction:** إضافة العملية
- **target_wave:** W3
- **origin:** V6§14
- **status:** APPLIED (W3): entity-resolution (split = close link)

### CR-16

- **issue:** history/events/outbox دون مرجع
- **correction:** ADR-P02
- **target_wave:** W3
- **origin:** V6§14
- **status:** APPLIED (W3): ADR-P02

### CR-17

- **issue:** أمن بلا تصنيف/Compartments/Threat Model/مفاتيح
- **correction:** Security Kernel
- **target_wave:** W3
- **origin:** V6§14
- **status:** APPLIED (W3): 08-security kernel

### CR-18

- **issue:** لا معالجة للعربية
- **correction:** ADR-P15
- **target_wave:** W3
- **origin:** V6§14
- **status:** APPLIED (W3): ADR-P15 + language-model

### CR-19

- **issue:** لا بيانات مرجعية
- **correction:** ADR-P14
- **target_wave:** W3
- **origin:** V6§14
- **status:** APPLIED (W3): ADR-P14 + reference-data

### CR-20

- **issue:** استقلالية AI غير مربوطة بعمليات
- **correction:** Autonomy Matrix
- **target_wave:** W3
- **origin:** V6§14
- **status:** APPLIED (W3): autonomy-matrix

### CR-21

- **issue:** تقنيات قبل أعباء العمل
- **correction:** ADR-P05
- **target_wave:** W8
- **origin:** V6§14
- **status:** APPLIED (W8): ADR-P05 + TECH-DECISIONS

### CR-22

- **issue:** ✓ دون أدلة في PRJ§123
- **correction:** تقارير بوابات
- **target_wave:** W0
- **origin:** V6§14
- **status:** APPLIED_IN_SPEC (gate report W0)

### CR-23

- **issue:** شريحة تنفيذ واسعة
- **correction:** شرائح رفيعة
- **target_wave:** W1
- **origin:** V6§14
- **status:** APPLIED (release/slice plan W1)

### CR-24

- **issue:** لا Jurisdiction في الصلاحيات
- **correction:** إضافته
- **target_wave:** W3
- **origin:** V6§14
- **status:** APPLIED as REQ-FND-011 (W2)

### CR-25

- **issue:** إعادة البناء بلا Unknown وبلا As-Of
- **correction:** إضافتهما
- **target_wave:** W3
- **origin:** V6§14
- **status:** APPLIED (W3): temporal-model §8

### CR-26

- **issue:** P00–P02 غير موثقة
- **correction:** W1
- **target_wave:** W1
- **origin:** V6§14
- **status:** APPLIED (W1)

### CR-27

- **issue:** updated يوحي بالكتابة فوق القيم
- **correction:** إصدار لكل تحديث T1/T2
- **target_wave:** W3
- **origin:** V6§14
- **status:** APPLIED (W3): object-envelope

### CR-28

- **issue:** V5 مبتور
- **correction:** مستكمل في V6§24
- **target_wave:** W0
- **origin:** V6§14
- **status:** APPLIED_IN_SPEC (pending approval)

### CR-29

- **issue:** AnalysisCase وPlan مرشحان لـ God Aggregate
- **correction:** اختبار الحدود
- **target_wave:** W4
- **origin:** V6§14
- **status:** APPLIED: AnalysisCase (SLC-07, 5 aggregates) and Plan (SLC-08, identity + versions)

### CR-30

- **issue:** O1–O6 غير مربوطة بالمتطلبات
- **correction:** OUT ← BRQ
- **target_wave:** W2
- **origin:** V6§14
- **status:** APPLIED (W2) OUT ← BRQ

### CR-31

- **issue:** Evidence معرّف في مجالين: DOM-03 (PRJ§7.3) وDOM-06 (PRJ§7.6)
- **correction:** مجال مالك واحد لـ Evidence؛ الآخر يستخدمه بالمرجع
- **target_wave:** W3
- **origin:** W0 load (new)
- **status:** APPLIED (W3): claim-evidence-model §3

### CR-32

- **issue:** Authority معرّف في DOM-01 (BC01) وDOM-10 (BC04) — سياقان مختلفان
- **correction:** مالك واحد (مرشح: BC01)، وBC04 يستهلكه عبر عقد؛ BRL-003 يعتمد عليه
- **target_wave:** W3
- **origin:** W0 load (new)
- **status:** APPLIED (W3): ownership + context-map

### CR-33

- **issue:** كلمة Policy تعني ثلاثة مفاهيم: Access Policy (DOM-02)، Policy (DOM-25)، Policy Knowledge (DOM-21)، إضافة لـ Policy في V5 Event Storming
- **correction:** تمييزها في glossary.md بأسماء مختلفة
- **target_wave:** W0/W3
- **origin:** W0 load (new)
- **status:** APPLIED (W3): glossary + authorization-model

### CR-34

- **issue:** كلمة Requirement تعني: Collection Requirement (DOM-05)، Task Requirement (DOM-13)، ومتطلبات النظام
- **correction:** CollectionRequirement / TaskRequirement / REQ
- **target_wave:** W0/W3
- **origin:** W0 load (new)
- **status:** APPLIED (W3): glossary

### CR-35

- **issue:** Assignment تعني إسناد مهمة (DOM-13, UC-041) وإسناد أصل (UC-053, PRJ§88-G)
- **correction:** TaskAssignment / AssetAssignment ككائنين منفصلين
- **target_wave:** W3
- **origin:** W0 load (new)
- **status:** APPLIED (W3): glossary

### CR-36

- **issue:** Assessment تعني التقييم التحليلي (DOM-08) وتقييم الكفاءة/التعلم (BP40, BP44, VS05)
- **correction:** AnalyticalAssessment / CompetencyAssessment
- **target_wave:** W0/W3
- **origin:** W0 load (new)
- **status:** APPLIED (W3): glossary

### CR-37

- **issue:** Outcome تعني نتائج العمل O1–O6 (PRJ§37) وكائن تخطيط في DOM-12
- **correction:** OUT (Business Outcome) / PlanOutcome
- **target_wave:** W0
- **origin:** W0 load (new)
- **status:** APPLIED (W3): glossary + BO-PLAN-OUTCOME

### CR-38

- **issue:** Decision تعني قرار العمل (DOM-10) وقرار مطابقة الكيانات (PRJ§13) وقرار السياسة ALLOW/DENY (PRJ§66)
- **correction:** BusinessDecision / MatchDecision / PolicyDecision
- **target_wave:** W0
- **origin:** W0 load (new)
- **status:** APPLIED (W3): glossary

### CR-39

- **issue:** صلاحية 'Delete / Retain / Archive' مدمجة كصلاحية واحدة (PRJ§4)
- **correction:** ثلاث صلاحيات منفصلة، والحذف مرتبط بـ ADR-P08
- **target_wave:** W3
- **origin:** W0 load (new)
- **status:** APPLIED as REQ-FND-014 (W2)

### CR-40

- **issue:** معيار المسار /api/v1/{domain}/{resource} (PRJ§18) يخالفه كل مثال: /api/v1/tasks/{id}/actions/complete بلا مقطع domain
- **correction:** اعتماد صيغة واحدة وتطبيقها على كل العقود
- **target_wave:** W3
- **origin:** W0 load (new)
- **status:** APPLIED (W3): decided: /api/v1/{context}/{resource}; applied in W6 contracts

### CR-41

- **issue:** Tenant وWorkspace مستخدمان (PRJ§6، §88-A) لكن لا يظهران في أي مجال من الـ 26
- **correction:** إسنادهما لـ DOM-01 أو DOM-02 مع مالك
- **target_wave:** W3
- **origin:** W0 load (new)
- **status:** APPLIED (W3): domains DOM-01

### CR-42

- **issue:** Risk & Emergency (DOM-17) مصنف تحت مجموعة 'Risk, Training & Knowledge' لكنه في BC04 Operations؛ التجميع لا يطابق السياق
- **correction:** توحيد التجميع مع الـ Bounded Context أو توثيق سبب الاختلاف
- **target_wave:** W3
- **origin:** W0 load (new)
- **status:** APPLIED (W3): domains + bc-boundary-test

### CR-43

- **issue:** Evaluation في DOM-19 وAI Evaluation في DOM-23 وCompetency Assessment — ثلاثة مفاهيم تقييم إضافية
- **correction:** تمييزها في القاموس
- **target_wave:** W0
- **origin:** W0 load (new)
- **status:** APPLIED (W3): glossary

### CR-44

- **issue:** 'Event' في Information Fabric (حدث واقعي) يختلط بـ Domain Event (سجل نظامي)
- **correction:** RealWorldEvent للأول؛ Domain/Integration Event للثاني
- **target_wave:** W3
- **origin:** W3
- **status:** APPLIED (W3): meta-model §4

### CR-45

- **issue:** W3 audit design: same-transaction write into BC08 store violates FIT-01; single per-tenant sequence is a throughput bottleneck
- **correction:** audit_outbox per context + sharded hash chains + Merkle anchors
- **target_wave:** W4 (SLC-01)
- **origin:** SLC-01
- **status:** APPLIED: 08-security/audit-architecture.md

### CR-46

- **issue:** V6§13.5 example modelled SUSPENDED as a state returning to 'prior_state' (not expressible as a fixed transition table)
- **correction:** suspension as orthogonal flag (INV-TASK-06); V6 example superseded by AGG-TASK
- **target_wave:** W4 (SLC-03)
- **origin:** SLC-03
- **status:** APPLIED: AGG-TASK, SPEC-TASK-RULES

### CR-47

- **issue:** ADR-P06 §3 re-check used a central security-version table for objects; keeping it current requires cross-context writes
- **correction:** objects: LabelCheck OHS implemented by each owning context (batched per page); subjects: BC01 security-version KV (unchanged)
- **target_wave:** W4 (SLC-05)
- **origin:** SLC-05
- **status:** APPLIED: SPEC-DISCOVERY §4.1, ADR-P06 amendment

### CR-48

- **issue:** contracts generator did not support 'number' payload fields (found by OpenAPI validator in SLC-08)
- **correction:** generator supports number; earlier slices checked — none affected
- **target_wave:** W6 (SLC-08)
- **origin:** SLC-08
- **status:** APPLIED

### CR-49

- **issue:** CONFLICT-MODEL listed CF-05 (sync) as a BC02 claim conflict; stale state-changing commands are not claim disagreements
- **correction:** CF-05 represented by AGG-SYNC-CONFLICT (BC07); claims from synced observations still use CF-01..04
- **target_wave:** W4 (SLC-11)
- **origin:** SLC-11
- **status:** APPLIED: conflict-model, SPEC-FIELD-SYNC §5

### CR-50

- **issue:** offline-created objects need identities before reaching the server
- **correction:** creation commands accept client-generated ULID (client_id) — SLC-02 regenerated
- **target_wave:** W6 (SLC-11)
- **origin:** SLC-11
- **status:** APPLIED: slc02 contracts

### CR-51

- **issue:** ADR-P08 claimed backups become unrecoverable 'immediately' via key destruction, but key-store backups could revive destroyed keys
- **correction:** append-only key-destruction log + restore gate + key-store backup retention ≤ 35 d; class-bucket keys for disposition
- **target_wave:** W4 (SLC-12a)
- **origin:** SLC-12a
- **status:** APPLIED: SPEC-KEYS-DISPOSITION, ADR-P08 amendment, FIT-19

### CR-52

- **issue:** REQ-GOV-002 required a classification on every T1/T2 object, but 12 creation commands (links, configuration, derived objects) carry none
- **correction:** label source defined for every aggregate: explicit, derived by rule, or administrative default (LABEL-DERIVATION, SL-29)
- **target_wave:** W7 (consolidation)
- **origin:** global coverage check
- **status:** APPLIED

### CR-53

- **issue:** global coverage check: 15 R1 requirements not traced by any domain slice (platform & cross-cutting)
- **correction:** 8 traced via fitness functions and contract lint; 7 assigned to W8/W9 explicitly (TRACE-PLATFORM)
- **target_wave:** W8/W9
- **origin:** global coverage check
- **status:** APPLIED (W8): all 15 platform requirements traced (TRACE-PLATFORM)

### CR-54

- **issue:** search indexes treated as rebuildable-only, but full rebuild (≤ 24 h) exceeds the important-tier RTO (4 h)
- **correction:** OpenSearch snapshots every 15 min to object storage, restored in DR, then catch-up from Kafka
- **target_wave:** W8
- **origin:** W8 DR design
- **status:** APPLIED: DR-CONTINUITY §3

### CR-55

- **issue:** W9 consistency check: CMD-RUN-SUBMIT missing from OpenAPI — two creation commands mapped to the same path and the generator silently overwrote one
- **correction:** CMD-RUN-REPRODUCE moved to /analysis-runs/{id}/actions/reproduce; generator now fails on any path collision; all slices re-scanned (no other collision)
- **target_wave:** W9
- **origin:** W9 consistency check
- **status:** APPLIED

### CR-56

- **issue:** W9 consistency check: 19 of 74 quality scenarios had no explicit verification reference
- **correction:** Quality Verification Matrix maps every QAS to method and timing
- **target_wave:** W9
- **origin:** W9 consistency check
- **status:** APPLIED

### CR-57

- **issue:** reproducibility: contracts of early slices had been produced by older generator versions (missing x-offline-capable), and schema enrichments of 6 slices were applied by ad-hoc post-processing — regeneration would have lost them
- **correction:** all enrichments moved into slice source data (enrich hooks); every slice regenerated; full round-trip from Markdown-embedded tooling reproduces the package with 0 differing files
- **target_wave:** W9
- **origin:** W9 round-trip test
- **status:** APPLIED

### CR-58

- **issue:** AI retrieval needs a vector projection but projection versions only allowed search and graph
- **correction:** AGG-PROJECTION-VERSION kind extended with vector (embedding model version part of the projection version); SLC-05 regenerated
- **target_wave:** SLC-10
- **origin:** SLC-10
- **status:** APPLIED

### CR-59

- **issue:** task plan_ref assumed an operations plan only; collection plans also generate field tasks
- **correction:** plan_ref accepts an operations plan or a collection plan; SLC-03 source updated and regenerated
- **target_wave:** SLC-14
- **origin:** SLC-14
- **status:** APPLIED

### CR-60

- **issue:** SLC-17's continuity/contingency plans need a Plan (SLC-08) whose creation is triggered by a risk or incident, not by a decision or objective (R3-Q2 reuse decision), and Plan identity carried no notion of kind or trigger
- **correction:** AGG-PLAN gains plan_kind ∈ {OPERATIONS, CONTINGENCY} (INV-PLN-04) and an optional triggered_by reference; CMD-PLN-CREATE's guard accepts a risk_ref/incident_ref trigger for plan_kind=CONTINGENCY as an alternative to implementing a decision or objective; SLC-08 source updated and regenerated
- **target_wave:** SLC-17
- **origin:** SLC-17
- **status:** APPLIED

### CR-61

- **issue:** SLC-17's incident response tasks need to be created directly under an Incident without a plan, but AGG-TASK's creation guard only accepted a plan_ref or an ad_hoc_reason (CR-59)
- **correction:** CMD-TASK-CREATE gains an incident_ref alternative to plan_ref (direct response task under an Incident); SLC-03 source updated and regenerated
- **target_wave:** SLC-17
- **origin:** SLC-17
- **status:** APPLIED

### CR-62

- **issue:** SLC-18's logistics requests need to commit inventory quantity through SLC-09's existing Allocation (R3-Q3 reuse decision) rather than a second capacity-reservation engine, but AGG-ALLOCATION's creation guard described `target` as task/activity only (the payload field `target!:urn` itself was already generic)
- **correction:** CMD-ALC-REQUEST's guard text is broadened to accept a logistics-request reference as a third alternative to task/activity; no payload schema change (the URN was already untyped); SLC-09 source updated and regenerated — round-trip confirmed only the guard-text lines changed in AGG-ALLOCATION.md and commands-slc09.md, with OpenAPI/AsyncAPI/errors/acceptance byte-identical to the prior baseline
- **target_wave:** SLC-18
- **origin:** SLC-18
- **status:** APPLIED

### CR-63

- **issue:** SLC-19's After Action Review needs a completed exercise simulation to be a valid terminal source for a lesson-type Knowledge Object (R3-Q5 reuse decision), but AGG-KNOWLEDGE-OBJECT's CMD-KNO-DRAFT guard restricted lesson terminal sources to task, plan or incident only (REQ-KNW-002); the payload field itself (`source:urn`) was already generic
- **correction:** CMD-KNO-DRAFT's guard text is broadened to accept a completed exercise simulation as a fourth alternative terminal source for lessons, alongside task/plan/incident; REQ-KNW-002's statement and acceptance criteria are broadened to match; no payload schema change (the URN was already untyped); SLC-12 source updated and regenerated — round-trip confirmed only the guard-text line in AGG-KNOWLEDGE-OBJECT.md and the matching guard line in commands-slc12.md changed, with OpenAPI/AsyncAPI/errors/acceptance byte-identical to the prior baseline
- **target_wave:** SLC-19
- **origin:** SLC-19
- **status:** APPLIED

### CR-64

- **issue:** REQ-GOV-004's `use_cases` field pointed only to UC-085 (Manage Classification Scheme & Compartments, BC08, satisfies REQ-GOV-001/REQ-GOV-009 per AGG-CLASSIFICATION-SCHEME.md — REQ-GOV-004 is absent from that aggregate's own `traces.satisfies`), while the aggregate that actually declares `satisfies: REQ-GOV-004` is AGG-CLEARANCE (BC01), which had no Use Case at all; REQ-GOV-003 (also satisfied by AGG-CLEARANCE) likewise had `use_cases: —`. Net effect: no Use Case covered granting/modifying/suspending/revoking a user's clearance (CMD-CLR-GRANT/APPROVE/MODIFY/SUSPEND/REINSTATE/REVOKE), even though the commands, policies, events and acceptance tests for that lifecycle are fully specified
- **correction:** added UC-089 — Manage User Clearance (BC01, CAP-13.01, actor Security Officer, covers AGG-CLEARANCE's full command set) to use-cases.md (numbering: next free slot in the reserved cross-cutting 080–089 range per OQ-001); linked REQ-GOV-003.use_cases → UC-089 and REQ-GOV-004.use_cases → UC-085, UC-089 (both requirements.md prose and YAML blocks) since REQ-GOV-004's acceptance criterion ("after a downgrade of a user's access...") is the clearance-side (BC01) path, distinct from UC-085's object/scheme-side path (BC08)
- **residual_note:** AGG-CLASSIFICATION-SCHEME.md's own `traces.satisfies` (BC08) still does not list REQ-GOV-004, even though UC-085 is now documented as contributing to it via its scheme-activation security-version bump (INV-CLS-04). Left unchanged pending human review — flagged here rather than edited silently, since it touches a different bounded context's approved aggregate file
- **target_wave:** W7 (post-hoc, discovered during BC01 feature deep-dive, not a slice-generation artifact)
- **origin:** Dynamic Discovery reverse-check on AGG-AUTHORITY-GRANT/AGG-CLEARANCE (Reverse Discovery pass against trace-slc01.md)
- **status:** APPLIED (confirmed 2026-09-30 under owner-delegated authority; master-study §20.3 item 3)

### CR-65

- **issue:** CR-64's residual_note flagged that AGG-CLASSIFICATION-SCHEME.md (BC08) did not list REQ-GOV-004 in its own `traces.satisfies`, even though requirements.md already documented UC-085 (Manage Classification Scheme & Compartments) as REQ-GOV-004's scheme/object-side use case. Confirmed during BC08 study: `INV-CLS-04` ("activation increments the security_version of all subjects in the tenant") is exactly the scheme-level enforcement of REQ-GOV-004's "stop returning the object to newly unauthorized subjects from the moment of the change in all access paths" — a third enforcement point alongside the CMD-*-RECLASSIFY pattern (per-object, BC02 and others) and AGG-CLEARANCE (per-user, BC01, CR-64)
- **correction:** added REQ-GOV-004 to AGG-CLASSIFICATION-SCHEME.md's `traces.satisfies` (prose front-matter and machine-readable YAML block), with an inline note explaining the INV-CLS-04 linkage; no change needed to requirements.md (REQ-GOV-004.use_cases already lists UC-085 for this side per CR-64) or to any commands/events/queries file — this is a traceability-declaration fix only, not a behavior change
- **target_wave:** W7 (post-hoc, discovered during BC08 feature deep-dive, closing the CR-64 residual_note)
- **origin:** Dynamic Discovery Phase 3 — BC08 study, closing CONFLICT-01/OQ-034's last open thread
- **status:** APPLIED

### CR-66

- **issue:** requirements.md `system_requirements` header stated `_181 items_` while the section (and its YAML block) holds 210 requirements (R1 114, R2 51, R3 45); the R3 requirements added in W1/W2-R3 on 2026-09-27 were never counted. The study's 04-cross-cutting §6.2 had built a false '21 intentional overlaps' explanation on the stale figure.
- **correction:** header set to 210 with a pointer to this CR; the actual overlap between bounded contexts (from traces.satisfies) is 11, recorded in 04-cross-cutting.md §6.2. The requirements.md YAML block, which did not parse (REQ-TRX-006 acceptance_criteria contained an unquoted 'SYS: rows'), was repaired so the machine-readable source loads again.
- **target_wave:** W9 baseline (editorial)
- **origin:** Dynamic Discovery Phase 3.7 — automated verification (spec/17-system-study/_build/verify_study.py) and owner-delegated decisions of 2026-09-30
- **status:** APPLIED (decision delegated by project owner (2026-09-30); master-study §20.3 item 5)

### CR-67

- **issue:** system-definition.md §4 still defined R3 as a single slice SLC-13 (and omitted SLC-12a, SLC-14..16); slices.md kept SLC-13 as g6_slc NOT_STARTED; use-cases.md gaps table resolved VS04 to SLC-13; EVOLUTION-ROADMAP.md said no R3 detailed design had started — while SLC-17/18/19 had been fully designed (DESIGN_COMPLETE, 2026-09-27..29).
- **correction:** system-definition §4 lists R1 SLC-01..08, SLC-11, SLC-12a; R2 SLC-09, 10, 12, 14, 15, 16; R3 SLC-17, 18, 19 (Communications still undecomposed, UNK-022). SLC-13 marked SUPERSEDED in slices.md (prose and YAML) with its decomposition; VS04 gap now resolves to SLC-17; the roadmap states that design is complete and only G6 is held (RSK-028).
- **target_wave:** W9 baseline (editorial)
- **origin:** Dynamic Discovery Phase 3.7 — automated verification (spec/17-system-study/_build/verify_study.py) and owner-delegated decisions of 2026-09-30
- **status:** APPLIED (decision delegated by project owner (2026-09-30); master-study §20.3 item 6)

### CR-68

- **issue:** Six reference-data categories (RD-HAZARD-CATEGORIES, RD-ASSET-TYPES, RD-RESOURCE-TYPES, RD-LOGISTICS-ITEM-TYPES, RD-CONDITION-GRADES, RD-EXERCISE-TYPES) were cited as mandatory guards in BC04/BC05 commands but absent from 04-information/reference-data.md (CONFLICT-03).
- **correction:** all six added to the code-list catalog (prose table and YAML) as tenant-defined, versioned lists. Seed values are Explicit where a source already states them (hazard categories: risk-contingency-spec §1; asset/resource types: R2-Q1; logistics items: logistics-spec §1), Derived for condition grades (each grade carries a serviceable flag, from AGG-ASSET guards) and Inferred examples for exercise types; the last two are marked for confirmation at tenant setup workshop.
- **target_wave:** W3 reference data (post-hoc)
- **origin:** Dynamic Discovery Phase 3.7 — automated verification (spec/17-system-study/_build/verify_study.py) and owner-delegated decisions of 2026-09-30
- **status:** APPLIED (decision delegated by project owner (2026-09-30); closes CONFLICT-03)

### CR-69

- **issue:** AGG-ERASURE-REQUEST's scoping step located subject keys only in BC01 and BC02, while AGG-QUALIFICATION-RECORD (BC05) carries personal_data: true (CONFLICT-04). Subject-key shredding already covers personal data about the person wherever stored, but BC05 was never asked to scope and confirm.
- **correction:** SYS:subject scope resolved guard now includes BC05 qualification records of the person; BC05 added to the erasure event consumers (scope + confirmation); key-hierarchy-and-disposition.md states that the subject DEK covers BC05 qualification records. Applied in the SLC-12a generator data and regenerated (aggregate, events catalog, AsyncAPI). Legal retention obligations remain handled by CMD-ERS-REJECT and legal hold, unchanged. Chosen per system-definition §6 'design for the strictest legal state'.
- **target_wave:** SLC-12a
- **origin:** Dynamic Discovery Phase 3.7 — automated verification (spec/17-system-study/_build/verify_study.py) and owner-delegated decisions of 2026-09-30
- **status:** APPLIED (decision delegated by project owner (2026-09-30); closes CONFLICT-04)

### CR-70

- **issue:** 50 requirements with clearly-actored behaviour had no Use Case (CONFLICT-05): REQ-RCM-001..016 (BC04, SLC-17), REQ-LOG-001..014 and REQ-TRX-001..015 (BC05, SLC-18/19), REQ-AI-009/010/011/013 and REQ-SRC-004 (BC07). Unlike OQ-034, every command involved has a named human actor, so this was a documentation gap, not a design choice.
- **correction:** 16 Use Cases added, each derived from the owning aggregate's command and policy tables (epistemic DER, following the CR-64/UC-089 precedent): UC-075..078 (AI model lifecycle, evaluation suites, routing and tool registry, projection rebuild), UC-140..144 (risk and incident), UC-150..152 (logistics), UC-160..163 (training and exercises). use_cases of all 50 requirements linked in requirements.md prose and YAML.
- **target_wave:** W2 requirements (post-hoc)
- **origin:** Dynamic Discovery Phase 3.7 — automated verification (spec/17-system-study/_build/verify_study.py) and owner-delegated decisions of 2026-09-30
- **status:** APPLIED (decision delegated by project owner (2026-09-30); closes CONFLICT-05)

### CR-71

- **issue:** Automated verification found the spec tooling no longer reproduced its generated files, despite the W9 round-trip claim: CR-63 and CR-65 had been applied by hand to generated Markdown only (CR-63's own 'round-trip confirmed' note was inaccurate), so regeneration would silently revert both; slice_gen wrote guard text without escaping '|', breaking three transition tables (AGG-TASK, AGG-OUTCOME-TRACKER, AGG-SUBSCRIPTION); generators hard-coded approved_at 2026-09-24 while SLC-18 files carry 2026-09-27; slc19_data lacked payload entries for three no-payload commands so SLC-19 could not be generated; AGG-CLASSIFICATION-SCHEME's acceptance spec did not verify REQ-GOV-004. Separately, three register/spec YAML blocks did not parse (corrections.md CR-64, requirements.md REQ-TRX-006, and SLC-18/19 hand-authored AGG-SCENARIO, AGG-SIMULATION, threat-model-slc18/19), open-questions.md had lost OQ-030's heading, and AGG-EXERCISE's matrix header named SYS commands absent from its own transition table.
- **correction:** slice_gen escapes '|' in guards; slice_gen, slice_contracts and acc_gen honour an optional per-slice APPROVED_AT (set for SLC-18); CR-63 and CR-65 moved into slc12_data/slc01_data; slc19_data completed. Regeneration of SLC-01..18 now reproduces every generated file byte-for-byte (V5 in 17-system-study/06-verification.md). SLC-19 remains hand-authored outside the tooling (DEBT-002). YAML blocks repaired (text preserved), OQ-030 heading restored, AGG-EXERCISE header aligned with its transitions.
- **target_wave:** W9 tooling (post-hoc)
- **origin:** Dynamic Discovery Phase 3.7 — automated verification (spec/17-system-study/_build/verify_study.py) and owner-delegated decisions of 2026-09-30
- **status:** APPLIED

### CR-72

- **issue:** acc_gen generated acceptance scenarios for actor commands only: 175 scheduler-driven (SYS:) transitions in 56 aggregates — including SYS creations such as alert raising and archive ingestion — had no acceptance scenario outside hand-written SLC-19.
- **correction:** acc_gen now emits a 'system-triggered transition' scenario outline (trigger, from, to, event; invariants hold as for actor commands) for every SYS transition including SYS creations; all SLC-01..18 acceptance files regenerated (55 files gained the scenario). V1b coverage: 175/175.
- **target_wave:** W6 acceptance (post-hoc)
- **origin:** Dynamic Discovery Phase 3.7 — automated verification (spec/17-system-study/_build/verify_study.py) and owner-delegated decisions of 2026-09-30
- **status:** APPLIED

### CR-73

- **issue:** ADR-P16 (Canonical CRS) was APPROVED_DELEGATED and its decision applied in 04-information/spatial-model.md, but its Decision Outcome section still read 'TBD — formal in W3'.
- **correction:** Decision Outcome states option 1 (canonical EPSG:4326 + original CRS and coordinates preserved), citing spatial-model.md and REQ-INF-029. Found during Phase 3.8 exploration (18-analysis-design).
- **target_wave:** W3 (editorial, post-hoc)
- **origin:** Phase 3.8 — 18-analysis-design exploration
- **status:** APPLIED

### CR-74

- **issue:** The ratified fitness-function model had no check for the module-boundary and generated-code rules introduced by ADR-P17/ADR-P18 (FIT-10 covers domain purity only).
- **correction:** FIT-20 added to 13-verification/fitness-functions.md (prose table and YAML; 20 items): no contexts→contexts or services→services imports, platform without context ports or business types, migrations limited to their own schema, command handlers reach repositories and the PDP only through the command pipeline, and contracts/ equal to the generator output. Severity ERROR. The Phase 2 entity index (17-system-study/01-entity-index.md) is a 2026-09-29 snapshot generated by PowerShell and does not list FIT-20 until regenerated.
- **target_wave:** Phase 3.8 (18-analysis-design)
- **origin:** ADR-P17, ADR-P18; independent review of Phase 3.8 stage 1
- **status:** APPLIED

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
corrections:
- id: CR-01
  issue: Geometry له مالكان في PRJ§9
  correction: المالك BC02 وحده
  target_wave: W3
  origin: V6§14
  status: 'APPLIED (W3): ownership + spatial-model'
- id: CR-02
  issue: كائنات بلا مالك
  correction: إكمال ownership.md
  target_wave: W3
  origin: V6§14
  status: 'APPLIED (W3): ownership (0 unowned)'
- id: CR-03
  issue: Envelope يحمل score واحداً
  correction: ثقة بسبعة أبعاد
  target_wave: W3
  origin: V6§14
  status: 'APPLIED (W3): object-envelope + confidence-model'
- id: CR-04
  issue: Envelope ينقصه Event/Effective Time وRecord Time لحظة
  correction: ADR-P01
  target_wave: W3
  origin: V6§14
  status: 'APPLIED (W3): object-envelope + temporal-model'
- id: CR-05
  issue: 'Situation: View أم Aggregate'
  correction: ADR-P07
  target_wave: W3
  origin: V6§14
  status: 'APPLIED (W3): ADR-P07'
- id: CR-06
  issue: حالات Task تخلط الحالات بالانتقالات
  correction: جدول V6§13.5
  target_wave: W4
  origin: V6§14
  status: 'APPLIED (SLC-03): AGG-TASK state machine, SPEC-TASK-RULES'
- id: CR-07
  issue: البادئة BR لنوعين
  correction: BRL / BRQ
  target_wave: W0
  origin: V6§14
  status: APPLIED_IN_SPEC (pending approval)
- id: CR-08
  issue: PRJ§47 يخلط الطبقات بسلسلة القيمة
  correction: C4 منفصل عن Value Stream
  target_wave: W8
  origin: V6§14
  status: 'APPLIED (W8): C4 views separate from value streams'
- id: CR-09
  issue: Use Cases ناقصة لـ VS04/VS05 ومجالات أخرى
  correction: إكمال للنطاق
  target_wave: W2
  origin: V6§14
  status: APPLIED (W2) for R1; R2/R3 gaps scheduled
- id: CR-10
  issue: '''مهم'' غير معرّف'
  correction: ADR-P03
  target_wave: W3
  origin: V6§14
  status: 'APPLIED (W3): ADR-P03 + importance-tiers'
- id: CR-11
  issue: لا مخزن متجهات
  correction: Vector Projection مؤمّنة
  target_wave: W3
  origin: V6§14
  status: 'APPLIED (W3): ADR-P06 (vector projection labels)'
- id: CR-12
  issue: الجانب الجغرافي بلا خرائط/Tiles/OGC/مسارات
  correction: ADR-P12
  target_wave: W3
  origin: V6§14
  status: 'APPLIED (W3): ADR-P12 + spatial-model'
- id: CR-13
  issue: Offline بلا تصميم
  correction: ADR-P09
  target_wave: W3
  origin: V6§14
  status: 'APPLIED (W3): ADR-P09'
- id: CR-14
  issue: عزل المستأجرين غير محدد
  correction: ADR-P04
  target_wave: W3
  origin: V6§14
  status: 'APPLIED (W3): ADR-P04'
- id: CR-15
  issue: لا Split/Unmerge
  correction: إضافة العملية
  target_wave: W3
  origin: V6§14
  status: 'APPLIED (W3): entity-resolution (split = close link)'
- id: CR-16
  issue: history/events/outbox دون مرجع
  correction: ADR-P02
  target_wave: W3
  origin: V6§14
  status: 'APPLIED (W3): ADR-P02'
- id: CR-17
  issue: أمن بلا تصنيف/Compartments/Threat Model/مفاتيح
  correction: Security Kernel
  target_wave: W3
  origin: V6§14
  status: 'APPLIED (W3): 08-security kernel'
- id: CR-18
  issue: لا معالجة للعربية
  correction: ADR-P15
  target_wave: W3
  origin: V6§14
  status: 'APPLIED (W3): ADR-P15 + language-model'
- id: CR-19
  issue: لا بيانات مرجعية
  correction: ADR-P14
  target_wave: W3
  origin: V6§14
  status: 'APPLIED (W3): ADR-P14 + reference-data'
- id: CR-20
  issue: استقلالية AI غير مربوطة بعمليات
  correction: Autonomy Matrix
  target_wave: W3
  origin: V6§14
  status: 'APPLIED (W3): autonomy-matrix'
- id: CR-21
  issue: تقنيات قبل أعباء العمل
  correction: ADR-P05
  target_wave: W8
  origin: V6§14
  status: 'APPLIED (W8): ADR-P05 + TECH-DECISIONS'
- id: CR-22
  issue: ✓ دون أدلة في PRJ§123
  correction: تقارير بوابات
  target_wave: W0
  origin: V6§14
  status: APPLIED_IN_SPEC (gate report W0)
- id: CR-23
  issue: شريحة تنفيذ واسعة
  correction: شرائح رفيعة
  target_wave: W1
  origin: V6§14
  status: APPLIED (release/slice plan W1)
- id: CR-24
  issue: لا Jurisdiction في الصلاحيات
  correction: إضافته
  target_wave: W3
  origin: V6§14
  status: APPLIED as REQ-FND-011 (W2)
- id: CR-25
  issue: إعادة البناء بلا Unknown وبلا As-Of
  correction: إضافتهما
  target_wave: W3
  origin: V6§14
  status: 'APPLIED (W3): temporal-model §8'
- id: CR-26
  issue: P00–P02 غير موثقة
  correction: W1
  target_wave: W1
  origin: V6§14
  status: APPLIED (W1)
- id: CR-27
  issue: updated يوحي بالكتابة فوق القيم
  correction: إصدار لكل تحديث T1/T2
  target_wave: W3
  origin: V6§14
  status: 'APPLIED (W3): object-envelope'
- id: CR-28
  issue: V5 مبتور
  correction: مستكمل في V6§24
  target_wave: W0
  origin: V6§14
  status: APPLIED_IN_SPEC (pending approval)
- id: CR-29
  issue: AnalysisCase وPlan مرشحان لـ God Aggregate
  correction: اختبار الحدود
  target_wave: W4
  origin: V6§14
  status: 'APPLIED: AnalysisCase (SLC-07, 5 aggregates) and Plan (SLC-08, identity + versions)'
- id: CR-30
  issue: O1–O6 غير مربوطة بالمتطلبات
  correction: OUT ← BRQ
  target_wave: W2
  origin: V6§14
  status: APPLIED (W2) OUT ← BRQ
- id: CR-31
  issue: 'Evidence معرّف في مجالين: DOM-03 (PRJ§7.3) وDOM-06 (PRJ§7.6)'
  correction: مجال مالك واحد لـ Evidence؛ الآخر يستخدمه بالمرجع
  target_wave: W3
  origin: W0 load (new)
  status: 'APPLIED (W3): claim-evidence-model §3'
- id: CR-32
  issue: Authority معرّف في DOM-01 (BC01) وDOM-10 (BC04) — سياقان مختلفان
  correction: 'مالك واحد (مرشح: BC01)، وBC04 يستهلكه عبر عقد؛ BRL-003 يعتمد عليه'
  target_wave: W3
  origin: W0 load (new)
  status: 'APPLIED (W3): ownership + context-map'
- id: CR-33
  issue: 'كلمة Policy تعني ثلاثة مفاهيم: Access Policy (DOM-02)، Policy (DOM-25)، Policy Knowledge (DOM-21)، إضافة لـ Policy
    في V5 Event Storming'
  correction: تمييزها في glossary.md بأسماء مختلفة
  target_wave: W0/W3
  origin: W0 load (new)
  status: 'APPLIED (W3): glossary + authorization-model'
- id: CR-34
  issue: 'كلمة Requirement تعني: Collection Requirement (DOM-05)، Task Requirement (DOM-13)، ومتطلبات النظام'
  correction: CollectionRequirement / TaskRequirement / REQ
  target_wave: W0/W3
  origin: W0 load (new)
  status: 'APPLIED (W3): glossary'
- id: CR-35
  issue: Assignment تعني إسناد مهمة (DOM-13, UC-041) وإسناد أصل (UC-053, PRJ§88-G)
  correction: TaskAssignment / AssetAssignment ككائنين منفصلين
  target_wave: W3
  origin: W0 load (new)
  status: 'APPLIED (W3): glossary'
- id: CR-36
  issue: Assessment تعني التقييم التحليلي (DOM-08) وتقييم الكفاءة/التعلم (BP40, BP44, VS05)
  correction: AnalyticalAssessment / CompetencyAssessment
  target_wave: W0/W3
  origin: W0 load (new)
  status: 'APPLIED (W3): glossary'
- id: CR-37
  issue: Outcome تعني نتائج العمل O1–O6 (PRJ§37) وكائن تخطيط في DOM-12
  correction: OUT (Business Outcome) / PlanOutcome
  target_wave: W0
  origin: W0 load (new)
  status: 'APPLIED (W3): glossary + BO-PLAN-OUTCOME'
- id: CR-38
  issue: Decision تعني قرار العمل (DOM-10) وقرار مطابقة الكيانات (PRJ§13) وقرار السياسة ALLOW/DENY (PRJ§66)
  correction: BusinessDecision / MatchDecision / PolicyDecision
  target_wave: W0
  origin: W0 load (new)
  status: 'APPLIED (W3): glossary'
- id: CR-39
  issue: صلاحية 'Delete / Retain / Archive' مدمجة كصلاحية واحدة (PRJ§4)
  correction: ثلاث صلاحيات منفصلة، والحذف مرتبط بـ ADR-P08
  target_wave: W3
  origin: W0 load (new)
  status: APPLIED as REQ-FND-014 (W2)
- id: CR-40
  issue: 'معيار المسار /api/v1/{domain}/{resource} (PRJ§18) يخالفه كل مثال: /api/v1/tasks/{id}/actions/complete بلا مقطع domain'
  correction: اعتماد صيغة واحدة وتطبيقها على كل العقود
  target_wave: W3
  origin: W0 load (new)
  status: 'APPLIED (W3): decided: /api/v1/{context}/{resource}; applied in W6 contracts'
- id: CR-41
  issue: Tenant وWorkspace مستخدمان (PRJ§6، §88-A) لكن لا يظهران في أي مجال من الـ 26
  correction: إسنادهما لـ DOM-01 أو DOM-02 مع مالك
  target_wave: W3
  origin: W0 load (new)
  status: 'APPLIED (W3): domains DOM-01'
- id: CR-42
  issue: Risk & Emergency (DOM-17) مصنف تحت مجموعة 'Risk, Training & Knowledge' لكنه في BC04 Operations؛ التجميع لا يطابق
    السياق
  correction: توحيد التجميع مع الـ Bounded Context أو توثيق سبب الاختلاف
  target_wave: W3
  origin: W0 load (new)
  status: 'APPLIED (W3): domains + bc-boundary-test'
- id: CR-43
  issue: Evaluation في DOM-19 وAI Evaluation في DOM-23 وCompetency Assessment — ثلاثة مفاهيم تقييم إضافية
  correction: تمييزها في القاموس
  target_wave: W0
  origin: W0 load (new)
  status: 'APPLIED (W3): glossary'
- id: CR-44
  issue: '''Event'' في Information Fabric (حدث واقعي) يختلط بـ Domain Event (سجل نظامي)'
  correction: RealWorldEvent للأول؛ Domain/Integration Event للثاني
  target_wave: W3
  origin: W3
  status: 'APPLIED (W3): meta-model §4'
- id: CR-45
  issue: 'W3 audit design: same-transaction write into BC08 store violates FIT-01; single per-tenant sequence is a throughput
    bottleneck'
  correction: audit_outbox per context + sharded hash chains + Merkle anchors
  target_wave: W4 (SLC-01)
  origin: SLC-01
  status: 'APPLIED: 08-security/audit-architecture.md'
- id: CR-46
  issue: V6§13.5 example modelled SUSPENDED as a state returning to 'prior_state' (not expressible as a fixed transition table)
  correction: suspension as orthogonal flag (INV-TASK-06); V6 example superseded by AGG-TASK
  target_wave: W4 (SLC-03)
  origin: SLC-03
  status: 'APPLIED: AGG-TASK, SPEC-TASK-RULES'
- id: CR-47
  issue: ADR-P06 §3 re-check used a central security-version table for objects; keeping it current requires cross-context
    writes
  correction: 'objects: LabelCheck OHS implemented by each owning context (batched per page); subjects: BC01 security-version
    KV (unchanged)'
  target_wave: W4 (SLC-05)
  origin: SLC-05
  status: 'APPLIED: SPEC-DISCOVERY §4.1, ADR-P06 amendment'
- id: CR-48
  issue: contracts generator did not support 'number' payload fields (found by OpenAPI validator in SLC-08)
  correction: generator supports number; earlier slices checked — none affected
  target_wave: W6 (SLC-08)
  origin: SLC-08
  status: APPLIED
- id: CR-49
  issue: CONFLICT-MODEL listed CF-05 (sync) as a BC02 claim conflict; stale state-changing commands are not claim disagreements
  correction: CF-05 represented by AGG-SYNC-CONFLICT (BC07); claims from synced observations still use CF-01..04
  target_wave: W4 (SLC-11)
  origin: SLC-11
  status: 'APPLIED: conflict-model, SPEC-FIELD-SYNC §5'
- id: CR-50
  issue: offline-created objects need identities before reaching the server
  correction: creation commands accept client-generated ULID (client_id) — SLC-02 regenerated
  target_wave: W6 (SLC-11)
  origin: SLC-11
  status: 'APPLIED: slc02 contracts'
- id: CR-51
  issue: ADR-P08 claimed backups become unrecoverable 'immediately' via key destruction, but key-store backups could revive
    destroyed keys
  correction: append-only key-destruction log + restore gate + key-store backup retention ≤ 35 d; class-bucket keys for disposition
  target_wave: W4 (SLC-12a)
  origin: SLC-12a
  status: 'APPLIED: SPEC-KEYS-DISPOSITION, ADR-P08 amendment, FIT-19'
- id: CR-52
  issue: REQ-GOV-002 required a classification on every T1/T2 object, but 12 creation commands (links, configuration, derived
    objects) carry none
  correction: 'label source defined for every aggregate: explicit, derived by rule, or administrative default (LABEL-DERIVATION,
    SL-29)'
  target_wave: W7 (consolidation)
  origin: global coverage check
  status: APPLIED
- id: CR-53
  issue: 'global coverage check: 15 R1 requirements not traced by any domain slice (platform & cross-cutting)'
  correction: 8 traced via fitness functions and contract lint; 7 assigned to W8/W9 explicitly (TRACE-PLATFORM)
  target_wave: W8/W9
  origin: global coverage check
  status: 'APPLIED (W8): all 15 platform requirements traced (TRACE-PLATFORM)'
- id: CR-54
  issue: search indexes treated as rebuildable-only, but full rebuild (≤ 24 h) exceeds the important-tier RTO (4 h)
  correction: OpenSearch snapshots every 15 min to object storage, restored in DR, then catch-up from Kafka
  target_wave: W8
  origin: W8 DR design
  status: 'APPLIED: DR-CONTINUITY §3'
- id: CR-55
  issue: 'W9 consistency check: CMD-RUN-SUBMIT missing from OpenAPI — two creation commands mapped to the same path and the
    generator silently overwrote one'
  correction: CMD-RUN-REPRODUCE moved to /analysis-runs/{id}/actions/reproduce; generator now fails on any path collision;
    all slices re-scanned (no other collision)
  target_wave: W9
  origin: W9 consistency check
  status: APPLIED
- id: CR-56
  issue: 'W9 consistency check: 19 of 74 quality scenarios had no explicit verification reference'
  correction: Quality Verification Matrix maps every QAS to method and timing
  target_wave: W9
  origin: W9 consistency check
  status: APPLIED
- id: CR-57
  issue: 'reproducibility: contracts of early slices had been produced by older generator versions (missing x-offline-capable),
    and schema enrichments of 6 slices were applied by ad-hoc post-processing — regeneration would have lost them'
  correction: all enrichments moved into slice source data (enrich hooks); every slice regenerated; full round-trip from Markdown-embedded
    tooling reproduces the package with 0 differing files
  target_wave: W9
  origin: W9 round-trip test
  status: APPLIED
- id: CR-58
  issue: AI retrieval needs a vector projection but projection versions only allowed search and graph
  correction: AGG-PROJECTION-VERSION kind extended with vector (embedding model version part of the projection version); SLC-05
    regenerated
  target_wave: SLC-10
  origin: SLC-10
  status: APPLIED
- id: CR-59
  issue: task plan_ref assumed an operations plan only; collection plans also generate field tasks
  correction: plan_ref accepts an operations plan or a collection plan; SLC-03 source updated and regenerated
  target_wave: SLC-14
  origin: SLC-14
  status: APPLIED
- id: CR-60
  issue: SLC-17's continuity/contingency plans need a Plan (SLC-08) triggered by a risk or incident, not a decision
    or objective (R3-Q2 reuse decision); Plan identity carried no notion of kind or trigger
  correction: AGG-PLAN gains plan_kind (OPERATIONS, CONTINGENCY; INV-PLN-04) and an optional triggered_by reference;
    CMD-PLN-CREATE accepts a risk_ref/incident_ref trigger for plan_kind=CONTINGENCY as an alternative to implementing
    a decision or objective; SLC-08 source updated and regenerated
  target_wave: SLC-17
  origin: SLC-17
  status: APPLIED
- id: CR-61
  issue: SLC-17's incident response tasks need to be created directly under an Incident without a plan, but AGG-TASK's
    creation guard only accepted a plan_ref or an ad_hoc_reason (CR-59)
  correction: CMD-TASK-CREATE gains an incident_ref alternative to plan_ref; SLC-03 source updated and regenerated
  target_wave: SLC-17
  origin: SLC-17
  status: APPLIED
- id: CR-62
  issue: SLC-18's logistics requests need to commit inventory quantity through SLC-09's existing Allocation (R3-Q3
    reuse decision) rather than a second capacity-reservation engine, but AGG-ALLOCATION's creation guard described
    target as task/activity only (the payload field target!:urn itself was already generic)
  correction: CMD-ALC-REQUEST's guard text is broadened to accept a logistics-request reference as a third alternative
    to task/activity; no payload schema change; SLC-09 source updated and regenerated — round-trip confirmed only
    the guard-text lines changed, with OpenAPI/AsyncAPI/errors/acceptance byte-identical to the prior baseline
  target_wave: SLC-18
  origin: SLC-18
  status: APPLIED
- id: CR-63
  issue: SLC-19's After Action Review needs a completed exercise simulation to be a valid terminal source for a lesson-type
    Knowledge Object (R3-Q5 reuse decision), but AGG-KNOWLEDGE-OBJECT's CMD-KNO-DRAFT guard restricted lesson terminal sources
    to task, plan or incident only (REQ-KNW-002); the payload field itself (source:urn) was already generic
  correction: CMD-KNO-DRAFT's guard text is broadened to accept a completed exercise simulation as a fourth alternative terminal
    source for lessons, alongside task/plan/incident; REQ-KNW-002's statement and acceptance criteria are broadened to match;
    no payload schema change; SLC-12 source updated and regenerated — round-trip confirmed only the guard-text line in AGG-KNOWLEDGE-OBJECT.md
    and the matching guard line in commands-slc12.md changed, with OpenAPI/AsyncAPI/errors/acceptance byte-identical to the
    prior baseline
  target_wave: SLC-19
  origin: SLC-19
  status: APPLIED
- id: CR-65
  issue: AGG-CLASSIFICATION-SCHEME.md (BC08) did not list REQ-GOV-004 in traces.satisfies despite requirements.md already
    citing UC-085 for it (CR-64 residual_note); INV-CLS-04 (activation increments security_version of all subjects) is the
    scheme-level enforcement mechanism for REQ-GOV-004
  correction: added REQ-GOV-004 to AGG-CLASSIFICATION-SCHEME.md's traces.satisfies (prose + YAML); no requirements.md change
    needed
  target_wave: W7 (post-hoc, BC08 study)
  origin: Dynamic Discovery Phase 3 — BC08 study, closing CONFLICT-01/OQ-034
  status: APPLIED
- id: CR-64
  issue: REQ-GOV-004's use_cases field pointed only to UC-085 (Manage Classification Scheme & Compartments, BC08, satisfies
    REQ-GOV-001/REQ-GOV-009 per AGG-CLASSIFICATION-SCHEME.md — REQ-GOV-004 is absent from that aggregate's own traces.satisfies),
    while the aggregate that actually declares satisfies REQ-GOV-004 is AGG-CLEARANCE (BC01), which had no Use Case at all;
    REQ-GOV-003 (also satisfied by AGG-CLEARANCE) likewise had use_cases empty. Net result — no Use Case covered granting/modifying/suspending/revoking
    a user's clearance (CMD-CLR-GRANT/APPROVE/ MODIFY/SUSPEND/REINSTATE/REVOKE), even though the commands, policies, events
    and acceptance tests for that lifecycle are fully specified
  correction: 'added UC-089 — Manage User Clearance (BC01, CAP-13.01, actor Security Officer, covers AGG-CLEARANCE''s full
    command set) to use-cases.md (numbering: next free slot in the reserved cross-cutting 080-089 range per OQ-001); linked
    REQ-GOV-003.use_cases -> UC-089 and REQ-GOV-004.use_cases -> UC-085, UC-089 (both requirements.md prose and YAML blocks)
    since REQ-GOV-004''s acceptance criterion (after a downgrade of a user''s access...) is the clearance-side (BC01) path,
    distinct from UC-085''s object/scheme-side path (BC08)'
  residual_note: AGG-CLASSIFICATION-SCHEME.md's own traces.satisfies (BC08) still does not list REQ-GOV-004, even though UC-085
    is now documented as contributing to it via its scheme-activation security-version bump (INV-CLS-04). Left unchanged pending
    human review — flagged here rather than edited silently, since it touches a different bounded context's approved aggregate
    file
  target_wave: W7 (post-hoc, discovered during BC01 feature deep-dive, not a slice-generation artifact)
  origin: Dynamic Discovery reverse-check on AGG-AUTHORITY-GRANT/AGG-CLEARANCE (Reverse Discovery pass against trace-slc01.md)
  status: APPLIED (confirmed 2026-09-30 under owner-delegated authority; master-study §20.3 item 3)
- id: CR-66
  issue: requirements.md `system_requirements` header stated `_181 items_` while the section (and its YAML block) holds 210
    requirements (R1 114, R2 51, R3 45); the R3 requirements added in W1/W2-R3 on 2026-09-27 were never counted. The study's
    04-cross-cutting §6.2 had built a false '21 intentional overlaps' explanation on the stale figure.
  correction: 'header set to 210 with a pointer to this CR; the actual overlap between bounded contexts (from traces.satisfies)
    is 11, recorded in 04-cross-cutting.md §6.2. The requirements.md YAML block, which did not parse (REQ-TRX-006 acceptance_criteria
    contained an unquoted ''SYS: rows''), was repaired so the machine-readable source loads again.'
  target_wave: W9 baseline (editorial)
  origin: Dynamic Discovery Phase 3.7 — automated verification (spec/17-system-study/_build/verify_study.py) and owner-delegated
    decisions of 2026-09-30
  status: APPLIED (decision delegated by project owner (2026-09-30); master-study §20.3 item 5)
- id: CR-67
  issue: system-definition.md §4 still defined R3 as a single slice SLC-13 (and omitted SLC-12a, SLC-14..16); slices.md kept
    SLC-13 as g6_slc NOT_STARTED; use-cases.md gaps table resolved VS04 to SLC-13; EVOLUTION-ROADMAP.md said no R3 detailed
    design had started — while SLC-17/18/19 had been fully designed (DESIGN_COMPLETE, 2026-09-27..29).
  correction: system-definition §4 lists R1 SLC-01..08, SLC-11, SLC-12a; R2 SLC-09, 10, 12, 14, 15, 16; R3 SLC-17, 18, 19
    (Communications still undecomposed, UNK-022). SLC-13 marked SUPERSEDED in slices.md (prose and YAML) with its decomposition;
    VS04 gap now resolves to SLC-17; the roadmap states that design is complete and only G6 is held (RSK-028).
  target_wave: W9 baseline (editorial)
  origin: Dynamic Discovery Phase 3.7 — automated verification (spec/17-system-study/_build/verify_study.py) and owner-delegated
    decisions of 2026-09-30
  status: APPLIED (decision delegated by project owner (2026-09-30); master-study §20.3 item 6)
- id: CR-68
  issue: Six reference-data categories (RD-HAZARD-CATEGORIES, RD-ASSET-TYPES, RD-RESOURCE-TYPES, RD-LOGISTICS-ITEM-TYPES,
    RD-CONDITION-GRADES, RD-EXERCISE-TYPES) were cited as mandatory guards in BC04/BC05 commands but absent from 04-information/reference-data.md
    (CONFLICT-03).
  correction: 'all six added to the code-list catalog (prose table and YAML) as tenant-defined, versioned lists. Seed values
    are Explicit where a source already states them (hazard categories: risk-contingency-spec §1; asset/resource types: R2-Q1;
    logistics items: logistics-spec §1), Derived for condition grades (each grade carries a serviceable flag, from AGG-ASSET
    guards) and Inferred examples for exercise types; the last two are marked for confirmation at tenant setup workshop.'
  target_wave: W3 reference data (post-hoc)
  origin: Dynamic Discovery Phase 3.7 — automated verification (spec/17-system-study/_build/verify_study.py) and owner-delegated
    decisions of 2026-09-30
  status: APPLIED (decision delegated by project owner (2026-09-30); closes CONFLICT-03)
- id: CR-69
  issue: 'AGG-ERASURE-REQUEST''s scoping step located subject keys only in BC01 and BC02, while AGG-QUALIFICATION-RECORD (BC05)
    carries personal_data: true (CONFLICT-04). Subject-key shredding already covers personal data about the person wherever
    stored, but BC05 was never asked to scope and confirm.'
  correction: SYS:subject scope resolved guard now includes BC05 qualification records of the person; BC05 added to the erasure
    event consumers (scope + confirmation); key-hierarchy-and-disposition.md states that the subject DEK covers BC05 qualification
    records. Applied in the SLC-12a generator data and regenerated (aggregate, events catalog, AsyncAPI). Legal retention
    obligations remain handled by CMD-ERS-REJECT and legal hold, unchanged. Chosen per system-definition §6 'design for the
    strictest legal state'.
  target_wave: SLC-12a
  origin: Dynamic Discovery Phase 3.7 — automated verification (spec/17-system-study/_build/verify_study.py) and owner-delegated
    decisions of 2026-09-30
  status: APPLIED (decision delegated by project owner (2026-09-30); closes CONFLICT-04)
- id: CR-70
  issue: '50 requirements with clearly-actored behaviour had no Use Case (CONFLICT-05): REQ-RCM-001..016 (BC04, SLC-17), REQ-LOG-001..014
    and REQ-TRX-001..015 (BC05, SLC-18/19), REQ-AI-009/010/011/013 and REQ-SRC-004 (BC07). Unlike OQ-034, every command involved
    has a named human actor, so this was a documentation gap, not a design choice.'
  correction: '16 Use Cases added, each derived from the owning aggregate''s command and policy tables (epistemic DER, following
    the CR-64/UC-089 precedent): UC-075..078 (AI model lifecycle, evaluation suites, routing and tool registry, projection
    rebuild), UC-140..144 (risk and incident), UC-150..152 (logistics), UC-160..163 (training and exercises). use_cases of
    all 50 requirements linked in requirements.md prose and YAML.'
  target_wave: W2 requirements (post-hoc)
  origin: Dynamic Discovery Phase 3.7 — automated verification (spec/17-system-study/_build/verify_study.py) and owner-delegated
    decisions of 2026-09-30
  status: APPLIED (decision delegated by project owner (2026-09-30); closes CONFLICT-05)
- id: CR-71
  issue: 'Automated verification found the spec tooling no longer reproduced its generated files, despite the W9 round-trip
    claim: CR-63 and CR-65 had been applied by hand to generated Markdown only (CR-63''s own ''round-trip confirmed'' note
    was inaccurate), so regeneration would silently revert both; slice_gen wrote guard text without escaping ''|'', breaking
    three transition tables (AGG-TASK, AGG-OUTCOME-TRACKER, AGG-SUBSCRIPTION); generators hard-coded approved_at 2026-09-24
    while SLC-18 files carry 2026-09-27; slc19_data lacked payload entries for three no-payload commands so SLC-19 could not
    be generated; AGG-CLASSIFICATION-SCHEME''s acceptance spec did not verify REQ-GOV-004. Separately, three register/spec
    YAML blocks did not parse (corrections.md CR-64, requirements.md REQ-TRX-006, and SLC-18/19 hand-authored AGG-SCENARIO,
    AGG-SIMULATION, threat-model-slc18/19), open-questions.md had lost OQ-030''s heading, and AGG-EXERCISE''s matrix header
    named SYS commands absent from its own transition table.'
  correction: slice_gen escapes '|' in guards; slice_gen, slice_contracts and acc_gen honour an optional per-slice APPROVED_AT
    (set for SLC-18); CR-63 and CR-65 moved into slc12_data/slc01_data; slc19_data completed. Regeneration of SLC-01..18 now
    reproduces every generated file byte-for-byte (V5 in 17-system-study/06-verification.md). SLC-19 remains hand-authored
    outside the tooling (DEBT-002). YAML blocks repaired (text preserved), OQ-030 heading restored, AGG-EXERCISE header aligned
    with its transitions.
  target_wave: W9 tooling (post-hoc)
  origin: Dynamic Discovery Phase 3.7 — automated verification (spec/17-system-study/_build/verify_study.py) and owner-delegated
    decisions of 2026-09-30
  status: APPLIED
- id: CR-72
  issue: 'acc_gen generated acceptance scenarios for actor commands only: 175 scheduler-driven (SYS:) transitions in 56 aggregates
    — including SYS creations such as alert raising and archive ingestion — had no acceptance scenario outside hand-written
    SLC-19.'
  correction: 'acc_gen now emits a ''system-triggered transition'' scenario outline (trigger, from, to, event; invariants
    hold as for actor commands) for every SYS transition including SYS creations; all SLC-01..18 acceptance files regenerated
    (55 files gained the scenario). V1b coverage: 175/175.'
  target_wave: W6 acceptance (post-hoc)
  origin: Dynamic Discovery Phase 3.7 — automated verification (spec/17-system-study/_build/verify_study.py) and owner-delegated
    decisions of 2026-09-30
  status: APPLIED
- id: CR-73
  issue: ADR-P16 (Canonical CRS) was APPROVED_DELEGATED and its decision applied in 04-information/spatial-model.md, but its
    Decision Outcome section still read 'TBD — formal in W3'.
  correction: Decision Outcome states option 1 (canonical EPSG:4326 + original CRS and coordinates preserved), citing spatial-model.md
    and REQ-INF-029. Found during Phase 3.8 exploration (18-analysis-design).
  target_wave: W3 (editorial, post-hoc)
  origin: Phase 3.8 — 18-analysis-design exploration
  status: APPLIED
- id: CR-74
  issue: The ratified fitness-function model had no check for the module-boundary and generated-code rules introduced by ADR-P17/ADR-P18
    (FIT-10 covers domain purity only).
  correction: 'FIT-20 added to 13-verification/fitness-functions.md (prose table and YAML; 20 items): no contexts→contexts
    or services→services imports, platform without context ports or business types, migrations limited to their own schema,
    command handlers reach repositories and the PDP only through the command pipeline, and contracts/ equal to the generator
    output. Severity ERROR. The Phase 2 entity index (17-system-study/01-entity-index.md) is a 2026-09-29 snapshot generated
    by PowerShell and does not list FIT-20 until regenerated.'
  target_wave: Phase 3.8 (18-analysis-design)
  origin: ADR-P17, ADR-P18; independent review of Phase 3.8 stage 1
  status: APPLIED
```

</details>
