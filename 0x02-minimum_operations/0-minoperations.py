#!/usr/bin/python3
"""returns the minimum number of operations required to return n letters"""


def minOperations(n):
    """returns the minimum no of operations to return n letters"""
    next = 'H'
    body = 'H'
    op = 0
    while (len(body) < n):
        if n % len(body) == 0:
            op += 2
            next = body
            body += body
        else:
            op += 1
            body += next
    if len(body) != n:
        return 0
    return op
