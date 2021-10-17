from typing import List
from bisect import bisect_left
# https://leetcode.com/problems/longest-increasing-subsequence/

# there is a O(n log n) way (Patience: binary search)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] = longest increasing sequence ending at i
        dp = [1 for _ in nums]
        for i, num in enumerate(nums):
            for j in range(i):
                if num > nums[j]:
                    lis = dp[j] + 1
                    if lis > dp[i]:
                        dp[i] = lis
        return max(dp)
