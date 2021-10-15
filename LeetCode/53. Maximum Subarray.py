from typing import List
# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Keep track of max till the current number
        Reset max till current number if it becomes negative
        """
        cur_max = -10 ** 4 - 1
        max_till_here = 0
        for num in nums:
            max_till_here += num
            if max_till_here > cur_max:
                cur_max = max_till_here
            if max_till_here < 0:
                max_till_here = 0
        return cur_max
