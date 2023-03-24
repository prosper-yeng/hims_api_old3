from rest_framework import serializers

from lab_results_method.serializers import LabResultsMethodSerializer
from lab_test_order_details.serializers import LabTestOrderDetailsSerializer
from lab_test_results_category.serializers import LabTestResultsCategorySerializer
from lab_test_results_parameters.serializers import LabTestResultsParametersSerializer
from lab_test_results_type.serializers import LabTestResultsTypeSerializer
from .models import LabTestResults


class LabTestResultsSerializer(serializers.ModelSerializer):
    # result_category_name = serializers.CharField ( source='lab_test_results_category.name', required=False )
    # result_type_name = serializers.CharField ( source='results_type.name', required=False )
    # parameter_name = serializers.CharField ( source='lab_test_results_parameters.name', required=False )
    # method_name = serializers.CharField ( source='lab_results_method.name', required=False )

    class Meta:
        model = LabTestResults
        fields = [
            "id",
            "lab_test_order_details",
            "results_category",
            #'result_category_name',
            "results_parameter",
            #'parameter_name',
            "method",
            #'method_name',
            "result_type",
            #'result_type_name',
            "unit",
            "reference_range",
            "status",
            "is_deleted",
            "created_by",
        ]
        read_only_fields = ("id",)


class CombinedLabTestOderResultsSerializer(serializers.ModelSerializer):
    lab_test_order_details = LabTestOrderDetailsSerializer(many=False)
    results_category = LabTestResultsCategorySerializer(many=False)
    results_parameter = LabTestResultsParametersSerializer(many=False)
    method = LabResultsMethodSerializer(many=False)
    result_type = LabTestResultsTypeSerializer(many=False)

    class Meta:
        model = LabTestResults
        fields = "__all__"
