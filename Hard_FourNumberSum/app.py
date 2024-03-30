array = [7, 6, 4, -1, 1, 2]
targetSum = 16


def fourNumberSum(array, targetSum):
    # Write your code here.
    out = fourNumberSumHelper(array, targetSum, [])
    return out


# time: O(n^4)
def fourNumberSumHelper(array, targetSum, out, currArray=[], idx=0):
    if len(array) < 4 or idx > len(array) - 1:
        return out

    while idx < len(array):
        currArray.append(array[idx])
        if len(currArray) == 4:
            if sum(currArray) == targetSum:
                out.append(currArray.copy())
        else:
            out = fourNumberSumHelper(array, targetSum, out, currArray, idx + 1)
        currArray.pop(-1)
        idx += 1
    return out


print(fourNumberSum(array, targetSum))

"""
Input:
[7, 6, 4, -1, 1, 2]
16

Output:
[[7,6,4,-1], [7,6,1,2]]
"""
