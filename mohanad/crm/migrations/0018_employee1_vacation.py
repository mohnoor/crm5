# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-07-26 02:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0017_auto_20200726_0234'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee1',
            name='vacation',
            field=models.CharField(default=1, max_length=45),
            preserve_default=False,
        ),
    ]
