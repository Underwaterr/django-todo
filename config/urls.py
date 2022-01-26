from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from todo.views import TodoViewSet, TaskViewSet

router = routers.DefaultRouter()
router.register('todo', TodoViewSet)
router.register('task', TaskViewSet)

urlpatterns = [
    path('', include(router.urls))
]
