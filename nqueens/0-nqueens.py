#!/usr/bin/python3
"""Solving the N Queens problem using backtracking."""
import sys


def solve(n, row, queens, cols, diag1, diag2):
    """Place one queen per row from top to bottom.

    Uses three sets to track which columns and diagonals
    are already attacked, allowing O(1) conflict checks.

    Args:
        n: board size (and number of queens to place).
        row: current row being processed.
        queens: list where queens[i] is the column of the queen on row i.
        cols: set of columns already occupied.
        diag1: set of occupied "\\" diagonals (row - col).
        diag2: set of occupied "/" diagonals (row + col).
    """
    if row == n:
        # All rows filled, we have a complete solution
        print([[i, queens[i]] for i in range(n)])
        return

    for col in range(n):
        # Three possible conflicts: column, "\\" diagonal, "/" diagonal
        if col in cols or (row - col) in diag1 or (row + col) in diag2:
            continue

        # Place the queen and mark attacked squares
        queens[row] = col
        cols.add(col)
        diag1.add(row - col)
        diag2.add(row + col)

        solve(n, row + 1, queens, cols, diag1, diag2)

        # Backtrack: remove to try another column
        cols.remove(col)
        diag1.remove(row - col)
        diag2.remove(row + col)


def main():
    """Parse command-line arguments and start the solver."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve(n, 0, [0] * n, set(), set(), set())


if __name__ == "__main__":
    main()
