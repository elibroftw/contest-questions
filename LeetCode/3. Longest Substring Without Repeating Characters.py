# not the fastest, but most intuitive
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # the naive solution was O(n^2) which would clear a set every new search
        #   in this solution, compare the index of the characters seen
        #   and recompute the max length on every loop
        #   whenever we see a duplicate, we can just skip ahead to the index that we know has not hit a duplicate yet
        # rationale: if the character has been seen since we started, ignore
        # O(n) by comparing index rather than clearing the set
        start = result = 0
        seen = dict()

        for i, c in enumerate(s):

            if seen.get(c, -1) >= start:
                # if the character has been seen since we started a search,
                # restart the search from the index after the first character
                #   since we have already calculated the max between the repeating chars
                start = seen[c] + 1

            result = max(result, i - start + 1)
            seen[c] = i

        return result
