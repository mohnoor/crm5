# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-07-26 02:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0015_auto_20200726_0220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='eid',
            field=models.CharField(max_length=45),
        ),
    ]