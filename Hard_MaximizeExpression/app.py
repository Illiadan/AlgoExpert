array = [3, 6, 1, -3, 2, 7]
array2 = [40, 30, 1, 10, 9, 3]


def maximizeExpression(array):
    # Write your code here.
    if len(array) < 4:
        return 0
    else:
        outA = [array[0]]
        for idx in range(1, len(array)):
            if idx < len(array) - 3:
                outA.append(max(outA[-1], array[idx]))
            else:
                outA.append(None)
        outAB = [None, outA[0] - array[1]]
        for idx in range(2, len(array)):
            if idx < len(array) - 2:
                outAB.append(max(outAB[-1], outA[idx - 1] - array[idx]))
            else:
                outAB.append(None)
        outABC = [None, None, outAB[1] + array[2]]
        for idx in range(3, len(array)):
            if idx < len(array) - 1:
                outABC.append(max(outABC[-1], outAB[idx - 1] + array[idx]))
            else:
                outABC.append(None)
        outABCD = [None, None, None, outABC[2] - array[3]]
        for idx in range(4, len(array)):
            outABCD.append(max(outABCD[-1], outABC[idx - 1] - array[idx]))
        return max(outABCD[3:])


print(maximizeExpression(array2))

"""
Input:
[3,6,1,-3,2,7]

Output:
4

Idea:
len(array)<4: return 0
out = array[a] - array[b] + array[c] - array[d]
-> Indices!!! a<b<c<d & out max.
A-B+C-D

A:          [3,6,6,None,None,None]
A-B:        [None,-3,5,9,None,None]
A-B+C:      [None,None,-2,2,11,None]
A-B+C-D:    [None,None,None,1,0,4]
"""
