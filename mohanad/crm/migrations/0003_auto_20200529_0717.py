# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-05-29 07:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_auto_20200529_0716'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bills',
            old_name='id1',
            new_name='id',
        ),
    ]