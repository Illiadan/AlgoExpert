array = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
array2 = [-10, -2, -9, -4, -8, -6, -7, -1, -3, -5]
array3 = [-1000, -1000, 2, 4, -5, -6, -7, -8, -2, -100]
array4 = [-2, -1]
array5 = [-1000, 50, -1000, 10, 10, 10, 10, 10, 10]


# O(n) time | O(1) space
def kadanesAlgorithm(array):
    """Function takes in a non-empty array of integers and returns the maximum
    sum that can be obtained by summing up all of the integers in a non-empty subarray.
    The subarray must only contain adjacent numbers."""
    maxSum = float("-inf")
    currSum = float("-inf")
    for i in array:
        currSum = max(currSum + i, i)
        maxSum = max(maxSum, currSum)
    return maxSum


result = kadanesAlgorithm(array5)
print(result)
"""
3,8,-1,1,4,2,5,9,16,18,9,15,18,19,14,18
-1000,50,-950,10,20,30,40,50,60
"""
