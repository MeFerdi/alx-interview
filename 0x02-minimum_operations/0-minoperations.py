#!/usr/bin/python3
"""
Module for calculating minimum operations to achieve n 'H' characters.
"""

def minOperations(n):
    """
    Calculates the minimum number of operations needed to get exactly n 'H' characters.

    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: The minimum number of operations required, or 0 if impossible.
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        if n % factor == 0:
            operations += factor
            n //= factor
        else:
            factor += 1

    return operations
