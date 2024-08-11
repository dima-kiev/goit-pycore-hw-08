from collections import UserDict


class AddressBook(UserDict):

    def __init__(self):
        super().__init__()

    def add_record(self, record):
        self.data[record.name.value] = record

    def find_by_name(self, name):
        return self.data.get(name)

    def save(self, record):
        self.data[record.name.value] = record

    def find_all(self):
        return self.data.values()

    def del_by_name(self, name):
        del self.data[name]
