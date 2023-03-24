from django.db import models
from choice.views import StatusChoice, UrgencyTypeChoice, FastingTypeChoice
from django.contrib.auth.models import User

from lab_test.models import LabTest
from lab_test_order_cart.models import LabTestOrderCart
from lab_test_order_details.models import LabTestOrderDetails
from sample_type.models import SampleType

# from transaction.models import Transaction


class LabTestOrderedSample(models.Model):
    lab_test_order_details = models.ForeignKey(
        LabTestOrderDetails,
        on_delete=models.CASCADE,
        related_name="in_lab_test_ordered",
    )
    sample_type = models.ForeignKey(
        SampleType, on_delete=models.CASCADE, related_name="sample_type_ordered"
    )
    is_deleted = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="lab_test_ordered_sample_user"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=100, choices=StatusChoice.choices, default=StatusChoice.ACTIVE
    )

    def __str__(self):
        return "{}".format(self.lab_test_order_details)
