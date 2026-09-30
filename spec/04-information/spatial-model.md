---
id: SPATIAL-MODEL
type: architecture
title: Spatial Architecture
wave: W3
tier: T0
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
traces: {decided_by: [ADR-P12, ADR-P16, ADR-P06], requirements: [REQ-INF-008, REQ-INF-028, REQ-INF-029, REQ-INF-030, REQ-SIT-007], corrects: [CR-01, CR-12]}
---

# Spatial Architecture

## 1. الملكية
الموقع والهندسة **قيم (Value Objects)** داخل كائنات BC02، وليست كائنات مستقلة. المالك: **BC02** (CR-01). الكيان من نوع `location` (مكان مسمى) كيان عادي في BC02.

## 2. تمثيل الهندسة

| الحقل | القاعدة |
|---|---|
| `geometry` | GeoJSON في EPSG:4326، ترتيب lon/lat |
| `crs_original`, `coordinates_original` | تُحفظ كما وصلت |
| `accuracy_m` | إلزامي؛ الدقة الموضعية بالمتر (CEP50 عند الإمكان) |
| `accuracy_basis` | measured / reported / estimated / unknown |
| الارتفاع | اختياري: `z` مع `vertical_datum` (افتراضياً EGM2008) |
| الأنواع المسموحة | Point، LineString، Polygon، Multi*، GeometryCollection |

## 3. الصلاحية الهندسية (REQ-INF-028)
رفض: هندسة غير صالحة (تقاطع ذاتي، حلقات غير مغلقة، اتجاه خاطئ بعد التطبيع)، إحداثيات خارج النطاق، غياب CRS أو الدقة. يُسجل الرفض بسبب في الحجر (REQ-INF-006).

## 4. تاريخ الموقع (REQ-INF-030)
موقع الكيان المتحرك سلسلة ادعاءات `location` ثنائية الزمن. المسار (Track) إسقاط مرتب زمنياً من هذه الادعاءات والملاحظات. للبيانات عالية التردد (حساسات): تُخزن كملاحظات مقسمة زمنياً، ويُشتق منها ادعاء موقع مُلخّص بمعدل محدد لكل نوع.

## 5. العمليات المكانية
| العملية | القاعدة |
|---|---|
| intersects, within, contains, bbox | على الهندسة الكانونية |
| distance, area, buffer | جيوديسية، أو بإسقاط محلي مناسب يُسجل في lineage (ADR-P16) |
| nearest neighbor | فهرس مكاني + حد أعلى للمسافة إلزامي |
| زماني-مكاني | الفلتر الزمني يُطبق قبل المكاني للجداول المقسمة زمنياً |

## 6. التقديم والتبادل
- **استيراد:** OGC API Features/Maps/Tiles، WMS/WFS، GeoJSON، GeoPackage، GeoTIFF/COG، KML.
- **تقديم:** Vector tiles للطبقات التشغيلية، وRaster tiles من COG.
- **أمن البلاطات:** ADR-P06 §6. طبقات الأساس الموسومة unclassified فقط قابلة للتخزين المشترك.

## 7. الجودة المكانية (بُعد data_quality)
`SPATIAL_OK | LOW_ACCURACY (accuracy_m > حد النوع) | TRANSFORMED | DEVICE_GPS_SUSPECT`.
