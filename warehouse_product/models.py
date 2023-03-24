from django.db import models
from choice.views import StatusChoice
from django.contrib.auth.models import User

from medication_type.models import MedicationType
from product_category.models import ProductCategory
from product_type.models import ProductType
from status.models import Status
from unit_of_measurement.models import UnitOfMeasurement
from warehouse.models import Warehouse


class WarehouseProduct(models.Model):
    warehouse = models.ForeignKey(
        Warehouse,
        on_delete=models.CASCADE,
        related_name="warehouseId_in_Wharehouse_product",
    )
    # product_category= models.ForeignKey ( ProductCategory, on_delete=models.CASCADE,
    # related_name='Procuct_category_in_Wharehouse_product' )
    product_type = models.ForeignKey(
        ProductType, on_delete=models.CASCADE, related_name="product_type_in_Wharehouse"
    )
    name = models.TextField(max_length=100, null=False, unique=True)
    brand = models.TextField(max_length=100, null=True, blank=True, unique=False)
    description = models.TextField(max_length=100, null=True, blank=True, unique=False)
    bar_code = models.TextField(max_length=200, null=True, blank=True, unique=False)
    icd_code = models.TextField(max_length=100, null=True, blank=True, unique=False)
    side_effect = models.TextField(max_length=100, null=True, blank=True, unique=False)
    serial_number = models.TextField(
        max_length=100, null=True, blank=True, unique=False
    )
    unit_of_measurement = models.ForeignKey(
        UnitOfMeasurement,
        on_delete=models.CASCADE,
        related_name="unit_of_measurement_type_in_warehouse_product",
    )
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="warehouse_product_user"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.name)
