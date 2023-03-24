# Generated by Django 4.0.5 on 2023-01-24 09:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("company", "0001_initial"),
        ("mode_of_payment", "0001_initial"),
        ("sponsor", "0001_initial"),
        ("status", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PaymentBySponsor",
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
                ("invoice_id", models.CharField(max_length=10)),
                ("amount_paid", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "payment_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("is_deleted", models.BooleanField(default=False)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("modified_on", models.DateTimeField(auto_now=True)),
                (
                    "company",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="company_in_sponsor_payment",
                        to="company.company",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="payment_by_sponsor",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "mop",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="mop_in_sponsor_payment",
                        to="mode_of_payment.modeofpayment",
                    ),
                ),
                (
                    "sponsor",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sponsor_type_in_sponsor_payment",
                        to="sponsor.sponsor",
                    ),
                ),
                (
                    "status",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="payment_sponsor_status",
                        to="status.status",
                    ),
                ),
            ],
        ),
    ]
