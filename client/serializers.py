from rest_framework import serializers

from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    client_type_name = serializers.CharField(source="client_type.name", required=False)
    country_name = serializers.CharField(source="nation.name", required=False)
    region_name = serializers.CharField(source="region.name_of_region", required=False)
    district_name = serializers.CharField(
        source="district.name_of_district", required=False
    )
    town_name = serializers.CharField(source="town.name", required=False)

    class Meta:
        model = Client
        fields = [
            "id",
            "name",
            "client_type",
            "client_type_name",
            "contact_person",
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
            "discount_allowed",
            "created_by",
        ]
        read_only_fields = ("id",)
