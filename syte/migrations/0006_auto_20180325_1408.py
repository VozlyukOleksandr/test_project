# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-25 11:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('syte', '0005_auto_20180325_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='file',
            field=models.FileField(default='', upload_to=''),
        ),
    ]
