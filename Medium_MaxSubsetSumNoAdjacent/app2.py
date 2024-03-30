array = [75, 105, 120, 75, 90, 135]


# O(n) time | O(1) space
def maxSubsetSumNoAdjacent(array):
    """Function take sin an array of positive integers and returns the maximum sum
    of non-adjacent elements in the array."""
    if len(array) == 0:
        return 0
    if len(array) == 1:
        return array[0]
    secondPredecessor = array[0]
    firstPredecessor = max(secondPredecessor, array[1])
    for idx in range(2, len(array)):
        current = max(firstPredecessor, secondPredecessor + array[idx])
        secondPredecessor = firstPredecessor
        firstPredecessor = current
    return firstPredecessor


result = maxSubsetSumNoAdjacent(array)
print(result)
