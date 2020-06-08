# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-08 19:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_auto_20200608_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='doors',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='car',
            name='fuel',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='car',
            name='passengers',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='car',
            name='transmission',
            field=models.CharField(default='', max_length=10),
        ),
    ]
