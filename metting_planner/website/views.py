from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def welcome(request):
    return HttpResponse('Hi welcome to metting planner')

def date(request):
    return HttpResponse(f'This page was served at  {str(datetime.now())}')

def about(request):
    return HttpResponse('Just gettin it prettier')