matrix = [[5, 3, -1, 5], [-7, 3, 7, 4], [12, 8, 0, 0], [1, -8, -8, 2]]
size = 2


def maximumSumSubmatrix(matrix, size):
    # Write your code here.
    sums = []
    for idx in range(len(matrix) - (size - 1)):
        for idy in range(len(matrix[0]) - (size - 1)):
            value = 0
            for idz in range(size):
                value += sum(matrix[idx + idz][idy : idy + size])
            sums.append(value)
    return max(sums)


print(maximumSumSubmatrix(matrix, size))

"""
Input:
[
    [5,3,-1,5],
    [-7,3,7,4],
    [12,8,0,0],
    [1,-8,-8,2]
]
2

Output:
18

Idea:

"""
