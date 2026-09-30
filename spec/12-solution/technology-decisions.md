---
id: TECH-DECISIONS
type: technology-decisions
title: Technology Decisions (W8) — from workload and capability evidence
wave: W8
tier: T0
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
traces:
  decides:
  - ADR-P05
  inputs:
  - W8-INPUTS
  corrects:
  - CR-21
notes: كل اختيار مربوط بدليل عبء أو قدرة من الشرائح، مع ترخيص قابل للتشغيل في بيئة معزولة ومُحفّز مراجعة صريح. الأرقام تقديرية
  حتى القياس في Pilot.
---

# Technology Decisions (W8) — from workload and capability evidence

> كل اختيار مربوط بدليل عبء أو قدرة من الشرائح، مع ترخيص قابل للتشغيل في بيئة معزولة ومُحفّز مراجعة صريح. الأرقام تقديرية حتى القياس في Pilot.

## decisions

_19 items_

### TD-01

- **capability:** Operational store (all contexts)
- **decision:** PostgreSQL 16+ with PostGIS, btree_gist, range types (tstzrange), RLS, declarative partitioning; one cluster per cell (CloudNativePG operator); schema + role per context
- **options_considered:** PostgreSQL only · distributed SQL (CockroachDB/Yugabyte) · per-context separate engines
- **evidence:** LIB §6 (bitemporal intervals + exclusion constraints), LDM-SLC02 (partitioning, spatial per partition), ADR-P04 (RLS), WL-01 (design 5,000 concurrent)
- **license:** PostgreSQL License
- **reversal_trigger:** Single-cell primary write utilisation > 70 % in pilot or projected at envelope → move busiest contexts (BC02 ingestion) to their own cluster (schemas/roles already separate)

### TD-02

- **capability:** Search projection
- **decision:** OpenSearch (Apache 2.0) — nested fact documents, Arabic analyzer + custom char filters (N1–N8), geo, index aliases, search_after cursors; separate cluster from observability logs
- **options_considered:** PostgreSQL FTS + pgvector · OpenSearch · Elasticsearch (licence) · Solr
- **evidence:** SPEC-DISCOVERY §8: fact-level nested filtering applied before scoring/counting/faceting is a functional requirement (P-51..P-53), not only a load one; plus 500 q/s on 1e8 facts (WL-02a)
- **license:** Apache 2.0
- **reversal_trigger:** Decided by capability (RSK-022 resolved): revisit only if OpenSearch cannot meet QAS-PERF-003 in pilot

### TD-03

- **capability:** Graph projection
- **decision:** No graph database in R1: relationship projection tables in PostgreSQL + bounded recursive queries (depth ≤ 3, paths ≤ 4) with visibility filters applied per hop
- **options_considered:** Neo4j (PRJ§77) · Apache AGE · PostgreSQL recursive CTE
- **evidence:** WL-08e: ≈ 20 graph q/s, depth ≤ 3; SR-10 (no component before measured need)
- **license:** —
- **reversal_trigger:** QAS-PERF-018 (p95 ≤ 1 s depth 2) missed at pilot volume, or visible fan-out > 500 common → evaluate dedicated graph engine (projection is rebuildable, low switching cost)

### TD-04

- **capability:** Event log / bus
- **decision:** Apache Kafka (KRaft, Apache 2.0) per cell, operated by Strimzi; transactional outbox relayed by CDC (Debezium) ; dedicated high-priority topic for security.versions
- **options_considered:** PostgreSQL outbox polling only · NATS JetStream · Apache Kafka
- **evidence:** WL-06a (5,000/s sustained, 50,000/s bursts 60 s), many independent consumers with replay (projections, evaluators, sync), partition-key ordering in every AsyncAPI contract (tenant + aggregate)
- **license:** Apache 2.0
- **reversal_trigger:** NATS JetStream kept as documented alternative if pilot shows Kafka ops burden unacceptable for the operations team (ASM-008)

### TD-05

- **capability:** Runtime platform
- **decision:** Kubernetes (RKE2 distribution, air-gap install supported) with operators for stateful services; one cluster per cell
- **options_considered:** VMs + systemd · Docker Compose · Kubernetes
- **evidence:** cells + shared/dedicated/sovereign profiles from one release (PLT-002), air-gapped install/upgrade with rollback (QAS-OPS-001), ≥ 15 deployment units + 8 stateful services, horizontal scaling (SR-01), job queueing (TD-12)
- **license:** Apache 2.0
- **reversal_trigger:** — (CR-21: now justified by W8 evidence, not assumed)

### TD-06

- **capability:** Object storage
- **decision:** S3-compatible API as the contract; default implementation Ceph RGW (sites with Ceph) or MinIO (smaller cells); Object Lock (WORM) for audit anchors and key-destruction log copies
- **options_considered:** MinIO · Ceph RGW · file system
- **evidence:** SR-05 direct signed transfers, PB-class design (WL-05a), WORM anchors (audit-architecture), backups
- **license:** Ceph: LGPL · MinIO: AGPL (legal review, DEP-HUM-004)
- **reversal_trigger:** —

### TD-07

- **capability:** Key management
- **decision:** OpenBao (MPL, open fork of Vault) Transit engine for envelope encryption; KEKs in site HSM via PKCS#11; DEKs wrapped in PostgreSQL key store; destruction log append-only + WORM copy
- **options_considered:** HashiCorp Vault (BSL) · OpenBao · cloud KMS (not allowed air-gapped)
- **evidence:** SPEC-KEYS-DISPOSITION (millions of DEKs, restore gate), FM-S01-08
- **license:** MPL 2.0
- **reversal_trigger:** HSM vendor chosen per site

### TD-08

- **capability:** Policy engine
- **decision:** Open Policy Agent: decision tables compiled to Rego; signed bundles; embedded evaluation (WASM/library) in each unit; partial evaluation produces allowed_scope filters for search/lists
- **options_considered:** OPA · Cedar · custom interpreter
- **evidence:** QAS-PERF-009 (10,000 decisions/s, p95 ≤ 5 ms embedded), ADR-P06 allowed_scope pre-filter, ADR-P11
- **license:** Apache 2.0
- **reversal_trigger:** —

### TD-09

- **capability:** Identity broker
- **decision:** Keycloak per cell as OIDC/SAML federation broker to tenant IdPs; SCIM via provisioning service in BC01
- **options_considered:** Keycloak · direct IdP integration per service
- **evidence:** REQ-FND-005, air-gapped, multi-tenant realms
- **license:** Apache 2.0
- **reversal_trigger:** —

### TD-10

- **capability:** Maps & tiles
- **decision:** Dynamic operational vector tiles from PostGIS (ST_AsMVT) via Martin tile server with scope-keyed cache; base maps as PMTiles in object storage; raster COG via TiTiler; OGC API Features/Tiles via pygeoapi for exchange; MapLibre GL JS / Native on clients
- **options_considered:** GeoServer · Martin + PostGIS · pre-rendered only
- **evidence:** SPEC-SITUATION §5 (per-scope tiles, ≈ 2,000 tiles/s), ADR-P12, REQ-INF-008
- **license:** Martin: Apache/MIT · TiTiler: MIT · pygeoapi: MIT · MapLibre: BSD
- **reversal_trigger:** GeoServer if OGC WMS/WFS publishing breadth becomes a requirement (R2)

### TD-11

- **capability:** Cache / key-value
- **decision:** Valkey (BSD) for security-version replicas and caches; authoritative values stay in PostgreSQL (BC01)
- **options_considered:** Redis (licence change 2024) · Valkey · PostgreSQL only
- **evidence:** WL-01c (7,500 lookups/s, p99 ≤ 2 ms), QAS-SEC-003
- **license:** BSD
- **reversal_trigger:** —

### TD-12

- **capability:** Batch compute
- **decision:** Kubernetes Jobs with Kueue (fair sharing, per-tenant quotas); images from internal Harbor registry, signed (cosign) and digest-pinned
- **options_considered:** custom workers · Kueue · Airflow
- **evidence:** WL-11b, QAS-PERF-020, SPEC-ANALYSIS §3 (digest-pinned environments)
- **license:** Apache 2.0
- **reversal_trigger:** —

### TD-13

- **capability:** Timers & schedulers
- **decision:** PostgreSQL time buckets + leased workers inside owning units (no workflow engine)
- **options_considered:** Temporal · Quartz · PG buckets
- **evidence:** task-lifecycle-rules §3, SR-10
- **license:** —
- **reversal_trigger:** Adopt a workflow engine only if multi-step sagas beyond provisioning appear (R2+)

### TD-14

- **capability:** Observability
- **decision:** OpenTelemetry SDK + Collector; VictoriaMetrics (metrics), VictoriaLogs (logs), Jaeger (traces), Grafana dashboards; OpenCost for per-tenant cost allocation
- **options_considered:** Prometheus+Thanos · Grafana LGTM (AGPL) · Victoria* + Jaeger
- **evidence:** observability-slc* (≈ 70 signals), QAS-OBS-001, REQ-PLT-013
- **license:** Apache 2.0 (Grafana AGPL: unmodified, legal review)
- **reversal_trigger:** —

### TD-15

- **capability:** Service implementation
- **decision:** TypeScript on Node.js for services (DOC: PRJ§77); Python for analysis methods and raster/geo processing; generated contracts drive server stubs and clients
- **options_considered:** TypeScript · Kotlin/JVM · Go
- **evidence:** PRJ§77 (documented choice, no contrary evidence); contracts are language-neutral; OPA WASM available for Node
- **license:** —
- **reversal_trigger:** Hot paths failing QAS-PERF-001/013 in pilot may be re-implemented in Go behind the same contracts

### TD-16

- **capability:** Clients
- **decision:** Web: React + MapLibre GL JS, i18n with ICU messages, RTL via CSS logical properties, Hijri display via Intl (islamic-umalqura). Mobile field app: React Native with SQLCipher-encrypted SQLite, hardware-backed keystore, MapLibre Native
- **options_considered:** native iOS/Android · Flutter · React Native
- **evidence:** REQ-PLT-010/011, SPEC-FIELD-SYNC (encrypted store, signed queue), shared TypeScript contracts
- **license:** MIT/BSD
- **reversal_trigger:** Native modules for attestation and secure storage where RN libraries are insufficient

### TD-17

- **capability:** Delivery & supply chain
- **decision:** Signed images (cosign) + SBOM (Syft); offline bundles with Zarf (air-gapped install/upgrade/rollback); GitOps with Argo CD inside each site; internal Harbor registry; forward-only DB migrations (expand/contract)
- **options_considered:** manual installs · Helm only · Zarf + Argo CD
- **evidence:** QAS-OPS-001, REQ-PLT-001/002, FIT-12, THR-019
- **license:** Apache 2.0
- **reversal_trigger:** —

### TD-18

- **capability:** LLM inference serving (R2)
- **decision:** vLLM (Apache 2.0) on a per-cell GPU pool; open-weight models with Arabic support chosen by evaluation (AGG-MODEL-VERSION); batch jobs via Kueue
- **options_considered:** vLLM · TGI · cloud APIs (not allowed air-gapped)
- **evidence:** SLC-10 SPEC-AI §7, QAS-AI-003, W1 Q28 (local by default)
- **license:** Apache 2.0
- **reversal_trigger:** GPU pool size after R1 pilot (UNK-012); switch server if QAS-AI-003 missed

### TD-19

- **capability:** Vector retrieval (R2)
- **decision:** OpenSearch k-NN on the existing search cluster (vector projection kind) — no new component; pgvector as fallback for small cells
- **options_considered:** dedicated vector DB · OpenSearch k-NN · pgvector
- **evidence:** SR-10 (no new component without need); same label pre-filtering as search (ADR-P06)
- **license:** Apache 2.0
- **reversal_trigger:** dedicated vector store only if recall/latency targets fail at pilot volume

## removed_from_PRJ_baseline

- Neo4j (no graph workload justifying it — TD-03)
- Redis (licence; replaced by Valkey — TD-11)

## added_vs_PRJ_baseline

- Kubernetes justified by cells, air-gapped upgrades and operators (TD-05)
- OPA (TD-08)
- OpenBao + HSM (TD-07)
- Kueue + Harbor (TD-12)
- Zarf + Argo CD (TD-17)

## license_review_required

- MinIO (AGPL)
- Grafana (AGPL)
- HSM vendor terms
- all components — DEP-HUM-004 before G8

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
decisions:
- id: TD-01
  capability: Operational store (all contexts)
  decision: PostgreSQL 16+ with PostGIS, btree_gist, range types (tstzrange), RLS, declarative partitioning; one cluster per
    cell (CloudNativePG operator); schema + role per context
  options_considered: PostgreSQL only · distributed SQL (CockroachDB/Yugabyte) · per-context separate engines
  evidence: LIB §6 (bitemporal intervals + exclusion constraints), LDM-SLC02 (partitioning, spatial per partition), ADR-P04
    (RLS), WL-01 (design 5,000 concurrent)
  license: PostgreSQL License
  reversal_trigger: Single-cell primary write utilisation > 70 % in pilot or projected at envelope → move busiest contexts
    (BC02 ingestion) to their own cluster (schemas/roles already separate)
- id: TD-02
  capability: Search projection
  decision: OpenSearch (Apache 2.0) — nested fact documents, Arabic analyzer + custom char filters (N1–N8), geo, index aliases,
    search_after cursors; separate cluster from observability logs
  options_considered: PostgreSQL FTS + pgvector · OpenSearch · Elasticsearch (licence) · Solr
  evidence: 'SPEC-DISCOVERY §8: fact-level nested filtering applied before scoring/counting/faceting is a functional requirement
    (P-51..P-53), not only a load one; plus 500 q/s on 1e8 facts (WL-02a)'
  license: Apache 2.0
  reversal_trigger: 'Decided by capability (RSK-022 resolved): revisit only if OpenSearch cannot meet QAS-PERF-003 in pilot'
- id: TD-03
  capability: Graph projection
  decision: 'No graph database in R1: relationship projection tables in PostgreSQL + bounded recursive queries (depth ≤ 3,
    paths ≤ 4) with visibility filters applied per hop'
  options_considered: Neo4j (PRJ§77) · Apache AGE · PostgreSQL recursive CTE
  evidence: 'WL-08e: ≈ 20 graph q/s, depth ≤ 3; SR-10 (no component before measured need)'
  license: —
  reversal_trigger: QAS-PERF-018 (p95 ≤ 1 s depth 2) missed at pilot volume, or visible fan-out > 500 common → evaluate dedicated
    graph engine (projection is rebuildable, low switching cost)
- id: TD-04
  capability: Event log / bus
  decision: Apache Kafka (KRaft, Apache 2.0) per cell, operated by Strimzi; transactional outbox relayed by CDC (Debezium)
    ; dedicated high-priority topic for security.versions
  options_considered: PostgreSQL outbox polling only · NATS JetStream · Apache Kafka
  evidence: WL-06a (5,000/s sustained, 50,000/s bursts 60 s), many independent consumers with replay (projections, evaluators,
    sync), partition-key ordering in every AsyncAPI contract (tenant + aggregate)
  license: Apache 2.0
  reversal_trigger: NATS JetStream kept as documented alternative if pilot shows Kafka ops burden unacceptable for the operations
    team (ASM-008)
- id: TD-05
  capability: Runtime platform
  decision: Kubernetes (RKE2 distribution, air-gap install supported) with operators for stateful services; one cluster per
    cell
  options_considered: VMs + systemd · Docker Compose · Kubernetes
  evidence: cells + shared/dedicated/sovereign profiles from one release (PLT-002), air-gapped install/upgrade with rollback
    (QAS-OPS-001), ≥ 15 deployment units + 8 stateful services, horizontal scaling (SR-01), job queueing (TD-12)
  license: Apache 2.0
  reversal_trigger: '— (CR-21: now justified by W8 evidence, not assumed)'
- id: TD-06
  capability: Object storage
  decision: S3-compatible API as the contract; default implementation Ceph RGW (sites with Ceph) or MinIO (smaller cells);
    Object Lock (WORM) for audit anchors and key-destruction log copies
  options_considered: MinIO · Ceph RGW · file system
  evidence: SR-05 direct signed transfers, PB-class design (WL-05a), WORM anchors (audit-architecture), backups
  license: 'Ceph: LGPL · MinIO: AGPL (legal review, DEP-HUM-004)'
  reversal_trigger: —
- id: TD-07
  capability: Key management
  decision: OpenBao (MPL, open fork of Vault) Transit engine for envelope encryption; KEKs in site HSM via PKCS#11; DEKs wrapped
    in PostgreSQL key store; destruction log append-only + WORM copy
  options_considered: HashiCorp Vault (BSL) · OpenBao · cloud KMS (not allowed air-gapped)
  evidence: SPEC-KEYS-DISPOSITION (millions of DEKs, restore gate), FM-S01-08
  license: MPL 2.0
  reversal_trigger: HSM vendor chosen per site
- id: TD-08
  capability: Policy engine
  decision: 'Open Policy Agent: decision tables compiled to Rego; signed bundles; embedded evaluation (WASM/library) in each
    unit; partial evaluation produces allowed_scope filters for search/lists'
  options_considered: OPA · Cedar · custom interpreter
  evidence: QAS-PERF-009 (10,000 decisions/s, p95 ≤ 5 ms embedded), ADR-P06 allowed_scope pre-filter, ADR-P11
  license: Apache 2.0
  reversal_trigger: —
- id: TD-09
  capability: Identity broker
  decision: Keycloak per cell as OIDC/SAML federation broker to tenant IdPs; SCIM via provisioning service in BC01
  options_considered: Keycloak · direct IdP integration per service
  evidence: REQ-FND-005, air-gapped, multi-tenant realms
  license: Apache 2.0
  reversal_trigger: —
- id: TD-10
  capability: Maps & tiles
  decision: Dynamic operational vector tiles from PostGIS (ST_AsMVT) via Martin tile server with scope-keyed cache; base maps
    as PMTiles in object storage; raster COG via TiTiler; OGC API Features/Tiles via pygeoapi for exchange; MapLibre GL JS
    / Native on clients
  options_considered: GeoServer · Martin + PostGIS · pre-rendered only
  evidence: SPEC-SITUATION §5 (per-scope tiles, ≈ 2,000 tiles/s), ADR-P12, REQ-INF-008
  license: 'Martin: Apache/MIT · TiTiler: MIT · pygeoapi: MIT · MapLibre: BSD'
  reversal_trigger: GeoServer if OGC WMS/WFS publishing breadth becomes a requirement (R2)
- id: TD-11
  capability: Cache / key-value
  decision: Valkey (BSD) for security-version replicas and caches; authoritative values stay in PostgreSQL (BC01)
  options_considered: Redis (licence change 2024) · Valkey · PostgreSQL only
  evidence: WL-01c (7,500 lookups/s, p99 ≤ 2 ms), QAS-SEC-003
  license: BSD
  reversal_trigger: —
- id: TD-12
  capability: Batch compute
  decision: Kubernetes Jobs with Kueue (fair sharing, per-tenant quotas); images from internal Harbor registry, signed (cosign)
    and digest-pinned
  options_considered: custom workers · Kueue · Airflow
  evidence: WL-11b, QAS-PERF-020, SPEC-ANALYSIS §3 (digest-pinned environments)
  license: Apache 2.0
  reversal_trigger: —
- id: TD-13
  capability: Timers & schedulers
  decision: PostgreSQL time buckets + leased workers inside owning units (no workflow engine)
  options_considered: Temporal · Quartz · PG buckets
  evidence: task-lifecycle-rules §3, SR-10
  license: —
  reversal_trigger: Adopt a workflow engine only if multi-step sagas beyond provisioning appear (R2+)
- id: TD-14
  capability: Observability
  decision: OpenTelemetry SDK + Collector; VictoriaMetrics (metrics), VictoriaLogs (logs), Jaeger (traces), Grafana dashboards;
    OpenCost for per-tenant cost allocation
  options_considered: Prometheus+Thanos · Grafana LGTM (AGPL) · Victoria* + Jaeger
  evidence: observability-slc* (≈ 70 signals), QAS-OBS-001, REQ-PLT-013
  license: 'Apache 2.0 (Grafana AGPL: unmodified, legal review)'
  reversal_trigger: —
- id: TD-15
  capability: Service implementation
  decision: 'TypeScript on Node.js for services (DOC: PRJ§77); Python for analysis methods and raster/geo processing; generated
    contracts drive server stubs and clients'
  options_considered: TypeScript · Kotlin/JVM · Go
  evidence: PRJ§77 (documented choice, no contrary evidence); contracts are language-neutral; OPA WASM available for Node
  license: —
  reversal_trigger: Hot paths failing QAS-PERF-001/013 in pilot may be re-implemented in Go behind the same contracts
- id: TD-16
  capability: Clients
  decision: 'Web: React + MapLibre GL JS, i18n with ICU messages, RTL via CSS logical properties, Hijri display via Intl (islamic-umalqura).
    Mobile field app: React Native with SQLCipher-encrypted SQLite, hardware-backed keystore, MapLibre Native'
  options_considered: native iOS/Android · Flutter · React Native
  evidence: REQ-PLT-010/011, SPEC-FIELD-SYNC (encrypted store, signed queue), shared TypeScript contracts
  license: MIT/BSD
  reversal_trigger: Native modules for attestation and secure storage where RN libraries are insufficient
- id: TD-17
  capability: Delivery & supply chain
  decision: Signed images (cosign) + SBOM (Syft); offline bundles with Zarf (air-gapped install/upgrade/rollback); GitOps
    with Argo CD inside each site; internal Harbor registry; forward-only DB migrations (expand/contract)
  options_considered: manual installs · Helm only · Zarf + Argo CD
  evidence: QAS-OPS-001, REQ-PLT-001/002, FIT-12, THR-019
  license: Apache 2.0
  reversal_trigger: —
- id: TD-18
  capability: LLM inference serving (R2)
  decision: vLLM (Apache 2.0) on a per-cell GPU pool; open-weight models with Arabic support chosen by evaluation (AGG-MODEL-VERSION);
    batch jobs via Kueue
  options_considered: vLLM · TGI · cloud APIs (not allowed air-gapped)
  evidence: SLC-10 SPEC-AI §7, QAS-AI-003, W1 Q28 (local by default)
  license: Apache 2.0
  reversal_trigger: GPU pool size after R1 pilot (UNK-012); switch server if QAS-AI-003 missed
- id: TD-19
  capability: Vector retrieval (R2)
  decision: OpenSearch k-NN on the existing search cluster (vector projection kind) — no new component; pgvector as fallback
    for small cells
  options_considered: dedicated vector DB · OpenSearch k-NN · pgvector
  evidence: SR-10 (no new component without need); same label pre-filtering as search (ADR-P06)
  license: Apache 2.0
  reversal_trigger: dedicated vector store only if recall/latency targets fail at pilot volume
removed_from_PRJ_baseline:
- Neo4j (no graph workload justifying it — TD-03)
- Redis (licence; replaced by Valkey — TD-11)
added_vs_PRJ_baseline:
- Kubernetes justified by cells, air-gapped upgrades and operators (TD-05)
- OPA (TD-08)
- OpenBao + HSM (TD-07)
- Kueue + Harbor (TD-12)
- Zarf + Argo CD (TD-17)
license_review_required:
- MinIO (AGPL)
- Grafana (AGPL)
- HSM vendor terms
- all components — DEP-HUM-004 before G8
```

</details>
