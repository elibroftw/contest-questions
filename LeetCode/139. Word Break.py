from typing import List
from functools import lru_cache


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        @lru_cache
        def helper(i):
            if not s[i:]: return True
            for word in wordDict:
                if s[i:].startswith(word) and helper(i + len(word)):
                    return True
            return False
        return helper(0)


    def run_tests(self):
        assert self.wordBreak('leetcode', ['leet', 'code'])
        assert self.wordBreak('applepenapple', ['apple', 'pen'])
        assert not self.wordBreak('catsandog', ['cats', 'dog', 'sand', 'and', 'cat'])
        assert not self.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])
        assert self.wordBreak("catskicatcats", ["cats","cat","dog","ski"])
        assert self.wordBreak("catcats", ["cats","cat","dog","ski"])


s = Solution()
s.run_tests()
