from typing import List
# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Honing in on target again to solve in O(n)
        Come towards each other from the smaller height
        Compute the area before in/de-creasing x-axis to keep track of max area
        """
        area = 0
        i, j = 0, len(height) - 1
        while i < j:
            if height[i] > height[j]:
                area = max(height[j] * (j - i), area)
                j -= 1
            else:
                area = max(height[i] * (j - i), area)
                i += 1
        return area
