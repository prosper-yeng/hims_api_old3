# Generated by Django 4.0.5 on 2023-01-24 09:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="OpdBillType",
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
                ("name", models.CharField(max_length=100, unique=True)),
                ("adult_price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("child_price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("adult_discount", models.DecimalField(decimal_places=2, max_digits=5)),
                ("child_discount", models.DecimalField(decimal_places=2, max_digits=5)),
                ("created_on", models.DateTimeField(default=django.utils.timezone.now)),
                ("modified_on", models.DateTimeField(auto_now=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("created", "Created"),
                            ("approved", "Approved"),
                            ("active", "Active"),
                            ("deactivate", "Deactivate"),
                            ("suspended", "Suspended"),
                            ("delete", "Delete"),
                            ("closed", "Closed"),
                            ("registered", "Registered"),
                            ("vital done", "Vital Done"),
                            ("diagnosed", "Diagnosed"),
                            ("billed", "Billed"),
                            ("pending lab", "Pending Lab"),
                            ("pending pharmacy", "Pending Pharmacy"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="opd_billing_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
