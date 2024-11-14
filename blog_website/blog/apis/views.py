from django.http import JsonResponse
from blog.models import Blog
from .serializers import blogserialzer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def bloglist(request, format=None):
    if request.method == 'GET':
        blogs = Blog.objects.all()
        serializer = blogserialzer(blogs, many=True)
        return Response(serializer.data)  
    elif request.method == 'POST':
        serializer = blogserialzer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
@api_view(['GET', 'PUT', 'DELETE'])
def blogdetail(request, pk, format=None):
    try:
        blog = Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = blogserialzer(blog)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = blogserialzer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)