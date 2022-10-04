# IT5016D-Software-Development
Notes and exercises for Software Development paper

## Python 

### Module 2 Part 3 Number bases

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

