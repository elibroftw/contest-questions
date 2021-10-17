from typing import List
# https://leetcode.com/problems/combination-sum-iv/submissions/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # dp[i] = # ways to make i
        dp = [1] + [0] * target
        for i in range(1, target + 1):
            for num in nums:
                if num <= i:
                    dp[i] += dp[i - num]
        return dp[-1]
