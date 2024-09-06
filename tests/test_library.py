# test_library.py
import unittest
from app.library import Library
from app.books import Book
from app.members import Member
import os
class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.library = Library()
        self.book1 = Book("The Alchemist", "Paulo Coelho", "Adventure")
        self.book2 = Book("The Da Vinci Code", "Dan Brown", "Mystery")
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        self.member1 = Member(name="John Doe", email="mww@gmail.con", register_date="1-1-2000", role="admin")
        self.member2 = Member(name="Jane Doe", email="mk@fm.com", register_date="15-5-2010")
        self.library.add_member(self.member1)
        self.library.add_member(self.member2)

    def tearDown(self):
        if os.path.exists("books.json"):
            os.remove("books.json")
            os.remove("members.json")

    def test_add_book(self):
        self.assertEqual(len(self.library.get_books()), 2)
        self.library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction"))
        self.assertEqual(len(self.library.get_books()), 3)
        print("test_add_book passed")

    def test_add_member(self):
        self.assertEqual(len(self.library.get_members()), 2)
        self.library.add_member(Member(name="Alice Smith", email="ALCI@GMAIL.COM", register_date="1-1-2000", role="admin"))
        self.assertEqual(len(self.library.get_members()), 3)
        print("test_add_member passed")

    def test_get_book(self):
        book = self.library.get_book("The Alchemist")
        self.assertIsNotNone(book)
        self.assertEqual(book.title, "The Alchemist")
        print("test_get_book passed")

    def test_get_member(self):
        member = self.library.get_member("John Doe")
        self.assertIsNotNone(member)
        self.assertEqual(member.name, "John Doe")
        print("test_get_member passed")

    def test_remove_book(self):
        self.assertTrue(self.library.remove_book("The Alchemist"))
        self.assertEqual(len(self.library.get_books()), 1)
        self.assertIsNone(self.library.get_book("The Alchemist"))
        print("test_remove_book passed")

    def test_remove_member(self):
        self.assertTrue(self.library.remove_member("John Doe"))
        self.assertEqual(len(self.library.get_members()), 1)
        self.assertIsNone(self.library.get_member("John Doe"))
        print("test_remove_member passed")


    def test_update_book(self):
        self.assertTrue(self.library.update_book("The Alchemist", "Paulo Coelho", "Philosophy"))
        book = self.library.get_book("The Alchemist")
        self.assertEqual(book.genre, "Philosophy")
        print("test_update_book passed")

    def test_update_member(self):
        self.assertTrue(self.library.update_member("John Doe", "sazxx@gmaol.cpm", "staff"))
        member = self.library.get_member("John Doe")
        self.assertEqual(member.email, "sazxx@gmaol.cpm")
        self.assertEqual(member.role, "staff")
        print("test_update_member passed")

    def test_save_and_load_books(self):
        self.library.save_all_data()
        self.library.books = []
        self.assertEqual(len(self.library.get_books()), 0)
        self.library.load_books()
        self.assertEqual(len(self.library.get_books()), 2)
        print("test_save_and_load_books passed")

    def test_save_and_load_members(self):
        self.library.save_all_data()
        self.library.members = []
        self.assertEqual(len(self.library.get_members()), 0)
        self.library.load_members()
        self.assertEqual(len(self.library.get_members()), 2)
        print("test_save_and_load_members passed")

    def test_json_functionality(self):
        self.library.save_all_data()
        self.library.books = []
        self.library.members = []
        self.library.load_books()
        self.library.load_members()
        self.assertEqual(len(self.library.get_books()), 2)
        self.assertEqual(len(self.library.get_members()), 2)
        book_titles = [book.title for book in self.library.get_books()]
        member_names = [member.name for member in self.library.get_members()]
        self.assertIn("John Doe", member_names)
        self.assertIn("Jane Doe", member_names)
        self.assertIn("The Alchemist", book_titles)
        self.assertIn("The Da Vinci Code", book_titles)
        print("test_json_functionality passed")




if __name__ == '__main__':
    unittest.main()