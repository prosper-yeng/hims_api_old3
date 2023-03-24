# Generated by Django 4.0.5 on 2023-01-24 09:12

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import validator.views


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("payment_by_sponsor", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="PaymentDetailBySponsor",
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
                    "instrument_no",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("account_no", models.CharField(blank=True, max_length=200, null=True)),
                ("payer_name", models.CharField(blank=True, max_length=200, null=True)),
                ("post_dated", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "date_received",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "instrument_image",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="instrument_image",
                        validators=[
                            validator.views.validate_file_size,
                            django.core.validators.FileExtensionValidator(
                                allowed_extensions=["jpg", "png", "bmp", "jfif"]
                            ),
                        ],
                    ),
                ),
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
                        default="active",
                        max_length=100,
                    ),
                ),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("modified_on", models.DateTimeField(auto_now=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="payment_detail_by_sponsor",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "payment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="payment_in_PaymentBySponsor_detail",
                        to="payment_by_sponsor.paymentbysponsor",
                    ),
                ),
            ],
        ),
    ]
