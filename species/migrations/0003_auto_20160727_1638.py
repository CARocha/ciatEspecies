# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-27 16:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('species', '0002_auto_20160726_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='species',
            name='scientific_name',
            field=models.CharField(blank=True, max_length=450, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='species',
            unique_together=set([]),
        ),
    ]