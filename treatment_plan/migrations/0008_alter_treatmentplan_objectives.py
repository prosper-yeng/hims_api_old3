# Generated by Django 4.0.5 on 2023-03-07 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treatment_plan', '0007_alter_treatmentplan_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatmentplan',
            name='objectives',
            field=models.TextField(blank=True, null=True),
        ),
    ]
