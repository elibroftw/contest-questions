from typing import List
# https://leetcode.com/problems/two-sum/


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, v in enumerate(nums):
            if v in seen: return [seen[v], i]
            else: seen[target - v] = i
