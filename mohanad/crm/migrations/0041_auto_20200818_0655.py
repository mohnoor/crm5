# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-18 06:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0040_auto_20200818_0646'),
    ]

    operations = [
        migrations.DeleteModel(
            name='USCitizen',
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'permissions': (('can_change_service', 'Can change service'),)},
        ),
    ]
