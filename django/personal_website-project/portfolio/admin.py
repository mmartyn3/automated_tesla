from django.contrib import admin
from .models import Project

admin.site.register(Project) # import this model inside the admin
