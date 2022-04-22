from django import forms
from online_library.common.models import Profile, Book


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"

    def __init__(self, *args, disable_fields=False, **kwargs):
        super().__init__(*args, **kwargs)
        if disable_fields:
            self.__disable_fields()

    def __disable_fields(self):
        for field in self.fields.values():
            field.disabled = True


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            "title",
            "description",
            "image",
            "book_type"
        ]
