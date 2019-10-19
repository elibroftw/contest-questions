def possible_combos():
    pass

t = int(input())
for case in range(t):
    n, h  = [int(x) for x in input().split()]
    a_arr = [int(x) for x in input().split()]
    b_arr = [int(x) for x in input().split()]
    combos = [ (a_arr[0], 0), (0, b_arr[0]), (a_arr[0], b_arr[0]) ]
    for i in range(1, n - 1):
        temp = []
        for combo in combos:
            # check if they are both happy
            # if they are, then just increase ways
            # by the total number of combinations for the rest of the shift
            # and then do not append to temp
            ai, bi = a_arr[i], b_arr[i]
            current_a, current_b = combo[0], combo[1]
            temp.append( (current_a + ai, current_b) )       # a works
            temp.append( (current_a, current_b + bi) )       # b works
            temp.append( (current_a + ai, current_b + bi) )  # both work
        combos = temp
    i = n - 1
    ai = a_arr[i]
    bi = b_arr[i]
    ways = 0
    # if False: pass
    if i == 0:
        for combo in combos:
            if combo[0] >= h and combo[1] >= h: ways += 1
    else:
        for combo in combos:
            current_a = combo[0]
            current_b = combo[1]
            op1 = current_a + ai
            op2 = current_b + bi
            if op1 >= h and current_b >= h: ways += 1
            if op2 >= h and current_a >= h: ways += 1
            if op1 >= h and op2 >= h:       ways += 1
        
    print('Case #', case + 1, ': ', ways, sep='')


