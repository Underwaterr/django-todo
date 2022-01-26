from rest_framework import serializers
from .models import Todo, Task

class TodoSerializer(serializers.ModelSerializer):
    tasks = serializers.StringRelatedField(many=True)

    class Meta:
        model = Todo
        fields = ['name', 'tasks']

class TaskSerializer(serializers.HyperlinkedModelSerializer): 

    class Meta:
        model = Task
        fields = ['name', 'is_done', 'todo']
