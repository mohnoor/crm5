# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-30 04:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0050_auto_20200830_0400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bills',
            name='enddate',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='bills',
            name='startdate',
            field=models.DateTimeField(null=True),
        ),
    ]