from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

from meetings.models import Meeting

# Create your views here.

def welcome(request):
    return render(request, "website/welcome.html",
    {"num_meetings": Meeting.objects.count()})

def date(request):
    return HttpResponse(f'This page was served at  {str(datetime.now())}')
  
def about(request):
    return HttpResponse('Just gettin it prettier')

