"""The task does not specify the need to keep the data persistent, so assumption
   is made that there is no need to save the data
   All the tickets need to be created at run time and will be destroyed after exiting
"""

from tickets import Ticket
from menu import Menu

class Main:
    def __init__(self):
        self.name = "Ticketing System"
    
    def ticket_stats(self):
        # Print statistic for Submitted, Open, Resoleved tickets
        print("Number of Tickets Submitted:", Ticket.num_of_tickets)
        print("Number of Open Tickets:", Ticket.open_tickets)
        print("Number of Resoleved Tickets:", Ticket.resolved_tickets)
        print()
    
    def print_all_tickets(self):
        # Print all tickets information
        for ticket in Ticket.tickets:
            ticket.print_ticket()

    def run(self):
        # Run the program
        print("========== Creating Tickets ==========\n")
        # Creating 3 tickets, ticket2 autoresolve the password change and change
        # status to closed
        self.ticket1 = Ticket("ANNAC", "Anna Campbel", "annac@example.com", "Printer is not working")

        self.ticket2 = Ticket("OLGAN", "Olga Newman", "olgan@example.com", "Need Password Change")

        self.ticket3 = Ticket("JOHNW", "John Wright", "johnw@example.com", "Request for new monitor")

        self.ticket_stats()
        self.print_all_tickets()

        print("========== Respond to Ticket 2001 ==========\n")
        # Respond and resolve issue for ticket1, close and change stats
        self.ticket1.respond_to_ticket("Printer connection fixed")
        
        self.ticket_stats()
        self.print_all_tickets()

        print("========== Reopen ticket 2002 ==========\n")
        # Reopen closed ticket2, add response, change stats and status
        self.ticket2.reopen_ticket("Software update required")

        self.ticket_stats()
        self.print_all_tickets()

    def new_run(self):
        menu = Menu()
        while menu.exit is False:
            print(menu.menu())
            user_choice = menu.user_choice()
            if user_choice == "1": # create a ticket
                ticket = Ticket()
            elif user_choice == "2": # respond to a ticket
                pass
            elif user_choice == "3": # show stats for a ticket
                available_tickets = []
                for t in Ticket.tickets:
                    available_tickets.append(t.ticket_number)
                print("Available tickets", available_tickets)
                user_choice = input("Enter ticket number to show stats: ")
                for t in Ticket.tickets:
                    if t.ticket_number == int(user_choice):
                        t.print_ticket()
            elif user_choice == "4": # show stats for all tickets
                print(f"You entered {user_choice}")
            elif user_choice == "5": # re-open a ticket
                ticket_num = input("Enter ticket number to re-open: ")
                reopen_ticket()
            elif user_choice == "6": # display all tickets
                self.print_all_tickets()
            elif user_choice == "0":
                print(f"You entered {user_choice}")
                menu.exit = True
            else:
                print("Incorrect menu option. Please choose between 0 and 6")
        print("Exiting programm...")

program = Main()
program.new_run()





