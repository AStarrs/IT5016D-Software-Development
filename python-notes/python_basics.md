
# Module 2 Python Basics

## Module 2 Part 1: Python Fundamentals

### What is Python?

>Python is an interpreted, object-oriented, high-level programming language with
>dynamic semantics

What can you do with Python?

- Web Development (web frameworks: Pyramid, Django, Flask etc.)
- Data Analysis (has exelent libraries: NumPy and Pandas; libraries for visualisation: Matplotlib and Seaborn)
- Machine Learning (libraries inmplementing machine learning algorithms: Scikit-Learn, NLTK and TensorFlow)
- Computer Vision (Face detection, color detection while using Opencv and Python)
- Raspberry Pi
- Game Development (Create video games using module Pygame)
- Web Scraping (if you need to grab data from a website but the site does not have an API to expose data, you can use Python to scraping data)
- Writing Scripts (to automate repetitive stuff)
- browser Automation (Perform some neat things such as opening a browser and posting a Facebook status, do it with Selenium with Python)
- GUI Development (build GUI app using Python modules Tkinter, PyQt to support it)

### Python Standard Library

The Python Standard Library contains over 80,000 definitions that can be used in coding and is built into the Python application. In essence, the Standard Library contains definitions within modules and built-in functions as prewritten sequences of code.

Each pre-written sequence represents a small action which you will need to build
your program.

#### Built-In Functions 

A list of all built-in functions found in the Python Standard Library.
Think of these functions as key pre-made coding actions that are already
preloaded to use, without having to find them in the library.

### Python Language Reference

Just like in language, programming languages have semantic and syntax rules for
how the coding should be written.

#### Semantics

Semantics are about creating meaning with the language you are using. 

#### Syntax 

Syntax are about the structure of the language to create meaning. 

#### The Python Language Reference

The Python Language Reference contains all the syntax and core semantics of the
Python language that you need as a programmer. This is a critical reference
resource that will be referred to as you learn the semantics and syntax of this
language. 

### Interactive Mode Programming

Interactive Development Environments (IDE's) provide facilities for software development. They basically make the job of programming easier by including features such as:

- Source code editor
- Debugger
- Code completion
- Compiler
- Interpreter

IDE called `IDLE`. This stands for Integrated Development Environment or
Integrated Development and Learning Environment.

#### Python Shell 

Python shell displays the version of Python that you are using, along with other information and ends with the Python command line prompt (">>>").

Here in Python Shell, you are in the interpreter space where you can start typing straight away to generate your code for the programs we are going to create.

This is also called Interactive Model Programming. 

#### Interactive Mode Programming

The Python interpreter can be called (or invoked) by typing source code directly into the Python Shell.

To execute the code, the user simply hits 'enter'. The code that is typed in is not necessarily saved.

Previously run statements are saved in the computer memory but only for as long as the Python Shell is open.

When the shell is closed, all the statements are lost. This is called
Interactive Mode Programming.

#### The Python REPL

In Python, the command line environment, that is, the Python Shell you are looking at right now, is sometimes referred to as the REPL.

Python will:

- Read whatever the user types in at the command prompt,
- Evaluate it,
- Print it and then
- Loop back to the beginning - hence the term REPL.
  
When the text input is evaluated, the Python interpreter tries to execute it. If the input is valid then a command is executed on the CPU. Otherwise, a red error message is printed on the screen.

The triple arrow prompt (>>>) tells you that Python is waiting for you to type
something. Within an interactive Python session, you can enter fragments of
Python programs and see instant results.

## Module 2 Part 2: Data Types

### Introduction to Data Types

### Numeric Types

`Integers (int)` (For example -3,-2,-1, 0, 1, 2, 3)

Any whole number is an integer.

When working with the int type, you have access to a number of interesting features. One feature is the ability to use different numeric bases e.g.,

Base 2: Uses only 0 and 1 as numbers.
Base 8: Uses the numbers 0 to 7.
Base 10: Uses the usual numeric system.
Base 16: Is also called hex and uses the numbers 0 to 9 and the letters A to F
to create 16 different possible values.

`Floating-Point Values (float)` (for example 12.245)

Any number that includes a decimal portion is a floating-point value.

`Complex Numbers` (for example 5+4x)
A complex number consists of a real number and an imaginary number paired together. Real-world uses for complex numbers include:

Electrical engineering
Fluid dynamics
Quantum mechanics
Computer graphics
Dynamic systems

### String Types (str)

my_string = "Aoteroa - The Land of the Long Cloud."

It’s possible to convert any single letter to its numeric equivalent using the
`ord()` command. Sometimes you need to convert a string to a number. int() &
float()

### Boolean Types (bool)

When using Boolean value in Python, you rely on the bool type. A variable of
this type can contain only two values: True or False. 

You can assign a value by using the True or False keywords, or you can create an
expression that defines a logical idea that equates to true or false.

Boolean values are used for:

* Determining a variable type
* Setting 'flags' in a program. Examples of boolean flags include: is_running and is_alive
* Determining the flow control in programs, i.e. deciding which branch of instructions to execute, which is key to programming.

# BoolTests.py
#
# author: A. N. Other
# date: September 2016
 
print ("Test 1 ", bool(True))
print ("Test 2 ", bool(False))
print ("Test 3 ", bool("text"))
print ("Test 4 ", bool(""))
print ("Test 5 ", bool(" "))
print ("Test 6 ", bool(0))
print ("Test 7 ", bool())
print ("Test 8 ", bool(3))
print ("Test 9 ", bool(None))


Test 1  True
Test 2  False
Test 3  True
Test 4  False
Test 5  True
Test 6  False
Test 7  False
Test 8  True
Test 9  False

Notice that the bool operation returns False for Test 4 (containing an empty
string ""), but then True for Test 5 which contains a string of white space "
". Another point worth mentioning is that any integer returns True, but the
number zero returns False. Understanding this use of the boolean function is
very important. It will help make your programs more concise, and prevent you
from creating hard to find bugs later on.

### Casting

In coding you can change a variable from one data type to another data type - this is called casting. 

You can convert numbers to a string as well by using the str( ) command.

Casting functions:

`float(x)` returns floating point value

`int(x)` returns integer

`str(x)` returns string

### Primitive and Reference Types

`Primitive` types are the basic types of data. They possess a value that takes up a certain amount of allocated memory. They cannot be decomposed into simpler parts.

A primitive value is stored in a memory location, therefore, it always has a value.

If the primitive is of a numeric type, e.g. short, int etc., then that value could be zero, since zero is considered a value. 

Remember: a primitive type always has a value.

In Python, primitive types  include:

* int
* float
* boolean
* char

You can use variables to store primitive values and these variables will therefore always have a value.

The variable can never be Null.

`Reference` Types

Objects, by contrast, are considered reference types and these are covered later in the module.

A key difference is that reference types of data refer to a primitive type of data and by doing so, will not take up memory space as it has no value.

Examples include:

* String
* Dictionary
* List
* Tuple

A good clue for identifying reference types is that most reference types are collections of primitive types.

For example, the dictionary, list and tuple are all types of collection. String still follows this rule, although it is not obvious.

You can think of a string as a pointer to a collection of characters. 
A reference type is a pointer to a memory location.
If the pointer is not set, then the type value is Null (or None in Python)

#### Uses

A developer must know the difference between primitives and reference types for their program languages. There are some important differences which include:

* Reference type values can be null or none. Primitives always have a value
* Using variables by reference or by value will result in different outputs
* Reference types are immutable; they cannot be changed. The pointer can be bound to a new memory location but the old memory location still holds

### Getting String Input From The User

Python uses the input statement to return a string from the user. 

```
print ("Welcome to your first data entry program\n")
user_name = input("Please enter your name...\n")
user_yob = int(input("Please enter your year of birth...\n"))
 
print("Thank you for your input\n")
print("The name that you entered is ", user_name)
print("Your age in years is ", 2016 - user_yob)
```

Since the Python input statement returns a string, this value needs to be cast to integer.

To do this, the input statement is nested in int( ). This casts the string value
to an integer.

The point to note about casting in Python is that sometimes data can be lost.

For example, it is possible to cast the integer 6 to float 6.0 The reverse case is possible in Python but the fractional part will be lost.

If you tried to convert say, float 6.3 to int, then this would return just 6
since the 0.3 cannot be represented in an integer.

Handling User Input Errors
Most often the user of an application will enter invalid data.

In the example below, if the user entered string value of "six" the application would throw an error and terminate.

A programmer must anticipate all user errors to create an application that
cannot fail.

### Date and Time

Python uses the calendar, datetime and time modules to represent dates and times.

We can create our own duration using timedelta.

An example is timedelta(days=10). This defines a duration of 10 days. We can do the same for hours, minutes and seconds.

Why can't we do it for years?

Answer:
We cannot use time delta to create a duration in years because of leap years in the calendar. A duration may span any number of leap years dependant on the start time and the duration length.

### Mastering Printing with Numbers

## Module 2 Part 3: Number Bases

### Introduction to Number Bases

`Binary`

Computers understand only 2 things: power on, or power off. This is represented by very small switches, billions of which are found in every modern electronic device. The position of a switch can be represented by:

Power on = 1

Power off = 0

The storage units for binary are shown below.

1 bit = a single 0 or 1
1 byte = 8 bits = 1 character of text
(A nibble = 4 bits or half a byte)
1 KB = 1024 bytes
1 MB = 1024 KB or 1024x1024 bytes
1 GB = 1024 MB 
1 TB = 1024 GB

Notice that the units are not based on 10 but are in fact based on 2. This is
because binary uses base 2. This is represented by the table below:

| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |

Binary Conversion

Say that the binary number 101001 needs to be converted to normal (denary)
numbering. The number can be written into the binary table.

Conversion is easy. Simply multiply out each placeholder with its corresponding
value, then sum everything.

For example 

32x1 + 16x0 + 8x1 + 4x0 + 2x0 + 1x1 = 41

The answer, in this case, is 41.

f the calculation needs to be checked a reverse operation can be done instead.

For example 

The steps for this are:

Parse an empty binary table, the largest placeholder that can fit in 41 is
placeholder 32.

Since 32 is used, we write a 1 underneath it. The remainder from 41 - 32 is 9.

Parse the binary table from left to right starting at 32 and try to fit the
remainder into the placeholders.

Placeholder 16 is too big to take remainder of 9, so we write a 0 underneath it.

Placeholder 8 can fit 9, so we write a 1 underneath it. The remainder from 9 - 8
is 1.

Placeholders 4 and 2 are too big for 1, so we write a 0 underneath both.

The remainder of 1 fits into the last placeholder so we write a 1.


### Module 2 Part 4 Expressions and Statements

#### Introduction to Numeric Operators

`+` addition

`-` subtraction

`*` multiplication

`/` division true

`//` division integer

`%` modulus

##### Python shortcuts

`*=`    `x*=5`    `x=x*5`

`/=`    `x/=5`    `x=x/5`

`%=`    `x%=5`    `x=x%5`

`+=`    `x+=5`    `x=x+5`

`-=`    `x-=5`    `x=x-5`

#### If Statements

The If statement uses boolean conditional operations to create a branch in the program. If a condition is met, then some action is taken, otherwise, the interpreter skips the action and moves on to the next code block. 

The `If` statement on its own produces a single branch of execution, but only if the condition is met. The `else`: statement is optional. `If with Else` should be used to produce "either" and "or" branches of execution.

```
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
```

