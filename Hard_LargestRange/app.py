array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]

# O(n log n) time | O(n) space
def largestRange(array):
    # Write your code here.
    sortedArray = sorted(array)
    start = sortedArray[0]
    end = sortedArray[0]
    length = 1
    currNumber = sortedArray[0]
    currStart = sortedArray[0]
    currEnd = sortedArray[0]
    currLength = 1
    for idx in range(1, len(sortedArray)):
        if sortedArray[idx] == currNumber or sortedArray[idx] == currNumber + 1:
            currEnd = sortedArray[idx]
            currLength = currEnd - (currStart - 1)
        else:
            if currLength > length:
                start = currStart
                end = currEnd
                length = currLength
            currStart = sortedArray[idx]
            currEnd = sortedArray[idx]
            currLength = 1
        currNumber = sortedArray[idx]

    if currLength > length:
        start = currStart
        end = currEnd
        length = currLength
    return [start, end]


print(largestRange(array))

""""
Input:
[1,11,3,0,15,5,2,4,10,7,12,6]

Output:
[0,7]

Idea:
[0,1,2,3,4,5,6,7,10,11,12,15]
"""
