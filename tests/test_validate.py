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
        self.assertTrue(validate.validate_data("string1", "string2"))
        self.assertTrue(validate.validate_data("hello", "world"))
        with self.assertRaises(ValueError):
            validate.validate_data("string1", 123)
        with self.assertRaises(ValueError):
            validate.validate_data(456, "string2")
        with self.assertRaises(ValueError):
            validate.validate_data(None, "string2")

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

if __name__ == '__main__':
    unittest.main()