    def borrow_book(self, book_id):
        if book_id not in self.books:
            raise ValueError("Book not found")

        if self.books[book_id]["status"] == "Borrowed":
            raise ValueError("Book already borrowed")

        self.books[book_id]["status"] = "Borrowed"

    def return_book(self, book_id):
        if book_id not in self.books:
            raise ValueError("Book not found")

        self.books[book_id]["status"] = "Available"

