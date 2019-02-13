from time import time
# DOES NOT WORK FOR TEST CASE 2 in J5 and S4. I'm not sure if this is uWaterloo's mistake or mine
# Also this is not fully optimized as it TLE on DMOJ S4
n = 1


def create_move(other_side, this_side_visited):
    global done, new_configs, new_positions
    if new_positions is not None:
        hashable = '/'.join(new_positions)
        if hashable not in this_side_visited:
            this_side_visited.add(hashable)
            new_configs.append(new_positions)
            if new_positions in other_side:
                print(step)
                done = True
                return True
    return False


def check_if_done(look_for, look_in):
    global done
    if look_for in look_in:
        print(step)
        done = True
        return True
    return done


to_int = int
get_length = len

while n > 0:
    n = to_int(input())
    if n:
        start_time = time()
        step = 0
        start = input().split(' ')
        final = sorted(start)

        forward_configs = [start]
        visited_from_start = {'/'.join(start)}

        backward_configs = [final]
        visited_from_back = {'/'.join(final)}

        if start == final:
            print(step)
            done = True
        else:
            done = False

        while not done:
            step += 1
            new_configs = []
            for positions in forward_configs:
                if check_if_done(positions, backward_configs):
                    break
                else:
                    for i, pos in enumerate(positions):
                        if done:
                            break
                        if pos == '':
                            continue

                        left = i - 1
                        if left >= 0:
                            new_positions = None
                            left = positions[left]
                            if left == '':
                                new_positions = positions[:i - 1] + \
                                                [pos[0]] + [pos[1:]] + positions[i + 1:]
                            elif to_int(pos[0]) < to_int(left[0]):
                                new_positions = positions[:i - 1] + [
                                    pos[0] + positions[i - 1]] + [pos[1:]] + positions[i + 1:]
                            if create_move(backward_configs, visited_from_start):
                                break

                        right = i + 1
                        if right < n:
                            new_positions = None
                            right = positions[right]
                            if right == '':
                                new_positions = positions[:i] + [pos[1:]] + [pos[0]] + positions[i + 2:]
                            elif to_int(pos[0]) < to_int(right[0]):
                                new_positions = positions[:i] + [pos[1:]] + [
                                    pos[0] + positions[i + 1]] + positions[i + 2:]
                            if create_move(backward_configs, visited_from_start):
                                break
            forward_configs = new_configs.copy()
            step += 1
            new_configs = []
            for positions in backward_configs:
                # print(step, positions)  # DEBUG statement
                if check_if_done(positions, forward_configs):
                    break
                else:
                    for i, pos in enumerate(positions):
                        if done:
                            break
                        if pos == '':
                            continue

                        left = i - 1
                        if left >= 0:
                            new_positions = None
                            left = positions[left]
                            if left == '':
                                new_positions = positions[:i - 1] + [pos[0]] + [pos[1:]] + positions[i + 1:]
                            elif to_int(pos[0]) < to_int(left[0]):
                                new_positions = positions[:i - 1] + [
                                    pos[0] + positions[i - 1]] + [pos[1:]] + positions[i + 1:]
                            if create_move(forward_configs, visited_from_back):
                                break

                        right = i + 1
                        if right < n:
                            new_positions = None
                            right = positions[right]
                            if right == '':
                                new_positions = positions[:i] + [pos[1:]] + [pos[0]] + positions[i + 2:]
                            elif to_int(pos[0]) < to_int(right[0]):
                                new_positions = positions[:i] + [pos[1:]] + [
                                    pos[0] + positions[i + 1]] + positions[i + 2:]
                            if create_move(forward_configs, visited_from_back):
                                break
            backward_configs = new_configs.copy()

            if get_length(forward_configs) == get_length(backward_configs) == 0:
                print('IMPOSSIBLE')
                done = True
                break
        # print(time() - start_time)
