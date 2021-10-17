# https://leetcode.com/problems/sum-of-two-integers/

"""
Bit Manipulation
    Set union A | B
    Set intersection A & B
    Set subtraction A & ~B
    Set negation ALL_BITS ^ A or ~A
    Set bit A |= 1 << bit
    Clear bit A &= ~(1 << bit)
    Test bit (A & 1 << bit) != 0
    Extract last bit A&-A or A&~(A-1) or x^(x&(x-1))
    Remove last bit A&(A-1)
    Get all 1-bits ~0
"""


class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        mask = 0xffffffff
        while b:
            sum = (a ^ b) & mask
            carry = ((a & b) << 1) & mask
            a = sum
            b = carry

        if (a>>31) & 1: # If a is negative in 32 bits sense
            return ~(a^mask)
        return a
