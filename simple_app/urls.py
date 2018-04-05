from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomepageView.as_view(), name='home'),
    path('<slug:slug>/', views.EventBaseView.as_view(), name='eventbase'),
    path('<slug:slug>/speakers/', views.SpeakersView.as_view(), name='speakers'),
    path('<slug:slug>/schedule/', views.SessionsView.as_view(), name='schedule'),
]
