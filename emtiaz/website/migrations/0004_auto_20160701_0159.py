# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-30 21:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20160701_0157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='image',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rate',
            field=models.PositiveIntegerField(),
        ),
    ]
