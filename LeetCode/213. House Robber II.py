from typing import List
# https://leetcode.com/problems/house-robber-ii/

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp1, dp2 = 0, 0
        for num in nums[0:-1]:
            dp1, dp2 = dp2, max(dp1 + num, dp2)

        dp3, dp4 = 0, 0
        for num in nums[1:]:
            dp3, dp4 = dp4, max(dp3 + num, dp4)


        return max(dp2, dp4)
