from django.db import models

# Create your models here.
class Todo(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=256)
    is_done = models.BooleanField(default=False)
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.name
