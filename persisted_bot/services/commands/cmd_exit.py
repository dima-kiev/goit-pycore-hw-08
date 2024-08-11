from services.commands.abstract_cmd import AbstractCmd


class CmdExit(AbstractCmd):
    CMD_NAME = 'exit'

    def __init__(self, persistence_service):
        self.persistence_service = persistence_service
        super().__init__()

    def action(self):
        self.persistence_service.save()
        exit(1)
