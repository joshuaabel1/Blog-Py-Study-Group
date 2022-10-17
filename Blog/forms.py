from django.forms import ModelForm
from .model.models import Post

# Mediante ModelForm le podemos dar forma a nuestro formularios personalizados.

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content','image']