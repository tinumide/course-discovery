# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-09-10 17:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_add_case_record_type_id'),
        ('course_metadata', '0195_auto_20190909_1601'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='course',
            unique_together=set([('partner', 'key', 'draft'), ('partner', 'url_slug', 'draft'), ('partner', 'uuid', 'draft')]),
        ),
    ]