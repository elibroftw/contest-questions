# Author: Elijah Lopez
# https://icpcarchive.ecs.baylor.edu/index.php?option=com_onlinejudge&Itemid=8&category=530&page=show_problem&problem=3836


def solve_old(n, integers):
    # v2 solution. TLE
    iters = 0
    sums = {}
    valid_keys = set()
    keys_to_ignore = set()
    total_sum = 0
    for i, integer in enumerate(integers):
        # add integers in order
        total_sum += integer
        for k in valid_keys:
            if k not in keys_to_ignore:
                iters += 1
                v = sums[k]
                if v + integer < 0:
                    del sums[k]
                    keys_to_ignore.add(k)
                else: sums[k] += integer
        if integer >= 0:
            valid_keys.add(i)
            sums[i] = integer
    if total_sum < 0: return 0  # short-circuit
    for i, integer in enumerate(integers):
        for k in valid_keys:
            if k != i and k not in keys_to_ignore:
                iters += 1
                v = sums[k]
                if v + integer < 0:
                    del sums[k]
                    keys_to_ignore.add(k)
                else: sums[k] += integer
        if i in valid_keys: valid_keys.remove(i)
    return len(sums)


def solve(n, integers):
    # v3 solution. Optimized and passes
    iters = 0
    valid_seqs = n
    sum_cache = {}  # 'i:j': (index_stuck_at, sum)
    skip_cache = set()
    for i, integer in enumerate(integers):
        iters += 1
        integer = int(integer)
        if i in skip_cache: break  # short circuit
        if integer < 0:
            valid_seqs -= 1
            temp_sum = integer
            j = i - 1
            max_index = i - n
            while j > max_index:
                temp_num = int(integers[j])  # a previous integer
                if temp_num < 0:
                    if (j % n) in sum_cache:
                        temp_sum += sum_cache[j % n][1]
                        temp_j = sum_cache[j % n][0]
                        if temp_j > j: temp_j -= n
                        j = temp_j
                        temp_num = int(integers[j])
                skip_cache.add(j % n)
                temp_sum += temp_num
                if temp_sum >= 0:
                    sum_cache[i] = (j, temp_sum - temp_num)
                    # sum is positive again
                    #  would become negative if a bigger negative integer is before but that would have
                    #  triggered this kind of search and so we break to avoid double counting
                    break
                valid_seqs -= 1
                j -= 1
            if j <= max_index: return 0  # short circuit
    return valid_seqs


if __name__ == '__main__':
    n = 1
    while True:
        n = int(input())
        if not n: break
        # integers = [int(x) for x in input().split()]
        print(solve(n, input().split()))
