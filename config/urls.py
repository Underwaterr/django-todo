from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from todo.views import TodoViewSet, TaskViewSet, UserViewSet

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register('todo', TodoViewSet)
router.register('task', TaskViewSet)
router.register('user', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh-token/', TokenRefreshView.as_view()),
]
