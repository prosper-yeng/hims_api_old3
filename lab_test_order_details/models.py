from django.db import models
from choice.views import StatusChoice, UrgencyTypeChoice, FastingTypeChoice
from django.contrib.auth.models import User

from consultation.models import Consultation
from daily_attendance.models import DailyAttendanceModel
from lab_test.models import LabTest
from lab_test_order_cart.models import LabTestOrderCart
from lab_test_type.models import LabTestType
from person.models import Patient
from sample_type.models import SampleType
from site_type.models import SiteType
from status.models import Status


class LabTestOrderDetails(models.Model):
    # attendance = models.ForeignKey(DailyAttendanceModel, on_delete=models.CASCADE, related_name='attendance_in_test_order' )
    consultation = models.ForeignKey(
        Consultation,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="consultation_in_test_order",
    )
    # patient = models.ForeignKey ( Patient, on_delete=models.CASCADE, related_name='test_order_for_patient' )
    lab_test = models.ForeignKey(
        LabTest, on_delete=models.CASCADE, related_name="lab_test_orders_detail"
    )
    fasting_status = models.BooleanField(default=False)
    urgency = models.CharField(
        max_length=100,
        choices=UrgencyTypeChoice.choices,
        default=UrgencyTypeChoice.NORMAL,
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="lab_test_ordered_detailed_user"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    is_lab_result_taken = models.BooleanField(default=False)
    status = models.ForeignKey(
        Status, on_delete=models.CASCADE, related_name="status_in_test_order"
    )

    def __str__(self):
        return "{}".format(self.lab_test.name)
