from typing import List
# https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0 for _ in nums]
        for i, num in enumerate(nums):
            if i == 0:
                dp[0] = num
            elif i == 1:
                dp[1] = num
            else:
                # [0, 1, 2, 3]
                dp[i] = max(dp[:i - 1]) + num
        return max(dp)

    def rob2(self, nums):
        # not mine
        dp1, dp2 = 0, 0
        for num in nums:
            dp1, dp2 = dp2, max(dp1 + num, dp2)
        return dp2
