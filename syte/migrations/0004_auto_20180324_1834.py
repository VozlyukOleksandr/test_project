# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-24 16:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('syte', '0003_auto_20180324_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='bir_day',
            field=models.DateField(null=True),
        ),
    ]
