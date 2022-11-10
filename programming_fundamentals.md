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