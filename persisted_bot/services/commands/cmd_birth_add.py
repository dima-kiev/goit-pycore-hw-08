from models.birthday import Birthday
from models.record import Record
from services.commands.abstract_cmd import AbstractCmd


class CmdBirthAdd(AbstractCmd):
    CMD_NAME = 'birth_add'

    def __init__(self, storage):
        super().__init__()
        self.storage = storage

    def action(self):
        try:
            birth_add_cmd, name, birth = self.user_input.split(" ")
            existing_record = self.storage.find_by_name(name)
            if existing_record is None:
                new_record = Record(name, Birthday(birth), [])
                self.storage.add_record(new_record)
                return f"not found for {name}. created new record {new_record}"
            existing_record.add_birthday(Birthday(birth))
            self.storage.save(existing_record)
            return f"updated {existing_record}"
        except ValueError:
            return "Something went wrong. Should be birth_add NAME BIRTHDAY(MM.DD), but was: " + self.user_input
