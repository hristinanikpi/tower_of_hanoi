# Tower of Hanoi Solver 

## Author: Hristina Nikolic 
## Date: October, 2024

## Introduction 

This project was done as part of the interview process for the position of the Junior Solutions Engineer at Incode Technologies. 

## History

The tower of Hanoi is a mathematical puzzle. It consists of three rods and several disks of different diameters, which can slide onto any rod. The puzzle starts with the disks stacked on one rod in order of decreasing size, the smallest at the top, thus approximating a canonical shape. The objective of the puzzle is to move the entire stack to the last rod.

![Alt text](images/hanoi.png)

## Problem Statement

Move all the disks stacked on the first tower over the last tower using a helper tower in the Middle.

## Rules 
There are three simple rules:
1. Only one disk may be moved at a time.
1. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or an empty rod.
1. No disk may be placed on top of a disk that is smaller than it.

With 3 disks, the puzzle can be solved in 7 moves. The minimal number of moves required to solve a Tower of Hanoi puzzle is 2n − 1, where n is the number of disks.

## Solution 

I developped an application that solves the Hanoi Towers Puzzle, and has the following characteristics:
- The App must be implemented considering a Back-End service for algorithm/calculations execution, and a Front-End Application that shows the movements required to resolve it based on a specific number of disks.
- The Back-End service should be services/microservices that use JSON payloads.
- The Front-End could be a Web Application that will consume the Back End Service/API and must show the required movements to solve the Puzzle.

## Algorithm

The problem can be solved with a few different algorithms: 
1. Iterative 
1. Recursive 
1. Q-learning

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

To run the application, clone the repository and install the required packages:

```bash 
git clone https://github.com/hristinanikpi/tower_of_hanoi.git
cd tower_of_hanoi
pip install requirements.txt 
```

## Solving Time

I order to see how the application performs, we wanted to calculate the solving time for:
- 5 disks
- 10 disks 
- 20 disks 
- 50 disks 
