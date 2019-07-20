# COMMENTS
# I was going to use int(x) for x in input().split() and then use array.sort()
# But I thought it was too easy
# So I instead opted to use sorted a technique I learned on hackerrank

# I tried to make an array.sort() solution 
# BUT, I would have had to convert the integers to strings again!
# So I decided to not even bother

# I was also thinking about just counting number of 0's 1's and 2's 
# and then printing but that's also pretty simple of a solution
# and is not very usable if the range was greater

test_cases = int(input())

for _ in range(test_cases):
    n = int(input())
    array = input().split()
    array = sorted(array, key=lambda x: int(x))
    print(' '.join(array))