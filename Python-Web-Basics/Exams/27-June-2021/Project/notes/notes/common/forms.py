from django import forms
from notes.common.models import Profile, Note


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["title", "content", "image_url"]

    def __init__(self, *args, disable_fields=False, **kwargs):
        super().__init__(*args, **kwargs)
        if disable_fields:
            self.__disable_form_fields()

    def __disable_form_fields(self):
        for field in self.fields.values():
            field.disabled = True
