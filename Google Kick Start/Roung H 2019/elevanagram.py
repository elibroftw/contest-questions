from itertools import permutations
tc = int(input())
for t in range(1, tc + 1):
    digits = [int(x) for x in input().split()]
    my_digits = []
    for i, d in enumerate(digits):
        if d > 0:
            my_digits += [str(i + 1) for _ in range(d)]
    divisible = False
    num_of_digits = len(my_digits)
    for combo in permutations(my_digits, num_of_digits):
        number = int(''.join(combo))
        if number % 11 == 0:
            divisible = True
            break
    ans = 'YES' if divisible else 'NO'
    print('Case #', t, ': ', ans, sep='')
    