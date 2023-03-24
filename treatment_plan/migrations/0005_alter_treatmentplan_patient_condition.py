# Generated by Django 4.0.5 on 2023-02-18 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diagnosis', '0001_initial'),
        ('treatment_plan', '0004_alter_treatmentplan_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatmentplan',
            name='patient_condition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_condition_treatment_plan', to='diagnosis.diagnosis'),
        ),
    ]
