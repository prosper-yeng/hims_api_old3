from rest_framework import serializers
from .models import BedAllocation
from bed.serializers import BedSerializer
from admission.serializers import AdmissionDetailedSerializer


class BedAllocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BedAllocation
        fields = "__all__"
        read_only_fields = ["id", "is_active", "deallocated_date"]


class BedAllocationDetailsSerializer(serializers.ModelSerializer):
    admission = AdmissionDetailedSerializer()
    bed = BedSerializer()

    class Meta:
        model = BedAllocation
        fields = "__all__"
        read_only_fields = ["id", "is_active", "deallocated_date"]
