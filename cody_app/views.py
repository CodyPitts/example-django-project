from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Event, Speaker, Session


class HomepageView(ListView):
    model = Event
    template_name = 'home.html'
    context_object_name = 'event_list'

    def get_events(self):
        return Event.objects


class SessionsView(ListView):
    model = Session
    template_name = 'schedule.html'
    context_object_name = 'session_list'

    def dispatch(self, *args, **kwargs):
        self.slug = kwargs.get('slug', None)
        self.event = get_object_or_404(Event, slug=self.slug)
        return super(SessionsView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return Session.objects.filter(event=self.event)

    def get_context_data(self, **kwargs):
        context = super(SessionsView, self).get_context_data(**kwargs)
        context['event'] = self.event

        return context


class SpeakersView(ListView):
    model = Speaker
    template_name = 'speakers.html'
    context_object_name = 'speaker_list'

    def dispatch(self, *args, **kwargs):
        self.slug = kwargs.get('slug', None)
        self.event = get_object_or_404(Event, slug=self.slug)
        self.sessions = Session.objects.filter(event=self.event)

        return super(SpeakersView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        queryset = Speaker.objects.filter(session__in=self.sessions)

        return queryset

    def get_context_data(self, **kwargs):
        context = super(SpeakersView, self).get_context_data(**kwargs)
        context['event'] = self.event

        return context


class EventBaseView(DetailView):
    model = Event
    template_name = 'eventbase.html'

    def get_context_data(self, **kwargs):
        slug = self.kwargs['slug']
        context = super(EventBaseView, self).get_context_data(**kwargs)
        context['event'] = get_object_or_404(Event, slug=slug)

        return context
