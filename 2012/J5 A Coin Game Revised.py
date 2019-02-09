n = 1
# TODO: implement Bidirectional search
def create_move(new):
    global done
    if new is not None and new not in visited:
        visited.append(new_positions)
        new_configs.append([new_positions , step + 1])
        if new_positions == final:
            print(step + 1)
            done = True
            return True
    return False


while n > 0:
    n = int(input())
    if n:
        start = input().split(' ')
        configs = [[start, 0]]  # formation, step
        final = sorted(start)
        visited = [start]
        done = False
        while not done:
            new_configs = []
            for config in configs:
                if done: break

                step = config[1]
                positions = config[0]
                # print(step, positions)  # DEBUG statement
                if positions == final:
                    print(step)
                    done = True
                    break
                else:
                    #  [3, 2, 1]
                    for i, pos in enumerate(positions):
                        if done: break
                        if pos == '': continue

                        left = i - 1
                        if left >= 0:
                            new_positions = None
                            left = positions[left]
                            if left == '':
                                new_positions = positions[:i - 1] + [pos[0]] + [pos[1:]] + positions[i + 1:]
                            elif int(pos[0]) < int(left[0]):
                                new_positions = positions[:i - 1] + [pos[0] + positions[i - 1]] + [pos[1:]] + positions[i + 1:]                            
                            if create_move(new_positions): break
                        
                        right = i + 1
                        if right < n:
                            new_positions = None
                            right = positions[right]
                            if right == '':
                                new_positions = positions[:i] + [pos[1:]] + [pos[0]] + positions[i + 2:]
                            elif int(pos[0]) < int(right[0]):
                                new_positions = positions[:i] + [pos[1:]] + [pos[0] + positions[i + 1]] + positions[i + 2:]
                            if create_move(new_positions): break

            if len(configs) == 0:
                print('IMPOSSIBLE')
                done = True
                break
            else:
                configs = new_configs.copy()
