from tickets import Ticket


def show_stats():
    # Print statistic for Submitted, Open, Resoleved tickets
    print("Number of Tickets Submitted:", Ticket.num_of_tickets)
    print("Number of Open Tickets:", Ticket.open_tickets)
    print("Number of Resoleved Tickets:", Ticket.resolved_tickets)
    print()
    
def print_all_tickets():
    # Print all tickets information
    for ticket in Ticket.tickets:
        ticket.print_ticket()

ticket1 = Ticket("ANNAS", "Anna Starovoytova", "annas@example.com", "Printer is not working")

ticket2 = Ticket("OLGAN", "Olga Newman", "olgan@example.com", "Need Password Change")

ticket3 = Ticket("JOHNW", "John Wright", "johnw@example.com", "Request for new monitor")


show_stats()
print_all_tickets()


ticket1.respond_to_ticket("Printer connection fixed")
show_stats()
print_all_tickets()

ticket1.reopen_ticket("Software update required")
show_stats()
print_all_tickets()








