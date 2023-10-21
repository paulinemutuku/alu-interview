#!/usr/bin/python3
""" using pascal_triangle theory"""


def pascal_triangle(n):
    """Returns a list of lists of integers
    representing the Pascal’s triangle of n"""
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1, 1]]
    pascal = [[1], [1, 1]]
    for i in range(
            2, n):  # start at 2 because we already have the first two rows
        row = [1]  # first number is always 1
        for j in range(1, i):
            row.append(pascal[i - 1][j - 1] + pascal[i - 1]
                       [j])  # sum of the two numbers above
        row.append(1)  # last number is always 1
        pascal.append(row)  # add the row to the triangle
    return pascal


# print(pascal_triangle(3)) # [[1], [1, 1], [1, 2, 1]]
