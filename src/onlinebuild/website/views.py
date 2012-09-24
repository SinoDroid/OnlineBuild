#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.http import HttpResponse

def project(request, pid):
    response = HttpResponse()
    if request.method == 'GET':
        if pid is None:
            return HttpResponse("Hello" + "None")
    elif request.method == 'POST':
        return HttpResponse("Hello")
    else:
        response.status_code = 405
    return response

def task(request, tid):
    response = HttpResponse()
    if request.method == 'GET':
        return HttpResponse("Hello" + tid)
    elif request.method == 'POST':
        return HttpResponse("Hello")
    else:
        response.status_code = 405
    return response

def index(request):
    response = HttpResponse()
    if request.method == 'GET':
        return HttpResponse("Hello")
    elif request.method == 'POST':
        return HttpResponse("Hello")
    else:
        response.status_code = 405
    return response

