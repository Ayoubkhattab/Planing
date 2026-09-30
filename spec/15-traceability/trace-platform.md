---
id: TRACE-PLATFORM
type: traceability-matrix
title: Traceability — cross-cutting platform requirements (not owned by a domain slice)
wave: W7 → W8
status: GENERATED
notes: كل متطلبات المنصة الخمسة عشر متتبعة الآن (8 في SLC-12a، 7 في W8).
---

# Traceability — cross-cutting platform requirements (not owned by a domain slice)

> كل متطلبات المنصة الخمسة عشر متتبعة الآن (8 في SLC-12a، 7 في W8).

## requirements

_15 items_

### 

- **requirement:** REQ-GOV-002
- **design:** LABEL-DERIVATION (54 aggregates) + SL-29
- **verification:** contract lint: creation commands of explicit-label aggregates require label
- **status:** TRACED

### 

- **requirement:** REQ-GOV-005
- **design:** CELL-ARCHITECTURE §3 (default-deny egress, allow-listed egress gateway); egress monitoring test in PERF/security suite
- **verification:** egress monitoring test in W9 verification plan
- **status:** TRACED (W8)

### 

- **requirement:** REQ-PLT-001
- **design:** FIT-12 (no external network at runtime/build)
- **verification:** isolated-network CI stage
- **status:** TRACED

### 

- **requirement:** REQ-PLT-002
- **design:** RELEASE-CONFIG-MIGRATION §1 (one Zarf bundle; profiles as values; acceptance on 3 profiles)
- **verification:** same-release acceptance across shared/dedicated/sovereign modes
- **status:** TRACED (W8)

### 

- **requirement:** REQ-PLT-003
- **design:** observability-slc* (8 slices) + correlation id in every contract (X-Correlation-Id)
- **verification:** QAS-OBS-001 trace test
- **status:** TRACED

### 

- **requirement:** REQ-PLT-004
- **design:** DR-CONTINUITY §1–2 (tier per DU; DR drills)
- **verification:** DR drills per tier (W9 plan)
- **status:** TRACED (W8)

### 

- **requirement:** REQ-PLT-005
- **design:** async jobs specified: analysis runs, imports, builds, disposition, sync
- **verification:** API lint: no synchronous heavy operations (operations list)
- **status:** TRACED

### 

- **requirement:** REQ-PLT-006
- **design:** outbox/inbox in every LDM + AsyncAPI per slice; FIT-04
- **verification:** fault-injection test at commit
- **status:** TRACED

### 

- **requirement:** REQ-PLT-007
- **design:** OpenAPI 3.1 / AsyncAPI 3 versioned per slice; FIT-14
- **verification:** contract compatibility check
- **status:** TRACED

### 

- **requirement:** REQ-PLT-008
- **design:** cursor parameters in all generated list operations; FIT-13
- **verification:** OpenAPI lint
- **status:** TRACED

### 

- **requirement:** REQ-PLT-009
- **design:** ApiError schema in every generated OpenAPI
- **verification:** OpenAPI lint
- **status:** TRACED

### 

- **requirement:** REQ-PLT-010
- **design:** UI-ARCHITECTURE (i18n ICU, RTL, Hijri display)
- **verification:** bilingual/RTL UI review (W9)
- **status:** TRACED (W8)

### 

- **requirement:** REQ-PLT-011
- **design:** UI-ARCHITECTURE (web 360 px+, React Native field app)
- **verification:** UI acceptance (W9)
- **status:** TRACED (W8)

### 

- **requirement:** REQ-PLT-012
- **design:** DR-CONTINUITY §2 (backups per store, automated restore tests, restore gate)
- **verification:** scheduled restore tests (W9 plan)
- **status:** TRACED (W8)

### 

- **requirement:** REQ-PLT-013
- **design:** COST-MODEL + OpenCost (TD-14)
- **verification:** monthly per-tenant cost report (W9)
- **status:** TRACED (W8)

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
requirements:
- requirement: REQ-GOV-002
  design: LABEL-DERIVATION (54 aggregates) + SL-29
  verification: 'contract lint: creation commands of explicit-label aggregates require label'
  status: TRACED
- requirement: REQ-GOV-005
  design: CELL-ARCHITECTURE §3 (default-deny egress, allow-listed egress gateway); egress monitoring test in PERF/security
    suite
  verification: egress monitoring test in W9 verification plan
  status: TRACED (W8)
- requirement: REQ-PLT-001
  design: FIT-12 (no external network at runtime/build)
  verification: isolated-network CI stage
  status: TRACED
- requirement: REQ-PLT-002
  design: RELEASE-CONFIG-MIGRATION §1 (one Zarf bundle; profiles as values; acceptance on 3 profiles)
  verification: same-release acceptance across shared/dedicated/sovereign modes
  status: TRACED (W8)
- requirement: REQ-PLT-003
  design: observability-slc* (8 slices) + correlation id in every contract (X-Correlation-Id)
  verification: QAS-OBS-001 trace test
  status: TRACED
- requirement: REQ-PLT-004
  design: DR-CONTINUITY §1–2 (tier per DU; DR drills)
  verification: DR drills per tier (W9 plan)
  status: TRACED (W8)
- requirement: REQ-PLT-005
  design: 'async jobs specified: analysis runs, imports, builds, disposition, sync'
  verification: 'API lint: no synchronous heavy operations (operations list)'
  status: TRACED
- requirement: REQ-PLT-006
  design: outbox/inbox in every LDM + AsyncAPI per slice; FIT-04
  verification: fault-injection test at commit
  status: TRACED
- requirement: REQ-PLT-007
  design: OpenAPI 3.1 / AsyncAPI 3 versioned per slice; FIT-14
  verification: contract compatibility check
  status: TRACED
- requirement: REQ-PLT-008
  design: cursor parameters in all generated list operations; FIT-13
  verification: OpenAPI lint
  status: TRACED
- requirement: REQ-PLT-009
  design: ApiError schema in every generated OpenAPI
  verification: OpenAPI lint
  status: TRACED
- requirement: REQ-PLT-010
  design: UI-ARCHITECTURE (i18n ICU, RTL, Hijri display)
  verification: bilingual/RTL UI review (W9)
  status: TRACED (W8)
- requirement: REQ-PLT-011
  design: UI-ARCHITECTURE (web 360 px+, React Native field app)
  verification: UI acceptance (W9)
  status: TRACED (W8)
- requirement: REQ-PLT-012
  design: DR-CONTINUITY §2 (backups per store, automated restore tests, restore gate)
  verification: scheduled restore tests (W9 plan)
  status: TRACED (W8)
- requirement: REQ-PLT-013
  design: COST-MODEL + OpenCost (TD-14)
  verification: monthly per-tenant cost report (W9)
  status: TRACED (W8)
```

</details>
