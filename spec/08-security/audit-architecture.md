---
id: AUDIT-ARCHITECTURE
type: architecture
title: Audit Architecture (revised in SLC-01)
wave: W3→W4
tier: T0
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
traces: {requirements: [REQ-FND-015, REQ-FND-016], quality: [QAS-AUD-001, QAS-SEC-006, QAS-PERF-011], corrects: [CR-45]}
---

# Audit Architecture

## لماذا عُدّل في SLC-01 (CR-45)
التصميم في W3 كان يكتب سجل التدقيق "في نفس معاملة" تغيير الحالة داخل مخزن BC08، مع سلسلة hash واحدة متتابعة لكل مستأجر. عند تصميم الشريحة ظهر خللان:
1. **تعارض مع الملكية:** معاملة سياق BC04 لا يمكنها الكتابة في مخزن BC08 (FIT-01).
2. **عنق زجاجة توسعي:** تسلسل واحد بلا فجوات لكل مستأجر يُسلسل كل الكتابات؛ عند ~2,000 سجل/ث في الذروة يصبح نقطة اختناق (SR-00).

## التصميم المعدل

```text
Context transaction (any BC)
  ├── state change + history
  ├── outbox (domain events)
  └── audit_outbox (append-only, owned by the context)      ← نفس المعاملة: لا تغيير بلا تدقيق
            │ shipper (at-least-once, ≤ 5 s — QAS-PERF-011)
            ▼
BC08 Audit Store
  ├── dedupe by audit_id
  ├── assign seq per (tenant, shard)   shard = hash(resource_urn) mod N   (N = 16 default, increase by resharding epochs)
  ├── hash chain per (tenant, shard):  hash = H(prev_hash ‖ canonical(record))
  └── anchor every 5 min: Merkle root over all shard heads → write-once anchor store
```

## القواعد
1. `audit_outbox` في كل سياق: صلاحيات إدراج فقط، لا تعديل ولا حذف لحساب التطبيق.
2. نافذة ما قبل الشحن قصيرة (≤ 5 ث في الحالة الطبيعية)؛ فجوات الشحن تُكشف بمقارنة عدادات الإدراج في المصدر مع المستلم.
3. **التدهور:** إذا تعطل مخزن BC08، تتراكم السجلات محلياً والأوامر تستمر. إذا تجاوز التراكم 24 ساعة أو 80 % من السعة المخصصة → **الأوامر المغيرة للحالة تُرفض** (`AUDIT_UNAVAILABLE`) — لا تغيير بلا تدقيق مضمون.
4. قراءات البيانات فوق عتبة التدقيق: PEP يكتب سجلها في audit_outbox لسياق القراءة (غير متزامن مع الاستجابة لكن مضمون الشحن).
5. التحقق (QAS-SEC-006): إعادة حساب السلاسل يومياً ومقارنة الجذور بالمثبتات.
6. البحث في التدقيق للـ Auditor وSecurity Officer، وكل بحث مدقق بدوره.

## السجل
```text
AuditRecord
  audit_id (ULID, assigned in source context), tenant_id, source_context
  actor {urn, kind, on_behalf_of}, action, resource {urn, type, labels}
  purpose, policy_decision {decision, reason_code, policy_version}
  outcome {success|rejected, error_code}, correlation_id, causation_id, occurred_at
  -- assigned by BC08 --
  shard, seq, prev_hash, hash, anchor_ref
```
