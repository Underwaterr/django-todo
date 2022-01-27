from rest_framework import serializers
from .models import Todo, Task
from django.contrib.auth.models import User

class TodoSerializer(serializers.ModelSerializer):
    tasks = serializers.StringRelatedField(many=True)

    class Meta:
        model = Todo
        fields = ['name', 'tasks']


class TaskSerializer(serializers.HyperlinkedModelSerializer): 

    class Meta:
        model = Task
        fields = ['name', 'is_done', 'todo']


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return User.objects.create_superuser(**validated_data)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']
