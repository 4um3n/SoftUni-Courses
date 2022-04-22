from django.shortcuts import render
from django.urls import reverse_lazy
from music_app.albums.models import Album
from music_app.albums.forms import AlbumForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


class ListAlbumsView(ListView):
    template_name = "albums/home-with-profile.html"
    model = Album


class AlbumDetailsView(DetailView):
    template_name = "albums/album-details.html"
    model = Album
    pk_url_kwarg = "album_pk"


class CreateAlbumView(CreateView):
    template_name = "albums/add-album.html"
    form_class = AlbumForm
    success_url = reverse_lazy("home")


class EditAlbumView(UpdateView):
    template_name = "albums/edit-album.html"
    model = Album
    form_class = AlbumForm
    pk_url_kwarg = "album_pk"
    success_url = reverse_lazy("home")


class DeleteAlbumView(DeleteView):
    template_name = "albums/delete-album.html"
    model = Album
    form_class = AlbumForm
    pk_url_kwarg = "album_pk"
    success_url = reverse_lazy("home")

    def get_form_kwargs(self):
        kwargs = super(DeleteAlbumView, self).get_form_kwargs()
        kwargs["disable_fields"] = True
        kwargs["initial"] = self.get_object().__dict__
        return kwargs

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return self.form_valid(self.get_form())
