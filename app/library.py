from app.books import Book
import json
class Library:
    def __init__(self):
        self.books = []

    def __str__(self):
        return f"Library: {self.books}"

    def add_book(self, book):
        self.books.append(book)

    def get_books(self):
        return self.books

    def get_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                return True
        return False

    def update_book(self, title, author, genre):
        for book in self.books:
            if book.title == title:
                book.author = author
                book.genre = genre
                return True
        return False

    def save_books(self):
        with open("books.json", "w") as file:
            json.dump([book.to_dict() for book in self.books], file)

    def load_books(self):
        with open("books.json", "r") as file:
            books = json.load(file)
            self.books = [Book(book["title"], book["author"], book["genre"]) for book in books]

        return self.books

    def to_dict(self):
        return {
            "books": [book.to_dict() for book in self.books]
        }





