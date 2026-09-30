---
id: CELL-ARCHITECTURE
type: architecture
title: Cell Architecture, Profiles and Capacity Sizing
wave: W8
tier: T0
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
traces: {decided_by: [ADR-P04, ADR-P05], requirements: [REQ-PLT-002, REQ-FND-004, REQ-GOV-005], quality: [QAS-SCAL-001, QAS-SCAL-003]}
---

# Cell Architecture

## 1. الخلية
الخلية = عنقود Kubernetes + كل الخدمات ذات الحالة + كل وحدات النشر، في موقع واحد وولاية واحدة. لا مسار بيانات بين الخلايا (TB-05).

| الملف (profile) | من يدخله | الفرق |
|---|---|---|
| shared | مستأجرون صغار ومتوسطون (≤ 50 لكل خلية، أو حتى 80 % من السعة) | عزل منطقي مزدوج (ADR-P04) |
| dedicated | مستأجر كبير (> 20 % من سعة خلية) أو أعلى تصنيف | نفس الإصدار؛ مستأجر واحد |
| sovereign | متطلب سيادي/موقع | نفس الإصدار؛ موقع ومشغلون محليون |

الترقية من shared إلى dedicated: تصدير/استيراد على مستوى المستأجر (CMD-TEN-START-CELL-MIGRATION).

## 2. تقدير السعة لخلية واحدة عند نطاق التصميم (INF — للتحقق في Pilot)
الافتراضات: 5,000 مستخدم متزامن، 7,500 طلب/ث ذروة، 5,000 ملاحظة/ث مستدامة، 500 بحث/ث، 1e8 ادعاء، 1e9 ملاحظة (مع تقادم ساخن/دافئ).

| المكوّن | التقدير الأولي | الأساس |
|---|---|---|
| PostgreSQL | primary + 2 replicas؛ ~32 vCPU / 256 GB لكل عقدة؛ تخزين NVMe ≈ 10 TB ساخن | WL-01، WL-06a، LDM partitioning |
| Kafka | 3 brokers (KRaft) ~8 vCPU / 32 GB؛ احتفاظ 7 أيام | WL-06a (50k/s burst) |
| OpenSearch | 3 master + 6 data (~16 vCPU / 64 GB) | WL-02a/b |
| Valkey | 3 عقد (primary + replicas) | WL-01c |
| Object storage | يبدأ بـ ~100 TB قابل للتوسع | WL-05a، WL-11c |
| وحدات بلا حالة | ~60–120 pod عند الذروة | derived from latency budgets |
| Analysis jobs | حسب الحصص (مثلاً 64–256 vCPU) | WL-11b |

**قاعدة المعايرة:** كل رقم هنا فرضية حتى اختبار الأداء (PERF-TEST-STRATEGY). إذا تجاوز الحمل الفعلي 50 % من نطاق التصميم تُعاد المعايرة (ASM-010).

## 3. الخروج الشبكي والإقامة (REQ-GOV-005)
- NetworkPolicy افتراضية: **منع كل خروج**؛ استثناءات صريحة للمحولات (إلى أنظمة داخلية مسجلة) عبر egress gateway بقائمة سماح لكل خلية.
- الخلية في ولاية واحدة؛ النسخ الاحتياطية وموقع DR في نفس الولاية.
- مراقبة الخروج: أي اتصال خارج القائمة = تنبيه أمني P1 (التحقق في W9).
