from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from templates_advanced.core.views import render_page_with_form
from templates_advanced.pythons_auth.forms import SignUpForm, SignInForm


def sign_up(request):
    if request.method == "GET":
        return render_page_with_form(request, "auth/sign_up.html", SignUpForm())
    else:
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")

        return render_page_with_form(request, "auth/sign_up.html", form)


class SignUpView(CreateView):
    template_name = "auth/sign_up.html"
    form_class = SignUpForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        user = form.save()
        login(request=self.request, user=user)
        return super().form_valid(form)


def sign_in(request):
    if request.method == "GET":
        return render_page_with_form(request, "auth/sign_in.html", SignInForm())
    else:
        form = SignInForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")

        return render_page_with_form(request, "auth/sign_in.html", form)


def sign_out(request):
    logout(request)
    return redirect("index")
