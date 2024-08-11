from models.phone import Phone
from models.record import Record
from services.commands.abstract_cmd import AbstractCmd


class CmdEdit(AbstractCmd):
    CMD_NAME = 'append_phone'

    def __init__(self, storage):
        super().__init__()
        self.storage = storage

    def action(self):
        try:
            edit_cmd, name, new_phone = self.user_input.split(" ")
            existing_record = self.storage.find_by_name(name)
            if existing_record is None:
                new_record = Record(name, [Phone(new_phone)])
                self.storage.add_record(new_record)
                return f"not found for {name}. created new record {new_record}"
            existing_record.add_phone(Phone(new_phone))
            self.storage.save(existing_record)
            return f"updated {existing_record}"
        except ValueError:
            return "Something went wrong. Should be append_phone NAME NEW_PHONE, but was: " + self.user_input
