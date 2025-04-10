# library_system.py

import logging

# 1. Clean, Efficient, and Reusable Python Code
class Book:
    """A class representing a book in the library."""

    def __init__(self, title, author, genre, status='Available'):
        self.title = title
        self.author = author
        self.genre = genre
        self.status = status

    def display(self):
        """Print book details."""
        print(f'Title: {self.title}, Author: {self.author}, Genre: {self.genre}, Status: {self.status}')

    def borrow(self):
        """Update status to 'Borrowed' if book is available."""
        if self.status == 'Available':
            self.status = 'Borrowed'
            logging.info(f"'{self.title}' has been borrowed.")
            print(f"You have borrowed '{self.title}'.")
        else:
            logging.warning(f"Attempt to borrow already borrowed book: {self.title}")
            print(f"'{self.title}' is already borrowed.")

    def return_book(self):
        """Update status to 'Available' when returned."""
        self.status = 'Available'
        logging.info(f"'{self.title}' has been returned.")
        print(f"'{self.title}' has been returned.")


# 2. Collaboration Simulation (standard APIs)
# For now, we structure output and function names like real-world APIs
def show_all_books():
    """List all books in the library."""
    print("\n Library Catalog:")
    for book_id, book in library.items():
        print(f"ID: {book_id}", end=" - ")
        book.display()


# 3. Debugging and Troubleshooting with Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# 4. Staying Updated: Pythonic data handling (sets, dicts, comprehensions)
library = {
    1: Book("The Alchemist", "Paulo Coelho", "Fiction"),
    2: Book("Clean Code", "Robert C. Martin", "Programming"),
    3: Book("1984", "George Orwell", "Dystopian"),
    4: Book("Atomic Habits", "James Clear", "Self-Help"),
    5: Book("Python Crash Course", "Eric Matthes", "Programming")
}

# 5. Code Reviews and Feedback Simulation: Docstrings and modular functions

# 6. Documenting Code & Design Patterns
def borrow_book(book_id):
    """Borrow a book by its ID."""
    book = library.get(book_id)
    if book:
        book.borrow()
    else:
        logging.error(f"Book ID {book_id} not found.")
        print(" Book ID not found.")


def return_book(book_id):
    """Return a book by its ID."""
    book = library.get(book_id)
    if book:
        book.return_book()
    else:
        logging.error(f"Book ID {book_id} not found.")
        print(" Book ID not found.")


# 7. Refactoring for Performance: Using set comprehension
genres = {book.genre for book in library.values()}
print("\n📚 Available Genres:", genres)


# 8. Proficiency in Python — Core Structures: Classes, Dicts, Sets, Functions
if __name__ == "__main__":
    show_all_books()
    borrow_book(2)
    borrow_book(2)
    return_book(2)
    show_all_books()
