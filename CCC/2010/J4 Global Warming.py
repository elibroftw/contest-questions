from math import ceil

while True:
    user_input = input().split()
    length = int(user_input[0])
    if length == 0:
        break
    numbers = [int(x) for x in user_input[1:]]
    changes = []
    previous_value = 0
    for i, v in enumerate(numbers):
        if i > 0:
            changes.append(v - previous_value)
        previous_value = v
    if len(changes) == 0:
        print(numbers[0])
    for x in range(1, len(changes) + 1):
        cycle = changes[:x]
        new_cycle = cycle * ceil(len(changes) / x)
        if new_cycle[:len(changes)] == changes:
            print(x)
            break
