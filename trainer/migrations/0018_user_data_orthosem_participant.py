# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-12 21:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0017_auto_20170605_2158'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='data_orthosem_participant',
            field=models.BooleanField(default=False),
        ),
    ]