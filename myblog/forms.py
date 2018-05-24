from django.forms import ModelForm
from .models import Post


class MyForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'author']