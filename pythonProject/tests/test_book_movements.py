import unittest
from app.book_movements import Book_movements
from app.validate import is_the_member_exist, is_the_book_exist, validate_staff_role, validate_date


class TestBookMovements(unittest.TestCase):

    def setUp(self):
        # Reset the transaction ID counter
        Book_movements._id_counter = 1

        global is_the_member_exist, is_the_book_exist, validate_staff_role, validate_date

        self.original_is_the_member_exist = is_the_member_exist
        self.original_is_the_book_exist = is_the_book_exist
        self.original_validate_staff_role = validate_staff_role
        self.original_validate_date = validate_date

        is_the_member_exist = lambda x: True
        is_the_book_exist = lambda x: True
        validate_staff_role = lambda x: True
        validate_date = lambda x: x

    def tearDown(self):
        # Restore the original methods
        global is_the_member_exist, is_the_book_exist, validate_staff_role, validate_date
        is_the_member_exist = self.original_is_the_member_exist
        is_the_book_exist = self.original_is_the_book_exist
        validate_staff_role = self.original_validate_staff_role
        validate_date = self.original_validate_date

    def test_initialization_default_dates(self):
        movement = Book_movements(book_title="The Alchemist", member_name="Jane Doe", staff_name="John Doe")
        self.assertEqual(movement.book_title, "The Alchemist")
        self.assertEqual(movement.member_name, "Jane Doe")
        self.assertEqual(movement.staff_name, "John Doe")
        self.assertIsNotNone(movement.issue_date)
        self.assertIsNotNone(movement.due_date)
        self.assertFalse(movement.in_library)
        self.assertEqual(movement.transaction_id, 1)
        print("test_initialization_default_dates passed")

    def test_initialization_custom_dates(self):
        movement = Book_movements(book_title="The Alchemist", member_name="Jane Doe", staff_name="John Doe",
                                  issue_date="01-01-2023", due_date="10-01-2023")
        self.assertEqual(movement.book_title, "The Alchemist")
        self.assertEqual(movement.member_name, "Jane Doe")
        self.assertEqual(movement.staff_name, "John Doe")
        self.assertEqual(movement.issue_date, "01-01-2023")
        self.assertEqual(movement.due_date, "10-01-2023")
        self.assertFalse(movement.in_library)
        self.assertEqual(movement.transaction_id, 1)
        print("test_initialization_custom_dates passed")

    def test_string_representation(self):
        movement = Book_movements(book_title="The Alchemist", member_name="Jane Doe", staff_name="John Doe",
                                  issue_date="01-01-2023", due_date="10-01-2023")
        self.assertEqual(str(movement), "The Alchemist was issued to Jane Doe on 01-01-2023 and is due on 10-01-2023")
        print("test_string_representation passed")

    def test_to_dict_method(self):
        movement = Book_movements(book_title="The Alchemist", member_name="Jane Doe", staff_name="John Doe",
                                  issue_date="01-01-2023", due_date="10-01-2023")
        movement_dict = movement.to_dict()
        self.assertEqual(movement_dict['book_title'], "The Alchemist")
        self.assertEqual(movement_dict['member_name'], "Jane Doe")
        self.assertEqual(movement_dict['staff_name'], "John Doe")
        self.assertEqual(movement_dict['issue_date'], "01-01-2023")
        self.assertEqual(movement_dict['due_date'], "10-01-2023")
        self.assertFalse(movement_dict['in_library'])
        self.assertEqual(movement_dict['transaction_id'], 1)
        print("test_to_dict_method passed")

    def test_invalid_date(self):
        global validate_date
        validate_date = lambda x: int(x)  # Mock to throw error for invalid date
        with self.assertRaises(ValueError):
            Book_movements(book_title="The Alchemist", member_name="John Doe", staff_name="Jane Doe",
                           issue_date="Invalid-Date")
        print("test_invalid_date passed")

    def test_invalid_book(self):
        global is_the_book_exist
        is_the_book_exist = lambda x: False  # Mock to return False for invalid book
        with self.assertRaises(ValueError):
            Book_movements(book_title="Invalid Book", member_name="John Doe", staff_name="Jane Doe")
        print("test_invalid_book passed")

    def test_invalid_member(self):
        global is_the_member_exist
        is_the_member_exist = lambda x: False  # Mock to return False for invalid member
        with self.assertRaises(ValueError):
            Book_movements(book_title="The Alchemist", member_name="Invalid Member", staff_name="Jane Doe")
        print("test_invalid_member passed")

    def test_invalid_staff(self):
        global validate_staff_role
        validate_staff_role = lambda x: False  # Mock to return False for invalid staff role
        with self.assertRaises(ValueError):
            Book_movements(book_title="The Alchemist", member_name="John Doe", staff_name="Invalid Staff")
        print("test_invalid_staff passed")


if __name__ == '__main__':
    unittest.main()