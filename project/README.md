## Python project for Help Desk Ticketing System prototype

The ticketing system prototype was created to meet customer requirments for
handling Help Desk tickets for internal customers.

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

Program contains of three Python files:
* tickets.py
* main.py
* menu.py

### How to run the programm

1. Download three program files (tickets.py, main.py, menu.py) 

2. Run main.py in terminal with `python3 main.py`

3. Choose from the main manu options (0-6) to use ticketing system:

-=========== MAIN MENU ===========-

Please choose an option and press Enter:

1: Create a ticket
2: Respond to a ticket
3: Display a ticket
4: Show stats for all tickets
5: Re-open a ticket
6: Display all tickets

Press 0 for exit...

Note: There are 3 tickets created to populate the ticketing
system for testing. The task does not specify the need to keep the
data persistent, so I decided to create 3 tickets during the
runtime of the program to populate with some fake data

* To create new ticket, enter 1 and input information step by step following
   the system questions. 

* To respond to a ticket, press 2 and type ticket number from the list of Opened
   ticket numbers, enter response.

* To display a particular ticket, press 3 and enter a ticket number from the
   list of ticket numbers.

* To re-open ticket, enter 5 and type ticket number from the list of
   Closed tickets.



