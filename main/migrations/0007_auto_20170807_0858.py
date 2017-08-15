# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import main.models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20170807_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='category',
            field=models.ManyToManyField(to=b'main.Category', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='desc',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='hit_count',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='img',
            field=models.ImageField(default=b'', null=True, upload_to=main.models.get_file_path_img, blank=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 7, 8, 58, 26, 342362), null=True, blank=True),
        ),
    ]
