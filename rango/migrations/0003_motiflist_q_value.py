# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-16 07:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20170815_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='motiflist',
            name='q_value',
            field=models.FloatField(null=True),
        ),
    ]
