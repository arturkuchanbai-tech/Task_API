from django.urls import path
from . views import TaskDetailSerializer,TaskListSerializer
urlpatterns = [
    path('task/',TaskListSerializer),
    path('<int:id>/',TaskDetailSerializer)
]
