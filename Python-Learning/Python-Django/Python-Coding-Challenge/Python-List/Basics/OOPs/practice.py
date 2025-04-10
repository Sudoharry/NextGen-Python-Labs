""" 
    Book Library System:
    1) User can available the book
    2) Borrowed book will get return and update the status="Available"
    3) Logging module for debugging and error handling for better code simulations
    4) Display all the books
    5) Display all the genres available
"""
import logging

class Book:
    """ A class representing a book in the library."""
    def __init__(self,title,author, genre, status='Available'):
        self.title  = title
        self.author = author
        self.genre = genre
        self.status = status

    def display(self):
        """ Display collection of books in proper format"""
        print(f'Book:{self.title}, Author: {self.author}, Genre: {self.genre}, Status: {self.status}')

    def borrow_book(self):
        """ Borrow book based on the availabilty"""
        if self.status == 'Available':
            self.status == 'Borrowed'
            logging.info(f'{self.title} has been borrowed')
            print(f'You have borrowed {self.title}')
        else:
            logging.error('Attempting to get already borrowed book')
            print('Book is already borrowed')
    def return_book(self):
        """ Return books """
        

        
library = {
    1:Book("The Alchemist","Paulo Coelho","Fiction"),
    2:Book("Clean Code", "Robert C. Martin","Programming"),
    3:Book("1984","George Orwell","Dystopian"),
    4:Book("Atomic Habits","James Clear","Self-Help"),
    5:Book("Python Crash Course","Eric Matthes","Programming"),
}

# This will configure and set the logging for debugging based on the levels defined
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

# Library Catalog
def show_all_books():
    """List all books in the library."""
    print("\nLibrary Catalog:")
    for book_id, book  in library.items():
        print(f'ID: {book_id}', end= '-')
        book.display()

# Display Available Genres in the collections
genres = {book.genre for book in library.values()}
print('\nAvailable Genres:', genres)
