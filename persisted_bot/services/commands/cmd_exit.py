from services.commands.abstract_cmd import AbstractCmd


class CmdExit(AbstractCmd):
    CMD_NAME = 'exit'

    def __init__(self):
        super().__init__()

    def action(self):
        exit(1)
