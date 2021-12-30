# Lab 2.06 - Tic-Tac-Toe Revisited

## 1. In this file

### Predict what will be printed then type the program in your console to confirm.

### Example 1

```python
    a = 0
    while a < 10:
        print(a)
```
Predicted:
Actual:
What (if anything) differed from your prediction?: 

### Example 2

```python
    a = 0
    while a < 10:
        a = a + 1
        print(a)
```
Predicted:
Actual:
What (if anything) differed from your prediction?: 

### Example 3

```python
    a = 0
    while a < 10:
        print(a)
        a = a + 1
```
Predicted:
Actual:
What (if anything) differed from your prediction?: 

## 2. In this file

### Switch driver and navigator. Then, predict what will happen in the following cases.
> **When testing this out, copy and paste the code into main.py & click run, don't use the console.**

```python
    a = input("Would you like to quit: ")
    while a != "y" and a != "n" :
        a = input("Would you like to quit: ")
```
a) If you type "y" in response to the first input.
Predicted:
Actual:
What (if anything) differed from your prediction?: 

b) If you type "n" in response to the first input.
Predicted:
Actual:
What (if anything) differed from your prediction?: 

c) How would you get this program to result in an infinite loop?

d) How would you get this program to print "Would you like to quit: " 5 times?


## 3. In main.py, implement a simplified Tic Tac Toe game using a while loop.
### Requirements
* Allow users to keep playing up to 9 turns.
* Use variables to decide whose turn it is, and set them as `Xs` or `Os`.
* User picks a location on the board according to the number:

![tic-tac-toe](https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRrA_MowUM-KZXl1CpkrQhi8W505dM3cxZG1787i9qFz8KefqFkIQ)

* Depending on the position user gave, update the corresponding position of the board to reflect that.
* Print the updated board out.
* You will not need to determine the winner at this point.

**Answer the following questions before you start working in main.py:**

1. How many players should your game have?
2. When should the game end? Look at the requirements if you're not sure.

**Start working in main.py. There is some starter code for you, but you should not change it. However, you can use it in any way you'd like.**

***

### Bonus part 1

In real tic-tac-toe, you can't place your X or O in a position that already has an X or O. Modify your code so that if a player tries to place their letter in a position that was already played, the game will not let them. Instead, have it print out:
```error: Invalid move.```

### Bonus part 2
Figure out a way to break the while loop by hitting a win or tie condition. You will no longer need to have a max of 9 turns.
Answer the following question:
1. In what cases can player 1 (X) win?
2. In what cases can player 2 (O) win?
3. In what cases can the two players tie?