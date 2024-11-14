from rest_framework import serializers
from blog.models import Blog

class blogserialzer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'author', 'created_at', 'updated_at']
    