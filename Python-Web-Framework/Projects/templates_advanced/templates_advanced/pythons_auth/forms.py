from django import forms
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

UserModel = get_user_model()


class SignUpForm(UserCreationForm):
    class Meta:
        model = UserModel
        # field_classes = {}
        fields = ["username"]


class SignInForm(forms.Form):
    user = None
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput()
    )

    def clean_password(self):
        self.user = authenticate(
            username=self.cleaned_data["username"],
            password=self.cleaned_data["password"]
        )

        if self.user is None:
            raise ValidationError("Incorrect username/password")

    def save(self):
        return self.user
