import unittest
from src.library import Library

class TestLibrarySprint1(unittest.TestCase):

    def setUp(self):
        self.library = Library()

    def test_add_book_success(self):
        self.library.add_book("B1", "Python", "Guido")
        self.assertIn("B1", self.library.books)

    def test_duplicate_book_addition(self):
        self.library.add_book("B1", "Python", "Guido")
        with self.assertRaises(ValueError):
            self.library.add_book("B1", "Python Advanced", "Guido")

if __name__ == "__main__":
    unittest.main()

