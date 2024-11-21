from django.shortcuts import render
from blog.models import Blog

def home(request):
    blogs = Blog.objects.all()
    return render(request, 'landing/home.html', {'blogs': blogs})
def api_documentation(request):
    return render(request, 'landing/api_documentation.html')