from tickets import Ticket


def show_stats():
    print("Number of Tickets Submitted:", Ticket.num_of_tickets)
    print("Number of Open Tickets:", Ticket.open_tickets)
    print("Number of Resoleved Tickets:", Ticket.resolved_tickets)
    
ticket1 = Ticket(1, "Anna Starovoytova", "anna@example.com", "My python program is not working")

ticket2 = Ticket(1, "Anna Starovoytova", "anna@example.com", "My python program is not working")

# ticket3 = Ticket(1, "Anna Starovoytova", "anna@example.com", "My python program is not working")
# ticket4 = Ticket(1, "Anna Starovoytova", "anna@example.com", "My python program is not working")
# ticket5 = Ticket(1, "Anna Starovoytova", "anna@example.com", "My python program is not working")
# ticket6 = Ticket(1, "Anna Starovoytova", "anna@example.com", "My python program is not working")
# ticket7 = Ticket(1, "Anna Starovoytova", "anna@example.com", "My python program is not working")
# ticket8 = Ticket(1, "Anna Starovoytova", "anna@example.com", "My python program is not working")

# print(Ticket.print_stats())

# print(ticket1.ticket_number)
# show_stats()

# print("Ticket 1", ticket1.num_of_tickets)
# print("Ticket 2", ticket2.num_of_tickets)
# print("System: ", Ticket.num_of_tickets)