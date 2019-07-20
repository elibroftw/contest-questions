# COMMENTS
# Can't really say anything
# All I can say is that if your naive solution is too slow think from two angles

def get_eq(array, n):
    if n == 1: return 1
    i = 0
    j = n - 1
    s_start = int(array[i])
    s_end = int(array[j])
    while i < j:
        if s_start > s_end:
            j -= 1
            s_end += int(array[j])
        if s_start < s_end:
            i += 1
            s_start += int(array[i])
            # 1, 2, 3, 9
        if s_start == s_end:
            diff = j - i
            if diff == 2: return j
            elif diff < 2: return -1
            else:
                i += 1
                s_start += int(array[i])
                j -= 1
                s_end += int(array[j])
    return -1

test_cases = int(input())

for _ in range(test_cases):
    n = int(input())
    array = input().split()
    print(get_eq(array, n))
        