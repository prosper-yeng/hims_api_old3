from django.db import models
from choice.views import StatusChoice, UrgencyTypeChoice, FastingTypeChoice
from django.contrib.auth.models import User

from lab_test.models import LabTest
from lab_test_type.models import LabTestType
from sample_type.models import SampleType
from site_type.models import SiteType


class LabTestOrderCart(models.Model):
    patient = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="lab_order_cart_patient"
    )
    status = models.CharField(
        max_length=100, choices=StatusChoice.choices, default=StatusChoice.ACTIVE
    )
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="lab_test_order_cart_user"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.patient)
