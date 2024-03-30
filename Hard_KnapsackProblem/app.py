items = [[1, 2], [4, 3], [5, 6], [6, 7]]
capacity = 10


def knapsackProblem(items, capacity):
    # Write your code here.
    # return [
    #   10, // total value
    #   [1, 2], // item indices
    # ]
    values = [[0 for x in range(capacity + 1)] for y in range(len(items) + 1)]

    for idx in range(len(items)):
        for idy in range(capacity + 1):
            if idy < items[idx][1]:
                values[idx + 1][idy] = values[idx][idy]
            else:
                values[idx + 1][idy] = max(
                    items[idx][0] + values[idx][idy - items[idx][1]], values[idx][idy]
                )

    x = len(values) - 1
    y = len(values[0]) - 1
    maxValue = values[x][y]
    neededItems = []

    while x != 0 and y != 0:
        currValue = values[x][y]
        if values[x - 1][y] == currValue:
            x -= 1
        else:
            neededItems.append(x - 1)
            y -= items[x - 1][1]
            x -= 1

    return [maxValue, neededItems]


print(knapsackProblem(items, capacity))

"""
Input:
[[1,2], [4,3], [5,6], [6,7]]
10

Output:
[10,[1,3]]

Idea:
        0   1   2   3   4   5   6   7   8   9   10
[]      0   0   0   0   0   0   0   0   0   0   0      
[1,2]   0   0   1   1   1   1   1   1   1   1   1
[4,3]   0   0   1   4   4   5   5   5   5   5   5
[5,6]   0   0   1   4   4   5   5   5   6   9   9
[6,7]   0   0   1   4   4   5   5   6   6   9   10
-> 10 -> [[6,7], [4,3]]
-> [10, [1,3]]
"""
