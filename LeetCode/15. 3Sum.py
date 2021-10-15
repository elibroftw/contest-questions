from typing import List
# https://leetcode.com/problems/3sum/

from itertools import islice

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Quickest is O(n^2) so sort array first.

        First sort the list lowest to highest
        Now make tripples starting with the first unique number
        e.g., 3, 3, x,x uses only the first 3 for (3, X, X)
        Iterate rest of list to get different types of triplets
        This ensures we don't duplicate the indices.
        We add triplets to a reeturn set
        We don't have to worry about different arangements
        since triplets are in ascending order.
        """
        if len(nums) < 3:
            return []

        results = set()
        nums.sort()

        for i, num in enumerate(islice(nums, 0, len(nums) - 2)):
            if i >= 1 and num == nums[i - 1]:
                # avoid same first position
                continue

            looking_for = set()
            for x in islice(nums, i + 1, len(nums)):
                if x in looking_for:
                    results.add((num, x, -x-num))
                else:
                    looking_for.add(-x-num)
        return results
