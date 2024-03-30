array = [75, 105, 120, 75, 90, 135]


# O(n) time | O(n) space
def maxSubsetSumNoAdjacent(array):
    """Function take sin an array of positive integers and returns the maximum sum
    of non-adjacent elements in the array."""
    out = []
    for idx in range(len(array)):
        if idx == 0:
            out.append(array[idx])
        elif idx == 1:
            out.append(max(out[idx - 1], array[idx]))
        else:
            out.append(max(out[idx - 1], out[idx - 2] + array[idx]))
    if len(out) == 0:
        return 0
    return out[-1]


result = maxSubsetSumNoAdjacent(array)
print(result)
