# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-26 04:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0011_auto_20180626_1152'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='pulisher',
            new_name='pulisher1',
        ),
    ]
