# Author: Elijah Lopez
# https://icpcarchive.ecs.baylor.edu/index.php?option=com_onlinejudge&Itemid=8&category=530&page=show_problem&problem=3836



def solve(n, integers):
    # v3 solution
    iters = 0
    valid_seqs = n
    sum_cache = {}  # i: (index_stopped_at, sum)
    skip_cache = set()
    for i, integer in enumerate(integers):
        iters += 1
        integer = integers[i]
        if i in skip_cache: break  # short circuit
        if integer < 0:
            min_index = i - n
            temp_sum = integer
            j = i - 1
            valid_seqs -= 1
            while j > min_index:
                iters += 1
                temp_num = integers[j]
                pos_j = j % n
                if temp_num < 0:
                    if pos_j in sum_cache:
                        temp_sum += sum_cache[pos_j][1]
                        temp_j = sum_cache[pos_j][0]
                        if temp_j > j:
                            pos_j = temp_j
                            j = temp_j - n
                        else:
                            pos_j = temp_j + n
                            j = temp_j
                        temp_num = integers[j]
                skip_cache.add(pos_j)
                temp_sum += temp_num
                if temp_sum >= 0:
                    sum_cache[i] = (j, temp_sum - temp_num)
                    # sum is positive again
                    #  would become negative if a bigger negative integer is before but that would have
                    #  triggered this kind of search and so we break to avoid double counting
                    break
                valid_seqs -= 1
                j -= 1
    return valid_seqs


if __name__ == '__main__':
    n = 1
    while True:
        n = int(input())
        if not n: break
        input_lst = [int(x) for x in input().split()]
        print(solve(n, input_lst))
