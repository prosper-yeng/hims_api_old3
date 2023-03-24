from dataclasses import dataclass

from django.db.models import Count

from product_category.models import ProductCategory
from product_type.models import ProductType


@dataclass
class MyEntry:
    product_category: ProductCategory
    count: int


def group_product_type():
    data = []
    queryset = ProductType.objects.values("product_category").annotate(
        count=Count("id")
    )
    for entry in queryset:
        product_category = ProductCategory.objects.get(pk=entry["product_category"])
        my_entry = MyEntry(product_category, entry["count"])
        data.append(my_entry)
        return data
