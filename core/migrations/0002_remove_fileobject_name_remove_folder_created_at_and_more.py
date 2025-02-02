# Generated by Django 5.1.5 on 2025-02-02 14:10

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fileobject',
            name='name',
        ),
        migrations.RemoveField(
            model_name='folder',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='fileobject',
            name='file',
            field=models.FileField(upload_to=core.models.dynamic_upload_path),
        ),
    ]
