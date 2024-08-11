from services.commands.abstract_cmd import AbstractCmd


class CmdHello(AbstractCmd):
    CMD_NAME = 'hello'

    def __init__(self):
        super().__init__()

    def action(self):
        return "o_O really? try help"
