# SudokuSolver

## C and Python Implementations Using Backtracking
## By [Dev Bhartra](https://github.com/devbhartra) and [Sarthak Gupta](https://github.com/sarthak7gupta)

### _Abstract_:
Sudoku is a 9x9 matrix filled with numbers 1 to 9 in such a way that every row, column and sub-matrix (3x3) has each of the digits from 1 to 9. We are provided with a partially filled 9x9 matrix and have to fill every remaining cell in it.

### _The Naive Approach (Brute Force)_:
The Naive Algorithm is to generate all possible configurations of numbers from 1 to 9 to fill the empty cells. Try every configuration one by one until the correct configuration is found.

But this isn’t the most efficient approach to this problem. Such an algorithm would have a runtime complexity of O(N<sup>N²</sup>), where N is size of the Sudoku puzzle (i.e., 9 in classic Sudoku). The brute force algorithm would perform 2*10⁷⁷ operations to find a solution. That would not be practical.

### _Backtracking_:
#### What is backtracking?
Backtracking is an algorithmic-technique for solving problems recursively by trying to build a solution incrementally, one piece at a time, removing those solutions that fail to satisfy the constraints of the problem at any point of time (by time, here, is referred to the time elapsed till reaching any level of the search tree).

#### Backtracking applied to this problem:
Like all other Backtracking problems, we can solve the  puzzle by assigning numbers sequentially to empty cells. Before assigning a number, we check whether the insertion of a certain number is ‘valid’ or not. The satisfaction of these condition define an insertion as valid. The same number should not be present in that row, column or in the smaller internal 3x3 sub-matrix.

After checking for validity, we assign the number, and recursively check whether this assignment leads to a solution or not. If the assignment doesn’t lead to a solution, we then try the next number for the current empty cell. And if none of the number (1 to 9) leads to a solution, we return false.

Once there are no unallocated cells, the Sudoku is solved.
Worst case complexity for this is O(nm), where n is the number of possibilities for each square (i.e., 9 in classic Sudoku) and m is the number of spaces that are blank, which is rare. Actual tight bound is much much lesser than that, and very practical.

### _High Level Algorithm_:
~~~~
Algorithm SolveSudoku
    Input:  A 9x9 sudoku S, and a row position R & column position C
    Output: 1, with lexicographically first solution of the Sudoku in S, if a solution exists, else 0

if R > 9 and C > 9, return 1 // No cells left, sudoku is solved

if S(R, C) is filled, then // Try next cell
    if C <= 9, return SolveSudoku(S, R, C + 1) // Move to next column
    else if R <= 9, return SolveSudoku(S, R + 1, 0) // Row over, move to next row
    else return 1 // No cells left, sudoku is solved

else // R, C is yet to be filled
    for i ← 1 to 9, do: // Try every number
        if i is not already present in the same row, column, or sub-matrix as R, C in S, then // i is a valid entry
            fill i into S(R, C) // Try solving
            if SolveSudoku(S, R, C), return 1 // Solution is possible from here
            else reset S(R, C) to empty // Backtrack

return 0 // No solution found
~~~~

#### Usage (C only for 9x9)- `gcc SOLVER.c -o sudoku; ./sudoku inp1.txt`

#### Usage (Python for 2x2, 3x3, 4x4)- `python(3) SOLVER.py inp1.txt 0/1 {1 for solution with steps. 0 for only final solution}`

Input file needs to have space separated values, and 0 for empty cells

One row per line

Sample Input Files with
* -H suffix are hexadokus (16x16) (1-10, instead of standard 0-F, as 0 is used for empty cell)
* -2 suffix are quadokus (4x4)
* Rest are standard sudokus (9x9)
* Other sample inputs in inps.txt, can be created to multiple files as needed
