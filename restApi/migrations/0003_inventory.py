# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-06 17:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restApi', '0002_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('survivor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restApi.Survivor', verbose_name='Survivor')),
            ],
            options={
                'verbose_name': 'Inventory',
                'verbose_name_plural': 'Inventories',
            },
        ),
    ]
