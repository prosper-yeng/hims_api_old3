# Generated by Django 4.0.5 on 2023-02-01 23:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("admission", "0005_admission_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="admission",
            name="date",
            field=models.DateField(auto_now=True),
        ),
    ]
