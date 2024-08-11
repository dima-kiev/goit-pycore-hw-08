from services.commands.abstract_cmd import AbstractCmd


class CmdBirthList(AbstractCmd):
    CMD_NAME = 'birth_list'

    def __init__(self, birth_service):
        super().__init__()
        self.birth_service = birth_service

    def action(self):
        try:
            records = self.birth_service.get_upcoming_birthdays()
            all_records = ""
            for record in records:
                all_records = all_records + str(record) + "\n"
            return all_records
        except ValueError:
            return "Something went wrong. Should be birth_list, but was: " + self.user_input
