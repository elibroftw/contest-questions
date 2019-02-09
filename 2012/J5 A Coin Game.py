n = 1
while n > 0:
    n = int(input())
    if n:
        start = input().split(' ')
        configs = [[start, 0]]
        final = sorted(start)
        visited = [start]
        done = False
        while not done:
            new_configs = []
            for config in configs:  # config: [['1', '2'], STEP]
                step = config[1]
                if config[0] == final:
                    print(step)
                    done = True
                    break
                else:
                    positions = config[0]
                    for i, position in enumerate(positions):
                        try:
                            first = position[0]
                            new_config = []
                            if i > 0:
                                left = positions[i - 1]
                                if not left or first < positions[i - 1][0]:

                                    left = first + left

                                    new_config = positions[:i - 1].copy()
                                    new_config.append(left)
                                    new_config.append(position[1:])
                                    new_config.extend(positions[i + 1:].copy())

                                    if new_config:
                                        if new_config not in visited:
                                            new_configs.append([new_config.copy(), step + 1])
                                            visited.append(new_config.copy())
                            new_config = []
                            if i < n - 1:
                                right = positions[i + 1]
                                if not right or first < positions[i + 1][0]:

                                    right = first + right
                                    new_config = positions[:i].copy()  # up to i
                                    new_config.append(position[1:])  # add i
                                    new_config.append(right)
                                    new_config.extend(positions[i+2:].copy())
                                    if new_config:
                                        if new_config not in visited:
                                            new_configs.append([new_config.copy(), step + 1])
                                            visited.append(new_config.copy())

                        except IndexError:
                            continue

            if len(configs) == 0:
                print('IMPOSSIBLE')
                done = True
                break
            else:
                configs = new_configs.copy()
