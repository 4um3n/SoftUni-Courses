class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter:
    @staticmethod
    def format(book: Book) -> str:
        return book.content


class Printer:
    @staticmethod
    def get_book(content: str):
        return content


if __name__ == '__main__':
    b = Book("book content")
    f = Formatter()
    p = Printer()
    print(p.get_book(f.format(b)))
