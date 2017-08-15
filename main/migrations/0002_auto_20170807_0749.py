# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='content',
            options={'ordering': ['-id'], 'verbose_name': '\u0546\u0575\u0578\u0582\u0569', 'verbose_name_plural': '\u0546\u0575\u0578\u0582\u0569\u0565\u0580'},
        ),
        migrations.RemoveField(
            model_name='content',
            name='editor_choice',
        ),
        migrations.RemoveField(
            model_name='content',
            name='lang',
        ),
        migrations.DeleteModel(
            name='Language',
        ),
        migrations.AddField(
            model_name='content',
            name='general_slider',
            field=models.BooleanField(default=False, verbose_name='General Slider'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='content',
            name='news_line',
            field=models.BooleanField(default=False, verbose_name='News Line'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='content',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 7, 7, 49, 22, 838268), blank=True),
        ),
    ]
