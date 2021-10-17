from typing import List
# https://leetcode.com/problems/coin-change/


class Solution:

    def coinChange(self, coins: 'List[int]', amount: 'int') -> 'int':
        INF = float('inf')
        dp = [INF if i > 0 else 0 for _ in range(amount + 1)]
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        if dp[-1] == INF:
            return -1
        return dp[-1]
