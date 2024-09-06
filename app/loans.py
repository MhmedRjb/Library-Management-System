from app.validate import validate_str, validate_date, is_the_member_exist, validate_staff_role ,is_the_book_exist, is_book_available
from app.utils import to_dict
from datetime import datetime, timedelta

DEFAULT_DUE_DATE_AFTER = 3


class Book_movemtents:
    _id_counter = 1

    def __init__(self ,book_title: int, member_name: str, staff_name :str, issue_date: str = None, due_date: str = None,in_library :bool = 0 ) -> None:
        self._transaction_id = Book_movemtents._id_counter
        Book_movemtents._id_counter += 1
        self._transaction_id = Book_movemtents._id_counter
        self._book_title = book_title
        self._issue_date = validate_date(issue_date or datetime.today().strftime('%d-%m-%Y'))
        self._due_date = validate_date(due_date or (datetime.today() + timedelta(days=DEFAULT_DUE_DATE_AFTER)).strftime('%d-%m-%Y'))
        self._member_name = member_name
        self._staff_name = staff_name
        self._in_library = in_library

    def __str__(self) -> str:
        return f"{self._book_title} was issued to {self._member_name} on {self._issue_date} and is due on {self._due_date}"

    def validate_data(self) -> None:
        pass
        is_the_book_exist(self._book_title)
        is_book_available(self._book_title)
        is_the_member_exist(self._member_name, self._staff_name)
        validate_staff_role(self._staff_name)

    def to_dict(self) -> dict:
        return to_dict(self)

    @property
    def book_title(self) -> int:
        return self._book_title

    @property
    def issue_date(self) -> str:
        return self._issue_date

    @property
    def due_date(self) -> str:
        return self._due_date

    @property
    def member_name(self) -> str:
        return self._member_name
    @property
    def staff_name(self) -> str:
        return self._staff_name
    @property
    def transaction_id(self) -> int:
        return self._transaction_id
    @property
    def in_library(self) -> str:
        return self._in_library

    @in_library.setter
    def update_in_library(self, value: int) -> None:
        self._in_library = value





def main():
    movement1 = Book_movemtents(book_title=1, member_name="John Doe", issue_date="01-01-2023",staff_name="Jane Doe")
    movement2 = Book_movemtents(book_title=2, member_name="Jane Smith", issue_date="02-01-2023", due_date="05-01-2023",staff_name="Alice Smith")
    #update the in_library value
    movement1.update_in_library = 1

    print(movement1)
    print(movement2)
    print(movement1.to_dict())
    print(movement2.to_dict())

if __name__ == '__main__':
    main()