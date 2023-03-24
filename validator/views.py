from email.mime import image

from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django import forms


class MyDateInput(forms.DateInput):
    input_type = "date"


class MyTimeInput(forms.TimeInput):
    input_type = "time"


valid_phone_number = RegexValidator(
    regex=r"^\+?1?\d{9,15}$",
    message="Phone number must be entered in the format: '+233000000000'. "
    "Up to 15 digits allowed.",
)


def validate_file_size(file_field):
    file_size = file_field.size
    megabyte_limit = 1.00
    if file_size > megabyte_limit * 1024 * 1024:
        raise ValidationError("Max file size is %sMB" % str(megabyte_limit))
