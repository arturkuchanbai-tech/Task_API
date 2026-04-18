from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TasksViewSet,TagViewSet,CategoryViewSet
router = DefaultRouter()
router.register(r'tasks', TasksViewSet)
router.register(r'tags', TagViewSet)
router.register(r'categoris', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls))
]


