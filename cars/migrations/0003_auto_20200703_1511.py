# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-03 15:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_auto_20200703_1458'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='engine',
        ),
        migrations.AlterField(
            model_name='car',
            name='displacement',
            field=models.DecimalField(decimal_places=1, max_digits=4),
        ),
        migrations.AlterField(
            model_name='car',
            name='engine_type',
            field=models.CharField(choices=[('Inline 3', 'Inline 3'), ('Inline 4', 'Inline 4'), ('Inline 6', 'Inline 6'), ('Boxer 4', 'Boxer 4'), ('Boxer 6', 'Boxer 6'), ('V6', 'V6'), ('V8', 'V8'), ('V10', 'V10'), ('V12', 'V12'), ('W10', 'W10'), ('W12', 'W12'), ('Other', 'Other')], default='V8', max_length=40),
        ),
    ]