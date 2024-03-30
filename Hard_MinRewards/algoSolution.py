scores = [8, 4, 2, 1, 3, 6, 7, 9, 5]
scores2 = [5, 3, 4, 2, 1, 6, 9, 7, 8]  # [2,1,3,2,1,2,3,1,2]
scores3 = [1]


def minRewards(scores):
    # Write your code here.
    reward = [1 for _ in scores]

    for idx in range(1, len(scores)):
        if scores[idx] > scores[idx - 1]:
            reward[idx] = reward[idx - 1] + 1
    for idx in range(len(scores) - 2, -1, -1):
        if scores[idx] > scores[idx + 1]:
            reward[idx] = max(reward[idx], reward[idx + 1] + 1)

    print(f"{sum(reward)} :: {reward}")
    return sum(reward)


print(minRewards(scores))
