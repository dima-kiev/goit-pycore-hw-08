from models.field import Field
from datetime import datetime


class Birthday(Field):

    def __init__(self, birth_sting):
        super().__init__(self.parse_date(birth_sting))

    def parse_date(self, value):
        try:
            return datetime.strptime(str(datetime.today().year) + "." + value, '%Y.%m.%d')
        except ValueError as e:
            raise ValueError(f"Error parsing birthday date {value}, should be MM.DD")
