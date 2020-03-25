from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
	return render(request,
				  'generator/home.html',
				  {'password':'bburnley'})

def easter_egg(request):
	return HttpResponse("<h1>EGGS !</h1>")