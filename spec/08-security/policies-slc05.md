---
id: POLICIES-SLC05
type: policy-decision-tables
title: Policy Decision Tables — SLC-05
wave: W6
slice: SLC-05
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Policy Decision Tables — SLC-05

## command_policies

_4 items_

| id | command | subject | resource | decision | otherwise | obligations |
|---|---|---|---|---|---|---|
| POL-PRJ-CREATE-VERSION | CMD-PRJ-CREATE-VERSION | Platform Operator (platform tenant) | AGG-PROJECTION-VERSION | ALLOW | DENY | audit; mfa for PROMOTE |
| POL-PRJ-PROMOTE | CMD-PRJ-PROMOTE | Platform Operator (platform tenant) | AGG-PROJECTION-VERSION | ALLOW | DENY | audit; mfa for PROMOTE |
| POL-PRJ-RETIRE | CMD-PRJ-RETIRE | Platform Operator (platform tenant) | AGG-PROJECTION-VERSION | ALLOW | DENY | audit; mfa for PROMOTE |
| POL-PRJ-CANCEL-BUILD | CMD-PRJ-CANCEL-BUILD | Platform Operator (platform tenant) | AGG-PROJECTION-VERSION | ALLOW | DENY | audit; mfa for PROMOTE |

## query_policies

_6 items_

| id | query | subject | allowed_scope | otherwise |
|---|---|---|---|---|
| POL-SRCH-QUERY | QRY-SRCH-QUERY | any user; allowed_scope pre-filter + authoritative re-check | PDP allowed_scope → pre-filter on doc and fact labels; LabelCheck re-check on page | DENY (not-found shape) |
| POL-SRCH-SUGGEST | QRY-SRCH-SUGGEST | any user; same filter | PDP allowed_scope → pre-filter on doc and fact labels; LabelCheck re-check on page | DENY (not-found shape) |
| POL-GRAPH-NEIGHBORHOOD | QRY-GRAPH-NEIGHBORHOOD | any user; per-node and per-edge authorization | PDP allowed_scope → pre-filter on doc and fact labels; LabelCheck re-check on page | DENY (not-found shape) |
| POL-GRAPH-PATHS | QRY-GRAPH-PATHS | any user; per-node and per-edge authorization | PDP allowed_scope → pre-filter on doc and fact labels; LabelCheck re-check on page | DENY (not-found shape) |
| POL-PRJ-STATUS | QRY-PRJ-STATUS | platform operator | PDP allowed_scope → pre-filter on doc and fact labels; LabelCheck re-check on page | DENY (not-found shape) |
| POL-LABEL-CHECK | QRY-LABEL-CHECK (all owners) | discovery service workload identity only | returns visibility for the subject passed in the request context | DENY |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
command_policies:
- id: POL-PRJ-CREATE-VERSION
  command: CMD-PRJ-CREATE-VERSION
  subject: Platform Operator (platform tenant)
  resource: AGG-PROJECTION-VERSION
  decision: ALLOW
  otherwise: DENY
  obligations: audit; mfa for PROMOTE
- id: POL-PRJ-PROMOTE
  command: CMD-PRJ-PROMOTE
  subject: Platform Operator (platform tenant)
  resource: AGG-PROJECTION-VERSION
  decision: ALLOW
  otherwise: DENY
  obligations: audit; mfa for PROMOTE
- id: POL-PRJ-RETIRE
  command: CMD-PRJ-RETIRE
  subject: Platform Operator (platform tenant)
  resource: AGG-PROJECTION-VERSION
  decision: ALLOW
  otherwise: DENY
  obligations: audit; mfa for PROMOTE
- id: POL-PRJ-CANCEL-BUILD
  command: CMD-PRJ-CANCEL-BUILD
  subject: Platform Operator (platform tenant)
  resource: AGG-PROJECTION-VERSION
  decision: ALLOW
  otherwise: DENY
  obligations: audit; mfa for PROMOTE
query_policies:
- id: POL-SRCH-QUERY
  query: QRY-SRCH-QUERY
  subject: any user; allowed_scope pre-filter + authoritative re-check
  allowed_scope: PDP allowed_scope → pre-filter on doc and fact labels; LabelCheck re-check on page
  otherwise: DENY (not-found shape)
- id: POL-SRCH-SUGGEST
  query: QRY-SRCH-SUGGEST
  subject: any user; same filter
  allowed_scope: PDP allowed_scope → pre-filter on doc and fact labels; LabelCheck re-check on page
  otherwise: DENY (not-found shape)
- id: POL-GRAPH-NEIGHBORHOOD
  query: QRY-GRAPH-NEIGHBORHOOD
  subject: any user; per-node and per-edge authorization
  allowed_scope: PDP allowed_scope → pre-filter on doc and fact labels; LabelCheck re-check on page
  otherwise: DENY (not-found shape)
- id: POL-GRAPH-PATHS
  query: QRY-GRAPH-PATHS
  subject: any user; per-node and per-edge authorization
  allowed_scope: PDP allowed_scope → pre-filter on doc and fact labels; LabelCheck re-check on page
  otherwise: DENY (not-found shape)
- id: POL-PRJ-STATUS
  query: QRY-PRJ-STATUS
  subject: platform operator
  allowed_scope: PDP allowed_scope → pre-filter on doc and fact labels; LabelCheck re-check on page
  otherwise: DENY (not-found shape)
- id: POL-LABEL-CHECK
  query: QRY-LABEL-CHECK (all owners)
  subject: discovery service workload identity only
  allowed_scope: returns visibility for the subject passed in the request context
  otherwise: DENY
```

</details>
