from django.shortcuts import render
from django.urls import reverse_lazy
from music_app.profiles.models import Profile
from music_app.profiles.forms import ProfileForm
from django.views.generic import CreateView, DeleteView, DetailView


class CreateProfileView(CreateView):
    template_name = "profile/home-no-profile.html"
    form_class = ProfileForm
    success_url = reverse_lazy("home")


class DeleteProfileView(DeleteView):
    template_name = "profile/profile-delete.html"
    form_class = ProfileForm
    model = Profile
    success_url = reverse_lazy("home")

    def get_object(self, queryset=None):
        return self.model.objects.first()

    def get_form_kwargs(self):
        kwargs = super(DeleteProfileView, self).get_form_kwargs()
        kwargs["disable_fields"] = True
        return kwargs

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return self.form_valid(self.get_form())


class ProfileDetailsView(DetailView):
    template_name = "profile/profile-details.html"
    model = Profile

    def get_object(self, queryset=None):
        return self.model.objects.first()

