from services.commands.abstract_cmd import AbstractCmd


class CmdList(AbstractCmd):
    CMD_NAME = 'list'

    def __init__(self, storage):
        super().__init__()
        self.storage = storage

    def action(self):
        try:
            find_cmd = self.user_input
            records = self.storage.find_all()
            all_records = ""
            for record in records:
                all_records = all_records + str(record) + "\n"
            return all_records
        except ValueError:
            return "Something went wrong. Should be list, but was: " + self.user_input
