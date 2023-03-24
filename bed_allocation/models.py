# Django/DRF imports
from django.db import models

# Local app imports
from hims_api.basemodel import BaseModel
from admission.models import Admission
from bed.models import Bed


class BedAllocation(BaseModel):
    admission = models.ForeignKey(
        Admission, on_delete=models.PROTECT, related_name="admission_bedallocation"
    )
    bed = models.ForeignKey(
        Bed, on_delete=models.PROTECT, related_name="bed_bedallocation"
    )
    allocated_date = models.DateField(auto_now=True)
    deallocated_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.bed.number}"

    class Meta:
        ordering = ["-id"]
