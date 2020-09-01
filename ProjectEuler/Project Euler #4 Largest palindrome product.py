# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbe


def check_palindrome(x):
    x = str(x)
    # if x[0] != x[-1]: return False
    for i in range(len(x) // 2 + 1):
        if x[i] != x[-i - 1]:
            return False
    return True


one = 999
second = 998

while True:
    product = one * second
    if check_palindrome(product):
        print(product)
        print(one, second)
        break
    elif second > 990:
        second -= 1
    else:
        second = 998
        one -= 1

