from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(null=True, max_length=120)
    content = models.CharField(null=True, max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    image= models.ImageField(upload_to="staticfiles/image", null=True)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(null=True, max_length=500)
    date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.post, self.user

# que es un modelo?
# los modelos son lo que conocemos como clases 
# estos crean objetos por instancias desde nuestras views.