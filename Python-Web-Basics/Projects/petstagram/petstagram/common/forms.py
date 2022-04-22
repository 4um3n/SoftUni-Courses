from django import forms
from petstagram.common.models import Comment


class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control rounded-2'
            }
        )
    )

    class Meta:
        model = Comment
        fields = ('comment',)
