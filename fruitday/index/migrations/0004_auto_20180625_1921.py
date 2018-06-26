# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-25 11:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20180625_1850'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goods',
            options={'ordering': ['price'], 'verbose_name': '商品', 'verbose_name_plural': '商品'},
        ),
        migrations.AlterModelOptions(
            name='goodstype',
            options={'verbose_name': '商品类型', 'verbose_name_plural': '商品类型'},
        ),
        migrations.AlterModelOptions(
            name='users',
            options={'ordering': ['-id'], 'verbose_name': '用户', 'verbose_name_plural': '用户'},
        ),
        migrations.AlterModelTable(
            name='goods',
            table='goods',
        ),
        migrations.AlterModelTable(
            name='users',
            table='users',
        ),
    ]
