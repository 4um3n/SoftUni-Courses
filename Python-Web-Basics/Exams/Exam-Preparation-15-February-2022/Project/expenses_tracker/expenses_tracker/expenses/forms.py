from django import forms
from expenses_tracker.expenses.models import Expense


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        exclude = [
            "profile",
        ]

    def __init__(self, *args, disable_fields=False, **kwargs):
        super().__init__(*args, **kwargs)
        if disable_fields:
            self.__disable_fields()

    def __disable_fields(self):
        for field in self.fields.values():
            field.disabled = True
