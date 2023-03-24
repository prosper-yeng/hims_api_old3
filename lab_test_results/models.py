from django.db import models
from choice.views import StatusChoice
from django.contrib.auth.models import User

from lab_results_method.models import LabResultsMethod
from lab_test_order_details.models import LabTestOrderDetails
from lab_test_results_category.models import LabTestResultsCategory
from lab_test_results_parameters.models import LabTestResultsParameters
from lab_test_results_type.models import LabTestResultsType
from lab_test_type.models import LabTestType
from status.models import Status


class LabTestResults(models.Model):
    lab_test_order_details = models.ForeignKey(
        LabTestOrderDetails, on_delete=models.CASCADE, related_name="lab_test_results"
    )
    results_category = models.ForeignKey(
        LabTestResultsCategory,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="lab_test_category",
    )
    results_parameter = models.ForeignKey(
        LabTestResultsParameters,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="lab_test_parameter",
    )
    method = models.ForeignKey(
        LabResultsMethod,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="lab_test_method",
    )
    result_type = models.ForeignKey(
        LabTestResultsType,
        on_delete=models.CASCADE,
        related_name="lab_test_result_type",
    )
    unit = models.CharField(max_length=100, null=True, blank=True, unique=True)
    reference_range = models.CharField(
        max_length=100, null=True, blank=True, unique=True
    )

    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="lab_test_result_creator"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    status = models.ForeignKey(
        Status, on_delete=models.CASCADE, related_name="lab_test_result_status"
    )
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.lab_test_order_details)
