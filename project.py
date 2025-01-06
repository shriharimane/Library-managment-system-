
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.checked_out = False

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            return True
        else:
            return False

    def check_in(self):
        if self.checked_out:
            self.checked_out = False
            return True
        else:
            return False


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def display_books(self):
        print("Library Catalog:")
        for idx, book in enumerate(self.books, start=1):
            print(f"{idx}. {book.title} by {book.author} {'(Checked Out)' if book.checked_out else ''}")

    def remove_book(self, title):
        for idx, book in enumerate(self.books):
            if book.title.lower() == title.lower():
                del self.books[idx]
                return True
        return False

    def get_checked_out_books(self):
        checked_out_books = []
        for book in self.books:
            if book.checked_out:
                checked_out_books.append(book)
        return checked_out_books


def main():
    library = Library()

    
    book1 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    print("Welcome to the Library Management System!")
    while True:
        print("\nMenu:")
        print("1. Display Books")
        print("2. Search Book")
        print("3. Check Out Book")
        print("4. Check In Book")
        print("5. Add Book")
        print("6. Remove Book")
        print("7. Display Checked Out Books")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            library.display_books()
        elif choice == '2':
            title = input("Enter the title of the book: ")
            book = library.search_book(title)
            if book:
                print(f"Book found: {book.title} by {book.author}")
            else:
                print("Book not found.")
        elif choice == '3':
            title = input("Enter the title of the book you want to check out: ")
            book = library.search_book(title)
            if book:
                if book.check_out():
                    print("Book checked out successfully.")
                else:
                    print("Book is already checked out.")
            else:
                print("Book not found.")
        elif choice == '4':
            title = input("Enter the title of the book you want to check in: ")
            book = library.search_book(title)
            if book:
                if book.check_in():
                    print("Book checked in successfully.")
                else:
                    print("Book is not checked out.")
            else:
                print("Book not found.")
        elif choice == '5':
            title = input("Enter the title of the book you want to add: ")
            author = input("Enter the author of the book: ")
            new_book = Book(title, author)
            library.add_book(new_book)
            print("Book added successfully.")
        elif choice == '6':
            title = input("Enter the title of the book you want to remove: ")
            if library.remove_book(title):
                print("Book removed successfully.")
            else:
                print("Book not found.")
        elif choice == '7':
            checked_out_books = library.get_checked_out_books()
            print("Checked Out Books:")
            for book in checked_out_books:
                print(f"{book.title} by {book.author}")
        elif choice == '8':
            print("Thank you for using the Library Management System!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

