class TestSprint3(unittest.TestCase):

    def setUp(self):
        self.library = Library()
        self.library.add_book("B1", "Python", "Guido")

    def test_report_header(self):
        report = self.library.generate_report()
        self.assertIn("Book ID | Title | Author | Status", report)

    def test_report_contains_book(self):
        report = self.library.generate_report()
        self.assertIn("B1", report)

