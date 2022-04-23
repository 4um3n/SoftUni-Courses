from django.urls import path

from templates_advanced.pythons_auth.views import sign_up, sign_in, sign_out, \
    SignUpView

urlpatterns = [
    path('sign-up/', SignUpView.as_view(), name="sign up"),
    path('sign-in/', sign_in, name="sign in"),
    path('sign-out/', sign_out, name="sign out"),
]