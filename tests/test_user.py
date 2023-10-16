#!/usr/bin/python3
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        # Set up any data or resources needed for the tests
        self.user = User()

    def tearDown(self):
        # Clean up any resources after the tests are completed
        pass

    def test_user_instance(self):
        self.assertIsInstance(self.user, User)

    def test_user_attributes(self):
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))

    # Add more test cases as needed


if __name__ == '__main__':
    unittest.main()

