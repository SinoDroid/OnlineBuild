#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('onlinebuild.website.views',
    url(r'^$', 'project', {'project_id': None}, name = 'index'),
    url(r'^project/$', 'project', {'project_id': None}, name = 'list'),
    url(r'^project/((?P<project_id>\d+)/)?$', 'project', name = 'detail'),
    url(r'^task/(?P<task_id>\d+)/$', 'task'),
)
