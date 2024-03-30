array = [[1, 3, 4, 10], [2, 5, 9, 11], [6, 8, 12, 15], [7, 13, 14, 16]]
"""
1   3   4   10 
2   5   9   11
6   8   12  15
7   13  14  16
"""


def zigzagTraverse(array):
    # Write your code here.
    row = 0
    col = 0
    maxRow = len(array)
    maxCol = len(array[0])
    downwards = True
    out = []

    while row != maxRow and col != maxCol:
        out.append(array[row][col])

        if downwards:
            if row == maxRow - 1:
                col += 1
                downwards = False
            elif col == 0:
                row += 1
                downwards = False
            else:
                row += 1
                col -= 1
        else:
            if col == maxCol - 1:
                row += 1
                downwards = True
            elif row == 0:
                col += 1
                downwards = True
            else:
                row -= 1
                col += 1

    return out


print(zigzagTraverse(array))

"""
Input:
[[1, 3, 4, 10], [2, 5, 9, 11], [6, 8, 12, 15], [7, 13, 14, 16]]
1   3   4   10 
2   5   9   11
6   8   12  15
7   13  14  16

Output:
[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

Idea:
NxM array
start: top-left
2nd: one down
end: bottom-right
0,0 1,0 0,1 0,2 1,1 2,0 3,0 2,1 1,2 0,3 1,3 2,2 3,1 3,2 2,3 3,3
0: 0,0
1: 1,0 0,1
2: 0,2 1,1 2,0
3: 3,0 2,1 1,2 0,3
4: 1,3 2,2 3,1
5: 3,2 2,3
6: 3,3
"""
