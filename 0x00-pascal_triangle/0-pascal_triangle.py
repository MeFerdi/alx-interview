#!/usr/bin/python3
"""A script to determine pascal's triangle for any number"""

def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize with the first row

    for i in range(1, n):
        prev_row = triangle[-1]
        # Generate the next row by adding the adjacent values of the previous row
        row = [1]  # Start with 1
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)  # End with 1
        triangle.append(row)

    return triangle
