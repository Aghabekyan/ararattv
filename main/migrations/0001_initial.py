# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import embed_video.fields
import datetime
import main.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['-id'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='\u054e\u0565\u0580\u0576\u0561\u0563\u056b\u0580')),
                ('desc', models.TextField()),
                ('img', models.ImageField(default=b'', upload_to=main.models.get_file_path_img)),
                ('editor_choice', models.BooleanField(default=False, verbose_name='Editor Choise')),
                ('video', embed_video.fields.EmbedVideoField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('publish_date', models.DateTimeField(default=datetime.datetime(2017, 8, 7, 6, 51, 10, 215649), blank=True)),
                ('hit_count', models.IntegerField()),
                ('category', models.ManyToManyField(to='main.Category')),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': '\u0546\u0575\u0578\u0582\u0569',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ContentImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort', models.IntegerField()),
                ('image', models.ImageField(default=b'', upload_to=main.models.get_file_path_gallery)),
                ('content', models.ForeignKey(related_name=b'images', to='main.Content')),
            ],
            options={
                'ordering': ['-sort'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['-id'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='content',
            name='lang',
            field=models.ForeignKey(blank=True, to='main.Language', null=True),
            preserve_default=True,
        ),
    ]
