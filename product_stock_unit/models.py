from django.db import models

import quantity_unit_type.models
from choice.views import StatusChoice
from django.contrib.auth.models import User

from medication.models import Medication
from medication_quantity.models import MedicationQuantity
from quantity_unit_type.models import QuantityUnitType
from medication_unit_of_measurement.models import MedicationUnitOfMeasurement
from status.models import Status
from supplier.models import Supplier
from unit_of_measurement.models import UnitOfMeasurement
from warehouse_stock.models import WarehouseStock


class ProductStockUnit(models.Model):
    warehouse_stock = models.ForeignKey(
        WarehouseStock,
        on_delete=models.CASCADE,
        related_name="warehouse_quantity",
        verbose_name="Warehouse stock id",
    )

    quantity_unit_type = models.ForeignKey(
        "quantity_unit_type.QuantityUnitType",
        on_delete=models.CASCADE,
        related_name="quantity_unit_type_in_Product_stock_unit",
    )
    quantity = models.DecimalField(max_digits=10, decimal_places=1, default=0)

    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="product_stock_unit_user"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.quantity_unit_type)
