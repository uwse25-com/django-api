from rest_framework import status, viewsets
from apps.schedules.serializers import EventSerializer
from apps.schedules.models import Event


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
