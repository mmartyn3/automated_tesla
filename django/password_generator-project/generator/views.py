from django.shortcuts import render
from django.http import HttpResponse
import random # used to generate random password


# Create your views here.

def home(request):
	return render(request, 'generator/home.html')


def password(request):
	chars = list('abcdefghijklmnopstuvqxyz')
	length = int(request.GET.get('length', 17)) # defaults to 12 if no params selected in URL i.e. localhost:8000/password/

	if request.GET.get('uppercase'):
		chars.extend(list('ABCDEFGHIJKLMNOPSTUVQXYZ'))

	if request.GET.get('numbers'):
		chars.extend(list('123456789'))

	if request.GET.get('special'):
		chars.extend(list('!@£$%&_()?'))

	userpass = ''
	for i in range(length):
		userpass += random.choice(chars)

	return render(request, 'generator/password.html', {'password':userpass})


def about(request):
	return render(request, 'generator/about.html')