#!/usr/bin/python3
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    def setUp(self):
        # Set up any data or resources needed for the tests
        self.review = Review()

    def tearDown(self):
        # Clean up any resources after the tests are completed
        pass

    def test_review_instance(self):
        self.assertIsInstance(self.review, Review)

    def test_review_text(self):
        self.assertTrue(hasattr(self.review, 'text'))

    def test_review_place_id(self):
        self.assertTrue(hasattr(self.review, 'place_id'))

    def test_review_user_id(self):
        self.assertTrue(hasattr(self.review, 'user_id'))

    # Add more test cases as needed


if __name__ == '__main__':
    unittest.main()

