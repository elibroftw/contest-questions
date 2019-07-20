# COMMENTS
# At first I had two for loops but was creating a sub-array in the nested for loop every time
# and then used sum on said sub-array
# I also did not break the loop if new_sum > s
# This TLE

# So i stopped creating sub arrays, and incremented the new_sum variable
# Also added in the new_sum > s check
# This worked

# But I read the comments, and someone said he did the problem in O(n)
# So I thought about a solution
# If i started at i = 0, and j = 1
# The sum is the first variable
# If the sum is too small, I add element j to new_sum and j++
# If sum is too big, I subtract element i and i++

test_cases = int(input())


def get_sub(array, n, s):
    new_sum = array[0]
    i = 0
    j = 1
    while True:
        if new_sum < s:
            if j == n: break
            new_sum += array[j]
            j += 1
        if new_sum > s:
            new_sum -= array[i]
            i += 1
            if i == n: break
        if new_sum == s:
            print(i + 1, j)
            return
    print(-1)


for _ in range(test_cases):
    n, s = (int(x) for x in input().split())
    array = [int(x) for x in input().split()]
    get_sub(array, n, s)
