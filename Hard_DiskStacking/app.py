disks = [[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 3, 1], [4, 4, 5]]


def diskStacking(disks):
    # Write your code here.
    sortedDisks = sorted(disks, key=lambda x: x[2])
    heights = [x[2] for x in sortedDisks]

    for idx in range(1, len(sortedDisks)):
        for idy in range(0, idx):
            if (
                sortedDisks[idy][0] < sortedDisks[idx][0]
                and sortedDisks[idy][1] < sortedDisks[idx][1]
                and sortedDisks[idy][2] < sortedDisks[idx][2]
            ):
                heights[idx] = max(heights[idx], sortedDisks[idx][2] + heights[idy])

    currValue = max(heights)
    stack = []
    while currValue != 0:
        stack.insert(0, sortedDisks[heights.index(currValue)])
        currValue -= stack[0][2]
    return stack


print(diskStacking(disks))

"""
Input:
[[2,1,2],[3,2,3],[2,2,8],[2,3,4],[1,3,1],[4,4,5]]

Output:
[[2,1,2],[3,2,3],[4,4,5]]

Idea:
[[1,3,1],[2,1,2],[3,2,3],[2,3,4],[4,4,5],[2,2,8]]
input sorted by height: [1,2,3,4,5,8]
0:  [1,2,3,4,5,8]
1:  [1,2,3,4,5,8]
2:  [1,2,4,4,5,8] -> [1,2,5,4,5,8]
3:  [1,2,5,4,5,8]
4:  [1,2,5,4,6,8] -> [1,2,5,4,7,8] -> [1,2,5,4,10,8] -> [1,2,5,4,10,8]
5:  [1,2,5,4,10,8]
-> 10 -> idx: 4 ([4,4,5]) -> 10-5=5 -> idx:2 ([3,2,3]) -> 5-3=2 -> idx:1 ([2,1,2]) -> 2-2=0 -> insert(0)
-> [[2,1,2],[3,2,3],[4,4,5]]
"""
