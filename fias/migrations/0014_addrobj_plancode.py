# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-12-24 05:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fias', '0013_auto_20160825_0524'),
    ]

    operations = [
        migrations.AddField(
            model_name='addrobj',
            name='plancode',
            field=models.CharField(default='0000', max_length=4, verbose_name='Код элемента планировочной структуры'),
            preserve_default=False,
        ),
    ]
