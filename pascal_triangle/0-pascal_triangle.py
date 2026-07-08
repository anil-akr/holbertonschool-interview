#!/usr/bin/python3
"""Module that builds Pascal's triangle."""


def pascal_triangle(n):
    """
    Return a list of lists of integers representing Pascal's triangle of n.

    Args:
        n (int): the number of rows of the triangle.

    Returns:
        list: list of lists of integers, or an empty list if n <= 0.
        """
    if n <= 0:
        return []

    triangle = [[1]]

    for row_index in range(1, n):
        previous_row = triangle[row_index - 1]
        row = [1]
        for column_index in range(1, row_index):
            left_value = previous_row[column_index - 1]
            right_value = previous_row[column_index]
            row.append(left_value + right_value)
        row.append(1)
        triangle.append(row)

    return triangle
