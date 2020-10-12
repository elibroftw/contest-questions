from typing import List
from functools import lru_cache


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache
        def helper(s):
            if not s: return True  # s is empty
            for word in wordDict:
                # if s starts with a word and the rest of the string is made up of words in wordDict
                if s.startswith(word) and helper(s[len(word):]):
                    return True
            return False
        return helper(s)


    def run_tests(self):
        assert self.wordBreak('leetcode', ['leet', 'code'])
        assert self.wordBreak('applepenapple', ['apple', 'pen'])
        assert not self.wordBreak('catsandog', ['cats', 'dog', 'sand', 'and', 'cat'])
        assert not self.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])
        assert self.wordBreak("catskicatcats", ["cats","cat","dog","ski"])
        assert self.wordBreak("catcats", ["cats","cat","dog","ski"])


s = Solution()
s.run_tests()
