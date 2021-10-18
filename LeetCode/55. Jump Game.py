from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # dp[i]: bool (can be reached)
        fill_until = 0
        for i, num in enumerate(nums):
            if fill_until < i:
                return False
            fill_until = max(fill_until, i + num)
        return True
