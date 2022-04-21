class Book:
    def __init__(self, title, author, location):
        self.title = title
        self.author = author
        self.location = location


class Library:
    def __init__(self) -> None:
        self.books = []

    def add_book(self, book: Book) -> None:
        if book.title not in [b.title for b in self.books]:
            self.books.append(book)

    def find_book(self, title: str) -> Book:
        for book in self.books:
            if book.title == title:
                return book


class BookReader:
    def __init__(self, book: Book) -> None:
        self.book = book
        self.page = 0

    def read(self) -> None:
        self.page += 1
