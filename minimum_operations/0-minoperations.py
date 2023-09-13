#!/usr/bin/python3
"""
finding minimum number of opeartions
when a text editor only uses copy All and paste
"""


def minOperations(n):
    """
    a text editor with a single character H.
    given a number n, calculate the fewest no. of operations
    that result to n and H characters in the file.
    """

    if n <= 1:
        return 0

    for i in range(2, int((n/2)+1)):
        if n % i == 0:
            return minOperations(int(n/i)) + i
    return n
