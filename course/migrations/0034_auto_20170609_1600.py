# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-09 13:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0033_auto_20170428_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseinstance',
            name='archive_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='courseinstance',
            name='lifesupport_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
