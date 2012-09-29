#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.http import HttpResponse

from onlinebuild.service.providers import query_project_by_id, jsonize_projects


def project(request, project_id):
    projects = query_project_by_id()
    return HttpResponse(jsonize_projects(projects))

def task(request, task_id):
    pass

def build(request, project_id):
    'Start to build a project and return a unique build id.'
    pass

def status(request, task_id):
    pass