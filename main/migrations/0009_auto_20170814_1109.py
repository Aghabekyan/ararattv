# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20170813_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='general_slider',
            field=models.BooleanField(default=False, db_index=True, verbose_name='General Slider'),
        ),
        migrations.AlterField(
            model_name='content',
            name='news_line',
            field=models.BooleanField(default=False, db_index=True, verbose_name='News Line'),
        ),
        migrations.AlterField(
            model_name='content',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 14, 11, 9, 56, 535013), null=True, blank=True),
        ),
    ]
