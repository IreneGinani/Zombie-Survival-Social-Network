# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-06 17:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restApi', '0003_inventory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survivor',
            name='count_reports',
            field=models.IntegerField(default=0),
        ),
    ]
