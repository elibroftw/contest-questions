#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maxValue' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY rounds
#


from contextlib import suppress


def maxValue(n, rounds):
    # 1-based indexing

    # instead of updating every index every time, we can process at the end by
    #  assuming the value of each asset needs to up added to all the ones to the right
    # 1) add only to the starting index
    # 2) subtract from the index right after the ending index to cancel out the excessive additions from above
    # at the end we update the right index by the current index to take advantage of carry forward (no double counting)

    investments = [0 for _ in range(n)]

    for start, end, contrib in rounds:
        investments[start - 1] += contrib  # increase start
        with suppress(IndexError):
            # decrease right of end (to offset the + contrib in final processing)
            investments[end] -= contrib

    max_invested = investments[0] if n else 0
    for i in range(n - 1):  # avoid IndexError
        investments[i + 1] = investments[i]
        if investments[i + 1] > max_invested:
            max_invested = investments[i + 1]

    return max_invested


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    rounds_rows = int(input().strip())
    rounds_columns = int(input().strip())

    rounds = []

    for _ in range(rounds_rows):
        rounds.append(list(map(int, input().rstrip().split())))

    result = maxValue(n, rounds)

    fptr.write(str(result) + '\n')

    fptr.close()
