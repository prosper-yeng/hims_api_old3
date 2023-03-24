# Python/django imports
from rest_framework import serializers

from .models import PatientReview


class PatientReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientReview
        exclude = ["created_at", "updated_at"]
        read_only_fields = ["id"]
