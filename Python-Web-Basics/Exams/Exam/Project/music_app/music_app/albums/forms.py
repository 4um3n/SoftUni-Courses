from music_app.core import forms
from music_app.albums.models import Album


class AlbumForm(forms.CustomModelForm):
    class Meta:
        model = Album
        exclude = [
            "profile",
        ]

    placeholders = {
        "album_name": "Album Name",
        "artist": "Artist",
        "description": "Description",
        "image_url": "Image URL",
        "price": "Price",
    }
