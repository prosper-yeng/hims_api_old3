"""
hims_api URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView,
)
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path("", include_docs_urls(title="HMS API")),
    path("", include(("facility.urls", "facility"), namespace="facility")),
    path("", include(("select_item.urls", "select_item"), namespace="select_item")),
    path("", include(("groups.urls", "groups"), namespace="group")),
    path("", include(("permission.urls", "permission"), namespace="permission")),
    path("", include(("language.urls", "language"), namespace="language")),
    path("", include(("person.urls", "person"), namespace="person")),
    path(
        "",
        include(
            ("group_permission.urls", "group_permission"), namespace="group_permission"
        ),
    ),
    path("", include(("address.urls", "address"), namespace="address")),
    path(
        "",
        include(
            ("daily_attendance.urls", "daily_attendance"), namespace="daily_attendance"
        ),
    ),
    # path ( '', include ( ('group_service.urls', 'group_service'), namespace='group_service') ),
    path("", include(("service_type.urls", "service_type"), namespace="service_type")),
    path(
        "",
        include(("patient_doctor.urls", "patient_doctor"), namespace="patient_doctor"),
    ),
    path(
        "",
        include(
            ("transaction_type.urls", "transaction_type"), namespace="transaction_type"
        ),
    ),
    path(
        "", include(("currency_type.urls", "currency_type"), namespace="currency_type")
    ),
    path(
        "",
        include(("service_charge.urls", "service_charge"), namespace="service_charge"),
    ),
    path("", include(("service.urls", "service"), namespace="service")),
    # path ( '', include ( ('work_flow.urls', 'work_flow'), namespace='work_flow' ) ),
    # path ( '', include ( ('transaction.urls', 'transaction'), namespace='transaction' ) ),
    path("", include(("service_bill.urls", "service_bill"), namespace="service_bill")),
    # path ( '', include ( ('transaction_log.urls', 'transaction_log'), namespace='transaction_log' ) ),
    path("", include(("vital_sign.urls", "vital_sign"), namespace="vital_sign")),
    path("", include(("nation.urls", "nation"), namespace="nation")),
    path("", include(("region.urls", "region"), namespace="region")),
    path("", include(("district.urls", "district"), namespace="district")),
    path("", include(("town.urls", "town"), namespace="town")),
    path(
        "", include(("opd_bill_type.urls", "opd_bill_type"), namespace="opd_bill_type")
    ),
    path(
        "",
        include(
            ("opd_bill_patient.urls", "opd_bill_patient"), namespace="opd_bill_patient"
        ),
    ),
    path("", include(("lab_priority.urls", "lab_priority"), namespace="lab_priority")),
    path("", include(("sample_type.urls", "sample_type"), namespace="sample_type")),
    path(
        "", include(("lab_test_type.urls", "lab_test_type"), namespace="lab_test_type")
    ),
    path("", include(("lab_test.urls", "lab_test"), namespace="lab_test")),
    # path ( '', include ( ('lab_test_order_cart.urls', 'lab_test_order_cart'), namespace='lab_test_order_cart' ) ),
    #     path ( '', include ( ('lab_test_order.urls', 'lab_test_order'), namespace='lab_test_order' ) ),
    path(
        "",
        include(
            ("lab_test_order_details.urls", "lab_test_order_details"),
            namespace="lab_test_order_details",
        ),
    ),
    path("", include(("site_type.urls", "site_type"), namespace="site_type")),
    # path ( '', include ( ('medication_type.urls', 'medication_type'), namespace='medication_type' ) ),
    path("", include(("medication.urls", "medication"), namespace="medication")),
    path(
        "",
        include(
            ("medication_bill.urls", "medication_bill"), namespace="medication_bill"
        ),
    ),
    path(
        "", include(("lab_test_site.urls", "lab_test_site"), namespace="lab_test_site")
    ),
    path(
        "",
        include(
            ("medication_bill_detail.urls", "medication_bill_detail"),
            namespace="medication_bill_detail",
        ),
    ),
    path(
        "",
        include(("insurance_type.urls", "insurance_type"), namespace="insurance_type"),
    ),
    path("", include(("prescription.urls", "prescription"), namespace="prescription")),
    path(
        "",
        include(
            ("unit_of_measurement.urls", "unit_of_measurement"),
            namespace="unit_of_measurement",
        ),
    ),
    path(
        "",
        include(
            ("medication_unit_of_measurement.urls", "medication_unit_of_measurement"),
            namespace="medication_unit_of_measurement",
        ),
    ),
    path(
        "",
        include(
            ("medication_quantity.urls", "medication_quantity"),
            namespace="medication_quantity",
        ),
    ),
    path(
        "",
        include(
            ("medication_price.urls", "medication_price"), namespace="medication_price"
        ),
    ),
    path("", include(("dosage_type.urls", "dosage_type"), namespace="dosage_type")),
    path(
        "",
        include(
            ("medication_dosage.urls", "medication_dosage"),
            namespace="medication_dosage",
        ),
    ),
    # path ( '', include ( ('client_type.urls', 'client_type'), namespace='client_type' ) ),
    path(
        "",
        include(
            ("quantity_unit_type.urls", "quantity_unit_type"),
            namespace="quantity_unit_type",
        ),
    ),
    path("", include(("supplier.urls", "supplier"), namespace="supplier")),
    # path ( '', include ( ('client.urls', 'client'), namespace='client' ) ),
    path(
        "",
        include(
            ("medication_quantity_unit.urls", "medication_quantity_unit"),
            namespace="medication_quantity_unit",
        ),
    ),
    path("", include(("buyer.urls", "buyer"), namespace="buyer")),
    path(
        "",
        include(
            ("medication_order.urls", "medication_order"), namespace="medication_order"
        ),
    ),
    path(
        "",
        include(
            ("prescription_dosage.urls", "prescription_dosage"),
            namespace="prescription_dosage",
        ),
    ),
    path(
        "",
        include(("recipient_type.urls", "recipient_type"), namespace="recipient_type"),
    ),
    path(
        "",
        include(
            ("recommended_dosage.urls", "recommended_dosage"),
            namespace="recommended_dosage",
        ),
    ),
    path("", include(("warehouse.urls", "warehouse"), namespace="warehouse")),
    path("", include(("store.urls", "store"), namespace="store")),
    path(
        "",
        include(
            ("product_category.urls", "product_category"), namespace="product_category"
        ),
    ),
    path("", include(("product_type.urls", "product_type"), namespace="product_type")),
    path(
        "",
        include(
            ("warehouse_product.urls", "warehouse_product"),
            namespace="warehouse_product",
        ),
    ),
    path(
        "",
        include(
            ("warehouse_stock.urls", "warehouse_stock"), namespace="warehouse_stock"
        ),
    ),
    path(
        "",
        include(
            ("product_stock_unit.urls", "product_stock_unit"),
            namespace="product_stock_unit",
        ),
    ),
    path("", include(("order_batch.urls", "order_batch"), namespace="order_batch")),
    path(
        "",
        include(
            ("department_stock_order.urls", "department_stock_order"),
            namespace="department_stock_order",
        ),
    ),
    path(
        "", include(("product_price.urls", "product_price"), namespace="product_price")
    ),
    path(
        "",
        include(
            ("department_product_stock_unit.urls", "department_product_stock_unit"),
            namespace="department_product_stock_unit",
        ),
    ),
    path(
        "",
        include(
            ("lab_test_results_category.urls", "lab_test_results_category"),
            namespace="lab_test_results_category",
        ),
    ),
    path(
        "",
        include(
            ("lab_test_results_parameters.urls", "lab_test_results_parameters"),
            namespace="lab_test_results_parameters",
        ),
    ),
    path(
        "",
        include(
            ("lab_test_results_type.urls", "lab_test_results_type"),
            namespace="lab_test_results_type",
        ),
    ),
    path(
        "",
        include(
            ("lab_results_method.urls", "lab_results_method"),
            namespace="lab_results_method",
        ),
    ),
    path(
        "",
        include(
            ("lab_test_results.urls", "lab_test_results"), namespace="lab_test_results"
        ),
    ),
    path(
        "",
        include(
            ("test_consumable.urls", "test_consumable"), namespace="test_consumable"
        ),
    ),
    path(
        "",
        include(
            ("lab_test_results_upload.urls", "lab_test_results_upload"),
            namespace="lab_test_results_upload",
        ),
    ),
    path(
        "",
        include(("lab_test_price.urls", "lab_test_price"), namespace="lab_test_price"),
    ),
    path(
        "", include(("lab_test_bill.urls", "lab_test_bill"), namespace="lab_test_bill")
    ),
    path(
        "",
        include(
            ("mode_of_payment.urls", "mode_of_payment"), namespace="mode_of_payment"
        ),
    ),
    path("", include(("company.urls", "company"), namespace="company")),
    # path ( '', include ( ('payment.urls', 'payment'), namespace='payment' ) ),
    path(
        "",
        include(
            ("payment_individual.urls", "payment_individual"),
            namespace="payment_individual",
        ),
    ),
    path(
        "",
        include(("payment_detail.urls", "payment_detail"), namespace="payment_detail"),
    ),
    path(
        "",
        include(
            ("lab_test_ordered_sample.urls", "lab_test_ordered_sample"),
            namespace="lab_test_ordered_sample",
        ),
    ),
    path(
        "",
        include(
            ("lab_test_ordered_site.urls", "lab_test_ordered_site"),
            namespace="lab_test_ordered_site",
        ),
    ),
    path("", include(("department.urls", "department"), namespace="department")),
    path("", include(("religion.urls", "religion"), namespace="religion")),
    path("", include(("person_title.urls", "person_title"), namespace="person_title")),
    path("", include(("occupation.urls", "occupation"), namespace="occupation")),
    path(
        "",
        include(("marital_status.urls", "marital_status"), namespace="marital_status"),
    ),
    path("", include(("status.urls", "status"), namespace="status")),
    path("", include(("allergies.urls", "allergies"), namespace="allergies")),
    path(
        "", include(("relative_type.urls", "relative_type"), namespace="relative_type")
    ),
    path("", include(("relative.urls", "relative"), namespace="relative")),
    path(
        "",
        include(
            ("consulting_room.urls", "consulting_room"), namespace="consulting_room"
        ),
    ),
    path("", include(("sponsor_type.urls", "sponsor_type"), namespace="sponsor_type")),
    path("", include(("sponsor.urls", "sponsor"), namespace="sponsor")),
    path(
        "",
        include(
            ("sponsor_patient.urls", "sponsor_patient"), namespace="sponsor_patient"
        ),
    ),
    path("", include(("clinic_type.urls", "clinic_type"), namespace="clinic_type")),
    path(
        "",
        include(
            ("attendance_type.urls", "attendance_type"), namespace="attendance_type"
        ),
    ),
    # path ( '', include ( ('sponsor_service_price.urls', 'sponsor_service_price'), namespace='sponsor_service_price' ) ),
    path("", include(("select_unit.urls", "select_unit"), namespace="select_unit")),
    path("", include(("diagnosis.urls", "diagnosis"), namespace="diagnosis")),
    path("", include(("consultation.urls", "consultation"), namespace="consultation")),
    path("", include(("product.urls", "product"), namespace="product")),
    path(
        "",
        include(
            ("consultation_diagnosis.urls", "consultation_diagnosis"),
            namespace="consultation_diagnosis",
        ),
    ),
    path("", include(("procedure.urls", "procedure"), namespace="procedure")),
    path(
        "",
        include(
            ("diagnosed_procedure.urls", "diagnosed_procedure"),
            namespace="diagnosed_procedure",
        ),
    ),
    path(
        "",
        include(
            ("facility_category.urls", "facility_category"),
            namespace="facility_category",
        ),
    ),
    path("", include(("progress_bar.urls", "progress_bar"), namespace="progress_bar")),
    path(
        "",
        include(
            ("service_charge_sponsor.urls", "service_charge_sponsor"),
            namespace="service_charge_sponsor",
        ),
    ),
    path(
        "",
        include(
            ("patient_service_charge.urls", "patient_service_charge"),
            namespace="patient_service_charge",
        ),
    ),
    path(
        "",
        include(
            ("payment_by_sponsor.urls", "payment_by_sponsor"),
            namespace="payment_by_sponsor",
        ),
    ),
    path(
        "",
        include(
            ("payment_detail_Individual.urls", "payment_detail_Individual"),
            namespace="payment_detail_Individual",
        ),
    ),
    path(
        "",
        include(
            ("payment_detail_by_sponsor.urls", "payment_detail_by_sponsor"),
            namespace="payment_detail_by_sponsor",
        ),
    ),
    path(
        "",
        include(
            ("procedure_charge.urls", "procedure_charge"), namespace="procedure_charge"
        ),
    ),
    path(
        "",
        include(
            ("procedure_charge_by_sponsor.urls", "procedure_charge_by_sponsor"),
            namespace="procedure_charge_by_sponsor",
        ),
    ),
    path(
        "",
        include(
            ("procedure_schedule.urls", "procedure_schedule"),
            namespace="procedure_schedule",
        ),
    ),
    path(
        "",
        include(
            ("product_price_sponsor.urls", "product_price_sponsor"),
            namespace="product_price_sponsor",
        ),
    ),
    path(
        "",
        include(
            ("lab_test_price_sponsor.urls", "lab_test_price_sponsor"),
            namespace="lab_test_price_sponsor",
        ),
    ),
    path(
        "",
        include(
            ("patient_type.urls", "patient_type"),
            namespace="patient_type",
        ),
    ),
    # REPORTS
    path(
        "",
        include(
            ("reports.urls", "reports"),
            namespace="reports",
        ),
    ),
    # ADMISSION Related Routes Below
    path(
        "",
        include(
            ("doctors_note.urls", "doctors_note"),
            namespace="doctors_note",
        ),
    ),
    path(
        "",
        include(
            ("patient_discharge.urls", "patient_discharge"),
            namespace="patient_discharge",
        ),
    ),
    path(
        "",
        include(
            ("patient_review.urls", "patient_review"),
            namespace="patient_review",
        ),
    ),
    path(
        "",
        include(
            ("procedure_care.urls", "procedure_care"),
            namespace="procedure_care",
        ),
    ),
    path(
        "",
        include(
            ("treatment_plan.urls", "treatment_plan"),
            namespace="treatment_plan",
        ),
    ),
    path(
        "",
        include(
            ("medication_administration.urls", "medication_administration"),
            namespace="medication_administration",
        ),
    ),
    path(
        "",
        include(
            ("nurses_note.urls", "nurses_note"),
            namespace="nurses_note",
        ),
    ),
    path(
        "",
        include(
            ("bed.urls", "bed"),
            namespace="bed",
        ),
    ),
    path(
        "",
        include(
            ("bed_allocation.urls", "bed_allocation"),
            namespace="bed_allocation",
        ),
    ),
    path(
        "",
        include(
            ("room.urls", "room"),
            namespace="room",
        ),
    ),
    path(
        "",
        include(
            ("inter_hospital_patient_transfer.urls", "inter_hospital_patient_transfer"),
            namespace="inter_hospital_patient_transfer",
        ),
    ),
    path(
        "",
        include(
            ("intra_hospital_patient_transfer.urls", "intra_hospital_patient_transfer"),
            namespace="intra_hospital_patient_transfer",
        ),
    ),
    path(
        "",
        include(
            ("ward.urls", "ward"),
            namespace="ward",
        ),
    ),
    path(
        "",
        include(
            ("ward_type.urls", "ward_type"),
            namespace="ward_type",
        ),
    ),
    path(
        "",
        include(
            ("vital_signs_monitoring.urls", "vital_signs_monitoring"),
            namespace="vital_signs_monitoring",
        ),
    ),
    path(
        "",
        include(
            ("admission.urls", "admission"),
            namespace="admission",
        ),
    ),
    # RADIOLOGY Related Routes Below
    path(
        "",
        include(
            ("radiology_category.urls", "radiology_category"),
            namespace="radiology_category",
        ),
    ),
    path(
        "",
        include(
            ("radiology_type.urls", "radiology_type"),
            namespace="radiology_type",
        ),
    ),
    path(
        "",
        include(
            ("radiology_procedure.urls", "radiology_procedure"),
            namespace="radiology_procedure",
        ),
    ),
    path(
        "",
        include(
            ("radiology_procedure_price.urls", "radiology_procedure_price"),
            namespace="radiology_procedure_price",
        ),
    ),
    path(
        "",
        include(
            (
                "radiology_procedure_price_sponsor.urls",
                "radiology_procedure_price_sponsor",
            ),
            namespace="radiology_procedure_price_sponsor",
        ),
    ),
    path(
        "",
        include(
            ("radiology_procedure_request.urls", "radiology_procedure_request"),
            namespace="radiology_procedure_request",
        ),
    ),
    path(
        "",
        include(
            ("radiology_procedure_result.urls", "radiology_procedure_result"),
            namespace="radiology_procedure_result",
        ),
    ),
    path(
        "",
        include(
            ("radiology_material_used.urls", "radiology_material_used"),
            namespace="radiology_material_used",
        ),
    ),
    # EXTRA NURSES RELATED MODELS
    path(
        "",
        include(
            ("need_type.urls", "need_type"),
            namespace="need_type",
        ),
    ),
    path(
        "",
        include(
            ("patient_needs.urls", "patient_needs"),
            namespace="patient_needs",
        ),
    ),
    path(
        "",
        include(
            ("subjective_info.urls", "subjective_info"),
            namespace="subjective_info",
        ),
    ),
    path(
        "",
        include(
            ("physical_examination.urls", "physical_examination"),
            namespace="physical_examination",
        ),
    ),
    path(
        "",
        include(
            ("additional_data.urls", "additional_data"),
            namespace="additional_data",
        ),
    ),
    path(
        "",
        include(
            ("habit.urls", "habit"),
            namespace="habit",
        ),
    ),
    path(
        "",
        include(
            ("family_history.urls", "family_history"),
            namespace="family_history",
        ),
    ),
    path(
        "",
        include(
            ("social_history.urls", "social_history"),
            namespace="social_history",
        ),
    ),
    path(
        "",
        include(
            ("psychosocial_history.urls", "psychosocial_history"),
            namespace="psychosocial_history",
        ),
    ),
    path(
        "",
        include(
            ("immunizations.urls", "immunizations"),
            namespace="immunizations",
        ),
    ),
    path(
        "",
        include(
            ("obstetric_history.urls", "obstetric_history"),
            namespace="obstetric_history",
        ),
    ),
    path(
        "",
        include(
            ("patient_diagnosis.urls", "patient_diagnosis"),
            namespace="patient_diagnosis",
        ),
    ),
    path(
        "",
        include(
            ("patient_specific_goal.urls", "patient_specific_goal"),
            namespace="patient_specific_goal",
        ),
    ),
    path(
        "",
        include(
            ("intervention_type.urls", "intervention_type"),
            namespace="intervention_type",
        ),
    ),
    path(
        "",
        include(
            ("intervention_implementation.urls", "intervention_implementation"),
            namespace="intervention_implementation",
        ),
    ),
    path(
        "",
        include(
            ("evaluation.urls", "evaluation"),
            namespace="evaluation",
        ),
    ),

    # token routes below
    path("admin/", admin.site.urls),
    path("api/token/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/logout/", TokenBlacklistView.as_view(), name="token_logout"),
    path(
        "schema",
        get_schema_view(
            title="HIMS API",
            description="API for facility, persons, addresses, and workflow",
            version="1.0",
        ),
        name="openapi-schema",
    ),
]
