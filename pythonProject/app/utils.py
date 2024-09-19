import json
from typing import Type



def to_dict(obj: object) -> dict:
    return {attr: getattr(obj, attr) for attr in dir(obj)
            if not attr.startswith('_') and not
            callable(getattr(obj, attr))}


def save_data(file_path: str, data: list) -> None:
    with open(file_path, "w") as file:
        json.dump([item.to_dict() for item in data], file)

def load_data(file_name, cls):
    try:
        with open(file_name, "r") as file:
            data = json.load(file)
            return [cls(**item) for item in data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []