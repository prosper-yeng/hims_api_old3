from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.timezone import now


from choice.views import StatusChoice, FacilityCategoryChoice
from common.views import allowed_extension
from validator.views import validate_file_size, valid_phone_number


class Facility(models.Model):
    category = models.ForeignKey(
        "facility_category.FacilityCategory",
        on_delete=models.CASCADE,
        related_name="facility_cat",
    )
    name = models.CharField(max_length=100, null=False, verbose_name="Facility Name")
    website = models.CharField(max_length=100, null=True, blank=True)
    health_facility_code = models.CharField("Health Facility Code", max_length=255, blank=True, null=True)
    contact_name = models.CharField(
        max_length=100, null=False, verbose_name="Contact Name"
    )
    registration_no = models.CharField(
        max_length=100, null=False, verbose_name="Health service registration"
    )
    logo = models.FileField(
        validators=[
            validate_file_size,
            FileExtensionValidator(allowed_extensions=allowed_extension),
        ],
        upload_to="logos",
        verbose_name="Logo",
        null=True,
        blank=True,
    )
    primary_phone = models.CharField(
        validators=[valid_phone_number],
        blank=False,
        null=False,
        max_length=15,
        verbose_name="Primary Phone",
    )
    secondary_phone = models.CharField(
        validators=[valid_phone_number],
        max_length=15,
        verbose_name="Secondary Phone",
        blank=True,
        null=True,
    )
    email = models.EmailField(max_length=100, null=False)
    town = models.ForeignKey(
        "town.Town", on_delete=models.CASCADE, related_name="facility_town"
    )
    street = models.CharField(max_length=100, null=False, unique=False)
    postcode = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        unique=False,
        verbose_name="Postcode or Post Box",
    )
    digital_address = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        unique=False,
        verbose_name=" Digital Address",
    )
    status = models.ForeignKey(
        "status.Status", on_delete=models.CASCADE, related_name="facility_status"
    )
    default_facility = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="facility_created_by",
        max_length=100,
    )
    created_on = models.DateTimeField(default=now)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)
