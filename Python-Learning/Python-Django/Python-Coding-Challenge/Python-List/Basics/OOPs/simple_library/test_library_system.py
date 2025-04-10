# test_library_system.py
import pytest
from Basics.OOPs.simple_library.library_system import Book

def test_book_initial_status():
    book = Book("Test Book", "Test Author", "Test Genre")
    assert book.status == "Available"

def test_borrow_book():
    book = Book("Test Book", "Author", "Genre")
    book.borrow()
    assert book.status == "Borrowed"

def test_borrow_already_borrowed_book(capfd):
    book = Book("Test Book", "Author", "Genre")
    book.borrow()  # First borrow
    book.borrow()  # Second borrow should show warning

    captured = capfd.readouterr()
    assert "'Test Book' is already borrowed." in captured.out

def test_return_book():
    book = Book("Test Book", "Author", "Genre")
    book.borrow()
    book.return_book()
    assert book.status == "Available"
