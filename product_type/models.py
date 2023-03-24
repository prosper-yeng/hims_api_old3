from django.db import models
from choice.views import StatusChoice
from django.contrib.auth.models import User

from product_category.models import ProductCategory
from status.models import Status


class ProductType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, null=True, blank=True, unique=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.name)
