---
id: CLAIM-EVIDENCE-MODEL
type: information-model
title: Claim, Evidence, Source & Observation Model
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
wave: W3
tier: T0
traces: {requirements: [REQ-INF-001, REQ-INF-002, REQ-INF-021, REQ-INF-024, REQ-INF-027, REQ-INF-037], corrects: [CR-31]}
---

# Claim, Evidence, Source & Observation Model

## 1. Claim

```text
Claim
  id, urn, tenant_id
  subject_ref        URN of Entity | RealWorldEvent | Relationship
  predicate          code from RD-PREDICATES (defines value type, cardinality single|multi, unit family, freshness threshold)
  value              typed: string | number(+unit, UCUM) | date/fuzzyInterval | geometry | enum(code) | ref(URN)
  valid              [valid_from, valid_to)
  record             [recorded_from, recorded_to)       server-assigned
  source_refs[]      ≥ 1 (REQ-INF-037)
  evidence_links[]   0..n → EvidenceLink
  confidence         7 dimensions (confidence-model.md)
  status             ASSERTED | CORROBORATED | DISPUTED | RETRACTED
  asserted_by        user | adapter | analysis run | AI result (with lineage)
  security           level, compartments, caveats, personal_data
```

- الادعاء **لا يُعدل**. التصحيح والسحب يغلقان `recorded_to` فقط (temporal-model §3).
- `CORROBORATED` و`DISPUTED` حالات مشتقة تُحسب في الإسقاط، ولا تُكتب على السجل الأصلي.
- الادعاء قد يكون أعلى تصنيفاً من موضوعه: يمكن معرفة الكيان وحجب سمة منه.

## 2. Relationship

العلاقة كائن مستقل (PRJ§3.3) **ووجودها نفسه ادعاء**: `(source_entity, relationship_type, target_ref)` مع فترتي زمن ومصدر وأدلة وثقة وتصنيف. سمات العلاقة (مثل الدور) ادعاءات موضوعها العلاقة.

## 3. Evidence (مالك واحد: BC02 / DOM-03 — CR-31)

```text
Evidence
  id, urn, type        document | image | video | audio | measurement | dataset | testimony | observation_ref
  attachment_ref       content hash in object storage (REQ-INF-003)
  locator              page | bbox | time offset | row range   (يحدد الجزء الدال داخل الملف)
  source_ref
  collected_at, collected_by
  custody_chain[]      {holder, from, to, action}
  integrity_hash
  security

EvidenceLink
  evidence_ref, claim_ref
  stance               SUPPORTS | REFUTES | CONTEXT
  note, linked_by, recorded_from
```

DOM-06 (Observation & Field) **يستخدم** Evidence بالمرجع: الملاحظة الميدانية مع صورها تنتج Evidence من نوع `observation_ref`.

## 4. Source

```text
Source
  id, urn, type        person | organization | sensor | system | publication | open_source | analyst
  name (language-model forms), owner_org
  reliability          A–F (Admiralty scale, RD-SOURCE-RELIABILITY) — bitemporal claim on the source
  access_restrictions, protection_level     (حماية هوية المصدر البشري)
  security
```

**حماية المصادر:** هوية المصدر من نوع person تُصنف افتراضياً أعلى من المعلومة التي قدمها. المستخدم قد يرى الادعاء وموثوقية مصدره (مثلاً B) دون هوية المصدر.

## 5. Observation

```text
Observation
  id, urn, observer_ref, source_ref, device_ref?, field_session_ref?
  observed_at, event_time?, recorded_from (server)
  location (spatial envelope, accuracy required)
  method                visual | sensor | measurement | report | imagery_analysis
  measurements[]        {quantity code, value, unit (UCUM), uncertainty}
  narrative             text (language-model forms)
  attachments[]         → Evidence
  derived_claims[]      claims asserted from this observation (lineage)
  lifecycle             RECORDED → VALIDATED | REJECTED   (immutable after VALIDATED)
```

الملاحظة سجل ما رُصد؛ **الادعاءات هي ما نستنتجه منها**. "رأيت شاحنة حمراء عند X" ملاحظة؛ "الأصل Y موجود عند X" ادعاء مشتق منها ومرتبط بها.

## 6. سلسلة الإسناد (Provenance chain)

```text
Source ─produces→ Observation ─evidences→ Evidence ─supports→ Claim ─about→ Entity
                        └──────────── derived_claims ─────────────┘
Claim ─input→ Analysis Run ─produces→ Finding ─→ Assessment ─→ Decision
```
