"""Arabic terms used by build_analysis_design.py.

Aggregate names prefer the binding glossary (spec/00-governance/glossary.md) where it has the term;
the rest are study translations. Verb phrases are verbal nouns; '{a}' is replaced by the aggregate name.
"""

AGGREGATES = {
    # BC01
    "AGG-AUTHORITY-GRANT": "منح السلطة", "AGG-CLEARANCE": "التصريح الأمني", "AGG-DEVICE": "الجهاز الميداني",
    "AGG-HR-SYNC-PROPOSAL": "مقترح مزامنة الموارد البشرية", "AGG-ORGANIZATION": "المؤسسة", "AGG-PERSON": "الشخص",
    "AGG-ROLE-ASSIGNMENT": "إسناد الدور", "AGG-ROLE": "الدور", "AGG-SERVICE-ACCOUNT": "حساب الخدمة",
    "AGG-TENANT": "المستأجر", "AGG-USER": "حساب المستخدم",
    # BC02
    "AGG-ATTACHMENT": "المرفق", "AGG-CLAIM": "الادعاء", "AGG-COLLECTION-PLAN": "خطة الجمع",
    "AGG-COLLECTION-REQUIREMENT": "متطلب الجمع", "AGG-CONFLICT": "التعارض", "AGG-CORRELATION-PROPOSAL": "مقترح الربط",
    "AGG-CORRELATION-RULE": "قاعدة الربط", "AGG-ENTITY": "الكيان", "AGG-ER-CASE": "حالة مطابقة الكيانات",
    "AGG-EVIDENCE-LINK": "رابط الدليل", "AGG-EVIDENCE": "الدليل", "AGG-EXTERNAL-ID": "ربط المعرّف الخارجي",
    "AGG-IMPORT-BATCH": "دفعة الاستيراد", "AGG-MATCH-RULESET": "مجموعة قواعد المطابقة", "AGG-OBSERVATION": "الملاحظة",
    "AGG-REALWORLD-EVENT": "الحدث الواقعي", "AGG-RELATIONSHIP": "العلاقة", "AGG-SOURCE": "المصدر",
    # BC03
    "AGG-ALERT-RULE": "قاعدة التنبيه", "AGG-ALERT": "التنبيه", "AGG-ANALYSIS-CASE": "حالة التحليل",
    "AGG-ANALYSIS-METHOD": "طريقة التحليل", "AGG-ANALYSIS-RUN": "تشغيل التحليل", "AGG-ASSESSMENT": "التقييم",
    "AGG-CAP-MESSAGE": "رسالة CAP الصادرة", "AGG-FINDING": "النتيجة التحليلية", "AGG-SITUATION": "الموقف",
    # BC04
    "AGG-COORDINATION-CASE": "حالة التنسيق", "AGG-DECISION-REQUEST": "طلب القرار", "AGG-DECISION": "القرار",
    "AGG-INCIDENT": "الحادثة", "AGG-NOTIFICATION": "الإشعار", "AGG-OUTCOME-TRACKER": "متتبّع النتائج",
    "AGG-PLAN-VERSION": "إصدار الخطة", "AGG-PLAN": "الخطة", "AGG-RISK": "الخطر", "AGG-SUBSCRIPTION": "الاشتراك",
    "AGG-TASK-TYPE": "نوع المهمة", "AGG-TASK": "المهمة",
    # BC05
    "AGG-ALLOCATION": "تخصيص الموارد", "AGG-ASSET-ASSIGNMENT": "إسناد الأصل", "AGG-ASSET-RESERVATION": "حجز الأصل",
    "AGG-ASSET": "الأصل", "AGG-EXERCISE": "التمرين", "AGG-LOGISTICS-REQUEST": "طلب الإمداد",
    "AGG-MAINTENANCE-ORDER": "أمر الصيانة", "AGG-QUALIFICATION-RECORD": "سجل التأهيل", "AGG-RESOURCE-POOL": "مجمع الموارد",
    "AGG-ROLE-REQUIREMENT": "متطلبات الدور", "AGG-SCENARIO": "سيناريو التدريب", "AGG-SHIPMENT": "الشحنة",
    "AGG-SIMULATION": "تشغيل المحاكاة",
    # BC06
    "AGG-ARCHIVE-PACKAGE": "الحزمة الأرشيفية", "AGG-DISTRIBUTION": "التوزيع", "AGG-KNOWLEDGE-OBJECT": "كائن المعرفة",
    "AGG-PRODUCT-TEMPLATE": "قالب المنتج", "AGG-PRODUCT": "المنتج", "AGG-RECONSTRUCTION": "إعادة البناء التاريخي",
    # BC07
    "AGG-ADAPTER": "المحوّل", "AGG-AI-REQUEST": "طلب الذكاء الاصطناعي", "AGG-AI-RESULT": "نتيجة الذكاء الاصطناعي",
    "AGG-AI-ROUTING": "توجيه الذكاء الاصطناعي", "AGG-AI-TOOL": "أداة الذكاء الاصطناعي", "AGG-EVAL-SUITE": "حزمة التقييم",
    "AGG-INTEGRATION-CONNECTION": "اتصال التكامل", "AGG-MODEL-VERSION": "إصدار النموذج",
    "AGG-PRELOAD-PACKAGE": "حزمة التحميل المسبق", "AGG-PROJECTION-VERSION": "إصدار الإسقاط",
    "AGG-SENSOR-STREAM": "تدفق الحسّاس", "AGG-SYNC-CONFLICT": "تعارض المزامنة", "AGG-SYNC-SESSION": "جلسة المزامنة",
    # BC08
    "AGG-CLASSIFICATION-SCHEME": "مخطط التصنيف", "AGG-DISPOSITION-RUN": "تشغيل الإتلاف",
    "AGG-ERASURE-REQUEST": "طلب المحو", "AGG-LEGAL-HOLD": "التجميد القانوني", "AGG-POLICY-SET": "مجموعة السياسات",
    "AGG-RETENTION-SCHEDULE": "جدول الاحتفاظ", "AGG-SECURITY-EXCEPTION": "الاستثناء الأمني",
}

VERBS = {
    "ABORT": "إيقاف {a} نهائيًا مع السبب", "ACCEPT": "قبول {a}", "ACCEPT-PARTIALLY": "قبول {a} جزئيًا",
    "ACCEPT-QUARANTINE": "قبول العناصر المعزولة في {a}", "ACKNOWLEDGE": "الإقرار باستلام {a}", "ACTIVATE": "تفعيل {a}",
    "ACTIVATE-CONTINGENCY": "تفعيل خطة الاستمرارية لـ{a}", "ADD-ACTIVITY": "إضافة نشاط إلى {a}",
    "ADD-ASSUMPTION": "إضافة افتراض إلى {a}", "ADD-HYPOTHESIS": "إضافة فرضية إلى {a}", "ADD-OPTION": "إضافة خيار إلى {a}",
    "ADD-PARTICIPANT": "إضافة مشارك إلى {a}", "ADD-RESULT-ITEM": "إضافة بند نتيجة إلى {a}",
    "ADD-UNIT": "إضافة وحدة تنظيمية إلى {a}", "ADJUST-CAPACITY": "تعديل سعة {a}", "AMEND": "تعديل {a} بإصدار جديد",
    "AMEND-MINOR": "تعديل طفيف على {a}", "ANNUL": "إبطال {a}", "APPROVE": "اعتماد {a}", "APPROVE-GRANT": "اعتماد {a}",
    "APPROVE-RELEASE": "اعتماد إصدار {a}", "ASSERT": "تسجيل {a}", "ASSESS": "تقييم {a}", "ASSIGN": "إسناد {a}",
    "ASSIGN-RESPONSIBILITY": "إسناد مسؤولية ضمن {a}", "ATTACH-EVIDENCE": "إرفاق دليل بـ{a}", "BLOCK": "تعليق {a} كمحجوب",
    "CANCEL": "إلغاء {a}", "CANCEL-BUILD": "إلغاء بناء {a}", "CANCEL-RELEASE": "إلغاء إصدار {a}",
    "CHANGE-TYPE": "تغيير نوع {a}", "CITE": "الاستشهاد في {a}", "CLOSE": "إغلاق {a}", "COMPLETE": "إكمال {a}",
    "COMPLETE-CELL-MIGRATION": "إكمال ترحيل {a} إلى خلية أخرى", "COMPLETE-DECOMMISSION": "إكمال إخراج {a} من الخدمة",
    "COMPLETE-PROVISIONING": "إكمال تهيئة {a}", "COMPLETE-UPLOAD": "إكمال رفع {a}", "CONFIRM": "تأكيد {a}",
    "CONFIRM-DOWNLOAD": "تأكيد تنزيل {a}", "CONFIRM-MATCH": "تأكيد تطابق {a}", "CONTAIN": "احتواء {a}",
    "CORRECT": "تصحيح {a}", "CREATE": "إنشاء {a}", "CREATE-VERSION": "إنشاء إصدار جديد من {a}",
    "DE-ESCALATE": "خفض خطورة {a}", "DEACTIVATE": "إيقاف تفعيل {a}", "DEACTIVATE-UNIT": "إيقاف وحدة تنظيمية في {a}",
    "DECIDE-MATCH": "الحكم بتطابق {a}", "DECIDE-NOT-MATCH": "الحكم بعدم تطابق {a}", "DECLINE": "رفض قبول {a}",
    "DEFINE": "تعريف {a}", "DEFINE-SCENARIO": "تعريف سيناريو ضمن {a}", "DELEGATE": "تفويض {a}", "DELIVER": "تسليم {a}",
    "DELIVER-INJECT": "تسليم حقنة سيناريو ضمن {a}", "DEPART": "بدء نقل {a}", "DEPRECATE": "إهمال {a} (إيقاف الاستخدام الجديد)",
    "DESELECT-EVIDENCE": "استبعاد دليل من {a}", "DISABLE": "تعطيل {a}", "DISCARD": "تجاهل مسودة {a}",
    "DISMISS": "صرف النظر عن {a}", "DISPATCH": "إرسال {a}", "DISPATCH-RESPONSE": "توجيه الاستجابة لـ{a}",
    "DISPOSE": "التخلص من {a}", "DISTRIBUTE": "توزيع {a}", "DRAFT": "إعداد مسودة {a}", "EDIT": "تعديل {a}",
    "EDIT-DEFINITION": "تعديل تعريف {a}", "EDIT-NARRATIVE": "تعديل سرد {a}", "ENABLE": "تمكين {a}", "END": "إنهاء {a}",
    "ENROLL": "تسجيل {a}", "ERASE": "محو {a}", "ESCALATE": "تصعيد {a}", "EXTEND": "تمديد {a}",
    "FAIL-EVALUATION": "تسجيل فشل تقييم {a}", "FAIL-MAINTENANCE": "تسجيل فشل صيانة {a}",
    "FAIL-PROVISIONING": "تسجيل فشل تهيئة {a}", "FAIL-TEST": "تسجيل فشل اختبار {a}", "GENERATE": "توليد {a}",
    "GRANT": "منح {a}", "HOLD": "تعليق {a} مؤقتًا", "IDENTIFY": "تحديد {a}", "INITIATE-UPLOAD": "بدء رفع {a}",
    "LINK": "ربط {a}", "LINK-IDENTITY": "ربط هوية خارجية بـ{a}", "LINK-PERSON": "ربط شخص بـ{a}", "LOCK": "قفل {a}",
    "MAP": "تسجيل ربط {a}", "MARK-READ": "تعليم {a} كمقروء", "MARK-READY": "تعليم {a} كجاهز",
    "MARK-SATISFIED": "تعليم {a} كمستوفى", "MARK-UNSERVICEABLE": "تعليم {a} كغير صالح للخدمة",
    "MIGRATE-FORMAT": "ترحيل صيغة {a}", "MODIFY": "تعديل {a}", "MOVE-UNIT": "نقل وحدة تنظيمية في {a}", "OPEN": "فتح {a}",
    "PARK": "تأجيل {a}", "PAUSE": "إيقاف {a} مؤقتًا", "PLACE": "إنشاء {a}", "PLAN": "تخطيط {a}",
    "PLAN-TREATMENT": "تخطيط معالجة {a}", "PREEMPT": "استباق {a} بأولوية أعلى", "PREPARE": "إعداد {a}",
    "PROMOTE": "ترقية {a}", "PROPOSE": "اقتراح {a}", "PROVISION": "تهيئة {a}", "PUBLISH": "نشر {a}", "RAISE": "رفع {a}",
    "RATE-RELIABILITY": "تقدير موثوقية {a}", "REACTIVATE": "إعادة تفعيل {a}", "REAPPLY": "إعادة تطبيق {a}",
    "REASSESS": "إعادة تقييم {a}", "REASSIGN": "إعادة إسناد {a}", "RECLASSIFY": "إعادة تصنيف {a}", "RECORD": "تسجيل {a}",
    "RECORD-CHANGE": "تسجيل تغيير في {a}", "RECORD-CHECKPOINT": "تسجيل نقطة عبور لـ{a}",
    "RECORD-CONSUMPTION": "تسجيل استهلاك {a}", "RECORD-EVALUATION": "تسجيل تقييم ضمن {a}",
    "RECORD-FIRST-SIGN-IN": "تسجيل أول دخول لـ{a}", "RECORD-REUSE": "تسجيل إعادة استخدام {a}", "RECOVER": "استعادة {a}",
    "REGISTER": "تسجيل {a}", "REINSTATE": "إعادة {a} إلى السريان", "REJECT": "رفض {a}", "REJECT-GRANT": "رفض {a}",
    "RELEASE": "تحرير {a}", "REMOVE-ACTIVITY": "إزالة نشاط من {a}", "REMOVE-PARTICIPANT": "إزالة مشارك من {a}",
    "RENAME": "إعادة تسمية {a}", "RENAME-UNIT": "إعادة تسمية وحدة تنظيمية في {a}", "RENEW": "تجديد {a}",
    "REOPEN": "إعادة فتح {a}", "REPAIR": "إصلاح {a}", "REPORT": "الإبلاغ عن {a}", "REPORT-DAMAGE": "الإبلاغ عن تلف {a}",
    "REPORT-LOST": "الإبلاغ عن فقد {a}", "REPROCESS-QUARANTINE": "إعادة معالجة العناصر المعزولة في {a}",
    "REPRODUCE": "إعادة إنتاج {a}", "REQUEST": "طلب {a}", "REQUEST-DECISION": "طلب قرار ضمن {a}",
    "REQUEST-RELEASE": "طلب إصدار {a}", "REQUEST-SPLIT": "طلب فصل {a}", "RESCHEDULE": "إعادة جدولة {a}",
    "RESOLVE": "حل {a}", "RESOLVE-MANUALLY": "حل {a} يدويًا", "RESUME": "استئناف {a}", "RETIRE": "إحالة {a} إلى التقاعد",
    "RETIRE-ASSUMPTION": "سحب افتراض من {a}", "RETRACT": "سحب {a}", "RETRY": "إعادة محاولة {a}",
    "RETRY-INGEST": "إعادة محاولة استيعاب {a}", "RETRY-PROVISIONING": "إعادة محاولة تهيئة {a}", "RETURN": "إعادة {a} للمراجعة",
    "RETURN-TO-SERVICE": "إعادة {a} إلى الخدمة", "REVOKE": "سحب {a}", "ROTATE-CREDENTIAL": "تدوير بيانات اعتماد {a}",
    "ROTATE-KEY": "تدوير مفتاح {a}", "SCHEDULE": "جدولة {a}", "SEAL": "ختم {a}", "SELECT-EVIDENCE": "اختيار دليل لـ{a}",
    "SET-CERTIFICATION": "تحديد شهادة {a}", "SET-DUE": "تحديد موعد استحقاق {a}", "SET-PERMISSIONS": "تحديد صلاحيات {a}",
    "SET-PROTECTION": "تحديد مستوى حماية {a}", "SET-QUALITY-RULES": "تحديد قواعد جودة {a}", "SPLIT": "فصل {a}",
    "STAGE": "تجهيز {a} للإنتاج", "START": "بدء {a}", "START-CELL-MIGRATION": "بدء ترحيل {a} إلى خلية أخرى",
    "START-DECOMMISSION": "بدء إخراج {a} من الخدمة", "START-EVALUATION": "بدء تقييم {a}", "START-MAINTENANCE": "بدء صيانة {a}",
    "START-REVIEW": "بدء مراجعة {a}", "SUBMIT": "تقديم {a}", "SUBSCRIBE": "إنشاء {a}", "SUSPEND": "تعليق {a}",
    "TEST": "اختبار {a}", "TRANSFER": "نقل {a}", "TRANSFER-CUSTODY": "نقل عهدة {a}", "UNLINK": "فك ربط {a}",
    "UNLINK-IDENTITY": "فك ربط هوية خارجية عن {a}", "UNLOCK": "فتح قفل {a}", "UNSUBSCRIBE": "إلغاء {a}",
    "UNSUSPEND": "رفع تعليق {a}", "UPDATE-CHANNELS": "تحديث قنوات {a}", "UPDATE-CONDITION": "تحديث حالة {a} الفنية",
    "UPDATE-DETAILS": "تحديث بيانات {a}", "UPDATE-HYPOTHESIS": "تحديث فرضية في {a}", "UPDATE-LOCATOR": "تحديث محدِّد موقع {a}",
    "UPDATE-MAPPING": "تحديث ربط حقول {a}", "UPDATE-PROFILE": "تحديث ملف {a}", "UPDATE-QUOTAS": "تحديث حصص {a}",
    "UPDATE-RESPONSIBILITY": "تحديث مسؤولية ضمن {a}", "UPLOAD-BATCH": "رفع دفعة إلى {a}", "VALIDATE": "التحقق من {a}",
    "WITHDRAW": "سحب {a}",
}

# Per-command phrases where the verb template would mislead or repeat the aggregate name.
COMMAND_PHRASES = {
    "CMD-LHD-REQUEST-RELEASE": "طلب رفع {a}", "CMD-LHD-APPROVE-RELEASE": "اعتماد رفع {a}",
    "CMD-LHD-CANCEL-RELEASE": "إلغاء طلب رفع {a}", "CMD-RSV-HOLD": "إنشاء {a} مبدئيًا",
    "CMD-ASG-RETURN": "إرجاع الأصل وإنهاء {a}", "CMD-SCF-DISCARD": "حسم {a} بإسقاط الأمر الميداني",
    "CMD-ASG-ASSIGN": "تسجيل {a}", "CMD-AUT-GRANT": "إصدار {a}", "CMD-DST-DISTRIBUTE": "تنفيذ {a}",
    "CMD-LGR-REQUEST": "تقديم {a}", "CMD-RAS-ASSIGN": "تسجيل {a}",
}

# Aggregates grouped by domain category (a second tag next to the lifecycle operation type).
CATEGORIES = {
    "تحليل": {"AGG-ANALYSIS-CASE", "AGG-ANALYSIS-METHOD", "AGG-ANALYSIS-RUN", "AGG-ASSESSMENT", "AGG-FINDING",
              "AGG-ER-CASE", "AGG-CONFLICT", "AGG-MATCH-RULESET", "AGG-CORRELATION-PROPOSAL", "AGG-CORRELATION-RULE",
              "AGG-AI-REQUEST", "AGG-AI-RESULT"},
    "تقارير ومنتجات": {"AGG-PRODUCT", "AGG-PRODUCT-TEMPLATE", "AGG-DISTRIBUTION", "AGG-RECONSTRUCTION",
                       "AGG-ARCHIVE-PACKAGE", "AGG-KNOWLEDGE-OBJECT"},
    "تكامل": {"AGG-ADAPTER", "AGG-IMPORT-BATCH", "AGG-EXTERNAL-ID", "AGG-INTEGRATION-CONNECTION", "AGG-SENSOR-STREAM",
              "AGG-SYNC-SESSION", "AGG-SYNC-CONFLICT", "AGG-PRELOAD-PACKAGE", "AGG-HR-SYNC-PROPOSAL", "AGG-CAP-MESSAGE",
              "AGG-DEVICE"},
    "حوكمة وأمن": {"AGG-CLASSIFICATION-SCHEME", "AGG-DISPOSITION-RUN", "AGG-ERASURE-REQUEST", "AGG-LEGAL-HOLD",
                   "AGG-POLICY-SET", "AGG-RETENTION-SCHEDULE", "AGG-SECURITY-EXCEPTION", "AGG-CLEARANCE", "AGG-ROLE",
                   "AGG-ROLE-ASSIGNMENT", "AGG-AUTHORITY-GRANT", "AGG-SERVICE-ACCOUNT", "AGG-AI-ROUTING", "AGG-AI-TOOL",
                   "AGG-MODEL-VERSION", "AGG-EVAL-SUITE"},
}

# Arabic names of the 15 business actors (01-business/stakeholders.md gives English names only).
ACTORS_AR = {
    "ACT-01": "القيادي التنفيذي", "ACT-02": "المدير", "ACT-03": "المخطِّط", "ACT-04": "المحلل", "ACT-05": "المشغِّل",
    "ACT-06": "المستخدم الميداني", "ACT-07": "مدير الموارد", "ACT-08": "مستخدم الإمداد", "ACT-09": "مدير المخاطر",
    "ACT-10": "مدير التدريب", "ACT-11": "مدير المعرفة", "ACT-12": "أمين الأرشيف", "ACT-13": "مسؤول الأمن",
    "ACT-14": "المدقِّق", "ACT-15": "مسؤول الإدارة",
}
