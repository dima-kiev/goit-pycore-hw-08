from services.commands.abstract_cmd import AbstractCmd


class CmdDel(AbstractCmd):
    CMD_NAME = 'del'

    def __init__(self, storage):
        super().__init__()
        self.storage = storage

    def action(self):
        try:
            del_cmd, name = self.user_input.split(" ")
            record = self.storage.find_by_name(name)
            if record is None:
                return f"not found record for {name}"
            self.storage.del_by_name(name)
            return f"removed record {name}"
        except ValueError:
            return "Something went wrong. Should be del NAME, but was: " + self.user_input
