## Strings

A `string` is just a list of characters in any order and a character is anything that can be typed on a keyboard in one keystroke, such as, a letter, number or backslash.

An `empty string` is one that contains no characters at all. This is different to a null string, that is, a string that has not been set to any value.

Python can recognise a string by anything that is delimited by quotation marks or double quotation marks.

### Searching Strings

```
string_1 = "Whanau!"
 
print("The third letter is {0}\n".format(string_1[2]))
print("The length of the string is {0}".format(len(string_1)))
```

Python contains the count, find and index functions to help you search a string. 

```
string_1 = "here is a translation: Haera mai ki konei means come here!"
 
print("The number of times that k appears is {0}\n"
      .format(string_1.count("k")))
 
konei_endindex = string_1.find("konei") + len("konei")
print("The end index position of konei is {0}\n"
      .format(konei_endindex))
 
here_position = string_1.find("here", konei_endindex, len(string_1))
print("Looking for the string_1 here, anytime after konei...\n\n"
      "The string_1 here appears at index position..{0}"
      .format(here_position))
```

`Find( )` is a very useful means for searching strings. It returns the index integer of the item being searched for. If the function cannot find a matching string, then it returns -1. 

The find( ) syntax is:

```
<string being searched>.find(<string to search for>, <start index>, <end index>)
```

The start and end index parameters are optional. This lets us write code to search through just part of a string.

"find( ) only returns the first instance of the item being searched for. Any duplicates will be ignored."

To find all instances of a search term, the calling code must use a loop.

```
 
string_1 = "Ka mate kāinga tahi ka ora kāinga rua."
 
print("Does this string start with Ka?....{0}\n".format(string_1.startswith("Ka")))
 
print("Does this string start with Tr?....{0}\n".format(string_1.startswith("Tr")))
 
print("Does this string end with rua?....{0}\n".format(string_1.endswith("rua.")))
```

The starts with and ends with functions return boolean. Other functions used with strings include:

```
string_1.isalnum()         #check if all char are alphanumeric 
string_1.isalpha()         #check if all char in the string are alphabetic
string_1.isdigit()         #test if string contains digits
string_1.istitle()         #test if string contains title words
string_1.isupper()         #test if string contains upper case
string_1.islower()         #test if string contains lower case
string_1.isspace()         #test if string contains spaces
```

#### Programmer's Best Practice Tips
* Use the `find( )` function to search a string. This will return a value of minus 1 for a search that returns nothing.
* If a string variable is not set in your program, then remember to use null checking before calling the function.
 
### Editing Strings 

#### Replacing part of a string with a new variable value
```
string_1 = "Hello World"
 
 replacing part of a string
print("Replacing part of a string...\n{0}"
      .format(string_1.replace("Hello", "Goodbye")),
      "\n")
 
#Changing Upper and Lower Case Strings
string_1 = "hElLo wOrlD"
print("Making a string upper case...\n{0}"
      .format(string_1.upper()),
      "\n")
 
print("Making a string lower case...\n{0}"
      .format(string_1.lower()),
      "\n")
 
print("Making a string title case...\n{0}"
      .format(string_1.title()),
      "\n")
 
print("Making a string capitalised...\n{0}"
      .format(string_1.capitalize()),
      "\n")
 
print("Making a string swap case...\n{0}"
      .format(string_1.swapcase()),
      "\n")
 
print("Reversing and inserting characters to a string...\n{0}"
      .format("*".join(reversed(string_1))),
      "\n")
```

#### Removing content from a String 

Python strings have the `strip()`, `lstrip()`, `rstrip()` methods for removing any character from both ends of a string.

If the characters to be removed are not specified then white-space will be removed.

`strip()`     removes from both ends
`lstrip()`    removes leading characters (Left-strip)
`rstrip()`    removes trailing characters (Right-strip)

#### Concatenation 
combining two or more strings into a single string

To concatenate strings in Python use the "+" operator.

"Hello " + "World" = "Hello World"

"Hello " + "World" + "!" = "Hello World!"

```
string_1 = "Hello World"
 
print("Using the join method to add a : between every char...\n{0}"
      .format(":".join(string_1)),
      "\n")
 
print("Using the join method to add a whitespace between every char...\n{0}"
      .format(" ".join(string_1)),
      "\n")
```

#### Replacing part of a string 

Goodbye World

Python has `replace()` method that replaces each matching occurrence of the old  character/text in the string with the new character/text.

The replace() method can take maximum of 3 parameters:

* old - old substring you want to replace
* new - new substring which will replace the old substring
* count (optional) - the number of times you want to replace the old substring with the new substring

string_1 = "Hello World"

print ('Replacing Hello with GoodBye')

print (string_1.replace('Hello','GoodBye'))

#### Reversing and inserting characters to a string

#### Splitting Strings

`split()` 

The simplest use of the split function takes no arguments and splits a string on white spaces, to return a list of strings.

White space is the default delimiter. split( ) also has an optional single string argument to set the delimiter character/s instead.

string_1 = "It's only after we've lost everything " \
           "that we're free to do anything"
 
splitting the string

print("Splitting the string...\n{0}"
      .format(string_1.split()),
      "\n")
 
splitting the string on the letter e

print("Splitting the string on the letter e...\n{0}"
      .format(string_1.split("e")),
      "\n")

#### Programmer's Best Practice Tips
 

* When searching strings, use the find( ) function (and not the index( ) function) find( ) does not error when a search returns empty. The function returns the value minus 1 instead.
* Use the find( ) function overload to search just part of a string.
* Use the split( ) function and its overloads to split a string into a list of strings.
* Remember that the split( ) function default delimiter is white space, and that delimiter character/s are removed in a split operation.

