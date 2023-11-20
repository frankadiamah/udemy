from django.db import models
from django.utils import timezone

class More(models.Model):
    title =models.CharField(max_length=100)
    description =models.TextField(max_length=10000)
    date = models.DateField()
    
    def __str__(self): 
        return  self.title
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

