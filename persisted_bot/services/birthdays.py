from datetime import datetime, timedelta


class Birthdays:

    def __init__(self, storage):
        self.storage = storage

    def get_upcoming_birthdays(self):
        found = []
        today = datetime.today()
        for record in self.storage.find_all():
            delta = (record.birthday.value - today).days
            if 0 < delta < 7:
                found.append(record)

        return found
