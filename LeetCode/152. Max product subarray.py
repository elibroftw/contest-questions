from typing import List
# https://leetcode.com/problems/maximum-product-subarray/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Keep in mind that two negatives make a positive
        Therefore, need to keep track of two paths
        I:  The running maximum product and the previous max product
        II: The running minimum (max negative) product
        """
        # start with the first number as it makes things easier
        last_min = product = last_product = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            # the max product is either itself (a reset of the subarray),
            #                           the multiplication of the running max product, or
            #                           the multiplication of the running minimum product
            max_product = max(num, last_product * num, last_min * num)
            min_product = min(num, last_product * num, last_min * num)
            last_product = max_product
            last_min = min_product
            product = max(max_product, product)
        return product
