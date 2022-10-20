## This is a test of another md file in python folder

## Lists 

The Python list is a data type.

It is a container that holds a number of other objects, in a given order.

L = ["A", "B", "C"]

L = list()

`len(L)` returns the number of items in the list

`L[i]` returns the item at index i

`L[i:j]` returns a new list, containing the objects between i and j

### List Index and Negative index

You can use the index operator [ ] to access an item in a list. Index starts
from 0. And goes from left to right 0, 1, 2, 3, 4...

Negative index starts from the end of the list

-1 is the last item in the list

# empty list
my_list = []
# list of integers
my_list = [1, 2, 3]
# list with mixed datatypes
my_list = [1, "Hello", 3.4]
# nested list
my_list = ["mouse", [8, 4, 6]]

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

### To add to a list

primes.append(17)

primes

[1, 2, 3, 5, 7, 11, 13, 17]

#### Slicing the list

primes[2:5]

new list from index 2 to 5

the beginning value is included, but the ending value is not included

#### combining 2 lists together - Concatenation

letters = ['a', 'b', 'c']

numbers = [1, 2, 3]

letters + numbers

['a', 'b', 'c', 1, 2, 3]

#### Methods

dir(numbers)

### Iterating lists

Iterating is a means to loop through a list. The for-in structure is used
specifically to iterate through the collection of items, List being one of those
collection types.

sample_list = [1, 4, 5, 2, 9, 12]
 ```
for item in sample_list:
    print("An item in the sample list is ", item)
 ```
# If you need both the index and the item, use the enumerate function:
```
for index, item in enumerate(sample_list):
    print ("The element index is ",index," and the value is ", item)
 ```
# If you need only the index, use range and len:
```
for index in range(len(sample_list)):
    print ("The element index is ",index)
 ```
# The list object supports the iterator protocol. To explicitly
# create an iterator, use the built-in iter function:
 ```
i = iter(sample_list)
item = i.__next__() # fetch first value
print("An item in the sample list is ", item)
item = i.__next__() # fetch second value
print("An item in the sample list is ", item)
``` 
# Python provides various shortcuts for common list operations. For example,
# if a list contains numbers, the built-in sum function gives you the sum:
``` 
list_sum = sum(sample_list)
print("\nThe sum of the items in the list is.... ", list_sum)
 
subtotal = 23
total = sum(sample_list, subtotal)
print("\nThe sum of the items in the list and another number is.... ", total)
 
average = float(sum(sample_list)) / len(sample_list)
print("\nThe average of the items in the list is.... ", average)
 ```
# If a list contains strings, you can combine the string into
# a single long string using the join string method:

 ```
haka_list = ["Taringa","whakarongo!","Kia","rite!","Kia","rite!"]
joined_list = " ".join(haka_list)
print("\nThe joined list is....", joined_list)
```
 
### List Methods for Changing lists

`list.append(elem)`
Adds a single element to the end of the list. Common error: does not return the new list, just modifies the original.

`list_1.extend(list_2)`
Appends all of list_2 elements to the end of list_1.

`list.insert(index, elem)` 
Inserts the element at the given index, shifting elements to the right.

`list.index(elem)`
Searches for the given element from the start of the list and returns its index.
Throws a ValueError if the element does not appear (use "in" to check without a
ValueError - see below).

`list.remove(elem)`
Searches for the first instance of the given element and removes it (throws ValueError if not present)

`list.sort()`
Sorts the list in place (does not return it)

`list.reverse()`
Reverses the list in place (does not return it)

`list.pop(index)`
Removes and returns the element at the given index. Returns the rightmost element if index is omitted (roughly the opposite of append()).

`if value in L`: 
A boolean check to find out if a value exists in the list L


### Programmers Best Practice Tips

- Use `i, j and k` as variables in from statements. This is a coding convention recognised by experienced developers
- Use the `from` statement to iterate a list
- Use the `from element in list:` syntax to search for an item in a list. This approach avoids the error that might occur if the item being searched for doesn't exist in the list
- Use `list_name.append(item)` to add an item to the end of the list
- Use the `pop()` method to remove an item at the given index. This method returns the item being removed. It is a useful method, since it simulates the removal of something from a collection
- Use the `pop()` method to remove and return the last item if index is not provided. This helps us implement lists as stacks (first in, last out data structure)
- Use `list.count(item)` to return the number of elements that are equal to item
- Use the built-in `sort()` and `reverse()` methods to do sorting


## Tuples

A tuple is an immutable sequence of Python objects. Immutable means that the sequence cannot be changed. 

 There are a few cases where tuples are appropriate:

- Tuples perform faster than lists
- Tuples immutability makes them ideal for creating constants since they can't change. Using tuples can add a level of safety to your code. 

## Dictionaries 

 A dictionary is a collection, but it uses different syntax and semantics from
 other collection types. A single dictionary item consists of 2 parts separated
 by a colon. The first part is the dictionary key. The key is unique, so items
 from the same dictionary must have different keys. The second part is the item
 value. This can be of any type, but the key must be of an immutable data type
 such as string, number, or tuple. Dictionary items are separated by commas, and
 the whole dictionary is enclosed in curly braces. An empty dictionary without
 any items is written with just two curly braces, like this: `dictionary_1 = {}`
 
 Points to remember about dictionaries:

- Dictionaries use keys to access individual dictionary items and their values
- Dictionary items are unordered, unlike other containers. Syntactically dictionary items are written one after the other and are separated by commas. However, the items are not stored in any order 
- Dictionaries item keys must be of any immutable type
- Dictionary item values can be of any type
- Dictionaries cannot always be sorted. This depends on the types of the keys and values. Since some types, such as objects, have no obvious numeric value, sorting may not be possible.
- Dictionaries themselves are mutable. Items can be added or deleted. The dictionary itself can be emptied of all items.

### Programmer's Best Practice Tips
- Avoid creating infinite loops. These can cause a program to stall. Infinite loops are also difficult to test.
- Use i, j and k as variables in from statements. This is a coding convention recognised by experienced developers
- Use the "from element in list:" syntax to search for an item in a list. This approach avoids the error that might occur if the item being searched for doesn't exist in the list
- Use lists for most applications. Remember that tuples are immutable, and should only be used where the requirement is for a collection to be unchangeable
- Always write container elements on new lines. This makes the code easier to read.