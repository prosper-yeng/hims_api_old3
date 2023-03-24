from rest_framework import serializers
from .models import ProcedureCare


class ProcedureCareSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcedureCare
        exclude = ["created_at", "updated_at"]
        read_only_fields = ["id"]
