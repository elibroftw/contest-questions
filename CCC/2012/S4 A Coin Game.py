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
            if hashable in other_side: return True
            this_side_visited.add(hashable)
            new_configs.add(hashable)
    return False


def make_moves(lineups, opposite_lineups, visited):
    new_lineups = set()
    for coin_lineup in lineups:
        for i, coin_stack in enumerate(coin_lineup):
            if coin_stack:
                if i > 0:
                    possible_lineup = do_left(coin_lineup, coin_stack, i)
                    if create_move(opposite_lineups, visited, possible_lineup, new_lineups):
                        return True
                if i < n - 1:
                    possible_lineup = do_right(coin_lineup, coin_stack, i)
                    if create_move(opposite_lineups, visited, possible_lineup, new_lineups):
                        return True
    return new_lineups


def analyze_test_case(starting_lineup: tuple):
    final_lineup = tuple(sorted(starting_lineup))
    lines_forward = {starting_lineup}
    visited_from_start = {starting_lineup}

    lines_backward = {final_lineup}
    visited_from_back = {final_lineup}

    steps = 0
    if starting_lineup == final_lineup: return steps

    while True:
        steps += 1
        if steps % 2:
            lines_forward = make_moves(lines_forward, lines_backward, visited_from_start)
            if lines_forward == True: return steps
        else:
            lines_backward = make_moves(lines_backward, lines_forward, visited_from_back)
            if lines_backward == True: return steps
        if not lines_forward and not lines_backward:
            return 'IMPOSSIBLE'
n = 1
while n > 0:
    n = int(input())
    if n:
        starting_lineup = tuple(input().split())
        print(analyze_test_case(starting_lineup))
