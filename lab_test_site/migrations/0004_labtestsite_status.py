# Generated by Django 4.0.5 on 2023-03-21 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0001_initial'),
        ('lab_test_site', '0003_remove_labtestsite_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='labtestsite',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='labTestSite_status', to='status.status'),
            preserve_default=False,
        ),
    ]
