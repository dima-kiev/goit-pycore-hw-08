import pickle
from persisted_bot.services.adress_book import AddressBook


class Persistence:
    FILE_NAME = 'addr_book.pkl'

    def __init__(self):
        self.storage = AddressBook()

    def save(self):
        with open(self.FILE_NAME, "wb") as f:
            pickle.dump(self.storage, f)

    def load(self):
        try:
            with open(self.FILE_NAME, "rb") as f:
                addr_book = pickle.load(f)
                self.storage = addr_book
        except FileNotFoundError:
            print(f"Warning. file not found {self.FILE_NAME}")

        return self.storage
