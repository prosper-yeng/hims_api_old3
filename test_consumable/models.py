from django.db import models
from choice.views import StatusChoice
from django.contrib.auth.models import User

from department_stock_order.models import DepartmentStockOrder
from lab_results_method.models import LabResultsMethod
from lab_test_order_details.models import LabTestOrderDetails
from lab_test_results_category.models import LabTestResultsCategory
from lab_test_results_parameters.models import LabTestResultsParameters
from lab_test_results_type.models import LabTestResultsType
from lab_test_type.models import LabTestType
from warehouse_product.models import WarehouseProduct


class TestConsumable(models.Model):
    lab_test_order_details = models.ForeignKey(
        LabTestOrderDetails,
        on_delete=models.CASCADE,
        related_name="lab_test_Consumable",
    )
    department_stock = models.ForeignKey(
        DepartmentStockOrder,
        on_delete=models.CASCADE,
        related_name="department_order_product",
    )
    quantity = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    unit_type = models.ForeignKey(
        "quantity_unit_type.QuantityUnitType",
        on_delete=models.CASCADE,
        related_name="consumable_unit_type_id",
    )

    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="test_consumable_creator"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=100, choices=StatusChoice.choices, default=StatusChoice.ACTIVE
    )

    def __str__(self):
        return "{}".format(self.lab_test_order_details)
