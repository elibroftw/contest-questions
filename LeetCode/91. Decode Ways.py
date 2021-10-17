# https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:
        # dp[i] = ways to decode ending at i
        mapping = {str(i) for i in range(1, 27)}
        dp = [0] * len(s)
        for i in range(len(s)):
            if s[i] in mapping:
                if i > 0:
                    dp[i] = dp[i - 1]
                else:
                    dp[i] = 1
            if i > 0:
                if s[i - 1:i + 1] in mapping:
                    if i > 1:
                        dp[i] += dp[i - 2]
                    else:
                        dp[i] += 1
        return dp[-1]
