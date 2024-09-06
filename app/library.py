from app.books import Book
from app.members import Member
from app.validate import validate_str
import json
from app.utils import  to_dict, save_data ,load_data
class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def __str__(self):
        return f"Library: {self.books}"

    def save_all_data(self):
        save_data("books.json", self.books)
        save_data("members.json", self.members)

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)


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



    def load_books(self):
        self.books = load_data("books.json", Book)
        return self.books


    def add_member(self, member):
        self.members.append(member)
    def get_members(self):
        return self.members

    def get_member(self, name):
        for member in self.members:
            if member.name == name:
                return member
        return None
    def remove_member(self, name):
        for member in self.members:
            if member.name == name:
                self.members.remove(member)
                return True
        return False


    def update_member(self, name, email, role):
        for member in self.members:
            if member.name == name:
                member.email = email
                member.role = role
                return True
        return False

    def load_members(self):
        self.members = load_data("members.json", Member)
        return self.members




def main():
    # Create a library
    library = Library()
    # Add some books to the library
    library.add_book(Book("The Alchemist", "Paulo Coelho", "Adventure"))
    library.add_book(Book("The Da Vinci Code", "Dan Brown", "Mystery"))
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction"))
    library.add_book(Book("The Catcher in the Rye", "J.D. Salinger", "Fiction"))
    # Save the books to a JSON file
    library.save_all_data()
    # Load the books from the JSON file
    library.load_books()
    # Print the books in the library
    for book in library.get_books():
        print(book)
        print(book.to_dict())

    # Remove a book from the library
    library.remove_book("The Great Gatsby")
    # Update a book in the library
    library.update_book("The Da Vinci Code", "Dan Brown", "Thriller")
    # Print the books in the library
    for book in library.get_books():
        print(book)
        print(book.to_dict())

    # Add some members to the library
    library.add_member(Member(name="John Doe", email="m222erfa@gmail.com", role="admin"))
    library.add_member(Member(name="Jane Doe", email="nds@gr.xoj", role="staff"))
    for m in library.members:
        print(m)
    # Save the members to a JSON file
    library.save_all_data()
    # Load the members from the JSON file
    library.load_members()
if __name__ == '__main__':
    main()






