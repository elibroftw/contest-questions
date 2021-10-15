from typing import List
# https://leetcode.com/problems/search-in-rotated-sorted-array/


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Binary search + hone in on target
        For every middle, try to disregard one side
        by using the endpoints to determinet that all elements
        are > or < than the target.
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                # check if LHS does not contain target
                if nums[left] > target and nums[mid] >= nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                # check if RHS does not contain target
                if nums[right] < target and nums[mid] <= nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1
