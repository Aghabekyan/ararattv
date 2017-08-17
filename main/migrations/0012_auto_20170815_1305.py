# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20170815_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='hit_count',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 15, 13, 5, 20, 401583), null=True, blank=True),
        ),
    ]
