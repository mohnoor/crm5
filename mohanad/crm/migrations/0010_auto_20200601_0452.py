# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-06-01 04:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0009_instalment10_cuspaid'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('payment', models.IntegerField(null=True)),
                ('paiddate', models.CharField(max_length=45, null=True)),
                ('userpaid', models.CharField(max_length=45, null=True)),
                ('billid', models.CharField(max_length=45, null=True)),
                ('cuspaid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.customer')),
            ],
        ),
        migrations.RemoveField(
            model_name='instalment10',
            name='cuspaid',
        ),
        migrations.DeleteModel(
            name='instalment10',
        ),
    ]
