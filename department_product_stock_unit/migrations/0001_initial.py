# Generated by Django 4.0.5 on 2023-01-24 09:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("department_stock_order", "0001_initial"),
        ("quantity_unit_type", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("status", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="DepartmentProductStockUnit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "quantity",
                    models.DecimalField(decimal_places=1, default=0, max_digits=10),
                ),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("modified_on", models.DateTimeField(auto_now=True)),
                ("is_deleted", models.BooleanField(default=False)),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="department_stock_unit_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "department_stock",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="department_quantity",
                        to="department_stock_order.departmentstockorder",
                        verbose_name="department stock id",
                    ),
                ),
                (
                    "quantity_unit_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="quantity_unit_type_in_department_stock_unit",
                        to="quantity_unit_type.quantityunittype",
                    ),
                ),
                (
                    "status",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="status.status"
                    ),
                ),
            ],
        ),
    ]
