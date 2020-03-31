from django.shortcuts import render
from .models import Blog
# Create your views here.

def all_blogs(request):
    #blog_post = Blog.objects.all() # grab all objects from database that are in the Blog model
    blog_post = Blog.objects.order_by('-date')[:3] # limit to the latest 3 objects from database that are in the Blog model i.e. last 5 blog enteries
    return render(request, 'blog/all_blogs.html', {'blog_post':blog_post})
