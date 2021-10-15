from typing import List
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Binary Search
        """
        n = len(nums)
        if n == 1 or nums[-1] > nums[0]:
            return nums[0]
        idx = n // 2
        while True:
            n = n // 2 + 1
            if nums[idx - 1] > nums[idx]:
                return nums[idx]
            elif nums[idx] < nums[0]:
                idx -= n // 2
                n = n // 2 + 1
            else:
                idx += n // 2
