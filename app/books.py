import uuid
from app.validate import validate_str
from app.utils import to_dict
class Book:
    _id_counter = 1

    def __init__(self,title:str,author:str ,genre:str, id:int = None)->None:
        self._title = title
        self._author = author
        self._genre = genre
        self._id = Book._id_counter
        Book._id_counter += 1
        self.validate_data(title, author, genre)

    def validate_data(self, title:str, author:str, genre:str)->bool:
        validate_str(self.title, self.author, self.genre)

    def __str__(self)->str:
        return f"{self.title} by {self.author} is a {self.genre} book."

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

    def to_dict(self)->dict:
        return to_dict(self)

def main():
    book1 = Book("The Alchemist", "Paulo Coelho", "Adventure")
    book2 = Book("The Da Vinci Code", "Dan Brown", "Mystery")
    book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Classic")
    book4 = Book("The Catcher in the Rye", "J.D. Salinger", "Fiction")
    print(book1)
    print(book2)
    print(book3)
    print(book4)
    print(book1.to_dict())
    print(book2.to_dict())

if __name__ == '__main__':
    main()
