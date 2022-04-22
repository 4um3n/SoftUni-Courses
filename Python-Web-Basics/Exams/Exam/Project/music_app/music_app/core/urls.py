from django.urls import path
from music_app.core.views import HomeView
from music_app.core import signals

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
]
