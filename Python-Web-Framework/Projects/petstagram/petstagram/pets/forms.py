from django import forms
from petstagram.pets.models import Pet, Comment


class CreatePetForm(forms.ModelForm):
    CHOICE_TYPE_DOG = 'dog'
    CHOICE_TYPE_CAT = 'cat'
    CHOICE_TYPE_PARROT = 'parrot'
    TYPE_CHOICES = (
        (CHOICE_TYPE_DOG, 'Dog'),
        (CHOICE_TYPE_CAT, 'Cat'),
        (CHOICE_TYPE_PARROT, 'Parrot'),
    )

    type = forms.ChoiceField(
        choices=TYPE_CHOICES,
        required=True,
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            },

        ))
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        ))
    age = forms.IntegerField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'number'
            }
        ))
    image_url = forms.ImageField(
        required=True,
        widget=forms.FileInput(
            attrs={
                'class': 'form-control'
            }
        ))
    description = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'form-control rounded-2'
        }))

    class Meta:
        model = Pet
        fields = ('type', 'name', 'age', 'description', 'image_url')


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
