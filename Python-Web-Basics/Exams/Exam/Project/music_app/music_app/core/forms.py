from django import forms
from music_app.core.mixins import SetFormFieldsPlaceholders, DisableFormFieldsMixin


class CustomModelForm(forms.ModelForm, DisableFormFieldsMixin, SetFormFieldsPlaceholders):
    placeholders = None

    def __init__(self, *args, disable_fields=False, **kwargs):
        super(CustomModelForm, self).__init__(*args, **kwargs)

        if disable_fields:
            self._disable_form_fields()

        if self.placeholders is not None:
            self._set_placeholders(**self.placeholders)
