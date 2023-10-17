#!/usr/bin/python3
"""Unit tests for the Review class."""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for the Review class."""

    def setUp(self):
        """Set up any data or resources needed for the tests."""
        self.review = Review()

    def tearDown(self):
        """Clean up any resources after the tests are completed."""
        pass

    def test_review_instance(self):
        """Test that the review is an instance of the Review class."""
        self.assertIsInstance(self.review, Review)

    def test_review_text(self):
        """Test that the review has a text attribute."""
        self.assertTrue(hasattr(self.review, 'text'))

    def test_review_place_id(self):
        """Test that the review has a place_id attribute."""
        self.assertTrue(hasattr(self.review, 'place_id'))

    def test_review_user_id(self):
        """Test that the review has a user_id attribute."""
        self.assertTrue(hasattr(self.review, 'user_id'))


if __name__ == '__main__':
    unittest.main()
