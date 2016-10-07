# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-06 16:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 6, 16, 35, 38, 430203, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='purchasedad',
            name='cost',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='purchasedad',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 6, 16, 35, 38, 519262, tzinfo=utc)),
        ),
    ]