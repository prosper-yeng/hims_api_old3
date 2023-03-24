from rest_framework import serializers

from .models import PersonTitle


class PersonTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonTitle
        fields = ["id", "name", "status"]
