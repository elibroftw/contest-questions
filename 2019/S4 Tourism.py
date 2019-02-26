from math import ceil
# max of k
# make a path for taking each one
# not perfect solution
n, k = (int(x) for x in input().split())
attractions = [int(x) for x in input().split()]
combos = [(0, attractions)]  # score_so_far, attractions_left
fewest_days = ceil(n / k)
if n == k:
    print(max(attractions))
else:
    new_combos = []
    final_scores = []
    day = 0
    while not final_scores:
        day += 1
        for combo in combos:
            score_so_far, attractions_left = combo
            minimum_attractions = ceil(len(attractions_left) / (fewest_days - day) / k)
            if not minimum_attractions:
                final_scores.append(score_so_far + max(attractions_left))
            else:
                for i in range(minimum_attractions, min(k + 1, len(attractions_left) + 1)):
                    new_attractions_left = attractions_left[i:]
                    new_score = score_so_far + max(attractions_left[:i])
                    if new_attractions_left:
                        new_combo = (new_score, new_attractions_left)
                        new_combos.append(new_combo)
                    else:
                        final_scores.append(new_score)
        combos = new_combos.copy()
    print(max(final_scores))
