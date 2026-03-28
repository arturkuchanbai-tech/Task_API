from rest_framework import serializers
from .models import Task
class TaskDetailSerializer(serializers.ModelSerializer):
    model=Task
    field = '__all__'
class TaskListSerializer(serializers.ModelSerializer):
    model = Task
    field = ['id','title', 'description','completed','created']
    