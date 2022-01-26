from rest_framework import viewsets
from .serializers import TodoSerializer, TaskSerializer
from .models import Todo, Task

# Create your views here.
class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    # Auth goes here

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # Auth goes here
