from django.forms import ModelForm
from .model.models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content','image']