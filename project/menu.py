"""Provides menu class for generating and navigating the main menu"""

class Menu:
    def __init__(self):
        self.exit = False # flag to indicate if user exited 



    def menu(self):
        return '''
-== Wellcome to the Ticketing System ==-

Please choose an option and press Enter:

1: Create a ticket
2: Respond to a ticket
3: Show stats for a ticket
4: Show stats for all tickets
5: Re-open a ticket
6: Display all tickets

Press 0 for exit...
'''

    def user_choice(self):
        return input("Enter your choice: ")