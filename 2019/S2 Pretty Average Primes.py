# p is prime if no prime between 1 and root of p divides into p

memo = {1: False, 2: True}
def is_prime(p):
    if p in memo:
        return memo[p]
    if p not in memo:
        if p % 2 == 0 or p <= 1:
            memo[p] = False
            return False
        sqr = int(p ** 0.5) + 1
        for divisor in range(3, sqr, 2):
            if p % divisor == 0:
                memo[p] = False
                return False
    return True

inputs = int(input())
for _ in range(inputs):
    a = b = n = int(input())
    while not is_prime(a) or not is_prime(b):
        a -= 1
        b += 1
    print(a, b)
