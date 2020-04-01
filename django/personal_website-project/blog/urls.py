from django.urls import path
from . import views

app_name = 'blog'

# acts as homepage for Blog app
urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'), # when someone comes to the blog, is there any part of the url that is an int. If so, pass it on to the detail function in views.py
]
