from typing import List
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_profit = 0
        max_profit = 0
        for day in range(1, len(prices)):
            cur_profit = max(0, cur_profit + prices[day] - prices[day - 1])
            if cur_profit > max_profit:
                max_profit = cur_profit
        return max_profit
