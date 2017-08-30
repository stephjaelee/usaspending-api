# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-14 16:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('references', '0015_merge_20170712_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='congressional_code',
            field=models.TextField(blank=True, db_index=True, null=True, verbose_name='Congressional District Code'),
        ),
        migrations.AlterField(
            model_name='location',
            name='country_name',
            field=models.TextField(blank=True, db_index=True, null=True, verbose_name='Country Name'),
        ),
        migrations.AlterField(
            model_name='location',
            name='county_code',
            field=models.TextField(blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='county_name',
            field=models.TextField(blank=True, db_index=True, null=True),
        ),
    ]