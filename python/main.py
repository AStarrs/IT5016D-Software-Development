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

