from django.urls import path

from django_rest.books_api.views import ListCreateBookView, DetailUpdateDeleteBookView

urlpatterns = [
    path("books/", ListCreateBookView.as_view()),
    path("books/<int:book_pk>", DetailUpdateDeleteBookView.as_view()),
]
