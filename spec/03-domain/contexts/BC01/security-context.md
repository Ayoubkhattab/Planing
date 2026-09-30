---
id: PL-SECURITY-CONTEXT
type: published-language
title: SecurityContext (Published Language of BC01)
wave: W4
tier: T0
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
slice: SLC-01
traces: {requirements: [REQ-FND-010, REQ-FND-011, REQ-GOV-004], decided_by: [ADR-P06], quality: [QAS-PERF-010, QAS-SEC-003]}
---

# SecurityContext — اللغة المنشورة لـ BC01

كل طلب داخل المنصة يحمل SecurityContext. تبنيه البوابة من رمز الدخول وبيانات BC01، وتوقعه، وتمرره للتطبيقات عبر حد الثقة TB-02.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:platform:schema:security-context:1",
  "type": "object",
  "required": ["tenant_id", "cell_id", "subject", "roles", "clearance", "auth", "security_version", "issued_at", "expires_at"],
  "properties": {
    "tenant_id": {"type": "string"},
    "cell_id": {"type": "string"},
    "subject": {"type": "object", "required": ["urn", "kind"], "properties": {
      "urn": {"type": "string"}, "kind": {"enum": ["user", "service_account"]},
      "person_urn": {"type": ["string", "null"]}, "on_behalf_of": {"type": ["string", "null"]}}},
    "roles": {"type": "array", "items": {"type": "object", "required": ["role", "org_scope", "include_descendants"], "properties": {
      "role": {"type": "string"}, "org_scope": {"type": "string"}, "include_descendants": {"type": "boolean"}}}},
    "clearance": {"type": "object", "required": ["max_level", "compartments"], "properties": {
      "max_level": {"type": "string"}, "compartments": {"type": "array", "items": {"type": "string"}},
      "caveat_attributes": {"type": "object"}}},
    "auth": {"type": "object", "required": ["method", "strength", "auth_time"], "properties": {
      "method": {"enum": ["oidc", "saml", "workload"]}, "strength": {"enum": ["single_factor", "mfa"]},
      "auth_time": {"type": "string", "format": "date-time"}, "device_urn": {"type": ["string", "null"]}}},
    "security_version": {"type": "integer", "minimum": 1},
    "issued_at": {"type": "string", "format": "date-time"},
    "expires_at": {"type": "string", "format": "date-time", "description": "≤ issued_at + 60 s"}
  },
  "additionalProperties": false
}
```

## القواعد
1. **العمر ≤ 60 ثانية** داخلياً؛ رمز الجلسة الخارجي ≤ 15 دقيقة مع تجديد (W4 delegated decisions).
2. **فحص الإصدار في كل طلب:** الـ PEP يقارن `security_version` في السياق مع القيمة الحالية في مخزن الإصدارات الأمنية (key-value سريع). إن كان أقدم → يُعاد بناء السياق قبل التقييم. هذا ما يجعل السحب فورياً (QAS-SEC-003) دون انتظار انتهاء العمر.
3. **الغرض (purpose)** لا يُخزن في السياق؛ يأتي في ترويسة `X-Purpose` لكل طلب ويُقيّم في السياسة.
4. **لا صلاحيات محسوبة داخل السياق** سوى الأدوار والتصريح؛ القرار دائماً من PDP.
5. التوقيع: JWS بمفتاح البوابة في الخلية؛ التطبيقات ترفض أي سياق غير موقّع أو منتهٍ.
