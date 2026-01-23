# User Stories

This document describes the user requirements captured in the form of user stories.
Each user story is implemented in a specific sprint and verified through unit testing.

---

## US-1: Book Registration

**As a librarian**,  
I want to add books with unique book ID, title, and author,  
so that the library catalog can be maintained accurately.

**Acceptance Criteria:**
- Book ID must be unique
- Book details must be stored correctly
- Duplicate book IDs must not be allowed

**Sprint:** Sprint-1  
**Release Tag:** v0.1

---

## US-2: Borrow and Return Books

**As a library user**,  
I want to borrow and return books,  
so that book circulation can be managed efficiently.

**Acceptance Criteria:**
- Only available books can be borrowed
- Borrowed books cannot be borrowed again
- Returned books become available again

**Sprint:** Sprint-2  
**Release Tag:** v0.2

---

## US-3: Library Report Generation

**As a librarian**,  
I want to generate a library report,  
so that I can view the current status of all books.

**Acceptance Criteria:**
- Report should list all books
- Book availability status should be shown
- Report format should be readable

**Sprint:** Sprint-3  
**Release Tag:** v0.3
