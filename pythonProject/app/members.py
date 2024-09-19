import re
from app.validate import validate_email, validate_str, validate_date, validate_role
from datetime import datetime
from app.utils import to_dict

class Member:
    def __init__(self, name: str, email: str, register_date: str = None, role: str = 'client') -> None:
        self._name = name
        self._email = validate_email(email)
        self._role = validate_role(role)
        self.register_date = validate_date(register_date or datetime.today().strftime('%d-%m-%Y'))

    def __str__(self) -> str:
        return f"{self.name} {self.email} and registered on {self.register_date} as a {self.role}"

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        validate_str(value)
        self._name = value

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str) -> None:
        validate_email(value)
        self._email = value

    @property
    def role(self) -> str:
        return self._role

    @role.setter
    def role(self, value: str) -> None:
        validate_role(value)
        self._role = value

    def to_dict(self) -> dict:
        return to_dict(self)
def main():
    members = [
        Member(name="John Doe", email="john@doeexample.com", register_date="1-1-2000", role="admin"),
        Member(name="Jane Doe", email="jane.doe@example.com", register_date="15-5-2010"),
        Member(name="Alice Smith", email="alice.smith@example.com", register_date=""),
        Member(name="Bob Johnson", email="bob.johnson@example.com", register_date="31-12-1999")
    ]
    #CAHNGE THE ROLE OF THE FIRST MEMBER
    members[0].role = "staff"
    #CHANGE THE EMAIL OF THE SECOND MEMBER
    members[1].email = "M@GMAIL.COM"
    #CHANGE THE NAME OF THE THIRD MEMBER
    members[2].name = "Alice Johnson"
    #save the data to the json


    for m in members:
        print(m)
if __name__ == '__main__':
    main()