n = int(input())
scores = [0, 0]
computer_names = ['', '']
for i in range(n):
    user_input = input().split()
    name = user_input[0]
    r, s, d = (int(_) for _ in user_input[1:])
    score = 2 * r + 3 * s + d
    if score > scores[1]:
        if score > scores[0]:
            computer_names[1], computer_names[0] = computer_names[0], name
            scores[1], scores[0] = scores[0], score
        elif score == scores[0]:
            if name < computer_names[0]:
                computer_names[1], computer_names[0] = computer_names[0], name
                scores[1], scores[0] = scores[0], score
            else:
                computer_names[1], scores[1] = name, score
        else:
            scores[1] = score
            computer_names[1] = name

print(computer_names[0])
print(computer_names[1])
