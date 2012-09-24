#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.db import models
from django.contrib import admin


class Project(models.Model):
    name = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50)
    description = models.CharField(max_length = 200)
    path = models.CharField(max_length = 50)
    commands = models.CharField(max_length = 200)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ['name',]
        
    
class Task(models.Model):
    build_id = models.CharField(max_length = 50)
    state = models.IntegerField()
    last_modify = models.DateTimeField(auto_now = True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ['last_modify',]


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'description', 'path', 'commands')
    list_filter = ('author',)
    search_fields = ('name',)

    
class TaskAdmin(admin.ModelAdmin):
    list_display = ('build_id', 'state', 'last_modify', 'last_modify')
    list_filter = ('state',)
    search_fields = ('build_id',)
    
    
admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
