from django.db import models

# Create your models here.

class Project(models.Model): # required to generate table in database
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True) # blank makes the field optional i.e. if don't want a url attached to the image

    def __str__(self):
        """return default name for admin page"""
        return self.title
