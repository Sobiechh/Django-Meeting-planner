from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory

# Create your views here.

from .models import Meeting, Room
from .forms import MeetingForm

def detail(request, id):

    meeting = get_object_or_404(Meeting, pk=id)
    #better option is to replace this with get_or_404
    #meeting = Meeting.objects.get(pk=id) #pk primary key
    return render(request, "meetings/detail.html", 
    {"meeting":meeting})

def rooms_list(request):
    return render(request, "meetings/rooms_list.html", 
    {"rooms": Room.objects.all()})

MeetingForm = modelform_factory(Meeting, exclude=[]) #help with html form


def new(request):
    if request.method == "POST":
        # after subbmiting the form, process data
        form = MeetingForm(request.POST)
        if form.is_valid(): #eg wrong date
            form.save()
            return redirect("home")
    else:
        form = MeetingForm()
    return render(request, "meetings/new.html", {"form": form})