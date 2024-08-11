from persisted_bot.services.persistence import Persistence
from services.adress_book import AddressBook
from services.birthdays import Birthdays
from services.cmd_factory import CmdFactory
from views.view import View
from controllers.controller import Controller


def init_test_data(controller):
    controller.dispatch_command("add sasha 1234567890")
    controller.dispatch_command("add masha 1234567890")
    controller.dispatch_command("add misha 1234567890")
    controller.dispatch_command("add marisha 1234567890")
    controller.dispatch_command("append_phone sasha 0987654321")
    controller.dispatch_command("append_phone misha 0987654321")
    controller.dispatch_command("birth_add sasha 08.15")
    controller.dispatch_command("birth_add misha 08.16")
    controller.dispatch_command("birth_add masha 09.16")
    controller.dispatch_command("birth_add marisha 07.16")


def main():

    persistence_service = Persistence()
    storage = persistence_service.load()

    birthdays = Birthdays(storage)
    cmd_factory = CmdFactory(birthdays, storage, persistence_service)
    controller = Controller(cmd_factory)
    view = View(controller)

    # init_test_data(controller)

    view.start("help")


if __name__ == '__main__':
    main()
