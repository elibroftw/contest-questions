# https://leetcode.com/problems/longest-common-subsequence/


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp[i][j] = longest common subseq ending at text1[i] and text2[j]
        # if text1[i] != text2[j], the longest subseq is the same as i-1 or j-1 or 0
        # could also do dp[i] = longest common subseq ending at smaller[i]
            # since we are limited by one string
        dp = [ [0 for _ in text2] for _ in text1]
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    bf = dp[i - 1][j - 1] if i > 0 and j > 0 else 0
                    dp[i][j] = 1 + bf
                else:
                    bf1 = dp[i - 1][j] if i > 0 else 0
                    bf2 = dp[i][j - 1] if j > 0 else 0
                    dp[i][j] = max(bf1, bf2)
        return dp[-1][-1]
