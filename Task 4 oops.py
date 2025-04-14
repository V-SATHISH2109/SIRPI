"""
LIBRARY MANAGEMENT SYSTEM - FULL EXPLANATION

1. ABSTRACT BOOK CLASS (BASE FOR ALL BOOKS)
-----------------------------------------"""
from abc import ABC, abstractmethod

class Book(ABC):
    def __init__(self, title, author, isbn):
        # Stores basic book information
        self.title = title  # Book title (string)
        self.author = author  # Author name (string)
        self.isbn = isbn  # Unique ID (string)
    
    def __repr__(self):
        # Shows book details instead of memory address
        return f"Book(title='{self.title}', author='{self.author}')"
    
    @abstractmethod
    def check_availability(self):
        # Must be implemented by child classes
        pass
    
    @abstractmethod
    def borrow(self):
        # Must be implemented by child classes
        pass

"""2. PHYSICAL BOOK (MANAGES COPIES)
----------------------------------"""
class PhysicalBook(Book):
    def __init__(self, title, author, isbn, copies):
        super().__init__(title, author, isbn)
        self.__copies = copies  # Private copies count
    
    def check_availability(self):
        return self.__copies > 0  # True if available
    
    def borrow(self):
        if self.check_availability():
            self.__copies -= 1  # Reduce stock
            return True
        return False
    
    def return_book(self):
        self.__copies += 1  # Restore stock
    
    def get_copies(self):
        return self.__copies  # Getter for copies

"""3. E-BOOK (UNLIMITED ACCESS)
---------------------------"""
class EBook(Book):
    def check_availability(self):
        return True  # Always available
    
    def borrow(self):
        return True  # No copy management needed

"""4. USER SYSTEM (CORE FUNCTIONALITY)
-----------------------------------"""
class User(ABC):
    def __init__(self, name):
        self.name = name  # User's name
        self.borrowed_books = []  # List of borrowed books
    
    @abstractmethod
    def get_borrowing_limit(self):
        # Must be defined in child classes
        pass
    
    def borrow_book(self, book):
        # Checks borrowing limit and book availability
        if len(self.borrowed_books) < self.get_borrowing_limit():
            if book.borrow():  # Calls book-specific borrow
                self.borrowed_books.append(book)
                print(f"{self.name} borrowed {book.title}")
                return True
        print(f"{self.name} cannot borrow {book.title}")
        return False
    
    def return_book(self, book):
        # Returns book and updates physical copies
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            if isinstance(book, PhysicalBook):
                book.return_book()
            print(f"{self.name} returned {book.title}")

"""5. USER TYPES (DIFFERENT PRIVILEGES)
----------------------------------"""
class Student(User):
    def get_borrowing_limit(self):
        return 3  # Student limit: 3 books

class Professor(User):
    def get_borrowing_limit(self):
        return 5  # Professor limit: 5 books

"""6. LIBRARIAN (SPECIAL USER)
-------------------------"""
class Librarian(User):
    def get_borrowing_limit(self):
        return 0  # Cannot borrow books
    
    def add_book(self, catalog, book):
        # Special method to add books to catalog
        catalog.add_book(book)
        print(f"Added {book.title} to catalog")

"""7. BOOK CATALOG (SEARCH SYSTEM)
------------------------------"""
class BookCatalog:
    def __init__(self):
        self.books = []  # Stores all books
    
    def add_book(self, book):
        self.books.append(book)  # Add new book
    
    def search_by_title(self, title):
        # Case-insensitive title search
        return [b for b in self.books if b.title.lower() == title.lower()]
    
    def search_by_author(self, author):
        # Case-insensitive author search
        return [b for b in self.books if b.author.lower() == author.lower()]

"""8. TESTING THE SYSTEM (DEMO)
--------------------------"""
if __name__ == "__main__":
    # Create book instances
    book1 = PhysicalBook("The Great Gatsby", "F. Scott Fitzgerald", "123456", 5)
    book2 = EBook("Clean Code", "Robert Martin", "789012")
    
    # Create user instances
    student = Student("Alice")  # Can borrow 3 books
    professor = Professor("Bob")  # Can borrow 5 books
    librarian = Librarian("Carol")  # Manages catalog
    
    # Initialize empty catalog
    catalog = BookCatalog()
    
    # Librarian adds books to system
    librarian.add_book(catalog, book1)
    librarian.add_book(catalog, book2)
    
    # Borrow books (demonstrates limits)
    student.borrow_book(book1)  # Alice borrows physical book
    professor.borrow_book(book2)  # Bob borrows ebook
    
    # Search functionality test
    print("Search results:", catalog.search_by_title("Clean Code"))  # Returns ebook
    
    # Return book demonstration
    student.return_book(book1)  # Restores physical copy count
"""
HOW TO USE:
1. Run the code to see borrowing/returning in action
2. Test search functionality with different titles/authors
3. Try exceeding borrowing limits to see restrictions
4. Add new book types/user roles as needed
"""