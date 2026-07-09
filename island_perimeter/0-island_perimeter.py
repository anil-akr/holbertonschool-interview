#!/usr/bin/python3
"""
Module that provides a function to compute the perimeter of an island
represented in a 2D grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described by a 2D grid.

    Args:
        grid (list[list[int]]): A rectangular grid where 0 represents
            water and 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    number_of_rows = len(grid)
    for row_index in range(number_of_rows):
        number_of_columns = len(grid[row_index])
        for col_index in range(number_of_columns):
            if grid[row_index][col_index] == 1:
                if row_index == 0 or grid[row_index - 1][col_index] == 0:
                    perimeter += 1
                if (row_index == number_of_rows - 1
                        or grid[row_index + 1][col_index] == 0):
                    perimeter += 1
                if col_index == 0 or grid[row_index][col_index - 1] == 0:
                    perimeter += 1
                if (col_index == number_of_columns - 1
                        or grid[row_index][col_index + 1] == 0):
                    perimeter += 1
    return perimeter
