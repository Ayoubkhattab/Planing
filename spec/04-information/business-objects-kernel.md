---
id: BO-CATALOG-KERNEL
type: business-object-catalog
title: Business Object Catalog — Information Kernel (BC02)
wave: W3
tier: T0
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
notes: قالب V5§50 مختصر للنواة. التفاصيل الكاملة للسمات والأوامر في W4 (SLC-02، SLC-04).
---

# Business Object Catalog — Information Kernel (BC02)

> قالب V5§50 مختصر للنواة. التفاصيل الكاملة للسمات والأوامر في W4 (SLC-02، SLC-04).

## business_objects

_12 items_

### BO-ENTITY — Entity

- **owner:** BC02
- **domain:** DOM-03
- **tier:** T1 (attributes as claims); identity T2
- **key_rules:** identity only; attributes via claims
- **events:** EntityRegistered, EntityTypeChanged, EntityRetired
- **lifecycle:** ENTITY: ACTIVE → RETIRED
- **temporal:** ADR-P01
- **spatial:** ADR-P16 where located
- **security:** envelope
- **identity:** ULID + URN

### BO-EVENT — RealWorldEvent

- **owner:** BC02
- **domain:** DOM-03
- **tier:** T1
- **key_rules:** event_time (fuzzy) + location + participants via relationships
- **events:** RealWorldEventRegistered, …
- **lifecycle:** ACTIVE → RETIRED
- **temporal:** ADR-P01
- **spatial:** ADR-P16 where located
- **security:** envelope
- **identity:** ULID + URN

### BO-RELATIONSHIP — Relationship

- **owner:** BC02
- **domain:** DOM-03
- **tier:** T1
- **key_rules:** existence is a claim
- **events:** RelationshipAsserted, RelationshipRetracted
- **lifecycle:** via record time
- **temporal:** ADR-P01
- **spatial:** ADR-P16 where located
- **security:** envelope
- **identity:** ULID + URN

### BO-CLAIM — Claim

- **owner:** BC02
- **domain:** DOM-03
- **tier:** T1
- **key_rules:** immutable; close record_to to correct/retract
- **events:** ClaimAsserted, ClaimCorrected, ClaimRetracted
- **lifecycle:** via record time
- **temporal:** ADR-P01
- **spatial:** ADR-P16 where located
- **security:** envelope
- **identity:** ULID + URN

### BO-EVIDENCE — Evidence

- **owner:** BC02
- **domain:** DOM-03 (used by DOM-06)
- **tier:** T1
- **key_rules:** attachment by hash; custody chain
- **events:** EvidenceRegistered, EvidenceLinked, CustodyTransferred
- **lifecycle:** REGISTERED → SEALED
- **temporal:** ADR-P01
- **spatial:** ADR-P16 where located
- **security:** envelope
- **identity:** ULID + URN

### BO-SOURCE — Source

- **owner:** BC02
- **domain:** DOM-05
- **tier:** T1 (reliability) / T2 (profile)
- **key_rules:** identity protection levels
- **events:** SourceRegistered, SourceReliabilityRated
- **lifecycle:** ACTIVE → SUSPENDED → RETIRED
- **temporal:** ADR-P01
- **spatial:** ADR-P16 where located
- **security:** envelope
- **identity:** ULID + URN

### BO-OBSERVATION — Observation

- **owner:** BC02
- **domain:** DOM-06
- **tier:** T1
- **key_rules:** immutable after VALIDATED
- **events:** ObservationRecorded, ObservationValidated, ObservationRejected
- **lifecycle:** RECORDED → VALIDATED \| REJECTED
- **temporal:** ADR-P01
- **spatial:** ADR-P16 where located
- **security:** envelope
- **identity:** ULID + URN

### BO-CONFLICT — Conflict

- **owner:** BC02
- **domain:** DOM-03
- **tier:** T2
- **key_rules:** never modifies claims
- **events:** ConflictDetected, ConflictResolved, ConflictAccepted
- **lifecycle:** OPEN → UNDER_REVIEW → RESOLVED \| ACCEPTED_AS_CONFLICT; → SUPERSEDED
- **temporal:** ADR-P01
- **spatial:** ADR-P16 where located
- **security:** envelope
- **identity:** ULID + URN

### BO-ER-CASE — EntityResolutionCase

- **owner:** BC02
- **domain:** DOM-07 (proposals) / DOM-03
- **tier:** T2
- **key_rules:** decisions create SameAsLinks
- **events:** MatchProposed, MatchDecided, SplitRequested
- **lifecycle:** CANDIDATE → UNDER_REVIEW → MATCHED \| NOT_A_MATCH \| POSSIBLE_DUPLICATE; MATCHED → SPLIT_REQUIRED
- **temporal:** ADR-P01
- **spatial:** ADR-P16 where located
- **security:** envelope
- **identity:** ULID + URN

### BO-SAMEAS — SameAsLink

- **owner:** BC02
- **domain:** DOM-03
- **tier:** T2 (bitemporal record)
- **key_rules:** split = close record_to
- **events:** EntitiesLinked, EntitiesUnlinked
- **lifecycle:** via record time
- **temporal:** ADR-P01
- **spatial:** ADR-P16 where located
- **security:** envelope
- **identity:** ULID + URN

### BO-COLLECTION-REQUIREMENT — CollectionRequirement

- **owner:** BC02
- **domain:** DOM-05
- **tier:** T2
- **key_rules:** R2
- **events:** —
- **lifecycle:** R2
- **temporal:** ADR-P01
- **spatial:** ADR-P16 where located
- **security:** envelope
- **identity:** ULID + URN

### BO-LINEAGE — LineageRecord

- **owner:** BC02
- **domain:** DOM-03
- **tier:** T2 (append-only)
- **key_rules:** PROV-aligned
- **events:** LineageRecorded
- **lifecycle:** append-only
- **temporal:** ADR-P01
- **spatial:** ADR-P16 where located
- **security:** envelope
- **identity:** ULID + URN

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
business_objects:
- id: BO-ENTITY
  name: Entity
  owner: BC02
  domain: DOM-03
  tier: T1 (attributes as claims); identity T2
  key_rules: identity only; attributes via claims
  events: EntityRegistered, EntityTypeChanged, EntityRetired
  lifecycle: 'ENTITY: ACTIVE → RETIRED'
  temporal: ADR-P01
  spatial: ADR-P16 where located
  security: envelope
  identity: ULID + URN
- id: BO-EVENT
  name: RealWorldEvent
  owner: BC02
  domain: DOM-03
  tier: T1
  key_rules: event_time (fuzzy) + location + participants via relationships
  events: RealWorldEventRegistered, …
  lifecycle: ACTIVE → RETIRED
  temporal: ADR-P01
  spatial: ADR-P16 where located
  security: envelope
  identity: ULID + URN
- id: BO-RELATIONSHIP
  name: Relationship
  owner: BC02
  domain: DOM-03
  tier: T1
  key_rules: existence is a claim
  events: RelationshipAsserted, RelationshipRetracted
  lifecycle: via record time
  temporal: ADR-P01
  spatial: ADR-P16 where located
  security: envelope
  identity: ULID + URN
- id: BO-CLAIM
  name: Claim
  owner: BC02
  domain: DOM-03
  tier: T1
  key_rules: immutable; close record_to to correct/retract
  events: ClaimAsserted, ClaimCorrected, ClaimRetracted
  lifecycle: via record time
  temporal: ADR-P01
  spatial: ADR-P16 where located
  security: envelope
  identity: ULID + URN
- id: BO-EVIDENCE
  name: Evidence
  owner: BC02
  domain: DOM-03 (used by DOM-06)
  tier: T1
  key_rules: attachment by hash; custody chain
  events: EvidenceRegistered, EvidenceLinked, CustodyTransferred
  lifecycle: REGISTERED → SEALED
  temporal: ADR-P01
  spatial: ADR-P16 where located
  security: envelope
  identity: ULID + URN
- id: BO-SOURCE
  name: Source
  owner: BC02
  domain: DOM-05
  tier: T1 (reliability) / T2 (profile)
  key_rules: identity protection levels
  events: SourceRegistered, SourceReliabilityRated
  lifecycle: ACTIVE → SUSPENDED → RETIRED
  temporal: ADR-P01
  spatial: ADR-P16 where located
  security: envelope
  identity: ULID + URN
- id: BO-OBSERVATION
  name: Observation
  owner: BC02
  domain: DOM-06
  tier: T1
  key_rules: immutable after VALIDATED
  events: ObservationRecorded, ObservationValidated, ObservationRejected
  lifecycle: RECORDED → VALIDATED | REJECTED
  temporal: ADR-P01
  spatial: ADR-P16 where located
  security: envelope
  identity: ULID + URN
- id: BO-CONFLICT
  name: Conflict
  owner: BC02
  domain: DOM-03
  tier: T2
  key_rules: never modifies claims
  events: ConflictDetected, ConflictResolved, ConflictAccepted
  lifecycle: OPEN → UNDER_REVIEW → RESOLVED | ACCEPTED_AS_CONFLICT; → SUPERSEDED
  temporal: ADR-P01
  spatial: ADR-P16 where located
  security: envelope
  identity: ULID + URN
- id: BO-ER-CASE
  name: EntityResolutionCase
  owner: BC02
  domain: DOM-07 (proposals) / DOM-03
  tier: T2
  key_rules: decisions create SameAsLinks
  events: MatchProposed, MatchDecided, SplitRequested
  lifecycle: CANDIDATE → UNDER_REVIEW → MATCHED | NOT_A_MATCH | POSSIBLE_DUPLICATE; MATCHED → SPLIT_REQUIRED
  temporal: ADR-P01
  spatial: ADR-P16 where located
  security: envelope
  identity: ULID + URN
- id: BO-SAMEAS
  name: SameAsLink
  owner: BC02
  domain: DOM-03
  tier: T2 (bitemporal record)
  key_rules: split = close record_to
  events: EntitiesLinked, EntitiesUnlinked
  lifecycle: via record time
  temporal: ADR-P01
  spatial: ADR-P16 where located
  security: envelope
  identity: ULID + URN
- id: BO-COLLECTION-REQUIREMENT
  name: CollectionRequirement
  owner: BC02
  domain: DOM-05
  tier: T2
  key_rules: R2
  events: —
  lifecycle: R2
  temporal: ADR-P01
  spatial: ADR-P16 where located
  security: envelope
  identity: ULID + URN
- id: BO-LINEAGE
  name: LineageRecord
  owner: BC02
  domain: DOM-03
  tier: T2 (append-only)
  key_rules: PROV-aligned
  events: LineageRecorded
  lifecycle: append-only
  temporal: ADR-P01
  spatial: ADR-P16 where located
  security: envelope
  identity: ULID + URN
```

</details>
