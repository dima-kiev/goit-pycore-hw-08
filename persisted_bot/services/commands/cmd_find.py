from services.commands.abstract_cmd import AbstractCmd


class CmdFind(AbstractCmd):
    CMD_NAME = 'find'

    def __init__(self, storage):
        super().__init__()
        self.storage = storage

    def action(self):
        try:
            find_cmd, name = self.user_input.split(" ")
            record = self.storage.find_by_name(name)
            if record is None:
                return f"not found record for {name}"
            return f"found {record}"
        except ValueError:
            return "Something went wrong. Should be find NAME, but was: " + self.user_input
