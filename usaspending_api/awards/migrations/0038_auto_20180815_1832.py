# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-15 18:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0037_merge_subaward_and_subaward_matview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='award',
            name='uri',
            field=models.TextField(blank=True, db_index=True, help_text='The uri of the award', null=True),
        ),
    ]
