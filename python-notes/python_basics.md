## # Module 1 Programming Fundamentals

`IDE` - Itegrated Development Environtment 

`OOP` - Object-oriented programming

Instead of being a list of instructions, programs now act as models of the problems they solve. These instructions are broken into parts based on properties and methods (instructions) that can alter the properties when acting on them. 

Taking this Object-Oriented Programming approach, computer programs became much
more adaptable to their environment. Instead of using a single large executable
block of code, objects communicate with each other by sending messages back and
forth. One of the many advantages to this way of programming is that programs
became easier to understand, because they are written in more natural language.

## Programming language Types

### Low-Level Programming Languages

A low-level programming language is a programming language that provides little or no translation from a computer's instruction set. These are the commands or functions in the language that map closely to the computer processor instructions.

Generally, this refers to either machine code or assembly language. The word "low" refers to the small or non-existent amount of difference between the written language and machine language; because of this, low-level languages are sometimes described as being "close to the hardware". Programs written in low-level languages tend to be relatively non-portable, mainly because of the close relationship between the language and the hardware architecture.

A program written in a low-level language can be made to run very quickly (an equivalent program in a high-level language can be less efficient and use more memory). Low-level languages are simple, but considered difficult to use, due to large amounts of technical detail that the programmer must remember.

#### First Generation Language (1GL)

This is the lowest form of language often referred to as machine code.

Machine code is the only language that a computer can process directly without a previous transformation. It is made up of binary numbers, represented by 1's and 0's.

This makes the language suitable for the understanding of the machine, but far
more difficult to interpret and learn by the human programmer.

- The main advantage of programming in machine code is that the code can run very fast and very efficiently because the instructions are executed directly by the CPU.
- One of the main disadvantages of programming in machine code is that when an error occurs, the code is not as easy to fix.
- Machine-level code is very much adapted to a specific computer and CPU. The code cannot be used on other types of computers and CPUs.
- Machine-level code is still used occasionally by programmers to especially when programming lower-level functions of the system, such as drivers, interfaces with firmware and hardware devices.

#### Second Generation Language (2GL)

Assembly language is one level above machine code. Assembly language is converted into executable machine code by a utility program referred to as an assembler. The conversion process is referred to as assembly, or assembling the source code.

Assembly code maps human readable characters to the binary equivalents of the
machine instruction. This makes the language less difficult to understand
compared with machine code.

- Assembly code contains human readable characters that are converted to machine code by a program called an assembler.
- Every line of assembly code is converted to a single machine code instruction by the assembler.
- Assembly code is slightly easier to work with than machine code, but it is still harder to understand than high-level language code.
- Assembly code is specific to a computer, and its CPU. The code cannot be used on different types of computers and CPUs
  
### High-Level Programming Languages

A high-level programming language uses many natural language elements in its syntax.

It may automate (or even hide entirely) the complex parts of the underlying computer system (e.g. memory management). This makes the process of developing a program simpler and more understandable relative to a lower-level language.

High-level languages are slower at executing code than low-level languages. The
source code must first be either interpreted or compiled (or, in many cases,
both) before being executed on the CPU.

#### Execution modes

Execution modes are basically how the programming language will take action.

There are several execution modes for modern high-level programming languages, and each variation affects how quickly the instructions are acted upon and what they mean to the machine code in different ways.

Very often, the line between them is blurred, resulting in hybrids.

1. Compiled: A compiled programming language uses a program called a compiler to translate all the source code into machine code. The process is called compilation. The resultant machine code can be stored in memory and executed at CPU level at a later time.
Execution time is generally faster than that of interpreted languages since the
machine code can be generated ahead of execution time. There is no overhead of
translation at runtime.

2. Interpreted and Hybrid
When code written in a language is interpreted, the code is read and then executed directly, with no compilation stage.

A program called an interpreter reads each program statement, following the program flow. It then decides what to do, and does it. The program is executed a bit at a time as it is interpreted.

Interpreted languages are slower than compiled programs since the interpreter does its work at runtime.

The definition of compiled and interpreted languages becomes blurred since many
modern languages use both compilers and interpreters. We say that a language is
compiled or interpreted based on the common implementation practice, rather than
as a reference to an essential property of the language.

Many modern programming languages use a hybrid execution mode that uses both a compiler and interpreter. They execute a program in two parts.

1. The source code is compiled into an intermediate language called bytecode. Bytecode is neither source code nor machine code. The bytecode is then either compiled further into machine code
   
2. It is interpreted and executed directly on the CPU. Bytecode has some important features:
- It is `an intermediate language` between source code and machine code
- It is portable, so it can be used on any CPU or computer (provided that the computer has a suitable interpreter or compiler)
- It can be interpreted and run directly on the CPU
- It can be compiled further into machine code

#### Python
In Python, the source code is first compiled into bytecode. The bytecode is then interpreted and executed directly on the CPU.

The second point is an important one. It is an easy way to remember why Python
is considered an `interpreted` language rather than a compiled language.


## Programming Conventions

>There are a multitude of programming languages, therefore, it is important to have and apply common rules, guidelines and approaches regardless of which language you use.

>These are programming conventions and they make it easier for you and others to
>read and maintain your source code, and help to minimise errors.

### Standard libraries

To make a programmer's life easier and quicker, all the conventions used to guide or build our instructions, are usually stored in Standard Libraries.

Every programming software a standard library. 

Definition: A standard library contains definitions for commonly used
algorithms, data structures and functions for input and output.

A standard library is treated as part of the language by its programmers. In
short, the standard library for a language defines the built-in functions and
modules for that language.

Examples of components found in the standard library include:

- subroutines
- variables
- data structures, including different data types
- class definitions
- templates
- methods for interacting with the underlying hardware
- methods for interacting with the operating system

### Language Reference

A language reference functions like a manual to allow developers to understand the basic elements for building a computer program in the chosen language.

The advantage is they can code in the target language quickly, particularly if they know what they want to ask the computer to do.

Language references complement standard libraries by providing information on
the syntax of the language.

#### Syntax

Definition: Syntax is the set of rules that defines how a program will be
written and read, by either the compiler, interpreter or by human readers.

Writing code in a particular language requires knowledge of the language syntax.

Languages generally have different syntax, although sometimes there are
similarities.

#### Standard libraries - Style Guides 

Style guides within the standard library of your chosen programming language are written documents that set out rules or guidelines to follow when writing source code, e.g. how to approach indentation, vertical alignment, spaces, tabs, folder naming, asset naming, etc. This makes it easier for the original programmer and/or others to follow the code and update it later.

Note: Style guides are typically designed around a programming language so what might be best practice for Python may not be appropriate for C#. 

An important feature of Style Guides is comments. Comments are used to provide explanations or annotations about the source code.

For example, you might find some comments at the start of the program to describe what the code does, who wrote it and when.

Comments can also be used to:

Identify particular code blocks: Comments should be used where the code is complex, or where changes have been made.
Disable lines of code for testing: This can be useful when trying to debug code by disabling parts of the code, it makes it easier to find the bug.

Comments are generally ignored by compilers and interpreters. Depending on the programming language used, the syntax of comments can vary considerably.

## Data types

### Seeing Variables as Storage Boxes

When working with applications, you store information (the data) in variables. A variable is a kind of storage box.

- Whenever you want to work with the information, you access it using the
  variable.
- If you have new information you want to store, you put it in a variable.
- Changing information means accessing the variable first and then storing the
  new value in the variable.
- Just as you store things in boxes in the real world, so you store things in
  variables when working with applications.
- Each variable stores just one piece of information.

### Defining and Setting Types

The specific kind of variable is called a data type. Knowing the data type of a variable is important because it tells you what kind of information you find inside.

In addition, when you want to store information in a variable, you need a
variable of the correct data type to do it.

You can generally classify data types as numeric, string, and Boolean, although
there really isn’t any limit on just how you can view them.

#### Numerical data types

Numerical data types represent different ways of number classification

There are two types of group numbers: 

- whole numbers
- Decimal numbers

Defference between then is the range of numerical values that the data type can
store

There are also `Signed` and `Unsigned` numerical data types, that affects a
specific range of values that the given data type contains

`Signed` containes

- positive and negative values
- Ex. 16-bit short range: -32,768 to 32,767

`Unsigned` containes:

- only positive values
- Doubles the positive range Ex. 16-bit short range: 0 to 65,535

#### Booleans 

true (1) or false (0)

#### Characters

single pieses of letters

#### Primitive types

- int
- doubles 
- longs
- floats
- shorts
- boolean 
- chars

This types have a fixed size that don't depend on the data inside of them. 64
Bits

One int or one character

#### Data structures

made up of pieses of data and have a specialized way and format of  organizing
and storing these pieces.

Data structures help to connect and group data

Data structures give us organization, storage and access nad work with the data
in the efficient manner

#### Strings

A string is a sequence of characters.

it's a data type that's build out of another data type

Ex. name, tytle of book, sentence

#### Primitive vs. reference types in memory

Primitive types (variableName-> data):

- int 
- boolean
- character
- float
- double
- short
- long

Referenced Types (variableName -> memoryAddres -> value):

- strings 
- data structures


Istead ofstoring the entire data structure directly in a set of consecutive
bits, we will create an address that will point to where the structure, or some
part of the structure is in memory. Since we use  a reference to where the data
lives in memory we call strings and other data types implemented with data
structures `reference types` 

Reference types reference their specific value from an address of where the item
stored, rather than direct access to the data itself

```
1. Numerical data type - represent different ways of number classification. Using numerical data types allows to do manipulations with numbers (multiply, subtract and so on). 

2. Boolean data type - has only two values: true or false, used to perform logical operations where only two options available. Thus, this data type limited by condition whether asking question True or False, but could be convenient fo some specific tasks.

3.
```

## Flow Charts

`A flowchart` is a simple diagram that illustrates the stages or steps the
computer must complete to solve the problem.

## Sequence, Condition and Iteration Constructs

### The three main programming actions used are easily represented as flow chart sequences 

All flowcharts are typically constructs of sequence, condition (selections) and
iteration (loops).

#### Sequence

The sequence is represented by the flow-lines connecting the shapes.

Start at the “Start” sign (oval) and follow the flow-line until you reach a shape with an instruction in it.
After carrying out the instruction you flow to the next one.
The flow-lines are normally followed from top to bottom and from left to right.
However, if arrows are included on a flow-line, then the flow-line is followed
in the direction of the arrow.

#### Condition (selection)

Condition is represented by the diamond shape with two paths leaving it.
The decision in the diamond has a Yes/No answer, and the corresponding flow-line
is followed depending on the answer to the question.

#### Iteration (Loop)

Iteration is represented by a decision diamond that has one of the exit paths returning to a point higher in the flowchart.
This return path is called a loop.
The question inside the diamond is called the loop control condition.
There are two main types of flowchart iteration loops, which for convenience, will be referred to as Type A and Type B.

The Type A loop always executes the statements in the loop at least once. This is because the loop control condition is evaluated at the end of the loop, and the instructions in the body of the loop will have already been executed before then. It corresponds to the pseudocode form Repeat … Until. It can be referred to as a Trailing Decision Loop.

The Type B loop may not execute the loop instructions even once. This is because
the loop control condition comes before the execution of the loop instructions,
and a false result at the beginning would mean that the body of the loop is
bypassed. This type corresponds to the pseudocode form While. It can be referred
to as a Leading Decision Loop.


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

