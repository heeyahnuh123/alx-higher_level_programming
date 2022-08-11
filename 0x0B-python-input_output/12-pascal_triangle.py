#!/usr/bin/python3
"""
Module 14-pascal_triangle
Contains function that returns int lists of pascal triangle of any given size
"""


def pascal_triangle(n):
    """
    Return:
        empty list [] if n <= 0
        if n is 7, we should expect:
            [1]
            [1, 1]
            [1, 2, 1]
            [1, 3, 3, 1]
            [1, 4, 6, 4, 1]
            [1, 5, 10, 10, 5, 1]
            [1, 6, 15, 20, 15, 6, 1]
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    triangle = [[1]]
    for rows in range(n-1):
        row = [1]
        for i in range(rows):
            row.append(triangle[-1][i] + triangle[-1][i+1])
        row.append(1)
        triangle.append(row)
    return triangle