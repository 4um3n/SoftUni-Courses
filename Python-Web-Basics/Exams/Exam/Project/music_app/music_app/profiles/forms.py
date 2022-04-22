from music_app.core import forms
from music_app.profiles.models import Profile


class ProfileForm(forms.CustomModelForm):
    class Meta:
        model = Profile
        fields = "__all__"

    placeholders = {
        "username": "Username",
        "email": "Email",
        "age": "Age",
    }
