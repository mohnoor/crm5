# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-31 02:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0051_auto_20200830_0401'),
    ]

    operations = [
        migrations.AddField(
            model_name='bills',
            name='credit',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='bills',
            name='creditdate',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='bills',
            name='usercredit',
            field=models.CharField(max_length=45, null=True),
        ),
    ]
