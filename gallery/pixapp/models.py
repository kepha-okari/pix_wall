from django.db import models
import datetime as dt

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Images(models.Model):
    photo = models.ImageField(upload_to = 'Images/', null = True)
    name = models.CharField(max_length=30)
    descripton = models.TextField()
    location_taken = models.ForeignKey(Location)
    category = models.ManyToManyField(tag)
    time_uloaded = models.DateTimeField(auto_now_add=True, null=True)
