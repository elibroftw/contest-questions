from typing import List
# https://leetcode.com/problems/product-of-array-except-self/


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        product_is_zero = False
        for num in nums:
            if num == 0 and not product_is_zero:
                product_is_zero = True
            elif num == 0:
                return [0 for _ in range(len(nums))]
            else:
                product *= num
        answer = []
        for num in nums:
            if num == 0:
                answer.append(product)
            elif product_is_zero:
                answer.append(0)
            else:
                answer.append(product // num)
        return answer
