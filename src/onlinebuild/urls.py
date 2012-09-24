#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^service/', include('onlinebuild.service.urls')),
    url(r'^website/', include('onlinebuild.website.urls')),
    url(r'^', include('onlinebuild.website.urls')),
)
