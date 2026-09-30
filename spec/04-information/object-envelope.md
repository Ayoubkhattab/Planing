---
id: OBJECT-ENVELOPE
type: schema
title: Object Envelope v1 (corrected)
wave: W3
tier: T0
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
traces: {corrects: [CR-03, CR-04, CR-27], decided_by: [ADR-P01, ADR-P03, ADR-P04, ADR-P06, ADR-P08, ADR-P13, ADR-P16]}
---

# Object Envelope v1

الحزمة المشتركة لكل كائن. **عقد منطقي، وليس جدولاً واحداً** (PRJ§11). الكائنات تضمّن الأقسام التي تنطبق على مستوى أهميتها فقط.

## ما تغيّر عن PRJ§11

| PRJ§11 | v1 | السبب |
|---|---|---|
| `updated.by/at` | حُذف؛ استُبدل بـ `version` + `recorded_from` | CR-27: لا كتابة فوق القيم |
| `temporal.valid_from/to, observed_at, recorded_at` | فترتا `valid` و`record` + `event_time` بدقة + `observed_at` + `effective` | CR-04، ADR-P01 |
| `confidence.score/quality/freshness` | سبعة أبعاد بلا درجة مجمعة إلزامية | CR-03 |
| `security.classification/policy_id/access_scope` | `level, compartments, caveats, org_scope, security_version, personal_data` | ADR-P06، P08 |
| `spatial.geometry/crs` | canonical + original + accuracy | ADR-P16 |
| — | `importance_tier`، `urn` | ADR-P03، P13 |

## قواعد الحقول حسب المستوى

| القسم | T1 | T2 | T3 | T4 |
|---|---|---|---|---|
| identity, tenant, type, schema_version | إلزامي | إلزامي | إلزامي | إلزامي |
| version | — (الادعاءات هي التاريخ) | إلزامي | إلزامي | اختياري |
| temporal.valid / record | إلزامي | effective + recorded_at | — | — |
| provenance.source_refs | إلزامي (≥1) | عند الاشتقاق | — | — |
| confidence | إلزامي | — | — | — |
| security.level | إلزامي | إلزامي | يرث من الحاوي | — |
| audit | إلزامي | إلزامي | إلزامي | — |

## JSON Schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:platform:schema:object-envelope:1",
  "title": "ObjectEnvelope",
  "type": "object",
  "required": ["id", "urn", "tenant_id", "object_type", "schema_version", "importance_tier", "security", "audit"],
  "properties": {
    "id": {"type": "string", "pattern": "^[0-9A-HJKMNP-TV-Z]{26}$", "description": "ULID"},
    "urn": {"type": "string", "pattern": "^urn:[a-z0-9-]+:[a-z0-9-]+:[0-9A-HJKMNP-TV-Z]{26}$"},
    "tenant_id": {"type": "string"},
    "object_type": {"type": "string", "description": "code from reference data RD-OBJECT-TYPES"},
    "schema_version": {"type": "integer", "minimum": 1},
    "version": {"type": "integer", "minimum": 1, "description": "T2/T3 optimistic concurrency and version history"},
    "importance_tier": {"enum": ["T1", "T2", "T3", "T4"]},
    "lifecycle_state": {"type": "string"},
    "temporal": {
      "type": "object",
      "properties": {
        "valid_from": {"type": ["string", "null"], "format": "date-time"},
        "valid_to": {"type": ["string", "null"], "format": "date-time"},
        "recorded_from": {"type": "string", "format": "date-time", "description": "server-assigned"},
        "recorded_to": {"type": ["string", "null"], "format": "date-time", "description": "server-assigned"},
        "event_time": {"$ref": "#/$defs/fuzzyInterval"},
        "observed_at": {"type": ["string", "null"], "format": "date-time"},
        "effective_from": {"type": ["string", "null"], "format": "date-time"},
        "effective_to": {"type": ["string", "null"], "format": "date-time"}
      }
    },
    "spatial": {
      "type": "object",
      "required": ["geometry", "accuracy_m"],
      "properties": {
        "geometry": {"type": "object", "description": "GeoJSON geometry in EPSG:4326"},
        "crs_original": {"type": "string", "pattern": "^EPSG:[0-9]+$"},
        "coordinates_original": {"type": "object"},
        "accuracy_m": {"type": "number", "minimum": 0},
        "accuracy_basis": {"enum": ["measured", "reported", "estimated", "unknown"]}
      }
    },
    "provenance": {
      "type": "object",
      "properties": {
        "source_refs": {"type": "array", "items": {"type": "string"}},
        "lineage_ref": {"type": ["string", "null"]},
        "derived_from": {"type": "array", "items": {"type": "string"}}
      }
    },
    "confidence": {"$ref": "urn:platform:schema:confidence:1"},
    "security": {
      "type": "object",
      "required": ["level", "security_version"],
      "properties": {
        "level": {"type": "string", "description": "code from tenant classification scheme"},
        "compartments": {"type": "array", "items": {"type": "string"}},
        "caveats": {"type": "array", "items": {"type": "string"}},
        "org_scope": {"type": "string", "description": "owning org unit URN"},
        "security_version": {"type": "integer", "minimum": 1},
        "personal_data": {"type": "boolean", "default": false}
      }
    },
    "audit": {
      "type": "object",
      "required": ["created_by", "correlation_id"],
      "properties": {
        "created_by": {"type": "string"},
        "correlation_id": {"type": "string"},
        "causation_id": {"type": ["string", "null"]},
        "trace_id": {"type": ["string", "null"]}
      }
    }
  },
  "$defs": {
    "fuzzyInterval": {
      "type": ["object", "null"],
      "required": ["precision"],
      "properties": {
        "start": {"type": ["string", "null"], "format": "date-time"},
        "end": {"type": ["string", "null"], "format": "date-time"},
        "precision": {"enum": ["instant", "second", "minute", "hour", "day", "month", "year", "decade", "unknown"]},
        "uncertainty_before": {"type": ["string", "null"], "description": "ISO 8601 duration"},
        "uncertainty_after": {"type": ["string", "null"], "description": "ISO 8601 duration"}
      }
    }
  }
}
```
