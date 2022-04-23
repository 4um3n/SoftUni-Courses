from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django_rest.books_api.models import Book
from django_rest.books_api.serializers import BookSerializer


class ListCreateBookView(APIView):
    def get(self, request, *args, **kwargs):
        books = Book.objects.all()
        book_serializer = BookSerializer(books, many=True)
        return Response({"books": book_serializer.data})

    def post(self, request, *args, **kwargs):
        book_serializer = BookSerializer(data=request.data)
        if book_serializer.is_valid():
            book_serializer.save()
            return Response(book_serializer.data, status=status.HTTP_201_CREATED)
        return Response(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailUpdateDeleteBookView(APIView):
    def get(self, request, book_pk, *args, **kwargs):
        book = Book.objects.get(pk=book_pk)
        book_serializer = BookSerializer(book)
        return Response({"book": book_serializer.data})

    def put(self, request, book_pk, *args, **kwargs):
        book = Book.objects.get(pk=book_pk)
        book_serializer = BookSerializer(instance=book, data=request.data)
        if book_serializer.is_valid():
            book_serializer.save()
            return Response(book_serializer.data, status=status.HTTP_201_CREATED)
        return Response(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, book_pk, *args, **kwargs):
        book = Book.objects.get(pk=book_pk)
        book.delete()
        return Response(status=status.HTTP_200_OK)
