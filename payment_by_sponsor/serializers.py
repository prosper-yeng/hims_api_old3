from rest_framework import serializers

from company.serializers import CompanySerializer
from daily_attendance.serializers import DailyAttendanceSerializer
from patient_service_charge.serializers import CombinedPatientServiceChargeSerializer
from person.serializers import UserSerializer, PatientSerializer
from sponsor.serializers import SponsorSerializer
from .models import PaymentBySponsor


class PaymentBySponsorSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source="company.name", required=False)

    class Meta:
        model = PaymentBySponsor
        fields = [
            "id",
            'patient_service_charge',
            "invoice_id",
            "mop",
            "company",
            "company_name",
            "sponsor",
            "amount_paid",
            "payment_date",
            "is_deleted",
            "status",
            "created_by",
        ]
        read_only_fields = ("id",)


class CombinedPaymentSponsorSerializer(serializers.ModelSerializer):
    patient_service_charge = CombinedPatientServiceChargeSerializer(many=False)

    class Meta:
        model = PaymentBySponsor
        fields = "__all__"
