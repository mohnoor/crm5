# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-08-17 05:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0036_auto_20200815_0435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='emergencycount',
            field=models.IntegerField(default=1, null=True),
        ),
    ]
