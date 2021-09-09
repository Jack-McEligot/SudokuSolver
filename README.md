# Sudoku Solver
This program takes an unsolved Sudoku puzzle as a string and finds the solution to said puzzle (given that it is solvable)
## File Uses
### SudokuSolver.py
* This file solves a series of puzzles, and reports statistics involving the time elapsed for each puzzle solution and the maximum memory consumed by the program during said period. This is used to gauge the effectiveness of the implemented backtracking algorithm.
### PromptedExecution.py
* This file takes an unsolved puzzle and attempts to find the solution by using a depth-first search backtracking algorithm. It does not currently check for incorrect input.
## Solve a puzzle
1. Launch the PromptedExecution.py script, and input 9 rows of a puzzle in the format (zeros are empty spaces, X's are given numbers)
* "00x00x0x0 x000x000x 00x00x0x0 00x00x0x0 x000x000x 00x00x0x0 00x00x0x0 x000x000x 00x00x0x0"
2. Hit enter, and wait for program to solve. This may take up to several minutes depending on the complexity of the puzzle.
