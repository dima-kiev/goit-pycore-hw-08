from models.field import Field


def validate_name(name):
    if len(name) < 1:
        raise ValueError("Name must be at least 1 character long")


class Name(Field):

    def __init__(self, name):
        validate_name(name)
        super().__init__(name)
