from tickets import Ticket

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


program = Main()
program.run()





