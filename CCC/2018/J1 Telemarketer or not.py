# seven-digit phone numbers
# last four digits have three properties
# the first of these four digits is an 8 or 9;
# the last digit is an 8 or 9;
# the second and third digits are the same.


def check():
    n = []
    for i in range(4):
        n.append(int(input()))
    if n[0] != 8 and n[0] != 9: return 'answer'
    if n[3] != 8 and n[3] != 9: return 'answer'
    if n[1] != n[2]: return 'answer'
    return 'ignore'


print(check())
