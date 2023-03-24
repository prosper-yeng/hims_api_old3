from django.db import models
from django.contrib.auth.models import User, Group


from consulting_room.models import ConsultingRoom
from daily_attendance.models import DailyAttendanceModel
from person.models import Patient
from select_unit.models import SelectUnit
from status.models import Status

# from transaction.models import Transaction


class VitalSign(models.Model):
    # patient = models.ForeignKey ( Patient, on_delete=models.CASCADE, related_name='vital_sign_patient', )
    attendance = models.ForeignKey(
        DailyAttendanceModel,
        on_delete=models.CASCADE,
        related_name="vital_sign_patient",
    )

    # transaction = models.OneToOneField ( Transaction, on_delete=models.CASCADE, related_name='vital_sign_transaction', )
    weight = models.DecimalField(max_digits=10, decimal_places=1, null=True, blank=True)
    weight_unit = models.ForeignKey(
        SelectUnit,
        on_delete=models.CASCADE,
        related_name="weight_unit",
        null=True,
        blank=True,
    )
    height = models.DecimalField(max_digits=10, decimal_places=1, null=True, blank=True)
    height_unit = models.ForeignKey(
        SelectUnit,
        on_delete=models.CASCADE,
        related_name="hight_unit",
        null=True,
        blank=True,
    )
    temperature = models.DecimalField(
        max_digits=10,
        decimal_places=1,
        blank=True,
        null=True,
    )
    temperature_unit = models.ForeignKey(
        SelectUnit,
        on_delete=models.CASCADE,
        related_name="temp_unit",
        null=True,
        blank=True,
    )
    respiration_freq = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="This specifies the breathing rate",
    )
    respiration_freq_unit = models.ForeignKey(
        SelectUnit,
        on_delete=models.CASCADE,
        related_name="resp_unit",
        blank=True,
        null=True,
    )
    oxygen_saturation = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="This indicates the level of oxygen",
    )
    oxygen_saturation_unit = models.ForeignKey(
        SelectUnit,
        on_delete=models.CASCADE,
        related_name="oxygen_sat_unit",
        blank=True,
        null=True,
    )
    heart_rate = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="This indicates the heart or pulse rate",
    )
    heart_rate_unit = models.ForeignKey(
        SelectUnit,
        on_delete=models.CASCADE,
        related_name="heart_rate_unit",
        blank=True,
        null=True,
    )
    systolic_pressure = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text=" ",
    )
    systolic_pressure_unit = models.ForeignKey(
        SelectUnit,
        on_delete=models.CASCADE,
        related_name="systolic_unit",
        blank=True,
        null=True,
    )
    diastolic_pressure = models.CharField(
        max_length=100, blank=True, null=True, help_text=""
    )
    diastolic_pressure_unit = models.ForeignKey(
        SelectUnit,
        on_delete=models.CASCADE,
        related_name="diastolic_unit",
        blank=True,
        null=True,
    )
    consciousness_level = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="This indicates consciousness level of patient ",
    )
    temperature_location = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="This specifies where the temperature was taken",
    )
    pulse_rhythm = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="This indicates whether the pulse rate is regular or irregular",
    )
    history = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        help_text="This specifies the complains given by the patient ",
    )
    note = models.CharField(max_length=250, null=True, blank=True)
    consulting_room = models.ForeignKey(
        ConsultingRoom,
        on_delete=models.CASCADE,
        related_name="cons_room",
    )
    has_consultation = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="vital_sign_created_by"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    status = models.ForeignKey(
        Status, on_delete=models.CASCADE, related_name="select_item_status"
    )

    def __str__(self):
        return self.patient
