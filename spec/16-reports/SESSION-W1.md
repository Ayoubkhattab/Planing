---
id: SESSION-W1
type: session-report
wave: W1 (a + b)
date: 2026-09-24
basis: V6§21.3
---

# SESSION REPORT — W1 Discovery & Framing

**Mode:** delegated decisions. The project owner delegated decision authority to Claude with a standing priority on scalability.

## Artifacts produced / updated
| Artifact | Change |
|---|---|
| `elicitation/W1-answers.md` | 32 answers, each tagged with the unknown it closes |
| `01-business/system-definition.md` | problem, priorities, release scope, context — APPROVED_DELEGATED |
| `01-business/capabilities.md` | **new:** 14 L1 / 54 L2 capabilities, mapped to domains, outcomes, releases |
| `01-business/outcomes.md` | 12 measures with baseline-relative targets |
| `01-business/stakeholders.md` | 7 decision-rights (RACI) entries |
| `07-quality/scale-envelope.md` | **new:** design envelope + 12 scale-ready principles (SR-01..SR-12) |
| `07-quality/workloads.md` | **new:** 8 workloads with initial targets |
| `14-slices/slices.md` | release assignment R1/R2/R3 — HAP-02 |
| Registers | unknowns, assumptions (+3), risks (+3), HAPs, corrections, ownership, glossary (+3) |
| ADRs | 9 ADRs annotated with decisive W1 input (formal approval in W3) |

## How "always scalability" was applied
The instruction was applied as **SR-00 Scale-Ready, not Scale-First**:
- **Designed in from day one** (cheap now, expensive to retrofit): multi-tenancy with tenant in every partition key, cell-based deployment, stateless compute, async jobs, per-tenant quotas, rebuildable projections, cursor pagination, 10× headroom rule.
- **Not deployed up front** (expensive now, cheap to add later because projections are rebuildable): dedicated search cluster, graph database, dedicated event broker. Each is added only when a workload measurement triggers it (SR-10).
- **Why:** deploying all components up front with a small operations team is the more likely failure mode than running out of scale (RSK-013).

## Epistemic summary
- **DECISIONS (delegated):** 30 answers.
- **Not invented:** actual jurisdiction, actual budget, actual classification scheme. The design adapts to them; they are recorded as residual unknowns.
- **Design targets ≠ forecasts:** all numbers are envelope targets (ASM-010), recalibrated if reality exceeds 50% of the envelope.

## Unknown register
| Status | Count |
|---|---|
| closed by delegated decision | 17 |
| partially closed, non-blocking | 2 (UNK-002, UNK-012) |
| open | 1 (UNK-016 accessibility — W2) |

## Lint
| Rule | Before | After |
|---|---|---|
| SL-01 | 22 / 39 | 20 / 39 (Authority, Tenant resolved) |
| SL-15 | 8 / 8 | 8 / 8 (W2) |
| SL-19 | 0 | 0 — all delegated approvals carry approver and date |
| SL-20 | 0 real | 0 real |

## Gates
G0 **PASS (delegated)** · G1 **PASS (delegated)** · G2 FAIL · G3 PARTIAL (unblocked) · G6 BLOCKED

## Human decisions pending
- Ratification of all delegated decisions by the project owner at G6.
- UNK-002 legal confirmation before G8.

## Next recommended session
**W2 — Requirements & Quality Scenarios** for R1 scope: EARS system requirements per R1 capability, quality attribute scenarios from the envelope and service tiers, complete the 9 use-case gaps that fall in R1, requirements quality report.
**Then W3** — the kernel ADRs can now be formally decided, since their blocking unknowns are closed.
