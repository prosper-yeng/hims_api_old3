from django.db import models
from choice.views import StatusChoice, UrgencyTypeChoice, FastingTypeChoice
from django.contrib.auth.models import User

from lab_test_order_details.models import LabTestOrderDetails
from site_type.models import SiteType

# from transaction.models import Transaction


class LabTestOrderedSite(models.Model):
    lab_test_order_details = models.ForeignKey(
        LabTestOrderDetails,
        on_delete=models.CASCADE,
        related_name="in_lab_test_ordered_site",
    )
    site_type = models.ForeignKey(
        SiteType, on_delete=models.CASCADE, related_name="site_type_order_test"
    )
    is_deleted = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="lab_test_ordered_site_user"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=100, choices=StatusChoice.choices, default=StatusChoice.ACTIVE
    )

    def __str__(self):
        return "{}".format(self.site_type)
