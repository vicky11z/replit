# Lesson 1.05: Debugging



## Learning Objectives

Students will be able to...

* Define and identify: **interpreter, string, integer, float, value, errors, console, expression**
* Use the Python interpreter to evaluate simple math expressions
* Distinguish between an integer, float, and string
* Navigate the files in our lesson.


## Materials
 We have the following files.

 | **Duration**   | **Description**    |
| ---------- | -------------- |
| [Do Now](#DoNow.md) |  Our usual warm up.         |
|  Read Me | This document |
| [Class Norms](#ClassNorms.md) | Our class norms          |

They can be acessed by clicking on the [files menu.](#FilesNav.png)

Files that end in **md** are "markdown files" which is a shorthand way of making web pages.

Files that end in **py** are "python files". If you click the run button main.py will execute. You don't need to do this for the lab.

## Most Common Debugging technique

The print statement.

## The next most Common

The breakpoint

## The Three Types of Errors
[From](http://bwagner.org/ibhl1/csregular/unit07_math/notes/02_errors.html)

### Syntax Errors
Syntax errors, occur when we violate a syntax rule, no matter how minor. These errors are detected at compile time. For instance, if a semicolon is missing at the end of a statement or if a variable is used before it is declared, the compiler is unable to translate the program into byte code. The good news is that when the Java compiler finds a syntax error, it prints an error message, and we can make the needed correction. The bad news is that the error messages are often quite cryptic. Knowing that there is a syntax error at a particular point in a program, however, is usually a sufficient clue for finding the error.

### Run-time Errors
Run-time errors occur when we ask the computer do something that it considers illegal, such as dividing by 0. For example, suppose that the symbols x and y are variables. Then the expression x/y is syntactically correct, so the compiler does not complain. However, when the expression is evaluated during execution of the program, the meaning of the expression depends on the values contained in the variables. If the variable y has the value 0, then the expression cannot be evaluated. The good news is that the Java run-time environment will print a message telling us the nature of the error and where it was encountered. Once again, the bad news is that the error message might be hard to understand.

### Logic Errors
Logic errors (also called design errors or bugs) occur when we fail to express ourselves accurately. For instance, in every day life, we might give someone the instruction to turn left when what we really meant to say is to turn right. In this example

The instruction is phrased properly, and thus syntax is correct.
The instruction is meaningful, and thus the semantics are valid(not run-time error).
But the instruction does not do what we intended, and thus it is logically incorrect.
The bad news is that programming environments do not detect logic errors automatically. The good news is that there are strategies you can use to prevent logic errors and detect them when they occur.



## Common Python Error Messages

In [python](https://runestone.academy/runestone/books/published/thinkcspy/Debugging/KnowyourerrorMessages.html), We can get a few different errors

### IndentError
You are either indented too much or too little.

### ParseError
Parse errors happen when you make an error in the syntax of your program. Syntax errors are like making grammatical errors in writing. If you don’t use periods and commas in your writing then you are making it hard for other readers to figure out what you are trying to say. Similarly Python has certain grammatical rules that must be followed or else Python can’t figure out what you are trying to say.

Usually ParseErrors can be traced back to missing punctuation characters, such as parentheses, quotation marks, or commas. Remember that in Python commas are used to separate parameters to functions. Paretheses must be balanced, or else Python thinks that you are trying to include everything that follows as a parameter to some function.

Here are a couple examples of Parse errors in the example program we have been using. See if you can figure out what caused them.

```python
current_time_str = input("What is the current time (in hours 0-23)?")
wait_time_str = input("How many hours do you want to wait")

current_time_int = int(current_time_str)
wait_time_int = int(wait_time_int)

final_time_int = current_time_int + wait_time_int
print(final_time_int)


time_int + wait_time_int
print(final_time_int)
```


### TypeError
TypeErrors occur when you you try to combine two objects that are not compatible. For example you try to add together an integer and a string. Usually type errors can be isolated to lines that are using mathematical operators, and usually the line number given by the error message is an accurate indication of the line.

Here’s an example of a type error created by a Polish learner. See if you can find and fix the error.

```python
a = input('wpisz godzine')
x = input('wpisz liczbe godzin')
int(x)
int(a)
h = x // 24
s = x % 24
print (h, s)
a = a + s
print ('godzina teraz', a)
```
​
###  NameError
Name errors almost always mean that you have used a variable before it has a value. Often NameErrors are simply caused by typos in your code. They can be hard to spot if you don’t have a good eye for catching spelling mistakes. Other times you may simply mis-remember the name of a variable or even a function you want to call. You have seen one example of a NameError at the beginning of this section. Here is another one. See if you can get this program to run successfully:

```python
a = input('wpisz godzine')
x = input('wpisz liczbe godzin')
int(x)
int(a)
h = x // 24
s = x % 24
print (h, s)
a = a + s
print ('godzina teraz', a)
```


## Addtional Resources

* [Repl.it documentation] (https://docs.repl.it/misc/quick-start)
*  [Operators and Expressions](https://realpython.com/python-operators-expressions/)

This prints out the local variables
```python
for x in ([k + " " + str(type(v)) +" : " + str(v) + "\n" for k,v in locals().items() if k[0] != "_"]):
  print(x)
```

This creates a breakpoint and it puts you into pdb
```python
breakpoint()
```

from a breakpoint you can list lines. and print values

## Pacing Guide


#### Day 1 
| **Duration**   | **Description**    |
| ---------- | -------------- |
| 5 Minutes | Welcome and Review |
|25 Minutes | Quiz |
| 25 Minutes | Debugging Activity |




## Resources

* [Using the debugger](https://blog.repl.it/python-debugger)
* [Associated Reading - section 1.1](https://tealsk12.github.io/2nd-semester-introduction-to-computer-science/readings.md#associatedreadings/1.1)
* [pdb commands](https://web.stanford.edu/class/physics91si/2013/handouts/Pdb_Commands.pdf)
