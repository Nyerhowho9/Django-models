from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 200)
    text = models.TextField()
    Created_date = models.DateTimeField()
    Published_date = models.DateTimeField()