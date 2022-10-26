from tickets import Ticket


def show_stats():
    print("Number of Tickets Submitted:", Ticket.num_of_tickets)
    print("Number of Open Tickets:", Ticket.open_tickets)
    print("Number of Resoleved Tickets:", Ticket.resolved_tickets)
    print()
    
ticket1 = Ticket("ANNAS", "Anna Starovoytova", "anna@example.com", "My python program is not working")

ticket2 = Ticket("OLGAS", "Olga Starovoytova", "anna@example.com", "Need Password Change")

ticket3 = Ticket("JOHNW", "John Wright", "anna@example.com", "My python program is not working")
# ticket4 = Ticket(1, "Anna Starovoytova", "anna@example.com", "My python program is not working")
# ticket5 = Ticket(1, "Anna Starovoytova", "anna@example.com", "My python program is not working")
# ticket6 = Ticket(1, "Anna Starovoytova", "anna@example.com", "My python program is not working")
# ticket7 = Ticket(1, "Anna Starovoytova", "anna@example.com", "My python program is not working")
# ticket8 = Ticket(1, "Anna Starovoytova", "anna@example.com", "My python program is not working")

# print(Ticket.print_stats())

# print(ticket1.new_password())
show_stats()

# print("Ticket 1", ticket1.num_of_tickets)
# print("Ticket 2", ticket2.num_of_tickets)
# print("System: ", Ticket.num_of_tickets)

ticket1.print_ticket()
ticket2.print_ticket()
ticket3.print_ticket()

