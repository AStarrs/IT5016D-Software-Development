class Ticket:

    num_of_tickets = 0
    open_tickets = 0
    resolved_tickets = 0

    def __init__(self, staff_id, creator, email, description):
        self.staff_id = staff_id
        self.creator = creator
        self.email = email
        self.description = description

        Ticket.num_of_tickets += 1
        Ticket.open_tickets +=1

    
    def print_ticket(self):
        '''Displays main information about the ticket'''
        # return '{} {} {} {} {}'.format(self.ID, self.creator, self.email, self.description, self.response)
        print("Staff ID:", self.staff_id)
        print("Creator:", self.creator)
        print("Email:", self.email)
        print("Description:", self.description)
        # return f'{self.staff_id}\n{self.creator}\n{self.email}\n{self.description}'


    def print_stats(self):
        pass