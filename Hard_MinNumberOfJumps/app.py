array = [3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]


def minNumberOfJumps(array):
    # Write your code here.
    jumps = 0
    if len(array) == 1:
        return jumps
    currIdx = 0
    while currIdx + array[currIdx] < len(array) - 1:
        print(f"{currIdx} + {array[currIdx]} <-> {len(array)-1}")
        currMax = 0
        tempIdx = 0
        for idx in range(currIdx + 1, currIdx + array[currIdx] + 1):
            print(f"{currMax} <-> {idx} + {array[idx]}")
            if currMax < idx + array[idx]:
                currMax = idx + array[idx]
                tempIdx = idx
        currIdx = tempIdx
        jumps += 1
    return jumps + 1


print(minNumberOfJumps(array))

"""
Input:
[3,4,2,1,2,3,7,1,1,1,3]

Output:
4

Idea:
0+3: -> 1+4,2+2,3+1 -> 1+4: -> 2+2,3+1,4+2,5+3 -> 5+3: -> 6+7,7+1,8+1 -> 6+7: >=len(array)-1
"""
