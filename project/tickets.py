class Ticket:

    num_of_tickets = 0
    open_tickets = 0
    resolved_tickets = 0

    def __init__(self, staff_id, creator, email, description):
        Ticket.num_of_tickets += 1
        Ticket.open_tickets +=1
        self.staff_id = staff_id
        self.creator = creator
        self.email = email
        self.description = description
        self.response = "Not Yet Provided"
        self.status = "Open"

        self.ticket_number = Ticket.num_of_tickets + 2000

        if "password change" in self.description.lower():
            self.new_password()

    def print_ticket(self):
        '''Displays main information about the ticket'''
        # return '{} {} {} {} {}'.format(self.ID, self.creator, self.email, self.description, self.response)
        print("Ticket Number:", self.ticket_number)
        print("Staff ID:", self.staff_id)
        print("Creator:", self.creator)
        print("Email:", self.email)
        print("Description:", self.description)
        print("Response:", self.response)
        print("Status:", self.status)
        print()
        # return f'{self.staff_id}\n{self.creator}\n{self.email}\n{self.description}'

    # @classmethod
    # def print_stats(cls):
    #     print("Number of Tickets Submitted:", Ticket.num_of_tickets)
    #     print("Number of Open Tickets:", Ticket.open_tickets)
    #     print("Number of Resoleved Tickets:", Ticket.resolved_tickets)

    def ticket_response(self):
        Ticket.open_tickets +=1
        Ticket.open_tickets +=1
        pass

    def new_password(self):

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
