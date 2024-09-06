# test_validate.py
import unittest
from app.validate import validate

class TestValidate(unittest.TestCase):
    def test_validate_email(self):
        self.assertTrue(validate.validate_email("test@example.com"))
        self.assertTrue(validate.validate_email("mhmed+ahmed+332+test@example.com"))
        self.assertTrue(validate.validate_email("user_name@example.co.uk"))
        with self.assertRaises(ValueError):
            validate.validate_email("invalid-email")
        with self.assertRaises(ValueError):
            validate.validate_email("user@.com")
        with self.assertRaises(ValueError):
            validate.validate_email("user@com")
        with self.assertRaises(ValueError):
            validate.validate_email("user.com")

    def test_validate_data(self):
        self.assertTrue(validate.validate_str("string1", "string2"))
        self.assertTrue(validate.validate_str("hello", "world"))
        with self.assertRaises(ValueError):
            validate.validate_str("string1", 123)
        with self.assertRaises(ValueError):
            validate.validate_str(456, "string2")
        with self.assertRaises(ValueError):
            validate.validate_str(None, "string2")

    def test_validate_date(self):
        self.assertEqual(validate.validate_date("05-10-2023"), "05-10-2023")
        self.assertEqual(validate.validate_date("31/12/1999"), "31-12-1999")
        self.assertEqual(validate.validate_date("1-1-2000"), "01-01-2000")
        self.assertEqual(validate.validate_date("1/1/2000"), "01-01-2000")
        with self.assertRaises(ValueError):
            validate.validate_date("1-1/20000")
        with self.assertRaises(ValueError):
            validate.validate_date("1/1-2000")
        with self.assertRaises(ValueError):
            validate.validate_date("001-1-200")
        with self.assertRaises(ValueError):
            validate.validate_date("01-001-2000")
        with self.assertRaises(ValueError):
            validate.validate_date("40-01-20000")
        with self.assertRaises(ValueError):
            validate.validate_date("01-13-2000")
    def test_is_the_book_exist(self):
        with open("books.json", "w") as file:
            file.write('''
            [
                {"title": "The Alchemist", "author": "Paulo Coelho", "genre": "Adventure"},
                {"title": "The Da Vinci Code", "author": "Dan Brown", "genre": "Mystery"}
            ]
            ''')
        self.assertTrue(validate.is_the_book_exist("The Alchemist"))
        with self.assertRaises(ValueError):
            validate.is_the_book_exist("The Great Gatsby")
        with self.assertRaises(ValueError):
            validate.is_the_book_exist(123)
    def test_is_the_member_exist(self):
        with open("members.json", "w") as file:
            file.write('''
            [
                {"name": "John Doe", "email": "mm@gmail.com", "register_date": "1-1-2000", "role": "admin"},
                {"name": "Jane Doe", "email": "kd@df.cxo", "register_date": "15-5-2010"}
            ]
            ''')
        self.assertTrue(validate.is_the_member_exist("John Doe"))
        with self.assertRaises(ValueError):
            validate.is_the_member_exist("Alice Smith")

        with self.assertRaises(ValueError):
            validate.is_the_member_exist(123)

    def test_validate_role(self):
        with  open("members.json", "w") as file:
            file.write('''
            [
                {"name": "John Doe", "email": "cd@fk.com", "register_date": "1-1-2000", "role": "staff"},
                {"name": "Jane Doe", "email": "dasd@ds.com", "register_date": "15-5-2010", "role": "client"}
            ]
            ''')
        self.assertTrue(validate.validate_staff_role("John Doe"))
        with self.assertRaises(ValueError):
            validate.validate_staff_role("Jane Doe")
if __name__ == '__main__':
    unittest.main()