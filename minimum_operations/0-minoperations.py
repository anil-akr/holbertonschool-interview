#!/usr/bin/python3
"""Module for minimum operations."""


def minOperations(n):
    """Calculate the fewest number of operations needed."""
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations = operations + factor
            n = n // factor
        factor = factor + 1

    return operations

