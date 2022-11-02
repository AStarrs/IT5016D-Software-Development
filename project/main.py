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

    def choose_ticket(self, closed_only=False, opened_only=False):
        available_tickets = []
        for t in Ticket.tickets:
            # create a list of Closed tickets numbers
            if closed_only and t.status == "Closed":
                available_tickets.append(t.ticket_number)
            # create a list of Opened tickets numbers
            elif opened_only and t.status != "Closed":
                available_tickets.append(t.ticket_number)
            # create a list of all tickets numbers
            elif not closed_only and not opened_only:
                available_tickets.append(t.ticket_number)
        print("Available tickets:", available_tickets)
        ticket_chosen = input("Enter ticket number: ")
        return ticket_chosen

    def new_run(self):
        menu = Menu()

        # pre-creating 3 tickets as a test example for convenience
        print("""
This is just tickets created to populate the ticketing
system for testing. The task does not specify the need to keep the
data persistent, so I decided to create 3 tickets during the
runtime of the program to populate with some fake data """)
        Ticket("ANNAC", "Anna Campbel", "annac@example.com", "Printer is not working")
        Ticket("OLGAN", "Olga Newman", "olgan@example.com", "Need Password Change")
        Ticket("JOHNW", "John Wright", "johnw@example.com", "Request for new monitor")

        while menu.exit is not True:
            print(menu.menu())
            user_choice = menu.user_choice()
            if user_choice == "1": # create a ticket
                print("-=========== CREATE NEW TICKET ===========-\n")
                Ticket()
            elif user_choice == "2": # respond to a ticket
                print("-=========== RESPOND TO TICKET ===========-\n")
                ticket_chosen = self.choose_ticket(opened_only=True)
                for t in Ticket.tickets:
                    if t.ticket_number == int(ticket_chosen):
                        response = input("Type new response: ")
                        t.respond_to_ticket(response)
                        print()
                        t.print_ticket()
            elif user_choice == "3": # display a ticket
                print("-=========== SHOW STATS FOR A TICKET ===========-\n")
                ticket_chosen = self.choose_ticket()
                for t in Ticket.tickets:
                    if t.ticket_number == int(ticket_chosen):
                        t.print_ticket()
            elif user_choice == "4": # show stats for all tickets
                print("-=========== STATS FOR ALL TICKETS ===========-\n")
                self.ticket_stats()
            elif user_choice == "5": # re-open a ticket
                print("-=========== REOPEN A TICKET ===========-\n")
                ticket_chosen = self.choose_ticket(closed_only=True)
           
                for t in Ticket.tickets:
                    if t.ticket_number == int(ticket_chosen):
                        t.reopen_ticket()
                        print(f"Ticket {ticket_chosen} has been re-opened\n")
                        t.print_ticket()

            elif user_choice == "6": # display all tickets
                print("-=========== DISPLAY ALL TICKETS ===========-\n")
                self.print_all_tickets()
            elif user_choice == "0":
                print("Exiting programm...")
                menu.exit = True
            else:
                print("Incorrect menu option. Please choose between 0 and 6")



program = Main()
program.new_run()





