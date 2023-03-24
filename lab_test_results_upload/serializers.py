from rest_framework import serializers

from .models import LabTestResultsUpload


class LabTestResultsUploadSerializer(serializers.ModelSerializer):
    # result_category_name = serializers.CharField ( source='lab_test_results_category.name', required=False )

    class Meta:
        model = LabTestResultsUpload
        fields = ["id", "lab_test_order_details", "lab_test_results", "created_by"]
        read_only_fields = ("id",)
