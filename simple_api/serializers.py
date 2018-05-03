from simple_app.models import Speaker, Event
from rest_framework import serializers


class SpeakerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Speaker
        fields = ('first_name', 'last_name', 'title', 'bio', 'url')


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('event_name', 'start_date', 'end_date', 'city', 'state', 'venue', 'description', 'url')
