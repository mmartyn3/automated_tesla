from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.

def all_blogs(request):
    #blog_post = Blog.objects.all() # grab all objects from database that are in the Blog model
    blog_posts = Blog.objects.order_by('-date')[:3] # limit to the latest 3 objects from database that are in the Blog model i.e. last 5 blog enteries
    return render(request, 'blog/all_blogs.html', {'blog_posts':blog_posts})

def detail(request, blog_id):
    # import get_object_or_404 module. Either return a specific page or return a page not found error i.e. 404
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blog})
