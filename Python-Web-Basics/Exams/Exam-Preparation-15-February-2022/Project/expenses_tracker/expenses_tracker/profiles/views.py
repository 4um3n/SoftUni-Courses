from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, FormView, UpdateView, DeleteView

from expenses_tracker.profiles.form import ProfileForm
from expenses_tracker.profiles.models import Profile


# def profile_details(request):
#     profile = Profile.objects.first()
#
#     if request.method == "GET":
#         context = {
#             "profile": profile
#         }
#         return render(request, "profile/profile.html", context)
#     else:
#         pass


class ProfileDetailsView(DetailView):
    template_name = "profile/profile.html"
    model = Profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = self.model.objects.first()
        return context

    def get_object(self, queryset=None):
        return get_object_or_404(Profile)


# def profile_edit(request):
#     profile = Profile.objects.first()
#
#     if request.method == "GET":
#         form = ProfileForm(initial=profile.__dict__)
#     else:
#         form = ProfileForm(request.POST, request.FILES, instance=profile)
#         if form.is_valid():
#             form.save()
#             return redirect("profile details")
#
#     context = {"form": form}
#     return render(request, "profile/profile-edit.html", context)


class EditProfileView(UpdateView):
    template_name = "profile/profile-edit.html"
    model = Profile
    form_class = ProfileForm

    def get_object(self, queryset=None):
        return get_object_or_404(Profile)

    def get_success_url(self):
        return reverse_lazy("profile details")


# def profile_delete(request):
#     profile = Profile.objects.first()
#
#     if request.method == "GET":
#         return render(request, "profile/profile-delete.html")
#     else:
#         profile.delete()
#         return redirect("home")


class ProfileDeleteView(DeleteView):
    template_name = "profile/profile-delete.html"

    def get_object(self, queryset=None):
        return get_object_or_404(Profile)

    def get_success_url(self):
        return reverse_lazy("home")
