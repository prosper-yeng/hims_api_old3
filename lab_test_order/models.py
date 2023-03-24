from django.db import models
from choice.views import StatusChoice, UrgencyTypeChoice, FastingTypeChoice
from django.contrib.auth.models import User

from lab_test.models import LabTest
from lab_test_order_cart.models import LabTestOrderCart
from lab_test_type.models import LabTestType
from sample_type.models import SampleType
from site_type.models import SiteType


class LabTestOrder(models.Model):
    lab_test_order_cart = models.ForeignKey(
        LabTestOrderCart,
        on_delete=models.CASCADE,
        related_name="lab_order_cart_to_patient",
    )
    lab_test = models.ForeignKey(
        LabTest,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="lab_test_orders",
    )
    urgency = models.CharField(
        max_length=100,
        choices=UrgencyTypeChoice.choices,
        default=UrgencyTypeChoice.NORMAL,
    )
    fasting_status = models.CharField(
        max_length=100,
        choices=FastingTypeChoice.choices,
        default=FastingTypeChoice.NONFASTING,
    )
    sample_types = models.ManyToManyField(SampleType, related_name="lab_sample_type")
    site_types = models.ManyToManyField(SiteType, related_name="lab_test_site")
    is_deleted = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="lab_test_ordered_ordered"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=100, choices=StatusChoice.choices, default=StatusChoice.ACTIVE
    )

    def __str__(self):
        return "{}".format(self.lab_test)
