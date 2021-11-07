from project.library import Library
from unittest import TestCase, main


class LibraryTests(TestCase):
    def setUp(self) -> None:
        self.library = Library("library_name")

    def test_init_library(self):
        self.assertEqual("library_name", self.library.name)
        self.assertDictEqual({}, self.library.books_by_authors)
        self.assertDictEqual({}, self.library.readers)

    def test_name_property_setter_cannot_be_empty_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.library.name = ''

        self.assertEqual(f"Name cannot be empty string!", str(ex.exception))

    def test_name_property_setter_success(self):
        self.library.name = "new_name"
        self.assertEqual("new_name", self.library.name)

    def test_add_book(self):
        self.assertDictEqual({}, self.library.books_by_authors)
        self.library.add_book("author", "title")
        self.assertDictEqual({"author": ["title"]}, self.library.books_by_authors)
        self.library.add_book("author", "title1")
        self.assertDictEqual({"author": ["title", "title1"]}, self.library.books_by_authors)

    def test_add_reader(self):
        self.assertDictEqual({}, self.library.readers)
        result = self.library.add_reader("reader")
        self.assertDictEqual({"reader": []}, self.library.readers)
        self.assertIsNone(result)
        result = self.library.add_reader("reader")
        self.assertEqual(f"reader is already registered in the library_name library.", result)

    def test_rent_book(self):
        # Reader not in readers
        self.assertDictEqual({}, self.library.readers)
        result = self.library.rent_book("name", "author", "title")
        self.assertEqual(f"name is not registered in the library_name Library.", result)

        # Author not in authors
        self.library.readers = {"name": []}
        self.assertDictEqual({}, self.library.books_by_authors)
        result = self.library.rent_book("name", "author", "title")
        self.assertEqual(f"library_name Library does not have any author's books.", result)

        # Title not in author's titles
        self.library.books_by_authors = {"author": ["title"]}
        result = self.library.rent_book("name", "author", "title1")
        self.assertEqual(f"""library_name Library does not have author's "title1".""", result)

        # Success
        result = self.library.rent_book("name", "author", "title")
        self.assertIsNone(result)
        self.assertDictEqual({"author": []}, self.library.books_by_authors)
        self.assertDictEqual({"name": [{"author": "title"}]}, self.library.readers)


if __name__ == '__main__':
    main()
