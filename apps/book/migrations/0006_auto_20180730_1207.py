# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-07-30 04:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_auto_20180730_1126'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='prod',
            new_name='pro',
        ),
    ]
