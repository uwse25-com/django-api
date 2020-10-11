from rest_framework import status, viewsets
from apps.schedules.serializers import EventSerializer, TaskSerializer
from apps.schedules.models import Event, Task


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
