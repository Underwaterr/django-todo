from rest_framework import serializers
from .models import Todo, Task

class TodoSerializer(serializers.ModelSerializer):
    tasks = serializers.StringRelatedField(many=True)

    class Meta:
        model = Todo
        fields = ['name', 'tasks']

class TaskSerializer(serializers.ModelSerializer): 
    todo = serializers.HyperlinkedRelatedField(view_name='todo-detail', read_only=True)

    class Meta:
        model = Task
        fields = ['name', 'is_done', 'todo']
