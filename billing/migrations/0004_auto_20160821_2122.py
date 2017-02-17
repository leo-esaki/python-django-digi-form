# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-21 11:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0003_auto_20160821_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='target_plans',
            field=models.ManyToManyField(blank=True, help_text='Leaving empty will make this coupon valid for all plans', to='billing.Plan'),
        ),
    ]
