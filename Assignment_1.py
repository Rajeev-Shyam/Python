# Student Number: 123117795

# Base class: Person
class Person:
    """
    Represents a person with name and contact information.
    This class is inherited by Member and Librarian.
    """
    def __init__(self, name, contact):
        self._name = name  # Name is protected
        self._contact = contact  # Contact information is protected

    def get_name(self):
        """Returns the person's name."""
        return self._name

    def get_contact(self):
        """Returns the person's contact information."""
        return self._contact


# Inherited class: Member
class Member(Person):
    """
    Represents a library member who can borrow books.
    Inherits from the Person class.
    """
    def __init__(self, name, contact, member_id):
        super().__init__(name, contact)
        self.__member_id = member_id  # Member ID is private
        self.__borrowed_books = []  # List to store borrowed books

    def borrow_book(self, book):
        """Adds a book to the member's borrowed books list."""
        if isinstance(book, Book):
            if not book.is_borrowed:
                self.__borrowed_books.append(book)
                book.mark_borrowed()
            else:
                raise ValueError("Book is already borrowed")
        else:
            raise ValueError("Invalid book")

    def return_book(self, book):
        """Removes a book from the member's borrowed books list."""
        if book in self.__borrowed_books:
            self.__borrowed_books.remove(book)
            book.mark_returned()
        else:
            raise ValueError("Book not found in borrowed list")

    def get_borrowed_books(self):
        """Returns a list of the member's borrowed books."""
        return [book.get_title() for book in self.__borrowed_books]


# Inherited class: Librarian
class Librarian(Person):
    """
    Represents a librarian responsible for managing the library's operations.
    Inherits from the Person class.
    """
    def __init__(self, name, contact, employee_id):
        super().__init__(name, contact)
        self.__employee_id = employee_id  # Employee ID is private

    def issue_book(self, member, book):
        """Issues a book to a library member."""
        try:
            member.borrow_book(book)
        except ValueError as e:
            print(f"Error: {e}")

    def accept_return(self, member, book):
        """Accepts a returned book from a library member."""
        try:
            member.return_book(book)
        except ValueError as e:
            print(f"Error: {e}")


# Aggregated class: Book
class Book:
    """
    Represents a book in the library.
    """
    def __init__(self, title, author):
        self.__title = title  # Title is private
        self.__author = author  # Author is private
        self.__is_borrowed = False  # Indicates whether the book is borrowed or not

    @property
    def is_borrowed(self):
        """Returns whether the book is borrowed or not."""
        return self.__is_borrowed

    def mark_borrowed(self):
        """Marks the book as borrowed."""
        self.__is_borrowed = True

    def mark_returned(self):
        """Marks the book as returned."""
        self.__is_borrowed = False

    def get_title(self):
        """Returns the title of the book."""
        return self.__title


# Aggregated class: Library
class Library:
    """
    Represents a library that contains books, members, and librarians.
    """
    def __init__(self, library_name):
        self.__library_name = library_name  # Library name is private
        self.__books = []  # List of books (aggregation)
        self.__members = []  # List of members (aggregation)
        self.__librarians = []  # List of librarians (aggregation)

    def add_book(self, book):
        """Adds a book to the library's collection."""
        if isinstance(book, Book):
            self.__books.append(book)
        else:
            raise ValueError("Invalid book")

    def add_member(self, member):
        """Registers a new library member."""
        if isinstance(member, Member):
            self.__members.append(member)
        else:
            raise ValueError("Invalid member")

    def add_librarian(self, librarian):
        """Adds a librarian to the library staff."""
        if isinstance(librarian, Librarian):
            self.__librarians.append(librarian)
        else:
            raise ValueError("Invalid librarian")

    def get_library_summary(self):
        """Returns a summary of the library's current status."""
        return {
            "library_name": self.__library_name,
            "books_count": len(self.__books),
            "members_count": len(self.__members),
            "librarians_count": len(self.__librarians)
        }
