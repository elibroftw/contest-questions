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


# using tuples and deques instead of sets to keep track of lineups
# requires bidirectional search to be more optimal
# from queue import deque
# # use a stack to keep track of configuartions

# def run_bfs(starting_lineup: tuple, size: int):
#     # returns minimum_moves: int | 'IMPOSSIBLE': str
#     # starting_lineup: (tuple of tuples of int) ; tuple of coin stacks
#     # assume first coin is the top of a coin stack
#     # use a queue for keeping track of the lineups (FIFO)
#     final_lineup = tuple(sorted(starting_lineup))
#     # base case
#     if starting_lineup == final_lineup: return 0
#     # todo: bidirectional search
#     lines_forward, lines_backward = deque((starting_lineup,)), deque((final_lineup,))
#     new_lines_forward, new_lines_backward = deque(), deque()
#     visited_forward, visited_backward = {starting_lineup}, {final_lineup}
#     steps = 1
#     while True:
#         if not lines_forward:
#             if not new_lines_forward:
#                 break
#             lines_forward, new_lines_forward = new_lines_forward, lines_forward
#             steps += 1
#         lineup = lines_forward.popleft()
#         # for each position, try moving top coin left or right
#         for i, coin_stack in enumerate(lineup):
#             if coin_stack:
#                 if i > 0:
#                     # try moving top of stack to the left
#                     left_of_i = lineup[i - 1]
#                     if not left_of_i or left_of_i[0] >= coin_stack[0]:
#                         # valid to move the coin left
#                         left_of_i = (coin_stack[0],) + left_of_i
#                         possible_lineup = lineup[:i - 1] + (left_of_i,) + (lineup[i][1:],) + lineup[i + 1:]
#                         if possible_lineup not in visited_forward:
#                             if possible_lineup == final_lineup:
#                                 return steps
#                             visited_forward.add(possible_lineup)
#                             new_lines_forward.append(possible_lineup)
#                 if i < size - 1:
#                     # try moving top of stack to the right
#                     right_of_i = lineup[i + 1]
#                     if not right_of_i or right_of_i[0] >= coin_stack[0]:
#                         # valid to move the coin right
#                         right_of_i = (coin_stack[0],) + right_of_i
#                         possible_lineup = lineup[:i] + (lineup[i][1:],) + (right_of_i,) + lineup[i + 2:]
#                         if possible_lineup not in visited_forward:
#                             if possible_lineup == final_lineup:
#                                 return steps
#                             visited_forward.add(possible_lineup)
#                             new_lines_forward.append(possible_lineup)
#     return 'IMPOSSIBLE'


while True:
    n = int(input())
    if n == 0:
        break
    starting_lineup = tuple(input().split())
    print(analyze_test_case(starting_lineup))
    # lineup = tuple(((pos,) for pos in input().split()))
    # print(run_bfs(lineup, n))
