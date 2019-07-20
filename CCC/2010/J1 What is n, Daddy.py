n = int(input())

if n < 6:
    output = n // 2 + 1
else:
    hand_1 = 5
    hand_2 = n - 5
    output = 1
    for i in range(n//2):
        hand_1 -= 1
        hand_2 += 1
        if hand_2 > hand_1:
            break
        output += 1
print(output)
