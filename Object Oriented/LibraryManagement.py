# Encapsulation: We define classes with specific attributes and methods to control access.
class Book:
    def __init__(self, title, author, isbn):
        # private attributed to prevent direct access
        self._title = title
        self._author = author
        self._isbn = isbn
        # A flag to indicate if the book is checked out or not
        self._is_checked_out = False 


    # Writing a public method to get book details (encapsulation)
    def get_details(self):
        return f"Title: {self._title}, Author: {self._author}, ISBN: {self._isbn}"
    
    
    # Method to check out the book (encapsulation)
    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            print(f"{self._title} has been checked out")
        else:
            print(f"{self._title} is already checked out")

    # Method to return the book

    def return_book(self):
        if not self._is_checked_out:
            print(f"This book has not been checked out, you cannot return this")
            return
        
        self._is_checked_out = False
        print(f"Thank you for returning this book")


# Inheritance: We can create a subclass for specialized users, like Staff or Patron

class User:
    def __init__(self, name) -> None:
        self.name = name
        self.borrowed_books = []

    def borrow_books(self, book):
        if len(self.borrowed_books) > 5:
            print(" You cannot borrow more than 5 books")
            print("Current status of your borrows:")
            for books in self.borrowed_books:
                print(books.get_details())
        else:
            book.check_out()
            library.remove_book(book)
            self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            library.add_book(book)
        else:
            print("You haven't borrowed this book")

# Patron class (inherits User): A regular user who borrows books
class Patron(User):
    pass  # Patron inherits all behavior of User with no additional modifications

# Staff class (inherits User) can Perform some extra actions. 
class Staff(User):
    # only a staff can add or remove book from library catelouge
    def add_book(self, library, book):
        library.add_book(book)
        print(f"{self.name} has added {book.get_details()} to the library")

    def remove_book(self, library, book):
        if book in library.collection:
            library.remove_book(book)
            print(f"{self.name} has removed the book: {book.get_details()}")

    
#Polymorphism: Differenct classes (patron and staff) can interact with same methods in a unified way

class Library:
    def __init__(self) -> None:
        self.collections = []

    
    # adding a book to library
    def add_book(self, book):
        self.collections.append(book)
    
    def remove_book(self, book):
        if book in self.collections:
            self.collections.remove(book)
        else:
            print("The book requested could not be found in the lib collection")

    
    def show_books(self):
        print("The available books in the library are")
        for book in self.collections:
            print(book.get_details())
                  

library = Library()

book1 = Book("1984", "George Orwell", "11252124")
book2 = Book("Asura", "Anand Neelakanthan","23523541")
book3 = Book("Short Stories by Alexander Pushkin", "Alexander Pushkin","123125")


library.add_book(book1)
library.add_book(book2)


staff = Staff("Margarette")
customer1 = Patron("Jenkins")

staff.add_book(library, book3)


library.show_books()

customer1.borrow_books(book1)

library.show_books()

customer1.return_book(book1)

library.show_books()