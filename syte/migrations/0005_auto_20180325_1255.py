# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-25 09:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('syte', '0004_auto_20180324_1834'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='file',
        ),
    ]