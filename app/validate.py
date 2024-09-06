# app/validate.py
import re
from datetime import datetime
import json
class validate:
    @staticmethod
    def validate_email(email: str) -> bool:
        pattern_email = re.compile(r"^[\w\.\+-]+@([\w-]+\.)+[\w-]{2,4}$")
        if not pattern_email.match(email):
            raise ValueError(f"Invalid email -{email}")
        return True

    @staticmethod
    def validate_str(*strings: str) -> bool:
        for string in strings:
            if not isinstance(string, str):
                raise ValueError("string only")
        return True
    @staticmethod
    def validate_date(date: str) -> bool:
        pattern_date = re.compile(r"^(3[01]|[12][0-9]|0?[1-9])(\/|-)(1[0-2]|0?[1-9])\2([0-9]{4})$")
        match = pattern_date.match(date)
        if not pattern_date.match(date):
            raise ValueError("Invalid date please use the format dd-mm-yyyy")
        day, separator, month, year = match.groups()
        normalized_date = datetime.strptime(f"{day}{separator}{month}{separator}{year}",
                                            f"%d{separator}%m{separator}%Y")
        return normalized_date.strftime("%d-%m-%Y")

    @staticmethod
    def validate_role(data: str) -> bool:
        roles = ["client", "staff", "admin"]
        if data not in roles:
            raise ValueError( {data},"not one of the available", roles)
        return True

    @staticmethod
    def is_the_member_exist(member_name: str) -> bool:
        validate_str(member_name)
        with open("members.json", "r") as file:
            members = json.load(file)
            for member in members:
                if member["name"] == member_name:
                    return True
                else:
                    raise ValueError(f"{member_name} is not in the library")

    @staticmethod
    def is_the_book_exist(title: str) -> bool:
        validate_str(title)
        with open("books.json", "r") as file:
            books = json.load(file)
            for book in books:

                if book["title"] == title:
                    return True
                else:
                    raise ValueError(f"{title} is not in the library")

    @staticmethod
    def is_book_available(title: str) -> bool:
        pass
        return True


    @staticmethod
    def validate_staff_role(member_name: str) -> bool:
        with open("members.json", "r") as file:
            members = json.load(file)
            for member in members:
                if member["name"] == member_name:
                    if member["role"] in ["staff", "admin"]:
                        return True
                    else:
                        raise ValueError(f"{member_name} is not a staff member")
        return True


validate_email = validate.validate_email
validate_str = validate.validate_str
validate_date = validate.validate_date
validate_role = validate.validate_role
is_the_member_exist = validate.is_the_member_exist
is_the_book_exist = validate.is_the_book_exist
is_book_available = validate.is_book_available
validate_staff_role = validate.validate_staff_role
