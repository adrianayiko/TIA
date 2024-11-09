from django import forms
from .models import Blog
from django.db import models  
from django.forms import fields      

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content','author','image','caption']
        
        