# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2016-06-02 17:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_auto_20160602_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='publish_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]