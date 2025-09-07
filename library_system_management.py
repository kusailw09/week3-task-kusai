import json
import os

FILE = "books.json"

class Book:
    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def to_dict(self):
        return {"title": self.title, "author": self.author,
                "isbn": self.isbn, "available": self.available}

class Library:
    def __init__(self):
        self.books = []
        self.load_books()

    def load_books(self):
        if os.path.exists(FILE):
            with open(FILE, "r") as f:
                self.books = [Book(**b) for b in json.load(f)]

    def save_books(self):
        with open(FILE, "w") as f:
            json.dump([b.to_dict() for b in self.books], f, indent=2)

    def add_book(self, title, author, isbn):
        self.books.append(Book(title, author, isbn))
        self.save_books()

    def borrow_book(self, isbn):
        for b in self.books:
            if b.isbn == isbn and b.available:
                b.available = False
                self.save_books()
                return f"You borrowed: {b.title}"
        return "Book not available"

    def return_book(self, isbn):
        for b in self.books:
            if b.isbn == isbn and not b.available:
                b.available = True
                self.save_books()
                return f"You returned: {b.title}"
        return "Invalid return"

    def list_books(self):
        return [f"{b.title} by {b.author} | {'Available' if b.available else 'Borrowed'}"
                for b in self.books]

# --- Example Usage ---
lib = Library()
lib.add_book("Harry Potter", "J.K. Rowling", "123")
lib.add_book("Rich Dad Poor Dad", "R. Kiyosaki", "456")

print(lib.list_books())
print(lib.borrow_book("123"))
print(lib.list_books())
print(lib.return_book("123"))
