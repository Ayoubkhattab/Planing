---
id: RELEASE-CONFIG-MIGRATION
type: architecture
title: Release, Configuration & Migration
tier: T2
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
wave: W8
traces: {requirements: [REQ-PLT-001, REQ-PLT-002, REQ-PLT-007], quality: [QAS-OPS-001, QAS-EVO-001], decided_by: [TD-17]}
---

# Release, Configuration & Migration

## 1. الإصدار (REQ-PLT-002)
- **حزمة واحدة لكل إصدار** (Zarf): صور موقعة + SBOM + مخططات Helm + ترحيلات قاعدة البيانات + حزم السياسات الأساسية.
- ملفات الخلية (shared / dedicated / sovereign) **قيم تهيئة** لا نسخ مختلفة من الكود.
- مجموعة القبول نفسها تُشغّل على الملفات الثلاثة قبل اعتماد الإصدار.
- الترقية: blue/green للوحدات بلا حالة؛ ترحيلات expand/contract؛ رجوع ≤ ساعة (QAS-OPS-001).

## 2. التهيئة (V5 #85)
| النوع | المكان | التغيير |
|---|---|---|
| منصة (موارد، إصدارات، شبكة) | Git داخل الموقع + Argo CD | مراجعة شخصين |
| مستأجر (حصص، سياسات، تصنيف، احتفاظ، أنواع المهام…) | Aggregates في BC01/BC08/BC04 (مُدققة ومُصدرة) | عبر الأوامر المعرفة |
| أسرار | OpenBao | لا أسرار في Git أو الصور |

## 3. الترحيل (V5 #87)
- لا ترحيل من أنظمة قديمة في R1 (UNK-014 مغلق): الاستيراد عبر المحولات ودفعات الاستيراد (SLC-02).
- ترحيل المخططات: أمامي فقط؛ لا حذف عمود في نفس الإصدار الذي يتوقف عن استخدامه.
- الإسقاطات: إصدار جديد + ترقية (AGG-PROJECTION-VERSION).
- العقود: إصدار رئيسي جديد يتعايش ≥ 6 أشهر (QAS-EVO-001).
