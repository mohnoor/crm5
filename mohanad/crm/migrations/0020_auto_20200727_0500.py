# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-07-27 05:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0019_auto_20200727_0239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee1',
            name='endtime',
            field=models.CharField(default='4:00 PM', max_length=45),
        ),
        migrations.AlterField(
            model_name='employee1',
            name='worktime',
            field=models.CharField(default='8:00 AM', max_length=45),
        ),
    ]