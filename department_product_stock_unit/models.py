from django.db import models

import quantity_unit_type.models
from choice.views import StatusChoice
from django.contrib.auth.models import User
from department_stock_order.models import DepartmentStockOrder
from status.models import Status


class DepartmentProductStockUnit(models.Model):
    department_stock = models.ForeignKey(
        DepartmentStockOrder,
        on_delete=models.CASCADE,
        related_name="department_quantity",
        verbose_name="department stock id",
    )

    quantity_unit_type = models.ForeignKey(
        "quantity_unit_type.QuantityUnitType",
        on_delete=models.CASCADE,
        related_name="quantity_unit_type_in_department_stock_unit",
    )
    quantity = models.DecimalField(max_digits=10, decimal_places=1, default=0)

    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="department_stock_unit_user"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.quantity_unit_type)
