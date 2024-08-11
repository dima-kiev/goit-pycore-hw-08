from models.phone import Phone
from models.record import Record
from services.commands.abstract_cmd import AbstractCmd


class CmdAdd(AbstractCmd):
    CMD_NAME = 'add'

    def __init__(self, storage):
        super().__init__()
        self.storage = storage

    def action(self):
        try:
            add_cmd, name, phone = self.user_input.split(" ")
            normalized_phone = int(phone)
            new_record = Record(name, None, [Phone(phone)])
            self.storage.add_record(new_record)
            return f"{new_record} was successfully added"
        except ValueError:
            print("Something went wrong. Should be add NAME PHONE, but was: " + self.user_input)
            raise ValueError
