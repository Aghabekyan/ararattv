# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20170818_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 18, 9, 19, 55, 237614), null=True, db_index=True, blank=True),
        ),
        migrations.AlterField(
            model_name='program',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 18, 9, 19, 55, 238839), null=True, blank=True),
        ),
    ]
