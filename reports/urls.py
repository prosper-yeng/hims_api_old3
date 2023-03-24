# Python/django imports
from django.urls import path

# Local apps imports
from .records_views import *
from .consulting_views import *
from .customer_views import *
from .login_devices_views import *
from .pharmarcy_views import *
from .laboratory_views import *

urlpatterns = [
    # Records Routes
    path(
        "api/reports/patient-list",
        PatientListViewSet.as_view(),
        name="patient_list_report",
    ),
    path(
        "api/reports/attendance-trend",
        AttendanceTrendViewSet.as_view(),
        name="attendance_trend_report",
    ),
    path(
        "api/reports/registration-fees",
        RegistrationFeesViewSet.as_view(),
        name="registration_fees_report",
    ),
    path(
        "api/reports/patient-with-sponsor",
        PatientsWithSponsorViewSet.as_view(),
        name="patient_with_sponsor_report",
    ),
    # Consulting Routes
    path(
        "api/reports/diagnosis-history",
        DiagnosisHistoryViewSet.as_view(),
        name="diagnosis_history_report",
    ),
    path(
        "api/reports/consultation-history",
        ConsultationHistoryViewSet.as_view(),
        name="consultation_history_report",
    ),
    path(
        "api/reports/patients-medical-history",
        PatientsMedicalHistoryViewSet.as_view(),
        name="patient_medical_history_report",
    ),
    # Customer Routes
    path(
        "api/reports/suppliers-report",
        SuppliersReportViewSet.as_view(),
        name="suppliers_report_report",
    ),
    path(
        "api/reports/buyers-report",
        BuyersReportViewSet.as_view(),
        name="buyers_report_report",
    ),
    path(
        "api/reports/client-report",
        ClientReportViewSet.as_view(),
        name="client_report_report",
    ),
    # Login Devices
    path(
        "api/reports/user-devices",
        LoggedInUserDevicesReportViewSet.as_view(),
        name="user_devices_report"
    ),
    # Pharmacy Routes
    path(
        "api/reports/prescription-report",
        PrescriptionReportViewSet.as_view(),
        name="prescription_report",
    ),
    path(
        "api/reports/warehouse-stock",
        StockViewSet.as_view(),
        name="warehouse_stock",
    ),
    # Laboratory Routes
    path(
        "api/reports/labs-performed-report",
        LabsPerformedReportViewSet.as_view(),
        name="labs_performed_report"
    ),
    path(
        "api/reports/lab-results-of-patient-report",
        LabResultsOfPatientReportViewSet.as_view(),
        name="lab_results_of_patient_report"
    ),
    path(
        "api/reports/stock-reorder-level-reports",
        StockReorderLevelReportViewSet.as_view(),
        name = "stock_reorder_level_reports"
    ),
    path(
        "api/reports/lab-test-report",
        LabTestReportView.as_view(),
        name="lab_results_report"
    )
]
