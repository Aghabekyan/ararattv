#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from embed_video.fields import EmbedVideoField

import uuid
import os
import time
# Create your models here.


def get_file_path_img(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s/%s.%s" % (time.strftime("%Y/%m/%d"), uuid.uuid4(), ext)
    return os.path.join('img/', filename)


def get_file_path_gallery(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s/%s.%s" % (time.strftime("%Y/%m/%d"), uuid.uuid4(), ext)
    return os.path.join('gallery/', filename)


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return '%s' % (self.name)

    class Meta:
        ordering = ["-id"]


class ContentImage(models.Model):
    content = models.ForeignKey('Content', related_name='images')
    sort = models.IntegerField()
    image = models.ImageField(upload_to=get_file_path_gallery, default='')

    def image_tag(self):
        return u'<img src="%s" height="100"/>' % self.image.url
    image_tag.allow_tags = True

    def __unicode__(self):
        return '%s' % ('Gallery Image')

    class Meta:
        ordering = ["-sort"]

from django import forms
from django.utils.safestring import mark_safe
from django.utils.html import format_html


class Content(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(blank=True, null=True)
    img = models.ImageField(upload_to=get_file_path_img, default='', blank=True, null=True)
    category = models.ManyToManyField('Category', blank=True, null=True)
    general_slider = models.BooleanField(
        default=False, verbose_name=u'General Slider', db_index=True)
    news_line = models.BooleanField(default=False, verbose_name=u'News Line', db_index=True)
    video = EmbedVideoField(blank=True)  # same like models.URLField()
    create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    publish_date = models.DateTimeField(default=datetime.now(), blank=True, null=True)
    hit_count = models.IntegerField(blank=True, null=True, default=0)

    def image_tag(self):
        if self.img:
            return u'<img src="%s" height="100"/>' % self.img.url
        else:
            return u'<img src="http://www.almau.edu.kz/img/no_image.png" height="100"/>'

    def video_tag(self):
        if self.video:
            return format_html(('<iframe width="150" height="100" src="%s?rel=0&amp;showinfo=0" frameborder="0" allowfullscreen></iframe>' % self.video).replace("watch?v=", "embed/"))
        else:
            return ''

    image_tag.allow_tags = True

    class Meta:
        ordering = ["-id"]
        verbose_name = "Article"
        verbose_name_plural = "Articles"


class Program(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField(default=datetime.now(), blank=True, null=True)

    class Meta:
        ordering = ["-date"]
