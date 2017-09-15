# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-05-25 13:47
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('naistenhelsinki', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='placepage',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326, verbose_name='paikka'),
        ),
    ]
