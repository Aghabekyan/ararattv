from django.conf.urls import patterns, url

from main import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^article/(?P<article_id>\d+)$', views.article, name='article'),
                       url(r'^program/(?P<program_id>\d+)$', views.program, name='program'),
                       url(r'^hitcounter$', views.hitcounter, name='hitcounter'),
                       # url(r'^category/(?P<category_id>\d+)$', views.category, name='category'),
                       )
