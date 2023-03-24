from rest_framework import serializers

from .models import Sponsor


class SponsorSerializer(serializers.ModelSerializer):
    sponsor_type_name = serializers.CharField(
        source="sponsor_type.name", required=False
    )
    town_name = serializers.CharField(source="town.name", required=False)

    class Meta:
        model = Sponsor
        fields = [
            "id",
            "name",
            "sponsor_type",
            "sponsor_type_name",
            "contact_person",
            "email",
            "primary_phone",
            "secondary_phone",
            "town",
            "town_name",
            "street",
            "post_code",
            "created_on",
            "status",
            "created_by",
        ]

        read_only_fields = ("id",)
