#!/usr/bin/python3
"""Defines the pascal's triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.

    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]

        if i >0:
            for j in range(1, i):
                prev_row = triangle[i - 1]
                row.append(prev_row[j - 1] + prev_row[j])

        if i > 0:
            row.append(1)

        triangle.append(row)

    return triangle
