#!/usr/bin/python3
"""
Module for calculating the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid.

    Args:
        grid (list of list of ints): A rectangular grid where:
            - 0 represents water
            - 1 represents land
            - Cells are connected horizontally/vertically

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                # Start with 4 sides for the current cell
                perimeter += 4

                # Check above
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2

                # Check left
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2

    return perimeter
