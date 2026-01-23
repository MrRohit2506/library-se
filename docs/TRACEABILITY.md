# Traceability Matrix

Traceability ensures that each user requirement is properly linked to its
implementation, testing, and release version.

| User Story | Sprint   | Feature Implemented                     | Function / Module | Test Case                         | Git Tag |
|------------|-----------|-----------------------------------------|-------------------|-----------------------------------|---------|
| US-1       | Sprint-1 | Add book to library                     | add_book()        | test_add_book_success             | v0.1    |
| US-1       | Sprint-1 | Prevent duplicate book ID               | add_book()        | test_duplicate_book               | v0.1    |
| US-2       | Sprint-2 | Borrow book                             | borrow_book()     | test_borrow_book                  | v0.2    |
| US-2       | Sprint-2 | Prevent borrowing unavailable book      | borrow_book()     | test_borrow_unavailable_book      | v0.2    |
| US-2       | Sprint-2 | Return book                             | return_book()     | test_return_book                  | v0.2    |
| US-3       | Sprint-3 | Generate library report                 | generate_report() | test_report_header                | v0.3    |
| US-3       | Sprint-3 | Validate report entries                 | generate_report() | test_report_has_book              | v0.3    |
