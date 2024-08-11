class View:

    def __init__(self, controller):
        self.controller = controller

    def start(self, init_command):
        print(self.controller.dispatch_command(init_command))
        while True:
            prob_command = input("wats`up, Doc? ")
            print(self.controller.dispatch_command(prob_command))
