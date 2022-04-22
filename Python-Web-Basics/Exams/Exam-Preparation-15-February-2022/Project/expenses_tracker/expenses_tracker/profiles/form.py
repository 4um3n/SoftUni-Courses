from django import forms

from expenses_tracker.profiles.models import Profile


class ProfileForm(forms.ModelForm):
    profile_picture = forms.ImageField(
        required=False,
        widget=forms.FileInput(
            attrs={
                "class": "form-file",
            }
        )
    )

    class Meta:
        model = Profile
        fields = "__all__"
