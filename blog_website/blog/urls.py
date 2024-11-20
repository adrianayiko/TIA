from django.urls import path
from . import views
from blog.apis import views as api_views
from rest_framework.urlpatterns import format_suffix_patterns # api
from rest_framework.authtoken.views import obtain_auth_token # api authentication

app_name = 'blog'

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('<int:pk>/', views.blog_detail, name='blog_detail'),
    path('create/', views.blog_create, name='blog_create'),
    path('<int:pk>/update/', views.blog_update, name='blog_update'),
    path('<int:pk>/delete/', views.blog_delete, name='blog_delete'),
    path('apis/', api_views.bloglist, name='blog_list_api'), # api
    path('apis/<int:pk>', api_views.blogdetail, name='blog_detail_api'), # api
    path('login/', obtain_auth_token, name='api_token_auth'), # api authentication
    path('logout/', api_views.logout, name='logout'), # api authentication
    
    
] 

urlpatterns = format_suffix_patterns(urlpatterns) # api
