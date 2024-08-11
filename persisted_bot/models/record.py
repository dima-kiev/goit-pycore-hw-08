from models.name import Name


class Record:

    def __init__(self, name, birthday=None, phones=None):
        self.name = Name(name)
        self.birthday = birthday
        if phones is None:
            phones = []
        self.phones = phones

    def add_phone(self, phone):
        self.phones.append(phone)
        return self

    def add_birthday(self, birthday):
        self.birthday = birthday
        return self

    def __str__(self):
        return (f"Contact name: {self.name.value}, birthday: {self.birthday}, "
                f"phones: {'; '.join(p.value for p in self.phones)}")
