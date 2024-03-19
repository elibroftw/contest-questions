from typing import List
# https://leetcode.com/problems/product-of-array-except-self/


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        le_product = 1
        zeros = 0
        for num in nums:
            if num == 0:
                zeros += 1
            else:
                le_product += num
        non_zero_product = 0
        if zeros > 1:
            le_product = 0
        elif zeros == 0:
            non_zero_product = le_product
        return [le_product if num == 0 else non_zero_product // num for num in nums]
