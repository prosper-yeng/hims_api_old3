from rest_framework import serializers

from .models import OpdBillPatient


class OpdBillPatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpdBillPatient
        fields = [
            "id",
            "patient",
            "name",
            "adult_price",
            "child_price",
            "created_by",
            "adult_discount",
            "child_discount",
        ]

        read_only_fields = ("id",)
