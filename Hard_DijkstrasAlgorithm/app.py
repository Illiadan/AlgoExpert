start = 0
edges = [
    [[1, 7]],
    [[2, 6], [3, 20], [4, 3]],
    [[3, 14]],
    [[4, 2]],
    [],
    [],
]


def dijkstrasAlgorithm(start, edges):
    # Write your code here.
    sums = [float("inf") for x in range(len(edges))]
    sums[start] = 0
    visited = []

    while len(visited) != len(edges):
        print(sums)
        currMin = float("inf")
        currIdx = None
        for idx in range(len(sums)):
            if not idx in visited and sums[idx] <= currMin:
                currMin = sums[idx]
                currIdx = idx
        for edge in edges[currIdx]:
            sums[edge[0]] = min(sums[edge[0]], sums[currIdx] + edge[1])
        visited.append(currIdx)
    for idx in range(len(sums)):
        if sums[idx] == float("inf"):
            sums[idx] = -1

    return sums


print(dijkstrasAlgorithm(start, edges))

"""
Input:
start = 0
edges = [
    [[1, 7]],
    [[2, 6], [3, 20], [4, 3]],
    [[3, 14]],
    [[4, 2]],
    [],
    [],
]

Output:
[0,7,13,27,10,-1]

Idea:

"""
