# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-26 11:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_goods_goodstype'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='unit',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
