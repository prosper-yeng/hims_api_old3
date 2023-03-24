from rest_framework import serializers

from daily_attendance.serializers import DailyAttendanceSerializer
from patient_service_charge.serializers import CombinedPatientServiceChargeSerializer
from person.serializers import UserSerializer, PatientSerializer
from .models import PaymentIndividual
from company.serializers import CompanySerializer


class PaymentIndividualSerializer(serializers.ModelSerializer):
    # company_name = serializers.CharField ( source='company.name', required=False )

    class Meta:
        model = PaymentIndividual
        fields = [
            "id",
            "patient_service_charge",
           #"attendance",
            "mop",
            "company",
            #'company_name',
            "sponsor",
            "amount_paid",
            "payment_date",
            "is_deleted",
            "status",
            "created_by",
        ]
        read_only_fields = ("id",)


class CombinedPaymentPatientSerializer(serializers.ModelSerializer):
    patient_service_charge = CombinedPatientServiceChargeSerializer(many=False)

    class Meta:
        model = PaymentIndividual
        fields = "__all__"
