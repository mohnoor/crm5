# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-07-04 03:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_remove_custumer_cserve'),
    ]

    operations = [
        migrations.AddField(
            model_name='custumer',
            name='cserve',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='crm.serves'),
        ),
    ]
