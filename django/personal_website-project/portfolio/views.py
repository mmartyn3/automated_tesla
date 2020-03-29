from django.shortcuts import render
from .models import Project

# Create your views here.

def home(request):
    projects = Project.objects.all() # grab all objects from database that are under Project
    return render(request, 'portfolio/home.html', {'projects':projects})
