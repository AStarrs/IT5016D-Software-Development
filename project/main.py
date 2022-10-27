from tickets import Ticket


# def show_stats():
#     # Print statistic for Submitted, Open, Resoleved tickets
#     print("Number of Tickets Submitted:", Ticket.num_of_tickets)
#     print("Number of Open Tickets:", Ticket.open_tickets)
#     print("Number of Resoleved Tickets:", Ticket.resolved_tickets)
#     print()
    
# def print_all_tickets():
#     # Print all tickets information
#     for ticket in Ticket.tickets:
#         ticket.print_ticket()

# ticket1 = Ticket("ANNAC", "Anna Campbel", "annac@example.com", "Printer is not working")

# ticket2 = Ticket("OLGAN", "Olga Newman", "olgan@example.com", "Need Password Change")

# ticket3 = Ticket("JOHNW", "John Wright", "johnw@example.com", "Request for new monitor")


# show_stats()
# print_all_tickets()


# ticket1.respond_to_ticket("Printer connection fixed")
# show_stats()
# print_all_tickets()

# ticket1.reopen_ticket("Software update required")
# show_stats()
# print_all_tickets()



class Main:
    def __init__(self):
        self.name = "Ticketing System"
    
    def show_stats(self):
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
        print("========== Creating Tickets ==========\n")

        self.ticket1 = Ticket("ANNAC", "Anna Campbel", "annac@example.com", "Printer is not working")

        self.ticket2 = Ticket("OLGAN", "Olga Newman", "olgan@example.com", "Need Password Change")

        self.ticket3 = Ticket("JOHNW", "John Wright", "johnw@example.com", "Request for new monitor")

        self.show_stats()
        self.print_all_tickets()

        print("========== Respond to Ticket 2001 ==========\n")
        # Respond and resolve issue for ticket1, close and change stats
        self.ticket1.respond_to_ticket("Printer connection fixed")
        
        self.show_stats()
        self.print_all_tickets()

        print("========== Reopen ticket 2002 ==========")
        # Reopen closed ticket2, change stats
        self.ticket2.reopen_ticket("Software update required")

        self.show_stats()
        self.print_all_tickets()


program = Main()
program.run()





