from rest_framework import serializers

from .models import MedicationPrice


class MedicationPriceSerializer(serializers.ModelSerializer):
    # medication = serializers.CharField ( source='medication.name', required=False )
    class Meta:
        model = MedicationPrice
        fields = ["id", "medication", "sponsor", "selling_unit_price", "created_by"]
        read_only_fields = ("id",)
