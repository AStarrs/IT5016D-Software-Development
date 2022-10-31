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

    # def run(self):
    #     # Run the program
    #     print("========== Creating Tickets ==========\n")
    #     # Creating 3 tickets, ticket2 autoresolve the password change and change
    #     # status to closed
    #     self.ticket1 = Ticket("ANNAC", "Anna Campbel", "annac@example.com", "Printer is not working")

    #     self.ticket2 = Ticket("OLGAN", "Olga Newman", "olgan@example.com", "Need Password Change")

    #     self.ticket3 = Ticket("JOHNW", "John Wright", "johnw@example.com", "Request for new monitor")

    #     self.ticket_stats()
    #     self.print_all_tickets()

    #     print("========== Respond to Ticket 2001 ==========\n")
    #     # Respond and resolve issue for ticket1, close and change stats
    #     self.ticket1.respond_to_ticket("Printer connection fixed")
        
    #     self.ticket_stats()
    #     self.print_all_tickets()import os

    #     print("========== Reopen ticket 2002 ==========\n")
    #     # Reopen closed ticket2, add response, change stats and status
    #     self.ticket2.reopen_ticket("Software update required")

    #     self.ticket_stats()
    #     self.print_all_tickets()

    def choose_ticket(self):
        available_tickets = []
        for t in Ticket.tickets:
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
                ticket_chosen = self.choose_ticket()
                for t in Ticket.tickets:
                    if t.ticket_number == int(ticket_chosen):
                        response = input("Type new response: ")
                        t.respond_to_ticket(response)
            elif user_choice == "3": # show stats for a ticket
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
                ticket_chosen = self.choose_ticket()
                for t in Ticket.tickets:
                    if t.ticket_number == int(ticket_chosen):
                        t.reopen_ticket()
                        print(f"Ticket {ticket_chosen} has been re-opened")
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





