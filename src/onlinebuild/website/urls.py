#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, url
from onlinebuild.website.views import index, project, task

urlpatterns = patterns('',
    url(r'^$', index),
    url(r'^project/((?P<pid>\d+)/)?$', project),
    url(r'^task/(?P<tid>\d+)/$', task),
)
