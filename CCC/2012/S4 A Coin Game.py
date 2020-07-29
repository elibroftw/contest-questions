# PASSES ALL TEST CASES ON CCC and DMOJ
# Lesson learned: use sets when order and index is not important,
# since a lookup for a set is O(1) v. list which is O(n)


def stack_empty(stack: str):
    """ returns whether the coin stack is empty """
    return stack == ''


def do_left(coin_lineup, coin_stack, centre_stack_index):
    i = centre_stack_index
    left_stack = coin_lineup[i - 1]
    if stack_empty(left_stack):
        return coin_lineup[:i - 1] + (coin_stack[0], coin_stack[1:]) + coin_lineup[i + 1:]
    elif int(coin_stack[0]) < int(left_stack[0]):
        return coin_lineup[:i - 1] + (coin_stack[0] + coin_lineup[i - 1], coin_stack[1:]) + coin_lineup[i + 1:]


def do_right(coin_lineup, coin_stack, centre_stack_index):
    # global coin_lineup, coin_stack
    i = centre_stack_index
    right_stack = coin_lineup[i + 1]
    if stack_empty(right_stack):
        return coin_lineup[:i] + (coin_stack[1:], coin_stack[0]) + coin_lineup[i + 2:]
    elif int(coin_stack[0]) < int(right_stack[0]):
        return coin_lineup[:i] + (coin_stack[1:], coin_stack[0] + coin_lineup[i + 1]) + coin_lineup[i + 2:]


def create_move(other_side, this_side_visited, new_lineup, new_configs):
    if new_lineup is not None:
        hashable = tuple(new_lineup)
        if hashable not in this_side_visited:
            if hashable in other_side:
                print(step)
                return True
            this_side_visited.add(hashable)
            new_configs.add(hashable)
    return False


n = 1
while n > 0:
    n = int(input())
    if n:
        start = input().split()
        final = tuple(sorted(start))

        start = tuple(start)
        lines_forward = {start}
        visited_from_start = {start}

        lines_backward = {final}
        visited_from_back = {final}

        step = 0
        done = start == final
        if done: print(step)

        while not done:
            step += 1
            new_configs = set()
            for coin_lineup in lines_forward:
                if done: break
                for i, coin_stack in enumerate(coin_lineup):
                    if coin_stack:
                        if i > 0:
                            possible_lineup = do_left(coin_lineup, coin_stack, i)
                            done = create_move(lines_backward, visited_from_start, possible_lineup, new_configs)
                            if done: break
                        if i < n - 1:
                            possible_lineup = do_right(coin_lineup, coin_stack, i)
                            done = create_move(lines_backward, visited_from_start, possible_lineup, new_configs)
                            if done: break
            lines_forward = new_configs.copy()

            step += 1
            new_configs = set()
            for coin_lineup in lines_backward:
                if done: break
                for i, coin_stack in enumerate(coin_lineup):
                    if coin_stack:
                        if i > 0:
                            possible_lineup = do_left(coin_lineup, coin_stack, i)
                            done = create_move(lines_forward, visited_from_back, possible_lineup, new_configs)
                            if done: break
                        if i < n - 1:
                            possible_lineup = do_right(coin_lineup, coin_stack, i)
                            done = create_move(lines_forward, visited_from_back, possible_lineup, new_configs)
                            if done: break
            lines_backward = new_configs.copy()

            if not lines_forward and not lines_backward:
                print('IMPOSSIBLE')
                done = True
                break
