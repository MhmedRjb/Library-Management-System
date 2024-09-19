from app.validate import validate_str, validate_date, is_the_member_exist, validate_staff_role, is_the_book_exist, \
    is_book_available
from app.utils import to_dict
from datetime import datetime, timedelta

DEFAULT_DUE_DATE_AFTER = 3


class Book_movements:
    _id_counter = 1

    def __init__(self, book_title, member_name, staff_name, issue_date=None, due_date=None,return_date=None):
        self.book_title = book_title
        self.member_name = member_name
        self.staff_name = staff_name
        self.return_date=return_date
        self.issue_date = issue_date if issue_date else datetime.today().strftime('%d-%m-%Y')
        self.due_date = due_date if due_date else (datetime.today() + timedelta(days=DEFAULT_DUE_DATE_AFTER)).strftime(
            '%d-%m-%Y')
        # self.in_library = False
        self.transaction_id = Book_movements._id_counter
        Book_movements._id_counter += 1
        self.issue_date = validate_date(self.issue_date)
        self.due_date = validate_date(self.due_date)
        self.validate_data()

    def __str__(self) -> str:
        return f"{self.book_title} was issued to {self.member_name} on {self.issue_date} and is due on {self.due_date}"

    def validate_data(self) -> None:
        is_the_book_exist(self.book_title)
        is_the_member_exist(self.member_name)
        validate_staff_role(self.staff_name)
        is_book_available(self.book_title)

    def to_dict(self) -> dict:
        return to_dict(self)
    


def main():
    movement1 = Book_movements(book_title="The Alchemist", member_name="John Doe", issue_date="01-01-2023",
                               staff_name="Jane Doe", return_date="01-01-2023")
    movement2=Book_movements(
        book_title="The Alchemist",
        member_name="John Doe",
        staff_name="Jane Doe",
        issue_date="01-01-2023",
    )
    print(movement1)
    print(movement2)
    print(movement1.to_dict())
    print(movement2.to_dict())


if __name__ == '__main__':
    main()
