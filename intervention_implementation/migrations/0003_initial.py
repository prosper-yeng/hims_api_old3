# Generated by Django 4.0.5 on 2023-02-22 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('intervention_implementation', '0002_initial'),
        ('patient_specific_goal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='interventionimplementation',
            name='patient_specific_goal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_specific_goal_intervention_implementation', to='patient_specific_goal.patientspecificgoal'),
        ),
    ]
