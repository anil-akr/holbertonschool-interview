#!/usr/bin/env python3
"""N Queens solver using backtracking."""
import sys


def is_safe(queens, row, col):
    """Check whether a queen can be placed without causing a conflict"""
    for placed_row, placed_col in queens:
        if placed_col == col or abs(placed_row - row) == abs(placed_col - col):
            return False
    return True


def solve(row, queens, board_size):
    """Solve the n queens with backtracking and print each solution"""
    if row == board_size:
        print(queens)
        return

    for col in range(board_size):
        if is_safe(queens, row, col):
            queens.append([row, col])
            solve(row + 1, queens, board_size)
            queens.pop()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        board_size = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if board_size < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve(0, [], board_size)
