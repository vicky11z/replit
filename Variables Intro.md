[This Lesson is taken from Real Python Website](https://realpython.com/python-variables/)

### Variable Assignment
Think of a variable as a name attached to a particular object. In Python, variables need not be declared or defined in advance, as is the case in many other programming languages. To create a variable, you just assign it a value and then start using it. Assignment is done with a single equals sign (=):

>>> n = 300
This is read or interpreted as “n is assigned the value 300.” Once this is done, n can be used in a statement or expression, and its value will be substituted:

>>> print(n)
300
Just as a literal value can be displayed directly from the interpreter prompt in a REPL session without the need for print(), so can a variable:

>>> n
300
Later, if you change the value of n and use it again, the new value will be substituted instead:

>>> n = 1000
>>> print(n)
1000
>>> n
1000
Python also allows chained assignment, which makes it possible to assign the same value to several variables simultaneously:

>>> a = b = c = 300
>>> print(a, b, c)
300 300 300
The chained assignment above assigns 300 to the variables a, b, and c simultaneously.

### Variable Types in Python
In many programming languages, variables are statically typed. That means a variable is initially declared to have a specific data type, and any value assigned to it during its lifetime must always have that type.

Variables in Python are not subject to this restriction. In Python, a variable may be assigned a value of one type and then later re-assigned a value of a different type:

>>> var = 23.5
>>> print(var)
23.5

>>> var = "Now I'm a string"
>>> print(var)
Now I'm a string


### Variable Names
The examples you have seen so far have used short, terse variable names like m and n. But variable names can be more verbose. In fact, it is usually beneficial if they are because it makes the purpose of the variable more evident at first glance.

Officially, variable names in Python can be any length and can consist of uppercase and lowercase letters (A-Z, a-z), digits (0-9), and the underscore character (_). An additional restriction is that, although a variable name can contain digits, the first character of a variable name cannot be a digit.

Note: One of the additions to Python 3 was full Unicode support, which allows for Unicode characters in a variable name as well. You will learn about Unicode in greater depth in a future tutorial.

For example, all of the following are valid variable names:

>>> name = "Bob"
>>> Age = 54
>>> has_W2 = True
>>> print(name, Age, has_W2)
Bob 54 True
But this one is not, because a variable name can’t begin with a digit:

>>> 1099_filed = False
SyntaxError: invalid token
Note that case is significant. Lowercase and uppercase letters are not the same. Use of the underscore character is significant as well. Each of the following defines a different variable:

>>> age = 1
>>> Age = 2
>>> aGe = 3
>>> AGE = 4
>>> a_g_e = 5
>>> _age = 6
>>> age_ = 7
>>> _AGE_ = 8

>>> print(age, Age, aGe, AGE, a_g_e, _age, age_, _AGE_)
1 2 3 4 5 6 7 8
There is nothing stopping you from creating two different variables in the same program called age and Age, or for that matter agE. But it is probably ill-advised. It would certainly be likely to confuse anyone trying to read your code, and even you yourself, after you’d been away from it awhile.

It is worthwhile to give a variable a name that is descriptive enough to make clear what it is being used for. For example, suppose you are tallying the number of people who have graduated college. You could conceivably choose any of the following:

>>> numberofcollegegraduates = 2500
>>> NUMBEROFCOLLEGEGRADUATES = 2500
>>> numberOfCollegeGraduates = 2500
>>> NumberOfCollegeGraduates = 2500
>>> number_of_college_graduates = 2500

>>> print(numberofcollegegraduates, NUMBEROFCOLLEGEGRADUATES,
... numberOfCollegeGraduates, NumberOfCollegeGraduates,
... number_of_college_graduates)
2500 2500 2500 2500 2500
All of them are probably better choices than n, or ncg, or the like. At least you can tell from the name what the value of the variable is supposed to represent.

On the other hand, they aren’t all necessarily equally legible. As with many things, it is a matter of personal preference, but most people would find the first two examples, where the letters are all shoved together, to be harder to read, particularly the one in all capital letters. The most commonly used methods of constructing a multi-word variable name are the last three examples:

Camel Case: Second and subsequent words are capitalized, to make word boundaries easier to see. (Presumably, it struck someone at some point that the capital letters strewn throughout the variable name vaguely resemble camel humps.)
Example: numberOfCollegeGraduates
Pascal Case: Identical to Camel Case, except the first word is also capitalized.
Example: NumberOfCollegeGraduates
Snake Case: Words are separated by underscores.
Example: number_of_college_graduates
Programmers debate hotly, with surprising fervor, which of these is preferable. Decent arguments can be made for all of them. Use whichever of the three is most visually appealing to you. Pick one and use it consistently.

You will see later that variables aren’t the only things that can be given names. You can also name functions, classes, modules, and so on. The rules that apply to variable names also apply to identifiers, the more general term for names given to program objects.

The Style Guide for Python Code, also known as PEP 8, contains Naming Conventions that list suggested standards for names of different object types. PEP 8 includes the following recommendations:

Snake Case should be used for functions and variable names.
Pascal Case should be used for class names. (PEP 8 refers to this as the “CapWords” convention.)

