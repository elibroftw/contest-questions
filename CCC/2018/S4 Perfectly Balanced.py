# This problem was very tough for me to grasp and then speed up my code
# Without help: 9/15 but took ~2 hours to code
# After reading DMOJ editorial and looking at a C++ solution: 15/15
# C++ solution: https://github.com/aeternalis1/Contest-problems/blob/master/CCC/CCC-'18-S4-Balanced-Trees.cpp
# Does not pass DMOJ Batch #5. Not sure if language error or if code can be optimized further

memo = {1: 1, 2: 1}  # Used for memoization
# memoization is the storing of past calculations to stop repeated calculations

def perfectly_balanced(w):  # as all things should be
    if w not in memo:
        output = 0
        i = 1  # let i be the min weight of the subtrees in the tree of weight w
        branches = w  # number of threes that could have a weight of i
        while i < w:
            num = w // i - w // (i + 1)
            # all trees with min weight of i (some invalid trees)
            # - number of trees with max weight (removal of invalid trees)
            # = number of subtrees that have a max weight of i
            # e.g. w == 36, i == 1. num = 18 because 18 subtrees have weight of 1
            output += num * perfectly_balanced(i)  # self-explanatory
            branches -= num  # you used up those branches so remove them
            i = w // branches  # calculates the next smallest weight. Rather than using a for loop. Useful for big numbers
            # Suppose w == 36, i == 1. branches will now equal 18
            # 36 // 18 == 2; the smallest weight for all subtrees to be valid
            # 36 // 36 == 1 # 36 // 12 == 3
        memo[w] = output  # setting the memo map so that 
    return memo[w]


n = int(input())
print(perfectly_balanced(n))
