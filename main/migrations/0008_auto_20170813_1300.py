# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20170807_0858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 13, 13, 0, 43, 69310), null=True, blank=True),
        ),
    ]
