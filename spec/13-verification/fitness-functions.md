---
id: FITNESS-FUNCTIONS
type: fitness-model
title: Architecture Fitness Functions
wave: W3
tier: T0
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
notes: كل مبدأ معماري مهم → قاعدة → آلية تحقق → شدة. المخالفة ERROR تكسر البناء؛ الاستثناء يتطلب ADR (V5§82).
---

# Architecture Fitness Functions

> كل مبدأ معماري مهم → قاعدة → آلية تحقق → شدة. المخالفة ERROR تكسر البناء؛ الاستثناء يتطلب ADR (V5§82).

## fitness_functions

_20 items_ (FIT-20 added with ADR-P17/P18, 2026-09-30)

| id | rule | from | verification | severity |
|---|---|---|---|---|
| FIT-01 | No cross-context data store access | SA-003; BRL-014 | static analysis of connection configs + DB grants per context | ERROR |
| FIT-02 | tenant_id present in every table, partition key, index doc, event and object path | ADR-P04; SR-02 | schema lint + projection lint | ERROR |
| FIT-03 | Every retrieval path passes a PEP before data access | REQ-FND-010; ADR-P06 | call-graph test: no repository/search call without prior policy decision in trace | ERROR |
| FIT-04 | State change, audit record and outbox entry commit atomically | ADR-P02; audit §1 | fault-injection test at commit | ERROR |
| FIT-05 | T1 claims are never updated in place except closing recorded_to | ADR-P01; REQ-INF-024 | DB trigger/permission check + test | ERROR |
| FIT-06 | Every attribute declares importance tier | ADR-P03; SL-10 | schema lint | ERROR |
| FIT-07 | Identifiers are ULID + URN; no id rewrite on merge | ADR-P13 | schema lint + ER tests | ERROR |
| FIT-08 | Every geometry has CRS and accuracy; canonical EPSG:4326 | ADR-P16; SL-12 | schema lint + ingestion tests | ERROR |
| FIT-09 | No created_at/updated_at used as business time | SL-11 | schema + query lint | ERROR |
| FIT-10 | Domain layer has no dependency on HTTP, DB, broker, UI frameworks | PRJ§68 | dependency rule test | ERROR |
| FIT-11 | Projections rebuildable: rebuild yields identical results on reference set | REQ-SRC-004 | scheduled rebuild test | ERROR |
| FIT-12 | No external network dependency at runtime or build (air-gapped) | REQ-PLT-001 | isolated-network CI stage | ERROR |
| FIT-13 | No list API with offset pagination | SR-12 | OpenAPI lint | ERROR |
| FIT-14 | No breaking contract change without new major version | REQ-PLT-007 | contract compatibility check | ERROR |
| FIT-15 | No last-write-wins merge for T1/T2 in sync | ADR-P09 | sync test suite | ERROR |
| FIT-16 | Policy engine failure denies | REQ-FND-013 | chaos test | ERROR |
| FIT-17 | Aggregates with > 7 internal entities need ADR | SL-24 | model lint | WARNING |
| FIT-18 | No new infrastructure component without workload evidence + ADR | SR-10 | dependency manifest review | WARNING |
| FIT-19 | Restore gate: after any key-store restore, every key in the destruction log is unusable before services start | CR-51; QAS-PRV-002 | scheduled restore drill | ERROR |
| FIT-20 | Hexagonal dependency rules: domain imports nothing outside shared-kernel; no contexts→contexts, services→services or cross-schema migration dependencies; commands reach aggregates only through the command pipeline | ADR-P17; ADR-P18 | static dependency analysis in CI over the module graph + migration path lint | ERROR |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
fitness_functions:
- id: FIT-01
  rule: No cross-context data store access
  from: SA-003; BRL-014
  verification: static analysis of connection configs + DB grants per context
  severity: ERROR
- id: FIT-02
  rule: tenant_id present in every table, partition key, index doc, event and object path
  from: ADR-P04; SR-02
  verification: schema lint + projection lint
  severity: ERROR
- id: FIT-03
  rule: Every retrieval path passes a PEP before data access
  from: REQ-FND-010; ADR-P06
  verification: 'call-graph test: no repository/search call without prior policy decision in trace'
  severity: ERROR
- id: FIT-04
  rule: State change, audit record and outbox entry commit atomically
  from: ADR-P02; audit §1
  verification: fault-injection test at commit
  severity: ERROR
- id: FIT-05
  rule: T1 claims are never updated in place except closing recorded_to
  from: ADR-P01; REQ-INF-024
  verification: DB trigger/permission check + test
  severity: ERROR
- id: FIT-06
  rule: Every attribute declares importance tier
  from: ADR-P03; SL-10
  verification: schema lint
  severity: ERROR
- id: FIT-07
  rule: Identifiers are ULID + URN; no id rewrite on merge
  from: ADR-P13
  verification: schema lint + ER tests
  severity: ERROR
- id: FIT-08
  rule: Every geometry has CRS and accuracy; canonical EPSG:4326
  from: ADR-P16; SL-12
  verification: schema lint + ingestion tests
  severity: ERROR
- id: FIT-09
  rule: No created_at/updated_at used as business time
  from: SL-11
  verification: schema + query lint
  severity: ERROR
- id: FIT-10
  rule: Domain layer has no dependency on HTTP, DB, broker, UI frameworks
  from: PRJ§68
  verification: dependency rule test
  severity: ERROR
- id: FIT-11
  rule: 'Projections rebuildable: rebuild yields identical results on reference set'
  from: REQ-SRC-004
  verification: scheduled rebuild test
  severity: ERROR
- id: FIT-12
  rule: No external network dependency at runtime or build (air-gapped)
  from: REQ-PLT-001
  verification: isolated-network CI stage
  severity: ERROR
- id: FIT-13
  rule: No list API with offset pagination
  from: SR-12
  verification: OpenAPI lint
  severity: ERROR
- id: FIT-14
  rule: No breaking contract change without new major version
  from: REQ-PLT-007
  verification: contract compatibility check
  severity: ERROR
- id: FIT-15
  rule: No last-write-wins merge for T1/T2 in sync
  from: ADR-P09
  verification: sync test suite
  severity: ERROR
- id: FIT-16
  rule: Policy engine failure denies
  from: REQ-FND-013
  verification: chaos test
  severity: ERROR
- id: FIT-17
  rule: Aggregates with > 7 internal entities need ADR
  from: SL-24
  verification: model lint
  severity: WARNING
- id: FIT-18
  rule: No new infrastructure component without workload evidence + ADR
  from: SR-10
  verification: dependency manifest review
  severity: WARNING
- id: FIT-19
  rule: 'Restore gate: after any key-store restore, every key in the destruction log is unusable before services start'
  from: CR-51; QAS-PRV-002
  verification: scheduled restore drill
  severity: ERROR
- id: FIT-20
  rule: 'Hexagonal dependency rules: domain imports nothing outside shared-kernel; no contexts→contexts, services→services
    or cross-schema migration dependencies; commands reach aggregates only through the command pipeline'
  from: ADR-P17; ADR-P18
  verification: static dependency analysis in CI over the module graph + migration path lint
  severity: ERROR
```

</details>
