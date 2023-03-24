from django.db import models

import quantity_unit_type.models
from choice.views import StatusChoice
from django.contrib.auth.models import User

from department.models import Department
from order_batch.models import OrderBatch
from status.models import Status

from warehouse_product.models import WarehouseProduct


class DepartmentStockOrder(models.Model):
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="department"
    )
    order_batch = models.ForeignKey(
        OrderBatch, on_delete=models.CASCADE, related_name="order_batch"
    )
    warehouse_product = models.ForeignKey(
        WarehouseProduct,
        on_delete=models.CASCADE,
        related_name="wharehouse_supplier_in_stock",
    )
    order_quantity_unit_type = models.ForeignKey(
        "quantity_unit_type.QuantityUnitType",
        on_delete=models.CASCADE,
        related_name="order_quantity_unit_type",
    )
    order_quantity = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    expiry_date = models.DateField(null=True, blank=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="department_order_user"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.warehouse_product)
