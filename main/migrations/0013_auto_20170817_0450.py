# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20170815_1305'),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='\u054e\u0565\u0580\u0576\u0561\u0563\u056b\u0580')),
                ('date', models.DateTimeField(default=datetime.datetime(2017, 8, 17, 4, 50, 52, 478336), null=True, blank=True)),
            ],
            options={
                'ordering': ['-id'],
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='content',
            options={'ordering': ['-id'], 'verbose_name': 'Article', 'verbose_name_plural': 'Articles'},
        ),
        migrations.AlterField(
            model_name='content',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 17, 4, 50, 52, 476933), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
