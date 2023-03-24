import datetime

import pytz
from django.db import models
from django.contrib.auth.models import User, Group
from hims_api.basemodel import BaseModel
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now

from choice.views import StatusChoice, GenderChoice
from facility.models import Facility
from language.models import Language
from status.models import Status
from validator.views import validate_file_size, valid_phone_number
from common.views import allowed_extension

from django.core.validators import FileExtensionValidator
from hims_api.basemodel import BaseModel
from .utils import get_random_string

Group.add_to_class("default", models.BooleanField(default=False))

User.add_to_class(
    "group",
    models.ForeignKey(
        Group, on_delete=models.CASCADE, null=False, blank=False, related_name="group"
    ),
)
User.add_to_class(
    "middle_name",
    models.CharField(max_length=50, blank=True, null=True, verbose_name="Middle Name"),
)
User.add_to_class("date_of_birth", models.DateField(max_length=8))
User.add_to_class(
    "gender",
    models.CharField(
        max_length=100, choices=GenderChoice.choices, default=GenderChoice.MALE
    ),
)
User.add_to_class(
    "facility",
    models.ForeignKey(
        "facility.Facility",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name="facility",
    ),
)
User.add_to_class(
    "nationality",
    models.CharField(max_length=100, choices=pytz.country_names.items(), default="GH"),
)
User.add_to_class(
    "national_id", models.CharField(max_length=100, blank=True, null=True)
)
User.add_to_class(
    "photo_url",
    models.FileField(
        validators=[
            validate_file_size,
            FileExtensionValidator(allowed_extensions=allowed_extension),
        ],
        upload_to="persons",
        verbose_name="Photo",
        null=True,
        blank=True,
    ),
)
User.add_to_class(
    "primary_phone",
    models.CharField(
        validators=[valid_phone_number],
        max_length=15,
        blank=False,
        null=False,
        verbose_name="Primary Phone",
    ),
)
User.add_to_class(
    "secondary_phone",
    models.CharField(
        validators=[valid_phone_number],
        max_length=15,
        verbose_name="Secondary Phone",
        blank=True,
        null=True,
    ),
)
User.add_to_class("default_pwd_changed", models.BooleanField(default=False))
User.add_to_class(
    "status",
    models.ForeignKey(Status, on_delete=models.CASCADE, related_name="user_status"),
)
User.add_to_class(
    "created_by",
    models.IntegerField(
        null=False,
        blank=False,
    ),
)
User.add_to_class("created_on", models.DateTimeField(default=now))


class Patient(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="patient_user",
    )
    title = models.ForeignKey(
        "person_title.PersonTitle",
        on_delete=models.CASCADE,
        related_name="patient_title",
        null=True,
        blank=True,
    )
    hospital_record_no = models.CharField("Hospital Record Number", max_length=255, blank=True, null=True)
    marital_status = models.ForeignKey(
        "marital_status.MaritalStatus",
        null=True,
        on_delete=models.CASCADE,
        related_name="patient_marital_status",
    )
    occupation = models.ForeignKey(
        "occupation.Occupation",
        on_delete=models.CASCADE,
        related_name="patient_occupation",
    )

    religion = models.ForeignKey(
        "religion.Religion", on_delete=models.CASCADE, related_name="patient_religion"
    )
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="patient_by"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    status = models.ForeignKey(
        Status, on_delete=models.CASCADE, related_name="patient_status"
    )

    def __str__(self):
        if self.user.middle_name:
            return "{} {} {}".format(
                self.user.first_name, self.user.middle_name, self.user.last_name
            )
        else:
            return "{} {}".format(self.user.first_name, self.user.last_name)

    @property
    def full_name(self):
        if self.user.middle_name:
            f_name = "{} {} {}".format(
                self.user.first_name, self.user.middle_name, self.user.last_name
            )
        else:
            f_name = "{} {}".format(self.user.first_name, self.user.last_name)

        return "{} {}".format(self.title.text, f_name)


class Staff(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user",
    )
    title = models.ForeignKey(
        "person_title.PersonTitle",
        on_delete=models.CASCADE,
        related_name="staff_title",
        null=True,
        blank=True,
    )
    marital_status = models.ForeignKey(
        "marital_status.MaritalStatus",
        null=True,
        on_delete=models.CASCADE,
        related_name="staff_marital_status",
    )
    occupation = models.ForeignKey(
        "occupation.Occupation",
        on_delete=models.CASCADE,
        related_name="staff_occupation",
    )

    religion = models.ForeignKey(
        "religion.Religion",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="staff_religion",
    )

    def __str__(self):
        if self.user.middle_name:
            return "{} {} {}".format(
                self.user.first_name, self.user.middle_name, self.user.last_name
            )
        else:
            return "{} {}".format(self.user.first_name, self.user.last_name)

    @property
    def full_name(self):
        if self.user.middle_name:
            f_name = "{} {} {}".format(
                self.user.first_name, self.user.middle_name, self.user.last_name
            )
        else:
            f_name = "{} {}".format(self.user.first_name, self.user.last_name)

        return "{} {}".format(self.title.text, f_name)


class UserVerificationCode(BaseModel):
    code = models.CharField(max_length=75)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_verification_code_user"
    )
    expires = models.DateTimeField(default=datetime.datetime.utcnow)

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name_plural = "Verification Codes"

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = get_random_string(75)
        super().save(*args, **kwargs)

    def is_expired(self):
        return datetime.datetime.utcnow().hour > self.expires.hour + 2

    def get_duration(self):
        current_hour = datetime.datetime.utcnow().hour
        expired_hour = self.expires.hour
        return current_hour - 3 > expired_hour


class LoggedInUserDevices(BaseModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="logged_in_user_user"
    )
    ip_address = models.GenericIPAddressField()
    os = models.CharField(max_length=255)
    browser = models.CharField(max_length=255)
    expires = models.DateTimeField(default=datetime.datetime.utcnow)
    is_active = models.BooleanField(default=True)

    def is_refresh_token_expired(self):
        return datetime.datetime.utcnow().day >= self.created_at.day + 1

    class Meta:
        ordering = ["-id"]
