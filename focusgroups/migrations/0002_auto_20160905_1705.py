# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-05 17:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('focusgroups', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='community',
            name='county',
        ),
        migrations.RemoveField(
            model_name='focusgroup',
            name='county',
        ),
        migrations.AddField(
            model_name='community',
            name='province',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='focusgroups.Province'),
        ),
    ]
