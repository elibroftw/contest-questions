user_input = input()
h_flips = user_input.count('H') % 2
v_flips = user_input.count('V') % 2

if h_flips and v_flips:
    print(4, 3)
    print(2, 1)
elif h_flips:
    print(3, 4)
    print(1, 2)
elif v_flips:
    print(2, 1)
    print(4, 3)
else:
    print(1, 2)
    print(3, 4)