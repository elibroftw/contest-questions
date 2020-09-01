# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

memo = {2: True}


def is_prime(x):
    if x in memo:
        return memo[x]
    if not x % 2:
        memo[x] = False
        return False
    for j in range(3, int(pow(x, 0.5)), 2):
        if not x % j:
            memo[x] = False
            return False
    memo[x] = True
    return True


n = 600851475143
latest_factor = 0
while True:
    for i in range(3, n + 1, 2):
        if is_prime(i):
            if not n % i:
                latest_factor = i
                while not n % i:
                    n = n // i
                break
    if n == 1:
        break

print(latest_factor)
