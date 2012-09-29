#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.http import HttpResponse
from django.template import loader, Context

from onlinebuild.service.providers import query_projects, query_project_by_id, query_tasks

def project(request, project_id):
    if project_id:
        projects = query_project_by_id(project_id)
        context_dict = {
            'projects' : projects,
        }
        pass
        t = loader.get_template('project_detail.tpl')
    else:
        projects = query_projects()
        context_dict = {
            'projects' : projects,
        }
        t = loader.get_template('project_list.tpl')
    c = Context(context_dict)
    return HttpResponse(t.render(c))

def task(request, task_id):
    response = HttpResponse()
    if request.method == 'GET':
        return HttpResponse("Hello" + task_id)
    elif request.method == 'POST':
        return HttpResponse("Hello")
    else:
        response.status_code = 405
    return response