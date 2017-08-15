# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import embed_video.fields
import main.models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20170807_0750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='category',
            field=models.ManyToManyField(to=b'main.Category', blank=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='desc',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='hit_count',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='img',
            field=models.ImageField(default=b'', upload_to=main.models.get_file_path_img, blank=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 7, 8, 57, 20, 742304), blank=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='video',
            field=embed_video.fields.EmbedVideoField(blank=True),
        ),
    ]
