# Tower of Hanoi Solver 

## Author: Hristina Nikolic 
## Date: October, 2024

## Introduction 

This project was done as part of the interview process for the position of the Junior Solutions Engineer at Incode Technologies. 

## History

The tower of Hanoi is a mathematical puzzle. It consists of three rods and several disks of different diameters, which can slide onto any rod. The puzzle starts with the disks stacked on one rod in order of decreasing size, the smallest at the top, thus approximating a canonical shape. The objective of the puzzle is to move the entire stack to the last rod.

![Alt text](images/hanoi.png) 

**Figure 1** Tower of Hanoi Illustration

## Problem Statement

Move all the disks stacked on the first tower over the last tower using a helper tower in the Middle.

## Rules 
There are three simple rules:
1. Only one disk may be moved at a time.
1. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or an empty rod.
1. No disk may be placed on top of a disk that is smaller than it.

With 3 disks, the puzzle can be solved in 7 moves. The minimal number of moves required to solve a Tower of Hanoi puzzle is 2<sup>n</sup> − 1, where n is the number of disks.

## Solution 

I developped an application that solves the Hanoi Towers Puzzle, and has the following characteristics:
- The App must be implemented considering a Back-End service for algorithm/calculations execution, and a Front-End Application that shows the movements required to resolve it based on a specific number of disks.
- The Back-End service should be services/microservices that use JSON payloads.
- The Front-End could be a Web Application that will consume the Back End Service/API and must show the required movements to solve the Puzzle.

## Algorithm

The problem can be solved with a few different algorithms: 
1. Iterative Algorithm - The iterative algorithm for the Tower of Hanoi employs a systematic approach to move disks without recursion, often utilizing a loop and following specific rules based on the parity of the number of disks. It typically involves moving disks between the rods in a predetermined sequence, ensuring that smaller disks are always placed on top of larger disks. This approach also requires 2<sup>n</sup> − 1 moves, providing an efficient way to solve the puzzle without the overhead of recursive function calls.
1. Recursive Algorithm - The recursive algorithm for solving the Tower of Hanoi involves breaking down the problem into smaller subproblems. It recursively moves the top n−1n−1 disks from the source rod to an auxiliary rod, then moves the largest disk directly to the destination rod, and finally moves the n−1n−1 disks from the auxiliary rod to the destination rod. This elegant method utilizes the principle of recursion to achieve the solution in 2<sup>n</sup> − 1 moves.

For this application, we chose to implement ... 

## Application Diagram 

## Tech Stack

### Back-end 

The back-end will:
- Calculate the sequence of moves required to solve the puzzle based on the number of disks.
- Expose an API endpoint that receives the number of disks and returns the steps in JSON format.

Language: Python 

Framework: Flask (Python) 

API: RESTful JSON API

### Front-end

The front-end will:
- Allow the user to input the number of disks.
- Consume the back-end API to retrieve the list of moves.
- Display the steps to solve the puzzle and optionally show the graphical representation of the puzzle.

Language: JavaScript, HTML, CSS

## Requrements and Installation 

The application was developed using Python 3. 

Additionally, it uses Python's module Flusk.

First, clone the repository and install the required packages:

```bash 
git clone https://github.com/hristinanikpi/tower_of_hanoi.git
cd tower_of_hanoi
pip install requirements.txt 
```

Afterwards, run the app, use the following command: 

```bash 
python3 app.py 
```

## Demonstration 

The application for 3 disks runs as follow: 

![Alt text](images/solution_3_disks.png) 

**Figure 2** Tower of Hanoi Solver for 3 disks 

The apllication for 4 disks runs as follow:

![Alt text](images/solution_4_disks.png) 

**Figure 3** Tower of Hanoi Solver for 4 disks 

## Solving Time

In order to determine how well the application performs, we calculated the solving time for different numbers of disks.

|    | Recursive Algorithm   | Iterative Algorithm   |
|------------|:----------:|-----------:|
| 5 disks| Row 1 Col 2| Row 1 Col 3|
| 10 disks| Row 2 Col 2| Row 2 Col 3|
| 20 disks| Row 3 Col 2| Row 3 Col 3|
| 50 disks| Row 3 Col 2| Row 3 Col 3|

**Table 1** Table of solving time for different numbers of disks for recursive and iterative algorithm
