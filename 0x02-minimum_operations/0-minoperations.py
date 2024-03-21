#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly
    n H characters in the file.
    """
    if n <= 1:
        return 0

    operations = 0
    i = 2
    while i * i <= n:
        while n % i == 0:
            operations += i
            n /= i
        i += 1
    if n > 1:
        operations += n
    return int(operations)


if __name__ == "__main__":
    n = 4
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

    n = 12
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
