#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('onlinebuild.service.views',
    url(r'^project/$', 'project', {'project_id': None}, name = 'list'),
    url(r'^project/((?P<project_id>\d+)/)?$', 'project', name = 'detail'),
    url(r'^task/(?P<task_id>\d+)/$', 'task'),
    url(r'^build/$', 'build'),
)