# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-28 03:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0045_auto_20200828_0247'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='payment_total',
            field=models.CharField(max_length=45, null=True),
        ),
    ]