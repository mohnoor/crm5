# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-28 02:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0044_replay_id1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='pointing',
            field=models.CharField(max_length=45, null=True),
        ),
    ]