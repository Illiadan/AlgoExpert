scores = [8, 4, 2, 1, 3, 6, 7, 9, 5]
scores2 = [5, 3, 4, 2, 1, 6, 9, 7, 8]  # [2,1,3,2,1,2,3,1,2]
scores3 = [1]


def minRewards(scores):
    # Write your code here.
    reward = [None] * len(scores)
    connections = {}
    minIndices = {}

    for idx in range(len(scores)):
        if idx - 1 < 0:
            left = 0
        else:
            left = -1 if scores[idx - 1] < scores[idx] else 1
        if idx + 1 > len(scores) - 1:
            right = 0
        else:
            right = -1 if scores[idx + 1] < scores[idx] else 1
        connections[idx] = [left, right]
        if left + right > 0 or (left == 0 and right == 0):
            minIndices[idx] = None

    for idx in minIndices:
        res = 0
        for idy in range(idx - 1, -1, -1):
            if connections[idy][1] != -1:
                break
            res += 1
        for idy in range(idx + 1, len(scores)):
            if connections[idy][0] != -1:
                break
            res += 1
        minIndices[idx] = res

    minIdx = sorted(minIndices.keys(), key=lambda x: minIndices[x], reverse=True)
    for idx in minIdx:
        reward[idx] = 1

    for idx in minIdx:
        idy = idx - 1
        while idy >= 0:
            if not reward[idy] == None or not connections[idy + 1][0] == 1:
                break
            reward[idy] = reward[idy + 1] + connections[idy + 1][0]
            idy -= 1
        idy = idx + 1
        while idy < len(scores):
            if not reward[idy] == None or not connections[idy - 1][1] == 1:
                break
            reward[idy] = reward[idy - 1] + connections[idy - 1][1]
            idy += 1
    print(f"{sum(reward)} :: {reward}")
    return sum(reward)


print(minRewards(scores))

"""
Input:
[8, 4, 2, 1, 3, 6, 7, 9, 5]

Output:
25 [4,3,2,1,2,3,4,5,1]

Idea:
{
    0: [0,-1]   -> 4
    1: [1,-1]   -> 3
    2: [1,-1]   -> 2
    3: [1,1]    -> 1
    4: [-1,1]   -> 2
    5: [-1,1]   -> 3
    6: [-1,1]   -> 4 
    7: [-1,-1]  -> 5
    8: [1,0]    -> 1
}
"""
