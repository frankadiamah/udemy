
from django.db import models
from embed_video.fields import EmbedVideoField
from . validators import file_size

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='static/practice/')
    url = models.URLField(blank=True)
    
    def __str__(self): 
        return  self.title + self.description

class Video(models.Model):
    caption =models.CharField(max_length=200)
    video = models.FileField(upload_to='static/practice/',validators=[file_size])   
    def __str__(self):
        return self.caption 
    

class Item(models.Model):
    video = EmbedVideoField()     

    def __str__(self):
        return self.video