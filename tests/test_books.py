# test_books.py
import unittest
from app.books import Book

class TestBook(unittest.TestCase):

    def setUp(self):
        Book._id_counter = 1  # Reset the ID counter before each test
        self.book = Book("The Alchemist", "Paulo Coelho", "Adventure")

    def test_initialization(self):
        self.assertEqual(self.book.title, "The Alchemist")
        self.assertEqual(self.book.author, "Paulo Coelho")
        self.assertEqual(self.book.genre, "Adventure")
        print("test_initialization passed")

    def test_str_method(self):
        self.assertEqual(str(self.book), "The Alchemist by Paulo Coelho is a Adventure book.")
        print("test_str_method passed")

    def test_title_property(self):
        self.book.title = "The Da Vinci Code"
        self.assertEqual(self.book.title, "The Da Vinci Code")
        print("test_title_property passed")

    def test_author_property(self):
        self.book.author = "Dan Brown"
        self.assertEqual(self.book.author, "Dan Brown")
        print("test_author_property passed")

    def test_genre_property(self):
        self.book.genre = "Mystery"
        self.assertEqual(self.book.genre, "Mystery")
        print("test_genre_property passed")
    def test_to_dict(self):
        book_dict = self.book.to_dict()
        expected_dict = {
            "title": "The Alchemist",
            "author": "Paulo Coelho",
            "genre": "Adventure",
            "id": 1
        }
        self.assertEqual(book_dict, expected_dict)
        print("test_to_dict passed")

    def test_validate_data(self):
        self.assertIsNone(self.book.validate_data("The Alchemist", "Paulo Coelho", "Adventure"))
        self.assertFalse(self.book.validate_data(123, 123, 123))
        print("test_validate_data passed")

if __name__ == '__main__':
    unittest.main()