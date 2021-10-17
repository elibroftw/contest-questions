from typing import List
# https://leetcode.com/problems/coin-change/


class Solution:

    d = {}

    def coinChange(self, coins: List[int], amount: int) -> int:

        if amount == 0:
            return 0
        if amount in self.d:
            return self.d[amount]

        fewest_coins = -1

        for coin in reversed(coins):
            if amount == coin:
                self.d[amount] = 1
                return 1
            elif coin < amount:
                temp = self.coinChange(coins, amount - coin) + 1
                if 0 < temp < fewest_coins or (fewest_coins == -1 and temp > 0):
                    fewest_coins = temp
        self.d[amount] = fewest_coins
        return fewest_coins


if __name__ == '__main__':
    assert Solution().coinChange([3], 2) == -1
