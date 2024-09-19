# test_library.py
import unittest
from app.library import Library
from app.books import Book
from app.members import Member
from app.book_movements import Book_movements
import os
import json

class TestLibrary(unittest.TestCase):

    def setUp(self):
        # Create mock data for books.json
        self.mock_books = [
            {"title": "The Alchemist", "author": "Paulo Coelho", "genre": "Adventure"},
            {"title": "The Da Vinci Code", "author": "Dan Brown", "genre": "Mystery"}
        ]
        with open("books.json", "w") as file:
            json.dump(self.mock_books, file)

        # Create mock data for members.json
        self.mock_members = [
            {"name": "John Doe", "email": "mww@gmail.con", "register_date": "1-1-2000", "role": "admin"},
            {"name": "Jane Doe", "email": "mk@fm.com", "register_date": "15-5-2010", "role": "client"}
        ]
        with open("members.json", "w") as file:
            json.dump(self.mock_members, file)

        self.mock_movements = [
            {"book_title": "The Alchemist", "member_name": "John Doe", "issue_date": "01-01-2023", "due_date": "10-01-2023", "staff_name": "Alice Smith"},
            {"book_title": "The Da Vinci Code", "member_name": "Jane Doe", "issue_date": "02-01-2023", "due_date": "12-01-2023", "staff_name": "Bob Smith"}
        ]

        self.library = Library()
        self.book1 = Book("The Alchemist", "Paulo Coelho", "Adventure")
        self.book2 = Book("The Da Vinci Code", "Dan Brown", "Mystery")
        self.library.add_item(self.book1)
        self.library.add_item(self.book2)
        self.member1 = Member(name="John Doe", email="mww@gmail.con", register_date="1-1-2000", role="admin")
        self.member2 = Member(name="Jane Doe", email="mk@fm.com", register_date="15-5-2010")
        self.library.add_item(self.member1)
        self.library.add_item(self.member2)
        self.movement1 = Book_movements(book_title="The Alchemist", member_name="John Doe", issue_date="01-01-2023", due_date="10-01-2023", staff_name="Alice Smith")
        self.movement2 = Book_movements(book_title="The Da Vinci Code", member_name="Jane Doe", issue_date="02-01-2023", due_date="12-01-2023", staff_name="Bob Smith")
        self.library.add_item(self.movement1)
        self.library.add_item(self.movement2)

    # def tearDown(self):
    #     if os.path.exists("books.json"):
    #         os.remove("books.json")
    #     if os.path.exists("members.json"):
    #         os.remove("members.json")
    #     if os.path.exists("loans.json"):
    #         os.remove("loans.json")
    #

    def test_add_book(self):
        self.assertEqual(len(self.library.get_items('Book')), 2)
        self.library.add_item(Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction"))
        self.assertEqual(len(self.library.get_items('Book')), 3)
        print("test_add_book passed")

    def test_add_member(self):
        self.assertEqual(len(self.library.get_items('Member')), 2)
        self.library.add_item(Member(name="Alice Smith", email="ALCI@GMAIL.COM", register_date="1-1-2000", role="admin"))
        self.assertEqual(len(self.library.get_items('Member')), 3)
        print("test_add_member passed")

    def test_add_book_movement(self):
        self.assertEqual(len(self.library.get_items('Book_movements')), 2)
        self.library.add_item(Book_movements(book_title="The Alchemist", member_name="John Doe", issue_date="03-01-2023", due_date="13-01-2023", staff_name="Charlie Brown"))
        self.assertEqual(len(self.library.get_items('Book_movements')), 3)
        print("test_add_book_movement passed")

    def test_get_book(self):
        book = self.library.get_item('Book', "The Alchemist")
        self.assertIsNotNone(book)
        self.assertEqual(book.title, "The Alchemist")
        print("test_get_book passed")

    def test_get_member(self):
        member = self.library.get_item('Member', "John Doe", identifier_key='name')
        self.assertIsNotNone(member)
        self.assertEqual(member.name, "John Doe")
        print("test_get_member passed")

    def test_get_book_movement(self):
        movement = self.library.get_item('Book_movements', "The Alchemist", identifier_key='book_title')
        self.assertIsNotNone(movement)
        self.assertEqual(movement.book_title, "The Alchemist")
        print("test_get_book_movement passed")

    def test_remove_book(self):
        self.assertTrue(self.library.remove_item('Book', "The Alchemist"))
        self.assertEqual(len(self.library.get_items('Book')), 1)
        self.assertIsNone(self.library.get_item('Book', "The Alchemist"))
        print("test_remove_book passed")

    def test_remove_member(self):
        self.assertTrue(self.library.remove_item('Member', "John Doe", identifier_key='name'))
        self.assertEqual(len(self.library.get_items('Member')), 1)
        self.assertIsNone(self.library.get_item('Member', "John Doe", identifier_key='name'))
        print("test_remove_member passed")

    def test_remove_book_movement(self):
        self.assertTrue(self.library.remove_item('Book_movements', "The Alchemist", identifier_key='book_title'))
        self.assertEqual(len(self.library.get_items('Book_movements')), 1)
        self.assertIsNone(self.library.get_item('Book_movements', "The Alchemist", identifier_key='book_title'))
        print("test_remove_book_movement passed")

    def test_update_book(self):
        self.assertTrue(self.library.update_item('Book', "The Alchemist", {"author": "Paulo Coelho", "genre": "Philosophy"}))
        book = self.library.get_item('Book', "The Alchemist")
        self.assertEqual(book.genre, "Philosophy")
        print("test_update_book passed")

    def test_update_member(self):
        self.assertTrue(self.library.update_item('Member', "John Doe", {"email": "sazxx@gmaol.cpm", "role": "staff"}, identifier_key='name'))
        member = self.library.get_item('Member', "John Doe", identifier_key='name')
        self.assertEqual(member.email, "sazxx@gmaol.cpm")
        self.assertEqual(member.role, "staff")
        print("test_update_member passed")

    def test_update_book_movement(self):
        self.assertTrue(self.library.update_item('Book_movements', "The Alchemist", {"due_date": "15-01-2023"}, identifier_key='book_title'))
        movement = self.library.get_item('Book_movements', "The Alchemist", identifier_key='book_title')
        self.assertEqual(movement.due_date, "15-01-2023")
        print("test_update_book_movement passed")

    def test_save_and_load_books(self):
        self.library.save_all_data()
        self.library.items['Book'] = []
        self.assertEqual(len(self.library.get_items('Book')), 0)
        self.library.load_items('Book', "books.json", Book)
        self.assertEqual(len(self.library.get_items('Book')), 2)
        print("test_save_and_load_books passed")

    def test_save_and_load_members(self):
        self.library.save_all_data()
        self.library.items['Member'] = []
        self.assertEqual(len(self.library.get_items('Member')), 0)
        self.library.load_items('Member', "members.json", Member)
        self.assertEqual(len(self.library.get_items('Member')), 2)
        print("test_save_and_load_members passed")

    def test_save_and_load_book_movements(self):
        self.library.save_all_data()
        self.library.items['Book_movements'] = []
        self.assertEqual(len(self.library.get_items('Book_movements')), 0)
        self.library.load_items('Book_movements', "loans.json", Book_movements)
        self.assertEqual(len(self.library.get_items('Book_movements')), 2)
        print("test_save_and_load_book_movements passed")

    def test_json_functionality(self):
        self.library.save_all_data()
        self.library.items['Book'] = []
        self.library.items['Member'] = []
        self.library.items['Book_movements'] = []
        self.library.load_items('Book', "books.json", Book)
        self.library.load_items('Member', "members.json", Member)
        self.library.load_items('Book_movements', "loans.json", Book_movements)
        self.assertEqual(len(self.library.get_items('Book')), 2)
        self.assertEqual(len(self.library.get_items('Member')), 2)
        self.assertEqual(len(self.library.get_items('Book_movements')), 2)
        book_titles = [book.title for book in self.library.get_items('Book')]
        member_names = [member.name for member in self.library.get_items('Member')]
        movement_titles = [movement.book_title for movement in self.library.get_items('Book_movements')]
        self.assertIn("John Doe", member_names)
        self.assertIn("Jane Doe", member_names)
        self.assertIn("The Alchemist", book_titles)
        self.assertIn("The Da Vinci Code", book_titles)
        self.assertIn("The Alchemist", movement_titles)
        self.assertIn("The Da Vinci Code", movement_titles)
        print("test_json_functionality passed")

if __name__ == '__main__':
    unittest.main()