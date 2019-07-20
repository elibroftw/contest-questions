variables = {'A': 0, 'B': 0}
while True:
    user_input = input()
    values = user_input.split()
    instruction = int(values[0])
    if instruction == 1:
        variables[values[1]] = int(values[2])
    elif instruction == 2:
        print(variables[values[1]])
    elif instruction == 3:
        variables[values[1]] += variables[values[2]]
    elif instruction == 4:
        variables[values[1]] *= variables[values[2]]
    elif instruction == 5:
        variables[values[1]] -= variables[values[2]]
    elif instruction == 6:
        variables[values[1]] //= variables[values[2]]
    else:  # 7
        break

