# Generated by Django 4.0.5 on 2023-02-22 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0006_alter_loggedinuserdevices_options'),
        ('treatment_plan', '0005_alter_treatmentplan_patient_condition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatmentplan',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='treatment_plan_doctor', to='person.staff'),
        ),
    ]
