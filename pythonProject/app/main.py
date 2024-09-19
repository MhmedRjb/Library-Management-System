import json
from app.books import Book
from app.members import Member
from app.book_movements import Book_movements
from app.validate import validate_email, validate_str, validate_date, validate_role, is_the_member_exist, is_the_book_exist
from app.utils import to_dict, save_data, load_data
import datetime
class Library:
    def __init__(self):
        self.items = {
            'Book': [],
            'Member': [],
            'Book_movements': []
        }

    def __str__(self):
        return f"Library: {self.items}"

    def save_all_data(self):
        save_data("books.json", self.items['Book'])
        save_data("members.json", self.items['Member'])
        save_data("loans.json", self.items['Book_movements'])

    def add_item(self, item):
        item_type = type(item).__name__
        if item_type in self.items:
            self.items[item_type].append(item)
        else:
            raise ValueError(f"Item of type {item_type} is not supported")

    def get_items(self, item_type):
        return self.items.get(item_type, [])

    def get_item(self, item_type, identifier, identifier_key='title'):
        for item in self.items.get(item_type, []):
            if getattr(item, identifier_key) == identifier:
                return item
        return None

    def remove_item(self, item_type, identifier, identifier_key='title'):
        for item in self.items.get(item_type, []):
            if getattr(item, identifier_key) == identifier:
                self.items[item_type].remove(item)
                return True
        return False

    def update_item(self, item_type, identifier, updates, identifier_key='title'):
        for item in self.items.get(item_type, []):
            if getattr(item, identifier_key) == identifier:
                for key, value in updates.items():
                    setattr(item, key, value)
                return True
        return False

    def load_items(self, item_type, filename, item_class):
        self.items[item_type] = load_data(filename, item_class)
        return self.items[item_type]

    def add_member(self, name, email, role):
        self.add_item(Member(name, email, role))

    def borrow_book(self, book_title, member_name, staff_name, issue_date=None):
        validate_str(book_title, member_name, staff_name)
        is_the_book_exist(book_title)
        is_the_member_exist(member_name)

        book = self.get_item('Book', book_title)
        if book.status != "available":
            raise ValueError(f"The book '{book_title}' is currently not available for borrowing.")

        book.status = "borrowed"
        movement = Book_movements(book_title, member_name, staff_name, issue_date)
        self.add_item(movement)
        self.save_all_data()
        print(f"Book '{book_title}' borrowed by '{member_name}' with staff '{staff_name}' on '{movement.issue_date}'")


    def return_book(self, book_title):
        is_the_book_exist(book_title)
        print(f"Received input: '{book_title}' (Type: {type(book_title)})")  # Debugging output
        book = self.get_item('Book', book_title)
        print(book.status)
        print(book)
        print(f"Received input: '{book_title}' (Type: {type(book_title)})")  # Debugging output
        if book.status != "borrowed":
            raise ValueError(f"The book '{book_title}' is not currently borrowed.")

        #bring the movement book based on the book title and update the return date
        for movement in self.items['Book_movements']:
            if movement.book_title == book_title:
                movement.return_date = datetime.today().strftime('%d-%m-%Y')
                break
        print(f"Received input: '{book_title}' (Type: {type(book_title)})")  # Debugging output

        book.status = "available"
        self.save_all_data()
        print(f"Book '{book_title}' has been returned and is now available.")


def add_book(library):
    while True:
        try:
            while True:
                title = input("Enter book title: ")
                try:
                    validate_str(title)
                    break
                except ValueError as e:
                    print(e)
                    print("Please enter a valid title.")

            while True:
                author = input("Enter book author: ")
                try:
                    validate_str(author)
                    break
                except ValueError as e:
                    print(e)
                    print("Please enter a valid author.")

            while True:
                genre = input("Enter book genre: ")
                try:
                    validate_str(genre)
                    break
                except ValueError as e:
                    print(e)
                    print("Please enter a valid genre.")

            library.add_item(Book(title, author, genre))
            library.save_all_data()

            print(f"Book {title} added successfully")
            break
        except ValueError as e:
            print(e)
            print("Please try again.")



def list_books(library):
    for book in library.get_items('Book'):
        print(book)

def remove_book(library, title):
    validate_str(title)
    is_the_book_exist(title)
    library.remove_item('Book', title)
    library.save_all_data()


def add_member(library):
    while True:
        try:
            while True:
                name = input("Enter member name: ")
                try:
                    validate_str(name)
                    break
                except ValueError as e:
                    print(e)
                    print("Please enter a valid name.")

            while True:
                email = input("Enter member email: ")
                try:
                    validate_email(email)
                    break
                except ValueError as e:
                    print(e)
                    print("Please enter a valid email.")

            while True:
                role = input("Enter member role: ")
                try:
                    validate_role(role)
                    break
                except ValueError as e:
                    print(e)
                    print("Please enter a valid role.")

            while True:
                register_date = input("Enter member register date (dd-mm-yyyy) or leave blank for today: ")
                try:
                    validate_date(register_date)
                    break
                except ValueError as e:
                    print(e)
                    print("Please enter a valid date.")

            library.add_item(Member(name=name, email=email, role=role, register_date=register_date))
            library.save_all_data()

            print(f"Member {name} added successfully")
            break
        except ValueError as e:
            print(e)
            print("Please try again.")

def list_members(library):
    for member in library.get_items('Member'):
        print(member)

def remove_member(library, name):
    validate_str(name)
    is_the_member_exist(name)
    library.remove_item('Member', name, identifier_key='name')
    library.save_all_data()



def return_book(self, book_title):
    validate_str(book_title)
    is_the_book_exist(book_title)

    book = self.get_item('Book', book_title)
    if book.status != "borrowed":
        raise ValueError(f"The book '{book_title}' is not currently borrowed.")

    book.status = "available"
    self.save_all_data()
    print(f"Book '{book_title}' has been returned and is now available.")


def main_menu(library):
    while True:
        print("\nLibrary Management System")
        print("1. Add a new book")
        print("2. List all books")
        print("3. Remove a book")
        print("4. Add a new member")
        print("5. List all members")
        print("6. Remove a member")
        print("7. Borrow a book")
        print("8. Return a book")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_book(library)
        elif choice == '2':
            list_books(library)
        elif choice == '3':
            while True:
                try:
                    title = input("Enter book title to remove: ")
                    remove_book(library, title)
                    print(f"Book {title} removed successfully")
                    break
                except ValueError as e:
                    print(e)
                    print("Please try again.")
        elif choice == '4':
            add_member(library)

        elif choice == '5':
            list_members(library)
        elif choice == '6':
            while True:
                try:
                    name = input("Enter member name to remove: ")
                    remove_member(library, name)
                    print(f"Member {name} removed successfully")
                    break
                except ValueError as e:
                    print(e)
                    print("Please try again.")
        elif choice == '7':
            while True:
                try:
                    book_title = input("Enter book title: ")
                    member_name = input("Enter member name: ")
                    staff_name = input("Enter staff name: ")
                    issue_date = input("Enter issue date (dd-mm-yyyy) or leave blank for today: ")
                    library.borrow_book(book_title, member_name, staff_name, issue_date)
                    break
                except ValueError as e:
                    print(e)
                    print("Please try again.")
        elif choice == '8':
            while True:
                try:
                    book_title = input("Enter book title to return: ")
                    print(f"Received input: '{book_title}' (Type: {type(book_title)})")  # Debugging output
                    library.return_book(book_title)
                    break
                except ValueError as e:
                    print(e)
                    print("Please try again.")
        elif choice == '9':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
def main():
    library = Library()
    library.load_items('Book', "books.json", Book)
    library.load_items('Member', "members.json", Member)
    main_menu(library)

if __name__ == '__main__':
    main()