from django.db import models

# Create your models here.

class Blog(models.Model): # required to generate table in database
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/images/')
    date = models.DateField()
