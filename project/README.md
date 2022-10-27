## Python project for Help Desk Ticketing System prototype

The ticketing system prototype was created to meet customer requirments for
hendling Help Desk tickets for internal customers.

### Program functiionality

* create tickets from internal customers only
* help desk staff access tickets and respond to tickets
* allocate a ticket number
* automaticaly close responded tickets and change statistics and ticket status
* show tickets statistics (total, open and resolved)
* autoresolve tickets with password change requests (autocreate password, update
 responce with new password and change status and statistics)
* reopen closed tickets (with status and stats update)
* print all tickets

### Program structure

Program contains of two Python files:
* tickets.py
* main.py

#### tickets.py 

`class Ticket`

Ticket has `class variables`, which are used to keep track of tickets statistics:

`num_of_tickets`
`open_tickets`
`resolved_tickets`

`tickets` variable is a list to hold created tickets in memory (used for
printing all tickets)

The main `__init__` method allows to create tickets, update stats, autoresolve
password change, allocate ticket number and add created ticket to a list of
tickets

#### main.py


