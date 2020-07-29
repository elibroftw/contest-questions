# PASSES ALL TEST CASES ON CCC and DMOJ
# Lesson learned: use sets when order and index is not important,
# since a lookup for a set is O(1) v. list which is O(n)


def do_left(left):
    global new_positions
    new_positions = None
    left = positions[left]
    if left == '':
        new_positions = positions[:i - 1] + (pos[0],) + (pos[1:],) + positions[i + 1:]
    elif to_int(pos[0]) < to_int(left[0]):
        new_positions = positions[:i - 1] + (pos[0] + positions[i - 1],) + (pos[1:],) + positions[i + 1:]

def do_right(right):
    global new_positions
    new_positions = None
    right = positions[right]
    if right == '':
        new_positions = positions[:i] + (pos[1:],) + (pos[0],) + positions[i + 2:]
    elif to_int(pos[0]) < to_int(right[0]):
        new_positions = positions[:i] + (pos[1:],) + (pos[0] + positions[i + 1],) + positions[i + 2:]


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


to_int = int
get_length = len
n = 1

while n > 0:
    n = to_int(input())
    if n:
        start = input().split()
        final = tuple(sorted(start))

        start = tuple(start)
        forward_configs = {start}
        visited_from_start = {start}

        backward_configs = {final}
        visited_from_back = {final}

        step = 0
        done = start == final
        if done: print(step)

        while not done:
            step += 1
            new_configs = set()
            for positions in forward_configs:
                # positions = positions.split(' ')
                if done: break
                for i, pos in enumerate(positions):
                    if pos:
                        if i > 0:
                            do_left(i - 1)
                            if create_move(backward_configs, visited_from_start):
                                break

                        if i < n - 1:
                            do_right(i + 1)
                            if create_move(backward_configs, visited_from_start):
                                break
            forward_configs = new_configs.copy()

            step += 1
            new_configs = set()
            for positions in backward_configs:
                if done: break
                # positions = positions.split(' ')
                for i, pos in enumerate(positions):
                    if pos:
                        if i > 0:
                            do_left(i - 1)
                            if create_move(forward_configs, visited_from_back):
                                break

                        if i < n - 1:
                            do_right(i + 1)
                            if create_move(forward_configs, visited_from_back):
                                break

            backward_configs = new_configs.copy()

            if not forward_configs and not backward_configs:
                print('IMPOSSIBLE')
                done = True
                break
