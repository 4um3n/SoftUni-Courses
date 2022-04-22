from django import forms
from todo.todo_app.models import Todo


class TodoForm(forms.Form):
    title = forms.CharField(
        label='Title',
        max_length=10,
    )
    description = forms.CharField(
        widget=forms.Textarea(),
        max_length=100,
    )
