from django.db import models

import quantity_unit_type.models
from choice.views import StatusChoice
from django.contrib.auth.models import User

from status.models import Status
from supplier.models import Supplier
from warehouse_product.models import WarehouseProduct


class WarehouseStock(models.Model):
    warehouse_product = models.ForeignKey(
        WarehouseProduct,
        on_delete=models.CASCADE,
        related_name="warehouse_product_id_in_stock",
    )
    supplier = models.ForeignKey(
        Supplier, on_delete=models.CASCADE, related_name="wharehouse_supplier_in_stock"
    )
    quantity_unit_type = models.ForeignKey(
        "quantity_unit_type.QuantityUnitType",
        on_delete=models.CASCADE,
        related_name="quantity_unit_type_id",
    )
    ordered_quantity = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    reorder_level = models.IntegerField(default=0)
    quantity = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    note = models.TextField(max_length=200, null=True, blank=True, unique=False)
    batch_no = models.TextField(max_length=200, null=True, blank=True, unique=False)
    expiry_date = models.DateField(null=True, blank=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="warehouse_stock_quantity_user"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.batch_no)

    def save(self, *args, **kwargs):
        if not self.ordered_quantity:
            self.ordered_quantity = self.quantity
        super().save(*args, **kwargs)