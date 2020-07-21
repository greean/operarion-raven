from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    context = {"events": Event.objects.all()}
    return render(request, "raven/index.html", context)

# def detail(request, event_id):
#     e = Event.objects.get(pk=event_id)
#     return HttpResponse(e)

def event(request, event_id):
    context = {"event": Event.objects.get(pk=event_id)}
    return render(request, "raven/event.html", context)

def city(request, city_name):
    context = {"city": Location.objects.get(name=city_name)}
    return render(request, "raven/city.html", context)   

def cities(request):
    context = {"cities": Location.objects.all()}
    return render(request, "raven/cities.html", context)