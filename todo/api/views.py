from rest_framework import viewsets
from .serializers import TaskSerializer
from .models import Task

# Create your views here.


class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer