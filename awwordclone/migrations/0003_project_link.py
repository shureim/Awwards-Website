# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-16 11:35
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awwordclone', '0002_auto_20181116_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.TextField(null=True, validators=[django.core.validators.URLValidator()]),
        ),
    ]
