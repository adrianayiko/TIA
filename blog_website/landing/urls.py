from django.urls import path
from . import views

app_name = 'landing'
urlpatterns = [
    path('', views.home, name='home'),
    path('api-docs/', views.api_documentation, name='api_documentation'),    
]