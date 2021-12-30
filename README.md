## Variables and Printing

In this section we will learn about python variables and how to display them using the print function.

### Getting Started
The details of what to type into the console are in the respective DoNow and Lab files. If you want to execute them in the main program the instructions are below.

In short expressions on the command line execute as you think they would 

```python
print(2*3*5)
```
prints 30

And variables are very similar to how they were in Snap! They are addresses that we can put values into.


```python
city = "San Francisco"
print(city)
```
Prints San Francisco

### Running through main.py

The DoNow page shows various expressions that you can type into the console. Lines that are indented in the DoNow function will execute when the main program is run. For instance the following function will run in main:

```python
def theNow():
  print(2*3*5)
```

because in the main we have

```python
from DoNow import theNow

theNow()
```

If we don't want to execute the DoNow we can comment it out

```python
from DoNow import theNow

#theNow()
```

Likewise parts from the lab can be imported and executed

```python
from Lab import part1, challenge

part1()
challenge()
```