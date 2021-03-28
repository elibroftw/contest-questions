from contextlib import suppress


def tourism(n, k, attractions):
    # from https://github.com/zecookiez/CanadianComputingCompetition/blob/master/2019/Senior/tourism.cpp
    # NOTE: this solution was converted to Python, not made with a Pythonic mindest,
    #  the other two functions need to be optimized to work but are more Pythonic
    rmq = [0 for _ in range(n + 1)]
    dp = [0 for _ in range(n + 1)]
    # keep track of the highest scores following buckets of k
    for i in range(0, n, k):
        rmq[i] = attractions[i];
        for j in range(i + 1, min(n, i + k)):
            rmq[j] = max(rmq[j - 1], attractions[j])

    for j in range(0, n, k):
        # for each kth day...
        cur_max = attractions[j]
        c = 0
        for i in range(min(n - 1, j + k - 1), j - 1, -1):
            if cur_max <= rmq[i + 1]: dp[i] = dp[i + 1] - rmq[i + 1] + rmq[i]  # special case
            else: dp[i] = dp[i + 1]
            while(j - c >= max(0, i - k + 1)):
                assert j >= c
                cur_max = max(cur_max, attractions[j - c])
                dp[i] = max(dp[i], max(rmq[i], cur_max) + (0 if j == c else dp[j - c - 1]))
                c += 1
    return dp[n - 1]


def bfs_tourism(n, k, attractions: list):
    max_score = 0
    # [1, 2, 3, 4, 5, 6, 7, 8 ,9, 10] n = 10, k = 4
    scenarios = {0: 0}  # index: score
    maxes = {}
    # helper to cache min visits
    def get_max(start, end):
        if (start, end) not in maxes:
            maxes[(start, end)] = max(attractions[start:end])
        return maxes[(start, end)]

    while scenarios:
        new_scenarios = {}
        for index, score in scenarios.items():
            # the minimum visits to make to hold min. days condition
            visits_to_make = (n - index) % k
            if visits_to_make == 0: visits_to_make = k
            # the index of the last attraction of the day that must be visited
            min_visit_index = visits_to_make + index - 1
            cur_max = get_max(index, min_visit_index + 1)
            # TODO: Optimize for [3, 4, 3, 2, 1] n = 5, k = 4
            #   "Convex Hull Techhnique"
            for i in range(min_visit_index, min(index + k, n)):
                if attractions[i] > cur_max: cur_max = attractions[i]
                # minimum days used condition is met
                updated_score = score + cur_max
                new_index = i + 1
                if new_index == n:
                    # visited all attractions; update max_score
                    if updated_score > max_score: max_score = updated_score
                elif updated_score > new_scenarios.get(new_index, 0):
                    # keep only the highest score attained by the new index
                    new_scenarios[new_index] = updated_score
        scenarios = new_scenarios
    return max_score



def dp_tourism(n, k, attractions: list, start=0):
    """
    k: max attraction visits in a day
    n: number of attractions
    attractions: attraction scores
    return: maximum score in the fewsest days possible

    DP Guide:
    dp[i]: the max score of attractions[:i]
    Optimization Needed:
    Maintain only relevant maximums (convex hull) and skip the useless ones
    """
    lookup = {}
    def solver(state):
        if state in lookup:
            return lookup[state]
        if state == 1:
            lookup[state] = attractions[0]
            return lookup[state]
        if state <= k:
            lookup[state] = max(attractions[:state])
            return lookup[state]
        # max score at attraction #state
        #  needs to hold the condition that we are using the lowest number of days
        #  e.g. the day that attraction #state is visited,
        #   minimum of (state % k ? state % k : k) attractions were visited
        #   maximum of k days were visited

        # day score is at least the max of attractions definitely visited
        j = state % k
        if j == 0: j = k
        try:
            lookup[state] = day_score = max(attractions[state - j:state])
        except ValueError:
            lookup[state] = day_score = attractions[state - 3:state]

        # max score = day_score + prev_day_score [aka. lookup[prev_day]]
        # find the prev day that maximises max score
        # prev day is limited to max(0, state - k)

        for i in range(state - j, max(state - k, 0) -1, -1):
            with suppress(IndexError):
                if attractions[i] > day_score: day_score = attractions[i]
            # if the max score of the state can be beaten if we rearrange the composition
            #  update the max score possible
            if solver(i) + day_score > lookup[state]:
                lookup[state] = solver(i) + day_score
        return lookup[state]
    return solver(n)


if __name__ == "__main__":
    n, k = [int(x) for x in input().split()]
    attractions = [int(x) for x in input().split()]
    print(tourism(n, k, attractions))
