# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-25 04:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pixapp', '0005_auto_20180125_0727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pixapp.Tag'),
        ),
    ]
