from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from blog.models import Blog
from blog.apis.serializers import blogserialzer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# FILE: blog_website/blog/apis/test_views.py


class BlogListTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('blog:blog_list')
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_get_bloglist(self):
        Blog.objects.create(title='Test Blog', content='Test Content')
        response = self.client.get(self.url)
        blogs = Blog.objects.all()
        serializer = blogserialzer(blogs, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_post_bloglist(self):
        data = {'title': 'New Blog', 'content': 'New Content'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Blog.objects.count(), 1)
        self.assertEqual(Blog.objects.get().title, 'New Blog')

class BlogDetailTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.blog = Blog.objects.create(title='Test Blog', content='Test Content')
        self.url = reverse('blog:blog_detail', kwargs={'pk': self.blog.pk})
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_get_blogdetail(self):
        response = self.client.get(self.url)
        serializer = blogserialzer(self.blog)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_put_blogdetail(self):
        data = {'title': 'Updated Blog', 'content': 'Updated Content'}
        response = self.client.put(self.url, data, format='json')
        self.blog.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.blog.title, 'Updated Blog')

    def test_delete_blogdetail(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Blog.objects.count(), 0)

class LogoutTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('users:logout_view')
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_logout(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(Token.objects.filter(user=self.user).exists())