from typing import List
# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Keep track of sum on an interval basis
        Reset interval sum if it becomes negative
        """
        # minimum possible number
        max_sum = -10 ** 4 - 1
        interval_sum = 0
        for num in nums:
            interval_sum += num
            max_sum = max(max_sum, interval_sum)
            # reset if negative sum encountered
            interval_sum = max(interval_sum, 0)
        return max_sum
