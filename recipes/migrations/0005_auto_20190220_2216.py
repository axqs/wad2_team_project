# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-02-20 22:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_auto_20190220_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='chef',
            name='fname',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='chef',
            name='lname',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]