# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-22 10:01
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_userprofile_image'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='userprofile',
            managers=[
                ('london', django.db.models.manager.Manager()),
            ],
        ),
    ]
