from .models import Tasks, Tag, Category
from rest_framework import serializers
from django.contrib.auth.models import User


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields ='__all__'
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','username']
class TasksSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)
    tags = TagSerializer(many = True, read_only = True)
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Tasks
        fields = '__all__'
