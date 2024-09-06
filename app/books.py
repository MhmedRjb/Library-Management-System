import uuid
class Book:
    _id_counter = 1

    def __init__(self,title:str,author:str ,genre:str):
        self._title = title
        self._author = author
        self._genre = genre
        self._id = Book._id_counter
        Book._id_counter += 1

    def validate_data(self, title:str, author:str, genre:str)->bool:
        if not isinstance(title, str) or not isinstance(author, str) or not isinstance(genre, str):
            return False

    def __str__(self)->str:
        return f"{self.title} by {self.author} is a {self.genre} book."

    @property
    def title(self)->str:
        return self._title
    @title.setter
    def title(self, value)->None:
        self._title = value

    @property
    def author(self)->str:
        return self._author
    @author.setter
    def author(self, value)->None:
        self._author = value

    @property
    def genre(self)->str:
        return self._genre
    @genre.setter
    def genre(self, value:str)->None:
        self._genre = value

    def to_dict(self)->dict:
        return {
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            "id": self._id
        }

