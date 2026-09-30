---
id: ADR-P05
type: adr
title: Initial Technology Footprint
status: APPROVED_DELEGATED
wave: W8
deciders: HAP-08
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
blocked_by:
- WL-02
- WL-06
- WL-08
- UNK-003
- UNK-012
corrects:
- CR-21
verified_by:
- PERF-TEST-STRATEGY
- FIT-18
---

# ADR-P05: Initial Technology Footprint

## Context and Problem
PRJ§77 يختار Kafka وOpenSearch وNeo4j وRedis وKubernetes قبل أي نموذج أعباء عمل (يخالف A13).

## Considered Options
1. PostgreSQL/PostGIS كنواة (FTS، pgvector، استعلامات عودية) + Object Storage، والتوسع عند الإثبات
2. الحزمة الكاملة من البداية

## Initial Engineering Leaning (NOT a decision — V6 rule 75)
الخيار 1، وينقلب إن أظهر WL-06 أو WL-08 أحمالاً عالية.

## W1 Input (delegated answers)
Q20,Q22 + SR-10 → الخيار 1 مع مسار توسع مثبت — يُعتمد رسمياً في W3.

## Decision Outcome
**Neither option as stated. Evidence-based footprint (TECH-DECISIONS TD-01..TD-17):**
- **Kept from option 1:** PostgreSQL/PostGIS as the single operational store (all contexts, schema per context); **no graph database** in R1 (bounded recursive queries); timers in PostgreSQL; Valkey only as a cache of authoritative PostgreSQL values.
- **Added because slice evidence requires it:** OpenSearch (fact-level nested pre-filtering is a *functional* requirement of SPEC-DISCOVERY), Kafka KRaft (50,000/s bursts, replayable multi-consumer streams), Kubernetes (cells, air-gapped upgrades with rollback, operators), OPA, OpenBao + HSM, Kueue, Harbor, Zarf.
- **Removed from PRJ§77:** Neo4j, Redis (licence).

## Rationale
A13 / SR-10: every component traces to a workload or capability in `12-solution/w8-inputs.md`; each has an explicit reversal trigger.

## Consequences
- ✅ Every component justified by evidence; air-gapped and licence-compatible
- ✅ Graph and workflow engines avoided until measured need
- ⚠️ Operational footprint is substantial (8 stateful services per cell) — mitigated by operators and GitOps; ops team size (UNK-012) must be confirmed before G8
- ⚠️ All sizing is estimated until the performance tests (PERF-TEST-STRATEGY)

## Impact
- **operations:** operators (CloudNativePG, Strimzi, OpenSearch), Zarf, Argo CD
- **cost:** COST-MODEL (measured, not estimated)
- **security:** licence review (DEP-HUM-004)

## Verified By
PERF-TEST-STRATEGY, FIT-18

## Previously Blocked By
WL-02, WL-06, WL-08, UNK-003, UNK-012
