# Lesson 2.06: Game Loop

## Learning Objectives

Students will be able to...

* Define and identify: **while loop**.
* Use a while loop to simulate game play.

## Materials/Preparation

 | **Duration**   | **Description**    |
| ---------- | -------------- |
| [Do Now](#DoNow.md) |  Our usual warm up.         |
|  Read Me | This document |
| [Class Norms](#ClassNorms.md) | Our class norms          |
| [Lab](#lab.md) | The lab for today         |
| [main](#main.py) | The file that you should edit for the lab        |

* [Associated Readings 2.7](https://tealsk12.github.io/2nd-semester-introduction-to-computer-science/readings.md#associatedreadings/2.7)

## meanwhile ...

The main difference between an if and a while is that if executes once if a condition is true, and a while keeps executing as long as something is true. The something that remains true is called the [invariant](https://en.wikipedia.org/wiki/Loop_invariant)

It follows that each time you go through the loop that there must be something that might change the invariant, otherwise the loop will go on forever.

To help you and future programmers it is helpful to create an invariant that is understandable and if it *has* to be complicated at least explain why.


#### Discussion

* Ask: how might while loops be useful?
* Ask students to consider how they could write a loop using user input.
* What if you wanted the loop to stop when the user inputs "quit"?

