    def generate_report(self):
        report = "Book ID | Title | Author | Status\n"
        for book_id, details in self.books.items():
            report += f"{book_id} | {details['title']} | {details['author']} | {details['status']}\n"
        return report

