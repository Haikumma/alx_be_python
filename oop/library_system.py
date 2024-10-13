# Base class
class Book:
    def __init__(self, title, author):
        """Initialize the common attributes for all types of books."""
        self.title = title
        self.author = author

    def __str__(self):
        """String representation for Book."""
        return f"Book: {self.title} by {self.author}"


# Derived class for EBooks
class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize EBook specific attributes and call the parent constructor."""
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """String representation for EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


# Derived class for PrintBooks
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize PrintBook specific attributes and call the parent constructor."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """String representation for PrintBook."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


# Library class using composition
class Library:
    def __init__(self):
        """Initialize an empty list to store books."""
        self.books = []

    def add_book(self, book):
        """Add a book (Book, EBook, or PrintBook) to the library."""
        self.books.append(book)

    def list_books(self):
        """Print details of all books in the library."""
        for book in self.books:
            print(book)
