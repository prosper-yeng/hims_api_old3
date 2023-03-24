from rest_framework import serializers

from consultation.models import Consultation
from consultation_diagnosis.models import ConsultationDiagnosis
from daily_attendance.serializers import CombinedPatientAttendanceSerializer
from diagnosis.serializers import DiagnosisSerializer
from product_price.models import ProductPrice
from sponsor.serializers import SponsorSerializer
from vital_sign.serializers import CombinedPatientVitalSignSerializer
from warehouse_product.serializers import WarehouseProductSerializer
from .models import Prescription


class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = [
            "id",
            "warehouse_product",
            "price",
            "sponsor",
            "consultation_diagnosis",
            "quantity",
            "duration",
            "duration_unit",
            "prescription_date",
            "status",
            "created_by",
        ]
        read_only_fields = ("id",)


"""
class PatientSerializer (serializers.ModelSerializer):
    user = UserSerializer(many=False)

    title_name = serializers.CharField(source='person_title.name', required=False)
    occupation_name = serializers.CharField(source='occupation.name', required=False)
    marital_status_name = serializers.CharField(source='marital_status.name', required=False)
    religion_name = serializers.CharField(source='religion.name', required=False)

    facility_name = serializers.CharField(source='user.facility', required=False)
    email = serializers.CharField(source='user.email', required=False)

    class Meta:
        model = Patient
        fields = ('id',
                  'title',
                  'marital_status',
                  'occupation',
                  'religion',

                  'full_name',
                  'title_name',
                  'occupation_name',
                  'marital_status_name',
                  'religion_name',

                  'facility_name',
                  'email',

                  'user',
                  )

        read_only_fields = ('id',)

"""


class CombinedProductPriceSerializer(serializers.ModelSerializer):
    product = WarehouseProductSerializer(many=False)
    sponsor = SponsorSerializer(many=False)

    class Meta:
        model = ProductPrice
        fields = [
            "id",
            "product",
            "product_name",
            "sponsor",
            "sponsor_name",
            "profit_margin",
            "vat",
            "other_tax",
            "price",
            "cost_price",
            "discount",
            "is_deleted",
            "status",
            "created_by",
        ]
        read_only_fields = ("id",)


class ConsultationSerializer(serializers.ModelSerializer):
    # attendance = CombinedPatientAttendanceSerializer ( many=False )

    class Meta:
        model = Consultation
        fields = (
            "id",
            # 'patient',
            "vital_sign",
            #'attendance',
            "chief_complain",
            "objective",
            "note",
            "created_by",
            "created_on",
            "status",
        )


class ConsultationDiagnosisSerializer(serializers.ModelSerializer):
    consultation = ConsultationSerializer(many=False)
    diagnosis = DiagnosisSerializer(many=False)
    vital_sign = CombinedPatientVitalSignSerializer(many=False)

    class Meta:
        model = ConsultationDiagnosis
        fields = (
            "id",
            "consultation",
            "vital_sign",
            "diagnosis",
            "note",
            "is_confirmed",
            "created_by",
            "created_on",
            "status",
        )


class CombinedDiagnosisPrescriptionSerializer(serializers.ModelSerializer):
    consultation_diagnosis = ConsultationDiagnosisSerializer(many=False)
    # warehouse_product = ProductPriceSerializer ( many=False )

    class Meta:
        model = Prescription
        fields = "__all__"
