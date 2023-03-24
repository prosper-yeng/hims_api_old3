from rest_framework import serializers, fields
import datetime

from facility_category.serializers import FacilityCategorySerializer
from town.serializers import TownSerializer
from .models import Facility


class FacilitySerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(
        source="facility_category.name", required=False
    )
    # country_name = serializers.CharField(source='country.text', required=False)
    # region_name = serializers.CharField(source='region.text', required=False)
    # district_name = serializers.CharField(source='district.text', required=False)
    town_name = serializers.CharField(source="town.name", required=False)

    class Meta:
        model = Facility
        fields = [
            "id",
            "category",
            "name",
            "email",
            "website",
            "contact_name",
            "registration_no",
            "logo",
            "primary_phone",
            "secondary_phone",
            "town",
            "street",
            "postcode",
            "digital_address",
            "created_by",
            "status",
            "category_name",
            "default_facility",
            "town_name",
        ]


class CombinedUserFacilityTownSerializer(serializers.ModelSerializer):
    town = TownSerializer(many=False)
    category = FacilityCategorySerializer(many=False)

    class Meta:
        model = Facility
        fields = "__all__"
