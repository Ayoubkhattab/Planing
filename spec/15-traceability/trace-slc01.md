---
id: TRACE-SLC01
type: traceability-matrix
title: Traceability — SLC-01 (generated)
wave: W7
slice: SLC-01
status: GENERATED
notes: مولّدة من رؤوس المخرجات والكتالوجات؛ لا تُحرر يدوياً.
---

# Traceability — SLC-01 (generated)

> مولّدة من رؤوس المخرجات والكتالوجات؛ لا تُحرر يدوياً.

## requirements

_25 items_

| requirement | design_elements | operations | tests | status |
|---|---|---|---|---|
| REQ-FND-001 | AGG-TENANT, QRY-TEN-GET | 12 | TST-SLC01-INVARIANTS, TST-TENANT-SM | TRACED |
| REQ-FND-002 | AGG-ORGANIZATION, QRY-ORG-TREE | 9 | TST-ORGANIZATION-SM | TRACED |
| REQ-FND-003 | AGG-TENANT | 11 | TST-SLC01-INVARIANTS, TST-TENANT-SM | TRACED |
| REQ-FND-004 | AGG-TENANT | 11 | TST-TENANT-SM | TRACED |
| REQ-FND-005 | AGG-USER | 10 | TST-USER-SM | TRACED |
| REQ-FND-006 | AGG-PERSON, AGG-SERVICE-ACCOUNT, AGG-USER, QRY-USR-GET, QRY-USR-LIST | 22 | TST-PERSON-SM, TST-SERVICE-ACCOUNT-SM, TST-USER-SM | TRACED |
| REQ-FND-007 | AGG-AUTHORITY-GRANT, QRY-AUT-LIST | 8 | TST-AUTHORITY-GRANT-SM | TRACED |
| REQ-FND-008 | AGG-AUTHORITY-GRANT | 7 | TST-AUTHORITY-GRANT-SM, TST-SLC01-INVARIANTS | TRACED |
| REQ-FND-009 | AGG-AUTHORITY-GRANT, QRY-AUT-CHECK | 8 | TST-AUTHORITY-GRANT-SM, TST-SLC01-INVARIANTS | TRACED |
| REQ-FND-010 | QRY-PDP-DECIDE, QRY-SEC-CONTEXT | 2 | TST-SLC01-INVARIANTS | TRACED |
| REQ-FND-011 | AGG-POLICY-SET, AGG-ROLE-ASSIGNMENT | 7 | TST-POLICY-SET-SM, TST-ROLE-ASSIGNMENT-SM | TRACED |
| REQ-FND-012 | AGG-POLICY-SET | 5 | TST-POLICY-SET-SM | TRACED |
| REQ-FND-013 | PB-*/audit-architecture | 0 | TST-SLC01-INVARIANTS | TRACED |
| REQ-FND-014 | AGG-ROLE | 4 | TST-ROLE-SM | TRACED |
| REQ-FND-015 | PB-*/audit-architecture, QRY-AUD-SEARCH | 1 | TST-SLC01-INVARIANTS | TRACED |
| REQ-FND-016 | PB-*/audit-architecture, QRY-AUD-VERIFY | 1 | TST-SLC01-INVARIANTS | TRACED |
| REQ-FND-017 | AGG-SECURITY-EXCEPTION, QRY-EXC-LIST | 5 | TST-SECURITY-EXCEPTION-SM, TST-SLC01-INVARIANTS | TRACED |
| REQ-FND-018 | AGG-TENANT | 11 | TST-TENANT-SM | TRACED |
| REQ-GOV-001 | AGG-CLASSIFICATION-SCHEME, QRY-CLS-ACTIVE | 5 | TST-CLASSIFICATION-SCHEME-SM | TRACED |
| REQ-GOV-003 | AGG-CLEARANCE, QRY-CLR-GET | 7 | TST-CLEARANCE-SM, TST-SLC01-INVARIANTS | TRACED |
| REQ-GOV-004 | AGG-CLEARANCE | 6 | TST-CLEARANCE-SM, TST-SLC01-INVARIANTS | TRACED |
| REQ-GOV-008 | AGG-PERSON | 5 | TST-PERSON-SM | TRACED |
| REQ-GOV-009 | AGG-CLASSIFICATION-SCHEME, AGG-POLICY-SET, QRY-POL-GET | 10 | TST-CLASSIFICATION-SCHEME-SM, TST-POLICY-SET-SM | TRACED |
| REQ-OPS-005 | AGG-ROLE-ASSIGNMENT | 2 | TST-ROLE-ASSIGNMENT-SM | TRACED |
| REQ-OPS-009 | AGG-ROLE-ASSIGNMENT | 2 | TST-ROLE-ASSIGNMENT-SM | TRACED |

## quality

_10 items_

| qas | design | verification |
|---|---|---|
| QAS-SEC-001 | PB-01, tenant_id everywhere, RLS (LDM) | TST-SLC01-INVARIANTS: Cross-tenant |
| QAS-SEC-003 | PL-SECURITY-CONTEXT §2, security_versions KV | TST-SLC01-INVARIANTS: Revocation |
| QAS-SEC-005 | PB-03, FM-S01-03 | TST-SLC01-INVARIANTS: Policy engine failure |
| QAS-SEC-006 | audit chains + anchors | TST-SLC01-INVARIANTS: tampering |
| QAS-SEC-008 | SCIM → CMD-USR-DISABLE → EVT-SEC-VERSION-INCREMENTED | TST-SLC01-INVARIANTS: SCIM |
| QAS-AUD-001 | audit_outbox same transaction (FIT-04) | TST-SLC01-INVARIANTS: atomic audit |
| QAS-PERF-009 | embedded evaluators + signed bundles | performance test (W8 strategy) |
| QAS-PERF-010 | gateway cache (subject, security_version) | performance test |
| QAS-PERF-011 | audit shipper | performance test |
| QAS-SCAL-003 | provisioning saga | provisioning test ≤ 1 h |

## gaps

_empty_

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
requirements:
- requirement: REQ-FND-001
  design_elements:
  - AGG-TENANT
  - QRY-TEN-GET
  operations: 12
  tests:
  - TST-SLC01-INVARIANTS
  - TST-TENANT-SM
  status: TRACED
- requirement: REQ-FND-002
  design_elements:
  - AGG-ORGANIZATION
  - QRY-ORG-TREE
  operations: 9
  tests:
  - TST-ORGANIZATION-SM
  status: TRACED
- requirement: REQ-FND-003
  design_elements:
  - AGG-TENANT
  operations: 11
  tests:
  - TST-SLC01-INVARIANTS
  - TST-TENANT-SM
  status: TRACED
- requirement: REQ-FND-004
  design_elements:
  - AGG-TENANT
  operations: 11
  tests:
  - TST-TENANT-SM
  status: TRACED
- requirement: REQ-FND-005
  design_elements:
  - AGG-USER
  operations: 10
  tests:
  - TST-USER-SM
  status: TRACED
- requirement: REQ-FND-006
  design_elements:
  - AGG-PERSON
  - AGG-SERVICE-ACCOUNT
  - AGG-USER
  - QRY-USR-GET
  - QRY-USR-LIST
  operations: 22
  tests:
  - TST-PERSON-SM
  - TST-SERVICE-ACCOUNT-SM
  - TST-USER-SM
  status: TRACED
- requirement: REQ-FND-007
  design_elements:
  - AGG-AUTHORITY-GRANT
  - QRY-AUT-LIST
  operations: 8
  tests:
  - TST-AUTHORITY-GRANT-SM
  status: TRACED
- requirement: REQ-FND-008
  design_elements:
  - AGG-AUTHORITY-GRANT
  operations: 7
  tests:
  - TST-AUTHORITY-GRANT-SM
  - TST-SLC01-INVARIANTS
  status: TRACED
- requirement: REQ-FND-009
  design_elements:
  - AGG-AUTHORITY-GRANT
  - QRY-AUT-CHECK
  operations: 8
  tests:
  - TST-AUTHORITY-GRANT-SM
  - TST-SLC01-INVARIANTS
  status: TRACED
- requirement: REQ-FND-010
  design_elements:
  - QRY-PDP-DECIDE
  - QRY-SEC-CONTEXT
  operations: 2
  tests:
  - TST-SLC01-INVARIANTS
  status: TRACED
- requirement: REQ-FND-011
  design_elements:
  - AGG-POLICY-SET
  - AGG-ROLE-ASSIGNMENT
  operations: 7
  tests:
  - TST-POLICY-SET-SM
  - TST-ROLE-ASSIGNMENT-SM
  status: TRACED
- requirement: REQ-FND-012
  design_elements:
  - AGG-POLICY-SET
  operations: 5
  tests:
  - TST-POLICY-SET-SM
  status: TRACED
- requirement: REQ-FND-013
  design_elements:
  - PB-*/audit-architecture
  operations: 0
  tests:
  - TST-SLC01-INVARIANTS
  status: TRACED
- requirement: REQ-FND-014
  design_elements:
  - AGG-ROLE
  operations: 4
  tests:
  - TST-ROLE-SM
  status: TRACED
- requirement: REQ-FND-015
  design_elements:
  - PB-*/audit-architecture
  - QRY-AUD-SEARCH
  operations: 1
  tests:
  - TST-SLC01-INVARIANTS
  status: TRACED
- requirement: REQ-FND-016
  design_elements:
  - PB-*/audit-architecture
  - QRY-AUD-VERIFY
  operations: 1
  tests:
  - TST-SLC01-INVARIANTS
  status: TRACED
- requirement: REQ-FND-017
  design_elements:
  - AGG-SECURITY-EXCEPTION
  - QRY-EXC-LIST
  operations: 5
  tests:
  - TST-SECURITY-EXCEPTION-SM
  - TST-SLC01-INVARIANTS
  status: TRACED
- requirement: REQ-FND-018
  design_elements:
  - AGG-TENANT
  operations: 11
  tests:
  - TST-TENANT-SM
  status: TRACED
- requirement: REQ-GOV-001
  design_elements:
  - AGG-CLASSIFICATION-SCHEME
  - QRY-CLS-ACTIVE
  operations: 5
  tests:
  - TST-CLASSIFICATION-SCHEME-SM
  status: TRACED
- requirement: REQ-GOV-003
  design_elements:
  - AGG-CLEARANCE
  - QRY-CLR-GET
  operations: 7
  tests:
  - TST-CLEARANCE-SM
  - TST-SLC01-INVARIANTS
  status: TRACED
- requirement: REQ-GOV-004
  design_elements:
  - AGG-CLEARANCE
  operations: 6
  tests:
  - TST-CLEARANCE-SM
  - TST-SLC01-INVARIANTS
  status: TRACED
- requirement: REQ-GOV-008
  design_elements:
  - AGG-PERSON
  operations: 5
  tests:
  - TST-PERSON-SM
  status: TRACED
- requirement: REQ-GOV-009
  design_elements:
  - AGG-CLASSIFICATION-SCHEME
  - AGG-POLICY-SET
  - QRY-POL-GET
  operations: 10
  tests:
  - TST-CLASSIFICATION-SCHEME-SM
  - TST-POLICY-SET-SM
  status: TRACED
- requirement: REQ-OPS-005
  design_elements:
  - AGG-ROLE-ASSIGNMENT
  operations: 2
  tests:
  - TST-ROLE-ASSIGNMENT-SM
  status: TRACED
- requirement: REQ-OPS-009
  design_elements:
  - AGG-ROLE-ASSIGNMENT
  operations: 2
  tests:
  - TST-ROLE-ASSIGNMENT-SM
  status: TRACED
quality:
- qas: QAS-SEC-001
  design: PB-01, tenant_id everywhere, RLS (LDM)
  verification: 'TST-SLC01-INVARIANTS: Cross-tenant'
- qas: QAS-SEC-003
  design: PL-SECURITY-CONTEXT §2, security_versions KV
  verification: 'TST-SLC01-INVARIANTS: Revocation'
- qas: QAS-SEC-005
  design: PB-03, FM-S01-03
  verification: 'TST-SLC01-INVARIANTS: Policy engine failure'
- qas: QAS-SEC-006
  design: audit chains + anchors
  verification: 'TST-SLC01-INVARIANTS: tampering'
- qas: QAS-SEC-008
  design: SCIM → CMD-USR-DISABLE → EVT-SEC-VERSION-INCREMENTED
  verification: 'TST-SLC01-INVARIANTS: SCIM'
- qas: QAS-AUD-001
  design: audit_outbox same transaction (FIT-04)
  verification: 'TST-SLC01-INVARIANTS: atomic audit'
- qas: QAS-PERF-009
  design: embedded evaluators + signed bundles
  verification: performance test (W8 strategy)
- qas: QAS-PERF-010
  design: gateway cache (subject, security_version)
  verification: performance test
- qas: QAS-PERF-011
  design: audit shipper
  verification: performance test
- qas: QAS-SCAL-003
  design: provisioning saga
  verification: provisioning test ≤ 1 h
gaps: []
```

</details>
