# Task 5 - Library Management System


# Book class
class Book:

    # Constructor
    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.status = "Available"

    # Method to display book information
    def display_book(self):
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Status:", self.status)

    # Method to issue a book
    def issue_book(self):
        if self.status == "Issued":
            print("Book is already issued.")
        else:
            self.status = "Issued"
            print("Book issued successfully.")


# List to store books
books = []


# Function to add a book
def add_book():

    title = input("Enter book title: ")
    author = input("Enter author name: ")
    book_id = input("Enter book ID: ")

    # Create book object
    book = Book(title, author, book_id)

    # Add book to the list
    books.append(book)

    print("Book added successfully.")


# Function to view all books
def view_books():

    if len(books) == 0:
        print("No books available.")

    else:
        for book in books:
            book.display_book()


# Function to search a book
def search_book():

    search = input("Enter Book ID or Title: ")

    found = False

    for book in books:

        if book.book_id == search or book.title.lower() == search.lower():
            book.display_book()
            found = True

    if found == False:
        print("Book not found.")


# Function to issue a book
def issue_book():

    book_id = input("Enter Book ID to issue: ")

    found = False

    for book in books:

        if book.book_id == book_id:
            book.issue_book()
            found = True

    if found == False:
        print("Book not found.")


# Function to delete a book
def delete_book():

    book_id = input("Enter Book ID to delete: ")

    found = False

    for book in books:

        if book.book_id == book_id:
            books.remove(book)
            print("Book deleted successfully.")
            found = True
            break

    if found == False:
        print("Book not found.")


# Main menu
while True:

    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Delete Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
        input("\nPress Enter to continue...")

    elif choice == "2":
        view_books()
        input("\nPress Enter to continue...")

    elif choice == "3":
        search_book()
        input("\nPress Enter to continue...")

    elif choice == "4":
        issue_book()
        input("\nPress Enter to continue...")

    elif choice == "5":
        delete_book()
        input("\nPress Enter to continue...")

    elif choice == "6":
        print("Program ended.")
        break

    else:
        print("Invalid choice. Please try again.")
        input("\nPress Enter to continue...")