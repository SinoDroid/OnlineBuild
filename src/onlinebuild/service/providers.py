#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.utils import simplejson

from onlinebuild.service.models import Project, Task
from onlinebuild.utils.datetime import timestamp

def query_projects():
    'Retrieve all the projects.'
    projects = Project.objects.all()
    return projects

def query_project_by_id(project_id):
    'Retrieve project by its id.'
    projects = Project.objects.all()
    projects = projects.filter(id=project_id)
    return projects

def query_tasks(category_id, keyword, sort_order):
    tasks = Task.objects.all()
    return tasks

def jsonize_projects(projects):
    'Convert the project list to JSON array.'
    project_list = []
    for project in projects:
        project_dict = {
            "Id" : project.id,
            "Name" : project.name,
            "Author" : project.author,
            "Description" : project.description,
            "Path" : project.path,
            "Commands" : project.commands,
            "LastModify" : timestamp(project.last_modify),
        }
        project_list.append(project_dict)
    return simplejson.dumps(project_list)

def jsonize_project(project, app_name, package_name, version_code, version_name):
    'Convert the project to JSON array.'
    pass

def jsonize_tasks(tasks):
    'Convert the task list to JSON array.'
    pass

def jsonize_task(task):
    'Convert the task to JSON array.'
    pass

def build_project(project, build_id):
    'Build a project, and then write to result to the database.'
    pass