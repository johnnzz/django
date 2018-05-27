from django.forms import ModelForm
from .models import Post
"""
myblog forms using ModelForm
"""


# form to enter a post
class MyForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'author']