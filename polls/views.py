from django.shortcuts import render
from django.http import HttpResponse

def polls_views(request):
    return HttpResponse('Hello World')