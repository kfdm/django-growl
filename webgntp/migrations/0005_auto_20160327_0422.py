# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-27 04:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webgntp', '0004_notification_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prowlkey',
            name='key',
            field=models.CharField(max_length=40),
        ),
    ]
