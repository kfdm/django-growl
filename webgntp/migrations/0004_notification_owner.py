# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-27 03:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webgntp', '0003_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='notification', to=settings.AUTH_USER_MODEL, verbose_name='owner'),
            preserve_default=False,
        ),
    ]