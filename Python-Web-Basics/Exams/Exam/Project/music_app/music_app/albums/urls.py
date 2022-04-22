from django.urls import path
from music_app.albums.views import ListAlbumsView, AlbumDetailsView, CreateAlbumView, EditAlbumView, DeleteAlbumView

urlpatterns = [
    path("list/", ListAlbumsView.as_view(), name="list albums"),
    path("add/", CreateAlbumView.as_view(), name="create album"),
    path("edit/<int:album_pk>", EditAlbumView.as_view(), name="edit album"),
    path("delete/<int:album_pk>", DeleteAlbumView.as_view(), name="delete album"),
    path("details/<int:album_pk>", AlbumDetailsView.as_view(), name="album details"),
]
