# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-01-16 08:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digi', '0011_fix_guidepages_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='themepage',
            name='twitter_hashtag',
            field=models.CharField(default='', max_length=255),
        ),
    ]
