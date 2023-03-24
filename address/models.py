import pytz
from django.db import models
from django.contrib.auth.models import User

# from users.models import CustomUser
from django.utils.timezone import now

from choice.views import StatusChoice, AddressTypeChoice


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="person")
    address_type = models.CharField(
        max_length=100, null=True, blank=True, choices=AddressTypeChoice.choices
    )
    # country = models.ForeignKey ( 'nation.Nation', on_delete=models.CASCADE, related_name='address_country' )
    # region = models.ForeignKey ( 'region.Region', on_delete=models.CASCADE, related_name='address_region' )
    # district = models.ForeignKey ( 'district.District', on_delete=models.CASCADE, related_name='address_district' )
    town = models.ForeignKey(
        "town.Town", on_delete=models.CASCADE, related_name="address_town"
    )
    street = models.CharField(max_length=100, null=False, unique=False)
    postcode = models.CharField(
        max_length=100, null=False, unique=False, verbose_name="Postcode/Post Box"
    )
    house_number = models.CharField(
        max_length=100, null=False, unique=False, verbose_name=" House Number "
    )
    digital_address = models.CharField(
        max_length=100, null=True, unique=False, verbose_name=" Digital Address"
    )
    status = models.CharField(
        max_length=100, null=True, blank=True, choices=StatusChoice.choices
    )
    created_by = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    created_on = models.DateTimeField(default=now)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} {}".format(self.person, self.town)
