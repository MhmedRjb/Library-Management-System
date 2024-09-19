import unittest
from datetime import datetime
from app.members import Member

class TestMember(unittest.TestCase):

    def setUp(self):
        self.member1 = Member(name="John Doe", email="john@doeexample.com", register_date="1-1-2000", role="admin")
        self.member2 = Member(name="Jane Doe", email="jane.doe@example.com", register_date="15-5-2010")
        self.member3 = Member(name="Alice Smith", email="alice.smith@example.com", register_date="")
        self.member4 = Member(name="Bob Johnson", email="bob.johnson@example.com", register_date="31-12-1999")

    def test_initialization(self):
        self.assertEqual(self.member1.name, "John Doe")
        self.assertEqual(self.member1.email, "john@doeexample.com")
        self.assertEqual(self.member1.role, "admin")
        self.assertEqual(self.member1.register_date, "01-01-2000")


    def test_name_property(self):
        self.member1.name = "John Smith"
        self.assertEqual(self.member1.name, "John Smith")
        with self.assertRaises(ValueError):
            self.member1.name = 123

    def test_email_property(self):
        self.member1.email = "john.smith@example.com"
        self.assertEqual(self.member1.email, "john.smith@example.com")
        with self.assertRaises(ValueError):
            self.member1.email = "invalid-email"


    def test_role_property(self):
        self.member1.role = "staff"
        self.assertEqual(self.member1.role, "staff")
        with self.assertRaises(ValueError):
            self.member1.role = "invalid-role"
    def test_to_dict(self):
        member_dict = self.member1.to_dict()
        expected_dict = {
            "name": "John Doe",
            "email": "john@doeexample.com",
            "role": "admin",
            "register_date": "01-01-2000"
        }
        print(member_dict)


if __name__ == '__main__':
    unittest.main()