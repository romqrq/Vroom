# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-14 16:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_delete_addon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='county',
            field=models.CharField(blank=True, choices=[('Dublin', 'Dublin'), ('Cork', 'Cork'), ('Galway', 'Galway')], max_length=30),
        ),
        migrations.AlterField(
            model_name='car',
            name='image2',
            field=models.ImageField(blank=True, upload_to='media/images'),
        ),
        migrations.AlterField(
            model_name='car',
            name='image3',
            field=models.ImageField(blank=True, upload_to='media/images'),
        ),
        migrations.AlterField(
            model_name='car',
            name='image4',
            field=models.ImageField(blank=True, upload_to='media/images'),
        ),
        migrations.AlterField(
            model_name='car',
            name='image5',
            field=models.ImageField(blank=True, upload_to='media/images'),
        ),
    ]
