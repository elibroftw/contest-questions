# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
from collections import defaultdict
import math

def nCr(n,r):
    f = math.factorial
    return f(n) // f(r) // f(n - r)


def sherlockAndAnagrams(s):
    # for each index, go right from it 
    # and make a substring out of the letter's,
    # put this into a dictionary where the key is a lexiograhically sorted string
    # at the very end, go through each strirng and do v Choose 2 where v is the counter
    counter = defaultdict(int)
    number = 0
    length = len(s)
    for i in range(length):
        for j in range(i, length):
            counter[''.join(sorted(s[i:j + 1]))] += 1
    for k, v in counter.items():
        if v > 1: number += nCr(v, 2)
    return number


assert sherlockAndAnagrams('abba') == 4
assert sherlockAndAnagrams('abcd') == 0
assert sherlockAndAnagrams('ifailuhkqq') == 3
assert sherlockAndAnagrams('kkkk') == 10
