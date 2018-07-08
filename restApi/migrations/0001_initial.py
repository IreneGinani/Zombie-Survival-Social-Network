# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-08 00:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Inventory',
                'verbose_name_plural': 'Inventories',
            },
        ),
        migrations.CreateModel(
            name='Inventory_Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('survivor_id', models.IntegerField(blank=True, default=0, null=True)),
                ('items', models.IntegerField()),
                ('inventories', models.ManyToManyField(to='restApi.Inventory', verbose_name='Inventories')),
            ],
            options={
                'verbose_name': 'Inventory_Item',
                'verbose_name_plural': 'Inventories_Items',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('point', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Items',
            },
        ),
        migrations.CreateModel(
            name='Survivor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=100)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('is_infected', models.BooleanField()),
                ('count_reports', models.IntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'verbose_name': 'Survivor',
                'verbose_name_plural': 'Survivors',
            },
        ),
        migrations.AddField(
            model_name='inventory',
            name='survivor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='restApi.Survivor', verbose_name='Survivor'),
        ),
    ]
