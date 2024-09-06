import re
from app.validate import validate_email, validate_data, validate_date ,validate_role
from datetime import datetime
class member:
    def __init__(self, name: str, email: str ,register_date: str ,role:str ='client' ) -> None:
        self.name = name
        self.email = email
        self.role = role
        self.register_date = validate_date(register_date or datetime.today().strftime('%d-%m-%Y'))
        self.validate_str()
        self.validate_email()
        self.validate_role()


    def __str__(self) -> str:
        return f"{self.name} {self.email} and registered on {self.register_date} as a {self.role}"

    def validate_email(self) -> None:
        validate_email(self.email)

    def validate_str(self) -> None:
        validate_data(self.name,self.role)

    def validate_role(self) -> None:
        validate_role(self.role)

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str) -> None:
        self._email = value



def main():
    members = [
        member(name="John Doe", email="john@doeexample.com", register_date="1-1-2000", role="admin"),
        member(name="Jane Doe", email="jane.doe@example.com", register_date="15-5-2010"),
        member(name="Alice Smith", email="alice.smith@example.com", register_date=""),
        member(name="Bob Johnson", email="bob.johnson@example.com", register_date="31-12-1999")
    ]

    for m in members:
        print(m)
if __name__ == '__main__':
    main()