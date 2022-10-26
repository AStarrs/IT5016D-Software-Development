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

        self.ticket_number = Ticket.num_of_tickets + 2000

    def print_ticket(self):
        '''Displays main information about the ticket'''
        # return '{} {} {} {} {}'.format(self.ID, self.creator, self.email, self.description, self.response)
        print("Ticket Number:", self.ticket_number)
        print("Staff ID:", self.staff_id)
        print("Creator:", self.creator)
        print("Email:", self.email)
        print("Description:", self.description)
        print("Response:", "Not Yet Provided")
        # return f'{self.staff_id}\n{self.creator}\n{self.email}\n{self.description}'

    # @classmethod
    # def print_stats(cls):
    #     print("Number of Tickets Submitted:", Ticket.num_of_tickets)
    #     print("Number of Open Tickets:", Ticket.open_tickets)
    #     print("Number of Resoleved Tickets:", Ticket.resolved_tickets)

    def ticket_response(self):
        pass

    def new_password(self):
        first_part = str(self.staff_id)[:2]
        second_part = self.creator[:3]
        print(first_part+second_part)
