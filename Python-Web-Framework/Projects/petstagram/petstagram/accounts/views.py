from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
import django.contrib.auth.urls

from petstagram.accounts.forms import UserProfileForm
from petstagram.accounts.models import UserProfile
from petstagram.common.views import render_page_with_form
from petstagram.pets.models import Pet
from petstagram.settings import LOGIN_URL


def sign_up(request):
    if request.method == "GET":
        form = UserCreationForm()
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(LOGIN_URL)

    return render_page_with_form(request, "registration/signup.html", form)


def user_profile_details(request):
    profile = UserProfile.objects.get(pk=request.user.pk)
    pets = Pet.objects.filter(user=profile)

    if request.method == "GET":
        form = UserProfileForm(initial=profile.__dict__)
    else:
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("user profile details")

    context = {
        "profile": profile,
        "pets": pets,
        "form": form,
    }
    return render(request, "accounts/user_profile.html", context)
