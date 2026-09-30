---
id: SESSION-W2
type: session-report
wave: W2
date: 2026-09-24
basis: V6§21.3
---

# SESSION REPORT — W2 Requirements & Quality Scenarios

**Mode:** delegated decisions (acting decision owner), scalability priority.
**Format change (HAP-11, approved by the project owner):** every file in the package is now Markdown. Each data file shows readable tables and keeps its full machine-readable YAML in a collapsible block at the end, so V6 A15 (machine-readable specs) still holds.

## Artifacts produced / updated
| Artifact | Content |
|---|---|
| `02-requirements/requirements.md` | 8 BRQ rewritten with statements, outcomes, acceptance; **114 system requirements** in EARS, each with acceptance criteria, verification method, source, capability, use cases, quality links |
| `02-requirements/quality-scenarios.md` | **43 quality attribute scenarios**: performance 8, scalability 5, availability 3, recoverability 3, reliability/resilience/integrity 3, security 7, privacy 1, offline 1, data quality 1, temporal 1, audit 1, traceability 2, usability 2, accessibility 1, evolvability 1, operability 1, observability 1, cost 1 |
| `02-requirements/use-cases.md` | catalog complete for R1: 24 new use cases (UC-080..UC-105), release per use case, requirement links, gap resolutions |
| `01-business/business-rules.md` | 7 ambiguous rules rewritten; each rule lists the requirements that enforce it |
| `07-quality/workloads.md` | +4 workloads (document, batch, ingestion, export), linked to quality scenarios |
| `16-reports/REQUIREMENTS-QUALITY-REPORT.md` | ISO 29148 checks, 5 requirement conflicts found and resolved |
| `00-governance/decisions/ADR-P16.md` | new: canonical CRS (WGS 84 + original) |

## Delegated decisions taken in W2
| Decision | Value |
|---|---|
| Command latency | p95 ≤ 300 ms, p99 ≤ 1 s at design load |
| Read latency | single object p95 ≤ 300 ms; list p95 ≤ 1 s |
| Map tiles | p95 ≤ 500 ms |
| Burst handling | 50,000 events/s for 60 s with 0 loss via backpressure |
| Tenant provisioning | automated, ≤ 1 h, no code or schema change |
| Accessibility | WCAG 2.2 AA (closes UNK-016) |
| Contract evolution | previous major version supported ≥ 6 months |
| Canonical CRS | WGS 84 + original CRS kept (ADR-P16 input) |
| Arabic search | recall ≥ 95 % across spelling variants and transliterations |
| Field usability | observation with photo median ≤ 60 s |

## Key engineering findings
1. **Authorization revocation must not wait for the index.** Index lag is 30 s, but revoking access must take effect on the next request. This forces an authorization re-check at query time on search results — a design constraint for W3/SLC-05, now fixed as REQ-GOV-004 and QAS-SEC-003.
2. **Inference protection extends beyond search.** It covers alerts, notifications and map tiles (REQ-SIT-006, REQ-COM-002, REQ-SIT-007).
3. **Scale is testable.** QAS-SCAL-001 states the 10× rule as an acceptance test: 100 → 1,000 → 5,000 concurrent users with zero architectural change.

## Lint / checks
| Check | Result |
|---|---|
| SL-15 requirements have acceptance + verification | 0 violations (was 8/8) |
| SL-16 high-priority QAS have measures | 0 violations |
| SL-20 dangling references | 0 |
| SL-01 single owner | 20 / 39 (W3) |
| Ambiguity scan | 1 documented false positive |

## Gates
G0 PASS · G1 PASS · **G2 PASS** (all delegated) · G3 PARTIAL · G6 BLOCKED

## Next recommended session
**W3 — Information Kernel:** formal decision of ADR-P01, P02, P03, P04, P06, P07, P13, P14, P15, P16; information models (Entity, Event, Relationship, Claim, Evidence, Source, Observation); corrected Object Envelope; confidence, conflict and entity-resolution models; ownership of the remaining 20 objects; security kernel (classification, trust boundaries, authorization model).
