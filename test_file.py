# Student Number: 123117795

# Import necessary classes from Assignment_1
from Assignment_1 import Member, Librarian, Book, Library

def test_library_system():
    """Function to test the library management system."""
    try:
        # Create members
        member1 = Member("John Doe", "123-456-7890", "M001")
        member2 = Member("Jane Smith", "987-654-3210", "M002")

        # Create a librarian
        librarian = Librarian("Alice Johnson", "555-123-4567", "L001")

        # Create books
        book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
        book2 = Book("1984", "George Orwell")

        # Create a library
        library = Library("City Library")

        # Add books, members, and librarian to the library
        library.add_book(book1)
        library.add_book(book2)

        library.add_member(member1)
        library.add_member(member2)

        library.add_librarian(librarian)

        # Librarian issues books to members
        librarian.issue_book(member1, book1)
        librarian.issue_book(member2, book2)

        # Print borrowed books for each member
        print(f"{member1.get_name()} borrowed: {member1.get_borrowed_books()}")
        print(f"{member2.get_name()} borrowed: {member2.get_borrowed_books()}")

        # Librarian accepts returned books
        librarian.accept_return(member1, book1)
        librarian.accept_return(member2, book2)

        # Print library summary
        summary = library.get_library_summary()
        print("Library Summary:", summary)

    except ValueError as e:
        print("Error:", e)

# Run the test function
test_library_system()
