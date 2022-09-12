from datetime import datetime
from turtle import title
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(null=True, max_length=120)
    content = models.CharField(null=True, max_length=500)
    date = models.CharField(null=True, max_length=120)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(null=True, max_length=500)
    date = models.DateTimeField(datetime.now())

# que es un modelo?
# los modelos son lo que conocemos como clases 
# estos crean objetos por instancias desde nuestras views.