from django.db import models
from choice.views import StatusChoice
from django.contrib.auth.models import User

from lab_test.models import LabTest
from site_type.models import SiteType


class LabTestSite(models.Model):
    lab_test = models.ForeignKey(LabTest, on_delete=models.CASCADE)
    site_type = models.ForeignKey(SiteType, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    status = models.ForeignKey ("status.Status", on_delete=models.CASCADE, related_name="labTestSite_status")
    def __str__(self):
        return "{}".format(self.lab_test)
