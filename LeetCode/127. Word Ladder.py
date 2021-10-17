from typing import List
# https://leetcode.com/problems/word-ladder/submissions/
import string

class Solution:

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # bidirectional search
        words = set(wordList)
        if endWord not in words:
            return 0
        starts = {beginWord}
        ends = {endWord}
        words_used = 1
        while starts:
            words_used += 1
            words -= starts
            next_words = set()
            for word in starts:
                for i in range(len(word)):
                    left, right = word[:i], word[i + 1:]
                    for char in string.ascii_lowercase:
                        next_word = left + char + right
                        if next_word in words:
                            if next_word in ends:
                                return words_used
                            next_words.add(next_word)
            starts = next_words
            if len(starts) > len(ends):
                # search from other side if there's less nodes to search from
                starts, ends = ends, starts
        return 0
