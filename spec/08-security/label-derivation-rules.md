---
id: LABEL-DERIVATION
type: security-model
title: Label Derivation Rules — every aggregate (REQ-GOV-002 clarified)
wave: W7 (SLC-12a consolidation)
tier: T0
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
notes: 'REQ-GOV-002 تعني: لكل كائن T1/T2 تسمية معروفة المصدر — صريحة، أو مشتقة بقاعدة ثابتة، أو إدارية افتراضية. القاعدة SL-29:
  كل Aggregate مدرج هنا بمصدر تسمية.'
---

# Label Derivation Rules — every aggregate (REQ-GOV-002 clarified)

> REQ-GOV-002 تعني: لكل كائن T1/T2 تسمية معروفة المصدر — صريحة، أو مشتقة بقاعدة ثابتة، أو إدارية افتراضية. القاعدة SL-29: كل Aggregate مدرج هنا بمصدر تسمية.

## rules

_84 items_

| aggregate | bc | slice | tier | label_source | personal_data |
|---|---|---|---|---|---|
| AGG-TENANT | BC01 | SLC-01 | T2 | administrative (tenant default administrative level, INTERNAL unless configured) | no |
| AGG-ORGANIZATION | BC01 | SLC-01 | T2 | administrative (tenant default administrative level, INTERNAL unless configured) | no |
| AGG-PERSON | BC01 | SLC-01 | T2 | administrative (tenant default administrative level, INTERNAL unless configured) | yes |
| AGG-USER | BC01 | SLC-01 | T2 | administrative (tenant default administrative level, INTERNAL unless configured) | no |
| AGG-SERVICE-ACCOUNT | BC01 | SLC-01 | T2 | administrative (tenant default administrative level, INTERNAL unless configured) | no |
| AGG-ROLE | BC01 | SLC-01 | T2 | administrative (tenant default administrative level, INTERNAL unless configured) | no |
| AGG-ROLE-ASSIGNMENT | BC01 | SLC-01 | T2 | administrative (tenant default administrative level, INTERNAL unless configured) | no |
| AGG-AUTHORITY-GRANT | BC01 | SLC-01 | T2 | administrative (tenant default administrative level, INTERNAL unless configured) | no |
| AGG-CLEARANCE | BC01 | SLC-01 | T2 | administrative (tenant default administrative level, INTERNAL unless configured) | no |
| AGG-CLASSIFICATION-SCHEME | BC08 | SLC-01 | T2 | administrative (tenant default administrative level, INTERNAL unless configured) | no |
| AGG-POLICY-SET | BC08 | SLC-01 | T2 | administrative (tenant default administrative level, INTERNAL unless configured) | no |
| AGG-SECURITY-EXCEPTION | BC08 | SLC-01 | T2 | administrative (tenant default administrative level, INTERNAL unless configured) | no |
| AGG-SOURCE | BC02 | SLC-02 | T1 reliability / T2 profile | explicit (label! in creation command) | no |
| AGG-OBSERVATION | BC02 | SLC-02 | T1 | explicit (label! in creation command) | no |
| AGG-ENTITY | BC02 | SLC-02 | T2 identity; attributes T1 as claims | explicit (label! in creation command) | no |
| AGG-REALWORLD-EVENT | BC02 | SLC-02 | T2 identity; attributes T1 | explicit (label! in creation command) | no |
| AGG-RELATIONSHIP | BC02 | SLC-02 | T1 | explicit (label! in creation command) | no |
| AGG-CLAIM | BC02 | SLC-02 | T1 | explicit (label! in creation command) | no |
| AGG-EVIDENCE | BC02 | SLC-02 | T1 | explicit (label! in creation command) | no |
| AGG-EVIDENCE-LINK | BC02 | SLC-02 | T1 | max(evidence label, claim label) — INV-EVL-02 | no |
| AGG-ATTACHMENT | BC02 | SLC-02 | T1 metadata | explicit (label! in creation command) | no |
| AGG-IMPORT-BATCH | BC02 | SLC-02 | T2 | administrative (reference/configuration object) | no |
| AGG-EXTERNAL-ID | BC02 | SLC-02 | T2 | administrative (reference/configuration object) | no |
| AGG-ADAPTER | BC07 | SLC-02 | T2 | administrative (tenant default administrative level, INTERNAL unless configured) | no |
| AGG-TASK | BC04 | SLC-03 | T2 | explicit (label! in creation command) | no |
| AGG-TASK-TYPE | BC04 | SLC-03 | T2 | administrative (reference/configuration object) | no |
| AGG-QUALIFICATION-RECORD | BC05 | SLC-03 | T2 | administrative + personal_data | yes |
| AGG-CONFLICT | BC02 | SLC-04 | T2 (bitemporal resolution records) | max(member claim labels) — INV-CNF-04 | no |
| AGG-ER-CASE | BC02 | SLC-04 | T2 | max(left entity label, right entity label) | no |
| AGG-MATCH-RULESET | BC02 | SLC-04 | T2 | administrative (reference/configuration object) | no |
| AGG-PROJECTION-VERSION | BC07 | SLC-05 | T3 | T3 — none (platform operational) | no |
| AGG-SITUATION | BC03 | SLC-06 | T2 definition; content is a projection | explicit (label! in creation command) | no |
| AGG-ALERT-RULE | BC03 | SLC-06 | T2 | explicit (label! in creation command) | no |
| AGG-ALERT | BC03 | SLC-06 | T2 | max(rule label, triggering object labels) — INV-ALR-02 | no |
| AGG-SUBSCRIPTION | BC04 | SLC-06 | T3 | T3 — none (visibility of target governs) | no |
| AGG-NOTIFICATION | BC04 | SLC-06 | T3 | = referenced object label (content never embedded) | no |
| AGG-ANALYSIS-CASE | BC03 | SLC-07 | T2 lifecycle; T1 selections | explicit (label! in creation command) | no |
| AGG-ANALYSIS-METHOD | BC03 | SLC-07 | T2 | administrative (reference/configuration object) | no |
| AGG-ANALYSIS-RUN | BC03 | SLC-07 | T1 results / T2 lifecycle | explicit on submit, ≥ max(input labels); reproduction copies source run label — INV-RUN-02 | no |
| AGG-FINDING | BC03 | SLC-07 | T1 | explicit (label! in creation command) | no |
| AGG-ASSESSMENT | BC03 | SLC-07 | T1 content / T2 lifecycle | explicit (label! in creation command) | no |
| AGG-DECISION-REQUEST | BC04 | SLC-08 | T2 | explicit (label! in creation command) | no |
| AGG-DECISION | BC04 | SLC-08 | T2 | explicit (label! in creation command) | no |
| AGG-PLAN | BC04 | SLC-08 | T2 | explicit (label! in creation command) | no |
| AGG-PLAN-VERSION | BC04 | SLC-08 | T2 | = plan label | no |
| AGG-OUTCOME-TRACKER | BC04 | SLC-08 | T2 | = plan label | no |
| AGG-DEVICE | BC01 | SLC-11 | T2 | administrative (tenant default administrative level, INTERNAL unless configured) | no |
| AGG-PRELOAD-PACKAGE | BC07 | SLC-11 | T2 | = requested level (≤ tenant offline max) | no |
| AGG-SYNC-SESSION | BC07 | SLC-11 | T2 | administrative (tenant default) | no |
| AGG-SYNC-CONFLICT | BC07 | SLC-11 | T2 | = target object label | no |
| AGG-RETENTION-SCHEDULE | BC08 | SLC-12a | T2 | administrative | no |
| AGG-LEGAL-HOLD | BC08 | SLC-12a | T2 | administrative (Legal) | no |
| AGG-DISPOSITION-RUN | BC08 | SLC-12a | T2 | administrative | no |
| AGG-ERASURE-REQUEST | BC08 | SLC-12a | T2 | administrative + personal_data | yes |
| AGG-ASSET | BC05 | SLC-09 | T2 (location as T1 claims on the linked entity) | explicit (label! in creation command) | no |
| AGG-MAINTENANCE-ORDER | BC05 | SLC-09 | T2 | = asset label | no |
| AGG-ASSET-RESERVATION | BC05 | SLC-09 | T2 | explicit (label! in creation command), ≥ asset label | no |
| AGG-ASSET-ASSIGNMENT | BC05 | SLC-09 | T2 | max(asset label, task label) | no |
| AGG-RESOURCE-POOL | BC05 | SLC-09 | T2 | explicit (label! in creation command) | no |
| AGG-ALLOCATION | BC05 | SLC-09 | T2 | max(pool label, target label) | no |
| AGG-ROLE-REQUIREMENT | BC05 | SLC-09 | T2 | administrative | no |
| AGG-PRODUCT-TEMPLATE | BC06 | SLC-12 | T2 | administrative | no |
| AGG-PRODUCT | BC06 | SLC-12 | T1 content / T2 lifecycle | explicit (label! in creation command), ≥ included content | no |
| AGG-DISTRIBUTION | BC06 | SLC-12 | T2 | = product label | no |
| AGG-KNOWLEDGE-OBJECT | BC06 | SLC-12 | T1 content / T2 lifecycle | explicit (label! in creation command), ≥ source | no |
| AGG-ARCHIVE-PACKAGE | BC06 | SLC-12 | T1 | = max label of archived records | no |
| AGG-RECONSTRUCTION | BC06 | SLC-12 | T2 | ≥ max label of reported elements (≤ requester clearance) | no |
| AGG-AI-REQUEST | BC07 | SLC-10 | T1 (when its output is used) / T2 | = max(context item labels) ≤ requester clearance | no |
| AGG-AI-RESULT | BC07 | SLC-10 | T1 | = originating request label | no |
| AGG-MODEL-VERSION | BC07 | SLC-10 | T2 | administrative | no |
| AGG-AI-ROUTING | BC07 | SLC-10 | T2 | administrative | no |
| AGG-AI-TOOL | BC07 | SLC-10 | T2 | administrative | no |
| AGG-EVAL-SUITE | BC07 | SLC-10 | T2 | = max label of evaluation items (tenant samples) or administrative | no |
| AGG-COLLECTION-REQUIREMENT | BC02 | SLC-14 | T2 | explicit (label! in creation command) | no |
| AGG-COLLECTION-PLAN | BC02 | SLC-14 | T2 | explicit, ≥ requirements | no |
| AGG-COORDINATION-CASE | BC04 | SLC-15 | T2 | explicit (label! in creation command) | no |
| AGG-CORRELATION-PROPOSAL | BC02 | SLC-15 | T2 | max(input labels) | no |
| AGG-CORRELATION-RULE | BC02 | SLC-15 | T2 | administrative | no |
| AGG-INTEGRATION-CONNECTION | BC07 | SLC-16 | T2 | administrative | no |
| AGG-SENSOR-STREAM | BC07 | SLC-16 | T2 | = source label | no |
| AGG-HR-SYNC-PROPOSAL | BC01 | SLC-16 | T2 | administrative + personal_data | yes |
| AGG-CAP-MESSAGE | BC03 | SLC-16 | T2 | = alert label (must be ≤ external release level) | no |
| AGG-RISK | BC04 | SLC-17 | T2 | explicit (label! in creation command) | no |
| AGG-INCIDENT | BC04 | SLC-17 | T1 | explicit (label! in creation command) | no |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
rules:
- aggregate: AGG-TENANT
  bc: BC01
  slice: SLC-01
  tier: T2
  label_source: administrative (tenant default administrative level, INTERNAL unless configured)
  personal_data: false
- aggregate: AGG-ORGANIZATION
  bc: BC01
  slice: SLC-01
  tier: T2
  label_source: administrative (tenant default administrative level, INTERNAL unless configured)
  personal_data: false
- aggregate: AGG-PERSON
  bc: BC01
  slice: SLC-01
  tier: T2
  label_source: administrative (tenant default administrative level, INTERNAL unless configured)
  personal_data: true
- aggregate: AGG-USER
  bc: BC01
  slice: SLC-01
  tier: T2
  label_source: administrative (tenant default administrative level, INTERNAL unless configured)
  personal_data: false
- aggregate: AGG-SERVICE-ACCOUNT
  bc: BC01
  slice: SLC-01
  tier: T2
  label_source: administrative (tenant default administrative level, INTERNAL unless configured)
  personal_data: false
- aggregate: AGG-ROLE
  bc: BC01
  slice: SLC-01
  tier: T2
  label_source: administrative (tenant default administrative level, INTERNAL unless configured)
  personal_data: false
- aggregate: AGG-ROLE-ASSIGNMENT
  bc: BC01
  slice: SLC-01
  tier: T2
  label_source: administrative (tenant default administrative level, INTERNAL unless configured)
  personal_data: false
- aggregate: AGG-AUTHORITY-GRANT
  bc: BC01
  slice: SLC-01
  tier: T2
  label_source: administrative (tenant default administrative level, INTERNAL unless configured)
  personal_data: false
- aggregate: AGG-CLEARANCE
  bc: BC01
  slice: SLC-01
  tier: T2
  label_source: administrative (tenant default administrative level, INTERNAL unless configured)
  personal_data: false
- aggregate: AGG-CLASSIFICATION-SCHEME
  bc: BC08
  slice: SLC-01
  tier: T2
  label_source: administrative (tenant default administrative level, INTERNAL unless configured)
  personal_data: false
- aggregate: AGG-POLICY-SET
  bc: BC08
  slice: SLC-01
  tier: T2
  label_source: administrative (tenant default administrative level, INTERNAL unless configured)
  personal_data: false
- aggregate: AGG-SECURITY-EXCEPTION
  bc: BC08
  slice: SLC-01
  tier: T2
  label_source: administrative (tenant default administrative level, INTERNAL unless configured)
  personal_data: false
- aggregate: AGG-SOURCE
  bc: BC02
  slice: SLC-02
  tier: T1 reliability / T2 profile
  label_source: explicit (label! in creation command)
  personal_data: false
- aggregate: AGG-OBSERVATION
  bc: BC02
  slice: SLC-02
  tier: T1
  label_source: explicit (label! in creation command)
  personal_data: false
- aggregate: AGG-ENTITY
  bc: BC02
  slice: SLC-02
  tier: T2 identity; attributes T1 as claims
  label_source: explicit (label! in creation command)
  personal_data: false
- aggregate: AGG-REALWORLD-EVENT
  bc: BC02
  slice: SLC-02
  tier: T2 identity; attributes T1
  label_source: explicit (label! in creation command)
  personal_data: false
- aggregate: AGG-RELATIONSHIP
  bc: BC02
  slice: SLC-02
  tier: T1
  label_source: explicit (label! in creation command)
  personal_data: false
- aggregate: AGG-CLAIM
  bc: BC02
  slice: SLC-02
  tier: T1
  label_source: explicit (label! in creation command)
  personal_data: false
- aggregate: AGG-EVIDENCE
  bc: BC02
  slice: SLC-02
  tier: T1
  label_source: explicit (label! in creation command)
  personal_data: false
- aggregate: AGG-EVIDENCE-LINK
  bc: BC02
  slice: SLC-02
  tier: T1
  label_source: max(evidence label, claim label) — INV-EVL-02
  personal_data: false
- aggregate: AGG-ATTACHMENT
  bc: BC02
  slice: SLC-02
  tier: T1 metadata
  label_source: explicit (label! in creation command)
  personal_data: false
- aggregate: AGG-IMPORT-BATCH
  bc: BC02
  slice: SLC-02
  tier: T2
  label_source: administrative (reference/configuration object)
  personal_data: false
- aggregate: AGG-EXTERNAL-ID
  bc: BC02
  slice: SLC-02
  tier: T2
  label_source: administrative (reference/configuration object)
  personal_data: false
- aggregate: AGG-ADAPTER
  bc: BC07
  slice: SLC-02
  tier: T2
  label_source: administrative (tenant default administrative level, INTERNAL unless configured)
  personal_data: false
- aggregate: AGG-TASK
  bc: BC04
  slice: SLC-03
  tier: T2
  label_source: explicit (label! in creation command)
  personal_data: false
- aggregate: AGG-TASK-TYPE
  bc: BC04
  slice: SLC-03
  tier: T2
  label_source: administrative (reference/configuration object)
  personal_data: false
- aggregate: AGG-QUALIFICATION-RECORD
  bc: BC05
  slice: SLC-03
  tier: T2
  label_source: administrative + personal_data
  personal_data: true
- aggregate: AGG-CONFLICT
  bc: BC02
  slice: SLC-04
  tier: T2 (bitemporal resolution records)
  label_source: max(member claim labels) — INV-CNF-04
  personal_data: false
- aggregate: AGG-ER-CASE
  bc: BC02
  slice: SLC-04
  tier: T2
  label_source: max(left entity label, right entity label)
  personal_data: false
- aggregate: AGG-MATCH-RULESET
  bc: BC02
  slice: SLC-04
  tier: T2
  label_source: administrative (reference/configuration object)
  personal_data: false
- aggregate: AGG-PROJECTION-VERSION
  bc: BC07
  slice: SLC-05
  tier: T3
  label_source: T3 — none (platform operational)
  personal_data: false
- aggregate: AGG-SITUATION
  bc: BC03
  slice: SLC-06
  tier: T2 definition; content is a projection
  label_source: explicit (label! in creation command)
  personal_data: false
- aggregate: AGG-ALERT-RULE
  bc: BC03
  slice: SLC-06
  tier: T2
  label_source: explicit (label! in creation command)
  personal_data: false
- aggregate: AGG-ALERT
  bc: BC03
  slice: SLC-06
  tier: T2
  label_source: max(rule label, triggering object labels) — INV-ALR-02
  personal_data: false
- aggregate: AGG-SUBSCRIPTION
  bc: BC04
  slice: SLC-06
  tier: T3
  label_source: T3 — none (visibility of target governs)
  personal_data: false
- aggregate: AGG-NOTIFICATION
  bc: BC04
  slice: SLC-06
  tier: T3
  label_source: = referenced object label (content never embedded)
  personal_data: false
- aggregate: AGG-ANALYSIS-CASE
  bc: BC03
  slice: SLC-07
  tier: T2 lifecycle; T1 selections
  label_source: explicit (label! in creation command)
  personal_data: false
- aggregate: AGG-ANALYSIS-METHOD
  bc: BC03
  slice: SLC-07
  tier: T2
  label_source: administrative (reference/configuration object)
  personal_data: false
- aggregate: AGG-ANALYSIS-RUN
  bc: BC03
  slice: SLC-07
  tier: T1 results / T2 lifecycle
  label_source: explicit on submit, ≥ max(input labels); reproduction copies source run label — INV-RUN-02
  personal_data: false
- aggregate: AGG-FINDING
  bc: BC03
  slice: SLC-07
  tier: T1
  label_source: explicit (label! in creation command)
  personal_data: false
- aggregate: AGG-ASSESSMENT
  bc: BC03
  slice: SLC-07
  tier: T1 content / T2 lifecycle
  label_source: explicit (label! in creation command)
  personal_data: false
- aggregate: AGG-DECISION-REQUEST
  bc: BC04
  slice: SLC-08
  tier: T2
  label_source: explicit (label! in creation command)
  personal_data: false
- aggregate: AGG-DECISION
  bc: BC04
  slice: SLC-08
  tier: T2
  label_source: explicit (label! in creation command)
  personal_data: false
- aggregate: AGG-PLAN
  bc: BC04
  slice: SLC-08
  tier: T2
  label_source: explicit (label! in creation command)
  personal_data: false
- aggregate: AGG-PLAN-VERSION
  bc: BC04
  slice: SLC-08
  tier: T2
  label_source: = plan label
  personal_data: false
- aggregate: AGG-OUTCOME-TRACKER
  bc: BC04
  slice: SLC-08
  tier: T2
  label_source: = plan label
  personal_data: false
- aggregate: AGG-DEVICE
  bc: BC01
  slice: SLC-11
  tier: T2
  label_source: administrative (tenant default administrative level, INTERNAL unless configured)
  personal_data: false
- aggregate: AGG-PRELOAD-PACKAGE
  bc: BC07
  slice: SLC-11
  tier: T2
  label_source: = requested level (≤ tenant offline max)
  personal_data: false
- aggregate: AGG-SYNC-SESSION
  bc: BC07
  slice: SLC-11
  tier: T2
  label_source: administrative (tenant default)
  personal_data: false
- aggregate: AGG-SYNC-CONFLICT
  bc: BC07
  slice: SLC-11
  tier: T2
  label_source: = target object label
  personal_data: false
- aggregate: AGG-RETENTION-SCHEDULE
  bc: BC08
  slice: SLC-12a
  tier: T2
  label_source: administrative
  personal_data: false
- aggregate: AGG-LEGAL-HOLD
  bc: BC08
  slice: SLC-12a
  tier: T2
  label_source: administrative (Legal)
  personal_data: false
- aggregate: AGG-DISPOSITION-RUN
  bc: BC08
  slice: SLC-12a
  tier: T2
  label_source: administrative
  personal_data: false
- aggregate: AGG-ERASURE-REQUEST
  bc: BC08
  slice: SLC-12a
  tier: T2
  label_source: administrative + personal_data
  personal_data: true
- aggregate: AGG-ASSET
  bc: BC05
  slice: SLC-09
  tier: T2 (location as T1 claims on the linked entity)
  label_source: explicit (label! in creation command)
  personal_data: false
- aggregate: AGG-MAINTENANCE-ORDER
  bc: BC05
  slice: SLC-09
  tier: T2
  label_source: = asset label
  personal_data: false
- aggregate: AGG-ASSET-RESERVATION
  bc: BC05
  slice: SLC-09
  tier: T2
  label_source: explicit (label! in creation command), ≥ asset label
  personal_data: false
- aggregate: AGG-ASSET-ASSIGNMENT
  bc: BC05
  slice: SLC-09
  tier: T2
  label_source: max(asset label, task label)
  personal_data: false
- aggregate: AGG-RESOURCE-POOL
  bc: BC05
  slice: SLC-09
  tier: T2
  label_source: explicit (label! in creation command)
  personal_data: false
- aggregate: AGG-ALLOCATION
  bc: BC05
  slice: SLC-09
  tier: T2
  label_source: max(pool label, target label)
  personal_data: false
- aggregate: AGG-ROLE-REQUIREMENT
  bc: BC05
  slice: SLC-09
  tier: T2
  label_source: administrative
  personal_data: false
- aggregate: AGG-PRODUCT-TEMPLATE
  bc: BC06
  slice: SLC-12
  tier: T2
  label_source: administrative
  personal_data: false
- aggregate: AGG-PRODUCT
  bc: BC06
  slice: SLC-12
  tier: T1 content / T2 lifecycle
  label_source: explicit (label! in creation command), ≥ included content
  personal_data: false
- aggregate: AGG-DISTRIBUTION
  bc: BC06
  slice: SLC-12
  tier: T2
  label_source: = product label
  personal_data: false
- aggregate: AGG-KNOWLEDGE-OBJECT
  bc: BC06
  slice: SLC-12
  tier: T1 content / T2 lifecycle
  label_source: explicit (label! in creation command), ≥ source
  personal_data: false
- aggregate: AGG-ARCHIVE-PACKAGE
  bc: BC06
  slice: SLC-12
  tier: T1
  label_source: = max label of archived records
  personal_data: false
- aggregate: AGG-RECONSTRUCTION
  bc: BC06
  slice: SLC-12
  tier: T2
  label_source: ≥ max label of reported elements (≤ requester clearance)
  personal_data: false
- aggregate: AGG-AI-REQUEST
  bc: BC07
  slice: SLC-10
  tier: T1 (when its output is used) / T2
  label_source: = max(context item labels) ≤ requester clearance
  personal_data: false
- aggregate: AGG-AI-RESULT
  bc: BC07
  slice: SLC-10
  tier: T1
  label_source: = originating request label
  personal_data: false
- aggregate: AGG-MODEL-VERSION
  bc: BC07
  slice: SLC-10
  tier: T2
  label_source: administrative
  personal_data: false
- aggregate: AGG-AI-ROUTING
  bc: BC07
  slice: SLC-10
  tier: T2
  label_source: administrative
  personal_data: false
- aggregate: AGG-AI-TOOL
  bc: BC07
  slice: SLC-10
  tier: T2
  label_source: administrative
  personal_data: false
- aggregate: AGG-EVAL-SUITE
  bc: BC07
  slice: SLC-10
  tier: T2
  label_source: = max label of evaluation items (tenant samples) or administrative
  personal_data: false
- aggregate: AGG-COLLECTION-REQUIREMENT
  bc: BC02
  slice: SLC-14
  tier: T2
  label_source: explicit (label! in creation command)
  personal_data: false
- aggregate: AGG-COLLECTION-PLAN
  bc: BC02
  slice: SLC-14
  tier: T2
  label_source: explicit, ≥ requirements
  personal_data: false
- aggregate: AGG-COORDINATION-CASE
  bc: BC04
  slice: SLC-15
  tier: T2
  label_source: explicit (label! in creation command)
  personal_data: false
- aggregate: AGG-CORRELATION-PROPOSAL
  bc: BC02
  slice: SLC-15
  tier: T2
  label_source: max(input labels)
  personal_data: false
- aggregate: AGG-CORRELATION-RULE
  bc: BC02
  slice: SLC-15
  tier: T2
  label_source: administrative
  personal_data: false
- aggregate: AGG-INTEGRATION-CONNECTION
  bc: BC07
  slice: SLC-16
  tier: T2
  label_source: administrative
  personal_data: false
- aggregate: AGG-SENSOR-STREAM
  bc: BC07
  slice: SLC-16
  tier: T2
  label_source: = source label
  personal_data: false
- aggregate: AGG-HR-SYNC-PROPOSAL
  bc: BC01
  slice: SLC-16
  tier: T2
  label_source: administrative + personal_data
  personal_data: true
- aggregate: AGG-CAP-MESSAGE
  bc: BC03
  slice: SLC-16
  tier: T2
  label_source: = alert label (must be ≤ external release level)
  personal_data: false
- aggregate: AGG-RISK
  bc: BC04
  slice: SLC-17
  tier: T2
  label_source: explicit (label! in creation command)
  personal_data: false
- aggregate: AGG-INCIDENT
  bc: BC04
  slice: SLC-17
  tier: T1
  label_source: explicit (label! in creation command)
  personal_data: false
```

</details>
