# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-26 05:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0013_auto_20180626_1305'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='pulisher',
            new_name='pusher',
        ),
    ]
