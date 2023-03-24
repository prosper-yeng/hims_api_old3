from rest_framework import serializers

from lab_test_ordered_site.models import LabTestOrderedSite
from person.serializers import UserSerializer
from site_type.serializers import SiteTypeSerializer

from lab_test_order_details.serializers import LabTestOrderDetailsSerializer


class LabTestOrderedSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabTestOrderedSite
        fields = [
            "id",
            "lab_test_order_details",
            "site_type",
            "is_deleted",
            "created_by",
        ]
        read_only_fields = ("id",)


class CombinedSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    site_type = SiteTypeSerializer(many=False)
    lab_test_order_details = LabTestOrderDetailsSerializer(many=False)

    class Meta:
        model = LabTestOrderedSite
        fields = "__all__"
