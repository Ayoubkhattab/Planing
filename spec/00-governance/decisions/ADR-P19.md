---
id: ADR-P19
type: adr
title: Handling of Authorization Outcomes (403 vs 404, MFA step-up, approval-required)
status: APPROVED
wave: Phase 3.8 (18-analysis-design, stage 4)
deciders: project owner (chose all three outcomes, 2026-10-01)
approved_by: project owner
approved_at: '2026-10-01'
blocked_by: []
depends_on:
- ADR-P06
- ADR-P11
- ADR-P17
related:
- CR-75
verified_by:
- FIT-03
- FIT-16
---

# ADR-P19: Handling of Authorization Outcomes

## Context and Problem
The policy decision point returns `ALLOW`, `DENY`, `CONDITIONAL`, `REDACT`, `AGGREGATE` or `REQUIRE_APPROVAL` with obligations (REQ-FND-012, `08-security/authorization-model.md` §2). The ratified sources leave three outcomes without a defined API behaviour (source issue S-07 in `18-analysis-design/00-index.md` §6):

1. **Visible but not permitted.** ADR-P06 item 5 makes not-found and forbidden indistinguishable for resources the caller may not see. The header of every `05-contracts/errors-*.md` allows `403` "only for a resource the user is entitled to see but not act on", yet no operation in the 28 OpenAPI files declares `403`.
2. **Unmet pre-execution obligation.** 36 command policies carry an `mfa` obligation (`08-security/policies-slc*.md`); ADR-P17 step 6 says the command is rejected when it is not met, but no error code exists.
3. **`REQUIRE_APPROVAL`.** No command policy returns it (all 477 decide `ALLOW` when matched); it appears for policy-level approvals such as bulk export (`POL-EXPORT-BULK`, authorization-model §4). Business approvals are already modelled as explicit states with segregation of duties (e.g. `CMD-PLV-APPROVE`, `CMD-TASK-APPROVE`), and AGG-ALLOCATION already turns the obligation into an explicit state (`SYS:checks passed, policy requires approval` → `REQUESTED`, capacity held ≤ 1 h).

## Decision Drivers
1. No disclosure of existence for invisible resources (ADR-P06, THR-005).
2. A client must be able to tell "authenticate more strongly" from "you may not do this" without trial and error.
3. Nothing executes before every pre-execution obligation is met (ADR-P17 step 6).
4. Operational simplicity in R1: no new platform-wide workflow component unless evidence requires it (SR-10, FIT-18).

## Considered Options
- **(1) Visible but not permitted:** (a) `403 AUTHZ_DENIED` when visible, `404` otherwise; (b) always `404`.
- **(2) MFA obligation:** (a) `401` with a step-up challenge; (b) `403` with a dedicated code.
- **(3) `REQUIRE_APPROVAL`:** (a) reject with a dedicated code and keep approvals explicit in aggregates; (b) a generic `ApprovalRequest` aggregate that holds the command as pending and executes it on approval.

## Decision Outcome
The project owner chose **1(a), 2(a), 3(a)**:

| Outcome | HTTP | Code | `retryable` | Behaviour |
|---|---|---|---|---|
| Resource invisible to the caller (any denial) | 404 | `NOT_FOUND` | no | Same body shape as a missing resource; nothing about the resource (existence, version, state) is returned. Unchanged from ADR-P06 item 5. |
| Resource visible, action not permitted | 403 | `AUTHZ_DENIED` | no | `ApiError.policy.reason_code` is set; no resource attributes beyond what the caller can already see. "Visible" means a `view` decision on the same resource returns `ALLOW`/`REDACT`. |
| `mfa` obligation and the session's authentication strength is insufficient | 401 | `MFA_STEP_UP_REQUIRED` (new) | yes, after step-up | The response carries the required authentication strength as a challenge (OIDC `acr_values`). The client re-authenticates and retries **with the same `Idempotency-Key`**; nothing has executed. |
| `REQUIRE_APPROVAL` | 403 | `APPROVAL_REQUIRED` (new) | no | `ApiError.details.approver` names the approver role; nothing executes. No generic approval workflow; an operation that needs routine approval gets an explicit aggregate (bulk export: **[Missing]** — to be specified with the export capability). |
| `CONDITIONAL` | — | — | — | Its conditions are obligations: pre-execution ones are checked at pipeline step 6 (today only `mfa`); post-execution ones (`audit`, `watermark`, `notify…`) at step 10. |
| `REDACT` / `AGGREGATE` | 200 | — | — | Query results are returned with the named fields redacted, or as aggregates with `min_group` (PRV-02). Not applicable to commands. |
| PDP unavailable or erroring | 503 | `POLICY_ENGINE_UNAVAILABLE` | yes | Request denied (REQ-FND-013, FIT-16). Unchanged. |

**Pipeline placement (ADR-P17):** the 404/403 choice is made at step 5 (full authorization with the loaded resource); the `401` step-up at step 6; `VERSION_CONFLICT` only after both (step 7). Coarse authorization at step 2 always answers `404` for resources, because nothing has been loaded yet.

## Consequences
### Positive
- Users who can see a resource get an honest `403` instead of a confusing "not found".
- Step-up is a normal retry: idempotency guarantees no double execution.
- No new platform aggregate in R1.

### Negative
- Contracts must declare `401` and `403` on every command, and the error catalogs must add `MFA_STEP_UP_REQUIRED` and `APPROVAL_REQUIRED` (CR-75, applied through the spec tooling in the source-correction round).
- The PEP needs a second, cheap `view` evaluation to decide between `403` and `404`; covered by the ≤ 60 s decision cache (authorization-model §5).
- Bulk export stays unavailable until its explicit aggregate is specified.

### Risks and mitigations
- **Risk:** a `403` on a list-visible resource could leak an attribute through `reason_code`. **Mitigation:** reason codes are a closed list that names the rule, never resource data; covered by the zero-disclosure tests of QAS-SEC-002.

## Related Decisions
- ADR-P06 (as amended by CR-47) — non-disclosure and result re-checks; unchanged for invisible resources.
- ADR-P11 — PEP/PDP placement.
- ADR-P17 — the command pipeline steps referenced above.
