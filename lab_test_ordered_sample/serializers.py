from rest_framework import serializers

from lab_test_ordered_sample.models import LabTestOrderedSample
from person.serializers import UserSerializer

from lab_test_order_details.serializers import LabTestOrderDetailsSerializer
from sample_type.serializers import SampleTypeSerializer


class LabTestOrderedSampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabTestOrderedSample
        fields = [
            "id",
            "lab_test_order_details",
            "sample_type",
            "is_deleted",
            "status",
            "created_by",
        ]
        read_only_fields = ("id",)


class CombinedSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    sample_type = SampleTypeSerializer(many=False)
    lab_test_order_details = LabTestOrderDetailsSerializer(many=False)

    class Meta:
        model = LabTestOrderedSample
        fields = "__all__"
