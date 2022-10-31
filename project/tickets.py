"""Ticket class provides main methods and general statistics storage for
runtime"""

class Ticket:

    num_of_tickets = 0
    open_tickets = 0
    resolved_tickets = 0

    tickets = []

    def __init__(self, staff_id=None, creator=None, email=None, description=None):
        Ticket.num_of_tickets += 1
        Ticket.open_tickets += 1
        # if no data at ticket creation ask user for input
        if not staff_id or not creator or not email or not description:
            self.staff_id = input("Enter staff ID: ")
            self.creator = input("Enter your name: ")
            self.email = input("Enter your email: ")
            self.description = input("Enter the description of your issue: ")
        else:
            # used in main.py to pre-generate some tickets without user input
            self.staff_id = staff_id
            self.creator = creator
            self.email = email
            self.description = description
        self.response = "Not Yet Provided"
        self.status = "Open"

        self.ticket_number = Ticket.num_of_tickets + 2000

        if "password change" in self.description.lower():
            self.autoresolve_password_change()

        Ticket.tickets.append(self)
        print(f"\nNew ticket {self.ticket_number} has been created")


    def print_ticket(self):
        #Displays main information about the ticket
        print("Ticket Number:", self.ticket_number)
        print("Staff ID:", self.staff_id)
        print("Creator:", self.creator)
        print("Email:", self.email)
        print("Description:", self.description)
        print("Response:", self.response)
        print("Status:", self.status)
        print()


    def respond_to_ticket(self, response):
        # update instace response attribute
        self.response = response

        # Update status
        self.status = "Closed"

        # Update ticket statistics
        Ticket.open_tickets -=1
        Ticket.resolved_tickets +=1
    

    def autoresolve_password_change(self):

        # Generate new password
        first_part = self.staff_id[:2]
        second_part = self.creator[:3]
        new_password = first_part + second_part

        # Update response
        self.response = f"New password generated: {new_password}"  
        
        # Update status
        self.status = "Closed"

        # Update ticket statistics
        Ticket.open_tickets -=1
        Ticket.resolved_tickets +=1
        print("\nTicket has been automatically closed and new password generated")
        print(self.response)

    def reopen_ticket(self):
        # Update status and reopen ticket
        self.status = "Reopened"

        # Update ticket statistics
        Ticket.open_tickets +=1
        Ticket.resolved_tickets -=1
    


# ticket1 = Ticket()

# ticket2 = Ticket("12345", "anna", "anna@test.com", "Problem with my keyboard")