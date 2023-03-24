from rest_framework import serializers

from lab_test.serializers import LabTestSerializer
from site_type.serializers import SiteTypeSerializer
from .models import LabTestSite


class LabTestSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabTestSite
        fields = ["id", "lab_test", "site_type", "created_by"]

        read_only_fields = ("id",)


class CombinedLabTestSiteSerializer(serializers.ModelSerializer):
    lab_test = LabTestSerializer(many=False)
    site_type=SiteTypeSerializer(many=False)


    class Meta:
        model = LabTestSite
        fields = "__all__"