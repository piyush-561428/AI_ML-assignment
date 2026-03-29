# AI_ML-assignment
Repository Made For Flipped Course "Fundamentals of AI&amp;ML"

# 8-Puzzle Solver (Breadth-First Search)

This project is a Python-based implementation of an *8-Puzzle Solver* using the *Breadth-First Search (BFS)* algorithm. The 8-puzzle is a classic sliding puzzle consisting of a $3 \times 3$ grid with numbered tiles and one empty space (0).

## Overview
The goal is to reach the state:

      1 2 3
      4 5 6
      7 8 0

This solver uses BFS to explore all possible moves layer-by-layer, ensuring that the first solution found is the one with the *minimum number of moves*.

---

## Setup & Requirements
* *Language:* Python 3.x
* *Libraries:* None (Uses standard collections.deque)

### Installation
1. Ensure you have Python installed.
2. Save the provided script as puzzle_solver.py.

---

## How to Use

1. *Open your terminal* or command prompt.
2. *Navigate* to the folder containing the script.
3. *Run the program*:
   bash
   python puzzle_solver.py
   

### Modifying the Start State
#To change the puzzle configuration, open the script and edit the start list and the x, y coordinates (the position of the 0):

      start = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
      x, y = 1, 1 # Row 1, Column 1




---

## Logic Behind the Solver
* *BFS (Breadth-First Search):* Explores all neighbors of a state before moving deeper. This guarantees the shortest path.
* *Visited Set:* Keeps track of every board configuration already checked to avoid infinite loops.
* *PuzzleState Class:* A simple container for the board layout, the coordinates of the empty space, and the move count (depth).

---

## Example Output:
      Initial State:
      1 2 3
      4 0 5
      6 7 8
      --------
      Depth: 0
      1 2 3
      4 0 5
      6 7 8
      --------
      ...
      Goal state reached at depth 2
