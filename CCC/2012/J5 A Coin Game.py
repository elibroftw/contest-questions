# PASSES ALL TEST CASES ON CCC and DMOJ
# Lesson learned: use sets when order and index is not important,
# since a lookup for a set is O(1) v. list which is O(n)


def do_left(left):
    global new_positions, coin_lineup, coin_stack
    new_positions = None
    left = coin_lineup[left]
    if left == '':
        new_positions = coin_lineup[:i - 1] + (coin_stack[0],) + (coin_stack[1:],) + coin_lineup[i + 1:]
    elif int(coin_stack[0]) < int(left[0]):
        new_positions = coin_lineup[:i - 1] + (coin_stack[0] + coin_lineup[i - 1],) + (coin_stack[1:],) + coin_lineup[i + 1:]

def do_right(right):
    global new_positions
    new_positions = None
    right = coin_lineup[right]
    if right == '':
        new_positions = coin_lineup[:i] + (coin_stack[1:],) + (coin_stack[0],) + coin_lineup[i + 2:]
    elif int(coin_stack[0]) < int(right[0]):
        new_positions = coin_lineup[:i] + (coin_stack[1:],) + (coin_stack[0] + coin_lineup[i + 1],) + coin_lineup[i + 2:]


def create_move(other_side, this_side_visited):
    global done, new_configs, new_positions
    if new_positions is not None:
        hashable = tuple(new_positions)
        if hashable not in this_side_visited:
            if hashable in other_side:
                print(step)
                done = True
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
                # positions = positions.split(' ')
                if done: break
                for i, coin_stack in enumerate(coin_lineup):
                    if coin_stack:
                        if i > 0:
                            do_left(i - 1)
                            if create_move(lines_backward, visited_from_start):
                                break

                        if i < n - 1:
                            do_right(i + 1)
                            if create_move(lines_backward, visited_from_start):
                                break
            lines_forward = new_configs.copy()

            step += 1
            new_configs = set()
            for coin_lineup in lines_backward:
                if done: break
                # positions = positions.split(' ')
                for i, coin_stack in enumerate(coin_lineup):
                    if coin_stack:
                        if i > 0:
                            do_left(i - 1)
                            if create_move(lines_forward, visited_from_back):
                                break

                        if i < n - 1:
                            do_right(i + 1)
                            if create_move(lines_forward, visited_from_back):
                                break

            lines_backward = new_configs.copy()

            if not lines_forward and not lines_backward:
                print('IMPOSSIBLE')
                done = True
                break
