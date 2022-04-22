from django import forms
from book_rendering_system.landing_page.models import BookModel


class BootstrapFormMixin:
    def _init_bootstrap(self):
        for field in self.fields.values():
            field.widget.attrs = {
                "class": "dorm-control",
            }


class BookForm(forms.ModelForm, BootstrapFormMixin):
    class Meta:
        model = BookModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()


