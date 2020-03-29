"""password_generator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from generator import views

urlpatterns = [
    path('', views.home, name='home'), # when no extension is added i.e. homepage e.g. google.com
    path('password/', views.password, name='password'), # when extension called "easter_egg" is added e.g. google.com/easter_egg
    path('about', views.about, name='about')
]
