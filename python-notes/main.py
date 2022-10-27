# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

name = "Anna"

print(name)

age = 35

print(age)

3 + 5


print("Program 'Game Over' 2.0")
print("Same", "message", "as before")
print("Just",
 "a bit",
 "bigger")
print("Here", end=" ")
print("it is...")
print(
 """
  _____       ___      ___     ___ _____
 / ___|      /   |     / |    / | | ___|
 | |        / /| |    / /|   /| | | |__
 | |  _    / ___ |   / / |__/ | | | __|
 | |_| |  / /  | |  / /       | | | |___
 \_____/ /_/   |_| /_/        |_| |_____|
  _____   _      _ _____   _____
 /  _ \  | |   / / | ___|  |  _ 
 | | | | | |  / /  | |__   | |_| |
 | | | | | | / /   | __|   | _  /
 | |_| | | |/ /    | |___  | | \ 
 \_____/ |___/     |_____| |_|  \_
 """
 )
input("\n\nPress the enter key to exit.")

print("kia Ora, this is a parking meter")
ParkTime = 4
print ("Park time is ", ParkTime, " hours.")

rate = 4
cost = 0

if ParkTime > 3:
    cost = rate * 3
    rate -= 2
    ParkTime -= 3
    cost += rate * ParkTime
    print("The cost of the parking is $", cost)
else:
    cost = rate * ParkTime
    print("The cost of the parking is $", cost)


# Lists

L = ["A", "B", "C"]

my_list = ['p','r','o','b','e']
# Output: p
print(my_list[0])
# Output: o
print(my_list[2])
# Output: e
print(my_list[4])
# Error! Only integer can be used for indexing
# my_list[4.0]
# Nested List
n_list = ["Happy", [2,0,1,6]]
# Nested indexing
# Output: a
print(n_list[0][1])
# Output: 5
print(n_list[1][3])
# using negative indexing
# Output: e
print(my_list[-1])


primes = [1, 2, 3, 5, 7, 11, 13]

primes.append(17)

primes

letters = ['a', 'b', 'c']

numbers = [1, 2, 3]

letters + numbers


from datetime import datetime, timedelta
 
duration = 5
 
run = input("enter s to begin...")
 
period = timedelta(seconds=1)
 
next_time = datetime.now() + period
 
counter = 0
while run == 's' and counter < duration:
    if next_time <= datetime.now():
        print("..", counter)
        counter += 1
        # reevaluate the next_time variable
        next_time += period
 

# Tuples

bank_accounts = (("Joe", 33, "234 Great South Road", "022629107"),
                 ("Tama", 6000),
                 ("Suzanne", 21025, "45 Green Lane"),
                 ("Anihera", -75))
 
print("The number of bank accounts is ", len(bank_accounts))
 
# showing names and balances
for i in bank_accounts:
    print("\nThe name is ", i[0], " and the balance is $", i[1])
 
# showing only names with addresses
for i in bank_accounts:
    if len(i)>2:
        print("\nThe name is ", i[0], " and the address is ", i[2])


# The number of bank accounts is  4
 
# The name is  Joe  and the balance is $ 33
 
# The name is  Tama  and the balance is $ 6000
 
# The name is  Suzanne  and the balance is $ 21025
 
# The name is  Anihera  and the balance is $ -75
 
# The name is  Joe  and the address is  234 Great South Road
 
# The name is  Suzanne  and the address is  45 Green Lane


# Dictionaries

dictionary_1 = {"V344LDA":2000,
                "J245DWE":6350,
                "K265QWS":500}
 
# retrieving a value from the dictionary
print("The car with registration V344LDA is worth $", dictionary_1["V344LDA"])


# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}
 
 # add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'
 
# print out some cities
print ('-' * 10)
print ("NY State has: ", cities['NY'])
print ("OR State has: ", cities['OR'])

# print some states
print ('-' * 10)
print ("Michigan's abbreviation is: ", states['Michigan'])
print ("Florida's abbreviation is: ", states['Florida'])
 
# do it by using the state then cities dict
print ('-' * 10)
print ("Michigan has: ", cities[states['Michigan']])
print ("Florida has: ", cities[states['Florida']])
 
# print every state abbreviation
print ('-' * 10)
for state, abbrev in states.items():
    print("{0} is abbreviated {1}".format(state, abbrev))
 
# print every city in state
print( '-' * 10)
for abbrev, city in cities.items():
    print ("{0} has the city {1}".format(abbrev, city))
 
# now do both at the same time
print ('-' * 10)
for state, abbrev in states.items():
    print ("{0} state is abbreviated {1} and has city {2}".format(
        state, abbrev, cities[abbrev]))
 
print ('-' * 10)
# safely get a abbreviation by state that might not be there
state = states.get('Texas')
 
if not state:
    print ("Sorry, no Texas.")
 
# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print ("The city for the state 'TX' is: {0}".format(city))

# functions

def show_hello():
    print("Hello there, this is my very first function!!!\n\n")
 
print("Testing my first user defined function...\n\n")
 
# invoking the function
show_hello()
 
# invoking the function again
show_hello()

# tiangle area 

def triangle_area(b, h):
    '''returns the area of the triangle with base b and height h'''
    return 0.5 * b * h

triangle_area(3,6)

# strings

string_1 = "Hello World"
 
print("Using the join method to add a : between every char...\n{0}"
      .format(":".join(string_1)),
      "\n")

print("Using the join method to add a whitespace between every char...\n{0}"
      .format(" ".join(string_1)),
      "\n")

