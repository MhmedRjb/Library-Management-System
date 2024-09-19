import uuid
from app.validate import validate_str
from app.utils import to_dict
class Book:
    _id_counter = 1

    def __init__(self,title:str,author:str ,genre:str, id:int = None,status="available")->None:
        self._title = title
        self._author = author
        self._genre = genre
        self._id = Book._id_counter
        Book._id_counter += 1
        self._status = status
        self.validate_data(title, author, genre)

    def validate_data(self, title:str, author:str, genre:str)->bool:
        validate_str(self.title, self.author, self.genre)

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}, Status: {self.status}"
    @property
    def title(self)->str:
        return self._title
    @title.setter
    def title(self, value)->None:
        validate_str(value)
        self._title = value
    @property
    def id(self)->int:
        return self._id
    @property
    def author(self)->str:
        return self._author
    @author.setter
    def author(self, value)->None:
        validate_str(value)
        self._author = value

    @property
    def genre(self)->str:
        return self._genre

    @genre.setter
    def genre(self, value:str)->None:
        validate_str(value)
        self._genre = value

    @property
    def status(self)->str:
        return self._status
    @status.setter
    def status(self, value: str) -> None:
        validate_str(value)  # Optional: validate status if needed
        self._status = value




    def to_dict(self)->dict:
        return to_dict(self)

def main():
    book1 = Book("The Alchemist", "Paulo Coelho", "Adventure",status="available")
    book2 = Book("The Da Vinci Code", "Dan Brown", "Mystery",status="available")
    book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Classic",status="borrowed")
    book4 = Book("The Catcher in the Rye", "J.D. Salinger", "Fiction",status="borrowed")
    print(book1)
    print(book2)
    if book1.status != "available":
        print("The book is available")
    if book3.status == "borrowed":
        print("The book is borrowed")
    print(book3)
    print(book4)
    print(book1.to_dict())
    print(book2.to_dict())

if __name__ == '__main__':
    main()
