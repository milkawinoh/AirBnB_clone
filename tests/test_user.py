#!/usr/bin/python3
import unittest
from models.user import User


"""Unit tests for the User class."""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    def setUp(self):
        """Set up any data or resources needed for the tests."""
        self.user = User()

    def tearDown(self):
        """Clean up any resources after the tests are completed."""
        pass

    def test_user_instance(self):
        """Test that the user is an instance of the User class."""
        self.assertIsInstance(self.user, User)

    def test_user_attributes(self):
        """Test that the user has all the required attributes."""
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))


if __name__ == '__main__':
    unittest.main()
