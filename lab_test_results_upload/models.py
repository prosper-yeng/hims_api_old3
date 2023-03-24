from django.core.validators import FileExtensionValidator
from django.db import models
from choice.views import StatusChoice
from django.contrib.auth.models import User

from common.views import allowed_extension
from lab_results_method.models import LabResultsMethod
from lab_test_order_details.models import LabTestOrderDetails
from lab_test_results_category.models import LabTestResultsCategory
from lab_test_results_parameters.models import LabTestResultsParameters
from lab_test_results_type.models import LabTestResultsType
from lab_test_type.models import LabTestType
from validator.views import validate_file_size


class LabTestResultsUpload(models.Model):
    lab_test_order_details = models.ForeignKey(
        LabTestOrderDetails,
        on_delete=models.CASCADE,
        related_name="lab_test_results_upload",
    )
    lab_test_results = models.FileField(
        validators=[
            validate_file_size,
            FileExtensionValidator(allowed_extensions=allowed_extension),
        ],
        upload_to="lab_test_results_files",
        verbose_name="results upload",
        null=True,
        blank=True,
    )

    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="lab_test_result_upload_creator"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=100, choices=StatusChoice.choices, default=StatusChoice.ACTIVE
    )

    def __str__(self):
        return "{}".format(self.name)
