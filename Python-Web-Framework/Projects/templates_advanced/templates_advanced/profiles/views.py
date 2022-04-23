from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from templates_advanced.profiles.forms import ProfileForm
from templates_advanced.profiles.models import Profile
from templates_advanced.settings import LOGIN_URL


@login_required(login_url=LOGIN_URL)
def profile_details(request):
    profile = Profile.objects.get(pk=request.user.id)

    if request.method == "GET":
        form = ProfileForm(initial=profile.__dict__)
    else:
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("index")

    context = {
        "form": form,
        "profile": profile,
    }
    return render(request, "profiles/profile_details.html", context)
