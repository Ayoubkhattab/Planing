---
id: SESSION-W3
type: session-report
wave: W3
date: 2026-09-24
basis: V6§21.3
---

# SESSION REPORT — W3 Information Kernel

**Mode:** delegated decisions, scalability priority, Markdown only (HAP-11).

## Artifacts produced (29 new, 12 updated)
| Area | Files |
|---|---|
| Decisions | 15 ADRs approved (delegated) with outcome, rationale, consequences, impact, verification — P05 stays for W8 |
| `04-information/` | meta-model, object-envelope (JSON Schema), temporal-model, spatial-model, claim-evidence-model, confidence-model (JSON Schema), conflict-model, entity-resolution, provenance-lineage, importance-tiers, language-model, reference-data (20 code lists), business-objects-kernel (12 BOs) |
| `03-domain/` | ownership (48 BOs, 0 unowned), domains (corrected), context-map (Mermaid + contracts), bc-boundary-test (8 × 10 criteria) |
| `08-security/` | classification-scheme, trust-boundaries (10 TBs), authorization-model (PDP/PEP, decision tables), data-protection, audit-architecture, threat-model (20 STRIDE threats), privacy-threats (7 LINDDUN) |
| `10-ai/` | autonomy-matrix (14 operations, 6 forbidden) |
| `13-verification/` | fitness-functions (18) |
| `16-reports/` | SLC-00 walkthrough (18 steps), consistency check, gate report |

## The five design decisions that matter most
1. **Entity = identity + claims.** T1 attributes are never columns that get overwritten; they are bitemporal claims with sources. The "current value" is a computed view, and disagreement is shown, never silently resolved by "highest confidence".
2. **Merge is a link, not a rewrite.** Entity resolution records same-as links; claims stay on their original subject. Split = closing a link. Identity itself becomes bitemporal ("what did we believe was one entity on date K?").
3. **Two time axes answer two different questions.** "What was true at T" vs "what did we know at K" — the second is what decision review needs.
4. **Pre-filter + authoritative re-check.** Search and maps filter by allowed scope *before* counting, and re-check a security version so revocation is immediate despite 30 s index lag.
5. **Hybrid tenancy with cells.** Small tenants share cells with two independent isolation barriers; sovereign, top-classified or large tenants get dedicated cells from the same release.

## New findings
- **CR-44:** "Event" meant two things (real-world occurrence vs system domain event) → split into RealWorldEvent / Domain Event.
- **Requirements realigned:** REQ-INF-033/034 rewritten to match the link-based merge model.
- **SLC-00:** no ownership gap across 18 steps; one R1 limitation recorded as DEBT-001 (resources linked to tasks as text until SLC-09); one missing contract identified (AlertRaised → Notification) for W6.
- **New risks:** RSK-017 (large identity clusters), RSK-018 (policy engine on critical path), RSK-019 (claims model complexity for developers → build a shared kernel library first in SLC-02).

## Lint
| Rule | Result |
|---|---|
| SL-01 single owner | **0 / 48** (was 20) |
| SL-15, SL-19 | 0 |
| SL-20 dangling references | 0 real |

## Gates
G0–G2 PASS · **G3 PASS (delegated)** · G4/G5 PARTIAL · G6 BLOCKED, **slices unblocked**

## Next recommended session
**W4–W7 for SLC-01 (Tenancy, Identity, Organization, Authorization, Audit)** — the first slice, because every other slice depends on its SecurityContext, AuthorityCheck, PDP and audit contracts. Output: aggregates, complete state machines, commands/queries/events, invariants, policies, threat model and FMEA for the slice, OpenAPI/AsyncAPI embedded in Markdown, Gherkin acceptance, and G6-SLC readiness.
