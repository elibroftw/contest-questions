from typing import List
from bisect import bisect_left
# https://leetcode.com/problems/longest-increasing-subsequence/

# there is a O(n log n) method https://leetcode.com/problems/longest-increasing-subsequence/solutions/1326308/c-python-dp-binary-search-bit-segment-tree-solutions-picture-explain-o-nlogn/
# thinking for binary search: try keeping track of a possible longest sequence* BUT whenever you encounter a number that won't fit, replace the smallest number bigger than what you got with the number you found
    # afterwards, either a bigger number or a smaller number is found
    # in the case of the smaller number, it won't fit so it will replace an earlier number
    # in the case of bigger numbers, the last index will end up being replaced -> more opportunity to increase list
    # it works out since the indexes in between the first and last are only there to push a replacement of the last index
    # we would not actually be tracking the real longest sequence

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] = longest increasing sequence ending at i
        dp = [1 for _ in nums]
        # for each index, check the longest sequence for the previous indices
        #   and if the sequence can be longer update the current index
        for i, num in enumerate(nums):
            for j in range(i):
                if num > nums[j] and dp[j] >= dp[i]:
                    dp[i] = dp[j] + 1
        return max(dp)
