# Generated by Django 4.0.5 on 2023-03-07 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radiology_type', '0002_alter_radiologytype_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='radiologytype',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
