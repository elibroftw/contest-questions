from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if s == '': return True
        paths = {s}
        visited = set()
        while paths:
            new_paths = set()
            for path in paths:
                for word in wordDict:
                    word_len = len(word)
                    temp = path
                    while temp.startswith(word):
                        temp = temp[word_len:]
                        if temp == '': return True
                        if temp not in visited:
                            visited.add(temp)
                            new_paths.add(temp)
            paths = new_paths
        return False  # no matches found

    def run_tests(self):
        assert self.wordBreak('leetcode', ['leet', 'code'])
        assert self.wordBreak('applepenapple', ['apple', 'pen'])
        assert not self.wordBreak('catsandog', ['cats', 'dog', 'sand', 'and', 'cat'])
        assert not self.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])
        assert self.wordBreak("catskicatcats", ["cats","cat","dog","ski"])
        assert self.wordBreak("catcats", ["cats","cat","dog","ski"])


s = Solution()
s.run_tests()
