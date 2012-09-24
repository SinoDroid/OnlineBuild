#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.http import HttpResponse

def index(request):
    response = HttpResponse()
    if request.method == 'GET':
        return HttpResponse("Hello")
    elif request.method == 'POST':
        return HttpResponse("Hello")
    else:
        response.status_code = 405
    return response

