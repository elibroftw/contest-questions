# does not pass for n > 10^6, my algorithm is not good enough

def memoize(f):
    memo = {}

    def helper(a):
        if a in memo:
            return memo[a]
        memo[a] = f(a)
        return memo[a]
    return helper


n = int(input())


memo = {}
def perfectly_balanced(w):  # as all things should be
    if w in (1, 2):
        return 1
    if w not in memo:
        output = 0
        for i in range(2, w + 1):  # i is number of subtrees
            output += perfectly_balanced(w // i)
        memo[w] = output
    return memo[w]

# output = 1
# while n > 0:
    
print(perfectly_balanced(n))

# TODO: come up with no recursion solution
