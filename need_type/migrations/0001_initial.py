# Generated by Django 4.0.5 on 2023-02-22 23:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nurses_note', '0004_alter_nursesnote_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='NeedType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=255)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('nurses_note', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='nurses_note_need_type', to='nurses_note.nursesnote')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
