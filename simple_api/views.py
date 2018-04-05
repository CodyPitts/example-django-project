from simple_app.models import Speaker, Event
from rest_framework import viewsets
from .serializers import SpeakerSerializer, EventSerializer


class SpeakerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Speaker.objects.all().order_by('last_name')
    serializer_class = SpeakerSerializer


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
