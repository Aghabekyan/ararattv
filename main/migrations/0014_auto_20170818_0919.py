# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20170817_0450'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='program',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='content',
            name='category',
            field=models.ManyToManyField(db_index=True, to=b'main.Category', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 18, 9, 19, 46, 361952), null=True, db_index=True, blank=True),
        ),
        migrations.AlterField(
            model_name='program',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 18, 9, 19, 46, 363050), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='program',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
