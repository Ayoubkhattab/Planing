---
id: ADR-P18
type: adr
title: Repository and Module Structure (single repository, context packages composed into deployment units)
status: APPROVED_DELEGATED
wave: Phase 3.8 (18-analysis-design)
deciders: Claude (acting decision owner, delegated by project owner, 2026-09-30)
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-30'
blocked_by: []
depends_on:
- ADR-P17
- ADR-P05
related:
- TD-15
- TD-17
verified_by:
- FIT-01
- FIT-20
---

# ADR-P18: Repository and Module Structure

## Context and Problem
ADR-P17 fixes the rings *inside* a unit. Two facts make the physical layout non-trivial:

1. **A bounded context is a model boundary; a deployment unit is an operational boundary** (`12-solution/deployment-units.md`, principle line). They do not map one-to-one: BC02 runs in DU-04 and DU-05; BC03 in DU-06 and DU-07; BC07 in DU-09, DU-10, DU-11 and DU-16; DU-01 (gateway), DU-12 (tiles) and DU-13 (analysis jobs) host no aggregate.
2. **A cell runs one platform version** across all its units (`12-solution/cell-architecture.md` §1), delivered as one signed, air-gapped Zarf bundle with forward-only migrations (TD-17), from contracts that generate server stubs and clients (TD-15).

The layout must let one bounded context's model be reused by several units without copying, forbid code-level shortcuts between contexts (FIT-01), and produce one versioned release per cell.

## Decision Drivers
1. One model per bounded context, reused by every unit that runs it.
2. Cross-context access only through published contracts (OHS, events) — enforceable mechanically.
3. One atomic change can update a contract, its producer and its consumers.
4. One tagged commit produces the complete, reproducible air-gapped bundle.
5. Ownership and review boundaries per context remain clear.

## Considered Options

### Option 1 — Single repository; context packages separate from deployable services
- **Pros:** drivers 1–4 met directly — a unit is a thin composition root over context packages; contract changes and their consumers change atomically; one tag → one bundle; dependency rules checked across the whole tree.
- **Cons:** needs affected-only builds and tests to stay fast; per-folder ownership must be configured explicitly.

### Option 2 — One repository per deployment unit (16 repositories)
- **Pros:** strong isolation; independent pipelines.
- **Cons:** BC02, BC03 and BC07 models would be duplicated or published as versioned libraries between repos; contract changes need coordinated multi-repo releases; assembling one cell version from 16 repositories contradicts the single-version cell.

### Option 3 — One repository per bounded context (8 repositories)
- **Pros:** matches model ownership.
- **Cons:** units that compose several contexts' shared platform libraries still need cross-repo versioning; the gateway, tiles and analysis-job units have no natural home; one cell release still spans 8+ repositories.

## Decision Outcome
**Option 1.** The top-level layout, detailed in `18-analysis-design/13-project-structure.md`:

| Area | Contents | Depends on |
|---|---|---|
| `contracts/` | generated from `spec/05-contracts` (OpenAPI, AsyncAPI, error catalogs); server stubs and clients | nothing |
| `shared-kernel/` | pure value types shared by all contexts: ULID/URN (ADR-P13), bitemporal intervals (ADR-P01), LocalizedName (ADR-P15), security labels, error envelope | nothing |
| `contexts/bcNN-<name>/` | one package per bounded context: `domain/`, `application/`, `ports/` (ADR-P17) | shared-kernel, contracts of *other* contexts only |
| `platform/` | reusable adapter libraries: unit of work + outbox + audit outbox, inbox, idempotency store, PEP client, telemetry, lease-based scheduler | shared-kernel, contracts |
| `services/du-NN-<name>/` | one deployable per deployment unit: composition root, inbound and outbound adapters, configuration | contexts it runs, platform, contracts |
| `deploy/` | cell manifests, Zarf bundle definition, forward-only migrations per context schema | services |

**Rules:**
1. `contexts/*` never import another `contexts/*`; a context reaches another only through `contracts/` (generated client or event types).
2. `services/*` never import another `services/*`.
3. Each database schema is owned by exactly one context, which alone migrates it (FIT-01, TD-01). A context may own several schemas: BC07 owns `integration`, `field`, `ai` and the projection store (`06-data/logical-model/slc-02, 05, 10, 11`).
4. One repository tag = one platform version = one Zarf bundle for all units of a cell.
5. Ownership is declared per `contexts/*` and `services/*` folder.

## Rationale
Separating *context packages* (model boundary) from *services* (operational boundary) is the only layout in which the ratified many-to-one mapping between units and contexts needs no duplication and no cross-repository versioning. It also keeps a future unit split — such as the BC-BOUNDARY-TEST candidates DU-05 and DU-07 — to a new `services/` folder, with no model change.

## Consequences

### Positive
- The unit ↔ context mapping in `deployment-units.md` becomes a dependency list per service, reviewable in one place.
- Splitting or merging units never moves domain code.
- The dependency rules above are mechanically checkable (FIT-20).

### Negative
- CI must compute affected packages to keep build times bounded.
- A single repository needs folder-level ownership and review rules to keep context boundaries social as well as technical.

### Risks and mitigations
- **Risk:** `platform/` grows into a shared "utils" dumping ground that couples contexts. **Mitigation:** `platform/` holds only adapter infrastructure named in `11-hexagonal-reference.md`; no business types.
- **Risk:** `shared-kernel/` grows beyond value types. **Mitigation:** additions require an ADR amendment; no behaviour with I/O.

## Related Decisions
- ADR-P17 — internal rings realised inside each `contexts/*` package and `services/*` unit.
- TD-15 — contracts generate stubs and clients (`contracts/`).
- TD-17 — signed offline bundles and forward-only migrations (`deploy/`).
