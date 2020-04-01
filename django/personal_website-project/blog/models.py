from django.db import models

# Create your models here.

class Blog(models.Model): # required to generate table in database
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/images/')
    date = models.DateField()

    def __str__(self):
        """return default name for admin page"""
        return self.title + "---" + self.description[:50]
