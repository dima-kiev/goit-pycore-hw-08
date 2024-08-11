from models.field import Field


def validate(value: str):
    if len(value) != 10 or not value.isalnum():
        raise ValueError(f"phone number is invalid: {value}. Should be 10 digits")


class Phone(Field):

    def __init__(self, phone):
        validate(phone)
        super().__init__(phone)
