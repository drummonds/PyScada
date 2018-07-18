# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-10 15:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hmi', '0010_auto_20180705_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controlitem',
            name='variable',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pyscada.Variable'),
        ),
        migrations.AlterField(
            model_name='controlitem',
            name='variable_property',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pyscada.VariableProperty'),
        ),
    ]
