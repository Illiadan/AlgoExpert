matrix = [[0, -1, -3, 2, 0], [1, -2, -5, -1, -3], [3, 0, 0, -4, -1]]


# O(h*w) time | O(h*w) space
def minimumPassesOfMatrix(matrix):
    """Function takes in an integer matrix of potentially unequal height and width and returns
    the number of passes until all elements of the matrix are non-negative.
    A single pass through the matrix involves converting all negative integers that can be 
    converted at that point in time.
    A conversion from negative to positive integer has to be done by multiplying with -1 and
    is only allowed if the negative integer is adjacent to one or more positive integers.
    Adjacent in this sense means, to the left, to the right, above and below of the current element.
    0 is neither negative nor positive."""
    listOfNegatives = []
    listOfPositives = []
    for idy in range(len(matrix)):
        currNeg = []
        currPos = []
        for idx in range(len(matrix[idy])):
            if matrix[idy][idx] > 0:
                currPos.append(idx)
            elif matrix[idy][idx] < 0:
                currNeg.append(idx)
        listOfPositives.append(currPos)
        listOfNegatives.append(currNeg)
    if any(listOfNegatives) is False:
        return 0
    elif any(listOfPositives) is False:
        return -1
    else:
        return singlePassThroughMatrix(listOfPositives,
                                       listOfNegatives,
                                       len(matrix),
                                       len(matrix[0]),
                                       passCount=1)


def singlePassThroughMatrix(pos, neg, height, width, passCount):
    newPos = [[] for _ in range(height)]
    newNeg = neg
    for idy in range(len(pos)):
        for idx in range(len(pos[idy])):
            currValue = pos[idy][idx]
            if idy > 0 and currValue in neg[idy - 1]:
                newNeg[idy - 1].remove(currValue)
                newPos[idy - 1].append(currValue)
            if idy < height - 1 and currValue in neg[idy + 1]:
                newNeg[idy + 1].remove(currValue)
                newPos[idy + 1].append(currValue)
            if currValue > 0 and currValue - 1 in neg[idy]:
                newNeg[idy].remove(currValue - 1)
                newPos[idy].append(currValue - 1)
            if currValue < width - 1 and currValue + 1 in neg[idy]:
                newNeg[idy].remove(currValue + 1)
                newPos[idy].append(currValue + 1)
    if any(newNeg) is False:
        return passCount
    elif any(newPos) is False:
        return -1
    else:
        return singlePassThroughMatrix(newPos, newNeg, height, width,
                                       passCount + 1)


result = minimumPassesOfMatrix(matrix)
print(result)
"""
0   -1  -3  2   0   ->  neg's:  [[1,2],[1,2,3,4],[3,4]]
1   -2  -5  -1  -3  ->  pos's:  [[3],[0],[0]]
3   0   0   -4  -1              3:  newPos [[2],[3],[]]     newNeg [[1],[1,2,4],[3,4]]
                                0:  newPos [[2],[3,1],[]]   newNeg [[1],[2,4],[3,4]]
                                0:  newPos [[2],[3,1],[]]   newNeg [[1],[2,4],[3,4]]

0  -1   3  2   0    ->  neg:    [[1],[2,4],[3,4]]                
1   2  -5  1  -3    ->  pos:    [[2],[3,1],[]]
3   0   0 -4  -1                2:  newPos [[1],[2],[]]     newNeg [[],[4],[3,4]]
                                3:  newPos [[1],[2,4],[3]]  newNeg [[],[],[4]]
                                1:  newPos [[1],[2,4],[3]]  newNeg [[],[],[4]]

0  1  3  2  0       ->  neg:    [[],[],[4]]
1  2  5  1  3       ->  pos:    [[1],[2,4],[3]]
3  0  0  4 -1                   1:  newPos [[],[],[]]  newNeg [[],[],[4]]
                                2:  newPos [[],[],[]]  newNeg [[],[],[4]]
                                4:  newPos [[],[],[4]]  newNeg [[],[],[]]
0  1  3  2  0
1  2  5  1  3
3  0  0  4  1
"""
