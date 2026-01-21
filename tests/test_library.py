class TestSprint2(unittest.TestCase):

    def setUp(self):
        self.library = Library()
        self.library.add_book("B1", "Python", "Guido")

    def test_borrow_book(self):
        self.library.borrow_book("B1")
        self.assertEqual(self.library.books["B1"]["status"], "Borrowed")

    def test_borrow_unavailable(self):
        self.library.borrow_book("B1")
        with self.assertRaises(ValueError):
            self.library.borrow_book("B1")

    def test_return_book(self):
        self.library.borrow_book("B1")
        self.library.return_book("B1")
        self.assertEqual(self.library.books["B1"]["status"], "Available")

