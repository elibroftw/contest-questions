# https://leetcode.com/problems/number-of-1-bits/

class Solution:
    def hammingWeight(self, n: int) -> int:
        c = 0
        while n:
            n &= n - 1  # cuts off 1 each time
            c += 1
        return c
        return bin(n).count('1')
