#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, url
from onlinebuild.service.views import index

urlpatterns = patterns('',
    url(r'^categories/$', index),
)
