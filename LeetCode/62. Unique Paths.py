from typing import List
from functools import lru_cache
# https://leetcode.com/problems/unique-paths/

class Solution:
    @lru_cache
    def uniquePathsDFS(self, m: int, n: int) -> int:
        # DFS
        if m == 1 and n == 1:
            return 1
        rtrn = 0
        if m > 1:
            rtrn += self.uniquePaths(m - 1, n)
        if n > 1:
            rtrn += self.uniquePaths(m, n - 1)
        return rtrn

    def uniquePaths(self, m, n):
        """
        dp[i]: bottom of column i
        dp[0] = 1 by default
        dp[i] += dp[i - 1] for every row starting at 1
        update all columns since dp[i - 1] corresponds to values at each row
        """
        dp = [1] * n  # bottom of each column

        for _ in range(1, m):
            for i in range(1, n):
                dp[i] += dp[i - 1]

        return dp[-1]
