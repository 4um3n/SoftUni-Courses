from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from music_app.profiles.models import Profile


class HomeView(TemplateView):
    def get(self, request, *args, **kwargs):
        profile = Profile.objects.first()

        if profile is None:
            return redirect("create profile")
        else:
            return redirect("list albums")
