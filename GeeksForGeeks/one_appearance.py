# https://www.geeksforgeeks.org/find-the-element-that-appears-once/
# list of N (# of appearances) sets
# or just two sets, one set being one appearance, the latter being more than one appearance

def find_once(arr):
    once = set()
    more_than_once = set()
    for el in arr:
        if el not in more_than_once:
            if el in once:
                once.remove(el)
                more_than_once.add(el)
            else: once.add(el)
    return once.pop()


tests = [
    [12, 1, 12, 3, 12, 1, 1, 2, 3, 3],
    [10, 20, 10, 30, 10, 30, 30]
]
for test in tests:
    print(find_once(test))

# Custom input
# lst = [int(num) for num in input().split()]
# print(find_once(lst))