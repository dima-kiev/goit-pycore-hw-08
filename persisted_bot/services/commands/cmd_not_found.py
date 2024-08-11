from services.commands.abstract_cmd import AbstractCmd


class CmdNotFound(AbstractCmd):
    CMD_NAME = 'NOT_FOUND'

    def __init__(self):
        super().__init__()

    def action(self):
        return """WTF, Doc? valid commands only pleazzzzze!
        - help
        - hello
        - exit
        - close 
        - add <name> <phone> 
        - del <name>
        - find <name>
        - append_phone <name> <additional_phone>
        - list
        - birth_add <name> <birth MM.DD>
        - birth_list
        
        """
