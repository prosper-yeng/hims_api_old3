from rest_framework import serializers

from .models import Buyer


class BuyerSerializer(serializers.ModelSerializer):
    country_name = serializers.CharField(source="nation.name", required=False)
    region_name = serializers.CharField(source="region.name_of_region", required=False)
    district_name = serializers.CharField(
        source="district.name_of_district", required=False
    )
    town_name = serializers.CharField(source="town.name", required=False)

    class Meta:
        model = Buyer
        fields = [
            "id",
            "name",
            "email",
            "primary_phone",
            "secondary_phone",
            "country",
            "country_name",
            "region",
            "region_name",
            "district",
            "district_name",
            "town",
            "town_name",
            "street",
            "post_code",
            "created_by",
        ]
        read_only_fields = ("id",)
