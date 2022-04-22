from django import forms

from recipes.common.mixins import DisableFormFieldsMixin
from recipes.common.models import Recipe


class RecipeForm(forms.ModelForm, DisableFormFieldsMixin):
    class Meta:
        model = Recipe
        fields = "__all__"

    def __init__(self, *args, disable_fields=False, **kwargs):
        super().__init__(*args, **kwargs)
        if disable_fields:
            self._disable_form_fields()

