array = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
array2 = [-10, -2, -9, -4, -8, -6, -7, -1, -3, -5]
array3 = [-1000, -1000, 2, 4, -5, -6, -7, -8, -2, -100]
array4 = [-2, -1]
array5 = [-1000, 50, -1000, 10, 10, 10, 10, 10, 10]


# O(n^2) time | O(n) space
def kadanesAlgorithm(array):
    """Function takes in a non-empty array of integers and returns the maximum
    sum that can be obtained by summing up all of the integers in a non-empty subarray.
    The subarray must only contain adjacent numbers."""
    sums = [array[0]]
    for idx in range(1, len(array)):
        sums.append(sums[idx - 1] + array[idx])
    maxSum = max(sums)
    while len(sums) > 1:
        for idx in range(1, len(sums) + 1):
            sums[-idx] = sums[-idx] - sums[0]
        sums.remove(sums[0])
        maxSum = max(max(sums), maxSum)
    return maxSum


result = kadanesAlgorithm(array5)
print(result)
"""
-1000,50,-1000,10,10,10,10,10,10
[-1000,-950,-1950,-1940,-1930,-1920,-1910,-1900,-1890] -> max: -950
arr[-i] = arr[-i] - arr[0]
[0,50,-950,-940,-930,-920,-910,-900,-890]
arr.remove(arr[0])
[50,-950,-940,-930,-920,-910,-900,-890] -> max: 50

[-1000,-990,-980,-970,-960,-950,-940] -> max: 50
[10,20,30,40,50,60] -> max: 60
[10,20,30,40,50] -> max: 60
[10,20,30,40] -> max: 60
[10,20,30] -> max: 60
[10,20] -> max: 60
[10] -> max: 60
[]
"""
