from django.contrib import admin
from .models import Blog

# Register your models here.
admin.site.register(Blog) # import this model inside the admin
