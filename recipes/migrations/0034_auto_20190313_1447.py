# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-13 14:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0033_category_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='type',
            field=models.CharField(choices=[('CAT', 'Category'), ('CUS', 'Cuisines'), ('SPE', 'Special Occasions')], max_length=25),
        ),
    ]
