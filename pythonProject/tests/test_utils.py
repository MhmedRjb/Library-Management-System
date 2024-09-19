import unittest
import json
import os
from app.utils import load_data
from app.books import Book
from app.members import Member

class TestLoadData(unittest.TestCase):

    def setUp(self):
        self.test_books_file = "test_books.json"
        self.test_members_file = "test_members.json"
        self.invalid_file = "invalid_file.json"
        self.invalid_json_file = "invalid_json_file.json"

        with open(self.test_books_file, "w") as file:
            json.dump([
                {"title": "The Alchemist", "author": "Paulo Coelho", "genre": "Adventure"},
                {"title": "1984", "author": "George Orwell", "genre": "Dystopian"}
            ], file)

        with open(self.test_members_file, "w") as file:
            json.dump([
                {"name": "John Doe", "email": "john@example.com", "role": "admin"},
                {"name": "Jane Doe", "email": "jane@example.com", "role": "staff"}
            ], file)

        with open(self.invalid_json_file, "w") as file:
            file.write("{invalid json}")

    def tearDown(self):
        os.remove(self.test_books_file)
        os.remove(self.test_members_file)
        os.remove(self.invalid_json_file)
        if os.path.exists(self.invalid_file):
            os.remove(self.invalid_file)

    def test_load_data_books_success(self):
        books = load_data(self.test_books_file, Book)
        self.assertEqual(len(books), 2)
        self.assertEqual(books[0].title, "The Alchemist")
        self.assertEqual(books[1].title, "1984")

    def test_load_data_members_success(self):
        members = load_data(self.test_members_file, Member)
        self.assertEqual(len(members), 2)
        self.assertEqual(members[0].name, "John Doe")
        self.assertEqual(members[1].name, "Jane Doe")

    def test_load_data_file_not_found(self):
        books = load_data(self.invalid_file, Book)
        self.assertEqual(books, [])
        members = load_data(self.invalid_file, Member)
        self.assertEqual(members, [])

    def test_load_data_invalid_json(self):
        books = load_data(self.invalid_json_file, Book)
        self.assertEqual(books, [])
        members = load_data(self.invalid_json_file, Member)
        self.assertEqual(members, [])

if __name__ == '__main__':
    unittest.main()