from django.shortcuts import render
from .TaskSerializer import TaskListSerializer,TaskDetailSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from django.db import transaction
from rest_framework.viewsets import ModelViewSet







@api_view(['GET','PUT','DELETE'])
def task_detail_api_view(request, id):
    try:
        task = Task.objects.get(id=id)
    except Task.DoesNotExist:
        return Response(data={'error':'task does in not exist!'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method =='GET':
        data=TaskDetailSerializer(task, many=False).data
        return Response(data=data)
    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        task.title=request.data.get('title')
        task.description=request.data.get('description')
        task.completed=request.data.get('completed')
        task.save()
        return Response(status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def task_list_api_view(request):
    if request.method == 'GET':
        task = Task.objects.all()
        data = TaskListSerializer(Task, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = TaskListSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,data=serializer.errors)

        title = serializer.validated_data.get('title')
        descripton = serializer.validated_data.get('description')
        completed= serializer.validated_data.get('completed')


        task = Task.objects.create(
            title=title,
            description=descripton,
            completed=completed,
        )
        return Response(status=status.HTTP_201_CREATED)
    

    

